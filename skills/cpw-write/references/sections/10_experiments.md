# Evaluation

Use existing analytical results, parameter calculations, measurements, logs and
baseline sources. Explain which questions they answer and under what conditions.
New experiments, searches and implementations are separate research tasks.

## State the setup once

Identify what is fixed, what varies, the selected configurations and the objective
used to choose them. Describe the metric and its inclusions before interpreting
results. Hardware, concurrency, repetitions and statistics are relevant to
measurements; a byte count or operation-count model needs its own assumptions.

Keep analytical counts, measured values, reported external results and
extrapolations distinguishable. For a security estimate, name its source, model
and matched convention. A bound on one event does not alone establish the full
security of a construction.

Use a main location for shared counting conventions, baseline choices and
comparison conditions. Tables can refer to that location while keeping units and
local qualifications visible. Explain a correction or normalization where needed
to interpret the result; keep implementation bookkeeping out of the main narrative
when it has no bearing on the comparison.

## Write each result around its observation

For each table or figure, state the principal observation and the values needed
to assess it. Explain the connection to the design to the extent the evidence
permits. Include relevant overheads and regimes where a method loses.

Choose the order from the local argument. Once setup is established, an observation
can lead the paragraph. Avoid a repeated template for every figure, narration of
every table cell, or a sentence announcing a value immediately before reporting
it. Repeat a parameter name when a phrase such as "at this size" is ambiguous.

Each table should answer a distinct question or make a useful comparison.
Consolidate tables that duplicate the same information, preserving the underlying
evidence. A closing paragraph should explain a consequence or tradeoff.

## Match the comparison and attribution

- Identify the baseline, functionality, parameters and conditions shared or
  changed. Separate reproduced measurements from numbers quoted from a source.
  Differences in machine, implementation, parallelism or timing boundary can
  prevent a ratio from representing a direct speedup.
- Keep component size separate from complete-object size, and additional proof
  material separate from the entire response. Fixed surrounding costs can make
  a large component saving a modest total saving.
- Distinguish operation counts from elapsed time, expected values from bounds,
  and parameter-point comparisons from claims about an entire design family.
  State the ratio's denominator and direction; do not claim a "best balance"
  without a stated objective combining the metrics.
- Attribute a gain to a mechanism only when the selected configurations and
  controlled comparison support that explanation. Check that the mechanism is
  actually used. Improvements after several simultaneous changes establish an
  overall result without necessarily isolating each component's contribution.
- Use available ablations to answer a specific attribution question. Explain
  what the variants establish, including negative or inconclusive results.
  A local polishing request does not require running a missing ablation; narrow
  the claim or identify the gap.
- A stronger bound may enable a better parameter choice without changing the
  construction. A search result need not be a global optimum. Preserve these
  distinctions when explaining where an improvement comes from.

## Keep values connected to sources

Generate tables and plots from the recorded data when creating or updating them.
Use the manuscript's existing source links or evidence records. When the project
uses `EVIDENCE.md`, each reported numerical result should have an entry;
link literals as `1.23 s\ev{E1}` or with a same-line `% EV:E1,E2` comment.
A local revision in a manuscript without that ledger can use its existing logs,
tables, citations or notes without creating a new record system.

Keep units, rounding, comparison direction and percentages consistent with the
sources and with the abstract and contributions. Never insert a plausible number
as a temporary baseline. Mark missing information explicitly.

For a project using the CPW evidence audit, run the relevant check after changing
linked values: `make -C paper audit`, or
`python3 .paper-writing/scripts/audit_tex.py paper/main.tex EVIDENCE.md` for the
default installed layout. The checker covers ledger fields, log paths and linked
literals in reachable TeX files. Review units in headings, macro-generated and
graphic numbers, claim scope and derived arithmetic separately. Its limits are
documented in `docs/evidence-audit.md` at the toolkit root.

Deliver the requested evaluation text and necessary tables or figures within the
authorized editing scope. Report the checks actually performed and any remaining
gap that materially affects the result.
