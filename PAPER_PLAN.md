# Unified manuscript and publication plan

Date: 2026-08-30

## Editorial decision

All current results belong in one paper. The canonical source is
[`papers/unified/main.tex`](papers/unified/main.tex), and the corresponding
local build is [`papers/unified/main.pdf`](papers/unified/main.pdf).

The directories `papers/upper`, `papers/lower`, and `papers/finite` remain
archival source components. They preserve derivation history and permit
deterministic materialization of the unified manuscript, but they must not be
described as three independent publication outputs.

Working title:

> *Reproducible Ramsey Analysis Across Asymptotic and Finite Regimes:
> Retained Spines, Gaussian Residuals, and Proof-Carrying Barriers*

The paper's unity is methodological: each Part states an exact claim, identifies
its imported interfaces, supplies human-readable implications, and attaches
machine-checkable evidence at the appropriate level. The three mathematical
techniques are not presented as instances of one theorem.

## Claim hierarchy

### U — conditional asymptotic upper result

Subject to the version-pinned retained-spine and parameterized-book interfaces
and the certified six-stage off-diagonal rate,

\[
R(k,k)\le (3.780685290)^{k+o(k)},
\]

with certified unrounded base below `3.780685288379640114`.

The statement must remain explicitly source-relative and asymptotic. It does
not provide an effective finite-\(k\) threshold, a proof of global parameter
optimality, or a priority/world-best claim.

### L — source-relative fixed-ratio lower result

After fixing the source constant \(K\), for every sufficiently large fixed
\(C\), inside the pinned Gaussian reverse-induction and cumulant interfaces,
the controlled-residual ledger contributes

\[
\widehat H_*(C)=\frac{1+o_{C\to\infty}(1)}{64\log C}>0.
\]

The order of limits is part of the theorem: fix \(C\) and \(w>\omega_0\), let
\(\ell\to\infty\), then let \(w\downarrow\omega_0\), and only afterwards
examine \(C\to\infty\).
The statement is conditional on (S1)--(S5). Items (S1), (S2), (S4), and (S5)
are version-pinned source hypotheses; (S3) is the paper's additional
weighted-extension hypothesis and is not attributed as a theorem stated by
HMS or Lin--Niu. The threshold \(C_0(K)\) is existential and non-effective. No
comparison is made across incompatible terminal normalizations.

### F — local finite proof-carrying result

For the content-addressed 100-vertex seed and the stated one-sided edit metric,
free additions together with at most six seed-edge deletions cannot produce a
triangle-free graph with independence number below 18. Equivalently, the
local deletion repair radius is at least seven.

Exact seven remains `UNKNOWN`. This result neither constructs a
100-vertex \((3,18)\)-Ramsey graph nor proves \(R(3,18)\ge101\).

## Manuscript architecture

1. **Introduction and main results.** State all three results and the
   non-implications in one place.
2. **Evidence taxonomy.** Distinguish source interfaces, written analytic
   arguments, interval certificates, proof-carrying SAT theorems, and bounded
   observations.
3. **Part I: retained-spine diagonal upper bound.** Give the six-stage rate,
   exact-diagonal correlation certificate, and outer transfer with its exact
   trust boundary.
4. **Part II: controlled Gaussian residuals.** Define the source quantities,
   prove the residual and concavity ledger, propagate it through reverse
   induction, and preserve the fixed-\(C\) order of limits.
5. **Part III: proof-carrying finite barrier.** Define the seed and metric,
   prove the branch cover and CNF semantics, replay the six DRAT proofs, and
   record exact seven as `UNKNOWN`.
6. **Unified reproducibility section.** Give one tiered interface for fast,
   full asymptotic, finite-heavy, and paper-build checks.
7. **Appendices.** Include the proof-critical source interfaces, certificate
   correctness statements, exact parameters, hashes, and verification
   records needed by the three Parts.

Labels and symbols are namespaced by Part. Material shared only at the level
of evidence policy belongs in the global sections, not in a fabricated common
mathematical framework.

## Adversarial review gates

The retained first-round reviews are:

- [`reviews/ADVERSARIAL_MATH_REVIEW.md`](reviews/ADVERSARIAL_MATH_REVIEW.md);
- [`reviews/REPRODUCIBILITY_ADVERSARIAL_REVIEW.md`](reviews/REPRODUCIBILITY_ADVERSARIAL_REVIEW.md).

The mathematical review applies the statuses `PROVABLE AS STATED`,
`PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION`, and
`NOT CURRENTLY JUSTIFIED` claim by claim. The reproducibility review treats a
clean-clone replay as the publication criterion. A passing local numerical
program does not by itself close a missing theorem-to-code or
source-to-local-proof implication.

The post-repair reviews and their consolidated disposition are:

- [`reviews/UPPER_POST_REPAIR_REVIEW.md`](reviews/UPPER_POST_REPAIR_REVIEW.md);
- [`reviews/LOWER_POST_REPAIR_REVIEW.md`](reviews/LOWER_POST_REPAIR_REVIEW.md);
- [`reviews/GLOBAL_CLAIM_AUDIT.md`](reviews/GLOBAL_CLAIM_AUDIT.md);
- [`reviews/REPRODUCIBILITY_POST_REPAIR_REVIEW.md`](reviews/REPRODUCIBILITY_POST_REPAIR_REVIEW.md);
- [`reviews/FRESH_INDEPENDENT_MATH_REVIEW_2026-08-30.md`](reviews/FRESH_INDEPENDENT_MATH_REVIEW_2026-08-30.md);
- [`reviews/FINAL_TARGETED_ADVERSARIAL_REVIEW_2026-08-30.md`](reviews/FINAL_TARGETED_ADVERSARIAL_REVIEW_2026-08-30.md);
- [`reviews/FINAL_RELEASE_PREFLIGHT_2026-08-30.md`](reviews/FINAL_RELEASE_PREFLIGHT_2026-08-30.md);
- [`reviews/CHATGPT_PRO_REVIEW.md`](reviews/CHATGPT_PRO_REVIEW.md); and
- [`reviews/REVIEW_DISPOSITION.md`](reviews/REVIEW_DISPOSITION.md).

Every major local finding has now been handled in one of two ways:

1. repair the proof or artifact path and obtain a fresh adversarial recheck; or
2. weaken the corresponding statement so that the displayed assumptions
   genuinely imply it.

A separate ChatGPT Pro adversarial review completed on 2026-08-30 as a second
opinion. Every recoverable concrete objection was checked against the current
canonical source and repaired or dispositioned. The report remains an
AI-assisted author-side review, not external human peer review.

The unified release candidate currently compiles to 83 pages with local
post-review SHA-256
`6ff124cc1ae5f1504510c7a557cff1fe964c4ec24889e9e050294b56c9553885`.
Two clean builds of the post-review source under the pinned toolchain produced
byte-identical PDFs. The immutable-Release digest remains a later publication
gate.
The local quick, full, sources, finite-heavy, deterministic-materialization,
log, and representative-page visual gates have passed.

## Reproducibility deliverables

The final package should contain:

- the single canonical TeX source and PDF;
- a frozen Git commit;
- exact Python and TeX build specifications;
- machine-readable upper and lower parameters;
- all finite semantic metadata;
- an immutable manifest of the large CNF/DRAT pairs;
- the exact `drat-trim` source revision and a portable build procedure;
- logs that distinguish `PASS`, `SAT`, `UNSAT`, `UNKNOWN`, and `NOT_RERUN`;
- the adversarial reviews and their resolution record; and
- citation and licensing metadata approved for public release.

The heavy assets should be GitHub Release assets rather than ordinary Git
objects. Their public availability must be verified before the paper or
README calls the package public.

## Release sequence

1. **Completed locally:** resolve the mathematical and reproducibility review
   blockers.
2. **Completed locally:** regenerate and compile the unified manuscript twice
   with byte-identical output.
3. **Completed locally:** run quick, full, sources, and finite-heavy checks,
   including the semantic and DRAT replays.
4. **Completed locally:** inspect the final PDF and archive the build and
   verification records.
5. **Completed:** record the ChatGPT Pro review and its claim-by-claim
   disposition.
6. Push the final reviewed commit, require fast and full hosted verification
   on that exact commit, then create an
   immutable release containing exactly the manifest entries.
7. Verify the advertised process from a new clone without author-machine
   state.
8. Only then update the paper, README, status, and citation metadata with the
   real commit, release URL, version, date, and—if obtained—archival DOI.

Until those steps are complete, the correct label is **public source release
candidate**, not a completed immutable artifact release or published paper.
