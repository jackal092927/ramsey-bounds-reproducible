# Final targeted adversarial review

**Date:** 2026-08-30  
**Object reviewed:** the unified Ramsey-bounds manuscript and its pinned
computational evidence  
**Review mode:** three independent hostile reconstructions, one for each
headline result, followed by author-side verification and disposition

## 1. Executive verdict

No fatal or major mathematical defect was found.  Each headline result is
supportable only at the scope printed in the revised manuscript:

| Part | Verdict | Smallest safe interpretation |
|---|---|---|
| I: diagonal upper bound | Proved relative to the three version-locked Yang--Mao interfaces | Conditional/source-relative upper bound with certified constant \(3.780685290\) |
| II: fixed-ratio lower rate | Proved under the explicit interfaces S1--S5 | Conditional, fixed-\(C\), non-effective rate improvement; S3 remains an extra hypothesis |
| III: finite edit distance | Certified relative to the disclosed SAT/DRAT trust boundary | Every qualifying graph is at one-sided deletion distance at least seven from the fixed seed |

The manuscript does **not** establish the exact value of the finite edit
distance, a seven-deletion repair, \(R(3,18)\ge 101\), an unconditional
improvement to a published Ramsey theorem, or a proof-assistant-checked result.

## 2. Part I: upper-bound reconstruction

The reviewer checked the pinned Yang--Mao source interface, the local BookCor
proof, the finite-net descent, all six rate certificates, the max--min transfer,
and the exact diagonal endpoint.  An independent high-precision evaluation
gave
\[
U(1)=1.3299087618219930723187812632\ldots
\]
and
\[
\exp\!\left(U(1)-3.4754\cdot10^{-6}\right)
=3.7806852883796401133523716774\ldots
<3.780685290.
\]
The four 512-bit transfer replays and the upper audit tests were also
re-executed successfully.

Three minor presentation gaps were found and repaired:

1. The monotonicity argument for the exact diagonal denominator now displays
   \(D'(u)>4e^u-e^{u/2}>0\) on the relevant interval.
2. The passage to the diagonal envelope now separates the immediate \(M\le0\)
   case from the \(M>0\) substitution.
3. The dependency discussion now distinguishes external Yang--Mao interfaces,
   locally proved lemmas such as BookCor, and Arb containment as a computational
   trust component.

No stronger unconditional claim is licensed by this audit.

## 3. Part II: lower-bound reconstruction

The reviewer independently fetched the pinned HMS and Lin--Niu source files
and matched their SHA-256 identities.  The audit reconstructed:

- the distinction between \(p_C\) and the actual Gaussian edge probability
  \(p=p_C+C^{-1}\);
- conditioning on a fixed admissible history before applying the truncated
  Gaussian comparison;
- the three-factor Hölder/CGF ledger without double counting;
- the residual payment, exposure multiplicities
  \(K_r=\binom r3+2\binom r4\), and square penalty;
- extraction losses and the positive remaining exponent; and
- the red/blue crossing and the order of limits.

Within the explicitly defined scalar residual class, the audit confirmed the
meaning of
\[
\widehat H_*(C)=\frac{1+o(1)}{64\log C}.
\]
It is not a universal cap over adaptive, matrix-valued, higher-order, or other
Ramsey methods.

Three minor evidence/status problems were found and repaired:

1. S3 had been described both as an extra hypothesis and as locally proved.
   The revised text keeps S3 as an extra source interface and says only that
   the displayed algebra records what S3 must preserve.
2. The lower replay script no longer prints an overbroad theorem-reproduced
   sentinel; it now reports arithmetic-certificate reproduction.
3. A hash-frozen pre-canonical route note retains historical wording.  Rather
   than mutate that provenance object, the manuscript explicitly identifies it
   as pre-canonical and states that its old labels do not override the unified
   theorem statement.

Thus the safe conclusion remains conditional on S1--S5, fixed-\(C\), and
non-effective.  The arithmetic replay does not discharge the source-level
reverse-induction hypotheses.

## 4. Part III: finite SAT/DRAT reconstruction

The reviewer checked the one-sided deletion metric, the logical direction of
the CNF relaxation, the exhaustive three-way branching on the fixed seed
triangle, the budget-five/exact-six splice, and the fact that all original
nonedges remain free addition variables.  It also checked that semantic
reconstruction binds every DIMACS component to the stated graph problem and
that an UNKNOWN exact-seven search is never treated as nonexistence.

The certified implication is
\[
\alpha(F)<18,\quad F\text{ triangle-free}
\quad\Longrightarrow\quad
|E(H)\setminus E(F)|\ge7
\]
for the fixed labelled seed \(H\), subject to the disclosed PySAT,
semantic-reconstruction, drat-trim, compiler, and hardware trust boundary.

Three minor evidence issues were found and repaired:

1. The DRAT wrapper now requires an exact stripped status line
   “s VERIFIED” rather than accepting a substring.  The documentation also
   correctly allows checker timing lines to follow that status line.
2. A historical JSON field that encoded an unknown exact-seven proposition as
   false is now null, consistent with the adjacent status text.
3. The artifact-ledger introduction now distinguishes compressed and
   explicitly listed uncompressed digests.

These repairs do not change the certified lower bound seven.  They also do not
establish equality, find a seven-deletion repair, or imply a global Ramsey
number improvement.

## 5. Release and supply-chain audit

The public-release workflow was separately reviewed before publication.
Hosted action dependencies are pinned by full commit identity; runners are
pinned to Ubuntu 24.04; the release verifier checks the annotated tag object,
the dereferenced source commit, release immutability, the exact asset-name and
digest set, GitHub's release attestation, each asset verification result, and a
credential-free finite replay.

The downloader refuses draft, prerelease, mutable, incomplete, extra, renamed,
or digest-mismatched releases.  Publication must still proceed in this order:
push the verifier, pass full CI, create and verify the annotated tag, upload the
exact manifest set to a draft, validate it, publish once, and replay from an
anonymous clone.

This section records an audited protocol, not a claim that the final immutable
Release already existed at the time of this review.

## 6. Remaining pre-publication gates

At the close of this targeted review:

- all nine minor findings above were disposed;
- no fatal or major mathematical finding remained;
- the independent whole-paper review likewise reported no fatal or major
  mathematical defect;
- the separate ChatGPT Pro adversarial report was still running and therefore
  had not yet been incorporated;
- the final byte-reproducible PDF build, final hosted full verification,
  immutable Release publication, and credential-free post-release replay were
  still pending.

Consequently this report supports the revised scoped claims, but it is not
itself a substitute for the remaining release gates or for external human peer
review.

## Post-review status note

The running-state sentence above is preserved as the historical state at this
review's close. The ChatGPT Pro report subsequently completed; its concrete
objections, repairs, and dispositions are recorded in
`reviews/CHATGPT_PRO_REVIEW.md`. The immutable Release and credential-free
post-release replay remain separate open gates.
