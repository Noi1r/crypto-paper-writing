---
name: cpw-write
description: Plan, draft, revise, polish, or translate cryptography and security manuscripts, from a paragraph to a whole-paper structure. Use as the single CPW writing entrypoint; read its internal guides for the requested task. Not for toolkit maintenance or independent research execution.
---

# CPW manuscript writing

Use this entrypoint for article writing. Select the relevant internal guide below
and work within the author's requested scope. These guides are resources for the
current assistant; they do not require separate skill calls or agents.

## Start from the requested work

Identify the requested unit, its purpose, intended reader and surrounding
dependencies. Preserve a clear author structure and established terminology.
Read enough context to understand what has been established and what comes next.
Reuse decisions and source checks already made when their inputs have not changed.

Use the manuscript, author-provided passages, bibliography and relevant support.
If present, use `STATE.md` for actual paths and the writing plan, `CLAIMS.md`
for supported wording, `EVIDENCE.md` for numerical sources, and `LITERATURE.md`
for related work. A local edit can proceed from existing material without these
records, a toolkit installation or a personal style profile. Do not initialize
records or start a new literature search merely to polish a passage.

For a new paper or major reorganization, establish the actual results, study
suitable writing references and propose an outline suited to the work. Keep
decisions in existing project notes or `STATE.md` when used. Technical proximity
and usefulness as a writing example are separate considerations.

## Read only the guidance needed now

Resolve links relative to this skill directory, following its symlink if needed.
Select the guide for the requested unit; follow further links only for a concrete
decision. Do not load every chapter for a local revision.

| Requested work | Internal guide |
|---|---|
| Paragraph or section polishing, translation, iterative revision | [Collaborative polishing](references/collaborative-polishing.md) |
| A batch of proposed revisions for later discussion | [Paragraph comparison booklets](references/review-comparison.md) |
| New paper or substantial reorganization | [Writing from relevant papers](references/writing-from-related-work.md), then [overall structure](references/sections/00_overall_structure.md) |
| Title | [Title](references/sections/01_title.md) |
| Abstract | [Abstract](references/sections/02_abstract.md) |
| Introduction or contributions | [Introduction](references/sections/03_introduction.md) and, when needed, [contributions](references/sections/04_contributions.md) |
| Technical overview | [Technical overview](references/sections/05_technique_overview.md) |
| Related-work prose | [Related work](references/sections/06_related_work.md) |
| Background and notation | [Preliminaries](references/sections/07_preliminaries.md) |
| Construction, protocol or algorithm exposition | [Main technical content](references/sections/08_main_construction.md) |
| Presentation of security, correctness or analysis | [Security and correctness](references/sections/09_security_correctness.md) |
| Evaluation, including analytical cost comparisons | [Evaluation](references/sections/10_experiments.md) |
| Conclusion or appendix | [Conclusion](references/sections/11_conclusion.md) or [appendix](references/sections/12_appendix.md) |
| Deriving a personal style profile, explicitly requested | [Author style](references/author-style.md) |

For doubtful terminology or difficult prose, use
[field language and clarity](references/field-language-and-clarity.md).
[Synthetic revision examples](examples/revision-decisions.md) illustrate decisions
about structure, detail and attribution; their facts and wording are not templates.

## Shared writing decisions

- Reduce the reader's effort while preserving technical meaning, motivation and
  necessary explanatory links. Resolve concrete placement or duplication problems
  before fine word choices. Choose paragraph and sentence boundaries for the
  argument; fewer words alone do not establish an improvement.
- Use the subfield's established technical names and familiar words for ordinary
  explanation. Make the relevant objects, actions, conditions and reasoning
  connections clear. Introduce a symbol or intermediate quantity when its role
  is understandable, and preserve notation that already serves the paper well.
- Preserve assumptions, quantifiers, adversarial powers, probability space,
  security model and claim strength where relevant. Separate a technical
  correction from a language improvement. Editorial fluency cannot supply a
  missing proof, causal explanation or novelty result.
- Keep source facts, proved statements, manuscript derivations, cost models,
  local measurements, reported external results and estimates distinguishable.
  Never invent a citation, number, proof status or successful check.
- Use the primary source appropriate to the fact: a standard for its definition
  or normative parameters, and the original analysis or experiment for its
  results. Preserve the provenance of reused parameter choices and measurements.
- Trace changed numerical claims to their supporting material. Update evidence
  records and links when the project uses them; existing source notes or logs
  suffice for a local edit without a ledger. State a material missing source
  explicitly rather than filling the gap with a plausible value.

## Deliver and check

After a review or a batch of revision suggestions, offer a
[comparison booklet](references/review-comparison.md) when it would help the author
assess several passages later. Ask once unless already requested; finish the
requested review without making this optional artifact a prerequisite.

When revising, return a complete revised unit and a brief explanation of
substantive changes, unless the author asks for line edits or discussion only.
A passage that already serves its purpose may remain unchanged, with a brief
reason when useful. Preserve citation keys, labels, LaTeX commands and the current
revision-marking convention unless their change is authorized. Apply source edits
when requested or already authorized; discussion of wording alone does not
authorize file edits.

When the author changes the intended framing, reconsider the complete unit from
that objective. Check the affected meaning, notation, citations, numbers and
dependencies. Build changed LaTeX or audit changed evidence when warranted and
available; report only checks actually performed. Broader reviews, benchmarks
and submission work follow their own requested scope.
