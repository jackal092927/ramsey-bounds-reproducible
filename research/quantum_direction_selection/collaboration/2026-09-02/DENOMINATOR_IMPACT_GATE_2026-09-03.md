# Denominator impact gate: fixed eight holes or replicated growth

September 3, 2026. **LOCAL CONSEQUENCE OF THE ACCEPTED EIGHT-LABEL OPERATOR.** This note changes the paper framing, not the mathematics of the source reduction.

## Cleanest theorem uses no dummy padding

The eight-label construction needs only three maximally mixed label bits. With no ignored dummy register,
\[
D=8,
\qquad
M_x=\operatorname{diag}(1,p_x,p_x,p_x,p_x,p_x,0,0).
\]
Therefore the geometric construction has
\[
\beta_d(X_{\rm in})=8
\]
on every instance, while
\[
\beta_d(X_{\rm in}\to X_{\rm out})=
\begin{cases}
6,&x\in L,\\
1,&x\notin L.
\end{cases}
\]
The true normalized persistence is exactly \(3/4\) versus \(1/8\). Under the recorded geometric hypotheses, additive approximation remains \(\mathsf{BQP}_1^{G_2}\)-hard even under the strong promise that the initial target-degree Betti number is the fixed constant eight.

This is the most honest primary corollary. It removes the appearance that exponential denominator growth contributes to hardness. It may also be an appealing restriction: the computational difficulty lies in determining which of eight known logical homology classes survive through a succinct high-dimensional clique filtration.

## Growing denominator is exact but replicated

Adding \(m\) ignored mixed bits gives
\[
M_x^{(m)}=M_x\otimes I_{2^m},
\qquad
D=2^{m+3}.
\]
Every multiplicity is multiplied by \(2^m\), so the ratio and all spectral promises are unchanged. This is mathematically legitimate and may be useful when a problem definition insists that the denominator grow. It is a replication closure, not evidence that the hard computation acts independently on exponentially many initial holes.

Applying an exact reversible scrambling \(W\) to the mixed coordinates changes the operator to
\[
W^*(M_x\otimes I)W.
\]
This can make every physical input bit appear in the circuit or every computational-basis coordinate enter the label predicate, but it preserves the tensor degeneracy up to unitary equivalence. Such scrambling does not make the denominator intrinsic and should not be presented as a repair.

## What an intrinsic large-denominator result would require

A materially stronger density theorem needs a source family \(M_x\) whose growing perfect eigenspace is not a fixed ancillary tensor factor and whose YES/NO perfect-space fractions are separated. Possible sources include a restricted exact mixed-input circuit problem with an independently established standard-class hardness theorem or a counting source with controlled normalization. The existing arbitrary-threshold \(\mathsf{SDQC}_1\) trace promise is insufficient: subunit eigenvalues can change the trace without changing the perfect eigenspace.

Until such a source is proved, the paper should state the fixed-eight theorem first and list tensor replication as an optional closure property. This converts “padding-generated denominator” from a hidden weakness into an explicit scope boundary. It does not by itself raise the novelty rating above **MEDIUM, conditional**.
