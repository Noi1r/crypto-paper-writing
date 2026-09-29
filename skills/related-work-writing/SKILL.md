---
name: related-work-writing
description: Explain a cryptography paper's relation to the most relevant prior work, using verified sources and explicit comparison conditions. Choose organization and placement to suit the paper.
---

# Related-work writing

Read the paper's actual contribution, `LITERATURE.md`, the verified bibliography
(default `paper/refs.bib`) and the primary sources relevant to the comparison.
Use the source paths recorded in `STATE.md` for an existing manuscript.

## Choose the organization

Group works by the relationship the reader needs to understand: the problem,
method, assumptions, model, cost, or application setting. Chronological order can
help explain a development when that history matters. Use a comparison table
when its entries can be compared under stated conditions.

Place detailed related work early when readers need it to understand the problem
or contribution; place it later when comparison needs the paper's technical
context. In either case, the introduction should identify the closest work and
the paper's specific advance.

## Write and verify

- For each important comparison, identify what the prior work establishes and
  under which assumptions or configurations. Explain the relationship to the
  present result, including complementary work and differing settings.
- Verify technical characterizations and numbers against their primary source;
  retain section or page pointers in the literature notes.
- State factual differences. A different objective or security model is not
  itself a shortcoming. Do not infer an advantage from incomparable measurements.
- If a table is useful, define its metrics, symbols and qualifications. Include
  the present work where a matched comparison is possible.
- Check the relevant literature for close or concurrent work when the request
  involves positioning or novelty. Report the scope of that search.
- Follow the applicable venue policy for self-citations, and apply the same
  evidential standard to the authors' earlier work.

Deliver the requested section and any necessary citation corrections. Paragraph
counts, comparison axes and headings follow the selected organization.
See [the section guide](../paper-playbook/sections/06_related_work.md).
