# Common-multiplicity blow-up: functorial transfer corollary

2026-09-02. **LOCAL DERIVATION conditional on the cited source's symmetric-reduction and asymmetric-gap theorems.** The tiny check below verifies conventions, not those imported theorems.

## Convention and setup

Source: Hayakawa, [Unweighted Gapped Clique Homology](https://arxiv.org/html/2608.02726v1), Section 2.1, Definition 4.1, Lemma 4.2, Theorem 4.3. It uses coboundary-first weights: the raw simplex ket has norm w(sigma), the product of its vertex weights. Thus e_sigma=ket(sigma)/w(sigma) is normalized, and a coboundary incidence adding v has coefficient sign*w(v).

Let X_i be any finite diagram of clique complexes and inclusions. Give shared vertices the same weights. Choose one common M and integers f_v=M*w(v)^2, and use the same labeled copy block for each shared vertex at every level. The blow-up replaces v by a clique with f_v vertices and base edges by complete bipartite connections.

Define the degree-k isometry U_i by mapping e_sigma to the normalized sum over one-copy-per-block lifts of sigma:

    U_i e_sigma = (product_(v in sigma) f_v)^(-1/2) sum_copies ket(copied sigma).

Use orientations consistent across the diagram. For each one-copy-per-block lift, inherit the source simplex orientation; a block-major orientation may be used when it agrees, or corrected by the source's orientation sign. Write J_ij and Jhat_ij for the weighted-normalized and unweighted inclusions respectively.

## First lemma: no inclusion normalization factor

For every diagram arrow,

    Jhat_ij U_i = U_j J_ij.

Proof: common weights give J_ij e_sigma=e_sigma. Both sides then have exactly the same copied simplices, orientations and coefficients. Distinct base simplices have disjoint lift supports, so U_i is isometric. QED.

In the raw basis the same formula is

    U_i ket(sigma) = M^(-(k+1)/2) sum_copies ket(copied sigma).

This degree-dependent factor is real, but cancels across an inclusion, which preserves degree and uses common M. It must not be silently discarded when comparing operators in different degrees.

## Operator factors and harmonic transfer

The source's symmetric-reduction identity, expressed using the original weights rather than sqrt(f_v), gives within each level

    dhat_k U_(i,k) = sqrt(M) U_(i,k+1) d_(w,k),
    partialhat_k U_(i,k) = sqrt(M) U_(i,k-1) partial_(w,k),
    Deltahat_k U_(i,k) = M U_(i,k) Delta_(w,k).

An added vertex contributes sqrt(f_v)=sqrt(M)w(v); repeated-block coface terms cancel in opposite orientations. The boundary identity is the adjoint identity on the invariant symmetric sectors. These U_i are degree-wise isometries, not unscaled chain/cochain maps.

Theorem 4.3 of the source gives Deltahat >= min_v f_v on the asymmetric sector, for an arbitrary base clique complex. In particular, there are no asymmetric harmonic vectors. Consequently, if P_i and Phat_i are the respective harmonic projectors,

    Phat_i = U_i P_i U_i^*,
    ker Deltahat_i = U_i(ker Delta_i).

For a harmonic persistence map A_ij=P_j J_ij restricted to ker Delta_i, its blow-up counterpart satisfies

    Ahat_ij U_i = U_j A_ij.

Thus every arrow is unitarily equivalent on the full harmonic spaces. All its singular values are preserved, as are every guided overlap and every diagram-level algebraic rank invariant. This includes generalized rank for the resulting harmonic representation; it does not solve that rank efficiently.

If gamma_i is a positive lower bound on the nonzero spectrum of Delta_i, then the nonzero spectrum of Deltahat_i is bounded below by

    min(M gamma_i, min_(v in X_i) f_v).

If all vertex multiplicities have polynomial magnitude and are explicitly computable, the new graphs have polynomial size: Nhat_i=sum_v f_v, with adjacency determined by base adjacency or common block. This is a conditional transfer corollary, not a claim about arbitrary irrational weight inputs.

For a guide h in the initial harmonic space,

    ||Phat_j Jhat_ij U_i h|| = ||P_j J_ij h||.

Even without invoking the asymmetric-gap theorem, this last identity follows for symmetric input from the reducing-sector identity. The gap theorem is needed for the complete kernel correspondence and global promise transfer.

## Actual June 2026 harmonic-persistence hard family

Checked source: Gyurik-Schmidhuber-King-Dunjko-Hayakawa, [Provable Quantum Speedups](https://arxiv.org/html/2410.21258v2), Sections I.3-I.4, Lemmas 5-9 and Appendix B. Register vertices have weight one; added gadget vertices have one inverse-polynomial weight lambda. Lemma 6 constructs the initial guide as a succinct subset state wholly in the register. Lemma 7 states a final gap Omega(lambda^18 ell^-1 g), and Lemma 9 has exactly zero overlap in the NO case.

Choose lambda=2^-L inverse-polynomially small enough for those estimates and set M=2^(2L). Then register multiplicities are M and gadget multiplicities are one. The source estimates use a sufficiently small lambda relative to a known inverse-polynomial Hamiltonian-gap lower bound and the number of terms. A dyadic choice within a factor of two of a valid sufficiently small target retains this scale. This is a parameter-choice inference from its inequalities, not an independently audited proof of its imported gap theorem.

Every degree-p simplex in the initial guide contains only register vertices, so it has exactly M^(p+1) lifts. If the source guide is uniform over S, its image is exactly uniform over

    Shat = {(sigma, copy_0,...,copy_p): sigma in S, copy_r in [M]}.

Hence the lifted guide remains a subset state. Its product/union description stays compact by appending p+1 copy coordinates. Since M is a power of two, preparation adds exactly (p+1)log_2(M) Hadamards and copy-register bits to an existing guide-preparation circuit, plus reversible labeling. No exponential list of lifted simplices is created. The support cardinality |S|M^(p+1) is not a description-size cost.

The final global gap is at least min(M gamma_2,1), still inverse polynomial in the polynomially larger graph size. Guided overlap is unchanged exactly; the source's zero NO-overlap also avoids any ambiguity about exponentially small thresholds after graph-size blow-up. The original BQP1 hardness gate-set convention stays the original one: only the August paper's graph-theoretic Lemma 4.2/Theorem 4.3 are imported, not its differently-gated QMA1 hardness reduction.

**Guide orientation convention:** the positive subset-state statement inherits the June source's simplex orientations. Changing to a globally sorted-vertex computational basis can introduce signs. In that representation the preparation circuit must apply the efficiently computable source-orientation phases; it is then a signed subset state unless the target definition permits those phases. The spectral and persistence identities are basis-invariant, but a target promise insisting on strictly positive amplitudes in one prescribed sorted basis is not established by this argument. This distinction must be fixed explicitly in the final problem definition.

**Exact status:** conditional on the correctness and applicability of the cited source theorems, no additional functoriality, guide, or normalization obstruction remains for this special two-weight hard family. This appears to be a direct corollary combining the June and August papers, not a new substantial mechanism. What remains before stating a fully checked theorem is auditing the imported gap/selectivity results and the dyadic-parameter substitution in their exact hypotheses. Those are verification tasks, not identified missing research lemmas. A broader exhaustive novelty search has not been done.

This does not establish the July 2026 normalized-persistence conjecture: that conjecture requires a different, still unprovided exact-kernel multiplicity/filtration realization. Unweighting an already constructed family does not construct the missing family.

Additional scope checks: normalization by the total number of degree-p simplices is not preserved; that denominator can grow exponentially even for a polynomial graph blow-up. For a generic promise instance, a NO overlap below exp(-n) need not meet a new exp(-Nhat) cutoff; the exact-zero NO instances above avoid that issue. The June source promises the final-level nonzero gap only. A both-level-gap formulation requires checking the initial register separately rather than silently strengthening the source promise.

## Minimal failure without common multiplicities

One base vertex suffices. Give it one copy at the first level and two copies at the second. Literal inclusion sends the first symmetric state to (1,0), whereas the second symmetric state is (1,1)/sqrt(2). Their overlap is 1/sqrt(2), and the commuting-square residual is sqrt(2-sqrt(2)).

For growing but unequal blocks, the projection coefficient of an old orbit average onto the corresponding new average is sqrt(product_v f_(1,v)/f_(2,v)), with an additional asymmetric remainder. Independently choosing M at each level is therefore not harmless. A scalar rescaling does not remove that remainder.

## Tiny executable check

Run `python3 check_common_blowup.py`. It checks a three-vertex path contained in a filled triangle, f=(4,1,2), common M=4, and weights (1,1/2,1/sqrt(2)); each blow-up has seven vertices. Degrees 0,1,2 have exact zero inclusion residuals in floating-point arithmetic. Coboundary, adjoint and H1 Laplacian identities have residuals at most 7.7e-16. The unequal-multiplicity counterexample gives overlap 0.7071067812 and residual 0.7653668647. The symbolic argument above is the proof; this computation is only a convention/implementation check.

## Correction to the earlier report

The earlier PROBE_REPORT overstated the simultaneous asymmetric-gap obstacle: August Theorem 4.3 already covers arbitrary base clique complexes. Common-multiplicity functoriality is elementary. Therefore Candidate B's initially favorable research-novelty assessment must be downgraded to a likely direct corollary pending source verification, not promoted as a promising new ITCS mechanism.
