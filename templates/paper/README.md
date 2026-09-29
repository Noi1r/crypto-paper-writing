# Paper template (Springer LNCS)

Skeleton whose sections match `.paper-writing/skills/cpw-write/references/sections/`
(from the project root). Placeholders use
`<<...>>`; grep for `<<` before submission.

## Files

| file | purpose |
|---|---|
| `main.tex` | anonymous submission build; one shared source for all versions |
| `main_camera.tex` | proceedings/camera-ready driver (`\buildcamera`: de-anonymised) |
| `main_full.tex` | full-version driver (`\buildfull`: de-anonymised + `\iffull` material) |
| `authors.tex` | author block, only read in non-anonymous builds (do not upload with anonymous sources) |
| `macros.tex` | notation conventions; one concept, one macro; `\ev{E12}` evidence tags |
| `sections/*.tex` | abstract, intro, overview, prelim, construction, security, experiments, related, optional conclusion/appendix/comparison table |
| `refs.bib` | sample entries in house style (maintained by `cpw-lit`) |
| `Makefile` | `make` (submission), `make camera`, `make full`, `make check`, `make anon`, `make clean` |
| `fetch_llncs.sh` | uses the TeX installation's `llncs.cls`/`splncs04.bst`, otherwise downloads the official package from CTAN; the class is never committed |

## Build

```bash
make            # latexmk -pdf main.tex (fetches llncs.cls if the TeX tree lacks it)
make audit      # linked literal values/units, reachable TeX files, ledger + log paths
make check      # pdf_checks.py: page map, undefined refs, overfull boxes, fonts, overlap
make anon       # anon_check.py on sections/, refs.bib, macros.tex and the PDF
                # (put a private deny-list in .denylist.txt; it is git-ignored)
```

Run these build commands from `paper/`. Toolkit scripts are under
`../.paper-writing/`; `TOOLKIT_ROOT`, `EVIDENCE`, and `PROJECT_ROOT` can be
overridden for an existing layout. The bibliography used by this skeleton is
`paper/refs.bib` from the project root.

Annotate reported quantities as `1.23 s\ev{E1}`, or put `% EV:E1,E2` on the
same line as the corresponding values. `make audit` follows literal
`\input`/`\include`, including generated tables, and validates log-file paths.
It does not expand TeX macros or check numbers inside graphics, table-heading
units, claim scope, log contents, or the arithmetic of derived values. Review
those separately. Details: `../.paper-writing/docs/evidence-audit.md`.

Anonymity defaults in `main.tex`: empty PDF metadata via `\hypersetup`, and
`\pdfsuppressptexinfo=-1` so included figures do not embed their absolute source
paths (which can contain usernames).

## Rules

- Do not add `geometry`, change fonts, font sizes or line spacing (desk-reject risk).
- Add `a4paper` to the class options if the CFP requires A4.
- Tables and figures that carry numbers are generated into `tables/` from data files
  referenced in `EVIDENCE.md`.
- The input order is a starting outline. Merge the overview into the introduction
  or place it after necessary definitions; put detailed related work early or
  late. Omit evaluation when there are no experimental claims. Conclusion and
  appendix inputs start commented out; enable them when useful and allowed by
  the venue. Update labels and references when reorganizing the manuscript.
- The prompts describe content to supply; they do not assert results. Read the
  relevant section guide before filling them. For a new paper, study useful
  related papers and record the resulting writing plan in `STATE.md`; later edits
  reuse those choices along with the author's instructions and current conventions.

## IACR journals (TCHES, ToSC) and other formats

- **TCHES / ToSC** use the IACR journal class. At the time of writing the IACR
  publishes `iacrj` (https://publish.iacr.org/iacrj), which superseded the older
  `iacrtrans` class; check the current call for papers for which class is accepted.
  Typical usage: `\documentclass[journal=tches,submission]{iacrj}` (or
  `journal=tosc`); the `submission` option anonymises and adds line numbers. Use
  `\[...\]` rather than `$$...$$` (breaks line numbering). Captions: figures below,
  tables above. Bibliography style and source (e.g. CryptoBib/DBLP) follow the class
  documentation. Do not vendor the class; fetch it from the IACR site or CTAN in the
  same way as `fetch_llncs.sh`.
- ToSC counts material that must be carefully reviewed (e.g. proofs) toward the page
  limit even in appendices; TCHES/ToSC decisions can be "major revision", so keep the
  paper easy to patch (single-source tables, EVIDENCE tags).
- **ACM CCS** uses `acmart` (`sigconf`, `anonymous,review` options); **IEEE S&P / NDSS**
  use IEEE two-column templates; **USENIX Security** uses the USENIX template;
  **PoPETs** uses its own template. The playbook's section moves still apply, but
  the page budget changes (see `.paper-writing/skills/venue-calibration` from the project root). Section files can be
  reused; replace `main.tex` with the venue's driver.
