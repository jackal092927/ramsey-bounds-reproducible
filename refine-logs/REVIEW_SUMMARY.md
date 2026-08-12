# Review summary

> **Round-2 correction:** the subsequent independent audit found that the
> HorizonMath `R_0` test takes an orientation union instead of the required
> intersection.  Therefore `3.6960839` and the local `3.6958799` delta are
> invalid as Ramsey candidates.  See `round-2-correction.md`.  This supersedes
> the empirical-progress statement below.

- External reviewer: unavailable (login required); no score assigned.
- Internal verdict: REVISE.
- Main correction: put theorem-to-code audit and independent verification ahead
  of further numerical optimization.
- Empirical progress: reproduced `3.7992027396` and `3.69608391263`; found a
  one-coefficient candidate at `3.69587996127` accepted by the full public
  interval validator.
- Blocking proof issues: derivative-sign typo, `R_0` derivation/orientation,
  small-regime splice, and piecewise-witness semantics.
