# Draft from research materials

Use this guide to turn raw research notes, formal statements, constructions, and
experimental records into a clear first draft or new manuscript section. Follow
the technical and source-edit boundaries in [cpw-write](../SKILL.md).

Start from the current state of the project. Reuse any main argument, outline,
terminology, and reference analysis already recorded in `STATE.md` or project
notes. If the paper's overall organization is still open, consult
[writing from relevant papers](writing-from-related-work.md) first. You do not
need to initialize new ledgers or style files to begin drafting.

## Distill the core argument from the raw material

Read the author's notes, theorem statements, protocol descriptions, and data to
identify four anchors:

1. **The specific problem and setting:** What task is being solved, under what
   model or constraints, and where does the closest prior work leave off?
2. **The real technical obstacle:** Why do straightforward approaches or existing
   techniques fail, blow up in cost, or require an undesirable assumption here?
3. **The key observation or mechanism:** What structural property, algebraic
   relation, or protocol change overcomes that obstacle—and *how* does it work?
4. **The supported result and its boundary:** What theorem, asymptotic bound, or
   measured tradeoff follows, and under which exact assumptions or regimes?

State this storyline concisely in concrete terms before drafting long sections.
When a project has multiple results (for example, a new construction, a tighter
noise analysis that enables smaller parameters, and an implementation), clarify
how they fit together—whether they combine to support one headline contribution
or represent distinct results. Anchor the emphasis in what the evidence actually
proves rather than whichever number looks largest out of context.

Present one clear recommended framing. Offer an alternative framing only when
there is a genuine strategic choice (such as pitching to a theory vs. systems
audience). Ask the author only for missing facts that would alter the main claim
or mechanism; if a secondary benchmark is still running, draft the supported
construction and analysis first and mark the missing number explicitly.

## Turn the outline into a reader-centered explanation sequence

Use [overall structure](sections/00_overall_structure.md) for section placement.
Before drafting a technically dense section, map out the reader's path in a few
lines:

- **Entry state:** What definitions, notation, and intuition does the reader
  already have when entering this section?
- **Exit goal:** What exact statement, construction, or takeaway must the reader
  understand by the end of the section?
- **Bridging steps:** Which intermediate observations, definitions, or cost
  comparisons connect the entry state to the exit goal, in dependency order?

Name the substantive point of each step (*"Show why independent per-query setup
repeats identical work when $K$ is fixed"* $\to$ *"Define the batched index
reuse rule and state why verification soundness is preserved"*) rather than
writing generic placeholders like *"Background"* and *"Method"*.

Order the prose so every definition or helper quantity appears right when the
reader can see the question it answers. Establish what is being computed before
introducing the algebraic or systems machinery that accelerates it. Decide where
a concept gets its primary definition and where a one-line reminder or `\ref`
suffices.

## Write complete prose early

Pick the starting section that best resolves the main writing uncertainty:

- Draft the **Introduction** or **Contributions** first when positioning and
  claim scope need alignment.
- Draft the **Technical Overview** first when the hardest task is explaining how
  the core mechanism works without drowning in notation.
- Draft the **Main Construction** first when the boundary between inherited
  machinery and the paper's modification needs to be pinned down.

Deliver complete, readable prose with clear transitions and explicit conditions,
applying the relevant section guide and [field language and clarity](field-language-and-clarity.md).
Do not substitute bullet-point planning worksheets when the author asked for a
drafted section.

Adapt the pacing to the author's preference:

- **Stepwise collaboration:** Draft the agreed section or passage, incorporate
  feedback on tone and depth, and carry those choices forward.
- **Full-section or full-paper draft:** Write continuously through the supported
  material without stopping for approval after every subsection, and collect the
  few consequential open questions or missing citations in a concise note at the end.

Never invent a placeholder citation, synthetic benchmark number, or unproved
lemma to make a draft look complete; mark any material gap explicitly.

## Propagate feedback across dependent sections

Use the author's edits and reactions to calibrate technical depth, background
coverage, and voice. When feedback shifts a core claim or emphasis, trace the
ripple effects across connected sections—for example, narrowing a claim in the
evaluation may require updating the abstract, introduction, and contribution
list so they state the exact same scope. Record settled terminology or framing
choices briefly in `STATE.md` or existing notes so you never re-ask a decided
question.

## A first draft for later discussion

When preparing a draft for asynchronous review, organize it with stable section
or passage identifiers, complete prose, brief notes on key structural choices,
and the specific open questions that need the author's decision.

When drafting from raw notes, there is no prior manuscript passage—label the
author's inputs as source notes and your output as a draft (never fabricate an
"Original" manuscript passage). Once a first draft exists, subsequent revisions
can use a side-by-side [comparison booklet](review-comparison.md) if helpful.

## Check the resulting draft

Before returning the drafted unit, verify that:

- **Mechanism over buzzwords:** The prose explains *how* the construction or
  proof works and *why* the obstacle arises, rather than asserting that the
  method is "novel" or "efficient."
- **No silent jumps:** A reader at the target level can follow the motivation,
  steps, and conditions without guessing unstated premises.
- **Aligned scope and notation:** Symbols are defined before use, one term names
  one object throughout, and claim boundaries match across sections.
- **Strict evidence fidelity:** Proved statements, analytical models, local
  measurements, and prior-work numbers remain clearly distinguished.

See [the synthetic worked example](../examples/materials-to-draft.md) for an
end-to-end illustration from unordered research notes to a first draft and a
feedback-driven revision.
