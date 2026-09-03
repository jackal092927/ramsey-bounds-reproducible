# Conditional simultaneous unweighting of persistent Laplacians

September 2, 2026 PDT. Origin: Section 6 of the [completed first Pro response](PRO_PREVIOUS_TDA_RESPONSE.md). The derivation below was independently checked algebraically during consolidation. It is conditional on the stated single-complex symmetric-sector identity and asymmetric gap. It does not certify novelty or re-prove Hayakawa's local spectral package.

We restrict the formal statement to clique complexes, the domain of the imported result. Pro's proposed extension to arbitrary simplicial block substitutions is retained in its raw response but is not adopted here without checking the star/link argument.

## Statement

Let \(K_\alpha\subseteq K_\beta\) be a finite diagram of weighted clique complexes with a fixed positive weight \(w(v)\) for every shared vertex. Choose one \(F>0\) such that \(f_v=Fw(v)^2\) are positive integers. Use the same labeled clique block of \(f_v\) copies at every level containing \(v\). Write \(\widehat K_\alpha\) for the resulting unweighted blow-ups.

For each level and degree, the normalized one-copy-per-block lift \(U_{\alpha,k}\) is an isometry onto the subspace fixed by the product of block permutation groups (acting on oriented chains). Assume the imported single-complex identities
\[
\widehat\partial U_{\alpha,k}
=\sqrt F\,U_{\alpha,k-1}\partial_w,\qquad
\widehat\Delta_{\alpha,k}|_{T_{\alpha,k}^{\perp}}
\succeq f_{\min}(\alpha)I,
\]
where \(T_{\alpha,k}=\operatorname{ran}U_{\alpha,k}\) is reducing and
\(f_{\min}(\alpha)=\min_{v\in K_\alpha}f_v\). The source and blow-up use the same compatible orientation convention. Empty chain spaces have vacuous assertions; take nonempty initial vertex sets when defining \(f_{\min}\).

Equip the persistent chain domain with its **inherited** Hilbert-space inner product:
\[
D_{k+1}^{\alpha,\beta}
=\{z\in C_{k+1}(K_\beta):\partial_wz\in C_k(K_\alpha)\},
\quad b^{\alpha,\beta}=\partial_w|_{D_{k+1}^{\alpha,\beta}}.
\]
Its adjoint is computed relative to that inherited metric, not an arbitrary nonorthonormal nullspace basis. Define
\[
\Delta_k^{\alpha,\beta}
=b^{\alpha,\beta}(b^{\alpha,\beta})^\dagger
+(\partial_{w,k}^{\alpha})^\dagger\partial_{w,k}^{\alpha}.
\]

Then for every comparable pair,
\[
\widehat\Delta_k^{\alpha,\beta}
\cong F\Delta_k^{\alpha,\beta}\oplus R_{\alpha,\beta,k},
\qquad
R_{\alpha,\beta,k}\succeq f_{\min}(\alpha)I.
\]
The identification of the first summand is \(U_{\alpha,k}\). Consequently, for
\(0<\Lambda\le f_{\min}(\alpha)\),
\[
\mathbf1_{[0,\Lambda)}(\widehat\Delta_k^{\alpha,\beta})
=U_{\alpha,k}\mathbf1_{[0,\Lambda/F)}(\Delta_k^{\alpha,\beta})
U_{\alpha,k}^\dagger.
\]
This preserves all low eigenvalues in that interval with the stated scaling and multiplicities, including the kernel. It gives a conditional gap bound
\[
\widehat\gamma_+\ge
\min\{F\gamma_+(\Delta_k^{\alpha,\beta}),f_{\min}(\alpha)\}.
\]

## Proof

**Common sectors and the persistent domain.** Let \(G\) be the product of the permutation groups of all copy blocks in the diagram. It acts orthogonally on oriented chains and preserves each complex and each inclusion. Therefore the persistent domain is \(G\)-invariant and decomposes orthogonally into its fixed and complementary parts.

The fixed part is exactly
\[
(\widehat D_{k+1}^{\alpha,\beta})^G
=U_{\beta,k+1}D_{k+1}^{\alpha,\beta}.
\]
Indeed, for \(U_{\beta,k+1}z\), its boundary is
\(\sqrt F U_{\beta,k}\partial_wz\). Different base simplices have disjoint lift supports; this boundary lies in \(C_k(\widehat K_\alpha)\) precisely when \(\partial_wz\) is supported in \(K_\alpha\).

Hence the restricted persistent boundary on fixed sectors is \(\sqrt F\,b^{\alpha,\beta}\) in the two isometric coordinates. Its adjoint has the same factor. The down term also scales by \(F\). Equivariance prevents mixing between fixed vectors and their orthogonal complement. This proves the exact symmetric summand.

**Persistent domination.** The isometric inclusion
\(J:C_{k+1}(K_\alpha)\hookrightarrow D_{k+1}^{\alpha,\beta}\)
satisfies \(bJ=\partial_{k+1}^{\alpha}\). Since \(JJ^\dagger\preceq I\),
\[
bb^\dagger-bJJ^\dagger b^\dagger
=b(I-JJ^\dagger)b^\dagger\succeq0.
\]
The down terms are equal, so
\[
\Delta_k^{\alpha,\beta}\succeq\Delta_k^{\alpha,\alpha}.
\]
Apply this inequality to the blow-up and restrict to its reducing asymmetric sector. The imported ordinary-Laplacian gap supplies \(R\succeq f_{\min}I\). Functional calculus gives the spectral-projector statement. \(\square\)

## Scope and checks

This is a short conditional structural theorem. Its newness and independent paper value remain unknown. The standard domination inequality is not advertised as novel.

The argument does not deduce a persistent positive gap from the two endpoint positive gaps: shrinking a kernel can introduce new, small positive eigenvalues. It uses domination only to transfer the **already positive asymmetric sector** bound. It does not turn a low-energy approximation into an exact homology count, solve the unrestricted normalized-persistence conjecture, or provide a barcode algorithm.

Polynomial-size conversion additionally requires computable polynomial total multiplicity. Changing the copy counts across levels breaks the natural fixed sectors, as the existing one-vertex fixture shows.

The accompanying check_persistent_laplacian.py tests an actual persistent domain, computed using an orthonormal nullspace basis, for a four-cycle filled by two triangles sharing a later diagonal. Neither triangle alone has boundary supported on the initial cycle, but their linear combination does. It checks the induced metric/adjoint, exact symmetric-block identity numerically, cross-sector reduction, persistent domination, the asymmetric lower bound, and the persistent rank by independent cycle/boundary ranks. A finite check supports that implementation only.
