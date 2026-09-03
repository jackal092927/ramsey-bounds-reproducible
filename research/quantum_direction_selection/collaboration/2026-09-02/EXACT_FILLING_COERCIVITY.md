# Exact filling gives direct logical coercivity

2026-09-03. **LOCAL DERIVATION, CONDITIONAL ON THE EXPLICIT LOCAL PACKAGE BELOW.** This is a new continuation after collecting [the Pro response](PRO_REVIEW_2026-09-03.md). Its abstract proof has been checked locally; the complete supported clique-gadget palette and priority have not been certified. This note is the proposed object of the next focused Pro review.

The strongest improvement here is linear dependence on the promised logical gap. The gadget weight can be chosen without multiplying it by that gap. A second refinement controls mass outside the register by a quadratic, rather than linear, perturbation term. Neither statement identifies geometric harmonic vectors literally with logical ones.

## 1. Setting and exact local inputs

Let R be a register complex of top dimension d, V=Z_d(R), and P its orthogonal projector. Register vertices have weight one. For t>=1, attach gadgets Y_i with disjoint new vertices and no simplex containing new vertices from different gadgets. In normalized chain coordinates,
\[
C_d(X)=C_R\oplus\bigoplus_{i=1}^t C_i^{\rm priv},\qquad C_R=C_d(R).
\]
For x=omega_0+sum_i omega_i write x_i=omega_0+omega_i and let iota_i embed the corresponding single-gadget chain space into C_d(X).

Each logical constraint Pi_i is an orthogonal projector supported on V. Set H=sum_i Pi_i, let P_K project onto ker H inside V, and assume
\[
H\succeq g(P-P_K),\qquad 0<g\le1.
\]
H is logical; Delta is geometric. All constants below depend only on a fixed finite palette. There exist 0<lambda_0<=1 and c_0,C_0>0, with fixed kappa>=2, such that, for 0<lambda<=lambda_0:

1. Exact filling holds: ran Pi_i is contained in B_d(Y_i). For the quotient conclusion use equality B_d(Y_i) intersect V = ran Pi_i. Let K_i be the full single-gadget harmonic projector. Thus K_i Pi_i=0 exactly.
2. The local whole positive gap obeys Delta_i >= c_0 lambda^kappa (I-K_i), and
   \[
   \|K_i-(P-\Pi_i)\|\le C_0\lambda.
   \]
   This is an operator-norm bound after padding, obtained in fixed local dimension before tensoring.
3. There is an orthogonal spectral decomposition I=K_i+F_i+B_i+A_i, with A_i the high sector, B_i the bulk sector, and F_i the lifted constraint sector. Assume
   \[
   \Delta_i\succeq c_0 A_i,\qquad
   \Delta_i^\uparrow\succeq c_0\lambda^\kappa F_i.
   \]
4. For the corrected local-bulk tensor outside-harmonics projector Q_i and the projected differential pair T_i,
   \[
   \|B_i-Q_i\|\le C_0\lambda,\quad
   \|T_i\|\le C_0\lambda,\quad
   \|T_iQ_i z\|\ge c_0\lambda\|Q_i z\|.
   \]
   T_i is a projection of the actual boundary/coboundary pair, so T_iK_i=0. Its output retains a new vertex of gadget i. Consequently
   \[
   \sum_i\|T_i x_i\|^2\le
   e:=\langle x,\Delta x\rangle.
   \]
   This output orthogonality concerns T_i, not the register-output interface.
5. The latter interface is L_i=Pi_reg^{d-1} partial Pi_i^{priv}, with
   \[
   L_iL_i^*\preceq N_*\lambda^2I,\qquad
   \rho=\lambda^{-2}\|[L_1\ \cdots\ L_t]\|^2\le N_*t.
   \]

The normalized chain basis, common weights, and embeddings must agree at every level. Exact filling may be deduced from the local nullity, kernel limit, and weight gauge as in the existing dossier; no global gap is used in that deduction.

## 2. Direct up-Laplacian domination

**Lemma.** If ran Pi_i is a subspace of the local boundary space and the local whole positive gap is at least delta_i, then
\[
\Delta_i^\uparrow\succeq\delta_i\Pi_i.
\]

**Proof.** The Hodge decomposition splits the local chain space orthogonally into boundaries, harmonics, and coboundaries. On boundaries, Delta_i^\uparrow equals Delta_i; on the other two summands Delta_i^\uparrow vanishes. Hence
\[
\Delta_i^\uparrow\succeq
\delta_i P_{B_d(Y_i)}
\succeq\delta_i\Pi_i.
\]
The second inequality uses exact subspace containment, not a perturbative comparison with a lifted eigenvector. No commutation between Pi_i and Delta_i is required. This is a standard PSD consequence of exact filling. ∎

Since R has no (d+1)-simplices and the interiors are independent, all global up-boundary columns are partitioned by gadget:
\[
\Delta^\uparrow=\sum_i\iota_i\Delta_i^\uparrow\iota_i^*.
\]
Taking delta_i>=c_0 lambda^kappa gives
\[
\boxed{\Delta^\uparrow\succeq c_0\lambda^\kappa H^{\rm emb}},
\qquad
\boxed{\langle x,H^{\rm emb}x\rangle\le e/(c_0\lambda^\kappa)}. \tag{1}
\]
There is no factor t in (1). Its filling hypothesis is essential: with Delta^\uparrow=diag(1,0) and Pi=diag(0,1), no positive multiple of Pi is dominated.

This observation already improves the logical-gap dependence if combined with the Pro aggregate concentration estimate. Dropping its nonnegative H term bounds leakage outside V; (1) then bounds the forbidden logical component separately. There is no reason to divide the entire structural remainder by g.

## 3. Keep the actual interior mass in the interface estimate

For normalized x define
\[
U=\sum_i\|\omega_i\|^2,\quad
S=\sum_i\|(I-K_i)x_i\|^2,\quad
\chi=(t-2)_+\rho+N_*\le C t^2.
\]
Let a=partial_R omega_0, y_i=L_i omega_i, and y=sum_i y_i. The global register boundary is r=a+y; all non-register boundary outputs are in disjoint blocks.

The identity
\[
\sum_i\|y-y_i\|^2=(t-2)\|y\|^2+\sum_i\|y_i\|^2
\]
and the block-row bounds imply
\[
\sum_i\|y-y_i\|^2\le\chi\lambda^2 U.
\]
Using a+y_i=r-(y-y_i) and additivity of up energy,
\[
\sum_i\langle x_i,\Delta_i x_i\rangle
\le2t e+2\chi\lambda^2 U.
\]
Therefore
\[
S_A:=\sum_i\|A_i x_i\|^2
\le C(te+\chi\lambda^2U). \tag{2}
\]
The factor U is retained. Replacing it by one prematurely creates an avoidable additive interface error.

## 4. Bulk estimate without an additive kernel-leakage term

For b in ran B_i,
\[
\|T_i b\|
\ge \|T_iQ_i b\|-\|T_i(I-Q_i)b\|
\ge c_0\lambda(1-C_0\lambda)\|b\|-C_0^2\lambda^2\|b\|.
\]
For a sufficiently small fixed lambda_0 this is at least c lambda ||b||.

Apply this to b=B_i x_i. Because T_iK_i=0 exactly,
\[
T_iB_ix_i=T_ix_i-T_iA_ix_i-T_iF_ix_i.
\]
The full norm bound on T_i suffices for the last two terms. Squaring, summing, and using disjoint projected outputs gives
\[
S_B:=\sum_i\|B_ix_i\|^2
\le C(e/\lambda^2+S_A+S_F). \tag{3}
\]
Here
\[
S_F:=\sum_i\|F_ix_i\|^2\le e/(c_0\lambda^\kappa) \tag{4}
\]
by summing the local up-Laplacian inequalities before taking expectation.

Unlike the earlier argument on Q_i x_i, (3) works directly on the bulk spectral component, which is orthogonal to the exact kernel. It does not need a separate estimate on T_i acting on approximate low vectors. Combining (2)--(4),
\[
\boxed{S\le C[(t+\lambda^{-\kappa})e+\chi\lambda^2 U]}. \tag{5}
\]

## 5. Quadratic leakage outside the register

The local limiting projector P-Pi_i has no private support. Thus
\[
\|\omega_i\|^2
\le2\|(I-K_i)x_i\|^2+2C_0^2\lambda^2\|x_i\|^2.
\]
Since sum_i ||x_i||^2=1+(t-1)||omega_0||^2<=t,
\[
U\le2S+2C_0^2t\lambda^2. \tag{6}
\]
For z=(I-P)omega_0, the same argument holds for every i. Averaging gives
\[
\|z\|^2\le2S/t+2C_0^2\lambda^2. \tag{7}
\]
Let N=||(I-P)x||^2=U+||z||^2. If chi lambda^2 is below a sufficiently small palette constant, substitute (6) into (5) and absorb its S term:
\[
S\le C[(t+\lambda^{-\kappa})e+\chi t\lambda^4].
\]
Equations (6)--(7), and chi lambda^2=O(1), then give
\[
\boxed{N\le C[t\lambda^2+(t+\lambda^{-\kappa})e]}. \tag{8}
\]

This does not assert that separate kernel-projector differences have norm O(lambda^2). Their norms can remain O(lambda). Squaring private leakage, retaining U, and absorbing interface feedback yield (8). The Pro shared-output example is consistent with (2), and the generic rotated-projector example does not refute this stronger use of the differential and filling hypotheses.

## 6. Concentration with linear logical-gap dependence

Split the distance to the embedded logical kernel into geometric leakage and forbidden logical mass:
\[
\begin{aligned}
\|(I-P_K)x\|^2
&=N+\langle x,(P-P_K)x\rangle\\
&\le N+g^{-1}\langle x,H^{\rm emb}x\rangle\\
&\le C[t\lambda^2+(t+\lambda^{-\kappa})e]+
e/(c_0g\lambda^\kappa).
\end{aligned}
\]
For lambda<=c/t, kappa>=2 and g<=1, the energy coefficient is bounded by C/(g lambda^kappa). Hence
\[
\boxed{\|(I-P_K)x\|^2\le C[t\lambda^2+e/(g\lambda^\kappa)]}. \tag{9}
\]
This is an all-chain statement. The geometric kernel dimension is not assumed.

Choose
\[
0<\lambda\le c\min\{t^{-1},\eta t^{-1/2}\},
\qquad
0<E\le c'\eta^2g\lambda^\kappa,\qquad 0<\eta<1.
\]
Small palette constants also enforce lambda<=lambda_0. Then every normalized x of energy below E is within eta of the embedded ker H. The weight bound has no g factor.

Exact filling and independent interiors inject V/sum_i ran Pi_i into H_d(X). Projection injectivity on the geometric spectral subspace below E supplies the reverse dimension bound. Consequently
\[
\dim\ker\Delta=\dim\ker H,\qquad
\operatorname{spec}(\Delta)\cap(0,E)=\varnothing,\qquad
\|P_{\ker\Delta}-P_K\|\le\eta.
\]
The conclusion includes ker H=0. Nested term sets with common weights give the same natural quotient maps and true normalized persistent rank as before. These final dimension deductions are standard.

## 7. Explicit conservative scaling

A convenient dyadic choice is lambda=Theta(eta/t), with the fixed proportionality constant small enough for Section 6. Then
\[
E=\Omega(\eta^{\kappa+2}g/t^\kappa).
\]
For kappa=26,
\[
\boxed{E=\Omega(\eta^{28}g/t^{26})}.
\]
For common-copy unweighting with F=lambda^{-2} an integer, the inherited gap floor is min{F E,1}, so the same conservative choice gives
\[
\boxed{F E=\Omega(\eta^{26}g/t^{24})}.
\]
At fixed eta the bounds are Omega(g/t^26) and Omega(g/t^24). With the certified history lower bound g=1/(27L^3), retain both L and t explicitly.

These are attainable lower-bound scales, not claims that the actual spectral gap equals them. The construction still has large polynomial exponents and no near-term practicality claim. The weight and common-copy count can now be chosen independently of g; precision for resolving the final spectrum still depends on g.

## 8. Other corrections retained from the Pro review

The sharp two-projection bound is valid with 0<g<=1 and 0<alpha<=1:
\[
\gamma(g,\alpha)=\frac{g+1-\sqrt{(g+1)^2-4g\alpha}}2
\ge \frac{g\alpha}{g+1}.
\]
In its history application, use the chosen certified g=1/(8L^2), not an upper bound on the unknown actual gap. Alpha=1/(3L) yields
\[
g_2\ge 1/[3L(8L^2+1)]\ge1/(27L^3).
\]

For the harmonic-angle formula
\[
a=\sqrt{1-\eta_A^2}\sqrt{1-\eta_B^2}-\eta_A\eta_B,
\]
the squared-overlap bound requires a>=0. In general replace it by a_+=max{0,a}. Equal errors eta<1/sqrt(2) suffice. Our reduction may simply choose eta<=1/10.

The final preparation budget must include the difference between the preparable logical-history mixture and the actual harmonic mixture: at most eta plus history-preparation error. The total error for the simple overlap estimator includes this term, the O(eta^2) rank/overlap bias, and projection/sampling error.

Restricted BQP1(G_2) hardness obtained at D=1 is a conditional, normalization-degenerate consequence; it does not settle the arbitrary-D source complexity or unrestricted SDQC1 equivalence.

## 9. Source checking performed in this continuation

The following are narrow primary-source checks, not a full spectral-sequence or palette reconstruction:

- [King--Kohler arXiv v2, Lemma 9.1 and Claim 10.4](https://arxiv.org/html/2311.17234v2): checked the stated local spectrum and exact global up-Laplacian sum. Their general perturbation definition still needs conversion in fixed dimension before padding.
- [Hayakawa arXiv v1, Lemma 5.4](https://arxiv.org/html/2608.02726v1#S5): checked that the explicit finite family is given an exact register quotient, using the cited earlier constructions and join closure.
- [Rudolph arXiv v2, Appendix D.1](https://arxiv.org/html/2411.02681v2#A4.SS1): checked the displayed down-gain/loss states, join construction, algebraic two-qubit checks and supplementary-code reference. The numerical higher-locality checks reported there are not newly reproduced certificates.

The direct PSD lemma is an elementary consequence of those abstract assumptions; (2)--(9) are the continuation's independent derivation. Priority for this combination has not been established. The existing packet already summed the lifted-sector bound without t in its padding section; its looser final energy remainder also came from the termwise bulk estimate. The Pro response should not be credited with introducing an aggregate step already present in that packet.

## 10. Further same-day progress and next concrete gate

The actual representative graph has now passed exact topology, filling, central-bulk and zero-weight kernel checks; see [REPRESENTATIVE_GADGET_CERTIFICATE.md](REPRESENTATIVE_GADGET_CERTIFICATE.md). It is separate from the 15 small illustrative fixtures. Complete guarded-palette closure remains open.

A simpler route is written in [FINITE_CERTIFICATE_CONCENTRATION.md](FINITE_CERTIFICATE_CONCENTRATION.md). It replaces local spectral-projector convergence and sector assumptions by a finite zero-weight kernel identity and the projected bulk certificate. Elementary boundary-matrix scaling supplies a sufficient whole-positive-gap floor, without computing an optimal spectral valuation. It reaches (9) with fewer local inputs and a stronger geometric leakage bound. The present derivation is retained as a separate intermediate milestone.

The next focused Pro review should attack both routes under their exact hypotheses, then resolve the guarded attaching-sphere closure or identify the first finite obstruction. Do not upgrade either note to an unconditional full reduction merely because the abstract inequalities survive another review.
