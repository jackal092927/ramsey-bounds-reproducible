# Disposition of the Pro novelty and theorem-delta review

September 3, 2026. **RESPONSE COLLECTED; CLAIMS DISPOSITIONED AGAINST THE POST-DISPATCH LOCAL AUDIT; NO MATHEMATICAL COUNTEREXAMPLE FOUND.** Read this with [the raw response](PRO_NOVELTY_REVIEW_2026-09-03.md), [the local collision audit](NOVELTY_COLLISION_AUDIT_2026-09-03.md), and [the King--Kohler equation-level boundary](KING_COROLLARY_BOUNDARY_2026-09-03.md). The Pro response directly inspected the listed arXiv pages, but could access only metadata and the abstract for the final SIAM publication. Neither the response nor this disposition is an exhaustive priority certification.

## Decision

The project passes the current mathematical gate and should enter manuscript drafting. The proof should be organized around the corrected finite-certificate all-chain leakage theorem. The degenerate-kernel substitution, quotient dimension closure, and common-copy unweighting are consequences or applications and cannot carry the central novelty claim.

No counterexample was found to the theorem under its explicit finite-palette, private-support, exact-filling, all-bidegree-padding, interface, and independent-interior hypotheses. The remaining high-value source gate is narrower: inspect the final SIAM version of King--Kohler to determine whether it already repairs the arXiv-v2 padded-bulk argument or proves an equivalent uniform finite-local estimate. That uncertainty changes positioning and venue; it does not block a carefully scoped v0.

## Accepted conclusions

### 1. Strongest collision: accepted

King--Kohler's arXiv-v2 proof already applies its main sector estimates to an arbitrary full geometric chain and invokes positive definiteness only at the final logical coercivity step. If those estimates are uniform and correct after padding, replacing
\[
H\succeq gI
\quad\text{by}\quad
H\succeq g(P-P_K)
\]
and applying projection/min--max gives the qualitative whole-kernel theorem in a short argument. This agrees with the independent derivation in `KING_COROLLARY_BOUNDARY_2026-09-03.md`.

**Disposition:** the kernel substitution and dimension closure are mathematically valid but low-novelty consequences. They should appear as a compact corollary, not as the claimed new mechanism.

### 2. Padded coordinate-bulk objection: accepted as a mathematical issue in arXiv v2

The Pro response independently identified the same obstruction recorded locally. If a local bulk simplex is joined with an outside-register simplex containing a weight-one vertex, deleting that outside vertex remains inside the padded coordinate bulk with coefficient one. Therefore the literal full-coordinate bulk differential need not be (O(\lambda)). The archived exact fixture gives the corresponding quantitative failure.

**Disposition:** this is a mathematical objection to the displayed arXiv-v2 proof step, not merely a novelty concern. It does not establish that the final published theorem is false, because the final SIAM proof was inaccessible and may contain a repair.

### 3. Surviving transfer theorem: accepted, with one exposition requirement

The response's proposed estimate
\[
\operatorname{dist}(x,K_A)^2
\le C\left[t_A\lambda^2+
\frac{\langle x,\Delta_Ax\rangle}{g_A\lambda^\kappa}\right]
\]
matches the locally proved implication. Its key inputs are the zero-weight kernel decomposition, projected private-pair coercivity, outside-harmonic padding in every bidegree, the shared-register interface bound, and exact local filling. It avoids both the unrestricted padded coordinate bulk and a dimension-dependent conversion from basiswise perturbation to projector norm. It permits choosing (\lambda) independently of the logical gap and therefore yields a final geometric gap linear in (g_A).

The proof in the manuscript must not compress the PSD step into the phrase "exact filling plus a local gap." It must explicitly state that (\operatorname{ran}\Pi_j\subseteq B_d(Y_j)\), boundaries are orthogonal to the harmonic kernel, the up-Laplacian has the required positive spectral floor on its range, and up-columns partition across independent gadget interiors. Those facts yield
\[
\Delta_A^\uparrow\succeq c\lambda^\kappa H_A^{\rm emb}.
\]
This is an exposition obligation, not a newly found gap.

### 4. Gyurik et al. boundary: accepted

Gyurik et al. already state a gap above the complete final harmonic space in their particular guided construction. Their displayed proof moves from an arbitrary geometric low-energy vector to a lemma stated on the simulated-register image. The response correctly treats this as an apparent domain mismatch rather than a theorem refutation.

**Disposition:** do not claim the first whole-kernel gap. Present the present theorem as an independent all-chain repair and a uniform generalization with exact multiplicity, two endpoints, and filtered quotient naturality.

### 5. Quotient naturality: accepted at restricted scope

Independent interiors and exact filling give
\[
B_d(X_A)\cap V=W_A,
\qquad W_A=\sum_{j\in A}\operatorname{ran}\Pi_j.
\]
After the all-chain upper bound rules out additional homology, the map (v\mapsto[v]) identifies (H_d(X_A)) with (V/W_A). For (A\subseteq B), simplicial inclusion is the quotient epimorphism
\[
V/W_A\twoheadrightarrow V/W_B.
\]
Its rank is (\dim(V/W_B)=\dim\ker H_B).

**Disposition:** this gives the exact numerical persistent rank needed for the constructed nested-term-set family and bypasses literal compatible harmonic isometries there. It neither proves Lowe et al.'s Conjecture 2 nor resolves their unrestricted Conjecture 1. The algebra is standard; the value is in integrating it with the corrected transfer theorem.

### 6. Common-copy unweighting: accepted as a sourced corollary

Using the same labeled copy blocks at every level gives the commuting inclusion square. Hayakawa's symmetric-sector identity scales each weighted endpoint Laplacian by the common factor (F), and the asymmetric sector has a separate positive floor. For dyadic (\lambda), (F=\lambda^{-2}) is polynomial, and later gadget vertices can be present initially as isolated vertices because (d\ge1).

**Disposition:** the unweighted filtration theorem is a direct corollary of the weighted theorem plus Hayakawa's decomposition. It is no longer marked blocked. It should be included in v0, credited as such, with the common-block and orientation conventions explicit.

## Complexity and denominator positioning

The clean complexity statement remains the fixed-eight theorem. With no ignored mixed dummy bits,
\[
\beta_d(X_{\rm in})=8,
\qquad
\beta_d(X_{\rm in}\to X_{\rm out})=
\begin{cases}
6,&x\in L,\\
1,&x\notin L,
\end{cases}
\]
so the true normalized ratio is (3/4) versus (1/8). The source class is the exact gate-dependent (\mathsf{BQP}_1^{G_2}), together with the separately stated fixed cyclotomic gate families covered by Rudolph. No ordinary BQP, unrestricted (\mathsf{SDQC}_1), gate-independent (\mathsf{BQP}_1), or complex-phase theorem follows.

Ignored mixed bits give exact tensor replication, but the resulting growing denominator is not intrinsic. This is an impact and interpretation limitation, not a mathematical flaw. The paper should state the fixed-eight restriction first and mention replication only as a closure property.

## Novelty and source boundary

The external review rates the package medium and places it near TQC/Quantum, with a possible ITCS/ICALP case if the unweighted theorem, proof repair, and reusable transfer theorem are written cleanly. We record that as advice, not a writing gate. The current strategy explicitly separates venue strength from whether the result merits a complete manuscript.

The exact source-checking boundary is:

- the Pro response directly checked the relevant arXiv pages for King--Kohler, Gyurik et al., Lowe et al., Hayakawa, Crichigno--Kohler, Rudolph, and the nearby simplex-normalized work;
- it did not recompute the local certificates;
- it could not inspect the detailed final SIAM King--Kohler text;
- it did not exhaust later papers, citations, unpublished work, or all versions.

The finite falsification gate is therefore unchanged: if the final SIAM proof already contains the outside-harmonic/fixed-local repair or an equivalent uniform (t\lambda^2) leakage theorem, the analytic novelty drops sharply. The mathematical theorem and normalized-persistence application still remain valid at their stated dependencies.

## Action

Start manuscript v0 now. Lead with the community problem of true initial-homology-normalized persistence under whole-kernel endpoint gaps; state the finite-certificate transfer as the proof contribution; make quotient naturality the filtered bridge; state the fixed-eight weighted hardness theorem and the unweighted sourced corollary; and expose the source, denominator, gate-family, and quantitative-gap limits in the abstract and introduction.
