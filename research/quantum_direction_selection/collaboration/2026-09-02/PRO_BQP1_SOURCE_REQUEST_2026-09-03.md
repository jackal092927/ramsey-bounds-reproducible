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
