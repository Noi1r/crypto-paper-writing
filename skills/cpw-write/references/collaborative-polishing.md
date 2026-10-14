# Collaborative manuscript polishing

Polish a passage so its argument is effortless to follow in context, while
keeping its technical meaning, assumptions, and claim strength exact. Read
enough surrounding text before editing to see what the passage must accomplish,
what notation is already active, and where the argument goes next.

## Anchor the style and scope

Follow the author's instructions, the manuscript's established conventions, and
any writing plan or reference notes recorded in `STATE.md`. When structural
choices depend on subfield conventions, compare the relevant sections of the
selected reference papers (see [targeted field comparison](writing-from-related-work.md#check-a-structural-edit-against-the-field)).
A local polishing task reuses existing plans—never trigger a new literature
search or create a personal `STYLE.md` profile unless the author explicitly asks
for [author-style guidance](author-style.md).

Match the depth of intervention to the request:

- **Line & paragraph polishing:** Keep the author's structure, coverage, and
  argument order while sharpening sentence flow, terminology consistency, and
  logical transitions.
- **Compression / cutting to length:** Cut throat-clearing, repeated setup, and
  table narration that merely reads numbers aloud, while keeping the premises,
  conditions, and causal links the reader needs to follow the proof or design.
- **Structural reorganization:** Diagnose the concrete reading obstacle caused by
  the current order (for example, an optimization introduced before the quantity
  it computes), state what moving or merging passages achieves, and note any
  change in emphasis.

## Diagnose in order: structure, logic, flow, then words

When a passage feels rough, fix issues from top to bottom rather than polishing
sentences that belong in a different place:

1. **Paragraph role and placement:** Give each paragraph one governing task—orient
   the reader, motivate an obstacle, explain a mechanism, state a formal property,
   or interpret a comparison. Merge adjacent paragraphs that announce the same
   goal twice; split a paragraph that mixes setup with a separate proof or cost
   argument.
2. **Missing premises and reasoning links:** Check whether a reader has the inputs
   needed for each step. Adding transition words (`Therefore`, `Consequently`,
   `Moreover`) never repairs a missing logical premise—state the actual technical
   reason that connects Step A to Step B.
3. **Information flow (Given-before-New):** Start sentences with familiar context
   or objects just introduced (`Given this decomposition...`, `In Each round...`,
   `For any adversary $\mathcal{A}$...`), and place the new technical point, formula,
   or cost bound at the end of the sentence. Replace vague pronoun openings
   (`This shows...`, `It ensures...`) with explicit subjects (`This degree bound
   shows...`, `The MAC check ensures...`).
4. **Word choice and notation hygiene:** Apply the mechanics in
   [field language and clarity](field-language-and-clarity.md): keep one name per
   technical object, replace nominalizations and vague glue verbs (`leverage`,
   `facilitate`, `utilize`, `retain`) with concrete actions (`computes`, `sends`,
   `checks`, `allows public verification`), and weave symbols grammatically into
   the sentence.

## Introduce technical detail at the moment it earns its keep

- **Match background to its role.** In the introduction, keep historical or
  deployment context that explains *why the problem matters*, even if no later
  lemma invokes it. In preliminaries and technical sections, include only the
  definitions, interfaces, and cost models that later steps actually use.
- **State the question before the helper machinery.** Introduce an intermediate
  counter, auxiliary set, or algebraic trick alongside the exact bottleneck or
  verification check it resolves. If an object isn't used until three pages later,
  move its definition there instead of forcing the reader to memorize it early.
- **Distinguish inherited machinery from the paper's modification.** When
  modifying a standard or prior scheme, make clear which steps belong to the
  baseline and where the new construction diverges.
- **Earn every symbol and displayed equation.** Before coining a new symbol, check
  whether plain English or an existing symbol suffices. Display an equation when
  it highlights a key invariant, protocol check, recurrence, or complexity bound;
  do not re-display a definition simply because the object is mentioned again.
- **Define shared conventions once.** State global indexing, parameter, or
  benchmark conventions in one primary location and use brief pointers elsewhere.
  Keep qualifying conditions next to the claims they restrict whenever separating
  them would make a headline claim misleading.

## Keep explanations accessible without dulling precision

Unless the author specifies a narrower audience, write the abstract, introduction,
and technical overview so a cryptographer in a neighboring area can follow the
problem, obstacle, and core idea without flipping to the preliminaries.

Break up overloaded sentences that stack multiple subordinate clauses, caveats,
and parentheticals around the main verb. When splitting a sentence, preserve the
logical link and keep every security assumption, quantifier, or parameter condition
attached to the statement it limits. Never simplify prose by dropping a technical
hypothesis or upgrading a heuristic/model count into an unconditional or measured
result.

## Translation and Chinese-to-English academic revision

When translating Chinese drafts or revising English prose influenced by Chinese
sentence patterns, convert the structure into idiomatic cryptographic English
while keeping the exact technical scope:

- **Turn topic-comment chains into clear subject-verb sentences.** Chinese
  academic prose often opens with a broad topic clause followed by several
  floating participles (*"Regarding the bootstrapping step, by introducing the
  sparse packing method, it makes the key-switching cost significantly reduced"*).
  Rewrite with an explicit subject and direct verb: *"Our sparse packing method
  reduces the key-switching cost during bootstrapping from $O(N)$ to $O(\sqrt{N})$
  automorphisms."*
- **Eliminate dangling modifiers and subjectless passives.** Fix patterns like
  *"Utilizing the LWE assumption, the security of the scheme is proved"* or
  *"Aiming at the problem of high communication, a new protocol is proposed"*.
  Name the theorem, construction, or actor: *"Under the LWE assumption, Theorem 3
  establishes IND-CPA security"*; *"To reduce communication in the preprocessing
  phase, we batch..."*.
- **Calibrate claim strength across languages.** Phrases like *"极大地提升了"*,
  *"彻底解决了"*, or *"具有极强的安全性"* should be rendered through the actual
  supported bound, asymptotic improvement, or formal security notion—never
  translated literally into unsupported superlatives (*"completely solves"*,
  *"extremely secure"*).
- **Flag genuine technical ambiguities.** If a Chinese passage leaves a quantifier,
  adversary model, or comparison baseline implicit, ask the author or provide a
  brief Chinese note explaining the two possible readings rather than guessing
  the stronger claim.

## Deliver and verify

When reviewing multiple passages for asynchronous discussion, offer a
[paragraph comparison booklet](review-comparison.md) (numbered `C1, C2, ...`
items with gray original text, red proposed text, and concise rationale). For
live paragraph-by-paragraph editing, stay directly in the conversation.

Deliver the complete revised passage and briefly explain any non-obvious
structural or technical-wording choices. If a passage is already clear and
accurate, say so and keep it unchanged. Before returning the revision:

- Verify that readers can still follow the motivation, mechanism, and conditions
  without reconstructing deleted context.
- Confirm that assumptions, quantifiers, citations, LaTeX macros, and numbers
  match the source material.
- Run a build or evidence audit when editing source files on disk warrants it.
  If the author shifts the framing of a passage, rewrite the unit around the new
  objective rather than patching isolated words.

See [synthetic revisions](../examples/revision-decisions.md) for concrete
examples of these editorial judgments.
