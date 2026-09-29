# Paper project guidance

This directory is a paper project using `crypto-paper-writing`. Read
`STATE.md` before editing. Use `CLAIMS.md` for exact supported claim wording,
`EVIDENCE.md` for measured numbers, `LITERATURE.md` and verified `paper/refs.bib`
for citations, and `SUBMISSION.md` for current venue rules. If a claim lacks
support, state the gap and help resolve it before presenting it as fact.

Paths in the installed skills are relative to this project root;
toolkit resources use `.paper-writing/skills/`, `.paper-writing/templates/`, etc.
The default manuscript is `paper/main.tex` and its bibliography is
`paper/refs.bib`. For an existing manuscript, record its actual source,
bibliography, and build command in `STATE.md` and use those paths consistently.

For a new paper or major reorganization, first establish its actual results and
study relevant papers using
`.paper-writing/skills/paper-playbook/references/writing-from-related-work.md`.
Then adapt the whole-paper outline to the work, recording or linking the selected
references, structural choices and exposition plan in `STATE.md`.
Local edits reuse this plan and preserve the author's clear existing structure
and conventions. A personal `STYLE.md` is optional and created only on request.
Presentation choices must preserve technical meaning and evidence status.

Use terminology familiar to the relevant subfield and keep the same name for
the same technical object. Use ordinary, concrete prose around it and explain
necessary connections between steps. Apply
`.paper-writing/skills/polish-writing/SKILL.md` during drafting and revision for
natural language and readability without weakening the technical statement.

The installed writing toolkit is under `.paper-writing/`. Codex discovers its
skills through `.agents/skills/`; use `cpw-init`, `cpw-lit`, `cpw-write`,
`cpw-figure`, `cpw-review`, `cpw-rebuttal` or `cpw-submit` for the corresponding
task. These are workflows within the current Codex task; separate agents are
optional and require the author's request. Keep unpublished drafts, reviews, logs, and private
correspondence in this project. Do not submit or publish without the author's
explicit approval.
