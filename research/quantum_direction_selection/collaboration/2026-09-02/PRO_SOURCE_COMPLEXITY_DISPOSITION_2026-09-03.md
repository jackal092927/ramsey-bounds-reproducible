# Source-complexity review — independent disposition

September 3, 2026. **RESTRICTED SOURCE COROLLARY ACCEPTED; UNRESTRICTED SDQC1 CLAIM STOPPED.** The [complete Pro response](PRO_SOURCE_COMPLEXITY_REVIEW_2026-09-03.md) is preserved with 113 displayed equation sources in its [capture record](PRO_SOURCE_COMPLEXITY_REVIEW_CAPTURE_2026-09-03.json). Pro did not independently reopen Lowe--Kim--Bondesan--Hayakawa or any other primary source; it reviewed the source excerpts and local algebra supplied in the packet. The prior targeted local source check remains recorded in [SOURCE_COMPLEXITY_GATE.md](SOURCE_COMPLEXITY_GATE.md).

## Mathematical disposition

The interval lemma is correct. For
\[
0\preceq M\preceq I,\qquad S=\ker(I-M),\qquad M|_{S^\perp}\preceq rI,
\]
with \(f=\dim S/D\) and \(p=\operatorname{Tr}M/D\),
\[
f\le p\le r+(1-r)f.
\]
Consequently a trace promise \(p\ge a\) versus \(p\le b\) guarantees only
\[
f_{\rm YES}\ge \ell:=\max\!\left\{0,\frac{a-r}{1-r}\right\},
\qquad f_{\rm NO}\le b.
\]
The exact-fraction reduction separates the two promise cases precisely when
\[
\delta_f:=\ell-b>0
\]
(up to the finite-dimensional rational grid). The Pro response's same-\(f\) construction proves necessity under these operator promises: on a \(qD\)-dimensional subspace take \(M_N=I\oplus0\), while on its complement take \(M_Y=I\oplus\alpha I\) with \(\alpha=(a-q)/(1-q)\le r\). The two operators can satisfy opposite trace promises while having the same exact perfect-space fraction whenever the intervals overlap.

The amplification objection is also correct. Any exact amplification that preserves \(S\), perhaps tensored with a fixed ancilla, preserves \(f\) and drives the amplified normalized trace toward \(f\). It cannot recover an arbitrary original trace separation carried only by eigenvalues below one. This is a mathematical obstruction to that inference, not merely a novelty concern.

The spectator calculation remains exact:
\[
U'=U\otimes H_a^h,\quad J'=J\otimes I_a,\quad
P'_{\rm acc}=P_{\rm acc}\otimes I_a
\quad\Longrightarrow\quad M'=M\otimes I_a
\]
for either parity of \(h\). It implements single Hadamards for circuits already over the stated real gate family. It does not prove exact amplification in that family or conversion from arbitrary gate sets.

## Accepted consequence

Define the explicit circuit promise
\(\operatorname{SepPerfectFraction}^{\mathcal G_R}(a,b,r)\) using the exact gate set
\(\mathcal G_R=\{X,\mathrm{CX},\mathrm{CCX},H\}\), maximally mixed inputs, computational-basis clean ancillas, a fixed-local computational-basis output measurement, the off-perfect ceiling \(r\), the trace alternatives \(p\ge a\) or \(p\le b\), and \(\delta_f\ge1/\operatorname{poly}(n)\).

Conditional on the accepted geometric transfer theorem, this promise reduces in polynomial time to true normalized persistence with
\[
\beta_d(X_{\rm in})=D,\qquad
\beta_d(X_{\rm in}\to X_{\rm out})=\dim S,
\qquad q=f,
\]
and with inverse-polynomial gaps above both whole geometric kernels. Additive error \(<\delta_f/2\) decides the source. At \((a,b,r)=(2/3,1/3,1/3)\), the target cases are \(f\ge1/2\) and \(f\le1/3\); \(1/24\) error is safe.

The quotient theorem directly establishes the restricted rank conclusion sought by the source's Conjecture 1. It bypasses Conjecture 2 as a sufficient mechanism; it does not prove Conjecture 2's exact compatible harmonic-isometry identities.

## Claims rejected or withheld

- **Mathematical rejection:** arbitrary-threshold trace separation alone implies exact perfect-fraction separation.
- **Mathematical rejection:** perfect-subspace-preserving amplification repairs that implication.
- **Unproved:** an exact transformation that creates a separated perfect subspace from an arbitrary-threshold verifier while preserving the required interface, gate set, and spectral ceiling.
- **Complexity-significance risk:** one may define a restricted class named \(\operatorname{SepSDQC}_1^{\mathcal G_R}\), but no equivalence with a recognized unrestricted class is established. The explicit circuit-promise formulation carries the actual content and should be the headline.
- **Novelty risk:** this review did not compare the geometric theorem with the literature. It supports no priority or paper-readiness conclusion.

The hard stop is unchanged for BQP, DQC1, and unrestricted SDQC1. After this response was collected, a separate local derivation produced the [eight-label \(\mathsf{BQP}_1^{G_2}\) source](NORMALIZED_BQP1_SOURCE_GATE.md). That construction does not contradict the same-fraction obstruction: it deliberately maps a perfect-completeness source to separated perfect fractions. Its algebra and Rudolph source interface passed a local check, but it was not considered by this Pro response and requires a new bounded interface audit before the named-source upgrade is treated as externally reviewed. Novelty remains a later independent gate.
