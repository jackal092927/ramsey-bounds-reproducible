# Independent disposition of the BQP1 source-interface review

September 3, 2026. **OPERATOR AND COMPOSITION ACCEPTED UNDER THE DISPLAYED HYPOTHESES; PRIMARY-SOURCE CHECK REMAINS LOCAL; NOVELTY OPEN.**

## Decision

The completed [Pro review](PRO_BQP1_SOURCE_REVIEW_2026-09-03.md) correctly derives the eight-label compressed acceptance operator and its spectrum. An independent recheck finds no mathematical or circuit-interface counterexample. Combined with the already stated geometric transfer theorem, the construction supports a polynomial many-one reduction from the exact gate-dependent class \(\mathsf{BQP}_1^{G_2}\) to additive approximation of true initial-homology-normalized persistence for nested **weighted** clique complexes with inverse-polynomial gaps above both complete endpoint kernels.

This disposition does not adopt an unconditional geometric theorem, an unweighted theorem, a gate-independent \(\mathsf{BQP}_1\) result, ordinary \(\mathsf{BQP}\)-hardness, unrestricted \(\mathsf{SDQC}_1\)-hardness, novelty, or paper readiness.

## Independent operator check

Let \(Z\) be the preserved three-bit mixed label, \(D_{\rm dum}\) the untouched mixed dummy register, and \(J\) append the verifier, decision and scratch qubits in their fixed clean state. After running the clean-input verifier \(Q_x\) unconditionally, the reversible classical combiner computes its predicate into a fresh decision bit and uncomputes its scratch. Conjugating the decision projector gives a label-diagonal operator with blocks

\[
E_z=I\quad(z=000),\qquad
E_z=\Pi_q\quad(z\in T),\qquad
E_z=0\quad(z\in\{110,111\}).
\]

Because the verifier has no unresolved input register,
\[
\langle0_Q|Q_x^\dagger\Pi_qQ_x|0_Q\rangle=p_x
\]
is a scalar. Hence
\[
M_x=J^\dagger U_x^\dagger\Pi_aU_xJ
=\operatorname{diag}(1,p_x,p_x,p_x,p_x,p_x,0,0)
\otimes I_{\rm dummy}.
\]
Preservation of \(Z\) eliminates off-diagonal label blocks even for coherent label vectors. Entanglement between the verifier output and its workspace is already included in the scalar expectation. Clean compute-copy-uncompute makes the scratch disappear from the compression.

The combiner uses only \(X\), CX and CCX, with negative controls supplied by surrounding \(X\) gates. Since \(Q_x\) runs unconditionally, no controlled \(Q_x\), controlled \(H\otimes H\), single \(H\), approximate synthesis, spectator conversion, or complex phase is introduced. The fixed clean-input condition is essential: with an unresolved witness or mixed verifier input, the five blocks would generally contain an operator rather than \(p_x\).

## Spectrum, normalization and precision

With \(m\) ignored mixed bits, \(D=2^{m+3}\). If \(p_x=1\), six label blocks are perfect and two are zero, so both normalized trace and perfect-space fraction are \(3/4\), with zero off-perfect spectrum. If \(0\le p_x\le1/3\), only the unconditional block is perfect, giving perfect fraction \(1/8\), normalized trace \((1+5p_x)/8\le1/3\), and off-perfect ceiling at most \(1/3\). The edge cases \(p_x=0\) and \(p_x=1/3\) cause no exception.

The target values differ by \(5/8\). Threshold \(7/16\) with additive error \(\varepsilon<5/16\) separates them; the archived choice \(1/24\) is safely inside this range. Untouched dummy bits multiply the initial denominator and both perfect multiplicities by \(2^m\), so the ratio remains nontrivial while the denominator grows exponentially from a polynomial-size description.

That padding is mathematically legitimate, but it is an impact and exposition weakness. It does not show that hard dynamics acts nontrivially on every initial homology coordinate. The paper should call the denominator padding-generated rather than presenting it as an independent source of difficulty.

## Complexity consequence and evidence boundary

Assuming the corrected geometric theorem exactly as recorded, the output satisfies
\[
\beta_d(X_{\rm in})=D,
\qquad
\beta_d(X_{\rm out})
=\beta_d(X_{\rm in}\to X_{\rm out})
=\dim\ker(I-M_x),
\]
with whole-positive-spectrum endpoint gaps. Thus the weighted target is \(\mathsf{BQP}_1^{G_2}\)-hard. Under the separately checked statement \(\mathsf{BQP}_1^{\mathcal G}\subseteq\mathsf{BQP}_1^{G_2}\), the same target is hard for each covered fixed finite power-of-two-cyclotomic gate family \(\mathcal G\), considered separately.

Pro explicitly did not source-check Rudolph's Definition 2.2 or Theorems 2.3 and 3.4 and treated the geometric theorem as supplied. Before dispatch, this continuation performed a targeted check of those Rudolph statements for clean all-zero initialization, one computational-basis output measurement, perfect completeness, exact soundness reduction inside gate sets containing \(G_2\), and the stated cyclotomic inclusion. That was not a complete paper, proceedings-version, or priority audit. The optional finite-projector QSAT source and Marriott--Watrous route were not needed and were not checked in this gate.

## Relation to the earlier obstruction

The construction uses the exact distinction \(p_x=1\) versus \(p_x\le1/3\): five blocks become perfect precisely in YES instances. If both cases had \(p_x<1\), those blocks would remain nonperfect and both perfect fractions would be \(1/8\). It therefore evades the same-fraction obstruction through perfect completeness and does not repair arbitrary-threshold \(\mathsf{SDQC}_1\).

## Status and next gate

| Item | Disposition |
| --- | --- |
| Exact eight-label operator | **Accepted** |
| Coherent-label and garbage interface | **Accepted** |
| Exact \(G_2\) implementation | **Accepted** |
| \(3/4\) versus \(1/8\), error \(1/24\) | **Accepted** |
| Growing initial Betti denominator | **Accepted; padding-generated** |
| Weighted \(\mathsf{BQP}_1^{G_2}\)-hard composition | **Accepted conditional on the recorded geometric theorem** |
| Covered cyclotomic gate families | **Accepted conditional on the targeted Rudolph source check** |
| Unweighted hardness | **Conditional on separate common-copy unweighting** |
| Ordinary BQP / unrestricted SDQC1 / gate-independent BQP1 | **Withheld** |
| Novelty and publication value | **Open** |

The source-existence gate is closed at this scope. The next finite gate is a primary-source collision audit of the arbitrary-geometric-chain concentration theorem over degenerate logical kernels, its gap above the entire geometric kernel, natural filtered rank, and the eight-label non-all-or-none source composition. Exact multiplicity, the normalization definition, quotient dimension counting, ordinary min-max, and credited fixed gadgets must be excluded from any novelty claim.
