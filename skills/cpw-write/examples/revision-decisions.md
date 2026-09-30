# Synthetic revision decisions

These miniature cases illustrate writing choices. Their technical premises and
numbers are synthetic. In a real manuscript, establish the premises from its
sources before using a similar explanation.

## Give adjacent paragraphs different jobs

Suppose a draft has an "Our goal" paragraph saying that the work reduces proof
communication, followed by a "This work" paragraph repeating that objective.
If the first adds no problem constraint or research question, combine them and
use the space to explain the method. If it introduces a distinct requirement,
keep that requirement where it prepares the contribution.

The decision concerns the paragraphs' content. Neither heading is universally
required or forbidden.

## Keep background that explains different parts of the problem

Suppose a synthetic paper studies private collection of aggregate measurements
from intermittently connected participants. Its introduction contains:

> Aggregate measurements help an operator plan shared resources without needing
> every participant's individual reading. A private collection protocol aims to
> provide the group result while limiting what the operator learns about any one
> contribution.

> Participants may disconnect after sending their measurements. A protocol that
> requires everyone to remain online for a final round can leave an entire batch
> unfinished. This availability constraint motivates collection protocols that
> can complete when some participants are absent.

A compressed alternative says:

> This work studies private collection of aggregate measurements for networks
> with intermittent participants.

The alternative is accurate but drops the reasons for aggregation and for the
availability requirement. The original paragraphs answer different questions:
why the group result is useful, and why a final interactive round poses a problem.
For a polishing request, keep both paragraphs and improve local wording only
where there is a concrete benefit. Leaving them unchanged is also appropriate.

If the author needs a shorter introduction, propose cuts against that constraint
while preserving those explanatory connections; two paragraphs are not mandatory.
This differs from the preceding case, where adjacent passages repeat the same
objective without adding a requirement or reason.

## Explain a quantity before introducing its optimization

Premise: a toy computation sums contributions from candidates; candidates in
the same class have identical contributions.

Unhelpful opening: "We compute the multiplicities of all classes."

Possible revision: "Candidates in the same class contribute the same value to
the sum. We evaluate that value once and multiply it by the number of candidates
in the class."

Now the reader knows why the class count is needed. Formal class notation can
follow if it is useful in the algorithm or analysis.

## Select background through its later use

Suppose a paper replaces a compression step within a larger authenticated format.
Readers need the component's input and output, its authentication requirements
and the surrounding costs used in the comparison. A tutorial on every format
field would distract from that task.

Keep field encodings when an ambiguity affects the definition or argument.
Otherwise, define the concise notation used later and refer to the format's
specification for the remaining details. State changes to the format in the new
construction so readers can distinguish inherited behavior from the modification.

## Make an analytical contribution specific

Premise: one bound treats requests as independent; a new recurrence explicitly
tracks repeated selection of the same item.

Vague: "Our refined analysis yields a tighter bound."

Possible revision: "The recurrence records whether requests select the same
item, accounting for dependencies omitted by the independent-request bound."

If the paper establishes a tighter bound, state that result with its conditions.
The explanation supplies the mechanism; the source must supply the conclusion.

## Consolidate conventions without losing conditions

Suppose both a section opening and the paragraph after an equation explain that
the outer instance index is fixed while inner indices remain explicit.

Give the convention once before the first equation that uses it. Remove the
later duplicate. If another section needs the distinction to interpret a claim,
include a short reminder or reference there. This preserves the condition while
avoiding repeated definitions.

## Explain a component saving in the complete result

Premise: the fixed surrounding material occupies 800 bytes, and a component
shrinks from 400 to 200 bytes.

Possible revision: "The component size falls by 50%. The complete object shrinks
from 1,200 to 1,000 bytes, a 16.7% reduction, because the other 800 bytes are fixed."

If an operation-count model also improves, label it as a model result. These byte
counts do not establish an elapsed-time speedup.

Suppose the selected configuration disables batching. Its improvement cannot
establish a benefit from batching. Describe the supported parameter-point result,
or use an existing controlled comparison that actually isolates batching.

## Choose the source that supports the fact

Suppose an implementation paper uses parameter sets defined in a standard.
Introduce those sets as standard parameters and cite the standard. Attribute
the implementation paper's timings to that paper, with its measurement conditions.

For related work, distinguish a construction from one analysis of it. If a bound
omits a particular dependency, identify the bound and setting. Do not infer that
the entire construction lacks the corresponding feature.
