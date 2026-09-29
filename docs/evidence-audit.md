# Evidence audit: what is checked

Run from the installed paper project's root:

```bash
make -C paper audit
# or, for a different entry source:
python3 .paper-writing/scripts/audit_tex.py paper/main.tex EVIDENCE.md
```

The default check validates the ledger and follows literal `\input{...}` and
`\include{...}` dependencies, including generated tables. Input paths resolve
relative to the entry source's directory; log paths resolve relative to the
ledger's directory, or `--root` when provided. Missing files are errors.

## Link each literal result to its evidence

Suppose `E1` records `1.23 s` and `E2` records `256 bytes`:

```latex
Runtime is 1.23 s\ev{E1}; communication is 256 bytes\ev{E2}.
Runtime is 1.23 s. % EV:E1
Toy method & 1.23 & 256 \\ % EV:E1,E2
```

An inline tag binds the immediately preceding quantity on the same source line.
The template defines `\ev` as an invisible macro; `\evid` is a supported legacy
spelling. In an existing manuscript, define `\newcommand{\ev}[1]{}` once if it is
not already defined. A comment binds the numbers on that source line to the
listed rows; per-cell tags make a table's mapping more precise.

A number's occurrence elsewhere in the ledger is insufficient. The value must
match its linked row, and an explicit unit must match too: `1.23 GB\ev{E1}` fails.
Formatting such as `1.230`, `1{,}000`, `\,`, `\mathrm{s}`, and common scientific
notation is recognized. `seconds`/`second`/`s` are equivalent spellings; `s` and `ms`
are distinct. The checker does not silently convert units or round values.
Record the actual rounded value printed in the paper.

Outside tables, untagged decimals, quantities with supported units, and numeric
exponents are flagged. Bare integers are also checked inside `tabular`,
`tabular*`, `tabularx`, and `longtable`, or when explicitly tagged. `--strict`
checks all recognized integers, including mathematical constants. `--single-file`
limits the check to one file for a targeted edit; ledger validation still runs.

## Ledger checks

The first evidence table must contain ID, printed value, command and log columns.
IDs must be unique. Each measured row needs a command and a log file; missing
commit, machine, date or run-statistic fields produce warnings. A derived row
uses `derived: E1/E2`, references existing rows, and must not form a cycle. Its
formula is recorded for review, not evaluated by this tool.

Exit codes: `0` means these checks found no errors (warnings may remain); `1`
means findings were reported; `2` means an input could not be read or parsed.
An empty ledger table is valid for an empty draft; a missing or malformed ledger
is not treated as an empty table.

## Scope and exclusions

This is a static source check. Review the following separately:

- The source log's contents, measurement configuration, claim scope, and derived
  calculations. A valid link does not establish that the result is correct.
- Numbers and units emitted by custom macros, packages, generated graphics, or
  table headings. Standard literal input/include files are followed; arbitrary
  TeX expansion is not. A macro-based input path is reported as unresolved.
- The relationship between a displayed mathematical expression and a theorem.
  Recognizing some literals in an expression does not verify that expression.
- Conditional builds: both reachable branches are scanned. The checker does not
  evaluate TeX conditionals or determine which pages a given build renders.

For layout dimensions or mathematical constants intentionally outside the
measurement ledger, use a comment explaining the exclusion:

```latex
\fbox{\parbox{0.8\linewidth}{Toy diagram}} % papercheck:ignore (layout width)
```

`% papercheck:ignore-begin (reason)` / `% papercheck:ignore-end` can exclude a
block; unmatched or nested delimiters fail the check. Excluded inputs are not
followed. Keep exclusions narrow and review them before submission.
