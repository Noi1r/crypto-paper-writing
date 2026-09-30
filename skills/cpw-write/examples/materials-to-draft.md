# Synthetic example: from materials to a technical overview

This is an invented case for practicing the writing workflow. The supplied
results are premises of the example, not claims about a real proof system.
No measurement or literature novelty is asserted. The paragraph count and
starting section are choices for this case.

## Request and unordered materials

The author asks for a technical overview for cryptography researchers who know
what a verifier does but have not seen this implementation.

The available notes say:

- The baseline constructs a public lookup index before each verification request.
  The index is a deterministic function of public parameters K. The statement
  and proof can differ between requests using the same K.
- Verification reads this index without changing it. Both index construction
  and verification are deterministic in this example.
- The proposed implementation constructs the index once for a batch using the
  same K. It still runs the complete verification procedure for every request.
  A change in K requires constructing the corresponding index.
- A supplied lemma establishes identical acceptance
  decisions when each request receives the same index and other inputs as in
  the baseline. It is not a new cryptographic security theorem.
- In an operation-count model, index construction costs A and each verification
  costs V. For b requests with fixed K, the two model costs are b(A+V) and A+bV.
  Cache lookup and dispatch overhead are excluded from this model.
- Keeping the index between requests requires storage. Neither elapsed time nor
  peak memory has been measured.
- The notes establish no claim about how this approach compares with the wider
  literature.

These materials support drafting the mechanism and its modelled cost. No additional
experiment or literature claim is needed to explain this supplied example.

## Main argument and supporting roles

Recommended emphasis: explain how fixed public parameters permit repeated setup
to be shared while preserving each request's verification decision. The reuse
mechanism is the organizing idea, the lemma justifies the unchanged decisions,
and the operation counts express the resulting saving within the specified model.
Measured performance remains outside the available results.

This framing connects the notes without turning every note into a separate
contribution or treating an operation count as a runtime result.

## Explanation sequence

1. Establish what preparation is repeated and why requests can share it.
2. Explain the implementation change and the condition that preserves each
   verification decision.
3. Quantify the saved preparation in the given model and state the rebuild and
   storage requirements.

This sequence is enough to start writing. It introduces the cost symbols only
after the reader understands the work they count.

## Complete first draft

> In the verifier considered here, each request begins by constructing a public
> lookup index from the parameter set K. The statement and proof may change
> between requests, but index construction depends only on K. Requests sharing
> the same parameters therefore repeat the construction of an identical index.
> This repeated preparation motivates separating index construction from the
> verification performed for each request.
>
> We construct the index once for a batch whose requests share K and make it
> available to each verification. Every request still executes the complete
> verification procedure with its own statement and proof. Because the index is
> deterministic and verification does not modify it, each request receives the
> same index and other inputs as in the baseline. The lemma therefore applies:
> reuse leaves that request's acceptance decision unchanged.
>
> Let A be the cost of constructing the index and V the cost of verifying one
> request in the operation-count model. Counting these two operations, processing
> b requests separately costs b(A+V), whereas reuse costs A+bV. The saving is
> (b-1)A, so a batch of one request has no saving in this model. Cache lookup and
> dispatch overhead are outside these counts.
>
> Reuse requires the index to remain available between requests. When the public
> parameters change, the verifier constructs the corresponding index before
> using it. The cost model describes the avoided construction work; elapsed time
> and peak memory remain to be evaluated.

The draft explains the reason for reuse, its validity condition and the cost
boundary. It makes no inference about practical speedup from the model counts.

## Example author feedback

Suppose the author asks:

> Keep the technical overview focused on where the repeated work comes from and
> why reuse is valid. Put the detailed cost formula in Evaluation. Keep the
> condition for rebuilding the index explicit.

This changes the distribution of explanation across sections. The substantive
result and the conditions for reuse stay the same.

## Complete revision responding to that feedback

> In the verifier considered here, each request begins by constructing a public
> lookup index from the parameter set K. Although the statement and proof may
> differ between requests, index construction depends only on K. Requests sharing
> the same parameters therefore repeat identical preparation.
>
> We construct the index once for such a batch and reuse it while verifying each
> request. Every request still runs the complete verification procedure with its
> own statement and proof. Index construction is deterministic, and verification
> only reads the index. Each request therefore receives the same inputs as in
> the baseline. The lemma applies under this condition, so sharing the preparation
> leaves its acceptance decision unchanged.
>
> The index must remain available between requests. If the public parameters
> change, the verifier constructs the corresponding index before use. This
> separates the work shared by the batch from the verification required for each
> request. The cost analysis counts these two operations separately.

Carry the author's decision into the rest of the draft:

- Place the detailed count and its exclusions in Evaluation.
- Keep the parameter-change rule explicit in the construction.
- Describe any abstract or introduction result within the operation-count model
  until elapsed-time evidence is available.

These are composition decisions for this hypothetical paper. They do not require
all technical overviews to omit formulas.

## Checks for the exercise

Both versions preserve reuse under fixed parameters, verification of every request
and the condition for unchanged decisions. The first version gives the supplied model costs;
the revision moves their detailed presentation according to the hypothetical
feedback. Neither version invents a benchmark, a novelty comparison or an extended
security guarantee.

The exercise illustrates the requested deliverables and how feedback propagates.
It does not independently establish that the guide improves writing quality;
that judgment needs use on representative material and author feedback.
