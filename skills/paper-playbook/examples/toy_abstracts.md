# Synthetic abstract examples

All objects, results and measurements below are invented for writing practice.
The different paragraph structures serve these particular examples. Choose a
new paper's structure from its content and venue requirements.

## A theoretical result in one paragraph

> A toy relation may admit several encodings of the same witness, making it
> difficult to compare the statements checked by different implementations. We
> give a canonical encoding for a restricted class of these relations and prove
> that decoding preserves witness validity under the stated domain conditions.
> The construction isolates the domain condition needed by the proof and gives
> a counterexample when that condition is removed.

The result and its boundary are the substance of this abstract. An implementation
or performance sentence would require additional results.

## An empirical result in two paragraphs

> Small independent requests incur repeated setup costs in a toy evaluator. We
> study batching these requests when the setup can be shared, and give an
> implementation that keeps the per-request computation unchanged.
>
> On eight synthetic workloads, the batched implementation has 1.4–1.8× the
> baseline throughput and uses 1.2× its memory. These measurements concern the
> evaluator after input preparation. For single-request latency, the same
> implementation provides no improvement.

The second paragraph groups the measured result with its measurement boundary
and tradeoff. Its placement follows the content rather than a sentence quota.

## A protocol result with a specific tradeoff

> In a toy private-matching setting, preprocessing a fixed public index can
> reduce repeated local sorting work. We describe a protocol variant using this
> index and establish its stated privacy property in the semi-honest model.
> The variant reduces the local sorting cost while preserving the original
> communication bound; it requires the public index to remain fixed across runs.

The last condition qualifies the contribution and belongs with the result.
Nothing in this example supplies claims for an actual private-matching protocol.

## Revision exercise

Vague: “Our method is efficient and provides strong guarantees.”

A useful revision must identify the actual result and its assumptions from the
paper. It might report a measured throughput change or a proved property, but
those are different claims. Obtain the supporting material before choosing one.
