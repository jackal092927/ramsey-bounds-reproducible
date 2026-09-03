# Clean restricted reduction theorem for true normalized persistence

September 3, 2026. **LOCAL END-TO-END SYNTHESIS; FINITE PALETTE CERTIFICATES PASS; SEPARATED EXACT-SOURCE COROLLARY ESTABLISHED; UNRESTRICTED CLASS HARDNESS AND NOVELTY OPEN.** This is the strongest clean theorem currently supported by the local proofs and exact certificates. It is a promise-preserving transformation, not an unrestricted \(\mathsf{SDQC}_1\) or BQP hardness theorem.

## 1. Explicit source problem

Let U be a length-L real qubit circuit with k maximally mixed input qubits, computational-basis clean work qubits, and a fixed-local computational-basis final acceptance measurement P_acc (normally measurement of one designated output qubit). Put D=2^k>0. The allowed-input isometry is the standard inclusion
\[
J=I_{\rm mixed}\otimes |c\rangle_{\rm clean},
\]
where \(|c\rangle\) is a fixed computational-basis string; fixed computational-basis ancillas may be absorbed into this notation. The exact gate family is
\[
G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}.
\]
Equivalently, single H gates are allowed after adding the one mixed, unmeasured spectator from the exact extension below.

Define
\[
M=J^\dagger U^\dagger P_{\rm acc}UJ,\qquad
S=\ker(I-M).
\]
Assume the explicit spectral promise
\[
M|_{S^\perp}\preceq rI,\qquad r\le\frac13.
\tag{1}
\]
If a decision promise is desired, set \(p=\operatorname{Tr}(M)/D\) and promise
\[
p\ge\frac23\quad\text{or}\quad p\le\frac13.
\tag{2}
\]
Together with (1), this is the standard-constant instance of the explicit source promise
\(\operatorname{SepPerfectFraction}^{\mathcal G_R}(a,b,r)\), where
\(\mathcal G_R=\{X,\mathrm{CX},\mathrm{CCX},H\}\) before applying the mixed-spectator extension. The name denotes this circuit promise; it is not asserted to be a standard complexity class.

An arbitrary entangled input-code isometry or arbitrary global acceptance projector is outside the certified finite palette. No standard complexity classification of this restricted exact source problem is assumed.

## 2. Output

There is a polynomial-time construction of two nested weighted clique complexes
\[
X_{\rm in}\subseteq X_{\rm out}
\]
represented by polynomial-size graphs, with a common target degree d and binary vertex weights in \(\{1,\lambda\}\), such that
\[
\beta_d(X_{\rm in})=D,
\tag{3}
\]
and
\[
\beta_d(X_{\rm out})=\dim S,
\tag{4a}
\]
while the inclusion-induced map satisfies
\[
\operatorname{rank}\!\left[
H_d(X_{\rm in})\longrightarrow H_d(X_{\rm out})
\right]=\dim S.
\tag{4}
\]
Consequently their true normalized persistence is exactly
\[
\boxed{
\frac{\beta_d(X_{\rm in}\to X_{\rm out})}{\beta_d(X_{\rm in})}
=
\frac{\dim\ker(I-M)}{D}.
}
\tag{5}
\]
This is initial-homology normalization. No simplex-count denominator and no low-positive-energy surrogate occurs in (5).

Both degree-d geometric Laplacians have the exact endpoint kernel dimensions in (3) and (4a), and an inverse-polynomial gap above the whole kernel. For a fixed error parameter \(0<\eta<1\), a term bound t, logical gap g, and locality at most six, one may choose a dyadic
\[
\lambda=\Theta(\eta/t)
\]
within the fixed palette constants. With \(\kappa=26\), a common weighted positive-gap floor is
\[
E=\Omega\!\left(\frac{\eta^{28}g}{t^{26}}\right).
\tag{6}
\]
For the circuit histories below, \(g=\Omega(L^{-3})\), so (6) is inverse polynomial in the source size. These are conservative floors rather than optimal valuations or runtime estimates.

Under the separate common-copy unweighting theorem, choose \(F=\lambda^{-2}\) and use the same labeled copy blocks through the filtration. This gives nested unweighted clique complexes with the same Betti numbers, induced rank, and normalized ratio, and with positive-gap floor
\[
\min\{FE,1\},\qquad
FE=\Omega\!\left(\frac{\eta^{26}g}{t^{24}}\right).
\tag{7}
\]
This corollary is conditional on the recorded symmetric/asymmetric common-copy spectral decomposition.

## 3. Logical history Hamiltonians

Replace each \(H\otimes H\) transition by consecutive gain and loss propagation steps \(\sqrt2H\) and \(H/\sqrt2\). The forbidden vectors are rational three-term states; all other propagation and penalty terms are rank-one basis or two-term states with basis guards. Let the post-split legal clock positions still be denoted by L.

The initial logical Hamiltonian contains clock, propagation, and clean-input terms. Its complete zero space is the known history image
\[
\mathcal V
=
Z^{-1/2}\sum_{\tau=0}^{L-1}s_\tau|\tau\rangle U_\tau J,
\qquad s_\tau\in\{1,\sqrt2\},
\qquad \mathcal V^\dagger\mathcal V=I_D.
\tag{8}
\]
Propagation and the clean anchor rule out every extra zero vector; (8) is not merely an isometric lower-bound construction. The weighted path argument gives
\[
g_{\rm in}\ge\frac1{8L^2}.
\tag{9}
\]

Add the final rejection term for the second complex. Restricted to the initial history space, its zero space is exactly \(\mathcal VS\). Under (1), the principal-angle/output penalty is at least \(1/(3L)\) on its orthogonal complement. The sharp two-positive-operator bound gives
\[
g_{\rm out}
\ge
\frac{1}{3L(8L^2+1)}
\ge
\frac1{27L^3}.
\tag{10}
\]
Thus both logical Hamiltonians have known kernels and inverse-polynomial whole positive gaps. Equation (10) includes \(S=0\).

## 4. Complete finite local palette

Every logical rank-one term belongs to a fixed family through total support locality six:

- basis penalties use the elementary selected-petal cone;
- \(|0\rangle-|1\rangle\) uses the source-pinned **state_0m1** graph;
- \(|00\rangle-|11\rangle\) uses **state_00m11**;
- \(|01\rangle-|10\rangle\) is its exact second-bowtie X relabeling and also matches **state_01m10**;
- the four Hadamard three-term states are exact register relabelings of the certified **state_00m10m11** graph;
- computational-basis guards use the reviewed selected-cycle construction
  \[
  Z=(Y*S_\beta)\cup(R*B).
  \]

[REMAINING_ACTIVE_ATOM_CERTIFICATES.md](REMAINING_ACTIVE_ATOM_CERTIFICATES.md), [ACTIVE_HADAMARD_ORBIT.md](ACTIVE_HADAMARD_ORBIT.md), and [SELECTED_CYCLE_GUARD_CLOSURE.md](SELECTED_CYCLE_GUARD_CLOSURE.md) supply exact filling, zero-weight kernel, private-pair and guard-transfer evidence. All source graph replays are pinned to immutable code and have offline mathematical modes. This avoids any general integer-state gadget theorem.

For every palette member a target-degree certificate supplies
\[
B_d(Y_j)\cap V=\operatorname{ran}\Pi_j,\qquad
\ker D_{j,0}=V\oplus Q_j,
\tag{11}
\]
and a private projected pair
\[
T_j(\lambda)=\lambda T_{j,1},\qquad
T_{j,1}V=0,\qquad
\|T_{j,1}q\|\ge b\|q\|.
\tag{12}
\]
The finite family gives uniform constants. Unused logical registers are padded with outside harmonics in every actual bidegree. Distinct gadget interiors have disjoint private chain coordinates.

## 5. Geometric transfer

For any term set A, let \(H_A=\sum_{j\in A}\Pi_j\) be the logical operator and let \(\Delta_A\) be the full degree-d geometric Laplacian. They are different operators.

The finite-certificate theorem applies to every normalized geometric chain x:
\[
\|(I-P_{K_A})x\|^2
\le
C\left[
t\lambda^2+
\frac{\langle x,\Delta_Ax\rangle}{g_A\lambda^{26}}
\right],
\qquad
K_A=\ker H_A.
\tag{13}
\]
This is concentration toward the embedded logical kernel, not toward the initially unknown geometric kernel.

Independent gadget boundaries give
\[
B_d(X_A)\cap V
=
W_A:=\sum_{j\in A}\operatorname{ran}\Pi_j.
\tag{14}
\]
Hence \(V/W_A\) injects into \(H_d(X_A)\) and supplies \(\dim K_A\) exact zeros. Applying (13) to the entire geometric spectral subspace below E gives the reverse dimension inequality. Therefore
\[
H_d(X_A)\cong V/W_A,\qquad
\dim\ker\Delta_A=\dim K_A,
\qquad
\operatorname{spec}(\Delta_A)\cap(0,E)=\varnothing.
\tag{15}
\]
When \(K_A=0\), the whole spectrum starts at E.

For \(A\subseteq B\), the isomorphism in (15) is induced by \(v\mapsto[v]\). Inclusion is therefore the natural quotient map
\[
V/W_A\twoheadrightarrow V/W_B.
\tag{16}
\]
Take A to be the initial history terms and B to add final rejection. Equations (8), (15), and (16) prove (3)-(5).

## 6. Exact single-H extension and separated-fraction corollary

For a circuit over \(\{X,\mathrm{CX},\mathrm{CCX},H\}\), add one mixed unmeasured qubit a and replace every H by \(H\otimes H_a\). If h is the number of Hadamards,
\[
U'=U\otimes H_a^h,\qquad
P_{\rm acc}'=P_{\rm acc}\otimes I_a,\qquad
J'=J\otimes I_a.
\]
Then exactly
\[
M'=(J'^\dagger U'^\dagger P_{\rm acc}'U'J')=M\otimes I_a.
\tag{17}
\]
Both D and \(\dim S\) double, while their fraction, promise (1), and gap estimates remain unchanged. No complex-phase extension is asserted.

Finally, for
\[
f=\frac{\dim S}{D},
\]
one has exactly
\[
f\le p\le r+(1-r)f.
\tag{18}
\]
For general trace thresholds \(1\ge a>b\ge0\) with the same off-perfect bound \(r\le1/3\), define
\[
\ell=\max\!\left\{0,\frac{a-r}{1-r}\right\},
\qquad
\delta_f=\ell-b.
\tag{19}
\]
Equation (18) gives
\[
f_{\rm YES}\ge\ell,
\qquad
f_{\rm NO}\le b.
\tag{20}
\]
Thus, whenever \(\delta_f\ge1/\operatorname{poly}(n)>0\), the construction is a polynomial many-one reduction from
\(\operatorname{SepPerfectFraction}^{\mathcal G_R}(a,b,r)\) to additive approximation of (5) with error
\[
\varepsilon<\frac{\delta_f}{2}.
\tag{21}
\]
This is the minimal clean complexity corollary: the source is stated directly as an exact real-gate circuit promise with the standard mixed/clean interface, rather than identified with an unrestricted named class.

The condition \(\delta_f>0\) is also necessary for any promise-level reduction whose target statistic sees only the unchanged fraction \(f\). If the YES and NO intervals overlap at a rational \(q\), the admissible operators
\[
M_N=I_{qD}\oplus0,
\qquad
M_Y=I_{qD}\oplus\frac{a-q}{1-q}I
\]
have the same perfect-space fraction and can satisfy opposite trace promises. Exact amplification that preserves the perfect subspace, even up to a fixed ancillary tensor factor, cannot remove this obstruction.

Under (1)-(2), YES instances satisfy \(f\ge1/2\) and NO instances satisfy \(f\le1/3\), so \(\delta_f=1/6\). Estimating (5) to additive error strictly below \(1/12\), for example \(1/24\), distinguishes these promises. This consequence does not prove BQP, DQC1, or unrestricted \(\mathsf{SDQC}_1\) hardness. Defining a restricted gate-dependent class around this promise is formally possible but adds no standard-class equivalence.

A separate [eight-label source lemma](NORMALIZED_BQP1_SOURCE_GATE.md), derived after the source-complexity review, reduces exact \(\mathsf{BQP}_1^{G_2}\) verification to this standard-constant promise while forcing perfect fractions \(3/4\) and \(1/8\). Its independent local algebra/interface review and the subsequent bounded Pro audit passed; the [independent disposition](PRO_BQP1_SOURCE_DISPOSITION_2026-09-03.md) accepts the composition under this theorem's displayed hypotheses. Therefore (3)--(7) give weighted true-normalized-persistence hardness for that recognized gate-dependent class. This limited upgrade does not affect the rejection of arbitrary-threshold \(\mathsf{SDQC}_1\). Novelty remains open.

The strongest honest restriction uses no ignored mixed dummy bits: then \(D=8\), \(\beta_d(X_{\rm in})=8\), and the persistent ranks are exactly six in YES instances and one in NO instances. Hardness therefore already holds at fixed initial target-degree Betti number eight. Adding ignored mixed bits gives an exact tensor-replication closure with growing \(D\), but that growth is not a separate source of difficulty; see [DENOMINATOR_IMPACT_GATE_2026-09-03.md](DENOMINATOR_IMPACT_GATE_2026-09-03.md).

## 7. Current claims gate

The mathematical package has a complete fixed local palette, a conditional finite-certificate transfer theorem, an exact separated-source corollary, and a fixed-eight \(\mathsf{BQP}_1^{G_2}\) composition. The targeted local and Pro source-collision audits found no counterexample under the displayed hypotheses. They also established that the degenerate-kernel substitution, quotient dimension closure, and common-copy naturality cannot carry the main novelty claim.

The common-copy construction now gives an unweighted corollary, conditional on this weighted theorem and Hayakawa's symmetric/asymmetric decomposition. The same labeled copy blocks are used throughout the filtration, so the inclusion maps commute with the symmetric-sector isometries; the asymmetric positive floor excludes extra homology. This is a sourced application, not a new unweighting theorem.

The strongest defensible claim is therefore the finite-certificate arbitrary-chain estimate (13), its exact whole-kernel and natural quotient consequences (15)--(16), the fixed-eight gate-dependent hardness result, and the sourced unweighted corollary. A [19-page manuscript v0](manuscript_v0/README.md) states this package and its limitations.

The remaining priority gate is the detailed final SIAM King--Kohler proof. The completed Pro audit could inspect only its metadata and abstract. If the published proof already replaces the arXiv-v2 coordinate bulk with an equivalent outside-harmonic/fixed-local argument and obtains a uniform \(t\lambda^2\) leakage bound, the analytic novelty must be reduced. A fresh line-by-line manuscript proof audit against the owning finite certificates is also still required before paper-readiness can be claimed.

Ordinary \(\mathsf{BQP}\), unrestricted \(\mathsf{SDQC}_1\), gate-independent \(\mathsf{BQP}_1\), complex-phase coverage, intrinsic growing-denominator hardness, near-term practicality, and first-quantum-persistence claims remain withheld.
