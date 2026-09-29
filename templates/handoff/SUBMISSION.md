# SUBMISSION — <venue> <year>

## Venue rules (quoted from the CFP; URL + date read)

- CFP URL: <...>  ·  read on: <date>  ·  re-checked on: <date>
- Template/class: <...>  ·  paper size: <A4/letter>  ·  page numbers: <required?>
- Page limit: <N> pages; counts: <quote exactly: e.g. "excluding references" / "excluding the bibliography only">
- Supplementary material: <allowed? size cap? reviewers obliged to read? >
- Anonymity policy: <quote>  ·  self-citation rule: <third person?>
- Deadline: <date time AoE/UTC> = <local time>
- Rebuttal window: <dates>  ·  budget: <words/characters>
- Camera-ready: <deadline, page rule, forms>

## A. Format (desk-reject items)
- [ ] correct class, no geometry/font/spacing changes (`pdf_checks.py` width ≈ expected)
- [ ] body within limit as the CFP counts it (`pdf_checks.py --limit N`): body ends p.__, references start p.__
- [ ] page numbers present if required; paper size as required
- [ ] no overprinting (overlap scan), title+abstract+keywords on page 1 (if desired)
- [ ] all fonts embedded (`pdffonts`)

## B. Anonymity
- [ ] `anon_check.py` on sources, PDF, supplementary zip, artifact: HIGH=0 (paste summary line)
- [ ] PDF metadata empty; no embedded source paths
- [ ] self-citations in third person; no acknowledgements/funding
- [ ] anonymous mirror refreshed after last push; each file URL returns 200
- [ ] artifact README has no "our previous paper / same codebase" wording; no `.git`

## C. Content consistency
- [ ] 0 undefined references / citations; no `<<` placeholders; no `\todo`
- [ ] source audit completed with no errors; record the command and report
- [ ] separately review table-heading units, macro-generated and graphic numbers, derived computations, and each number's claim scope against its evidence
- [ ] abstract, contributions and any conclusion agree in claim scope, terminology and repeated numbers
- [ ] overview formulas agree with the body; any simplifications are explicit
- [ ] scope sentences match the security/parameter tables
- [ ] every contribution maps to a CLAIMS row with status survived/weakened
- [ ] main text explains the principal results, assumptions and ideas, with accessible proof pointers and appendix placement allowed by the venue

## D. References
- [ ] every entry verified by cpw-lit (DOI / ePrint page); published versions preferred
- [ ] acronyms braced; no publisher-export clutter; `--` page ranges
- [ ] bibliography count and order checked after the final compile

## E. Submission form
- [ ] plain-text abstract from `abstract_plain.txt` (not copied from PDF)
- [ ] topics / areas selected
- [ ] conflicts of interest per the venue's rules (advisor, same institution recently, frequent co-authors, family); being cited is not a conflict
- [ ] all authors, e-mails, affiliations, ORCIDs entered (not visible to reviewers)
- [ ] supplementary within size cap
- [ ] "ready for review" / final submit flag set

## F. Upload verification
- [ ] downloaded PDF sha256 == local: <hash>
- [ ] downloaded supplementary sha256 == local: <hash>
- [ ] last-24-hours rule: only error fixes; checklists A–C rerun after each fix

## Log
| time (UTC) | action | result |
|---|---|---|
