# All-chain concentration from finite zero-weight certificates

2026-09-03. **CONDITIONAL PROOF LOCALLY CHECKED AND REVIEWED; COMPLETE PALETTE NOT YET CERTIFIED.** This sharpens and simplifies [the spectral-sector derivation](EXACT_FILLING_COERCIVITY.md). The [bounded Pro review](PRO_BOUNDED_PROOF_REVIEW_2026-09-03.md) and [independent disposition](PRO_BOUNDED_PROOF_DISPOSITION_2026-09-03.md) support the implication under the stated finite hypotheses. One actual source representative passes every finite check below; closure for the complete guarded circuit palette is a separate gate. No optimal spectral valuation or priority is asserted.

The candidate result is
\[
\boxed{\|(I-P_K)x\|^2\le C\left(t\lambda^2+
\frac{\langle x,\Delta x\rangle}{g\lambda^\kappa}\right)}.
\tag{A}
\]
Here H is the logical sum of projectors, P_K projects onto its embedded kernel, and Delta is the full geometric Laplacian. This is an estimate for every normalized geometric chain. The positive logical gap g does not enter the choice of gadget weight.

## 1. Exact finite local data

An active gadget has a weight-one register R_a of top degree d_a, a finite set of new vertices of weight lambda, and its full clique complex Y_a. Work in the canonical Euclidean coordinates for normalized chains, so its degree-d_a differential pair is
\[
D_a(\lambda)=
\begin{bmatrix}\partial_{d_a}(\lambda)\\
\partial_{d_a+1}(\lambda)^*\end{bmatrix}
=D_{a,0}+\lambda D_{a,1}.
\]
The value at zero is a matrix limit; no invertible weight gauge at zero is assumed.

Let V_a=Z_{d_a}(R_a), with projector P_a. A certificate supplies an explicitly specified subspace Q_a supported entirely on private chain coordinates and an output projection R_a^{out}. Q_a need not be spanned by individual simplices: the proof only uses private support, orthogonality and the certified bounds. This makes explicit the scope already used by outside-harmonic padding. Require:

1. **Exact topology at positive weight:** at lambda=1,
   \[
   B_{d_a}(Y_a)\cap V_a=\operatorname{ran}\Pi_a
   \]
   for the intended logical projector Pi_a.
2. **Zero-weight kernel:**
   \[
   \ker D_{a,0}=V_a\oplus Q_a.
   \]
   The summands are orthogonal.
3. **Projected private differential:** with T_a(lambda)=R_a^{out}D_a(lambda),
   \[
   T_a(\lambda)=\lambda T_{a,1},\quad T_{a,1}P_a=0,\quad
   \|T_{a,1}Q_a z\|\ge b\|Q_a z\|.
   \]
   All retained output simplices contain a private vertex of this gadget.

Every matrix is of fixed size. Thus the positive gap of D_{a,0}^*D_{a,0}, the norms of D_{a,1} and T_{a,1}, and b>0 have constants uniform over a finite certified palette. No spectral-projector convergence or identification of a lifted eigenvector is assumed.

For integer matrices these properties admit finite exact certificates: rank lower bounds modulo a prime, matching rational upper bounds from explicitly known kernels, exact filling chains, and nonzero determinants of Gram matrices. This establishes a theorem for the specified finite graphs, not for every integer-state gadget.

## 2. A local positive-gap lower bound without spectral valuation

For a positive vertex weight w, let W_k be the diagonal matrix of products of weights on degree-k simplices. In the stated coordinates,
\[
\partial_{w,k}=W_{k-1}^{-1}\partial_{1,k}W_k.
\]
For 0<lambda<=1 with weights in {1,lambda},
\[
\sigma_{\min}(W_{k-1}^{-1})\ge1,\qquad
\sigma_{\min}(W_k)\ge\lambda^{k+1}.
\]
The singular-value inequality for invertible left and right scalings, at the fixed nonzero rank of the boundary, gives
\[
\sigma_{\min}^+(\partial_{w,k})\ge
\lambda^{k+1}\sigma_{\min}^+(\partial_{1,k}).
\]
For clarity, if A is any nonzero rectangular matrix and L,R are invertible, put K=ker A. For a unit x perpendicular to R^{-1}K,
\[
\operatorname{dist}(Rx,K)=\inf_{z\in R^{-1}K}\|R(x-z)\|
\ge\sigma_{\min}(R).
\]
Consequently ||LARx||>=sigma_min(L) sigma_min^+(A) sigma_min(R). This proves the scaling inequality without assuming full rank. Zero-rank boundary blocks can be omitted. The Hodge decomposition gives
\[
\gamma_+(\Delta_{a,d_a}(\lambda))
\ge c_a\lambda^{2d_a+4}.
\tag{B}
\]
For a finite palette with d_a=2m_a-1 and m_a<=m, take
\(\kappa=4m+2\) and a common c_a>=c>0. This is a lower bound, not a claim of equality, optimal order, or a leading coefficient.

One explicit constant is available directly from the unweighted integer Laplacian: if its rank is r>0 and its operator norm is at most an integer B>=1, the product of its nonzero eigenvalues is a nonzero integer coefficient of its characteristic polynomial. Thus
\[
\gamma_+(\Delta_a(1))\ge B^{-(r-1)}.
\]
The weight gauge also preserves the exact boundary intersection with V_a, because every register simplex has weight one.

## 3. Padding and independent attachment hypotheses

Pad an active gadget by joining with the unused register. Use reduced chain complexes for joins, including degree -1. The outside register has reduced homology only in its top degree q, and has a positive gap bounded below by a constant on all other modes. The join Laplacian is
\[
\Delta_{Y_a*R_{out}}=\Delta_{Y_a}\otimes I+
I\otimes\Delta_{R_{out}}
\]
on the direct sum of the appropriate bidegrees.

At the global target degree d=d_a+q+1, the only **outside-harmonic** bidegree is (d_a,q). Other bidegrees can and do occur; they have a positive outside gap. It follows that the padded zero-weight kernel is precisely
\[
V\oplus(Q_a\otimes\mathcal H_{out}),
\]
with a uniform positive gap on its complement. The local derivative norms remain uniform because only the fixed active gadget has lambda-dependent entries. Pad the private output projection with the outside harmonic projector; outside differential terms vanish on both sides. Conditions 1--3 and (B) then persist with constants independent of the outside register dimension. The padded exact filling statement follows from the join homology tensor decomposition. In particular, outside padding is different from building a product guard into a new active attaching sphere; the latter still needs a separate finite-family or closure argument.

Attach t>=1 padded gadgets along a common register R of top dimension d. Interiors are independent: there is no simplex using private vertices from different gadgets. Common weights and coordinate embeddings are used throughout. Write
\[
C_d(X)=C_R\oplus\bigoplus_i C_i^{priv},\qquad
x=\omega_0+\sum_i\omega_i,\quad x_i=\omega_0+\omega_i.
\]
For the register-output interface L_i, assume or verify
\[
L_iL_i^*\preceq N_*\lambda^2 I.
\tag{C}
\]
This follows for a fixed vertex palette by expressing removal of each possible private vertex as a signed coordinate partial isometry; only a fixed number of such removals can land entirely in the register. Its constant therefore does not grow with the outside register. Inputs of different L_i are orthogonal; their register outputs are shared.

Let P be the projector onto V=Z_d(R), H=sum_i Pi_i on V, and
\[
H\succeq g(P-P_K),\qquad 0<g\le1.
\]
The logical rank-one active constraints can have higher rank after outside padding.

## 4. Global interface energy

For a normalized x put e=||D_X x||^2, U=sum_i||omega_i||^2, and
\[
\rho=\lambda^{-2}\|[L_1\ \cdots\ L_t]\|^2\le N_*t,\qquad
\chi=(t-2)_+\rho+N_*\le C t^2.
\]
Set a=partial_R omega_0, y_i=L_i omega_i, y=sum_i y_i, and r=a+y. The exact identity
\[
\sum_i\|y-y_i\|^2=(t-2)\|y\|^2+\sum_i\|y_i\|^2
\le\chi\lambda^2 U
\]
also covers t=1. All non-register down outputs split by gadget, as do all up columns. Hence
\[
\sum_i\|D_i(\lambda)x_i\|^2
\le 2t e+2\chi\lambda^2 U.
\tag{D}
\]
The factor U is retained; replacing it by one loses the useful absorption step.

## 5. Leakage from finite zero-weight data

In each padded chain space let A_{i,0}=I-P-Q_i. The certified zero-weight gap and D_i(lambda)=D_{i,0}+lambda D_{i,1} yield
\[
\begin{aligned}
S_A:=\sum_i\|A_{i,0}x_i\|^2
&\le C\sum_i\|D_{i,0}x_i\|^2\\
&\le C\left(te+\chi\lambda^2 U+
\lambda^2\sum_i\|x_i\|^2\right)\\
&\le C(te+\chi\lambda^2 U+t\lambda^2).
\end{aligned}
\tag{E}
\]
Here sum_i||x_i||^2=1+(t-1)||omega_0||^2<=t.

Since T_iP=0,
\[
T_iQ_i x_i=T_i x_i-T_iA_{i,0}x_i.
\]
Bulk injectivity, ||T_i||<=C lambda, and orthogonal retained private output blocks imply
\[
S_Q:=\sum_i\|Q_i x_i\|^2
\le C\left(\frac{\sum_i\|T_i x_i\|^2}{\lambda^2}+S_A\right)
\le C(e/\lambda^2+S_A).
\tag{F}
\]
This output orthogonality concerns T_i; no such assumption is made for L_i.

Put N=||(I-P)x||^2. Orthogonality of V, Q_i and A_{i,0} gives
\[
N\le U+t\|(I-P)\omega_0\|^2=S_A+S_Q.
\]
Substituting (E)--(F), using U<=N, and choosing chi lambda^2 below a fixed palette constant gives
\[
\boxed{N\le C[t\lambda^2+(t+\lambda^{-2})e]}.
\tag{G}
\]
The sufficient choice lambda<=c/t is independent of the logical gap g. No estimate against Delta's unknown kernel entered this proof.

## 6. Logical coercivity and exact multiplicity

Exact filling and (B), applied on the local boundary subspace, imply the elementary operator inequality
\[
\Delta_i^\uparrow\succeq c\lambda^\kappa\Pi_i.
\]
Because R has no degree-(d+1) simplex, up columns partition exactly by gadget:
\[
\Delta^\uparrow=\sum_i\iota_i\Delta_i^\uparrow\iota_i^*
\succeq c\lambda^\kappa H^{emb}.
\tag{H}
\]
Split distance into geometric leakage and forbidden logical mass. Equations (G)--(H) give
\[
\begin{aligned}
\|(I-P_K)x\|^2
&=N+\langle x,(P-P_K)x\rangle\\
&\le C[t\lambda^2+(t+\lambda^{-2})e]
+\frac{e}{c g\lambda^\kappa}\\
&\le C[t\lambda^2+e/(g\lambda^\kappa)].
\end{aligned}
\]
The last step uses lambda<=c/t, kappa>=2, g<=1. This proves (A).

Choose
\[
\lambda\le c\min(t^{-1},\eta/\sqrt t),\qquad
E\le c'\eta^2g\lambda^\kappa,\qquad 0<\eta<1.
\]
Every normalized vector in the geometric spectral subspace below E has nonzero projection into ker H. Its dimension is therefore at most dim ker H. Exact local filling plus independent interior chains gives
\[
B_d(X)\cap V=\sum_i\operatorname{ran}\Pi_i,
\]
so V/sum_i ran Pi_i injects into H_d(X) and supplies at least dim ker H exact zeros. Consequently,
\[
\dim\ker\Delta=\dim\ker H,\quad
\operatorname{spec}(\Delta)\cap(0,E)=\varnothing,\quad
\|P_{\ker\Delta}-P_K\|\le\eta.
\]
The zero-dimensional logical kernel is included. There is no added global relative-acyclicity assumption.

For nested term sets, compatible quotient maps are surjective; their homology realizations have persistent rank equal to the later logical kernel dimension. An initial history kernel of known dimension D>0 therefore gives the true normalized fraction dim ker H_final/D.

A conservative dyadic lambda=Theta(eta/t) gives, for kappa=26,
\[
E=\Omega(\eta^{28}g/t^{26}).
\]
Under the separately imported common-copy unweighting theorem, F=lambda^{-2} gives a geometric floor min(FE,1), hence an attainable scale
\[
FE=\Omega(\eta^{26}g/t^{24}).
\]
These poor polynomial lower bounds are not practical runtime predictions.

## 7. What has and has not passed

[The actual Rudolph representative certificate](REPRESENTATIVE_GADGET_CERTIFICATE.md) verifies the active data for the projector onto |00>-|10>-|11>. Its source graph has 41 vertices, 322 edges, target degree 3, Betti number 3, zero-weight kernel dimension 180=4+176, and an injective projected central pair.

This is a complete check of the finite inputs needed by this route for that one graph, conditional on the documented graph replay matching the pinned source. The replay, integer matrices, modular arguments and full filling chain are archived. The earlier spectral-sector theorem remains an independent route with stronger imported hypotheses.

Outstanding: every other required active atom, closure under guarded attaching-sphere products through locality six, complete source/priority assessment, and the strongest meaningful exact source-complexity consequence. The current theorem is conditional on the finite family satisfying the listed data. It is not a certification of the full circuit reduction or submission readiness.

**Later September 3 update:** [explicit register relabelings](ACTIVE_HADAMARD_ORBIT.md) transport the representative certificate to all four unguarded active Hadamard three-term vectors. The [selected-cycle guard lemma](SELECTED_CYCLE_GUARD_CLOSURE.md) gives an alternative explicit guard construction and basis atom; its exact checks and bounded review support the conditional closure. [Source-pinned exact certificates](REMAINING_ACTIVE_ATOM_CERTIFICATES.md) now cover the one-qubit difference and both two-qubit two-term atoms. These components locally close the fixed palette for the [clean restricted theorem](CLEAN_RESTRICTED_REDUCTION_THEOREM.md). End-to-end review, source complexity, and priority remain open. These updates do not retroactively alter frozen Pro inputs.
