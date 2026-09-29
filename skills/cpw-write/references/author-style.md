# Learn an author's writing preferences

Use this procedure when the author asks to derive or refine a style profile from
previous writing. For the default new-paper workflow, use
[writing from relevant papers](writing-from-related-work.md)
instead. A personal profile is a separate optional artifact and does not block
drafting or polishing.

## Select useful samples

Start with a small set of papers or passages the author considers representative;
two or three papers often provide a practical first comparison. Prefer the final
author manuscript when available. For coauthored papers, ask which passages the
author wrote or particularly likes if that affects the inference.

Choose samples relevant to the intended task: abstracts for abstract style,
technical overviews for explaining ideas, protocol or proof passages for formal
exposition, and evaluation passages for discussing results. Compare like sections
before deciding whether a preference applies more broadly. The source paper's
template, topic, collaborators and editing history may explain a local pattern.

Use author-provided files or authorized source locations. For an ePrint reference,
use its canonical page for identity and metadata and follow the user's configured
full-text access workflow. Keep manuscript text and source-specific notes in the
paper project. This reusable toolkit stores synthetic examples and generic
procedures only.

## Infer useful decisions

Look for choices that would change a future revision:

| Dimension | What to examine |
|---|---|
| Information order | Whether a paragraph leads with its result, goal, definition or motivating obstacle, and in which contexts |
| Level of explanation | How intuition connects to formal statements, and how much background the reader is assumed to know |
| Technical density | When notation, displayed equations, examples or cross-references are introduced |
| Paragraph development | How reasons, mechanisms, evidence and scope follow the central point |
| Language | Preferred terminology, transitions, voice, punctuation and spelling conventions |
| Presentation | Use of headings, lists, theorem references and table or figure discussion |

Record a candidate preference with a source location, its applicable context and
any counterexamples in the selected samples. A pattern in one paper may be a
local choice. Frequent wording alone does not establish an author preference.
Do not copy sentence sequences or infer a preferred research contribution from
the samples. Assumptions, theorem strength and causal attribution are matters of
technical correctness, not style settings.

For example, a synthetic observation might suggest that result paragraphs often
state the observation before explaining it. The useful candidate is: "For
evaluation results, lead with the observation when the setup has already been
introduced." This does not require every paragraph to begin with a conclusion.

## Calibrate on a fresh passage

Apply the candidate profile to a short passage not used to derive it, keeping its
technical content fixed. Show the revision and explain the few stylistic choices
that matter. The author's feedback is stronger evidence than a frequency count.
Refine or drop candidates that make the new passage less clear or do not match
the author's intent. A single successful trial is a starting point, not evidence
that the profile generalizes to every paper type.

## Store and use the profile

Use the optional `.paper-writing/templates/style/STYLE.md` template to create
`STYLE.md` in the paper project when needed. Keep it short enough to guide an
edit: adopted preferences, their scope, candidate observations and source pointers.
Do not label inferred preferences as adopted without supporting author feedback
or an explicit instruction already present in the task.

Apply adopted preferences when they fit the passage. Current author instructions,
technical meaning and required venue formatting govern conflicts. Keep a
project-specific convention local unless the author asks to reuse it elsewhere.
Update an adopted preference when the author changes it; retain only the source
detail needed to understand that decision.
