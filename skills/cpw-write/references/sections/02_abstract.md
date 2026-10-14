# Abstract craft

Draft or revise the abstract from the manuscript's established contributions,
formal statements, and verified evidence. Check the target venue's abstract
rules (word limits, plain-text portal constraints, or paragraph norms) whenever
they apply.

## Give the reader four essentials

An effective cryptography abstract lets a busy reviewer grasp the paper's core
value in one pass:

1. **The problem and why it matters:** Name the concrete cryptographic setting or
   task and the specific bottleneck, gap, or assumption limitation in prior work.
   Avoid generic textbook openings (*"Cryptography is fundamental to modern
   security..."*).
2. **The key mechanism or insight:** State *what your approach does differently*
   at a conceptual level (for example, replacing per-query degree checks with a
   single batched linear combination, or reducing security to standard LWE via
   a lossy mode). Define a new term in the abstract only if it is central to the
   headline claim.
3. **The main established results:** State the principal theorem, asymptotic
   complexity, concrete cost, or measured performance with its exact metric and
   baseline.
4. **The qualifying scope:** Keep essential conditions attached to the result—the
   security model (standard model vs. ROM, semi-honest vs. malicious), parameter
   regime, or workload constraint—and note an open-source artifact or mechanized
   proof when it materially strengthens the paper.

Let the paper's content determine whether the abstract runs one paragraph or two.
Lead directly into the problem or result without meta-phrases like *"In this
paper, we first introduce... and then we discuss..."*.

## Verify before finalizing

1. **Exact alignment with the body:** Every claim and number in the abstract must
   appear with the same scope in the introduction, theorems, or evaluation tables.
   Keep proved bounds, analytical cost counts, and empirical timings distinct.
2. **Traceable comparisons:** When stating a speedup or size reduction, preserve
   the metric, baseline, and tested regime (for example, *"1.4–1.8× higher
   throughput than [Baseline] across eight batch workloads, with no improvement
   for single-request latency"*). Link numbers to `EVIDENCE.md` when used.
3. **Mechanisms over adjectives:** Replace empty intensifiers (*"highly
   efficient"*, *"strong security guarantees"*) with the actual bound, assumption,
   or measured figure—never invent a number to make a sentence sound stronger.
4. **Self-contained readability:** Avoid unexplained symbols, internal section
   numbers, or raw BibTeX `\cite{...}` keys unless the venue style explicitly uses
   citations in the abstract. Produce a clean plain-text version alongside the
   LaTeX version when preparing submission metadata.

See [synthetic abstract examples](../../examples/toy_abstracts.md) for how
theoretical, empirical, and protocol tradeoffs shape abstract structure.
