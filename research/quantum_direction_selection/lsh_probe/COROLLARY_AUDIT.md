# Independent five-minute audit: functorial unweighting

Date: 2026-09-02. Verdict: **algebraically sound under the stated compatible-weight and polynomial-size promises; likely a short direct corollary, not yet a substantive independent research contribution.**

## Sources checked

- [Hayakawa, Unweighted Gapped Clique Homology is QMA1-complete, August 2026 preprint](https://arxiv.org/html/2608.02726v1), Lemma 4.2, Theorem 4.3, and Section 8. Lemma 4.2 identifies normalized symmetric-copy chains with the vertex-weighted source, using vertex weights sqrt(f_v). Theorem 4.3 bounds the asymmetric sector in every degree. Section 8 explicitly identifies harmonic-persistence unweighting as an outlook, so the combined result is not already stated there as a theorem.
- [Provable quantum speedups for computing persistence in topological data analysis, June 2026 version](https://arxiv.org/html/2410.21258v2), Sections I.1, I.3–I.4, and II. Section I.1 uses coefficient w(v) for the boundary in the normalized simplex basis; hence the two weighted conventions match. Register vertices have weight 1, gadget vertices have small weight lambda. Its succinct initial states use products/unions of register edge sets. The formal Harmonic Persistence problem promises a nonzero spectral gap only for K2. The hardness reduction's NO case has zero final harmonic space.

## Direct derivation

Let K1 be a subcomplex of K2, both clique complexes, with a fixed vertex weight on their union. Assume all f_v=M w(v)^2 are positive integers, with their sum polynomial in source input size. Use the SAME copies and copy labels at both levels. Define, on normalized source simplex basis,

    U_i |sigma>' = (product_{v in sigma} f_v)^(-1/2)
                   sum_{one copy per v in sigma} |sigma_copies>.

Then U_i is an isometry. Let J be the inclusion in source normalized bases and Jhat the inclusion of blow-ups. Termwise,

    Jhat U_1 = U_2 J.

The symmetric-reduction lemma gives

    Deltahat_i U_i = M U_i Delta_i.

The symmetric sector is reducing. The asymmetric gap excludes asymmetric harmonic vectors, so

    Pker(Deltahat_i) = U_i Pker(Delta_i) U_i^dagger.

Consequently,

    Pker(Deltahat_2) Jhat U_1 = U_2 Pker(Delta_2) J.

This exactly preserves harmonic-overlap norms and the harmonic-to-harmonic persistence operator, including its singular values. It works simultaneously along a filtration with fixed weights, not only for one pair.

At each level,

    gamma_plus(Deltahat_i) >= min(M gamma_plus(Delta_i), min_v f_v).

After polynomial operator normalization this remains an inverse-polynomial gap. The source reduction's register K1 is a join of a fixed bowtie complex, so its positive gap can also be checked by the augmented join formula if a strengthened both-level-gap target is desired.

## Guide and size checks

If a source k-simplex belongs entirely to the unit-weight register, all f_v=M. It expands into M^(k+1) simplices with the SAME coefficient. Therefore U|S> is exactly the uniform state on the expanded subset, not a nonuniform weighted guide.

Replace every described oriented edge uv by the M^2 oriented cross-block edges u_a v_b. Products and equal-size disjoint unions of edge sets retain their succinct form. Their descriptions enlarge by O(M^2), polynomial when M is polynomial. Intrablock edges exist in the graph but need not be included in the guide. Lift the source's computably specified simplex orientations; do not silently replace them by globally sorted vertex orientations. Arbitrary non-register subset states would not generally remain uniform.

For source weights {1,1/q} with polynomial integer q, choose M=q^2. Register blocks have q^2 copies and gadget blocks are singletons. If the source theorem only requires lambda below a computable inverse-polynomial threshold, choose a sufficiently small inverse-integer value; do not require computing the exact source spectral gap. Exact inverse-square encodability avoids weight-rounding and projector-stability issues.

## Strongest caveats

1. **Novelty:** the central proof is a basis-level naturality check plus the two imported spectral theorems. It plausibly resolves the explicitly mentioned special-case outlook, but should be presented first as a lemma/corollary note. It does not yet establish a FOCS/STOC-level new mechanism.
2. **Normalization is NOT preserved:** division by the total number of k-simplices can introduce enormous dilution after blow-up. Do not infer normalized Betti/persistence hardness or useful normalized-trace estimation from this proof.
3. **NO-threshold bookkeeping:** a generic overlap below exp(-n) need not be below exp(-N) after N=poly(n) expansion. The specific hardness reduction avoids this because its NO overlap is exactly zero.
4. **No stronger class claim:** the conclusion is BQP1-hard and in BQP, not automatically BQP-complete or BQP1-complete.
5. **Input promises matter:** fixed common weights, common M, polynomial multiplicities, and the register-only guide are essential. Variable weights along the filtration or arbitrary rational weights are not covered for free.
6. **Unsigned-guide orientation caveat:** June Section I.1 allows arbitrary fixed orientations per simplex. Its harmonic cycle can be a positive subset state in that convention. Under globally increasing vertex labels, the same cycle generally requires negative amplitudes (already a directed 1-cycle cannot have all-positive coefficients under an acyclic global orientation). A target demanding a strictly positive uniform guide in the globally sorted basis is not justified by this transfer. Inherit source orientations, or explicitly allow efficiently computable orientation phases/signed subset states.

No independent fatal flaw found in the proposed corollary during this bounded audit. The underlying imported preprint theorems were inspected but not re-proved in full.
