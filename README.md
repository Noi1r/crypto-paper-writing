# crypto-paper-writing

A standalone writing toolkit for cryptography and security papers, extracted from
[`crypto-research-agents`](https://github.com/acprk/crypto-research-agents).
It covers literature and citation checks, manuscript drafting, figures, review,
rebuttal, anonymity, and final source/PDF checks. It does not include the original
research-phase orchestrator, toy cryptography library, or benchmark runner.

## Start a paper

```bash
./install.sh /path/to/my-paper
```

The installer adds an LNCS paper skeleton and empty working ledgers to the target
project. It also puts five writing roles, 18 skills, and seven `/cpw-*` prompts in
`.claude/`, with the reusable assets under `.paper-writing/`. Existing project files
are left alone. The source of truth stays in the paper project; this repository
contains templates and synthetic examples only.

With Claude Code, use `/cpw-lit`, `/cpw-write`, `/cpw-figure`, `/cpw-review`,
`/cpw-rebuttal`, and `/cpw-submit`. With Codex or another agent, read the matching
file in `agents/` or `skills/` and follow its procedure. The commands are prompt
definitions, not a separate executable.

## What is included

| Path | Purpose |
|---|---|
| `agents/` | Literature, writing, figures, simulated review, and submission/rebuttal roles |
| `skills/` | Section playbook, literature and bibliography checks, figures, review, rebuttal, anonymity, and camera-ready procedures |
| `templates/` | LNCS LaTeX skeleton, working ledgers, rebuttal and handoff templates |
| `figures/` | Synthetic chart/TikZ templates, styles, and a local-only figure harvester |
| `references/reading-lists/` | Public starting points for literature searches |
| `papercheck/`, `scripts/audit_tex.py` | Standalone evidence-ledger and LaTeX-number audit; no benchmark-runner dependency |
| `docs/zh/writing-playbook.md` | Chinese writing guide |

## Working contract

1. Record claims and their support in `CLAIMS.md`; use the supported wording in the paper.
2. Put every reported measurement in `EVIDENCE.md`, with the originating log and configuration. Run `make audit` from `paper/` before using a number in the manuscript.
3. Verify every BibTeX entry. For IACR ePrint, use its canonical page for metadata; inspect the paper itself for technical claims and exact notation.
4. Check the current venue call for papers before applying any page-limit or submission advice in the skills.
5. Keep drafts, review text, logs, private PDF corpora, and harvested figures in the private paper project. Do not add them to this toolkit. Ask the human author before any submission or public release.

The LaTeX skeleton uses Springer LNCS. Other venues can reuse its section files and
writing procedures with the venue's current class/template. Local compilation needs
`latexmk`; figure rendering needs Python 3.10+, NumPy, and Matplotlib. The audit
script itself uses only Python's standard library.

Run `python3 scripts/audit_tex.py --selftest` for the number auditor. See
[`SOURCE.md`](SOURCE.md) for the extraction boundary and provenance.

## License

MIT; attribution is retained in `LICENSE`.
