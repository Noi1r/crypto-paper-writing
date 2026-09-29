# Synthetic introduction and contribution examples

These examples illustrate choices for invented work. Their claims are local to
the examples; they do not prescribe contribution counts, order or research goals.

## One central result expressed in prose

> Different encodings of a toy relation can obscure which inputs a verifier
> accepts. Our contribution is a canonical encoding for the restricted domain
> defined in Section 2. Theorem 1 establishes preservation of witness validity.
> The domain restriction is essential: the example following the theorem shows
> why the construction does not extend to arbitrary encodings.

This paragraph names the result, points to its support and states a necessary
boundary. A theorem reference helps the reader locate the precise statement.

## Distinct outcomes expressed as a list

For an invented evaluator study, a short list can distinguish the mechanism from
the empirical result:

- We describe a batching implementation that shares request setup while keeping
  the per-request computation unchanged.
- We measure its throughput and memory tradeoff on the specified workloads,
  including cases where batching gives no latency benefit.

The list separates different kinds of support. A paper with further independent
results may need more items; one with a single result may need no list.

## Positioning a result in the introduction

> Existing toy evaluators prepare each request independently. This is appropriate
> when requests use unrelated setup data. Our workload contains repeated requests
> sharing that data, which motivates examining the setup cost separately. We
> evaluate a batched variant under this workload and report the resulting
> throughput, latency and memory tradeoff.

The comparison identifies the workload difference without characterizing the
prior design as generally inferior. The paragraph makes the actual question
visible before presenting the result.
