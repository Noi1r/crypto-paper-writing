# Overall structure

For a new paper or a requested reorganization, first establish its actual results
and study suitable reference papers using
[writing from relevant papers](../writing-from-related-work.md).
Then propose an outline before drafting whole sections. State each section's
purpose, available source material and conceptual dependencies, explaining the
reference choices that informed the plan. For a local edit, use the existing plan.

## Starting outline

| Part | Reader's task | Placement and optionality |
|---|---|---|
| Abstract | Understand the problem, method and main results | Content determines its paragraph structure |
| Introduction | Understand the motivation, contribution and closest prior work | Contributions can be prose or a list |
| Technical overview | Understand the obstacles and key ideas | Part of the introduction or a separate section; may follow preliminaries if definitions are essential |
| Preliminaries | Learn the notation, models and tools used later | A substantial problem statement or security model can have its own section |
| Main technical content | Follow the protocol, construction, algorithm or theoretical development | Split and order sections by their actual dependencies |
| Correctness, security and analysis | Assess the claimed properties and costs | Attach analysis to each construction or give it a separate section |
| Evaluation | Assess concrete results under stated conditions | Include analytical parameter comparisons, measurements or both when relevant |
| Related work | Understand the detailed relation to relevant results | Place early when it motivates the contribution, or later when comparison needs technical context |
| Conclusion | Synthesize the significance, limits or remaining questions | Optional when no useful synthesis is needed and venue rules permit omission |
| References and appendix | Find sources and detailed supporting material | Follow the applicable venue rules |

This is a starting reading order. Merge, split, move or omit sections according to
the content. Keep a concise account of the closest prior work in the introduction
regardless of where the detailed related-work section appears.

## Choose what gets space

Give the main contribution and its explanation enough space to be assessed.
Compress repetition or background that adds no explanatory role for the intended
reader. Useful background can establish motivation or context as well as support
later technical steps. Cut table narration that merely repeats visible entries.
Do not assign fixed percentages to sections or require the conclusion to fill the
last body page. Check the actual venue template, page limit and appendix policy
before making layout decisions; do not silently alter required typography.

## Maintain continuity

Use consistent names and notation across the manuscript. A notation table is
useful when it reduces lookup effort. Introduce the definitions needed for a
passage before relying on them. Cross-reference detailed statements and proofs;
simplified overview notation is acceptable when its relationship to the formal
statement is explicit.

Language and presentation choices follow the author's instructions, the current
manuscript and the writing plan developed from relevant papers. An existing
personal profile can supplement these choices when applicable; see
[collaborative polishing](../collaborative-polishing.md).

## Check the outline

Can readers identify the problem and contribution early, then acquire the
background needed for each technical step? Is every substantive claim supported
somewhere readers can find it? Does each planned section have a distinct purpose
and actual material to present?
