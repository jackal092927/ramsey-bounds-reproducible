# Result-to-claim gate: specialized-correlation retained spine

Date: 2026-08-12  
Judgment: independent secondary Codex evaluation after resolved referee replay

## Structured verdict

```text
claim_supported: yes
confidence: high
```

### what_results_support

Within the explicitly frozen conditional trust boundary, the evidence
supports both

$$
\mathcal G_2^{(3)}(10^{-6},11.62088)
$$

and

$$
R(k,k)\le
\exp\!\left((U(1)-2.87\cdot10^{-6})k+o(k)\right)
\le(3.780687577208)^{k+o(k)}.
$$

The boundary consists of the frozen local $P_6$/BookCor chain, Yang--Mao v1
regularization and parameterized book theorem, and Arb/python-flint
containment semantics.  The author 384-bit source and full-square checkers
pass.  A separately structured 512-bit checker, which imports neither author
checker, independently rebuilds the root-filter envelopes, generalized
$-\sigma$ expectation/tail argument, all source gates, $P_6$ concavity, the
complete weighted wedge, and decimal rounding.  The two proof-writing issues
found by the referee were resolved without changing any formula or parameter,
and all three revised executions pass.

The smallest relevant strict margins include

$$
5.72\cdot10^{-9}\quad\text{(degree slack)},
$$

$$
2.3362059296\cdot10^{-8}\quad\text{(red page)},
$$

and

$$
7.9347357905\cdot10^{-13}\quad\text{(decimal rounding)}.
$$

### what_results_dont_support

The evidence does not support describing the result as fully formalized,
equipped with an explicit finite-$k$ threshold, globally parameter-optimal,
independent of all upstream theorems, externally peer reviewed, or verified
as the current globally best or first-published Ramsey upper bound.  The new
checkers do not themselves reprove every upstream component of Yang--Mao v1,
the frozen $P_6$ theorem, or repaired BookCor.

### missing_evidence

No missing local evidence was identified for the stated conditional theorem.
Stronger descriptions would require the following additional evidence:

1. an independent end-to-end or formal audit of all upstream $P_6$, BookCor,
   and Yang--Mao interfaces;
2. effective error terms yielding an explicit finite-$k$ threshold;
3. a current literature and priority audit;
4. a global parameter-space proof before making an optimality claim.

### suggested_claim_revision

> Conditional on the Yang--Mao v1 regularization and parameterized book
> theorem, and on the declared frozen local $P_6$/BookCor computer-assisted
> inputs, we prove $\mathcal G_2^{(3)}(10^{-6},11.62088)$ and obtain the
> complete-interval certificate
> $R(k,k)\le(3.780687577208)^{k+o(k)}$.  This is a conditional
> computer-assisted local theorem; it does not claim an explicit finite-$k$
> threshold, global parameter optimality, or world-best status without a
> separate literature audit.

### next_experiments_needed

No further experiment is required for the conditional theorem itself.  The
highest-value strengthening steps are a third implementation in a different
software or formal-verification stack, an end-to-end upstream audit, an
effective-$o(k)$ derivation, and a current literature/priority search.
Continued parameter optimization would strengthen the result but is not a
gate for the present claim.

## Frozen resolved evidence

```text
c28026ed8d30e0c4096ccc46e3cc04d7026fa2c2975eab4a2537a9021a866ebe  SPECIALIZED_CORRELATION_SHARPENING.md
be17cc0848a54e606b4ad4bc3393b8ac317f030306c239d41bd0f90f38c5724a  check_specialized_correlation.py
83e79f2a2950c73d0a3697193b3fd826130d69f197f57febd4a8f9f1c25acdbf  RETAINED_SPINE_SHARPENED_CERTIFICATE.md
1a74a21d81002805657c74373c44b760c57edd36ad942d768e7d7afd6abfac40  check_retained_spine_sharpened.py
cf84ae77fa703ef93f7364ea9b33546fe3241efc03758ef8e1a6082bdbf00cd4  independent_check_retained_spine_sharpened.py
```

The resolved referee report is
`INDEPENDENT_RETAINED_SPINE_SHARPENED_REFEREE.md`.
