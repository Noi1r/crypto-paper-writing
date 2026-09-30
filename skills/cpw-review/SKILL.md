---
name: cpw-review
description: Review cryptography manuscript expression, organization, technical support, or submission readiness at the requested depth. Produce concrete findings and revision options without editing the manuscript.
---

# Review a manuscript

## Establish the requested scope

Infer the review's purpose, unit and depth from the author's request and current
collaboration. The author can combine concerns without naming a mode. For a broad
request to review a paper, examine its main argument, organization, readability
and the support needed to assess its principal claims; state the scope you used.
Ask a focused question only when ambiguity would materially change the work.

Read the relevant manuscript and enough surrounding material to assess it.
For expression and structure reviews, apply the
[shared context rule](../cpw-write/SKILL.md#shared-writing-decisions) when deciding
whether a passage needs more introduction or a transition.
Use `STATE.md`, `CLAIMS.md`, `EVIDENCE.md`, `LITERATURE.md` and existing review
notes when present and relevant, following their actual paths. Pasted text or an
existing manuscript can be reviewed without creating these records or installing
project assets. Reuse source checks whose inputs have not changed.

| Author's concern | Focus and relevant guidance |
|---|---|
| Expression and readability | Wording, paragraph coherence, necessary explanation and reader assumptions. Use [collaborative polishing](../cpw-write/references/collaborative-polishing.md) and the relevant chapter guide. Preserve useful content and author structure. |
| Organization and exposition | Section roles, conceptual dependencies, placement and coverage of material. Use [overall structure](../cpw-write/references/sections/00_overall_structure.md); consult established writing references for recommendations based on field convention. |
| Technical claims and evidence | Check the particular statement against its definitions, construction, proof, data or primary sources. Use [security and correctness](../cpw-write/references/sections/09_security_correctness.md) or [evaluation](../cpw-write/references/sections/10_experiments.md) as applicable. Report the actual extent of verification. |
| Submission readiness | Check the intended submission version against current venue rules and the requested citation, anonymity, build or artifact requirements. Use [venue calibration](../venue-calibration/SKILL.md), [anonymity checks](../anonymize-check/SKILL.md) and other submission tools only for applicable checks. Preparing a package belongs to [cpw-submit](../cpw-submit/SKILL.md). |

Use [mock review](../mock-review/SKILL.md) when simulated venue reviews are
requested or clearly part of the agreed review. Ordinary expression or structure
review does not automatically require venue research, anonymity checks or a
submission checklist.

A language review can reveal a correctness issue that affects the passage.
Identify and investigate that issue proportionately, distinguishing it from the
editorial suggestions. Inspect primary sources for decisive prior-art or comparison
claims when they bear on the requested review. Keep broader proof audits, new
experiments and searches within their separately agreed scope.

## Present useful findings

For each actionable point, give a precise location, the problem, its effect on
the reader or claim, the relevant support, and a proportionate proposed revision.
Distinguish a demonstrated error, a concern needing verification, a structural
option and a stylistic preference. Prioritize by importance to the requested
task. State when a passage already works; do not manufacture a finding or a fixed
number of suggestions.

Check consistency across the sections affected by a substantive finding, such as
the abstract, contribution, theorem and table reporting the same result. A local
wording review need only follow the dependencies that matter to that passage.
Do not infer correctness from a successful build, an accepted proof or a passing
format check. Report unavailable or unrun checks accurately.

Return the findings in the requested format. Use an existing `REVIEWS.md` or
other project record when requested or appropriate for an ongoing review;
a brief discussion can remain in the conversation. Preserve the manuscript.
Suggested text and preview copies remain candidates until source edits are
authorized in the current collaboration.

## Optional comparison for later discussion

After presenting the findings, offer a paragraph comparison booklet when several
proposed revisions would be easier to assess together, especially when the author
will review them later. Explain the format briefly: stable C1, C2, ... identifiers,
gray original passages, red candidate revisions, locations and concrete reasons.
Ask whether it would be useful unless the author has already requested it; a
normal review or live paragraph discussion does not need this extra artifact.

If requested, follow the shared
[comparison booklet guide](../cpw-write/references/review-comparison.md).
Keep the manuscript unchanged while preparing the review copy. Track the author's
choices by ID; producing the booklet does not authorize applying its suggestions.

Use reviewer viewpoints within the current Codex task. Actual subagents are
optional and require the author's request and an available delegation tool.
