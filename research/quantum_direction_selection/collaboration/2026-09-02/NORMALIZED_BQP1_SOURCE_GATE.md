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
