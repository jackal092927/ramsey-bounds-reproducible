# Disposition of the September 3 Pro response

2026-09-03. The full response to source snapshot a46f408 is archived in [PRO_REVIEW_2026-09-03.md](PRO_REVIEW_2026-09-03.md), collected at 10:08:55 UTC after the UI reported “Worked for 155m 30s.” This document separates model proposals, independent deductions, finite computation, primary-source checking, and unresolved claims.

## Claim-by-claim decisions

| Claim / proposal | Decision and independent check | Consequence |
| --- | --- | --- |
| Spectator M'=M tensor I, shared-output horizontal interface, fraction threshold and known initial kernel | **RETAINED.** Direct operator identities and the anchored history construction agree with the existing corrections. | The previously retracted objections remain retracted. |
| All-chain concentration followed by injection/min-max | **CONDITIONAL PROOF SURVIVES.** The analytic hypothesis is distinct from distance to the unknown geometric kernel. | Multiplicity and quotient deductions are standard, not the main contribution. |
| Aggregate lifted-sector bound without t | **VALID; CREDIT CORRECTED.** The frozen packet already contained the aggregate sum in the padding appendix, reproduced in ../../round2/NORMALIZED_PERSISTENCE_PROBE.md. The final loose t factor also arose from a termwise bulk estimate. | Do not attribute the aggregate observation's first appearance in this project to the new Pro answer. |
| Improved Pro floor eta^54 g^27/t^26 | **VALID CONDITIONAL LOWER-BOUND SCALE.** It sharpens the earlier loose t^27 scaling under the imported package. | Superseded by the stronger local continuation below; actual gaps need not equal these powers. |
| Shared-register interface norm can scale as lambda sqrt(t) | **VALID under shared outputs.** Horizontal block-row norm squares sum L_i L_i*. | Does not prove that an additive t^2 lambda^2 error is unavoidable after retaining actual private mass U and absorbing it. |
| Generic projector rotation forces a t lambda term | **INSUFFICIENT AS AN OBSTRUCTION.** It addresses generic projector estimates, not the exact filling/differential structure. | New leakage estimates use squared private mass, exact annihilation and absorption. |
| Sharp two-projector lower bound | **ADOPTED with domains stated.** For 0<g<=1 and 0<alpha<=1, canonical two-projection blocks give gamma=(g+1-sqrt((g+1)^2-4g alpha))/2 >=g alpha/(g+1). | Taking the certified g=1/(8L^2), alpha=1/(3L) gives g2>=1/[3L(8L^2+1)]>=1/(27L^3). |
| Squared principal-angle expression for arbitrary eta<1 | **CORRECTED: MATHEMATICAL ERROR WITHOUT A SIGN CONDITION.** A lower bound a on a nonnegative overlap can be squared only when a>=0. Use max(0,a)^2. | The desired small-error application survives, for example eta<=1/10. |
| Preparation/overlap estimator | **RETAINED WITH COMPLETE ERROR BUDGET.** Include eta between the logical-history and harmonic mixtures, history-preparation error, projection/sampling error, and O(eta^2) overlap bias. | Do not silently treat the exactly known history mixture as the exact geometric harmonic mixture. |
| BQP1(G2) hardness by D=1 | **CONDITIONAL NARROW CONSEQUENCE.** Requires a source allowing the clean work used by the verifier; then the fraction is 0 or 1. | Does not resolve arbitrary-D rank-fraction complexity, BQP hardness, or unrestricted SDQC1 equivalence. |
| Generalized-rank formula for a common quotient diagram | **VALID STANDARD ALGEBRA under its common-quotient and diagram assumptions.** | A secondary structural extension, not a replacement for the global theorem. |
| Persistent-Laplacian extension | **RETAINED AS SECONDARY CONDITIONAL RESULT.** Ordinary-to-persistent domination is already in Mémoli–Wan–Wang's Theorem 5.1 proof. | The earlier novelty emphasis on that inequality is rejected; priority of the complete block theorem remains open. |
| Primary-source reading and absence-of-prior-work assertions | **NOT ADOPTED AS VERIFIED EVIDENCE.** The visible answer's Sources panel contained only the packet, a pasted document, and the GitHub packet. | The model's claimed paper reading and negative literature searches need independent source evidence. |
| Full palette / full reduction / paper readiness | **NOT CERTIFIED.** | A local theorem and one finite certificate are progress, not completion of the paper. |

The two-projection proof can be read directly on each nontrivial canonical block of a projection P onto the first kernel and an output projection R. A compression eigenvalue alpha' in [alpha,1] gives the 2-by-2 block of g(I-P)+R with trace g+1 and determinant g alpha'. Its smaller eigenvalue is bounded below by gamma(g,alpha). The remaining one-dimensional blocks have eigenvalues at least min(g,1); the common zero block is removed. This includes an empty common kernel. We use a chosen certified lower bound g<=1, not an asserted upper bound on the actual first gap.

## Explicit sign-condition counterexample

Take a common reference one-dimensional subspace P=span((1,1)/sqrt(2)), and
\[
Q_A=\operatorname{span}(1,0),\qquad
Q_B=\operatorname{span}(1,99).
\]
Both projector distances to P are below eta=0.8: respectively 1/sqrt(2) and 98/sqrt(19604). The expression
\[
a=\sqrt{1-\eta^2}\sqrt{1-\eta^2}-\eta^2=1-2\eta^2=-0.28
\]
has square 0.0784, while the squared overlap is only 1/9802. Thus squaring the negative lower bound is false. The corrected lower bound is max(0,a)^2. For equal errors eta<1/sqrt(2), a is positive and the intended bound applies.

The [finite fixture record](EXACT_FILLING_COERCIVITY_CHECKS.json) includes this guard and a counterexample to dropping the exact-filling hypothesis in the PSD domination lemma.

## Independent continuation beyond the response

1. **Exact-filling coercivity.** Hodge decomposition and ran Pi_i subset B_d(Y_i) imply Delta_i^up>=delta_i Pi_i, without commutation or comparison to an approximate lifted eigenvector. Summing gives Delta^up>=c lambda^kappa H^emb with no t.
2. **Quadratic geometric leakage.** Retaining actual private mass in the shared-register interference term and absorbing it gives N<=C[t lambda^2+(t+lambda^-kappa)e] under the earlier local spectral package. This is proved in [EXACT_FILLING_COERCIVITY.md](EXACT_FILLING_COERCIVITY.md).
3. **Simpler finite-certificate route.** A zero-weight kernel identity and a projected bulk singular bound yield the stronger leakage form N<=C[t lambda^2+(t+lambda^-2)e]. An elementary diagonal-scaling bound supplies a local positive floor c lambda^(4m+2), without spectral valuation. See [FINITE_CERTIFICATE_CONCENTRATION.md](FINITE_CERTIFICATE_CONCENTRATION.md).
4. **Improved global dependence.** Both routes give distance squared <=C[t lambda^2+e/(g lambda^kappa)]. Choose lambda independently of g. The conservative m<=6 scales are weighted Omega(eta^28 g/t^26) and, under common-copy unweighting, Omega(eta^26 g/t^24).
5. **Actual finite source certificate.** Replayed the pinned Rudolph representative and proved its target homology, intended filling, zero-weight kernel and projected central bulk injectivity with integer/modular calculations. Full evidence is in [REPRESENTATIVE_GADGET_CERTIFICATE.md](REPRESENTATIVE_GADGET_CERTIFICATE.md).
6. **Higher-simplex correction.** That graph has degree-5 simplices at target degree 3. The old two-bidegree enumeration is false; the repaired proof quantifies over every bidegree and uses the positive outside gap whenever the outside degree is not harmonic.

The 15 separate weighted-clique fixtures check the elementary coercivity mechanism, exact up additivity and kernel counts, including zero final kernels. They are not Rudolph/King--Kohler palette certificates. The actual representative calculation is separate, exact, and source pinned.

## Primary checks actually performed in this continuation

- King--Kohler arXiv:2311.17234v2: Lemma 9.1 statement and Claim 10.4's exact up-Laplacian sum. The complete spectral-sequence proof and final SIAM version were not reread.
- Hayakawa arXiv:2608.02726v1, Section 5, especially Lemma 5.4: explicit finite-family register quotient and use of earlier constructions/joins. This is not a new full theorem audit.
- Rudolph arXiv:2411.02681v2, Appendix D.1: displayed active states, sphere-join statement, distinction between algebraic two-qubit and numerical higher-locality checks, and supplementary-code reference.
- The linked source repository at commit 30ac70e5dacdecce97c38d801c128ec3ed93a96a: README/license and the inspected graph-building functions. Exact replay and certificates are documented separately.
- The earlier Mémoli–Wan–Wang check remains recorded in [POST_DISPATCH_SOURCE_UPDATE.md](POST_DISPATCH_SOURCE_UPDATE.md).

These checks support the specified ingredients. They do not establish a global novelty claim, unrestricted source-class equivalence, or that every source theorem has been independently verified.

## Next focused Pro gate

Attack the two new proof routes, with priority on the finite-certificate theorem: diagonal singular scaling, all-bidegree padding, retained-mass interface absorption, and direct logical coercivity. Either give a concrete counterexample under the exact hypotheses, or improve/prove the result. Then resolve the guarded-palette closure or identify the smallest concrete missing atom. Request precise source locations for any priority collision. The new request should include both the certificate graph data and checker, not only a summary.

