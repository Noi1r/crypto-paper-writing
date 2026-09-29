# crypto-paper-writing

This repository is a reusable **paper-writing toolkit**, not a paper or research
project. Work on the toolkit follows `SPEC.md`. A paper project installed with
`./install.sh` keeps its own drafts, results, notes, and reviews.

For a paper project, use `STATE.md` and relevant source records when present.
The author decides the scope and claims. Local writing can use the current
manuscript and existing support without initializing a record system. Use
`CLAIMS.md`, `EVIDENCE.md` and `LITERATURE.md` when the project maintains them.
Do not turn a successful build into a correctness claim. Treat theory,
experiment, and prose as distinct sources of support.

Codex workflows and tools live in `skills/<name>/SKILL.md`. The installer
exposes them through the paper project's `.agents/skills/`. The seven `cpw-*`
skills provide task entrypoints. Article writing uses `cpw-write`; its internal
guides in `skills/cpw-write/references/` are read as needed and are not separately
registered skills. These workflows execute within the current Codex task and
do not define separate agents. Nothing is submitted, e-mailed, uploaded, or made
public without explicit human approval.

When working on this toolkit, use only synthetic examples and public sources.
Never add unpublished drafts, private reviews, real benchmark logs, server names,
or harvested paper figures. Run `scripts/privacy_scan.sh` with a local ignored
`.privacy-denylist` before pushing changes.
