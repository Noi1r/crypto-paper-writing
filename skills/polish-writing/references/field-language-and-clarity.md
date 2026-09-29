# Field language and clear exposition

Use this guide when drafting or revising prose that sounds unnatural, uses
unfamiliar terminology without need, or makes a sound idea difficult to follow.
The examples below are synthetic. Apply their decisions to the actual meaning
of the passage; they are not replacement sentences for a real paper.

## Choose words by their job

For a technical concept, use the term that matches the definition and the usage
in the relevant subfield. Check a doubtful term against the selected reference
sections or an authoritative definition. A word can have different meanings
across cryptographic subfields, so match the object and context as well as the
word. Reuse an established term consistently instead of alternating synonyms.

For ordinary explanation, prefer the familiar expression that states the action
accurately. Words such as "use", "compute", "send" and "check" often do the job
directly. A more specialized verb is appropriate when it communicates a genuine
distinction. New concepts may need new names; introduce and define them instead
of treating an invented label as familiar terminology.

If several choices recur, keep a short terminology note in the existing writing
plan or notation notes: the concept, chosen term, relevant source usage and any
distinction from nearby terms. A new glossary file is not a prerequisite for an
edit. Reuse resolved choices; look up a term again only for a concrete uncertainty.

## Recognize unhelpful phrasing

- Empty praise or emphasis: a claim of importance, power or elegance without the
  result that would explain it. State that result when supported, or remove the
  emphasis.
- Abstract noun chains: several nouns hide who performs the operation. Name the
  actor and use a verb where this makes the sentence clearer.
- Decorative terminology: a metaphor or compound label replaces a familiar
  object without adding a useful distinction. Prefer the established name.
- Repeated framing: sentences keep announcing what will be explained or end by
  praising a point already made. Keep signposts when they help navigation.
- Forced variation: synonyms make one object appear to be several objects, or
  repeated opening formulas make all paragraphs sound alike. Follow the local
  argument; do not impose a replacement pattern on every paragraph.

Review phrases such as "leverage", "facilitate", "seamless" and "powerful" in
context. They are prompts to look for a more concrete statement, not a blacklist.
Likewise, "robustness", "extraction" and "efficiency" can denote real technical
properties. Preserve their defined meanings.

## Reduce the reader's effort

Work from what the intended reader knows at this point in the paper. Explain
specialized machinery needed for the new idea, without repeatedly teaching
background already established. Introduce symbols close to their first use and
explain what a displayed relation contributes to the argument when that is unclear.

Make the subject and main action easy to find. Unpack compressed noun phrases,
resolve ambiguous pronouns and separate distinct reasoning steps when nesting
obscures their dependencies. Keep closely related conditions and conclusions
together when splitting them would make the argument harder to follow.

Supply a missing explanatory connection from the existing technical material.
If the material does not establish it, flag the gap rather than invent a cause,
proof step or mechanism. A well-placed example or short intuitive explanation can
help; neither is required in every paragraph.

Clarity is compatible with precise terminology and complete assumptions. A short
sentence that omits the security model or comparison condition can be less useful
than a longer sentence that states the result accurately.

## Synthetic revisions

### Replace abstract phrasing with an explicit action

Original: "The verifier leverages the commitment to facilitate the validation
of the prover's response."

Revision: "The verifier uses the commitment to check the prover's response."

This preserves the objects and action without adding an unsupported property.
If the context requires a specific check, explain that check from the protocol.

### Separate reasoning while keeping its condition

Original: "When the public index remains unchanged, its reuse across requests
eliminates repeated index construction while preserving the per-request checks."

Possible revision: "When the public index remains unchanged, requests can reuse
it. This avoids rebuilding the index for each request. The per-request checks
remain unchanged."

The shorter version can help if the original sentence interrupts a longer
argument. The original is also acceptable if its relationships are already easy
to follow. Neither wording establishes an end-to-end speedup.

### Explain a familiar technical term when needed

Retain "witness" for the object defined as a witness in the relation. In an
introductory passage for readers who need the context, explain the role, for
example "a witness w satisfying R(x, w) = 1 for the public input x". Substituting
"evidence" merely for variety can blur the connection to the formal definition.

## Finish the revision

Check the few phrases most likely to trouble the intended reader: unexpected
terms, vague objects, hidden actors, compressed conditions and unexplained jumps.
Then compare the revised passage with the source for assumptions, claim strength,
notation and numbers. Report unresolved ambiguities concisely. Naturalness does
not require adding informality, removing technical detail or varying wording
that already works.
