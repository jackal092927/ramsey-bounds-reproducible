# Authoritative status

Date: 2026-08-31

This file is the publication-facing status layer. Frozen records under
`routes/` preserve the state at which searches, proofs, and reviews were
created; historical labels in those files do not override this status.

## Overall disposition

```text
PUBLIC SOURCE REPOSITORY CREATED
ONE ARCHIVAL UNIFIED MANUSCRIPT
ONE STANDALONE ANONYMOUS ITCS QUANTUM DRAFT
RELEASE CANDIDATE NOT YET TAGGED OR PUBLISHED
CHATGPT PRO REVIEW COMPLETED; RECOVERABLE OBJECTIONS DISPOSITIONED
QUANTUM PART PROVED LOCALLY; QUANTUM-SPECIFIC PRO REVIEW RUNNING
FINAL-TAG CLEAN-CLONE AND RELEASE-ASSET VERIFICATION PENDING
```

The archival manuscript is
[`papers/unified/main.tex`](papers/unified/main.tex), with a local build at
[`papers/unified/main.pdf`](papers/unified/main.pdf).  The quantum source now
also has a standalone anonymous submission build at
[`papers/quantum/main.tex`](papers/quantum/main.tex) and
[`papers/quantum/main.pdf`](papers/quantum/main.pdf).  The upper, lower, and
finite directories remain source components rather than separate papers.

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
CONDITIONAL ON SOURCE ITEMS (S1), (S2), (S4), AND (S5)
WEIGHTED REVERSE PROPAGATION (S3) IS PROVED LOCALLY
Hhat_*(C) = (1+o_{C->infinity}(1))/(64 log C) > 0
fix K; fixed C,w first; ell -> infinity; w down to omega_0; then C -> infinity
C_0(K) is non-effective
```

The arithmetic checks reproduce the residual identities and asymptotic
coefficient. The post-repair adversarial review classifies the source-relative
Ramsey theorem as `PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION` because it
retains four version-pinned source items. Under (S1), (S2), (S4), and (S5),
the controlled-residual ledger, local weighted-propagation lemma (S3),
extraction, and crossing argument are `PROVABLE AS STATED`.  S3 is proved
from the indicator-kernel conjugation and tower property; it is neither an
extra assumption nor attributed to HMS or Lin--Niu. No all-\(C\),
finite-Ramsey, or cross-normalization priority claim is made.

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

A follow-up exact-seven branch-1 analysis proves the necessary degree cap
`degree <= 17` and therefore eliminates exactly 87.5813014052041% of the raw
six-edge residual deletion sets. The first nine bounded deletion-first runs
all ended `UNKNOWN`; an order-aware reconstruction then showed that two
apparent fixed-D independent-set stalls were vertex-order artefacts. Seven
repaired gates separated each returned master model in milliseconds but
reached their global walls in the master. All sixteen endpoints remain
`UNKNOWN`. Two solver-trusted fixed-deletion `UNSAT` endpoints have no
checked proof trace and are not theorem evidence. The reproducible diagnostic
record is
[`routes/finite/R3_18_BUDGET7_BENDERS_PILOT_2026-08-30.md`](routes/finite/R3_18_BUDGET7_BENDERS_PILOT_2026-08-30.md).

The subsequent proof-carrying route establishes four stronger branch-1
singleton consequences: `(11,62)`, `(18,61)`, `(18,64)`, and `(18,69)` must
all be preserved in every model of the frozen common relaxation.  Each
singleton CNF was reconstructed byte for byte and its DRAT proof replayed with
audited x86-64 and arm64 checker binaries.  A separately checked SAT model
proves that the common relaxation is nonempty; the same model has an explicit
independent 18-set, so it is not an exact-seven repair.  The singleton filter
adds 1,307,748,575,589 exclusions beyond the degree cap, removing 2.431110%
of its survivors.  The combined necessary filters exclude 87.88321365513743%
of raw residual supports.  Branch 1 and exact seven remain `UNKNOWN`; no
global Ramsey-number implication is made.  See
[`routes/finite/R3_18_BUDGET7_BRANCH1_CORE_PROOFS_2026-08-30.md`](routes/finite/R3_18_BUDGET7_BRANCH1_CORE_PROOFS_2026-08-30.md).

The subsequent structural pass found no stronger pure deletion-support clause
from the exact 396-unit projection, proved that any branch-1 target has a
maximal-triangle-free representative, and built the complete mask-union plus
maximality gate.  The frozen CNF has 639,290 variables, 1,972,360 clauses, and
SHA-256
`09e1784c3f43c4901dc6f6b4749fc5a74b025b08f74be58133edd1ed1096ebdb`.
Its only authorized 300-second Sirius probe ended with wrapper exit 124 and
`c UNKNOWN`.  No complete model or replayable proof exists; the incomplete
proof prefix was hashed and deleted and learned no cut.  The fail-closed
endpoint audit passes, but branch 1, exact seven, and the global Ramsey bounds
remain unchanged.  See
[`routes/finite/R3_18_BUDGET7_BRANCH1_MAXIMAL_UNION_GATE_2026-08-30.md`](routes/finite/R3_18_BUDGET7_BRANCH1_MAXIMAL_UNION_GATE_2026-08-30.md).

## Quantum result

Current scoped statements:

```text
PROVABLE WORST-CASE QUANTUM QUERY UPPER BOUND
N >= 4^(K-1)
Q <= O(2^K K log(K/eta))
NO NUMERICAL RAMSEY-BOUND OR ALL-CLASSICAL SEPARATION CLAIM
```

The main scale-aware implicit-majority algorithm represents every nested
candidate set by exact pivot constraints, samples it with capped symmetric
quantum search, and allocates estimation accuracy according to the cost of
each depth. A separate estimation-free size-biased recursion has query bound
$O(2^K K^2\log K\log(1/\eta))$ and extends to $q$ colours. Independent
mathematical reconstructions found no fatal or major correctness defect; the
exact binary and ternary split-tree diagnostics pass.

For randomized classical algorithms, the proved lower bound is only
$\Omega(2^{(2-\sqrt2)K})=\Omega(M^{1-1/\sqrt2})$, below the quantum exponent
$1/2$. Therefore the paper claims a new quantum upper bound and a
square-root query improvement, up to polylogarithmic factors, over the
standard deterministic recursion, not a
separation from the best randomized classical algorithm.

Jain--Li--Robere--Xun state an incompatible $N^{1-o(1)}$ quantum lower-bound
remark. Their formal Definition II.6 uses $N=2^n$ and their default target is
$K=n/2$; a different introductory shorthand is not used in our comparison.
Direct parameter substitution into the cited reduction and fixed-multiplicity
multi-collision theorem gives at most exponent $1/24$. The manuscript now
records this as an apparent mismatch in a side consequence, says explicitly
that it does not affect their principal TFNP separation theorems, and does not
use the disputed lower bound. Author clarification remains desirable.

The standalone ITCS draft contains only this quantum result.  It has 16 pages
total; the central claims, proofs, significance, and literature comparison
appear within the first ten pages, while the scope conclusion and Appendix A
share page 11.  It then gives three technical/reproducibility appendices.  Its
11pt single-column anonymous build,
cross-references, citations, embedded fonts, and metadata pass.  It contains
no author block, affiliation, personal email, or public repository URL; one
relevant prior paper by the submitting author is cited in ordinary
third-person form.  The current PDF SHA-256 is
`8ac5f6f08123f339b1ae80e51357ba4b251b71c5a71123c96dae9846c2874bf9`.
This is a prepared draft, not an uploaded or accepted submission; the JLRX
clarification remains the scientific submission gate.

## Review state

- First-round local mathematical and reproducibility audits: **completed**;
  their findings were retained as historical review evidence.
- Upper post-repair adversarial recheck: **passed conditionally**; U1--U4 and
  the generated-copy fidelity gate are closed.
- Lower post-repair adversarial recheck: **passed at the four-item source
  boundary**; a later targeted reconstruction proved the former S3 implication
  locally and removed it from the assumption ledger.
- Unified global-claim audit: **completed**; G1--G5 were repaired in the
  manuscript prose.
- Post-repair reproducibility audit: **all four major implementation findings
  closed**; public repository/release verification remains open.
- Current 26-asset finite-heavy gate: **passed**; it reconstructed six theorem
  formulas and four singleton formulas, replayed all ten DRAT proofs, checked
  the complete common-relaxation model, and left exact seven `UNKNOWN`.
- Fresh independent mathematical audit: **0 fatal, 0 major, 1 resolved
  terminological minor**; no theorem, constant, or proof architecture changed.
- Final theorem-specific adversarial reconstructions: **0 fatal, 0 major,
  9 resolved minor findings** across the upper, lower, and finite components;
  the scoped theorem statements are unchanged.
- Subsequent lower S3 closure audit: **proved locally** by indicator-kernel
  conjugation and reverse induction; the theorem still retains source items
  (S1), (S2), (S4), and (S5).
- Maximal-union adversarial implementation audit: **one real CLI symlink
  validation defect found and repaired**; 11 gate tests and 3 endpoint-audit
  tests pass, and a post-repair full rebuild retained the exact CNF hash.
- Final release-implementation audit: **0 blocker, 0 major, 0 minor after
  repair**; live publication and post-release replay remain pending.
- ChatGPT Pro second-opinion review: **completed and dispositioned on
  2026-08-30**; the uploaded artifact was a pre-final candidate, and the
  report is an AI-assisted author-side check rather than human peer review.
- Quantum theorem-specific adversarial review: **passed locally** for the
  scale-aware, size-biased, multicolour, canonicalization, and classical-lower
  arguments; priority and the JLRX parameter conflict remain open.
- Quantum ChatGPT Pro review: **completed and dispositioned on 2026-08-31**;
  it found no fatal correctness error, endorsed the scoped query theorem as
  apparently novel, and left significance/priority and the JLRX clarification
  as publication risks rather than mathematical defects.
- Final narrow quantum ChatGPT Pro differential review: **packet prepared but
  not transmitted as of 2026-09-01**; no result from this additional review is
  counted in the evidence ledger.
- Exact-seven ChatGPT Pro collaboration packet: **drafted but not submitted**;
  fresh action-time confirmation is still required before external transmission.

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
- [`reviews/LOWER_S3_CLOSURE_2026-08-30.md`](reviews/LOWER_S3_CLOSURE_2026-08-30.md)
- [`reviews/FINAL_RELEASE_PREFLIGHT_2026-08-30.md`](reviews/FINAL_RELEASE_PREFLIGHT_2026-08-30.md)
- [`reviews/QUANTUM_RAMSEY_MATHEMATICAL_AUDIT_2026-08-31.md`](reviews/QUANTUM_RAMSEY_MATHEMATICAL_AUDIT_2026-08-31.md)
- [`reviews/CHATGPT_PRO_QUANTUM_REVIEW_DISPOSITION_2026-08-31.md`](reviews/CHATGPT_PRO_QUANTUM_REVIEW_DISPOSITION_2026-08-31.md)
- [`reviews/JLRX_PARAMETER_AUDIT_2026-09-01.md`](reviews/JLRX_PARAMETER_AUDIT_2026-09-01.md)
- [`reviews/CHATGPT_PRO_QUANTUM_FINAL_DELTA_PROMPT_2026-09-01.md`](reviews/CHATGPT_PRO_QUANTUM_FINAL_DELTA_PROMPT_2026-09-01.md)
- [`reviews/CHATGPT_PRO_REVIEW.md`](reviews/CHATGPT_PRO_REVIEW.md)
- [`reviews/REVIEW_DISPOSITION.md`](reviews/REVIEW_DISPOSITION.md)

The current quantum-integrated unified PDF has 115 pages and
SHA-256
`a2bf661530592cd3833b526304cc502e3780d55e91a506e782914701befc64ae`.
Two clean Part-IV-integrated builds under the pinned toolchain were
byte-identical, and the visual audit passes. This is not a published-Release
digest until the separate immutable-release procedure succeeds.
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
- Final evidence tag and immutable 26-asset Release: not yet published.
- The exact final tag target commit will be recorded after publication; it is
  intentionally not self-referenced inside the commit that it identifies.
- Final-tag credential-free clone and Release-asset replay: pending.
- DOI or archival deposit: none assigned.
- Public reuse license: none granted; copyright is retained by Cheng Xin.

Therefore the current snapshot may be described as a public source release
candidate, but not yet as a completed immutable artifact release or a
peer-reviewed publication.

## Gate to change this status

The local mathematical, current quick-replay, compilation, and visual gates
are complete. Quantum-specific ChatGPT Pro review, expert priority review,
and clarification of the JLRX parameter conflict remain submission gates.
The package can move to public-release status only after:

1. the final tag and exact 26-asset immutable Release are published; and
2. the advertised workflow is verified from a credential-free fresh clone
   and public asset download.
