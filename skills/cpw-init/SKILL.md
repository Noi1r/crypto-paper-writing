---
name: cpw-init
description: Initialize or orient a crypto-paper-writing paper project from the locally installed toolkit, preserving existing files and recording its materials, paths and next writing tasks.
---

# Set up a paper project

Use the current paper project unless the user specifies a target. Read existing
`STATE.md` and project guidance when they exist. The paper project's reusable
toolkit is in `.paper-writing/`.

If the project has no toolkit yet, resolve the path of this `SKILL.md`, following
symlinks. Its toolkit root is three directories above the file: it contains
`skills/cpw-init/SKILL.md`, `install.sh`, and `templates/`. Confirm those resources
exist and run that root's `install.sh` with the intended paper-project directory.
For a source checkout that itself is the current directory, obtain the separate
paper-project location instead of initializing a manuscript inside the toolkit.
If the full toolkit is unavailable, report the missing resource rather than
inventing an installation path. Do not use `--user` when preparing a paper project.

Copy missing records from `.paper-writing/templates/blackboard/`. If `paper/` is
empty, copy `.paper-writing/templates/paper/` into it. Preserve existing work,
including guidance, references and the manuscript's own layout.

Ask only for paper-specific facts that remain necessary: the research question,
known results, target venue, deadline and source locations. Record the actual
manuscript/bibliography paths and build commands in `STATE.md`.

For a new manuscript, include selecting and reading suitable papers before
choosing its organization and exposition, following
`.paper-writing/skills/cpw-write/references/writing-from-related-work.md`.
Record a concise writing plan and the venue-rule verification task in `STATE.md`.
Link existing reference analysis for reuse. Initialization alone does not require
writing the manuscript or executing new experiments.
