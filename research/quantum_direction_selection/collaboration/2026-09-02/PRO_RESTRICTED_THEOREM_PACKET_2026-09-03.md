# Clean restricted reduction — bounded integration-review packet

This packet contains the complete bounded task, integrated theorem, and remaining-atom certificate narrative. Exact JSON and code stay in the same source commit; the reviewer is asked to treat those finite computations as supplied hypotheses.

| File | Bytes | SHA-256 |
| --- | --- | --- |
| PRO_RESTRICTED_THEOREM_REQUEST_2026-09-03.md | 3842 | 65d4e389e0c8261d266d0059d7ea0bd992bd13cf4f429841576931ed9881e38c |
| CLEAN_RESTRICTED_REDUCTION_THEOREM.md | 8905 | 2c9c6d477e383cdf52d3a19cb25a280c0d19a6869c2cd8afa7c7cc75f6ab8ffc |
| REMAINING_ACTIVE_ATOM_CERTIFICATES.md | 6709 | 5b526ab9bb8d7019931f9ea811a2a76e8d485194758049163561641c43423e99 |

--- BEGIN COMPLETE FILE: PRO_RESTRICTED_THEOREM_REQUEST_2026-09-03.md ---

# Bounded next gate: integrate the exact restricted theorem

September 3, 2026. Continue the same conversation after your completed selected-cycle guard review. That full response and a separate local disposition are archived. We accepted the conditional guard lemma after making its target-degree, augmented-gap, and degreewise-projection scopes explicit.

**TEXT ONLY. No browsing, downloads, code execution, file writes, literature review, or independent recomputation of the finite certificates. Return a completed hostile mathematical audit within 2500 words.**

This request has one goal: audit the attached clean restricted reduction theorem now that every required base atom has a source-pinned finite certificate. Treat the exact integer/modular checks reported in the attached atom note as hypotheses; we are not asking you to certify unseen computations. Treat the previously reviewed concentration and selected-cycle guard lemmas as established under their explicit hypotheses.

The source-pinned checks now cover:

- \(|0\rangle-|1\rangle\): 16 vertices, boundary ranks 15 and 24, Betti numbers (1,1,0), 24-term integer filling, zero-pair rank 30 with kernel 2+8, and nonzero 8-dimensional bulk Gram determinant;
- \(|00\rangle-|11\rangle\): 33 vertices, boundary ranks 32,209,437,272, Betti numbers (1,0,0,3,0), 248-term integer filling, zero-pair rank 596 with kernel 4+112, and nonzero 112-dimensional bulk Gram determinant;
- \(|01\rangle-|10\rangle\): exact weight-preserving graph relabeling by logical X on the second bowtie, including private vertices and the transported integer filling;
- basis atoms, four Hadamard three-term atoms, and arbitrary fixed computational-basis guards through total locality six are supplied by the already archived cone, orbit, and selected-cycle results.

The new theorem claims only a polynomial transformation from an explicitly stated exact real-gate circuit promise to nested weighted clique complexes (and a separately conditional common-copy unweighted version), with
\[
\beta_d(X_{\rm in})=D,\qquad
\operatorname{rank}[H_d(X_{\rm in})\to H_d(X_{\rm out})]=\dim\ker(I-M).
\]
It does not claim a standard-class hardness result.

Audit these precise integration points:

1. Does the four-item atom list exhaust every rank-one clock, input, propagation, and output term after the gain/loss split of \(H\otimes H\), including controlled flips and fixed controls?
2. Do the padded gadgets share one global target degree and form a natural inclusion when only the final rejection terms are added? Is the initial denominator exactly D, including the no-extra-history-kernel argument?
3. Does the logical output kernel equal the perfect-accepting subspace and does the off-perfect spectral promise give the stated positive gap, including the zero final kernel?
4. Do concentration, injection, and natural quotient maps prove exact whole homology and persistent rank, rather than only a low-energy count?
5. Are the weighted and conditional unweighted gap scales algebraically consistent at \(\kappa=26\)?
6. Is the spectator extension and the trace-to-fixed-space fraction separation stated at exactly the defensible strength?

Return a brief verdict and the first invalid inference, missing hypothesis, or missing atom if one exists. Otherwise give a concise corrected theorem/proof skeleton, listing any assumptions that must remain in the theorem statement. Distinguish a mathematical gap from novelty or source-complexity risk. Do not infer BQP-hardness, unrestricted SDQC1 equivalence, a complex-phase extension, optimal spectral valuation, practical performance, source priority, or paper readiness.

If the integration is valid, identify the smallest remaining theorem-level obstacle to an impactful TCS claim. That obstacle may be source complexity or novelty; do not embellish it.

--- END COMPLETE FILE: PRO_RESTRICTED_THEOREM_REQUEST_2026-09-03.md ---

--- BEGIN COMPLETE FILE: CLEAN_RESTRICTED_REDUCTION_THEOREM.md ---

# Clean restricted reduction theorem for true normalized persistence

September 3, 2026. **LOCAL END-TO-END SYNTHESIS; FINITE PALETTE CERTIFICATES PASS; SOURCE-PROMISE HARDNESS AND NOVELTY OPEN.** This is the strongest clean theorem currently supported by the local proofs and exact certificates. It is a promise-preserving transformation, not an unrestricted SDQC1 or BQP hardness theorem.

## 1. Explicit source problem

Let U be a length-L real quantum circuit with clean work, an explicitly mixed input register of dimension D>0, and one final acceptance measurement P_acc. The exact gate family is
\[
G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}.
\]
Equivalently, single H gates are allowed after adding the one mixed, unmeasured spectator from the exact extension below.

Let J embed the D-dimensional allowed input sector together with the clean work state, and define
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
No standard complexity classification of this restricted exact source problem is assumed.

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

Both degree-d geometric Laplacians have the exact kernel dimensions in (3)-(4) and an inverse-polynomial gap above the whole kernel. For a fixed error parameter \(0<\eta<1\), a term bound t, logical gap g, and locality at most six, one may choose a dyadic
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

## 6. Exact single-H extension and fraction promise

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
Under (1)-(2), YES instances satisfy \(f\ge1/2\) and NO instances satisfy \(f\le1/3\). Estimating (5) to additive error strictly below \(1/12\), for example \(1/24\), distinguishes these promises. This is a consequence for the explicit circuit promise. It does not, by itself, prove that this promise is BQP-hard, SDQC1-hard, or outside BPP.

## 7. Remaining claims gate

The mathematical package now has a complete fixed local palette and a clean conditional transfer theorem. The next nonlocal obligations are:

1. audit every dependency in this synthesis against its owning proof/certificate;
2. identify a natural standard or independently meaningful exact source problem;
3. establish novelty of the degenerate-kernel whole-gap plus normalized filtered-rank package;
4. decide whether the poor gap exponent is acceptable for a theory result despite its lack of practical value.

Until the source-promise and priority gates pass, the defensible claim is the explicit transformation (3)-(7), not a standard-class hardness theorem or paper-readiness verdict.

--- END COMPLETE FILE: CLEAN_RESTRICTED_REDUCTION_THEOREM.md ---

--- BEGIN COMPLETE FILE: REMAINING_ACTIVE_ATOM_CERTIFICATES.md ---

# Exact finite certificates for the remaining active atoms

September 3, 2026. **SOURCE-PINNED INTEGER CERTIFICATES PASS; PALETTE INTEGRATION LOCALLY COMPLETE FOR THE EXPLICIT REAL-GATE SOURCE.** This note covers the one-qubit difference and both two-qubit two-term states left open after the Hadamard-orbit and selected-cycle guard results. It does not establish source priority, an unrestricted complexity-class equivalence, or end-to-end paper correctness.

## 1. Source and execution boundary

The primary code is Dorian Rudolph's **gadget_homology.py** at immutable commit
\[
\texttt{30ac70e5dacdecce97c38d801c128ec3ed93a96a},
\]
with pinned SHA-256
\[
\texttt{c8918f9e037ae79796bb65640170c8e60f31883625d24348f3476f7644dcd29a}.
\]
Its repository license is GPLv2-or-later. The upstream code is not copied here.

[certify_remaining_active_atoms.py](certify_remaining_active_atoms.py) fetches the pinned file in default mode, asserts its hash, evaluates only **make_graph**, **thicken**, **fill_cycle**, **join_keep_names**, and the three requested state functions, and captures each graph at its first **clique_complex** call. Capture happens before Sage homology, plotting, or later top-level calculations. All subsequent clique enumeration, oriented boundaries, modular ranks, rational reconstruction, filling equations, zero-weight pairs, and graph isomorphisms are computed independently with Python and NumPy.

The full graph data and filling chains are in [REMAINING_ACTIVE_ATOM_CERTIFICATES.json](REMAINING_ACTIVE_ATOM_CERTIFICATES.json), SHA-256
\[
\texttt{82c0ece72ef13c65dc882195feec5ea9f09610e3b0a524e4ddb48c498ae8b077}.
\]
An offline mode reconstructs all three graphs from that archive, recomputes every atom section, and checks exact equality. It passed with every external-command call replaced by an exception; [the small offline receipt](OFFLINE_REMAINING_ACTIVE_ATOM_CHECKS.json) records this. Offline mode verifies the supplied graphs and mathematics, not upstream provenance.

## 2. One-qubit difference

The source function **state_0m1** implements
\[
\phi_- = |0\rangle-|1\rangle.
\]
The recovered graph has 16 vertices and clique counts
\[
(16,40,24)
\]
in degrees 0,1,2. Exact boundary ranks over \(\mathbb Q\) are
\[
\operatorname{rank}\partial_1=15,\qquad
\operatorname{rank}\partial_2=24,
\]
certified by matching lower bounds modulo \(1000003\) and rational upper bounds. Thus the ordinary Betti numbers are \((1,1,0)\). A 24-term integer two-chain, with denominator one, has boundary exactly the difference of the two oriented bowtie petals. The complementary register cycle \(|0\rangle+|1\rangle\) is independent modulo boundaries. Hence
\[
B_1(Y)\cap Z_1(R)=\mathbb C\phi_-.
\]

At zero private-vertex weight, the target differential pair has rank 30 on a 40-dimensional target space. The two register cycles and eight central edges are exact kernel vectors, so matching dimensions prove
\[
\ker D_0^{(1)}=V\oplus Q,\qquad \dim V=2,\quad\dim Q=8.
\]
The projected central pair has zero constant term and annihilates both register cycles at first order. Its \(8\times8\) integer Gram determinant is nonzero modulo \(1000003\), with determinant residue 512 and infinity norm 8. This proves injectivity on Q and supplies an explicit rational singular-value floor. The safe weighted whole-gap exponent is \(2(1)+4=6\).

## 3. Two-qubit two-term state

The source function **state_00m11** implements
\[
\phi_{00,11}=|00\rangle-|11\rangle.
\]
Its graph has 33 vertices and clique counts
\[
(33,241,646,712,272)
\]
in degrees 0 through 4. Exact boundary ranks are
\[
32,\ 209,\ 437,\ 272.
\]
The ordinary Betti numbers are
\[
(1,0,0,3,0).
\]
A denominator-one 248-term integer four-chain fills \(\phi_{00,11}\). The three logical complement cycles
\[
|00\rangle+|11\rangle,\qquad |01\rangle,\qquad |10\rangle
\]
remain independent modulo boundaries. Therefore
\[
B_3(Y)\cap Z_3(R)=\mathbb C\phi_{00,11}.
\]

The zero-weight degree-three pair has rank 596 on 712 target coordinates. Four register cycles plus 112 central tetrahedra give the matching 116-dimensional kernel:
\[
\ker D_0^{(3)}=V\oplus Q,\qquad \dim V=4,\quad\dim Q=112.
\]
The projected first-order central pair annihilates V. Its \(112\times112\) Gram determinant is nonzero modulo \(1000003\), with residue 655970 and infinity norm 12. Thus it is injective on Q. The safe weighted whole-gap exponent is 10.

## 4. The second two-term state by exact relabeling

Swapping the two petals of the second bowtie is logical \(X\) on qubit two. Applied to the complete **state_00m11** graph, including every private layer vertex, this permutation gives exactly the separately recovered source graph **state_01m10**. It sends
\[
|00\rangle-|11\rangle
\longmapsto
|01\rangle-|10\rangle.
\]
The checker verifies equality of the mapped vertex and edge sets, hence all clique complexes, and transports the 248-term integer filling with orientation signs. Signed permutation chain isometries transport the zero-weight kernel, projected bulk pair, and all spectral constants. No second rank computation is needed.

## 5. Palette consequence

The explicit weighted unary circuit construction requires only the following rank-one atom types after splitting each Hadamard pair:

1. computational-basis projectors;
2. the one-qubit clock difference \(|0\rangle-|1\rangle\);
3. the flip differences \(|00\rangle-|11\rangle\) and \(|01\rangle-|10\rangle\);
4. the four rational three-term Hadamard atoms.

The basis cone gives type 1. Sections 2–4 give types 2–3. [ACTIVE_HADAMARD_ORBIT.md](ACTIVE_HADAMARD_ORBIT.md) gives type 4 from one source-pinned representative. [SELECTED_CYCLE_GUARD_CLOSURE.md](SELECTED_CYCLE_GUARD_CLOSURE.md), now conditionally accepted after bounded review and local rechecking, tensors any base atom with every needed computational-basis guard without adding private vertices. The maximal total support locality is six.

Therefore the finite local certificate obligation is locally complete for the explicitly stated real-gate source
\[
G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}
\]
and for the exact mixed-spectator extension to single \(H\) gates. A finite common minimum supplies uniform constants, and \(m\le6\) gives the conservative exponent
\[
\kappa=4m+2\le26.
\]

This conclusion avoids an unrestricted integer-state gadget theorem and does not rely on approximate gate compilation. It concerns the local palette only. The remaining research burden is now end-to-end theorem integration, a meaningful exact source-promise consequence, and novelty relative to prior whole-kernel and filtered-homology results. The very poor polynomial gap remains unsuitable as a practical algorithmic claim.

--- END COMPLETE FILE: REMAINING_ACTIVE_ATOM_CERTIFICATES.md ---
