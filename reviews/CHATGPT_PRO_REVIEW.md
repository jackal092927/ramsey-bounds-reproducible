# ChatGPT Pro adversarial-review report and local disposition

Date received: 2026-08-30  
Scope: the pre-final unified manuscript uploaded to a private ChatGPT thread,
followed by line-by-line comparison with the current repository source  
Reviewer type: AI second opinion in ChatGPT Pro; not external human peer review

## Acquisition and evidence boundary

The review completed in the same private ChatGPT conversation to which the
manuscript had previously been transmitted. Before reading the result, the
account identity and Pro plan were rechecked in the visible account settings.
No follow-up prompt, file, or message was sent during retrieval.

The ChatGPT interface does not expose a digest for the uploaded PDF. The upload
preceded the current post-review source and must therefore be treated as a
review of a pre-final candidate. The reviewer also did not have a live view of
the repository's tracked certificate files or local large SAT artifacts. The
accessible final response began at its section 8.2; every visible item in
sections 8.2--10 was captured and normalized below. This file does not pretend
that an inaccessible earlier portion was recovered verbatim.

## Reviewer's headline verdict

The reviewer assigned **MAJOR REVISION** to the uploaded candidate. Its main
reason was not a discovered numerical counterexample. Rather, it considered
several theorem dependencies and computational objects insufficiently explicit
or unavailable to a PDF-only reviewer.

The review explicitly reported that it found no instance of the following
failure modes:

- a reversed max--min or outer endpoint;
- substitution of \(p\) for \(p_C\);
- an unpaid extraction multiplicity or a missing red--blue gap;
- an overbroad \(1/64\) method class in the current statement;
- an inverted CNF-relaxation implication;
- a nonexhaustive three-triangle-edge branch split; or
- an inference of existence or nonexistence from an `UNKNOWN` solver endpoint.

## Concrete findings and current dispositions

| area | Pro objection | current disposition |
|---|---|---|
| upper rate chain | The first prior was described only as "the same elementary witness," without printing its coefficient tuple or a theorem that starts the chain. | **VALID AND REPAIRED.** Appendix C now states \(c^{(0)}=(-1/4,2/25,2/25)\), prints \(F_0\), the exact splice, the analytic small-ratio obligation, the 4,096-cell 256-bit Arb obligation, and the finite-net implication proving the uniform prior rate. |
| upper source interface | A PDF-only reader could not know the exact Yang--Mao member and imported conclusions. | **CURRENTLY FIXED / REVIEW OF STALE PRESENTATION.** The current source names arXiv:2608.01962v1, authenticates the imported member, maps exact source lines, and states all three imported conclusions in the theorem interface. |
| upper half-line proof | The repair checklist requested a complete half-line argument. Local cross-checking found that the manuscript jumped from \(D'(u)>0\) to monotonicity without printing the already checked gate \(D(2.9)>0\). | **VALID LOCAL FINDING AND REPAIRED.** The base gate and the two-step implication \(D>0\Rightarrow B_T'>0\) are now explicit. |
| upper arithmetic precision | The candidate did not make the 256-bit rate-chain layer and 512-bit final-transfer layer sufficiently easy to distinguish. | **VALID CLARITY ISSUE AND REPAIRED.** The computation section now separates the two layers and states that structurally different implementations still share the Arb containment kernel. |
| upper machine objects | The reviewer could not inspect six JSON certificates, exact-diagonal cells, outer-wedge checks, accepted logs, or source snapshots from the PDF alone. | **MOSTLY A PDF-ONLY AVAILABILITY LIMIT.** All six JSON files, their complete hashes, all tracked checkers, and the deterministic rational cell-generation code are in the public source repository. The cells are generated partitions, not missing data files. External source members are version-pinned and hash-checked on download. Public immutability of the final tagged snapshot remains a release gate. |
| upper parser | The repair checklist requested fail-closed parsing and outward-decimal discipline. | **HARDENED POST-REVIEW.** The canonical loader rejects duplicate keys, unknown or missing fields, non-string numeric data, and non-finite decimals; canonical mode also enforces filenames, order, file hashes, and the final displayed tuple. The final base is printed from an outward upper enclosure. |
| lower hidden constant | The reviewer requested an explicit source-error constant \(K\), \(C_0(K)\), and a finite-\(C\) source theorem. | **CURRENTLY FIXED, WITH NOTATION STRENGTHENED.** The source now fixes one non-effective absolute \(K\), defines \(B_R(C)\), and makes explicit that \(\vartheta_C\), \(B_R(C)\), and \(C_0\) suppress their dependence on \(K\). The order is: fix \(K\); for each sufficiently large fixed \(C\) and fixed \(w>\omega_0\), take \(\ell\to\infty\); then let \(w\downarrow\omega_0\); only afterward study \(C\to\infty\). |
| lower S3 provenance | The source scalar baseline, the additional weighted implication, and the local nonuniform comparison were too tightly bundled in one item. | **VALID MINOR AND REPAIRED.** The scalar baseline is now part of (S2), only \((2.37)\Rightarrow(2.38)\) is the additional (S3) hypothesis, and the total-probability/projection identities are explicitly explanatory rather than a proof of S3. |
| lower histories and notation | The reviewer requested \(\mathfrak H^R_{r,i-1}\) histories and definitions of \(t_0,Q_0,u_j^0\) before use. | **HISTORIES WERE ALREADY FIXED; NOTATION REPAIRED.** "Red-admissible" was already defined as membership in \(\mathfrak H^R\). The post-review source now defines \(t_0\) and \(u_j^0\) at their first source-interface use; \(Q_0\) is defined where the reverse-induction state is introduced. |
| lower \(1/64\) scope | The reviewer warned against a universal optimality statement. | **CURRENTLY FIXED / REVIEW AGREES.** The cap applies only to Definition 16.1's scalar residual class and expressly excludes adaptive, matrix, and higher-order methods. |
| finite counter semantics | Clause regeneration used PySAT's sequential counter, but the paper did not give a constructive proof of its projection semantics. | **VALID TRUST-BOUNDARY HARDENING AND REPAIRED.** The finite part now proves the prefix-threshold sequential-counter lemma. A separate implementation that does not import PySAT regenerates the at-most-four and exact-five blocks, checks their clause digests and dimensions, constructs satisfying auxiliary assignments, and compares all six stored blocks when the release assets are present. |
| finite seed independence number | The reviewer asked whether \(\alpha(H)<18\) was proof-carrying rather than merely executable. | **ACCURATELY DELIMITED.** It is an exhaustive trusted-code check with small-instance cross-checks, not a DRAT or proof-assistant certificate. The text now emphasizes that this descriptive seed fact is not a premise of the deletion-barrier implication. |
| finite assets | A PDF-only reviewer could not replay the six budget-five and six exact-six CNF/DRAT assets. | **OPEN PUBLIC-RELEASE GATE, NOT A HIDDEN THEOREM CLAIM.** The twelve local payloads have already passed manifest authentication, semantic reconstruction, and DRAT replay. The final immutable GitHub Release has not yet been published, so the manuscript and README continue to describe public artifact replay as pending. |
| exact seven and global \(R(3,18)\) | The reviewer required project-relative wording and no inference \(R(3,18)\ge101\). | **CURRENTLY FIXED / REVIEW AGREES.** The package establishes neither \(\rho(H)=7\) nor \(\rho(H)\ge8\); all exact-seven branches remain `UNKNOWN`, and no global Ramsey-number improvement is claimed. |

## Post-Pro adversarial hardening

Combining the Pro objections with an independent source-to-PDF comparison
exposed three additional integration defects. None supplied a mathematical
counterexample, but one was statement-corrupting and therefore a submission
blocker until repaired:

1. The materializer globally replaced every parenthesized equation number.
   It consequently transformed the intended function evaluation `D(2.9)` into
   an equation reference while LaTeX still compiled. Replacement is now
   context-sensitive, appendix-to-main references have explicit scope maps,
   and regression tests cover both cases.
2. The finite-heavy orchestration passed DRAT-specific options to the new
   independent sequential-counter checker. The semantic checker and DRAT
   replayers now have separate, correctly typed invocations; the complete
   finite-heavy route subsequently passed.
3. Four missing backslashes before `\qquad` and a floating table that interrupted
   a proof sentence were corrected. The final PDF was visually rechecked at
   each affected page, and the repository verifier now detects recurrence of
   the bare token.

These repairs changed no theorem, constant, certificate, or SAT conclusion.
They do show why source-to-rendered-output comparison was necessary in addition
to successful compilation and numerical replay.

## Safe theorem statements after disposition

The strongest submission-safe statements remain:

1. Conditional on the exact version-pinned Yang--Mao source interface, the
   repaired local book induction, the six accepted rate certificates, the
   exact-diagonal certificate, the outer-wedge certificate, and Arb containment,

   \[
   R(k,k)\le \exp((U(1)-0.0000034754)k+o(k))
   \le (3.780685290)^{k+o(k)},
   \]

   with certified unrounded base below `3.780685288379640114`.

2. After fixing the non-effective source constant \(K\), and conditional on
   (S1), (S2), (S4), (S5), plus the additional weighted-extension hypothesis
   (S3), the fixed-ratio exponent receives the source-relative term

   \[
   \widehat H_*(C)=\frac{1+o(1)}{64\log C}
   \]

   in the stated order of limits. This is not an unconditional Ramsey
   improvement with S3 removed.

3. For the specified content-addressed labelled seed \(H\), every triangle-free
   \(F\) with \(\alpha(F)<18\) satisfies \(d_H(F)\ge7\), with additions outside
   \(E(H)\) free. This neither determines the exact radius nor implies
   \(R(3,18)\ge101\).

## Submission stop rules

No submission or immutable artifact release should describe the package as
fully publicly reproducible until the final tag, exact twelve-asset Release,
credential-free download, and clean-clone final-tag replay have passed. No
future edit may remove the Yang--Mao trust boundary, the additional status of
(S3), the conventional SAT/DRAT trusted kernel, or the exact-seven and global
\(R(3,18)\) disclaimers without new proof.

After the repairs above, neither the Pro report nor the independent local
reconstructions supply a known counterexample to any of the three scoped
statements. This is a stronger author-side correctness check, not a substitute
for anonymous external human peer review.
