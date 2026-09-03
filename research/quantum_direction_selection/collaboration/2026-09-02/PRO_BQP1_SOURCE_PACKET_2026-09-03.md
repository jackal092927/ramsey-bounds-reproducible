# Eight-label BQP1 source composition — bounded review packet

This packet contains one bounded interface/composition task, the new eight-label source lemma, its independent local audit, the corrected geometric transfer theorem it invokes, and the independent disposition of the preceding source-complexity review. The reviewer is asked to treat the geometric theorem and the listed Rudolph statements as supplied hypotheses, audit the exact circuit composition, and avoid novelty or unrestricted-class promotion.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PRO_BQP1_SOURCE_REQUEST_2026-09-03.md | 4665 | 4796c6bfacc826f6982dd91b093182420b5cc0c07947cf21a7cd6579f633331d |
| NORMALIZED_BQP1_SOURCE_GATE.md | 9285 | d537b46d9d5ae6871ce349f5eee21af389844310682d45bd5d4802b85bc9f94f |
| NORMALIZED_BQP1_SOURCE_GATE_INDEPENDENT_REVIEW.md | 3101 | a8ac59ad6f88cff2dd3ebe0fd3fa98c9af09fd6bc1e4c66bd9a6f96e8b047bb3 |
| CLEAN_RESTRICTED_REDUCTION_THEOREM.md | 12228 | 3d286762f3abf60366f9d47b3945218fb6f5434eefc27b6f7ff34f24008be0f3 |
| PRO_SOURCE_COMPLEXITY_DISPOSITION_2026-09-03.md | 4932 | d49a5ef5351fff31166f66eadb5911ec18c35cdd5fa59394242b8a8dd3025846 |

--- BEGIN COMPLETE FILE: PRO_BQP1_SOURCE_REQUEST_2026-09-03.md ---

# Bounded next gate: eight-label BQP1 source composition

September 3, 2026. Continue the same TDA conversation after your completed source-complexity review. Your full response and our independent disposition are archived. We retain your obstruction to arbitrary-threshold \(\mathsf{SDQC}_1\). A new, separate construction now attempts to obtain a recognized gate-dependent source by starting from perfect completeness rather than encoding an arbitrary trace gap.

**TEXT ONLY. No browsing, downloads, code execution, file writes, literature search, gadget re-audit, or novelty verdict. Return a completed hostile mathematical/interface audit within 2000 words.** Treat the corrected geometric transfer theorem as a hypothesis. Treat the following source statements as supplied facts from our targeted read of Rudolph arXiv:2411.02681v2, and say explicitly that you did not source-check them: Definition 2.2 gives uniform exact \(\mathsf{BQP}_1^{\mathcal G}\) circuits on clean all-zero qubits with one computational-basis output measurement and perfect completeness; Theorem 2.3 gives exact soundness reduction for gate sets containing
\[
G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\};
\]
Theorem 3.4 gives \(\mathsf{BQP}_1^{\mathcal G}\subseteq\mathsf{BQP}_1^{G_2}\) for each fixed finite gate set over the covered power-of-two cyclotomic fields.

Audit one proposed composition. Let \(Q_x\) be an exact \(G_2\) circuit on clean work, with output bit \(q\), such that
\[
x\in L\Rightarrow p_x=1,
\qquad
x\notin L\Rightarrow p_x\le\frac13.
\]
Add a maximally mixed three-bit label \(z\), optional ignored maximally mixed dummy bits, and clean reversible workspace. Run \(Q_x\) unconditionally. Preserve \(z\), and compute one fresh measured output bit for
\[
A(z,q)=[z=000]\ \lor\ \bigl(q\land[z\in\{001,010,011,100,101\}]\bigr).
\]
The constant Boolean combiner uses only \(X\), CX, and CCX; negative controls use surrounding \(X\) gates; temporary garbage is uncomputed. The claim is that compression through all clean qubits gives, on the mixed label/dummy domain,
\[
M_x=\operatorname{diag}(1,p_x,p_x,p_x,p_x,p_x,0,0)\otimes I_{\rm dummy}.
\tag{1}
\]

Check these points in order:

1. Derive or refute (1) as an operator identity, not merely a trace identity. Check possible label coherences, entanglement of \(q\) with the verifier workspace, clean-work initialization, uncomputation, and the fixed-local computational-basis output requirement.
2. Check exact gate compatibility. The construction never controls \(Q_x\); it only appends a classical reversible predicate. Does it remain exactly in \(G_2\) without single \(H\), controlled \(H\otimes H\), approximate synthesis, or the mixed-spectator trick?
3. Derive the entire spectrum relevant to the promise. In YES, should the trace fraction and perfect-space fraction both be \(6/8=3/4\), with off-perfect ceiling zero? In NO, should the trace fraction be \((1+5p_x)/8\le1/3\), the perfect-space fraction be exactly \(1/8\), and every off-perfect eigenvalue be at most \(1/3\)? Identify every edge case.
4. Check denominator growth and normalization. If \(m\) ignored mixed dummy bits are added, then \(D=2^{m+3}\) and both perfect multiplicities scale by \(2^m\). Does this give a legitimate growing initial Betti denominator while retaining the nontrivial \(3/4\)-versus-\(1/8\) normalized promise, or is there a hidden degeneracy?
5. Assuming the corrected geometric theorem, determine whether the composition is a polynomial many-one reduction showing additive approximation of true
\[
\beta_d(X_{\rm in}\to X_{\rm out})/\beta_d(X_{\rm in})
\]
for weighted nested clique complexes with inverse-polynomial gaps above both complete endpoint kernels is \(\mathsf{BQP}_1^{G_2}\)-hard. State a safe threshold/error. Then determine exactly what follows for the cyclotomic gate families from the supplied Theorem 3.4 and exact soundness reduction.
6. Explain why this does or does not evade your same-fraction obstruction without repairing arbitrary-threshold \(\mathsf{SDQC}_1\). Do not infer ordinary BQP, DQC1, QMA1, additive #BQP, unrestricted SDQC1, gate-independent BQP1, the unweighted corollary, novelty, or paper readiness.

Return: (i) a short verdict; (ii) a line-by-line operator proof or the first counterexample; (iii) a corrected conditional hardness corollary with exact gate, interface, fraction, gap, and precision assumptions; (iv) a status table separating mathematical validity, source facts not checked by you, gate-dependent class significance, unweighted conditionality, and novelty; and (v) one finite next gate. If the construction fails, give the smallest repair or a hard stop.

--- END COMPLETE FILE: PRO_BQP1_SOURCE_REQUEST_2026-09-03.md ---

--- BEGIN COMPLETE FILE: NORMALIZED_BQP1_SOURCE_GATE.md ---

# A nondegenerate BQP1 source for true normalized persistence

September 3, 2026. **LOCAL DERIVATION; RUDOLPH PRIMARY SOURCE CHECKED; INDEPENDENT LOCAL ALGEBRA/INTERFACE REVIEW PASSED; PRO REVIEW PENDING; NOVELTY OPEN.**

This note strengthens the explicit separated-source corollary without reviving the invalid arbitrary-threshold \(\mathsf{SDQC}_1\) inference. The direct output is a hardness result relative to an exact gate set. It is not ordinary gate-independent \(\mathsf{BQP}\)-hardness.

## Source facts

Rudolph's full version defines

\[
G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}
\]

and proves that, for every finite gate set \(\mathcal G\) over a \(2^k\)-th cyclotomic field,

\[
\mathsf{BQP}_1^{\mathcal G}
\subseteq
\mathsf{BQP}_1^{G_2}.
\]

The checked arXiv statements are Definition 2.2 for \(\mathsf{BQP}_1^{\mathcal G}\), Theorem 2.3 for exact soundness reduction when the gate set contains \(G_2\), and Theorem 3.4 for the cyclotomic-gate simulation. The proceedings page is linked for bibliographic completeness but was not needed for this derivation:

- Dorian Rudolph, *Towards a Universal Gateset for QMA1*, MFCS 2026, DOI [10.4230/LIPIcs.MFCS.2026.98](https://doi.org/10.4230/LIPIcs.MFCS.2026.98).
- Full version: [arXiv:2411.02681v2](https://arxiv.org/abs/2411.02681v2).

Rivera Cardoso--Meiburg--Nagaj give a published natural \(\mathsf{BQP}_1\)-complete finite-projector QSAT family; it is a source option, not needed for the elementary reduction below and was not independently checked in this pass:

- *Quantum SAT Problems with Finite Sets of Projectors Are Complete for a Plethora of Classes*, TQC 2025, DOI [10.4230/LIPIcs.TQC.2025.6](https://doi.org/10.4230/LIPIcs.TQC.2025.6).

## Eight-label source lemma

**Lemma.** Let \(Q_x\) be an exact \(G_2\) circuit with a fixed computational-basis clean input and one computational-basis output bit, satisfying

\[
x\in L \Longrightarrow p_x=1,
\qquad
x\notin L \Longrightarrow p_x\le\frac13.
\tag{1}
\]

There is a uniform exact \(G_2\) circuit with a maximally mixed input register of arbitrarily growing power-of-two dimension \(D\), generated using polynomially many mixed qubits, computational-basis clean work, and one fixed-local output measurement whose compressed acceptance operator \(M_x\) satisfies

\[
\begin{array}{c|c|c|c}
 & \operatorname{Tr}M_x/D
 & \dim\ker(I-M_x)/D
 & M_x|_{\ker(I-M_x)^\perp} \\ \hline
x\in L & 3/4 & 3/4 & 0\\
x\notin L & \le1/3 & 1/8 & \preceq I/3.
\end{array}
\tag{2}
\]

In particular this is an instance of
\(\operatorname{SepPerfectFraction}^{G_2}(2/3,1/3,1/3)\) with a non-all-or-none exact perfect-space fraction.

**Construction and proof.** Add a maximally mixed three-bit label \(z\in\{0,1\}^3\). Add any polynomial number of maximally mixed dummy bits and never act on them. Run \(Q_x\) unconditionally on its clean register. Preserve the label and reversibly compute a fresh output bit for the Boolean predicate
\[
A(z,q)=[z=000]\ \lor\ \bigl(q\land[z\in\{001,010,011,100,101\}]\bigr),
\]
where \(q\) is the output bit of \(Q_x\). Thus one label accepts unconditionally, five labels accept exactly when \(Q_x\) accepts, and two labels reject unconditionally.

The final Boolean combiner is a constant-size reversible computation and can be implemented with \(X\), CX and CCX, including negative controls by conjugating with \(X\). It does not control \(Q_x\), so it requires no controlled Hadamard or controlled \(H\otimes H\). Its temporary garbage is uncomputed before the single output measurement. Because the label is preserved, the acceptance operator is block diagonal in its computational basis.

In the computational label basis, and tensored with the identity on every ignored dummy bit, the compressed acceptance operator is exactly

\[
M_x=
\operatorname{diag}(1,p_x,p_x,p_x,p_x,p_x,0,0)
\otimes I_{\rm dummy}.
\tag{3}
\]

If \(p_x=1\), six of eight label blocks have eigenvalue one and two have eigenvalue zero, proving the YES row of (2). If \(p_x\le1/3\), only the unconditional-accept block has eigenvalue one, five blocks have eigenvalue \(p_x\), and two have eigenvalue zero. Therefore

\[
\frac{\operatorname{Tr}M_x}{D}
=\frac{1+5p_x}{8}
\le\frac{1+5/3}{8}=\frac13,
\qquad
\frac{\dim\ker(I-M_x)}{D}=\frac18,
\tag{4}
\]

and every nonperfect eigenvalue is at most \(1/3\). Tensoring ignored mixed bits multiplies both \(D\) and the perfect-space dimension by the same factor, so it makes \(D\) grow without changing either fraction. This proves the lemma.

The lemma itself starts from the standard \(1\)-versus-\(1/3\) \(\mathsf{BQP}_1^{G_2}\) promise. Rudolph's Theorem 2.3 supplies exact soundness reduction inside any gate set containing \(G_2\), so a verifier stated with only inverse-polynomial rejection gap can first be brought to this form without losing perfect completeness.

### Local interface audit

The checked Definition 2.2 initializes the BQP verifier's circuit qubits in a computational-basis all-zero state and measures one computational-basis output qubit. Thus \(Q_x\) contributes no unknown input register to the compressed operator; its acceptance block is the scalar \(p_x\). The only mixed logical coordinates introduced above are the preserved label and ignored dummy bits. Because the final predicate is diagonal in the label and output computational bases, compression through the clean ancillas gives (3), with no off-diagonal label blocks. The construction is uniform, adds constant active logic plus polynomially many ignored qubits, and stays exactly inside \(G_2\).

This local check found no algebraic or interface counterexample. A separate [independent local review](NORMALIZED_BQP1_SOURCE_GATE_INDEPENDENT_REVIEW.md) rederived the block compression and checked coherent labels, clean/mixed registers, reversible scratch, denominator growth, uniformity and exact gate support. Neither check replaces the requested bounded Pro audit or establishes novelty of the resulting persistence theorem.

## Optional exact power-amplification note

The following observation came from the parallel derivation and is not needed for the eight-label source. Marriott--Watrous, [*Quantum Arthur--Merlin Games*](https://arxiv.org/abs/cs/0506068), equation (3), gives the joint distribution of the alternating-projector transition bits on an eigenvector whose acceptance eigenvalue is \(p\). If acceptance is changed to require all \(N\) transition bits to be one, only the \(j=N\) term remains and the proposed new eigenvalue is \(p^N\). Hence, with \(N\) denoting their number of projector transitions,

\[
M_{\rm amp}=M^N,
\qquad
\ker(I-M_{\rm amp})=\ker(I-M),
\qquad
M_{\rm amp}|_{S^\perp}\preceq r^NI.
\tag{5}
\]

If a “round” is instead defined as a pair of transitions, \(t\) rounds give \(N=2t\) and the same formula reads \(M^{2t}=M^N\). This optional route requires a separate circuit-level interface check before use. It is unnecessary here because Rudolph already supplies exact \(G_2\) error reduction. In any case it does not repair arbitrary-threshold \(\mathsf{SDQC}_1\), because it leaves the exact perfect-space fraction unchanged.

## Normalized-persistence consequence

Apply the clean restricted geometric theorem to (3). Under that theorem's recorded local-gadget and concentration hypotheses, there is a polynomial transformation to nested **weighted** clique complexes

\[
X_{\rm in}\subseteq X_{\rm out}
\]

with

\[
\beta_d(X_{\rm in})=D,
\qquad
\beta_d(X_{\rm out})
=\beta_d(X_{\rm in}\to X_{\rm out})
=\dim\ker(I-M_x),
\tag{6}
\]

and inverse-polynomial gaps above the complete degree-\(d\) kernels at both endpoints. The true initial-homology-normalized persistence therefore has the promise

\[
\frac{\beta_d(X_{\rm in}\to X_{\rm out})}
{\beta_d(X_{\rm in})}
=
\begin{cases}
3/4,&x\in L,\\
1/8,&x\notin L.
\end{cases}
\tag{7}
\]

Thus additive error below \(5/16\) separates the values; the existing conservative choice \(1/24\) is more than sufficient. The weighted target is \(\mathsf{BQP}_1^{G_2}\)-hard. By Rudolph's theorem it is also hard for \(\mathsf{BQP}_1^{\mathcal G}\) for every fixed finite \(2\)-power-cyclotomic gate set \(\mathcal G\) covered there.

The **unweighted** nested-clique conclusion remains conditional on the separate common-copy unweighting theorem. It must not be reported at the same evidence level as (6)--(7).

## Claim firewall and next gate

This closes the named-source gate only in the following scoped sense:

- **LIMITED GO:** \(\mathsf{BQP}_1^{G_2}\)-hardness for the weighted, whole-kernel-gapped true normalized-persistence construction, conditional on the already recorded geometric theorem hypotheses.
- **WITHHELD:** gate-independent arbitrary \(\mathsf{BQP}_1\)-hardness.
- **NO-GO:** ordinary \(\mathsf{BQP}\), \(\mathsf{DQC}_1\), unrestricted \(\mathsf{SDQC}_1\), \(\mathsf{QMA}_1\), or additive \(\#\mathsf{BQP}\) hardness from this lemma.

The next decisive gate is novelty and positioning. In particular, the project must compare (7) with the nearby harmonic-persistence \(\mathsf{BQP}_1\)-hardness literature and with Lowe--Kim--Bondesan--Hayakawa, [arXiv:2607.03278v1](https://arxiv.org/abs/2607.03278v1). A valid source theorem is not by itself evidence that the complete normalized-filtration result is new or venue-ready.

--- END COMPLETE FILE: NORMALIZED_BQP1_SOURCE_GATE.md ---

--- BEGIN COMPLETE FILE: NORMALIZED_BQP1_SOURCE_GATE_INDEPENDENT_REVIEW.md ---

# Independent local review of the eight-label BQP1 source

September 3, 2026. **ALGEBRA AND CIRCUIT-INTERFACE REVIEW PASSED; EXTERNAL PRO REVIEW AND NOVELTY REVIEW NOT YET PERFORMED.**

## Scope

This review independently checks the local source lemma in [NORMALIZED_BQP1_SOURCE_GATE.md](NORMALIZED_BQP1_SOURCE_GATE.md). It assumes a pure/clean-input \(\mathsf{BQP}_1^{G_2}\) verifier \(Q_x\) with one computational-basis output bit, perfect completeness and soundness at most \(1/3\). It does not certify the downstream geometric theorem or publication priority.

## Operator check

Let the three-bit label be preserved. A reversible combiner writes its predicate into a fresh clean decision bit and then uncomputes its scratch. Conjugating the final decision projector by that combiner gives one unconditional-accept block, five blocks equal to the verifier output projector, and two zero blocks. After running \(Q_x\) unconditionally and compressing to the fixed clean input,

\[
M_x=\operatorname{diag}(1,p_xI_5,0I_2)\otimes I_{\rm dummy}.
\]

Coherent label superpositions cause no cross terms because the label is preserved and the decision projector is block diagonal. Verifier garbage is harmless after compression: each of the five conditional blocks contributes the same scalar acceptance probability \(p_x\).

Therefore:

- if \(p_x=1\), both normalized trace and perfect fraction are \(6/8=3/4\), and the complement has eigenvalue zero;
- if \(p_x\le1/3\), normalized trace is at most \((1+5/3)/8=1/3\), perfect fraction is exactly \(1/8\), and every nonperfect eigenvalue is at most \(1/3\).

## Interface and uniformity check

- The label and dummy bits are the only maximally mixed registers.
- The verifier input, work, decision and reversible scratch registers are clean.
- The verifier runs unconditionally, so no controlled-\(Q_x\) or controlled-\(H\otimes H\) is needed.
- The constant Boolean combiner uses only \(X\), CX and CCX, which are in \(G_2\).
- Dummy bits are untouched. They multiply the denominator and perfect-kernel dimension by the same power of two and do not alter either promise fraction.
- The circuit family is uniform: the three-label combiner is constant size and appending polynomially many idle mixed wires is a classical polynomial-time transformation.

The fresh decision bit is essential; the construction should not be described as irreversibly overwriting the verifier output.

## Verdict and firewall

The eight-label lemma is algebraically valid under the clean \(\mathsf{BQP}_1^{G_2}\) normal form. Combined with the separately recorded geometric theorem, it supports the scoped headline:

> Additive true normalized persistence for nested weighted clique complexes with inverse-polynomial endpoint whole-kernel gaps is \(\mathsf{BQP}_1^{G_2}\)-hard.

This review does not support ordinary \(\mathsf{BQP}\)-hardness, unrestricted \(\mathsf{SDQC}_1\)-hardness, gate-independent \(\mathsf{BQP}_1\)-hardness, or an unconditional unweighted claim. It also does not establish novelty relative to harmonic-persistence hardness. Those are separate gates.

--- END COMPLETE FILE: NORMALIZED_BQP1_SOURCE_GATE_INDEPENDENT_REVIEW.md ---

--- BEGIN COMPLETE FILE: CLEAN_RESTRICTED_REDUCTION_THEOREM.md ---

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

A separate [eight-label source lemma](NORMALIZED_BQP1_SOURCE_GATE.md), derived after the source-complexity review, locally reduces exact \(\mathsf{BQP}_1^{G_2}\) verification to this standard-constant promise while forcing perfect fractions \(3/4\) and \(1/8\). Its [independent local algebra/interface review](NORMALIZED_BQP1_SOURCE_GATE_INDEPENDENT_REVIEW.md) passed. Therefore (3)--(7) give weighted true-normalized-persistence hardness for that recognized gate-dependent class under the theorem's recorded geometric hypotheses. This limited upgrade does not affect the rejection of arbitrary-threshold \(\mathsf{SDQC}_1\), and it is still pending external Pro review and a novelty audit.

## 7. Remaining claims gate

The mathematical package now has a complete fixed local palette, a clean conditional transfer theorem, and an exact separated-source corollary. The next nonlocal obligations are:

1. audit every dependency in this synthesis against its owning proof/certificate;
2. establish novelty of the degenerate-kernel whole-gap plus normalized filtered-rank package;
3. obtain an external bounded review of the eight-label \(\mathsf{BQP}_1^{G_2}\) source and retain its exact gate-dependent scope;
4. perform a primary-source collision audit against nearby harmonic-persistence hardness and exact-kernel/clique-homology reductions;
5. decide whether the poor gap exponent is acceptable for a theory result despite its lack of practical value.

The strongest locally defensible claim is the explicit transformation (3)--(7), the separated-promise corollary (19)--(21), and the weighted \(\mathsf{BQP}_1^{G_2}\)-hard composition above. Ordinary \(\mathsf{BQP}\), unrestricted \(\mathsf{SDQC}_1\), gate-independent \(\mathsf{BQP}_1\), unconditional unweighted hardness and paper readiness remain withheld.

--- END COMPLETE FILE: CLEAN_RESTRICTED_REDUCTION_THEOREM.md ---

--- BEGIN COMPLETE FILE: PRO_SOURCE_COMPLEXITY_DISPOSITION_2026-09-03.md ---

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

--- END COMPLETE FILE: PRO_SOURCE_COMPLEXITY_DISPOSITION_2026-09-03.md ---
