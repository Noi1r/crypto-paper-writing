# Main technical content

Present the actual protocol, construction, algorithm or theoretical result in an
order that makes its dependencies clear. Open each section by identifying what it
delivers and why the reader needs it.

## Choose the development

For a protocol, explain the intended task or relation, participants and inputs,
message or state transitions, and outputs. For an algorithm, explain its goal,
inputs, key steps and result. For a theorem, state the objects, assumptions and
conclusion precisely before or alongside the argument that establishes it.

The formal statement may precede a construction when it helps orient readers,
or follow definitions that are needed to understand it. Place correctness,
security or cost analysis with the relevant component or in a dedicated section
according to the dependency and length of the argument.

Provide the rationale actually supporting a design choice: a theorem, analytic
tradeoff, experiment, search result or explicit design constraint. Do not imply
that an enumeration or optimality argument was performed when it was not.

Use algorithms, examples and diagrams when they expose a step more clearly than
prose alone. Explain all hypotheses and maintain the distinction between
sufficient and necessary conditions. Identify the metric and regime of each cost
claim; several metrics may be needed to express a real tradeoff.

## Check

Can the reader determine exactly what is defined or executed? Does each claim
have the assumptions and support it needs? Are the statements, notation and
implementation scope consistent across the relevant parts of the paper?
