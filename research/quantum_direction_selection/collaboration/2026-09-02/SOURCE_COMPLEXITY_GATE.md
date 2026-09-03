# Source-complexity gate for the restricted normalized-persistence theorem

September 3, 2026. **TARGETED PRIMARY-SOURCE AND ALGEBRA CHECK; UNRESTRICTED CLASS HARDNESS NOT ESTABLISHED.** This note asks what complexity consequence actually follows from [CLEAN_RESTRICTED_REDUCTION_THEOREM.md](CLEAN_RESTRICTED_REDUCTION_THEOREM.md). It separates a valid fixed-threshold source from the stronger arbitrary-threshold \(\mathsf{SDQC}_1\) claim.

## 1. Primary source checked

The primary source checked here is Lowe--Kim--Bondesan--Hayakawa, [arXiv:2607.03278v1](https://arxiv.org/html/2607.03278v1), specifically:

- Definition 2 in Section 3, which defines gate-set-dependent \(\mathsf{SDQC}_1\) using a perfectly accepted subspace, soundness at most \(1/3\) on its orthogonal complement, and arbitrary trace thresholds \(a-b\ge1/\operatorname{poly}(n)\);
- Section 3.1, especially equation (9), which says amplified acceptance is within a small additive amount of the normalized dimension of the perfect subspace;
- Sections 5.5--5.6, which use this normalized dimension for LEKD and local-Hamiltonian Normalized Persistence hardness;
- Section 7, Conjectures 1--2 and Lemma 11, which isolate exact kernel fidelity, whole-kernel gaps, and filtration-compatible encodings as the missing TDA ingredient.

This was a targeted read of the arXiv HTML, not a complete paper audit or a check of later versions. The six-source novelty ledger was not reverified.

## 2. Exact rank--trace lemma

Let
\[
0\preceq M\preceq I,
\qquad
S=\ker(I-M),
\qquad
M|_{S^\perp}\preceq rI,
\]
and put
\[
f=\frac{\dim S}{D},
\qquad
p=\frac{\operatorname{Tr}M}{D}.
\]
Then
\[
f\le p\le f+r(1-f)=r+(1-r)f.
\tag{1}
\]
Thus trace promises \(p\ge a\) and \(p\le b\) imply
\[
f_{\rm YES}\ge \max\!\left\{0,\frac{a-r}{1-r}\right\},
\qquad
f_{\rm NO}\le b.
\tag{2}
\]
The guaranteed fixed-space gap is therefore
\[
\delta_f=\max\!\left\{0,\frac{a-r}{1-r}\right\}-b.
\tag{3}
\]
A reduction through the exact kernel fraction requires \(\delta_f>0\).

For \((a,b,r)=(2/3,1/3,1/3)\), equation (3) gives
\[
f_{\rm YES}\ge\frac12,
\qquad
f_{\rm NO}\le\frac13,
\qquad
\delta_f=\frac16.
\]
An estimate with additive error strictly below \(1/12\), such as \(1/24\), decides this fixed-threshold promise.

## 3. Arbitrary trace gaps do not determine the perfect fraction

The user-supplied operator counterexample is decisive:
\[
M_{\rm YES}=\frac14 I_D,
\qquad
M_{\rm NO}=0.
\]
Both have \(S=0\) and hence \(f=0\), while their normalized traces are \(1/4\) and \(0\). They obey the off-perfect ceiling \(r=1/3\), so thresholds \(a=1/4,b=0\) distinguish their traces but no exact-kernel-fraction oracle can distinguish them.

This refutes the algebraic inference from an arbitrary inverse-polynomial trace gap to a perfect-subspace-dimension gap. It does not assert that this particular pair is realized by every fixed exact gate set.

The amplification statement in source equation (9) does not by itself repair the issue. If amplification preserves \(S\) exactly and suppresses all acceptance on \(S^\perp\), its new acceptance probability approaches \(f\). Two inputs with the same \(f\) remain indistinguishable by that quantity even if their original traces were separated. A valid unrestricted reduction needs an additional promise implying \(\delta_f>0\), or a different exact transformation whose perfect-space dimension encodes the original decision quantity. Merely reducing \(r\) while preserving \(S\) is insufficient.

This is a mathematical objection to the displayed arbitrary-threshold rank inference in the checked version of the source, not a complete verdict on the paper. A hidden circuit-specific invariant or a later correction could change the conclusion; none was identified in the checked sections.

## 4. Strongest immediate source statement

Define the explicit separated source promise \(\operatorname{SepPerfectFraction}^{\mathcal G_R}(a,b,r)\) by the standard mixed-input/clean-output circuit interface, exact gate family
\[
\mathcal G_R=\{X,\mathrm{CX},\mathrm{CCX},H\},
\]
and conditions (1)--(3) with \(\delta_f\ge1/\operatorname{poly}(n)\). The exact spectator construction converts \(\mathcal G_R\) circuits to the certified \(G_2\) palette while doubling \(D\) and \(\dim S\), so \(f\) and \(r\) are unchanged.

The clean reduction theorem then gives a polynomial many-one reduction from this promise to weighted clique-complex normalized harmonic persistence, with precision below \(\delta_f/2\), exact denominator \(D\), exact persistent rank \(\dim S\), and inverse-polynomial gaps above both whole kernels. At the standard constants, the required target precision may be fixed at \(1/24\).

This is a mathematically valid complexity corollary for an explicit source promise. One may optionally define a gate-dependent restricted class \(\operatorname{SepSDQC}_1^{\mathcal G_R}\) around this promise, but that name supplies no equivalence with a recognized class. Calling the target unrestricted \(\mathsf{SDQC}_1\)-hard requires two additional results that are not currently in the archive:

1. a theorem equating the arbitrary-threshold source definition with its separated fixed-threshold version while preserving the exact perfect subspace; and
2. exact gate-set compatibility for the amplification or source reduction, rather than approximate compilation between universal gate sets.

The primary source explicitly notes that \(\mathsf{SDQC}_1\) depends on the gate set because no general perfect-completeness-preserving gate-set reduction is known. The present theorem therefore supports at most a real-gate, explicitly separated variant until this is resolved.

## 5. Relation to the source conjectures

For the supported history family, the current construction proves the numerical conclusions needed for Normalized Harmonic Persistence directly:
\[
\beta_d(X_1)=\dim\ker H_1,
\qquad
\beta_d(X_1\to X_2)=\dim\ker H_2,
\]
with natural quotient maps and inverse-polynomial endpoint gaps. This bypasses the need to identify geometric harmonic representatives with logical kernel vectors by one exact common harmonic isometry.

Consequently it may establish the source's Conjecture 1 for the separated real-gate source even though it does not prove every operator-level isometry identity demanded by Conjecture 2. That distinction is potentially valuable: Conjecture 2 is a sufficient route, not logically necessary for the rank statement.

## 6. Completed Pro audit and decision gate

The bounded source-complexity request is now [completed and archived](PRO_SOURCE_COMPLEXITY_REVIEW_2026-09-03.md), with a separate [independent disposition](PRO_SOURCE_COMPLEXITY_DISPOSITION_2026-09-03.md). The response independently rederived the exact intervals, supplied a general same-fraction YES/NO construction showing necessity of \(\delta_f>0\), confirmed the spectator identity for either Hadamard parity, and located the first invalid unrestricted inference at the trace-to-perfect-fraction step. It performed no primary-source checking; all source statements were inherited from this note's packet.

**GO** for the explicit \(\operatorname{SepPerfectFraction}^{\mathcal G_R}\) reduction and its restricted Conjecture-1 rank conclusion. At \((a,b,r)=(2/3,1/3,1/3)\), the reduction has target gap \(1/6\) and safe additive error \(1/24\).

**STOP the unrestricted hardness claim.** No exact upgrading or gate-set-equivalence theorem is in the archive. Retain the representation/transfer theorem and the separated-promise corollary, and present arbitrary-threshold \(\mathsf{SDQC}_1\) as open. Classical reversible predicates give growing \(D\) and exact \(f=p\), but their constant additive-gap promise is sampleable and supplies only a baseline, not the desired quantum-hard source.

## 7. Later recognized-source upgrade

The completed Pro audit above correctly stopped the unrestricted inference but did not exhaust narrower recognized sources. A later local construction, recorded in [NORMALIZED_BQP1_SOURCE_GATE.md](NORMALIZED_BQP1_SOURCE_GATE.md), starts with a clean-input \(\mathsf{BQP}_1^{G_2}\) circuit of acceptance probability \(p_x\) and uses eight mixed labels to obtain

\[
M_x=\operatorname{diag}(1,p_xI_5,0I_2)\otimes I_{\rm dummy}.
\]

Its YES and NO perfect-space fractions are exactly \(3/4\) and \(1/8\), respectively, while the NO off-perfect spectrum is at most \(1/3\). The algebra and circuit interface have passed a separate [independent local review](NORMALIZED_BQP1_SOURCE_GATE_INDEPENDENT_REVIEW.md), and Rudolph's exact-gate theorem was checked at the primary source.

This changes the decision as follows:

- **LIMITED GO:** the weighted, whole-kernel-gapped normalized-persistence target has a locally proved \(\mathsf{BQP}_1^{G_2}\)-hard route under the recorded clean geometric theorem hypotheses;
- **STILL STOPPED:** unrestricted \(\mathsf{SDQC}_1\), ordinary \(\mathsf{BQP}\), and gate-independent arbitrary \(\mathsf{BQP}_1\) hardness;
- **CONDITIONAL:** the unweighted conclusion still depends on a separate common-copy unweighting theorem.

The bounded Pro audit and independent disposition have now accepted this exact interface under the displayed hypotheses. The next gate is no longer source existence; it is primary-source novelty and positioning against nearby harmonic-persistence hardness.
