# Related-work writing

Write the related-work section from the paper's actual contribution, verified
bibliography, and primary sources. Use `STATE.md` and `LITERATURE.md` when
present.

## Organize by technical axes, not a laundry list

Group prior works by the technical dimension the reader needs to compare—such
as the problem variant, underlying hardness assumption, adversarial model,
asymptotic regime, or algebraic mechanism. Avoid a paragraph of disconnected
"Author A did X. Author B did Y. Author C did Z." summaries; end each thematic
group by stating clearly where the present paper sits relative to that line of
work.

Place detailed related work early when readers need that context to understand
the problem setup, or place it after the main technical sections when a meaningful
comparison requires the paper's notation and cost model. Either way, always
compare against the closest 1–3 competitors directly in the introduction.

## Compare fairly and precisely

- **State what each prior work achieves under its own model:** Identify both its
  strengths and the specific constraint, assumption, or asymptotic bottleneck
  that distinguishes it from your result. A different threat model or target
  regime is a design trade-off, not a flaw.
- **Keep construction limits separate from analysis limits:** Distinguish what a
  prior protocol inherently requires from what a specific prior analysis bounded
  or what an earlier implementation measured. Do not claim a scheme lacks a
  property merely because one prior estimate omitted a term.
- **Verify numbers and claims in primary sources:** Check every cited complexity
  bound, parameter set, or runtime against the original paper (preserving section,
  table, or theorem pointers in your notes). Never copy a secondary summary from
  another paper's related-work section.
- **Cite the exact source for each fact:** Cite the normative standard for
  standard parameter sets or definitions, and cite the specific implementation
  or cryptanalysis paper for timings or attack costs obtained on those parameters.
- **Use comparison tables for multi-axis trade-offs:** When comparing several
  schemes across shared metrics (rounds, communication, prover/verifier ops,
  assumptions), add a self-contained table with explicit parameter definitions
  and footnotes for incomparable settings.
- **Follow venue rules on self-citation:** Write self-citations in the third
  person for double-blind submissions and apply the same evidential standard to
  your own prior papers.

See [synthetic related-work passages](../../examples/toy_overview_and_related.md)
for examples of balanced positioning across differing assumptions and workloads.
