# Exact source-complexity — bounded review packet

This packet contains one bounded source-complexity task, the targeted primary-source/algebra gate, the corrected restricted transfer theorem, and the independent disposition of the completed integration review. The reviewer is asked to accept the geometric theorem only for this gate and to stop at the first unproved threshold or exact-gate step.

| File | Bytes | SHA-256 |
| --- | --- | --- |
| PRO_SOURCE_COMPLEXITY_REQUEST_2026-09-03.md | 4657 | 2b27954ca349661bb1d09c926786d615f736ceaff98f4c1504e8e9711b33a6c8 |
| SOURCE_COMPLEXITY_GATE.md | 7056 | 8bb14dc9907cc8658357a00f22fc10246188b33373433e31cba15aff0f23b11d |
| CLEAN_RESTRICTED_REDUCTION_THEOREM.md | 9376 | 83342564a8426f2d01b5a68c0dfa7c5d50646264f232e192aff4666393bebbe6 |
| PRO_RESTRICTED_THEOREM_DISPOSITION_2026-09-03.md | 5639 | 6fb8eac7d3352ccacbd97dd6586df28d473013155b9715564f3f7d81623176c1 |

--- BEGIN COMPLETE FILE: PRO_SOURCE_COMPLEXITY_REQUEST_2026-09-03.md ---

# Bounded next gate: exact source complexity

September 3, 2026. Continue the same TDA conversation after your completed restricted-theorem integration review. That full response and an independent disposition are archived. We accepted your source-interface correction and now restrict to maximally mixed input qubits, computational-basis clean ancillas, and a fixed-local computational-basis output measurement.

**TEXT ONLY. No browsing, downloads, code execution, file writes, literature search, or renewed gadget audit. Return a completed hostile source-complexity analysis within 2400 words.** Treat the corrected geometric transfer theorem and its finite certificates as hypotheses for this gate.

This request has one objective: determine the strongest exact complexity consequence supported by the current theorem without silently promoting it to unrestricted \(\mathsf{SDQC}_1\)-hardness.

The supplied primary-source check records Lowe--Kim--Bondesan--Hayakawa arXiv:2607.03278v1 Definition 2 as follows. For an acceptance operator \(M\), there is a perfectly accepted subspace \(S\), every unit vector in \(S^\perp\) is accepted with probability at most \(r=1/3\), and the maximally mixed acceptance probability obeys \(p\ge a\) in YES and \(p\le b\) in NO, where Definition 2 permits arbitrary \(a-b\ge1/\operatorname{poly}\). The source explicitly says the class depends on the exact gate set. Its equation (9) says perfect-subspace-preserving amplification makes the new acceptance probability close to \(f=\dim S/D\). Sections 5.5--5.6 then use \(f\) for exact-kernel normalized persistence; Section 7 formulates exact kernel/gap/functorial realization as the missing TDA route.

Our exact algebra is
\[
f\le p\le r+(1-r)f,
\]
so the guaranteed fraction separation is
\[
\delta_f=\max\left\{0,\frac{a-r}{1-r}\right\}-b.
\]
At \((a,b,r)=(2/3,1/3,1/3)\), this is \(1/6\), and target error \(1/24\) is safe. Arbitrary trace gaps fail at the operator level: \(M_{\rm Y}=I/4\) and \(M_{\rm N}=0\) both have \(f=0\), while their traces differ and both obey \(r=1/3\).

Audit these points in order:

1. Prove or refute the displayed fraction intervals and the necessity of \(\delta_f>0\) for any reduction that reads only the exact perfect-space fraction.
2. Does exact-subspace-preserving Marriott--Watrous amplification repair arbitrary \(a,b\), or does it merely make the *new* trace close to the unchanged \(f\), thereby losing an original trace gap that came from imperfectly accepting states? Identify the first valid or invalid inference in the checked source route. Do not issue a global paper verdict.
3. Define the strongest noncircular restricted source statement. Is it defensible to call the target hard for a fixed-threshold separated class \(\operatorname{SepSDQC}_1^{\mathcal G_R}\), where \(\mathcal G_R=\{X,\mathrm{CX},\mathrm{CCX},H\}\), or should we state only a many-one reduction from an explicitly named circuit promise? Explain what additional theorem would be needed to reach the source's arbitrary-threshold Definition 2.
4. Check exact gate/interface compatibility. The source has one clean measured qubit and a maximally mixed remainder; our theorem permits that standard inclusion plus computational-basis clean work. The spectator identity converts every single \(H\) to \(H\otimes H\) with \(M'=M\otimes I\). Does this suffice for circuits already written over \(\mathcal G_R\)? Do not use approximate universality, a complex phase simulation, or assume that amplification remains in \(\mathcal G_R\) without proof.
5. Our quotient theorem directly proves endpoint Betti dimensions and induced rank, but does not assert one exact common harmonic isometry satisfying every operator identity in the source's Conjecture 2. Can it nevertheless prove the rank conclusion needed for a restricted version of Conjecture 1 directly? Distinguish bypassing a sufficient conjecture from proving that conjecture.
6. Give the smallest remaining lemma that would upgrade the result. If no exact threshold/gate-set reduction is derivable from the supplied facts, state a hard stop and retain only the separated-promise corollary.

Return: (i) a short verdict; (ii) a corrected theorem/corollary with all threshold and gate assumptions; (iii) a status table for explicit-promise reduction, separated-class hardness, unrestricted \(\mathsf{SDQC}_1\), restricted Conjecture 1, and Conjecture 2; and (iv) one finite next proof target or a stopping conclusion. Distinguish a mathematical obstruction from novelty and class-significance risk. Do not claim BQP/DQC1 hardness, complex-gate coverage, full source priority, or paper readiness.

--- END COMPLETE FILE: PRO_SOURCE_COMPLEXITY_REQUEST_2026-09-03.md ---

--- BEGIN COMPLETE FILE: SOURCE_COMPLEXITY_GATE.md ---

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
\delta_f=max\!\left\{0,\frac{a-r}{1-r}\right\}-b.
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

Define the explicit separated source promise \(\operatorname{SepSDQC}_1^{\mathcal G_R}(a,b,r)\) by the standard mixed-input/clean-output circuit interface, exact gate family
\[
\mathcal G_R=\{X,\mathrm{CX},\mathrm{CCX},H\},
\]
and conditions (1)--(3) with \(\delta_f\ge1/\operatorname{poly}(n)\). The exact spectator construction converts \(\mathcal G_R\) circuits to the certified \(G_2\) palette while doubling \(D\) and \(\dim S\), so \(f\) and \(r\) are unchanged.

The clean reduction theorem then gives a polynomial many-one reduction from this promise to weighted clique-complex normalized harmonic persistence, with precision below \(\delta_f/2\), exact denominator \(D\), exact persistent rank \(\dim S\), and inverse-polynomial gaps above both whole kernels. At the standard constants, the required target precision may be fixed at \(1/24\).

This is a mathematically valid complexity corollary for an explicit source promise. Calling it unrestricted \(\mathsf{SDQC}_1\)-hardness requires two additional results that are not currently in the archive:

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

## 6. Decision gate

**GO** if a precise complexity definition already standardizes \((a,b,r)=(2/3,1/3,1/3)\) for the exact real gate set, or if an exact transformation to such parameters is proved without changing the encoded perfect-space fraction. Then the current geometric theorem has a named restricted-class hardness consequence and directly advances the stated NHP conjecture.

**STOP the unrestricted hardness claim** if no such theorem is available. Retain the representation/transfer theorem and the separated-promise corollary, and present arbitrary-threshold \(\mathsf{SDQC}_1\) plus full source priority as open. Classical reversible predicates give growing \(D\) and exact \(f=p\), but their constant additive-gap promise is sampleable and supplies only a baseline, not the desired quantum-hard source.

--- END COMPLETE FILE: SOURCE_COMPLEXITY_GATE.md ---

--- BEGIN COMPLETE FILE: CLEAN_RESTRICTED_REDUCTION_THEOREM.md ---

# Clean restricted reduction theorem for true normalized persistence

September 3, 2026. **LOCAL END-TO-END SYNTHESIS; FINITE PALETTE CERTIFICATES PASS; SOURCE-PROMISE HARDNESS AND NOVELTY OPEN.** This is the strongest clean theorem currently supported by the local proofs and exact certificates. It is a promise-preserving transformation, not an unrestricted SDQC1 or BQP hardness theorem.

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

--- BEGIN COMPLETE FILE: PRO_RESTRICTED_THEOREM_DISPOSITION_2026-09-03.md ---

# Restricted-theorem integration review — independent disposition

September 3, 2026. **INTEGRATION ACCEPTED AFTER ONE SOURCE-INTERFACE CORRECTION.** The [complete external response](PRO_RESTRICTED_THEOREM_REVIEW_2026-09-03.md) is preserved separately with all 137 displayed equation sources. The review treated the finite atom calculations, the all-chain concentration theorem, and the selected-cycle guard theorem as hypotheses, exactly as requested. It performed no source-complexity proof, literature search, priority check, or independent recomputation.

## 1. Mathematical disposition

No counterexample was found under the corrected hypotheses. The one substantive objection is valid: the previous statement allowed an abstract isometry \(J\) and did not constrain \(P_{\rm acc}\), while the certified palette implements computational-basis anchors and guards. The source problem must therefore state
\[
J=I_{\rm mixed}\otimes |c\rangle_{\rm clean}
\]
for maximally mixed input qubits and a fixed computational-basis clean string, and must use a fixed-local computational-basis acceptance measurement. An arbitrary entangled input-code isometry or arbitrary global output projector is not covered.

This is a missing theorem hypothesis, not a failure of the reduction once that hypothesis is supplied. [CLEAN_RESTRICTED_REDUCTION_THEOREM.md](CLEAN_RESTRICTED_REDUCTION_THEOREM.md) has been corrected accordingly.

The response also correctly identifies an imprecise sentence: persistent rank is not itself the endpoint Betti number. The theorem now separately states
\[
\beta_d(X_{\rm out})=\dim S
\]
and
\[
\operatorname{rank}[H_d(X_{\rm in})\to H_d(X_{\rm out})]=\dim S.
\]
Both follow from the canonical quotient description, but they are logically distinct statements.

## 2. Integration checks

| Component | Independent disposition |
| --- | --- |
| Atom exhaustion | Accepted for the corrected circuit interface. Basis clock/input/output penalties, stationary and flipping reversible transitions, and the four gain/loss Hadamard atoms exhaust the stated exact gate history. Unacted-on qubits contribute identities and outside harmonics, not extra guarded atoms. |
| Common degree | Accepted under the reduced-join convention. An \(m\)-qubit target of degree \(2m-1\), joined with \(n-m\) outside bowties of degree \(2(n-m)-1\), lands in degree \(2n-1\). |
| Filtration | Accepted. The output graph adds rejection gadgets on fresh private vertices to the same register; no private-private cross edges are added. This gives the natural inclusion used by the quotient map. |
| Initial denominator | Accepted. Legal clock plus propagation gives one history per allowed input, and computational-basis input anchors restrict the seed exactly to the \(D=2^k\) mixed-input sector. The history map is an isometry and there are no additional logical zeros. |
| Output kernel and gap | Accepted. Positivity gives the kernel intersection, compression to history is \((I-M)/Z\), and the off-perfect promise supplies the positive principal-angle penalty. The two-positive-operator bound includes \(S=0\). |
| Whole geometric kernel | Accepted conditional on the stated all-chain concentration theorem. The register quotient injects \(\dim K_A\) exact zeros; concentration bounds the entire spectral subspace below \(E\) by the same dimension. This proves endpoint homology and a gap above the whole kernel, not an approximate-mode count. |
| Persistent rank | Accepted. The canonical endpoint identifications commute with register inclusion, so the induced map is the natural surjection \(V/W_A\to V/W_B\), including a zero target quotient. |
| Gap exponents | Accepted algebraically. With \(\lambda=\Theta(\eta/t)\) and \(\kappa=26\), the safe weighted floor is \(\Omega(\eta^{28}g/t^{26})\); multiplying by \(F=\lambda^{-2}\) gives the separate conditional unweighted floor \(\Omega(\eta^{26}g/t^{24})\). Polynomial-size unweighting requires fixed or inverse-polynomial \(\eta\) and common labeled copy blocks. |
| Spectator | Accepted exactly for a maximally mixed unmeasured spectator: \(M'=M\otimes I\), so both dimensions double and the fraction and off-perfect gap remain unchanged for either parity of the Hadamard count. |
| Fraction promise | Accepted. \(f\le p\le r+(1-r)f\) yields \(f\ge1/2\) versus \(f\le1/3\) at \((a,b,r)=(2/3,1/3,1/3)\). Additive error must be strictly below \(1/12\); \(1/24\) is safe. |

## 3. Surviving theorem and next obstruction

The surviving result is a polynomial representation/transfer theorem from one explicit exact real-circuit promise to true initial-homology-normalized persistence, with exact endpoint multiplicities, exact induced rank, and inverse-polynomial whole-kernel gaps. This is stronger than an exact multiplicity statement alone and does not use simplex normalization or a low-energy surrogate.

The first unresolved theorem-level obstacle is source complexity. The source promise simultaneously requires an exact eigenvalue-one subspace, an off-perfect spectral ceiling, and a trace gap over a growing maximally mixed sector. No reduction from a recognized standard source problem has yet been supplied. The \(D=1\) specialization loses the intended normalization content, so it is not an adequate substitute for an impactful normalized-persistence hardness result.

Novelty is a separate unresolved gate. The supplied ledger indicates collisions with parsimonious homology multiplicity and related harmonic-survival constructions, but neither this collection step nor the Pro review checked the underlying papers. No priority or paper-readiness conclusion is promoted here.

--- END COMPLETE FILE: PRO_RESTRICTED_THEOREM_DISPOSITION_2026-09-03.md ---
