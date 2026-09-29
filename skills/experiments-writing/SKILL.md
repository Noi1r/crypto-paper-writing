---
name: experiments-writing
description: Write an evaluation section from existing experimental evidence, with clear research questions, reproducible measurement conditions, fair comparisons and conclusions limited to the results.
---

# Experiments writing

Use the existing data, logs, `EVIDENCE.md`, relevant manuscript claims and baseline
sources. This writing workflow reports established measurements; new benchmark
execution is a separate research task.

## Organize around the questions

Identify which claims the evaluation addresses, the measurements needed to
interpret them, and what is actually available. Arrange setup and results so the
reader can assess each question. Choose tables and plots for those questions.
An evaluation section is appropriate when the paper reports experimental claims.

## Describe the relevant conditions

Report the workload, parameters, security or accuracy conditions, implementation
versions, hardware, concurrency, measured boundary, repetitions and statistic
that affect the result. State exclusions, failures and correctness checks that
were actually performed. For security estimates, identify their source and model;
a tool-derived security column is not applicable to every construction.

A comparison should identify the baseline and the conditions shared or changed.
Label separately measurements reproduced by the authors and numbers quoted from
another source. Explain material differences before interpreting a ratio.

## Interpret results

- State the principal observation and its scope, then explain it to the extent
  the evidence permits. Report relevant overheads and regimes where a method loses.
- Use ablation when it helps assess a component or attribution claim. Describe
  what the variants actually establish; a tested component's benefit does not
  imply that it is necessary in every setting.
- Attribute gains only as specifically as the controlled comparison supports.
  Several simultaneous changes may support an overall gain without identifying
  the contribution of each change.
- Keep cost-model predictions, measurements and extrapolations distinguishable.
  Report negative or inconclusive results when they affect a manuscript claim.

## Preserve the data connection

Generate tables and plots from the recorded data. Each reported numerical result
has an `EVIDENCE.md` entry; annotate literal values as `1.23 s\ev{E1}` or use a
same-line `% EV:E1,E2` comment. Keep rounded values, units and comparison direction
consistent with their source and with the abstract and contributions.

Run `make -C paper audit`, or
`python3 .paper-writing/scripts/audit_tex.py paper/main.tex EVIDENCE.md` for the
default layout. This checks ledger fields, log paths and linked literals in
reachable TeX files. Review units in headings, macro-generated and graphic
numbers, claim scope and derived arithmetic separately. See
`.paper-writing/docs/evidence-audit.md` for supported syntax and limitations.

Deliver the requested evaluation text with its necessary tables or figures, and
report the checks actually performed. See
[the section guide](../paper-playbook/sections/10_experiments.md).
