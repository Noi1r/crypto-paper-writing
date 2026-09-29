---
name: paper-playbook
description: Plan, draft, or restructure a cryptography paper by studying relevant papers' content coverage, organization and exposition, then adapting those choices to the paper's actual results and intended readers.
---

# Paper playbook

Help the reader understand the problem, the method, the established results,
and the conditions under which they hold. Choose the organization from the
paper's content and dependencies. Preserve a clear existing author structure.

## Start with the requested task

Read `STATE.md`, the relevant manuscript material and supporting records. Use
`CLAIMS.md` for substantive claims, `EVIDENCE.md` for reported measurements,
and `LITERATURE.md` plus the project's verified bibliography for citations.
Use the actual manuscript and bibliography paths recorded in `STATE.md`.

- **New paper or major restructuring:** follow
  [writing from relevant papers](references/writing-from-related-work.md).
  Establish this paper's results, read suitable reference papers, and use
  [the overall structure guide](sections/00_overall_structure.md) to propose
  an outline and presentation choices suited to this work.
- **A section:** read its guide below and enough surrounding text to understand
  its role. Reuse the project's writing references and plan; choose paragraphs
  and headings to explain the actual result.
- **Local polishing or translation:** use
  [polish-writing](../polish-writing/SKILL.md), preserving the requested scope.
- **Personal style profile, only when requested:** follow
  [author-style guidance](../polish-writing/references/author-style.md). An existing
  profile can supply explicitly adopted preferences where applicable.

Record or link the paper-specific writing plan in `STATE.md`. Local edits use
the current manuscript and available plan without repeating the initial search;
a missing optional plan or style profile does not block a local edit.

## Shared writing decisions

- Use terminology established in the relevant subfield and ordinary, concrete
  prose around it. Keep technical names consistent and make the steps of the
  explanation explicit. Apply the field-language and readability guidance in
  [polish-writing](../polish-writing/SKILL.md) when drafting as well as revising.
- Preserve assumptions, quantifiers, security models, comparison conditions,
  numerical values and proof status. Keep limitations that qualify a claim
  close enough to be read with it.
- Paragraphs, contributions, questions, insights and figures have no prescribed
  count. Introduce them when they help explain this paper's argument.
- References to theorems, algorithms, tables and sections are useful when they
  help readers locate support. Their placement depends on the passage.
- Report what the available proof, analysis or experiment establishes. Leave a
  precise gap when needed support is missing.
- Treat a toy example's technical facts and organization as specific to that
  example. A style preference cannot add a result or change its scope.

## Section guides

| Guide | Use it to decide |
|---|---|
| [Overall structure](sections/00_overall_structure.md) | section order, optional sections and space allocation |
| [Title](sections/01_title.md) | which object, question or result should identify the paper |
| [Abstract](sections/02_abstract.md) | how to explain the problem, method and main results concisely |
| [Introduction](sections/03_introduction.md) | how to motivate the problem and position the contribution |
| [Contributions](sections/04_contributions.md) | which results to highlight and how to order them |
| [Technical overview](sections/05_technique_overview.md) | how to explain obstacles and the observations that address them |
| [Related work](sections/06_related_work.md) | which relationships and comparison conditions to explain |
| [Preliminaries](sections/07_preliminaries.md) | which definitions and prior tools readers need |
| [Main content](sections/08_main_construction.md) | how to present the protocol, construction, algorithm or result |
| [Security and correctness](sections/09_security_correctness.md) | how to state properties, support and remaining gaps |
| [Evaluation](sections/10_experiments.md) | how existing measurements answer the research questions |
| [Conclusion](sections/11_conclusion.md) | whether a closing synthesis adds useful information |
| [Appendix](sections/12_appendix.md) | where detailed support belongs and how to reference it |

## Deliver and check

Return a complete requested unit with a short explanation of substantive changes.
Check its claim scope, notation, references and numbers against the relevant
sources. For source edits, validate affected LaTeX and evidence links when
applicable. Report which checks ran. Request a broader review when the task calls
for one; local wording changes do not require a new full-paper review.

The starter files are in `.paper-writing/templates/paper/`. Synthetic examples
under `examples/` illustrate particular choices, without prescribing their form.
