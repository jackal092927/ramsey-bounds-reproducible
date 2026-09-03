# King--Kohler corollary boundary and the surviving technical delta

September 3, 2026. **TARGETED SOURCE COMPARISON PLUS LOCAL ALGEBRA.** This note identifies which part of the degenerate-kernel result is already a short consequence of the King--Kohler proof architecture and which part still uses the new finite-certificate estimate. It does not audit every lemma in either paper.

## 1. The qualitative degenerate-kernel closure is short, conditionally

In [King--Kohler arXiv:2311.17234v2](https://arxiv.org/html/2311.17234v2), Theorem 10.1 is stated only as
\[
\lambda_{\min}(H)=0\Rightarrow\lambda_{\min}(\Delta)=0,
\qquad
H\succeq gI\Rightarrow\Delta\succeq EI.
\]
The proof nevertheless applies Lemmas 10.2--10.4 to an arbitrary normalized geometric chain \(x\). Equations (32) and the following display in the proof give, before positive definiteness is used, the schematic estimate
\[
1\le
\langle x,\Pi_Vx\rangle-
\langle x,H^{\rm emb}x\rangle+
C\left(t\lambda+t\lambda^2+
t e\lambda^{-\kappa}\right),
\tag{1}
\]
where \(e=\langle x,\Delta x\rangle\) and \(\kappa=4m+2\). The omitted register-complement term has a favorable sign.

Suppose (1) holds with a constant uniform in the instance size and
\[
H\succeq g(\Pi_V-P_K),\qquad P_K=P_{\ker H},\qquad0<g\le1.
\]
Writing \(p=\langle x,\Pi_Vx\rangle\), \(k=\langle x,P_Kx\rangle\), and \(h=\langle x,H^{\rm emb}x\rangle\), we have \(g(p-k)\le h\). Hence
\[
1-k=(1-p)+(p-k)
\le \frac{(1-p)+h}{g}
\le \frac{C}{g}\left(t\lambda+t\lambda^2+t e\lambda^{-\kappa}\right).
\tag{2}
\]
Choosing
\[
\lambda\le c\eta^2g/t,
\qquad
e<E\le c\eta^2g\lambda^\kappa/t
\]
makes every vector in the geometric spectral subspace below \(E\) project nontrivially into \(K\). Exact quotient injection then supplies \(\dim K\) zero modes, while injectivity of the projection on the entire sub-\(E\) spectral subspace gives at most \(\dim K\) such modes. Exact multiplicity and the gap above the whole kernel follow, including \(K=0\).

**Conclusion:** if the King--Kohler all-chain estimates are accepted with uniform constants and exact quotient injection is supplied, the qualitative degenerate-kernel multiplicity/gap theorem is a short corollary. Projection, min--max and dimension closure are not a credible novelty claim.

## 2. Why the imported estimate is not a clean uniform black box

### Basiswise perturbation does not imply a uniform projector bound

Definition 7.7 pairs orthonormal bases with per-vector distance \(O(\lambda)\). Lemma 7.4 then reads off an \(O(\lambda)\) projector-norm bound by summing the rank-one errors. That inference is not dimension-uniform without additional structure.

An explicit family shows the issue. Let \(r=\lambda^{-2}\), \(U=\mathbb R^r\oplus0\subset\mathbb R^{r+1}\), and let
\[
A=\lambda(1,\ldots,1):\mathbb R^r\to\mathbb R.
\]
Take \(U_\lambda\) to be the graph of \(A\), with the orthonormal basis formed by the columns of
\[
\begin{pmatrix}I\\A\end{pmatrix}(I+A^*A)^{-1/2}.
\]
Each column differs from its corresponding standard basis vector by exactly \(\lambda\sqrt{2-\sqrt2}=O(\lambda)\): the complement coordinate is \(\lambda/\sqrt2\), and the in-plane correction has norm \((1-1/\sqrt2)/\sqrt r\). But \(\|A\|=1\), so the largest principal angle is \(\pi/4\) and
\[
\|P_{U_\lambda}-P_U\|=1/\sqrt2.
\]
Thus the definition is adequate at fixed dimension but does not by itself give constants uniform over the exponentially growing padded register. A valid application must prove the estimate in the fixed active gadget before tensoring with the outside identity, or supply a direct operator estimate.

### The padded coordinate-bulk estimate has an outside differential

Claim 10.2 says every vertex touching the bulk has weight \(\lambda\). Under literal padding by an outside register, deleting or adjoining a weight-one outside vertex can stay inside the padded coordinate bulk. The archived exact fixture in `round2/check_padded_bulk.py` gives unrestricted squared boundary norm \(131073/65536\) at \(\lambda=1/256\), rather than \(O(\lambda^2)\). Restricting to local bulk tensored with outside harmonics cancels the outside differential and gives \(1/65536\).

Hayakawa's later [arXiv:2608.02726v1](https://arxiv.org/html/2608.02726v1), Lemma 6.1 proof sketch, explicitly places nonharmonic outside factors in the high band and invokes fixed active locality before tensor padding. That is compatible with this repair. It does not provide a degenerate-kernel theorem or the improved parameter dependence below.

## 3. Surviving technical delta

The finite-certificate theorem proves directly
\[
\boxed{
\|(I-P_K)x\|^2
\le C\left[t\lambda^2+
\frac{\langle x,\Delta x\rangle}{g\lambda^\kappa}\right].
}
\tag{3}
\]
It uses a fixed zero-weight kernel decomposition, a projected private differential, independent private supports, and exact filling. It does not use a growing-dimensional basiswise perturbation statement or the unrestricted padded coordinate bulk.

Equation (3) permits
\[
\lambda\le c\min(t^{-1},\eta/\sqrt t),
\qquad
E\le c'\eta^2g\lambda^\kappa.
\tag{4}
\]
The gadget scale is independent of the logical gap \(g\). For locality six, a conservative \(\lambda=\Theta(\eta/t)\) gives
\[
E=\Omega(\eta^{28}g/t^{26}),
\]
linear rather than degree-27 dependence on \(g\). This quantitative strengthening and its finite, checkable hypotheses are the plausible technical contribution. Whether that improvement plus the normalized-persistence application clears a strong venue remains an external novelty judgment.

## 4. Correct paper emphasis

The headline proof contribution should be the finite-certificate, instance-uniform estimate (3), framed as a repair and quantitative strengthening of the many-gadget analysis. The degenerate-kernel dimension closure should be presented as its corollary. The normalized-persistence theorem is then the main application: exact quotient naturality turns endpoint kernel control into a true persistent-rank ratio for a restricted BQP1 source.

The direction is **MEDIUM, conditional** until a referee-level comparison confirms that Hayakawa's fixed-family repair does not already yield (3) or an equally strong \(g\)-linear whole-kernel theorem. If it does, the remaining package is mostly an application and should not be sold as a standalone top-tier technical advance.
