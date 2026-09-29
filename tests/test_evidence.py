"""Synthetic regressions for evidence links, ledger errors and source coverage."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from papercheck import evidence

ROOT = Path(__file__).resolve().parents[1]


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.tex = self.root / "main.tex"
        self.ledger = self.root / "EVIDENCE.md"
        (self.root / "result.log").write_text("toy runtime: 1.23 s\n")
        evidence.append_row(str(self.ledger), "1.23 s", "python3 toy.py", "result.log",
                            "toy-commit", "toy-machine", "2026-01-01", "5 / median")
        self.rows = evidence.read_ledger(str(self.ledger))

    def audit(self, source, **kwargs):
        self.tex.write_text(source)
        return evidence.audit_tex(str(self.tex), self.rows, **kwargs)

    def cli(self):
        return subprocess.run([sys.executable, str(ROOT / "scripts/audit_tex.py"),
                               str(self.tex), str(self.ledger)], capture_output=True, text=True)

    def test_supported_tag_spellings_and_comments(self):
        for source in (r"Time: 1.230 s\ev{E1}.", r"Time: 1.23 s\evid{E1}.",
                       r"Time: 1.23\,\mathrm{s}. % EV:E1"):
            with self.subTest(source=source):
                self.assertEqual(self.audit(source), [])

    def test_numeric_coincidence_is_not_a_link(self):
        issues = self.audit("Time: 1.23 s.\nMemory: 1.23 GB.")
        self.assertEqual([i.kind for i in issues], ["unlinked", "unlinked"])

    def test_unknown_ids_in_all_supported_syntaxes(self):
        for source in (r"1.23 s\ev{E999}", r"1.23 s\evid{E999}", "1.23 s % EV:E999"):
            with self.subTest(source=source):
                self.assertIn("unknown-id", {i.kind for i in self.audit(source)})

    def test_wrong_value_unit_and_scale(self):
        for source in (r"9.99 s\ev{E1}", r"1.23 GB\ev{E1}", r"1.23 ms\ev{E1}"):
            with self.subTest(source=source):
                self.assertIn("mismatch", {i.kind for i in self.audit(source)})

    def test_multiple_values_need_their_own_links(self):
        issues = self.audit(r"Time 1.23 s\ev{E1}, memory 1.23 GB.")
        self.assertEqual([i.kind for i in issues], ["unlinked"])
        self.assertIn("orphan-tag", {i.kind for i in self.audit(r"Time \runtime\ev{E1}.")})

    def test_scientific_notation_and_exact_decimal_comparison(self):
        self.rows[0]["printed"] = "0.00123 s"
        for source in (r"Time: 1.23e-3 s\ev{E1}.", r"Time: 1.23\times 10^{-3}\,s\ev{E1}."):
            with self.subTest(source=source):
                self.assertEqual(self.audit(source), [])
        self.rows[0]["printed"] = "123456789012345678901234567890 bytes"
        self.assertIn("mismatch", {i.kind for i in self.audit(
            r"123456789012345678901234567891 bytes\ev{E1}")})

    def test_ranges_are_not_negative_quantities(self):
        self.rows[0]["printed"] = "2.1 s to 3.4 s"
        self.assertEqual(self.audit(r"Time: 2.1--3.4 s. % EV:E1"), [])
        self.rows[0]["printed"] = "-3.4 s"
        self.assertEqual(self.audit(r"Time: -3.4 s\ev{E1}."), [])

    def test_bare_integer_tables_and_explicit_integer_tags(self):
        self.rows[0]["printed"] = "256 bytes"
        self.assertEqual(self.audit(r"There are 256\ev{E1} entries."), [])
        issues = self.audit("\\begin{tabular}{lr}\nToy & 999 \\\\\n\\end{tabular}")
        self.assertIn("unlinked", {i.kind for i in issues})

    def test_recursive_tables_and_preamble(self):
        (self.root / "sections").mkdir()
        (self.root / "tables").mkdir()
        (self.root / "tables/result.tex").write_text("Toy & 1.23 \\\\ % EV:E1\n")
        (self.root / "sections/results.tex").write_text(
            "\\begin{tabular}{lr}\n\\input{tables/result}\n\\end{tabular}\n")
        source = "\\newcommand{\\size}{0.8}\n\\begin{document}\n\\input{sections/results}\n\\end{document}"
        self.assertEqual(self.audit(source), [])
        (self.root / "tables/result.tex").write_text("Toy & 999 \\\\\n")
        issues = self.audit(source)
        self.assertEqual([i.kind for i in issues], ["unlinked"])
        self.assertEqual(Path(issues[0].path).name, "result.tex")
        self.assertEqual(self.audit(source, recursive=False), [])

    def test_missing_dynamic_and_cyclic_inputs(self):
        self.assertIn("missing-input", {i.kind for i in self.audit(r"\input{absent}")})
        self.assertIn("unresolved-input", {i.kind for i in self.audit(r"\input{\tablepath}")})
        self.assertIn("include-cycle", {i.kind for i in self.audit(r"\input{main}")})

    def test_document_markers_do_not_hide_same_line_results(self):
        self.assertIn("unlinked", {i.kind for i in self.audit(
            r"\begin{document}Time: 9.99 s.\end{document}")})

    def test_comments_and_ignore_blocks(self):
        self.assertEqual(self.audit("% Time: 9.99 s\\ev{E999}\n"), [])
        self.assertEqual(self.audit("0.8 % papercheck:ignore (layout)\n"), [])
        self.assertIn("unlinked", {i.kind for i in self.audit("Time: 9.99 s. papercheck:ignore")})
        self.assertIn("ignore-block", {i.kind for i in self.audit("% papercheck:ignore-begin (layout)")})

    def test_ledger_and_log_validation_are_on_by_default(self):
        self.tex.write_text(r"Time: 1.23 s\ev{E1}.")
        self.assertEqual(self.cli().returncode, 0)
        (self.root / "result.log").unlink()
        result = self.cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn("log-not-found", result.stdout)
        self.ledger.unlink()
        self.assertEqual(self.cli().returncode, 2)

    def test_malformed_ledger_is_not_an_empty_ledger(self):
        for text in ("# EVIDENCE\n", "| ID | value |\n|---|---|\n| E1 | 1.23 s |\n"):
            self.ledger.write_text(text)
            with self.assertRaises(ValueError):
                evidence.read_ledger(str(self.ledger))

    def test_duplicate_and_derived_references(self):
        self.assertIn("duplicate-id", {i.kind for i in evidence.validate_ledger(self.rows * 2)})
        evidence.append_row(str(self.ledger), "2.00×", "derived: E2/E1", "-")
        rows = evidence.read_ledger(str(self.ledger))
        self.assertIn("derivation-cycle", {i.kind for i in evidence.validate_ledger(rows)})
        rows[-1]["command"] = "derived: E9/E1"
        self.assertIn("bad-derivation", {i.kind for i in evidence.validate_ledger(rows)})

    def test_empty_template_ledger_accepts_first_row(self):
        self.ledger.write_text((ROOT / "templates/blackboard/EVIDENCE.md").read_text())
        self.assertEqual(evidence.read_ledger(str(self.ledger)), [])
        self.assertEqual(evidence.append_row(str(self.ledger), "1.23 s", "toy", "result.log"), "E1")
        self.assertEqual(len(evidence.read_ledger(str(self.ledger))), 1)


if __name__ == "__main__":
    unittest.main()
