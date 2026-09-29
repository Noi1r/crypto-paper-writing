# Security, correctness and analysis

Explain which properties the paper establishes, in which model, and with what
support. Select the applicable material from the paper's actual claims.

## Formal properties

State the relevant experiment, adversarial powers, assumptions, quantifiers,
probability space and bound. For correctness, make the input domain and failure
conditions explicit. Connect the argument to the construction as specified.
Identify which statements have complete proofs, sketches or unresolved gaps.

When the paper uses a proof system, distinguish the encoded relation and its
security guarantee from the application's intended property where they differ.
A successful implementation run or accepted proof alone does not establish that
the intended relation was encoded correctly.

## Concrete estimates or empirical support

If reporting a security estimate, identify its model, tool or source, version,
parameters and relevant limitations. Distinguish an attack-cost estimate from a
formal reduction and from the absence of a successful attack in an experiment.
For compared parameter sets, explain the security convention being matched.

Report noise, failure probabilities, success rates or related measurements when
they support the actual claim, with their distributional assumptions and scope.
A parameter change needs analysis of the properties it affects; performance
improvement alone is not evidence of preserved security.

## Open issues and placement

State a known limitation and its effect on the claim plainly. Describe a repair
or alternative only when its properties are supported. Organize proofs locally
or in a dedicated section, with detailed material in an appendix where the
venue allows it and precise pointers from the main statements.
