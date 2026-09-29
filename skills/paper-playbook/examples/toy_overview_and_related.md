# Synthetic overview and comparison examples

The mechanisms and results here are invented for exposition. The examples show
how an explanatory choice depends on the result being discussed.

## An overview organized around one observation

> The repeated setup cost comes from rebuilding the same public lookup index for
> every request. Once this index is constructed, each request can read it without
> modifying it. We therefore keep the index across a batch and account separately
> for its construction and use. This change can amortize setup across the batch;
> it does not remove the per-request work or improve the single-request case.

One observation is enough for this example. A diagram is optional because the
state relationship can be described briefly in words.

## An overview organized by dependent proof steps

> We first show that decoding the canonical representation preserves the relation
> on the restricted domain. We then use this property to compare verification
> on the original and canonical encodings. The second argument depends on the
> domain condition in the first; outside that domain the correspondence fails.

Here a dependency gives the reader a useful order. The explanation can refer to
formal lemmas in the body without reproducing their full proofs.

## Related work under different conditions

> Method A prepares each request independently and supports changing the public
> index between requests. Method B reuses a fixed index and reduces repeated
> setup work. Our toy evaluator studies the latter workload. The results do not
> establish which method is preferable when the index changes frequently.

A comparison table would help if there were enough distinct methods and matched
metrics to compare. These few relationships can be explained directly.
