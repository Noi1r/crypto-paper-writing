---
name: cpw-write
description: Plan, draft, revise, polish, or translate cryptography and security manuscripts, from a single passage to a full-paper outline. Use as the single CPW writing entrypoint; read its internal guides for the requested task. Not for toolkit maintenance or independent research execution.
---

# CPW manuscript writing

Use this entrypoint for all manuscript writing tasks. Load only the internal
guide needed for the author's current request and stay within the agreed scope.
These guides are reference documents for the current session; they do not
spawn separate skill calls or subagents.

## Start from the requested work

Identify the target passage or section, its job in the paper, its intended
reader, and its surrounding dependencies. Preserve any clear structure and
established terminology the author already uses. Read enough surrounding context
to see what the reader already knows entering the passage and what the passage
must establish for later sections. Reuse prior writing decisions and source
checks whenever their inputs have not changed.

Work directly from the manuscript, author-provided text, bibliography, and
supporting notes. When present, read `STATE.md` for file paths and the writing
plan, `CLAIMS.md` for exact supported claim wording, `EVIDENCE.md` for numerical
provenance, and `LITERATURE.md` for prior-work comparisons. A local edit or
polishing task can proceed directly from the manuscript and existing notes—do
not initialize project ledgers, run a fresh literature search, or build a
style profile just to revise a passage.

For a new paper or major reorganization, establish the actual technical results
first, study suitable reference papers, and propose an outline tailored to the
work. Record the plan in `STATE.md` or existing project notes. Keep technical
proximity (closest prior art) distinct from rhetorical usefulness (well-written
exemplar papers). When drafting new prose from raw notes, proofs, or benchmark
records, use [drafting from research materials](references/drafting-from-materials.md)
to build the core argument, explanation order, and complete draft text.

## Read only the guidance needed now

Resolve links relative to this skill directory, following its symlink if needed.
Read the guide matching the current task; follow cross-links only when a
concrete decision requires them. Never preload every section guide for a local edit.

| Requested work | Internal guide |
|---|---|
| Paragraph or section polishing, translation, iterative revision | [Collaborative polishing](references/collaborative-polishing.md) |
| A batch of proposed revisions for asynchronous review | [Paragraph comparison booklets](references/review-comparison.md) |
| New paper or substantial reorganization | [Writing from relevant papers](references/writing-from-related-work.md), then [overall structure](references/sections/00_overall_structure.md) |
| First manuscript draft or a new section from notes and results | [Drafting from materials](references/drafting-from-materials.md), with the relevant chapter guide below |
| Title | [Title](references/sections/01_title.md) |
| Abstract | [Abstract](references/sections/02_abstract.md) |
| Introduction or contributions | [Introduction](references/sections/03_introduction.md) and, when needed, [contributions](references/sections/04_contributions.md) |
| Technical overview | [Technical overview](references/sections/05_technique_overview.md) |
| Related-work prose | [Related work](references/sections/06_related_work.md) |
| Background and notation | [Preliminaries](references/sections/07_preliminaries.md) |
| Construction, protocol, or algorithm exposition | [Main technical content](references/sections/08_main_construction.md) |
| Presentation of security, correctness, or analysis | [Security and correctness](references/sections/09_security_correctness.md) |
| Evaluation, including analytical cost comparisons | [Evaluation](references/sections/10_experiments.md) |
| Conclusion or appendix | [Conclusion](references/sections/11_conclusion.md) or [appendix](references/sections/12_appendix.md) |
| Deriving a personal style profile, when explicitly requested | [Author style](references/author-style.md) |

When diagnosing awkward phrasing, dense nominalizations, or unclear terminology,
read [field language and clarity](references/field-language-and-clarity.md).
[Synthetic revision examples](examples/revision-decisions.md) illustrate structural
and attribution choices; treat them as decision patterns, not sentence templates.

## Shared writing decisions

- **Fix structure before surface wording.** Give every paragraph one clear job
  in the argument. Resolve misplaced premises, missing logical steps, and
  duplicated explanations before tuning individual words. Choose sentence and
  paragraph boundaries to clarify the reasoning; shorter text is only better
  when it keeps the necessary motivation, conditions, and causal links intact.
- **Evaluate flow in context (Given-before-New).** Judge a passage by what the
  reader has already seen at that point in the manuscript. A body section can
  rely on earlier overviews, definitions, and notation without re-teaching them;
  add only the local reminders and transitions needed here. Within sentences and
  paragraphs, lead with familiar context or previously introduced objects and
  place the new technical observation, constraint, or result at the end. When a
  deliverable must stand alone (such as an abstract), make its context self-contained.
- **Pair exact domain terms with plain action verbs.** Use the subfield's
  established names consistently—never swap synonyms for a defined technical
  object (`witness`, `commitment`, `oracle`, `simulator`, `distinguisher`). Around
  those technical nouns, use direct verbs (`computes`, `sends`, `checks`, `bounds`,
  `reduces`, `interpolates`) instead of abstract noun chains or empty intensifiers.
  Integrate math cleanly into English grammar: pair new symbols with a descriptive
  noun on first mention (for example, "the ring dimension $d$") and never start a
  sentence with a bare symbol.
- **Never strengthen a claim through editorial polish.** Preserve all assumptions,
  quantifiers, adversarial capabilities, probability spaces, security models, and
  comparison regimes. Keep language improvements strictly separate from technical
  corrections; fluent prose cannot supply a missing reduction step, causal link,
  or novelty claim.
- **Keep evidence categories distinct.** Clearly distinguish proved theorems,
  analytical cost models, manuscript derivations, local benchmark measurements,
  numbers quoted from prior papers, and heuristic estimates. Cite the primary
  source that establishes each fact: cite a standard for normative parameters or
  definitions, and cite the specific analysis or implementation paper for its
  bounds or timings.
- **Keep every number traceable.** Trace modified numerical claims to their
  underlying logs, tables, or calculations. Update `EVIDENCE.md` and `\ev{...}`
  links when the project uses them; otherwise rely on existing source records.
  Flag any missing data or citation explicitly rather than inserting a placeholder
  number or an unverified reference.

## Deliver and check

After a review or a batch of multi-passage edits, offer a
[comparison booklet](references/review-comparison.md) once if asynchronous side-by-side
review would help the author; do not make it a prerequisite for normal editing.

When revising, return the complete revised passage along with a brief summary of
substantive changes unless the author asks for line notes or discussion only.
If a passage already works well, say so and leave it untouched. Keep citation
keys, `\label`/`\ref` targets, LaTeX macros, and revision-tracking markup intact
unless authorized to change them. Discussing candidate wording in chat does not
authorize editing manuscript files on disk; edit source files only when requested.

When the author changes a section's framing or emphasis, rebuild the passage
around the new goal rather than patching isolated sentences, and check any
downstream sections, notation, citations, or numbers affected by the shift.
Run LaTeX builds or evidence audits when warranted and available, reporting only
the checks actually executed.
