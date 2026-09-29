# Specification

`crypto-paper-writing` contains reusable *methods and templates*. The paper
project holds all paper-specific content.

## Boundary

- Included: literature/citation preparation, section writing, figures, evidence
  audit, review, rebuttal, anonymisation, artifact description, and final checks.
- Excluded: research ideation, proof development, baseline implementation,
  benchmark execution, toy cryptographic algorithms, and research-phase gates.
- Keep only public references and synthetic examples in this repository. Do not
  commit copied PDFs, harvested figures, unpublished manuscripts, reviews, real
  result logs, private personal data, email addresses, or machine identifiers.

## Paper project files

`STATE.md` tracks the writing status and outstanding work. `CLAIMS.md` holds each
claim's exact supported wording and support. `EVIDENCE.md` maps printed numbers
to commands, logs, configurations, and dates. `LITERATURE.md` records related
works and citation checks. `THEORY.md` is an optional pointer to proof sources;
the writing toolkit does not certify proofs. `REVIEWS.md`, `SUBMISSION.md`, and
`DECISIONS.md` record review actions and author decisions.

No claim is strengthened by editorial polishing. No measured number is copied
into `paper/` without an `EVIDENCE.md` row. BibTeX entries stay only after
verification. The author approves submissions and releases.

## Tooling

`scripts/audit_tex.py` imports the standalone `papercheck/evidence.py` ledger
reader and scans LaTeX numbers. It is a traceability aid: it cannot prove a
measurement is correct, detect every unsupported statement, or replace source
review. The `paper/Makefile` runs it on each section.

The LNCS class is fetched from the user's TeX installation or its official
distribution by `templates/paper/fetch_llncs.sh`; the class is not vendored.
The figure examples use synthetic data. Harvested figures stay local.
