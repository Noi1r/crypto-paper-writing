---
name: polish-writing
description: Polish or translate a cryptography manuscript passage into natural, field-appropriate and readable prose, using the project's writing references while preserving technical meaning and LaTeX structure.
---

# Polish writing

Improve the requested passage in its surrounding argument. Read enough context to
identify its purpose, dependencies and terminology before rewriting it.

## Choose the style context

Use the author's current instructions, the manuscript's clear existing conventions
and the paper-specific writing references and plan recorded or linked in `STATE.md`.
Adapt useful choices from corresponding sections of the selected papers to this
passage. Required venue formatting and technical meaning govern their use.

For a new paper or major restructuring, follow
[writing from relevant papers](../paper-playbook/references/writing-from-related-work.md)
to choose content coverage, organization and exposition. A local polishing task
reuses that work without a fresh literature search. With no plan, work from the
current passage and context using clear, direct prose.

Create a personal style profile only if explicitly requested; that separate
workflow is in [author-style guidance](references/author-style.md). An existing
`STYLE.md` can supply applicable adopted preferences but is not a prerequisite.

## Use the field's language

- Use the names and technical word combinations established in the relevant
  subfield and consistent with the manuscript's definitions. Consult the selected
  reference passages when a term is doubtful. An uncommon term is not wrong merely
  because it is absent from a small reference set.
- Keep one technical name for the same object. Do not vary terms such as
  commitment, witness or verifier just to avoid repetition. Distinguish terms
  that denote different properties or objects.
- In ordinary explanatory prose, prefer familiar words and concrete verbs:
  say what is computed, sent, checked, assumed or proved. Replace a grand or
  vague expression with the specific supported statement.
- Avoid invented labels, elaborate compound phrases, unnecessary metaphors and
  tooling jargon when an established term or direct description suffices. Define
  a new term when the work actually introduces a concept that needs one.
- Treat words such as "robust", "efficient" or "extract" by their meaning in
  context. A blanket word ban can remove legitimate technical language.

See [field language and clarity](references/field-language-and-clarity.md) for
examples and the revision checks below. The goal is natural academic prose with
clear reasoning, without a fixed sentence length or a quota of stylistic devices.

## Revise for the passage's purpose

- Give each paragraph a clear job in the argument. Remove repetition or move
  material when it obscures that job. A useful summary can synthesize a tradeoff
  rather than repeat individual results.
- Use active or passive voice according to the focus of the sentence. Choose
  paragraph headings, lists and punctuation for clarity and the adopted style.
- Introduce notation and displayed equations when they clarify a relation or will
  be reused. Preserve notation that already serves the paper well.
- Keep names, spelling conventions, reference style and numerical precision
  consistent with the manuscript. A language edit should not alter a value.

## Make the explanation easy to follow

Unless the author specifies another audience, make the introduction and overview
accessible to a cryptography researcher outside the immediate subtopic. Technical
sections can use the definitions already established in the paper.

Name the relevant object, actor, action and condition explicitly. Resolve vague
references such as "this" or "the above" when the reader would have to guess.
Explain the connection between consecutive steps when it is necessary to follow
the argument; a connective alone does not supply a reason. Use causal or logical
language only when that relationship is supported.

When an unfamiliar definition or formula would otherwise be opaque, explain its
purpose or consequence nearby. A small example can clarify a difficult step.
Choose their order and amount from the passage's needs. Preserve technical terms,
assumptions and precision while simplifying the surrounding prose.

## Preserve the technical statement

Check assumptions, quantifiers, adversarial powers, probability space, security
model, comparison conditions and evidence status when they matter to the passage.
Do not make a proof, novelty or causal claim stronger to improve the prose.
If a technical correction is needed, distinguish it from the language changes.
Keep citation keys, labels and LaTeX commands intact unless their edit is part of
the request. Follow the project's revision-marking convention.

## Translation

Translate the intended meaning into natural academic English. Resolve an
ambiguous technical meaning from context or flag it; fluent English is not a
reason to choose a stronger interpretation. Provide a Chinese back-translation
when requested or when it helps resolve a specific ambiguity.

## Output and checks

Return the complete revised passage and a brief rationale for substantive edits.
Reread it once for field-appropriate wording and once for missing explanatory
links: can the intended reader identify the object, action, conditions and main
point without reconstructing unstated dependencies? Check affected meanings,
references and numbers. For source edits, build or audit when the changed
material warrants it. A local polishing request does not require
an unrelated full-paper review, new experiment or stylistic rewrite elsewhere.
