# Paper project guidance

This directory is a paper project using `crypto-paper-writing`. Use
`STATE.md` and relevant support records when present: `CLAIMS.md` for supported
claim wording, `EVIDENCE.md` for reported numbers, `LITERATURE.md` and the
bibliography for citations, and `SUBMISSION.md` for venue rules. Local writing
can use existing manuscript sources and support without creating these records.
If a claim lacks support, state the gap before presenting it as fact.

Manuscript paths are relative to this project root. Markdown links inside a
skill are relative to that skill file; toolkit resources otherwise use
`.paper-writing/skills/`, `.paper-writing/templates/`, etc.
The default manuscript is `paper/main.tex` and its bibliography is
`paper/refs.bib`. For an existing manuscript, record its actual source,
bibliography, and build command in `STATE.md` and use those paths consistently.

For a new paper or major reorganization, first establish its actual results and
study relevant papers using
`.paper-writing/skills/cpw-write/references/writing-from-related-work.md`.
Then adapt the whole-paper outline to the work, recording or linking the selected
references, structural choices and exposition plan in `STATE.md`.
Local edits reuse this plan and preserve the author's clear existing structure
and conventions. A personal `STYLE.md` is optional and created only on request.
Presentation choices must preserve technical meaning and evidence status.

Use terminology familiar to the relevant subfield and keep the same name for
the same technical object. Use ordinary, concrete prose around it and explain
necessary connections between steps. Apply
`.paper-writing/skills/cpw-write/references/collaborative-polishing.md` during drafting and revision for
natural language and readability without weakening the technical statement.

Article writing uses `cpw-write`, with internal guides read as needed for
polishing, abstracts, technical exposition, evaluation and other sections.
The installed writing toolkit is under `.paper-writing/`. Codex discovers its
skills through `.agents/skills/`; use `cpw-init`, `cpw-lit`, `cpw-write`,
`cpw-figure`, `cpw-review`, `cpw-rebuttal` or `cpw-submit` for the corresponding
task. These are workflows within the current Codex task; separate agents are
optional and require the author's request. Keep unpublished drafts, reviews, logs, and private
correspondence in this project. Do not submit or publish without the author's
explicit approval.
