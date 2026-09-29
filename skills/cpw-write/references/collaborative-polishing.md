# Collaborative manuscript polishing

Improve the requested passage in its surrounding argument. Read enough context to
identify its purpose, dependencies and terminology before rewriting it.

## Choose the style context

Use the author's current instructions, the manuscript's clear existing conventions
and the paper-specific writing references and plan recorded or linked in `STATE.md`.
Adapt useful choices from corresponding sections of the selected papers to this
passage. Required venue formatting and technical meaning govern their use.

For a new paper or major restructuring, follow
[writing from relevant papers](writing-from-related-work.md)
to choose content coverage, organization and exposition. A local polishing task
reuses that work without a fresh literature search. With no plan, work from the
current passage and context using clear, direct prose.

Create a personal style profile only if explicitly requested; that separate
workflow is in [author-style guidance](author-style.md). An existing
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
- Use "retain" and its inflections sparingly. Avoid it as a default verb for
  properties, capabilities, or guarantees; state the concrete behavior instead.
  For example, prefer "allows public verification" to "retains public
  verifiability" when describing what a system enables. Use "retain" when
  keeping an existing object or property is the precise intended meaning.
  Do not mechanically replace every occurrence with "preserve" or "maintain".

See [field language and clarity](field-language-and-clarity.md) for
examples and the revision checks below. The goal is natural academic prose with
clear reasoning, without a fixed sentence length or a quota of stylistic devices.

## Diagnose structure before sentences

Identify internally what the passage must add to the surrounding argument:
orient the reader, motivate a question, explain a mechanism, state a result or
qualify a comparison. Check what the preceding text already establishes and what
the next passage needs. For an initial structural revision, read the section;
later sentence edits can reuse that context.

When several problems coexist, address paragraph role and content placement,
then missing premises or explanatory links, then unnecessary repetition, and
finally sentence flow and word choice. Move material to where its purpose is
clear. Do not manufacture a transition to keep content with no independent role.

A paragraph normally has one main task, with as many closely connected steps as
that task needs. Section openings orient the reader; subsection openings state
the local goal; result paragraphs explain an observation. A useful summary draws
out a consequence or tradeoff. Choose these roles from the argument rather than
requiring every paper to use the same sequence or headings.

## Revise for the passage's purpose

- Give each paragraph a clear job in the argument. Remove repetition or move
  material when it obscures that job. A useful summary can synthesize a tradeoff
  rather than repeat individual results.
- Check paragraph coherence even when every sentence is individually accurate.
  Each sentence should advance the argument and connect clearly to the preceding
  one. Merge or reorder sentences that repeat an idea or restart the explanation;
  adding connective words alone does not repair the flow.
- Check nearby sentences for repeated words and sentence patterns. Prefer removing
  redundant content or using clear references over cosmetic synonym swaps. Keep
  technical terms consistent, and repeat them when needed for precision.
- Use active or passive voice according to the focus of the sentence. Choose
  paragraph headings, lists and punctuation for clarity and the adopted style.
- Introduce notation and displayed equations when they clarify a relation or will
  be reused. Preserve notation that already serves the paper well.
- Keep names, spelling conventions, reference style and numerical precision
  consistent with the manuscript. A language edit should not alter a value.

## Introduce detail when its purpose is clear

Choose background by its use in the later argument. When the paper replaces one
component of a larger construction, explain the interfaces, relevant behavior
and assumptions needed for that replacement. Add implementation or serialization
detail when an algorithm, security argument or cost claim depends on it.

Introduce an intermediate count, auxiliary set or acceleration step alongside
the question it answers. If its purpose belongs to a later part of the argument,
move its definition there instead of asking the reader to remember an unexplained
object. Explain deviations from a standard in the new construction, while making
clear which behavior belongs to the standard itself.

Before introducing a symbol, check whether an existing name suffices and whether
the symbol will be reused or makes a relation materially clearer. A displayed
formula earns space when it exposes a new relation, invariant, algorithmic
update, verifier check, bound or cost. Reuse definitions instead of displaying
them again merely because the same object reappears.

Give shared conventions and definitions a main location. Elsewhere, use a short
reminder or precise reference when readers need it. Keep a qualification near a
claim when moving it away would make the claim misleading. Apply the same test
to tables: each should answer a distinct question or make a useful comparison.
When removing repeated presentation, preserve the underlying supporting data.

## Make the explanation easy to follow

Unless the author specifies another audience, make the introduction and overview
accessible to a cryptography researcher outside the immediate subtopic. Technical
sections can use the definitions already established in the paper.

Avoid excessively long sentences. Split a sentence when it carries several
independent points or contains layers of clauses and parenthetical qualifications
that obscure the main action. Do not keep merging sentences merely to reduce
repetition. After splitting, maintain clear logical links and keep each condition
or qualification next to the claim it limits. Judge sentence length by readability
rather than a fixed word limit; never shorten a sentence by dropping technical
conditions. Check coherence, repetition, and sentence complexity together.

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

For paragraph-by-paragraph work, deliver the requested unit and wait for the
author's next direction. Reuse accepted terminology and decisions. If the author
changes the framing, rebuild the unit around the new objective instead of
patching the previous draft sentence by sentence. Follow the source-edit
authorization and output contract in [the writing entrypoint](../SKILL.md).

For examples of these decisions, see
[synthetic revisions](../examples/revision-decisions.md).
