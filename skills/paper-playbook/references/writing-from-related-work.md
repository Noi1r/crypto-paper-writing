# Plan writing from relevant papers

Use this workflow when starting a new paper or substantially reorganizing one.
For a section edit or routine polishing, reuse the project's existing writing
references and plan. Read further only when a concrete decision needs more context.

## Start from this paper's results

Identify the research question, established results, intended contribution and
reader. Use the manuscript and relevant support records. These determine which
papers make useful references and what this paper can truthfully say.

## Select a small set of useful references

Start from the closest works in `LITERATURE.md`, existing reading notes and any
author suggestions. If these are insufficient, find relevant papers using the
literature-search procedures. There is no fixed paper count.

- Closely related technical work helps identify the background, definitions,
  comparisons and evaluation questions readers will expect.
- Clearly written papers with comparable contribution types and intended readers
  help choose exposition, organization and level of detail.
- The same paper can serve both roles, but technical proximity alone does not
  establish that its presentation is a useful example.

Read the relevant full-text sections and enough of the paper to understand their
role. For an ePrint paper, use `eprint.iacr.org` for identity, metadata and canonical
citation. Follow the user's configured full-text workflow, including Markdown
mirrors and the corresponding authoritative PDF where available. Match versions
when exact notation or source locations matter. Abstract-only access is
insufficient to assess a paper's full architecture or prose style; state any
access limitation and keep the writing plan provisional where it matters.

## Understand the writing choices

Compare corresponding sections and record only observations that inform a
decision for the current paper:

| Dimension | What to examine |
|---|---|
| Content coverage | What background is explained, which difficulty motivates the work, which comparisons and evaluation questions are addressed |
| Architecture | How overview, definitions, construction, analysis and evaluation depend on each other; why related work appears where it does |
| Exposition and style | How intuition connects to formal statements, how paragraphs develop, and when formulas, examples, headings or references help |
| Terminology and phrasing | Which names and technical word combinations describe the same objects or operations, and how ordinary prose makes them understandable |

For each useful observation, identify its source section and why it fits this
paper. Account for differences in topic, contribution type, venue constraints
and audience. Reference papers can suggest questions to address; their results,
assumptions, experiments and contribution claims do not become this paper's
content. Attribute any technical material used from them through normal citation.

For recurring terminology choices, note the relevant meaning and source usage
in the existing plan or terminology notes. Learn the field's vocabulary without
copying sentence sequences or unnecessary complexity. Apply
[field language and clarity](../../polish-writing/references/field-language-and-clarity.md)
when turning these observations into prose; even a technically close reference
may contain awkward phrasing that is not useful to imitate.

## Form a paper-specific writing plan

Use [the overall outline](../sections/00_overall_structure.md) as a starting
point. Propose the sections, each section's purpose and supporting material,
and the order that makes the argument understandable. Note the useful
presentation choices and any reasons to depart from the reference papers.

Keep a concise plan in `STATE.md` or link existing project notes from there.
Include the selected papers and sections, the decisions they informed, and the
planned outline. A separate style profile or additional planning file is not
required. Stop expanding the reference set once it supports the needed decisions.

When drafting is requested, begin with a key passage, such as the introduction or
technical overview, and use the author's feedback to refine the plan as writing
proceeds. Preserve explicit author preferences and clear conventions in an
existing manuscript. Paragraph counts, terminology and rhetorical moves should
fit the current content.

## Reuse the decisions

Later edits use the established plan. Revisit it when the contribution, audience
or requested organization changes, or when feedback reveals a specific problem.
Keep reference-specific notes in the paper project; the reusable toolkit holds
generic guidance and synthetic examples. Derive a reusable personal style
profile only when the author explicitly requests that separate task.
