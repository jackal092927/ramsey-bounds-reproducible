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
