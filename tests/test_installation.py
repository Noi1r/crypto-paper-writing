"""Install the toolkit only into temporary synthetic paper projects."""
import subprocess
import tempfile
import unittest
from pathlib import Path

from papercheck.evidence import append_row

ROOT = Path(__file__).resolve().parents[1]
WRITING_GUIDES = {
    "paper-playbook", "polish-writing", "abstract-craft", "technique-overview",
    "related-work-writing", "experiments-writing",
}


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "toy paper"
        self.project.mkdir()

    def install(self):
        return subprocess.run(["bash", str(ROOT / "install.sh"), str(self.project)],
                              capture_output=True, text=True, check=True)

    def audit(self):
        return subprocess.run(["make", "-C", str(self.project / "paper"), "audit"],
                              capture_output=True, text=True)

    def test_installed_audit_with_colliding_project_directories(self):
        for name in ("scripts", "skills", "figures", "templates", "references", "agents", "papercheck"):
            directory = self.project / name
            directory.mkdir()
            (directory / "keep.txt").write_text("project-owned\n")
        (self.project / "AGENTS.md").write_text("existing guidance\n")
        self.install()
        for name in ("scripts", "skills", "figures", "templates", "references", "agents", "papercheck"):
            self.assertEqual((self.project / name / "keep.txt").read_text(), "project-owned\n")
            self.assertEqual(len(list((self.project / name).iterdir())), 1)
        self.assertEqual((self.project / "AGENTS.md").read_text(), "existing guidance\n")
        expected = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        links = list((self.project / ".agents/skills").iterdir())
        self.assertEqual({p.name for p in links}, expected)
        self.assertFalse(expected & WRITING_GUIDES)
        writing = self.project / ".agents/skills/cpw-write"
        self.assertEqual(list(writing.rglob("SKILL.md")), [writing / "SKILL.md"])
        for guide in ("collaborative-polishing.md", "sections/02_abstract.md",
                      "sections/05_technique_overview.md", "sections/10_experiments.md"):
            self.assertTrue((writing / "references" / guide).is_file(), guide)
        for link in links:
            self.assertTrue(link.is_symlink(), str(link))
            self.assertTrue((link / "SKILL.md").is_file(), str(link))
            self.assertEqual(link.resolve(), (self.project / ".paper-writing/skills" / link.name).resolve())
        self.assertFalse((self.project / ".claude").exists())
        self.assertFalse((self.project / ".paper-writing/agents").exists())
        self.assertFalse((self.project / ".paper-writing/commands").exists())
        self.assertTrue((self.project / ".paper-writing/LICENSE").is_file())
        self.assertTrue((self.project / ".paper-writing/.gitignore").is_file())
        self.assertTrue((self.project / "paper/refs.bib").is_file())
        self.assertFalse((self.project / "refs.bib").exists())
        (self.project / "result.log").write_text("1.23 s\n")
        append_row(str(self.project / "EVIDENCE.md"), "1.23 s", "python3 toy.py", "result.log",
                   "toy-commit", "toy-machine", "2026-01-01", "5 / median")
        (self.project / "paper/main.tex").write_text("\\begin{document}\n\\input{tables/toy}\n\\end{document}\n")
        tables = self.project / "paper/tables"
        tables.mkdir()
        result_file = tables / "toy.tex"
        result_file.write_text("Time: 1.23 s\\ev{E1}.\n")
        result = self.audit()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result_file.write_text("Time: 9.99 s\\ev{E1}.\n")
        result = self.audit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("mismatch", result.stdout)
        self.assertIn("toy.tex", result.stdout)
        # Reinstalling preserves paper edits and edits to the installed snapshot.
        role = self.project / ".paper-writing/skills/cpw-write/SKILL.md"
        role.write_text("local skill customization\n")
        self.install()
        self.assertEqual(role.read_text(), "local skill customization\n")
        self.assertIn("9.99", result_file.read_text())

    def test_existing_manuscript_and_dangling_project_links_are_preserved(self):
        (self.project / "paper").mkdir()
        (self.project / "paper/main.tex").write_text("existing manuscript\n")
        (self.project / "STATE.md").symlink_to("state-written-elsewhere.md")
        self.install()
        self.assertEqual((self.project / "paper/main.tex").read_text(), "existing manuscript\n")
        self.assertFalse((self.project / "paper/Makefile").exists())
        self.assertTrue((self.project / "STATE.md").is_symlink())
        self.assertFalse((self.project / "state-written-elsewhere.md").exists())
        self.assertFalse((self.project / "scripts").exists())

    def test_existing_codex_skill_is_preserved_and_reported(self):
        custom = self.project / ".agents/skills/cpw-write"
        custom.mkdir(parents=True)
        (custom / "SKILL.md").write_text("project-specific writing skill\n")
        result = self.install()
        self.assertFalse(custom.is_symlink())
        self.assertEqual((custom / "SKILL.md").read_text(), "project-specific writing skill\n")
        self.assertIn("Kept existing Codex skill:", result.stdout)
        self.assertIn(".agents/skills/cpw-write", result.stdout)

    def test_user_install_registers_skills_without_creating_a_paper(self):
        target = Path(self.temp.name) / "user skills"
        for _ in range(2):
            subprocess.run(["bash", str(ROOT / "install.sh"), "--user", str(target)],
                           capture_output=True, text=True, check=True)
        expected = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        self.assertEqual({p.name for p in target.iterdir()}, expected)
        init_skill = target / "cpw-init/SKILL.md"
        self.assertEqual(init_skill.resolve().parents[2], ROOT)
        self.assertTrue((init_skill.resolve().parents[2] / "install.sh").is_file())
        for path in target.iterdir():
            self.assertTrue(path.is_symlink())
            self.assertEqual(path.resolve(), ROOT / "skills" / path.name)
        self.assertFalse((target.parent / "paper").exists())
        self.assertFalse((target / "STATE.md").exists())

    def test_user_install_preserves_existing_skill(self):
        target = Path(self.temp.name) / "user skills"
        existing = target / "cpw-write"
        existing.mkdir(parents=True)
        (existing / "SKILL.md").write_text("user-owned skill\n")
        result = subprocess.run(["bash", str(ROOT / "install.sh"), "--user", str(target)],
                                capture_output=True, text=True, check=True)
        self.assertEqual((existing / "SKILL.md").read_text(), "user-owned skill\n")
        self.assertIn("Kept existing Codex skill:", result.stdout)
        self.assertTrue((target / "cpw-init/SKILL.md").is_file())

    def test_old_registration_migrates_without_losing_customizations(self):
        old_skill = self.project / ".paper-writing/skills/paper-playbook"
        old_skill.mkdir(parents=True)
        original = "---\nname: paper-playbook\ndescription: Local writing guidance\n---\n\nLocal edit.\n"
        (old_skill / "SKILL.md").write_text(original)
        for kind, name in (("agents", "writer.md"), ("commands", "cpw-write.md"), ("skills", "paper-playbook")):
            folder = self.project / ".claude" / kind
            folder.mkdir(parents=True, exist_ok=True)
            (folder / name).symlink_to(f"../../.paper-writing/{kind}/{name}")
        custom = self.project / ".claude/commands/local.md"
        custom.write_text("custom entry\n")
        settings = self.project / ".claude/settings.json"
        settings.write_text('{"toy": true}\n')
        foreign = self.project / ".claude/skills/local"
        foreign.symlink_to("../../../custom-skills/local")
        self.install()
        self.assertFalse((self.project / ".claude/agents/writer.md").is_symlink())
        self.assertFalse((self.project / ".claude/commands/cpw-write.md").is_symlink())
        self.assertFalse((self.project / ".claude/skills/paper-playbook").is_symlink())
        self.assertEqual(custom.read_text(), "custom entry\n")
        self.assertEqual(settings.read_text(), '{"toy": true}\n')
        self.assertTrue(foreign.is_symlink())
        self.assertEqual((old_skill / "SKILL.md").read_text(), original)
        self.assertTrue((self.project / ".paper-writing/skills/cpw-write/references/writing-from-related-work.md").is_file())
        self.assertFalse((self.project / ".agents/skills/paper-playbook").is_symlink())
        self.assertTrue((self.project / ".agents/skills/cpw-write/SKILL.md").is_file())

    def test_old_writing_links_retire_without_removing_project_content(self):
        registration = self.project / ".agents/skills"
        registration.mkdir(parents=True)
        for name in WRITING_GUIDES:
            old = self.project / ".paper-writing/skills" / name
            old.mkdir(parents=True)
            (old / "SKILL.md").write_text("customized old guide: " + name)
            (registration / name).symlink_to("../../.paper-writing/skills/" + name)
        for _ in range(2):
            self.install()
            for name in WRITING_GUIDES:
                self.assertFalse((registration / name).is_symlink())
                self.assertFalse((registration / name).exists())
                old = self.project / ".paper-writing/skills" / name / "SKILL.md"
                self.assertEqual(old.read_text(), "customized old guide: " + name)
        self.assertTrue((registration / "cpw-write/references/collaborative-polishing.md").is_file())

    def test_user_writing_migration_preserves_foreign_entries(self):
        target = Path(self.temp.name) / "user skills"
        target.mkdir()
        managed = target / "abstract-craft"
        managed.symlink_to(ROOT / "skills/abstract-craft")
        foreign = target / "polish-writing"
        foreign.symlink_to(Path(self.temp.name) / "another toolkit/polish-writing")
        custom = target / "technique-overview"
        custom.mkdir()
        (custom / "SKILL.md").write_text("user-owned overview guidance")
        for _ in range(2):
            subprocess.run(["bash", str(ROOT / "install.sh"), "--user", str(target)],
                           capture_output=True, text=True, check=True)
            self.assertFalse(managed.is_symlink())
            self.assertTrue(foreign.is_symlink())
            self.assertEqual((custom / "SKILL.md").read_text(), "user-owned overview guidance")
        self.assertTrue((target / "cpw-write/references/sections/02_abstract.md").is_file())

    def test_legacy_config_directory_symlink_is_not_followed(self):
        external = Path(self.temp.name) / "external config"
        (external / "agents").mkdir(parents=True)
        legacy = external / "agents/writer.md"
        legacy.symlink_to("../../.paper-writing/agents/writer.md")
        (self.project / ".claude").symlink_to(external, target_is_directory=True)
        self.install()
        self.assertTrue(legacy.is_symlink())
        self.assertTrue((self.project / ".agents/skills/cpw-write/SKILL.md").is_file())

    def test_registration_root_symlink_does_not_write_elsewhere(self):
        external = Path(self.temp.name) / "external registration"
        external.mkdir()
        (self.project / ".agents").symlink_to(external, target_is_directory=True)
        result = subprocess.run(["bash", str(ROOT / "install.sh"), str(self.project)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(list(external.iterdir()), [])
        self.assertFalse((self.project / ".paper-writing").exists())


if __name__ == "__main__":
    unittest.main()
