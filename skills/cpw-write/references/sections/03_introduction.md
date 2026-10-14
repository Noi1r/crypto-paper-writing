# Introduction

Write the introduction so a cryptographer outside your immediate niche can see
why the problem matters, why existing approaches fall short in the target setting,
and how your contributions resolve that tension.

## Build a clear narrative arc

1. **Anchor the problem in a concrete setting:** Open with the specific task,
   deployment constraint, or theoretical question that drives the paper. Skip
   sweeping truisms about the digital era; start close enough to the technical
   area that the reader immediately recognizes the objects at play.
2. **Pinpoint the obstacle in prior work:** Explain what the closest existing
   schemes or analyses achieve and where they hit a barrier—whether an asymptotic
   bottleneck, an idealized assumption, an incompatibility with a verifier
   constraint, or a gap between heuristic practice and provable bounds. Cite
   primary sources accurately and describe prior trade-offs fairly without
   dismissing different models as "flawed."
3. **Bridge from the obstacle to your core idea:** Before listing formal
   results, give the reader a brief, intuitive glimpse of the mechanism that
   breaks the deadlock. State *what changes* in the construction or proof and
   *why* that change works.
4. **Present the contributions with their exact scope:** State what the paper
   proves, constructs, or measures, along with the assumptions and regimes required
   (see [contributions](04_contributions.md)).

Keep surrounding application motivation distinct from the formal cryptographic
problem so readers know what is motivating context and what is proved in the
paper. Avoid announcing the paper's goal two or three times in consecutive
paragraphs; let each paragraph advance the argument one step further.

Include a brief comparison with the closest prior art right in the introduction
even when a full Related Work section appears later in the paper. Add a dedicated
Technical Overview subsection or a short roadmap only when it genuinely helps
readers navigate the paper's structure.

## Check

- Can a reader state the exact research question, why straightforward solutions
  fail, and what your paper achieves after reading the introduction alone?
- Does every headline claim in the introduction match the assumptions, models,
  and numbers proved or measured in the body?
