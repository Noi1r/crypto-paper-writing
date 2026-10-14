# Main technical content

Present the protocol, construction, algorithm, or theorem development in an
order that respects logical dependencies. Open each section or subsection by
stating in one or two sentences what component it builds and how that component
fits into the overall architecture.

## Structure the exposition for clarity

- **Specify inputs, state, and outputs explicitly:** For a protocol, identify the
  participants, public parameters, private inputs, round-by-round message flow,
  and acceptance/output rules. For an algorithm, state its goal, inputs, core
  loop or algebraic steps, and output guarantee. For a theorem-led section, state
  all objects, hypotheses, and the exact conclusion before or alongside the proof.
- **Separate inherited machinery from your modification:** When extending or
  modifying an existing scheme, briefly recall the baseline steps the reader
  needs and explicitly mark where your construction changes the representation,
  message flow, or verification check. Do not force the reader to diff your
  protocol against an external paper from memory.
- **Make trust and verification boundaries unmistakable:** In verifier-facing
  or interactive steps, state clearly which values come from a trusted setup or
  accepted state, which values arrive from an untrusted party, what the verifier
  recomputes locally, and what exact equation triggers acceptance or abort. If a
  check is deferred or batched, state what is committed now and what is checked
  later.
- **Introduce optimization machinery after the base computation:** First state
  *what* quantity is being computed and *why*; only then introduce the algebraic
  packing, hoisting, or amortization trick that speeds it up. Show the key
  invariant or update equation that makes the optimization valid.
- **Ground design rationales in actual support:** Justify parameter choices or
  protocol steps using the theorem, analytical trade-off, search result, or
  system constraint that actually determined them—never imply an exhaustive
  optimality proof if the choice was heuristic or pragmatic.
- **Count complete costs:** When stating complexity or communication bounds in a
  technical section, specify the exact metric and regime, including output size,
  evaluation keys, or auxiliary transcripts when they belong to the step.

## Check

- Could an expert implement or verify the construction from your specification
  without guessing omitted indices, domains, or abort conditions?
- Is the boundary between recalled baseline steps and new technical steps explicit?
- Are notation, parameter constraints, and claim strength consistent between the
  prose, protocol boxes, and formal theorems?
