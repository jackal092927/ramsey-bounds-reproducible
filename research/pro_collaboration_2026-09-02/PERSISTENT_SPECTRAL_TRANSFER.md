# Simultaneous spectral transfer for persistent Laplacians

2026-09-02 PDT. Proposed by the retrieved ChatGPT Pro response; reconstructed locally below. **Status: a proved conditional structural corollary using the stated ordinary block-substitution theorem.** Its combined novelty is unestablished. This is not a quantum algorithm or a solution to the exact normalized-persistence hardness problem.

## Statement and conventions

Let $K_a\subseteq K_b$ range over a finite diagram of finite clique complexes, with compatible inclusions and one fixed positive weight $w(v)$ for each vertex. Use ordinary, unreduced chain spaces in degrees $k\ge0$, normalized simplex bases, and the weighted boundary

$$\partial_{w,k}[v_0,\ldots,v_k]
=\sum_{i=0}^k(-1)^i w(v_i)[v_0,\ldots,\widehat v_i,\ldots,v_k],$$

for $k\ge1$, with $\partial_{w,0}=0$. Augmented chains can instead be used consistently in all degrees. Choose $M>0$ with $f_v=Mw(v)^2$ positive integers. The copy blocks and their labels are the same throughout the diagram. Replace each vertex by a complete block of $f_v$ copies and each edge by all cross-block edges.

Assume the ordinary block-substitution facts of [Hayakawa, Lemma 4.2 and Theorem 4.3](https://arxiv.org/html/2608.02726v1): the fixed sectors identify with the weighted base chains under $U$, both boundary and adjoint intertwine with factor $\sqrt M$, and the ordinary asymmetric Hodge spectrum is at least $f_{\min}$. These are source theorems, not consequences of a finite fixture. The proof below supplies the persistent-domain step.

Let $J_{ab,k}$ be the isometric inclusion and define

$$D_{k+1}^{a,b}=\{z\in C_{k+1}(K_b,w):\partial_wz\in J_{ab,k}C_k(K_a,w)\},$$

$$b_{k+1}^{a,b}=J_{ab,k}^*\partial_w|_{D_{k+1}^{a,b}},\qquad
\Delta_{k,w}^{a,b}=b_{k+1}^{a,b}(b_{k+1}^{a,b})^*
+(\partial_{w,k}^a)^*\partial_{w,k}^a.$$

The domain has its inherited Hilbert norm; its adjoint is taken with that norm. Deleting outside rows from the full boundary and using its unrestricted domain would define a different operator.

For every pair and degree, the unweighted persistent Laplacian decomposes on the block-fixed sector $T_{a,k}$ and its orthogonal complement as

$$\widehat\Delta_k^{a,b}|_{T_{a,k}}
=U_{a,k}(M\Delta_{k,w}^{a,b})U_{a,k}^*,\qquad
\widehat\Delta_k^{a,b}|_{T_{a,k}^{\perp}}=R_{a,b,k}\succeq f_{\min}(a)I,$$

where $f_{\min}(a)=\min_{v\in K_a}f_v$. Empty chain spaces give vacuous blocks; if $K_a$ has no vertices, omit its minimum and interpret the entire statement as the zero-dimensional identity.

In particular, for $0<\Lambda\le f_{\min}(a)$,

$$\mathbf1_{[0,\Lambda)}(\widehat\Delta_k^{a,b})
=U_{a,k}\mathbf1_{[0,\Lambda/M)}(\Delta_{k,w}^{a,b})U_{a,k}^*.$$

The half-open cutoff is essential at the asymmetric threshold. Exact kernel multiplicities and persistent Betti numbers are preserved. Given a positive lower bound $\gamma$ on the base positive spectrum, the blown-up positive spectrum is bounded below by $\min(M\gamma,f_{\min}(a))$. Zero-dimensional kernels are allowed. A polynomial-time graph construction additionally requires $\sum_v f_v$ polynomial in the source input length; the structural identity itself does not imply that bound for arbitrary weights.

## Proof

**Naturality.** Define $U_{a,k}$ by replacing each base simplex with its normalized sum of one-copy-per-block lifts. Distinct base simplices have orthogonal lift supports. Compatible labels, weights and orientations give

$$\widehat J_{ab,k}U_{a,k}=U_{b,k}J_{ab,k}.$$

For each deleted base vertex, grouping its $f_v$ copies gives coefficient $\sqrt{f_v}=\sqrt M w(v)$, proving the boundary identity. The group $\prod_v S_{f_v}$ acts on oriented chains, with permutation signs included. A simplex containing two copies of one block is negated by the transposition of those copies, so it has no fixed coefficient. The fixed space is exactly the span of the stated orbit averages.

**Persistent domain.** Its defining support condition is invariant under the same group. Therefore its orthogonal fixed/asymmetric splitting is compatible with the source and target decompositions. For a fixed chain $U_{b,k+1}z$,

$$\widehat\partial U_{b,k+1}z\in C_k(\widehat K_a)
\iff U_{b,k}\partial_wz\in C_k(\widehat K_a)
\iff \partial_wz\in J_{ab,k}C_k(K_a,w).$$

The second equivalence follows from the disjoint orbit supports of base simplices present and absent in $K_a$. Thus

$$\widehat D_{k+1}^{a,b}\cap T_{b,k+1}
=U_{b,k+1}D_{k+1}^{a,b}.$$

On these Hilbert subspaces, the persistent boundary and its adjoint intertwine with $\sqrt M$. The persistent up operator consequently scales by $M$. So does the ordinary down operator. Equivariance of the boundary, invariant domain, and its orthogonal projection rules out fixed/asymmetric mixing exactly. This proves the symmetric block identity.

**Domination.** The ordinary source-domain inclusion $I:C_{k+1}(K_a)\hookrightarrow D_{k+1}^{a,b}$ is isometric and satisfies $bI=\partial_{k+1}^a$. Therefore

$$bb^*-\partial_{k+1}^a(\partial_{k+1}^a)^*
=b(I_D-II^*)b^*\succeq0.$$

The down terms agree, so $\Delta^{a,b}\succeq\Delta^{a,a}$. This applies to the blow-up as well. Restricting it to the reducing asymmetric sector and invoking the ordinary gap yields $R_{a,b,k}\succeq f_{\min}(a)I$. Functional calculus of the orthogonal blocks proves the projector and gap statements. The same $U_a$ is used for every arrow, so the construction is simultaneous over the diagram. $\square$

## What is already known and what remains to audit

The domination inequality is a special case of the operator decomposition in the proof of [Mémoli--Wan--Wang, Theorem 5.1](https://arxiv.org/html/2012.02808v1). It must not be called a new inequality. Hayakawa supplies the ordinary fixed/asymmetric block theorem. The restricted-domain equivariance argument is the local step connecting them. A targeted source check has not established priority for the combination or its significance as a standalone theorem.

Pro also suggested arbitrary simplicial complexes. The group-equivariance and persistent-domain arguments above extend immediately to block substitution defined by support membership in an arbitrary base complex. The remaining ordinary asymmetric bound appears to extend by the same expanded-star/join argument, but the formal statement above retains the published clique-complex scope. Nonflag numerical examples are diagnostic evidence for that extension, not its proof.

A sharp threshold example is one base vertex with $f$ copies: in degree zero, the symmetric constant vector has eigenvalue zero and every asymmetric vector has eigenvalue exactly $f$. Replacing $[0,f)$ with $[0,f]$ would add those extra modes.

This theorem concerns the **persistent** Laplacian, whose kernel has dimension equal to the persistent Betti number. It should not be confused with the ordinary later-level Laplacian or its harmonic-projection angle. The exact-kernel gadget reduction remains a separate claim.

## Finite verification

`check_persistent_unweighting.py` constructs the persistent domain as the nullspace of the outside-boundary rows, then forms the operator using an orthonormal domain basis. It checks multiple levels, degrees zero through two, nonuniform copies, new vertices, asymmetric directions, and a disk formed from two triangles whose outside diagonal cancels only in a linear combination. Thus the check would reject the tempting but incorrect row-deletion definition.

The probe is a small floating-point matrix check with explicit tolerances. The proof is the Hilbert-space argument above; extrapolation from small matrices is not used.
