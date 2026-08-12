# Authoritative status

Date: 2026-08-12

This file is the publication-facing status layer.  Frozen proof specifications
under `routes/` are intentionally byte-preserved because independent checkers
pin their SHA-256 identities.  Some of those frozen specifications still say
"pending review" or "noncanonical" because they record the state at the time
of freezing.  Those historical labels are superseded as follows.

## Current upper result

The exact-diagonal package has passed independent proof review and the
secondary result-to-claim gate.  Its scoped status is:

```text
INDEPENDENTLY REVIEWED LOCAL COMPUTER-ASSISTED THEOREM
R(k,k) <= (3.780685290)^(k+o(k))
certified unrounded base < 3.780685288379640114
```

The exact trust boundary is stated in `papers/upper/main.tex` and
`routes/upper/INDEPENDENT_EXACT_DIAGONAL_NEXT_REFEREE.md`.

## Current lower result

The controlled-residual weighted ledger has passed independent source-level
review and the secondary result-to-claim gate.  Its scoped status is:

```text
INDEPENDENTLY REVIEWED SOURCE-RELATIVE LOCAL THEOREM
fixed sufficiently large C
new term Hhat_*(C) = (1+o(1))/(64 log C) > 0
```

The exact trust boundary is stated in `papers/lower/main.tex` and
`routes/lower/INDEPENDENT_HISTORY_WEIGHT_OPTIMIZATION_REFEREE.md`.

## Current finite result

The fixed 100-vertex `R(3,18)` near miss has a proof-verified deletion radius
of at least seven under the specified free-addition/charged-deletion metric.
Exact-seven remains `UNKNOWN`.  There is no new global finite Ramsey bound and
no claim of `R(3,18) >= 101`.

