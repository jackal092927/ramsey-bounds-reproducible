# Authoritative status

Date: 2026-09-03

This file is the publication-facing status layer. Frozen records under
`routes/` preserve the state at which searches, proofs, and reviews were
created; historical labels in those files do not override this status.

## Overall disposition

```text
PUBLIC SOURCE REPOSITORY CREATED
ONE ARCHIVAL UNIFIED MANUSCRIPT
ONE STANDALONE ANONYMOUS ITCS QUANTUM SUBMISSION
RELEASE CANDIDATE NOT YET TAGGED OR PUBLISHED
CHATGPT PRO REVIEW COMPLETED; RECOVERABLE OBJECTIONS DISPOSITIONED
QUANTUM SUBMITTED AND RESUBMITTED SEPTEMBER 2; RECEIPT RECORDS READY FOR REVIEW
ADDITIONAL PRO DIFFERENTIAL REVIEW INCOMPLETE DUE TO NETWORK ERROR
TDA RESEARCH PACKET SYNCED; NEW PRO REVIEW AND THEOREM DEVELOPMENT RUNNING
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

The standalone ITCS draft contains only this quantum result. It has 16 pages
total; the main quantum upper-bound proof finishes on page 8, while the detailed
literature comparison and scope conclusion finish on page 11. The
introduction contains the merits and concise literature comparison within
the recommended first ten pages. Three appendices begin on page 12. Its
official LIPIcs v2021.1.3 single-column A4 build uses `anonymous` and a
review-only 11pt text adapter. Its
cross-references, citations, embedded fonts, and metadata pass.  It contains
only anonymous author placeholders, no real affiliation, personal email,
ORCID link, or public repository URL; one
relevant prior paper by the submitting author is cited in ordinary
third-person form.  The current PDF SHA-256 is
`e47b80073b1333668c2203c970548df55c1db51bdd005c268de4667077563cd7`.
The mathematical polish pass fixed the explicit classical truncation, conditional
concentration notation, per-call oracle cost wording, and abort semantics;
the main query theorem and its proof architecture are unchanged. The quantum
self-check and PDF build pass; the final standalone LIPIcs build has no
LaTeX/BibTeX warnings. The template migration changed no theorem, proof,
experiment, or citation entry. The official class and its provenance are
bundled with the standalone source; see `papers/quantum/TEMPLATE.md`.
The subsequent editorial pass rewrites Appendix C.2 as self-contained
small-instance numerical experiments, preserving the reported outcomes and
adding explicit experimental settings while removing source paths and run
commands. The anonymous paper does not depend on a code artifact; project
documentation retains reproduction instructions. The existing repository and
quantum code on the research branch are publicly viewable, but the repository
license reserves all rights. No visibility or licensing change was made.
The earlier PDF was uploaded and saved to ITCS submission #193 on September 2
at 16:31:33 PDT; its SHA-256 is
`bd11783756a99ac1ab865548ab08078dbb969d3034b44ef8df2e134640696a2f`,
matching the server checksum prefix `bd117837`. It is preserved at
`papers/quantum/submitted/itcs2027-paper193-2026-09-02.pdf`.
After the author confirmed no PC conflicts, final submission was completed on
September 2 at approximately 16:37 PDT. HotCRP returned `Updated submission`
and explicitly confirmed **ready for review**, with no further action needed.
This is a submitted paper, not an acceptance decision.
The user reports sending the JLRX clarification email. A reply is desirable
but not a prerequisite: the proof is independent and the discrepancy is
explicitly scoped. PC conflicts remain `None`, as confirmed by the author.
The already-uploaded PDF, title, abstract, topics, and AI disclosures were
retained. HotCRP explicitly allows updates until September 4, 2026, 16:59:59 PDT,
and now offers `Save and resubmit`. See `papers/quantum/SUBMISSION_CHECKLIST.md`
for the submitted artifact and live confirmation record.
The subsequent local revision shortens the AI disclosure and its body
description without changing the mathematical content or numerical outcomes.
It uses `GPT-based tools`, identifies ChatGPT and Codex once, and summarizes
the roles as brainstorming, constructive discussion, polishing, and review,
with theoretical arguments and numerical experiments identified in the body.
It omits section numbers and model/tier labels. At the author's request, this
revision was uploaded and resubmitted on September 2 at 17:04:26 PDT. HotCRP
returned `Updated submission (changed Submission)`, displayed checksum prefix
`e47b8007`, and confirmed **ready for review** with the corresponding checkbox
still checked. Other submission fields were not changed. The revised submitted
PDF is preserved at
`papers/quantum/submitted/itcs2027-paper193-2026-09-02-v2.pdf`.

A further local revision was committed on September 4 (commit `0314274`) but
**has not been uploaded**; HotCRP still holds the September 2 PDF. The
revision adds a self-contained proof of the random-Painter weight bound in
Appendix B (the earlier citation pointed at the online-Ramsey theorem rather
than the estimate inside its proof), restates the randomized lower bound in
distributional form, adds a quantum greedy search on $G(N,1/2)$ with
$\widetilde O(N^{1/4})$ queries and hence a polynomial quantum-versus-randomized
separation on random graphs, records the $\Omega(N^{1/24})$ quantum lower
bound that the JLRX reduction yields at multiplicity two, reframes the
introduction around the JLRX query question with a bounds table, and names
Claude in the AI disclosure. The candidate PDF has SHA-256 prefix
`86776bc4` and 25 pages, builds with no diagnostics, and passes the identity
and self-check scans. Before uploading, the author must verify the new
material, approve the disclosure wording, and replace the HotCRP abstract;
the open items are listed at the top of
`papers/quantum/SUBMISSION_CHECKLIST.md`.

## Normalized persistence candidate

Current scoped statement:

```text
LOCAL SUBMISSION CANDIDATE; INDEPENDENTLY REVIEWED 2026-09-04
BQP1^{G_2}-HARDNESS OF NORMALIZED (HARMONIC) PERSISTENCE, PROBLEM 9 OF LOWE ET AL.
WEIGHTED AND UNWEIGHTED CLIQUE COMPLEXES; ENDPOINT GAP PROMISES
NO SDQC1, BQP, GATE-INDEPENDENT, OR CONTAINMENT CLAIM
```

The manuscript at
[`research/quantum_direction_selection/collaboration/2026-09-02/manuscript_v0/`](research/quantum_direction_selection/collaboration/2026-09-02/manuscript_v0/)
was independently re-derived on September 4 with no mathematical error found;
seven rigor gaps were closed and the presentation was rewritten for ITCS (see
`PROOF_AUDIT.md` and `CHECK_REPORT.md` there).  The build is 28 clean pages.
HotCRP lists the ITCS 2027 registration deadline as September 2, 2026,
7:59:59 PM EDT and the submission deadline as September 4, 2026, 7:59:59 PM
EDT; a new upload is possible only for a submission registered before the
first date.

A version-2 draft with four new results (exponent 10 from filling depth,
general perfect-subspace-fraction source with SDQC1 fraction-form hardness
and 2^r initial holes, hard-and-in-BQP instances via large overlap and
state preparation, #P-completeness of gapped clique Betti numbers) is in
`manuscript_v2/` next to the frozen version 1, with proofs in
`V2_ENHANCEMENT_PLAN_2026-09-04.md`; it builds cleanly (34 pages) and awaits
external review.

## Current research collaboration

The September 3 [project dossier](research/pro_collaboration_2026-09-02/README.md)
consolidates the Ramsey results, TDA candidates, useful obstructions and four
historical Pro replies. The [canonical TDA collaboration](research/quantum_direction_selection/collaboration/2026-09-02/README.md)
owns the newly sent packet and its continuing review/development round.
The main candidate transfers exact kernel multiplicity to true normalized
persistence, with explicit fixed-gadget imports and a specified exact circuit
promise. Unrestricted SDQC1 hardness and paper readiness are not established.
The supplement records the corrected mixed-spectator extension, a conditional
persistent spectral-transfer corollary, the already-known domination
inequality, and 39 finite diagnostic checks. The prior seven probes, quantum
self-check and current source/hash consistency checks passed; their precise
scope is in [VERIFICATION.md](research/pro_collaboration_2026-09-02/VERIFICATION.md).

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
- Final narrow quantum ChatGPT Pro differential review: **incomplete**;
  the existing conversation shows interim analysis followed by a network
  error. No final verdict from it is counted. No new prompt was sent.
- Quantum submission-readiness recheck: **submission candidate after scoped
  corrections**; no fatal main-query-theorem defect found. JLRX source
  parameters were rechecked. Author silence and the additional AI review's
  failure are not mathematical submission prerequisites.
- Exact-seven ChatGPT Pro response: **completed historical response recovered**
  in the original registered conversation. It received text only and predates
  the checked singleton results. Its useful suggestions and superseded claims
  are recorded in the supplemental collaboration disposition.
- Current TDA Pro collaboration: **new consolidated packet sent and running**
  at fixed GitHub snapshot a46f4087693edc088663e0cbf4f6aa9961494325. A single
  hourly follow-up collects, checks and archives resulting milestones; a new
  response is not counted until it is actually retrieved.

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
- [`reviews/QUANTUM_SUBMISSION_READINESS_2026-09-01.md`](reviews/QUANTUM_SUBMISSION_READINESS_2026-09-01.md)
- [`reviews/CHATGPT_PRO_QUANTUM_FINAL_DELTA_PROMPT_2026-09-01.md`](reviews/CHATGPT_PRO_QUANTUM_FINAL_DELTA_PROMPT_2026-09-01.md)
- [`reviews/CHATGPT_PRO_REVIEW.md`](reviews/CHATGPT_PRO_REVIEW.md)
- [`reviews/REVIEW_DISPOSITION.md`](reviews/REVIEW_DISPOSITION.md)

The current quantum-integrated unified PDF has 115 pages and
SHA-256
`8fcb9c04133bf558391f452894a94c1bb7cfb917aa1b7d1036ebbc755dfcb3b6`.
For an earlier Part-IV-integrated candidate, two clean builds under the pinned
toolchain were byte-identical. The current build and visual audit pass. This is not a published-Release
digest until the separate immutable-release procedure succeeds.
Its final log has no overfull box, undefined or multiply defined reference,
LaTeX warning, error, or fatal diagnostic, but does retain nonfatal underfull
hbox/vbox spacing diagnostics in the archival layout. The standalone submission
build has no such diagnostics, and its revised pages were inspected visually.

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

The earlier local mathematical, quick-replay, compilation, and visual gates
are recorded above. The quantum paper has already been submitted according
to its September 2 receipt. Completion of the failed differential AI review
and receipt of author clarification are not outstanding prerequisites for
that recorded submission. Priority and significance remain scientific review
questions. This September 3 consolidation checked the local files and GitHub;
it did not refresh the conference server or change submission fields.
The package can move to public-release status only after:

1. the final tag and exact 26-asset immutable Release are published; and
2. the advertised workflow is verified from a credential-free fresh clone
   and public asset download.
