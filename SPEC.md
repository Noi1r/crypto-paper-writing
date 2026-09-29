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

`STATE.md` tracks the writing status, selected writing references, paper-specific
plan and outstanding work. It can link existing planning notes. `CLAIMS.md` holds each
claim's exact supported wording and support. `EVIDENCE.md` maps printed numbers
to commands, logs, configurations, and dates. `LITERATURE.md` records related
works and citation checks. The default bibliography is `paper/refs.bib`; record
different manuscript and bibliography paths in `STATE.md` for existing projects.
Installed toolkit resources are addressed through `.paper-writing/`, independently
of similarly named project directories. `THEORY.md` is an optional pointer to proof sources;
the writing toolkit does not certify proofs. `REVIEWS.md`, `SUBMISSION.md`, and
`DECISIONS.md` record review actions and author decisions.

For a new paper or major reorganization, establish its actual results, study
relevant papers' content coverage, organization and exposition, and then propose
a writing plan suited to the work. The closest technical paper and a useful
writing example may differ. Reuse this analysis for later section edits; a local
polishing task does not trigger a new literature search.

`STYLE.md` is a separate optional personal profile created only at the author's
request. It can record adopted preferences and candidate observations. The
toolkit contains generic procedures and a blank template, with no private
manuscripts or personal style corpus.

Writing guidance supplies section goals, decision criteria and an adaptable
whole-paper outline. Section and paragraph counts follow the actual content;
templates must not pre-fill technical conclusions or required contribution types.
Drafting and polishing use terminology appropriate to the relevant subfield and
plain, concrete explanations. Readability improvements preserve technical names,
assumptions and claim strength; neither a blanket word blacklist nor a fixed
sentence length defines the writing style.

No claim is strengthened by editorial polishing. No measured number is copied
into `paper/` without an `EVIDENCE.md` row. BibTeX entries stay only after
verification. The author approves submissions and releases.

## Tooling

`install.sh --user` registers the checkout's skills in the user's local skill
directory through symlinks, preserving existing entries. The checkout remains
the source of those skills. `cpw-init` can locate that full toolkit through its
resolved skill path and install project assets into the requested paper directory.

The installer registers project-local Codex skills under `.agents/skills/`, using
links to `.paper-writing/skills/`. The `cpw-*` entry skills cover initialization,
literature, writing, figures, review, rebuttal and submission preparation. Their
frontmatter uses skill metadata; tool availability and model selection remain
with the current Codex session. Supporting procedures can also be invoked as
skills. User-owned skill entries and existing project files are preserved.

Reinstallation fills missing resources and removes only links recognized as
having been created by the old installer. It does not overwrite local edits to
the installed toolkit or remove unrelated configuration.

`scripts/audit_tex.py` imports the standalone `papercheck/evidence.py` ledger
reader and scans literal LaTeX quantities linked by `\ev{ID}` or `% EV:ID`.
The default check validates ledger fields, log-file existence and acyclic derived
references, and follows literal `\input`/`\include` dependencies from the entry
source. Recognized values and visible units must match the linked evidence rows.
Missing inputs and incomplete ignore blocks are errors.

It is a traceability aid: it cannot prove a measurement is correct, recompute a
derived expression, expand arbitrary TeX macros, inspect numbers rendered inside
graphics, infer units from table headings, or verify claim scope. Conditional
branches are scanned conservatively. See `docs/evidence-audit.md` for its syntax
and limits; the paper project's `make audit` invokes this check.

The LNCS class is fetched from the user's TeX installation or its official
distribution by `templates/paper/fetch_llncs.sh`; the class is not vendored.
The figure examples use synthetic data. Harvested figures stay local.
