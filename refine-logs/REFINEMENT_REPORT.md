# Refinement report

> **Superseding correction:** the public validator's symmetric-region test is
> unsound for the GNNW theorem.  It accepts either orientation (`min`) where
> membership requires both (`max`).  The `3.6960839` and `3.6958799` artifacts
> below are now negative regression cases, not upper-bound candidates.  See
> `round-2-correction.md`.

## Completed

- Audited the current 2026 literature landscape and selected the diagonal upper
  bound as the most tractable first target.
- Reproduced the published GNNW parameter base near `3.7992` with the public
  numerical pipeline.
- Reproduced the HorizonMath interval result
  `c=3.6960839126332994` with positive slacks.
- Tested a controlled degree-5 coefficient sweep while keeping all witnesses
  fixed.
- Fully validated `a5=-0.07795`, obtaining
  `c=3.695879961267919` and positive reported margins.
- Pinned source archive, Git commit, and file hashes; added a reproduction
  script.

## Not completed

- No independent interval verifier has been implemented yet.
- The source-theorem/validator equivalence has not passed human review.
- The external review service was unavailable because it required login.
- Therefore no new mathematical bound is claimed.

## Key learning

The current numerical ansatz still has room for a small objective improvement,
but numerical search is not the highest-value next action.  The decisive work is
to turn the validator's predicates into an independently reviewed mathematical
certificate.
