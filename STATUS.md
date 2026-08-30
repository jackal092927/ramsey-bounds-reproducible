# Authoritative status

Date: 2026-08-30

This file is the publication-facing status layer. Frozen records under
`routes/` preserve the state at which searches, proofs, and reviews were
created; historical labels in those files do not override this status.

## Overall disposition

```text
PUBLIC SOURCE REPOSITORY CREATED
ONE CANONICAL UNIFIED MANUSCRIPT
RELEASE CANDIDATE NOT YET TAGGED OR PUBLISHED
CHATGPT PRO REVIEW TRANSMITTED; FINAL RESPONSE AND DISPOSITION PENDING
FINAL-TAG CLEAN-CLONE AND RELEASE-ASSET VERIFICATION PENDING
```

The canonical manuscript is
[`papers/unified/main.tex`](papers/unified/main.tex), with a local build at
[`papers/unified/main.pdf`](papers/unified/main.pdf). The directories
`papers/upper`, `papers/lower`, and `papers/finite` are archival source
components, not separate papers.

## Upper result

Current scoped statement:

```text
CONDITIONAL / SOURCE-RELATIVE ASYMPTOTIC RESULT
R(k,k) <= (3.780685290)^(k+o(k))
certified unrounded base < 3.780685288379640114
```

The complete six-stage interval chain, independent region replay, and four
outer transfer checks reproduce the displayed base. The post-repair
adversarial review classifies the headline as `PROVABLE AS STATED` under the
explicit conditional trust boundary: three version-pinned Yang--Mao v1
interfaces, the locally proved BookCor/correlation implications, and Arb ball
containment. No effective finite-\(k\) threshold, global optimum, priority, or
world-best claim is made.

## Lower result

Current scoped statement:

```text
SOURCE-RELATIVE FIXED-LARGE-C RESULT
CONDITIONAL ON (S1)--(S5), INCLUDING THE ADDITIONAL HYPOTHESIS (S3)
Hhat_*(C) = (1+o_{C->infinity}(1))/(64 log C) > 0
fixed C first, then ell -> infinity; threshold in C is non-effective
```

The arithmetic checks reproduce the residual identities and asymptotic
coefficient. The post-repair adversarial review classifies the source-relative
Ramsey theorem as `PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION`. Under the
fully stated interface (S1)--(S5), the controlled-residual ledger, extraction,
and crossing argument are `PROVABLE AS STATED`. Items (S1), (S2), (S4), and
(S5) are version-pinned source hypotheses; (S3) is a separately stated
weighted-extension hypothesis and is not attributed as a theorem stated by
HMS or Lin--Niu. No all-\(C\), finite-Ramsey, or cross-normalization priority
claim is made.

## Finite result

Current scoped statement:

```text
LOCAL FIXED-SEED PROOF-CARRYING THEOREM
one-sided deletion repair radius >= 7
exact-seven status = UNKNOWN
```

The mathematical adversarial review freshly replayed the six DRAT proofs and
classified the radius-at-least-seven theorem as `PROVABLE AS STATED` under the
conventional checker, encoding, and case-cover trust boundary. The result is
local to the pinned 100-vertex seed and edit metric. It does not construct a
100-vertex \((3,18)\)-Ramsey graph and does not prove
\(R(3,18)\ge101\).

## Review state

- First-round local mathematical and reproducibility audits: **completed**;
  their findings were retained as historical review evidence.
- Upper post-repair adversarial recheck: **passed conditionally**; U1--U4 and
  the generated-copy fidelity gate are closed.
- Lower post-repair adversarial recheck: **passed only at the stated
  conditional boundary**; the main theorem still requires the explicit extra
  hypothesis (S3).
- Unified global-claim audit: **completed**; G1--G5 were repaired in the
  manuscript prose.
- Post-repair reproducibility audit: **all four major implementation findings
  closed**; public repository/release verification remains open.
- Current finite-heavy semantic and six-DRAT replay: **passed**; exact seven
  remains `UNKNOWN`.
- Fresh independent mathematical audit: **0 fatal, 0 major, 1 resolved
  terminological minor**; no theorem, constant, or proof architecture changed.
- Final theorem-specific adversarial reconstructions: **0 fatal, 0 major,
  9 resolved minor findings** across the upper, lower, and finite components;
  the scoped theorem statements are unchanged.
- Final release-implementation audit: **0 blocker, 0 major, 0 minor after
  repair**; live publication and post-release replay remain pending.
- ChatGPT Pro second-opinion review: **transmitted on 2026-08-30 and still in
  progress**; no final response has yet been archived or dispositioned.

Review files:

- [`reviews/ADVERSARIAL_MATH_REVIEW.md`](reviews/ADVERSARIAL_MATH_REVIEW.md)
- [`reviews/REPRODUCIBILITY_ADVERSARIAL_REVIEW.md`](reviews/REPRODUCIBILITY_ADVERSARIAL_REVIEW.md)
- [`reviews/UPPER_POST_REPAIR_REVIEW.md`](reviews/UPPER_POST_REPAIR_REVIEW.md)
- [`reviews/LOWER_POST_REPAIR_REVIEW.md`](reviews/LOWER_POST_REPAIR_REVIEW.md)
- [`reviews/GLOBAL_CLAIM_AUDIT.md`](reviews/GLOBAL_CLAIM_AUDIT.md)
- [`reviews/REPRODUCIBILITY_POST_REPAIR_REVIEW.md`](reviews/REPRODUCIBILITY_POST_REPAIR_REVIEW.md)
- [`reviews/FINITE_HEAVY_CURRENT_RUN_2026-08-30.md`](reviews/FINITE_HEAVY_CURRENT_RUN_2026-08-30.md)
- [`reviews/FRESH_INDEPENDENT_MATH_REVIEW_2026-08-30.md`](reviews/FRESH_INDEPENDENT_MATH_REVIEW_2026-08-30.md)
- [`reviews/FINAL_TARGETED_ADVERSARIAL_REVIEW_2026-08-30.md`](reviews/FINAL_TARGETED_ADVERSARIAL_REVIEW_2026-08-30.md)
- [`reviews/FINAL_RELEASE_PREFLIGHT_2026-08-30.md`](reviews/FINAL_RELEASE_PREFLIGHT_2026-08-30.md)
- [`reviews/REVIEW_DISPOSITION.md`](reviews/REVIEW_DISPOSITION.md)

The current release-candidate PDF has 79 pages and SHA-256
`bad787b9a37430d39d17d789c9dddc39db212db2db0954fa668dd43c96993804`.
This is a candidate hash until the external review is dispositioned and the
final two clean builds agree.
Its final log has no overfull box, undefined or multiply defined reference,
LaTeX warning, error, or fatal diagnostic; representative pages were also
inspected visually.

## Repository and release state

- Local Git history and verified GitHub remote: present.
- Public source repository: confirmed at
  <https://github.com/jackal092927/ramsey-bounds-reproducible>.
- Initial public snapshot commit:
  `6f833effcfb9e39f388998c5bfe4281d5c88805a`.
- Initial-commit anonymous clone plus fast and full hosted verification:
  passed. These runs do not verify the eventual final tag or Release assets.
- Final evidence tag and immutable twelve-asset Release: not yet published.
- The exact final tag target commit will be recorded after publication; it is
  intentionally not self-referenced inside the commit that it identifies.
- Final-tag credential-free clone and Release-asset replay: pending.
- DOI or archival deposit: none assigned.
- Public reuse license: none granted; copyright is retained by Cheng Xin.

Therefore the current snapshot may be described as a public source release
candidate, but not yet as a completed immutable artifact release or a
peer-reviewed publication.

## Gate to change this status

The local mathematical, implementation, replay, compilation, and visual gates
are complete. The package can move to public-release status only after:

1. the external ChatGPT Pro second-opinion review is completed and every
   concrete objection is repaired or dispositioned;
2. the final tag and exact twelve-asset immutable Release are published; and
3. the advertised workflow is verified from a credential-free fresh clone
   and public asset download.
