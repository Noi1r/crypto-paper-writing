# Evidence for printed numbers

Every measured or derived number printed in `paper/` gets a row here. Use a
path in the paper project for the original log. For a derived number, write
`derived: E1/E2` in the command column and `-` for the log. A row establishes
traceability, not correctness; check the configuration and computation too.

Link literal quantities in the manuscript with `1.23 s\ev{E1}` or a same-line
`% EV:E1` comment. Table rows can use `% EV:E1,E2`; per-cell tags give a more
precise mapping. The auditor checks the linked value and any visible unit. It
also checks that log files exist, but does not read their contents to validate
the measurement or recompute derived formulas. See
`.paper-writing/docs/evidence-audit.md` for the supported syntax and limits.

| ID | Number/fact as printed in paper | Command | Log path | Commit | Machine | Date | Runs/median |
|---|---|---|---|---|---|---|---|
