# crypto-paper-writing

This repository is a reusable **paper-writing toolkit**, not a paper or research
project. Work on the toolkit follows `SPEC.md`. A paper project installed with
`./install.sh` keeps its own drafts, results, notes, and reviews.

For a paper project, read `STATE.md` and the relevant source ledgers first. The
author decides the scope and claims. Use `CLAIMS.md` for the exact supported
wording, `EVIDENCE.md` for reported numbers, and `LITERATURE.md` plus verified
`refs.bib` for citations. Do not turn a successful build into a correctness claim.
Treat theory, experiment, and prose as distinct sources of support.

Codex workflows and supporting procedures live in `skills/<name>/SKILL.md`.
The installer exposes them through the paper project's `.agents/skills/`.
The seven `cpw-*` skills provide task entrypoints; they execute within the current
Codex task and do not define separate agents. Nothing is submitted, e-mailed,
uploaded, or made public without explicit human approval.

When working on this toolkit, use only synthetic examples and public sources.
Never add unpublished drafts, private reviews, real benchmark logs, server names,
or harvested paper figures. Run `scripts/privacy_scan.sh` with a local ignored
`.privacy-denylist` before pushing changes.
