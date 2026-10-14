# Contributions

Make the paper's advances and their technical substance immediately scannable.
Ground every item in the manuscript's proved theorems, constructions, and
verified evaluation records.

## State the mechanism ("how"), not just the outcome ("that")

Reviewers discount contribution bullets that merely assert quality (*"We propose
a novel protocol and prove its security; experiments show high efficiency"*).
Structure each contribution so the reader sees both **the technical mechanism**
and **the conditioned result**:

- **Analytical or theoretical contribution:** Name the structural property,
  dependency, or reduction technique that yields the result, followed by the
  formal statement and model (*"We introduce a recurrence that tracks repeated
  item selection across queries (Theorem 2), tightening the failure bound from
  $O(q^2/N)$ to $O(q/N)$ in the standard model"*).
- **Construction or protocol contribution:** State what component or interaction
  changes and what asymptotic or concrete property follows (*"We replace per-gate
  key switching with a hoisted automorphism over packed ciphertexts (Section 4),
  reducing rotation keys from $O(d)$ to $O(\sqrt{d})$ without increasing
  multiplicative depth"*).
- **Implementation and evaluation contribution:** Specify what was built, the
  comparison baseline, the headline trade-off, and the regime where it holds,
  including regimes where the method offers no gain.

## Group and order for clarity

- Merge steps that form a single logical advance; separate results that rely on
  distinct techniques or different kinds of evidence (e.g., a formal proof vs. an
  empirical benchmark).
- Include explicit pointers to the supporting theorems, algorithms, sections, or
  tables (`Theorem 1`, `Algorithm 2`, `Table 3`), while stating the result clearly
  in words so the reader does not have to flip pages to know what was achieved.
- Match the verb to the evidence: use `prove` or `establish` for theorems,
  `derive` or `bound` for analytical models, and `measure` or `evaluate` for
  benchmarks.
- State necessary boundary conditions directly inside the contribution item whenever
  omitting them would overstate the claim.

## Check

- Does each contribution state a concrete mechanism and a falsifiable outcome?
- Are all assumptions, security models, and comparison baselines explicit?
- Do all theorem, section, and table pointers resolve to the exact promised support?
- Have you eliminated redundant bullets that restate the same result in different words?
