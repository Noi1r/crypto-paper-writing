---
name: technique-overview
description: Explain a cryptography paper's actual technical obstacles and the observations or mechanisms that address them, with enough detail to connect intuition to the main results.
---

# Technical overview

The reader should be able to explain the main idea, why the difficulty arises,
and how the technique addresses it before reading the full technical development.

## Inputs

Read the main statements and constructions, the relevant prior work, and the
existing introduction. Use the current notation and the overview references and
presentation choices in the project's writing plan. The overview can be part of
the introduction or a separate section; use the manuscript's structure unless a
change improves understanding.

## Develop the explanation

- Identify the difficulty that actually motivates the technical step. Explain
  the relevant prior approach only as far as needed to understand that difficulty.
- State the observation, mechanism or proof idea that changes what can be done.
  Connect it to the result and explain the assumptions it needs.
- Order the explanation by its conceptual dependencies. Use questions, insight
  headings, a worked example, formulas or a diagram when they clarify a step.
  Their number and form follow the content.
- Define the notation needed here locally. If substantial definitions are
  required, consider a minimal background paragraph or a different placement.
- Point to the precise statements or algorithms that develop the idea. A
  simplified formula is acceptable when its simplification and scope are clear.

## Check

Can a reader trace the stated obstacle through the proposed idea to a supported
result? Are the conditions stated before they are used? Does the overview agree
with the body without repeating the entire related-work discussion or proof?
An intuitive explanation should not upgrade a conjecture, heuristic or partial
result to a theorem.

Deliver a complete overview in its existing source location. Request a figure
only if there is a concrete relation or process that it would help explain.
See [the section guide](../paper-playbook/sections/05_technique_overview.md).
