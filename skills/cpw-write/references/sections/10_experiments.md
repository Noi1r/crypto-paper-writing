# Evaluation

Present analytical parameter comparisons, operation counts, and experimental
benchmarks so the reader can see which technical questions they answer and under
what exact conditions. Running new benchmarks or implementations belongs to
research execution, not manuscript polishing.

## State the experimental or analytical setup once

Open the evaluation by defining the shared testbed and comparison rules in one
place:

- **What is held fixed and what varies:** Security level (and the estimator or
  convention used to match it), ring/field parameters, input sizes, threat model,
  and network/hardware environment (CPU, cores/threads, RAM, LAN/WAN latency and
  bandwidth, run count, and summary statistic such as median or mean).
- **What each metric includes:** Make the timing or size boundary explicit (for
  example, whether setup/key generation is separated from online runtime, or
  whether proof size includes public commitment headers).
- **Evidence category:** Keep analytical cost models, local measurements run on
  the same machine, and numbers quoted from prior papers visually and verbally
  distinct in both prose and table captions.

## Lead each result paragraph with the takeaway observation

Rather than narrating a table row by row (*"Table 2 shows the results. For
$n=2^{16}$, ours is 1.2 s and Baseline is 2.4 s..."*), organize each paragraph
around the **observation and its technical explanation**:

1. **State the headline observation and its quantitative range:** *"Across batch
   sizes $b \in [16, 256]$, sharing the lookup index reduces amortized verification
   time by $1.4\text{--}1.8\times$ compared to independent per-query setup (Table 2)."*
2. **Connect the observation to the mechanism:** Explain *why* the curve or
   ratio behaves that way—for example, which cost term dominates at small $b$,
   where memory bandwidth saturates, or how a tighter noise bound allows a
   smaller modulus.
3. **Report crossovers, overheads, and regimes where the method loses:** State
   plainly where the trade-off flips (e.g., single-query latency or extra key
   storage). Honest boundary reporting builds far more reviewer trust than selective
   cherry-picking.

Ensure every table and figure answers a distinct question; merge duplicate tables
and cut prose that merely reads visible numbers aloud without interpreting them.

## Keep comparisons and causal attribution rigorous

- **Separate component gains from end-to-end gains:** If a sub-protocol shrinks
  by $50\%$ while fixed surrounding data occupies $800\text{ B}$, report both the
  $50\%$ component reduction and the resulting $16.7\%$ end-to-end reduction.
- **Distinguish model counts from wall-clock speedups:** Operation counts, gate
  counts, and byte formulas establish analytical savings; do not describe them as
  measured runtime speedups unless wall-clock timings were actually recorded.
- **Attribute gains only to isolated variables:** Claim that a specific trick
  causes a speedup only when an ablation or controlled comparison isolates that
  trick. When several optimizations are enabled together, credit the combined
  design unless an ablation breaks down their individual shares.
- **Preserve baseline provenance:** When comparing against a baseline on a
  different thread count, hardware platform, or parameter regime (or quoting numbers
  from a prior paper), state that difference right next to the ratio.

## Trace every number to its source

Keep all numerical values, units, rounding, and speedup directions consistent
 across the abstract, introduction, tables, figures, and body prose. Never insert
a placeholder number to complete a sentence; flag missing measurements explicitly.

When the project uses `EVIDENCE.md`, link reported numbers via `\ev{E1}` or a
same-line `% EV:E1` comment and run `make -C paper audit` (or
`python3 .paper-writing/scripts/audit_tex.py paper/main.tex EVIDENCE.md`) after
editing numerical passages. Because the automated audit checks only linked
literals and log paths, manually verify table column headers, units, derived
ratios, and claim scope before finishing.
