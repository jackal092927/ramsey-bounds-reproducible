# Quantum generalized persistence: bounded independent probe

Date: 2026-09-02. Scope: source-led literature check, analytic obstruction, one small executable check. No changes to QuantumTDA, no external model submission, no experiments beyond the mathematical fixture below.

## Bottom line

**No positive quantum speedup theorem is established.** The strongest concrete progress is a native simplicial counterexample to the raw limit/colimit projector route. All local complexes and local spectral data are fixed, both module constraint gaps stay bounded away from zero, but the relevant overlap is exponentially small.

For the Dey-Xin / AIDA decomposition line, the only quantum candidate worth the next bounded probe is an exact, reversible, incrementally updated ExtensionDecomp split test. The first lemma must be about the actual finite-field equations, not QSVT or an unexplained quantum rank oracle. If that lemma fails or a classical local-algebra reduction removes the search, stop the quantum-decomposition branch.

## 1. Exact literature/model map

| Source | Object and model | Consequence here |
|---|---|---|
| Dey-Xin, [Generalized Persistence Algorithm](https://arxiv.org/abs/1904.03766v7), JACT 2022 | Indecomposable decomposition of graded presentation matrices; distinctly graded setting; bound O(N^(2 omega + 1)). | Full decomposition is not a generalized-rank query. |
| Dey-Jendrysiak-Kerber, [Decomposing Multiparameter Persistence Modules](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.41/LIPIcs.SoCG.2025.41.html), SoCG 2025 | Repeated-grade relations; Theorem 18 has O(N^(2 omega + 1) + N^(omega + 2) q^(k^2/4 + O(k))). Theorem 23 gives O(N^3) on interval-decomposables. | The paper explicitly notes polynomial general algebra algorithms and corrects earlier MeatAxe complexity interpretations. Its enumeration term is not a lower bound. |
| Dey-Xin, [Generalized Ranks via Unfolding](https://arxiv.org/html/2403.08110v4), September 2025 version | Arbitrary finite-poset simplicial filtration; unfold, find full zigzag intervals, impose fold-back conditions. O(t^(omega + 2)); top-dimensional case O(t^omega), graph H1 linear. | Best continuity with the user's work, but graph/top-dimensional cases are poor speedup targets. |
| Gyurik-Schmidhuber-King-Dunjko-Hayakawa, [Provable Quantum Speedups](https://arxiv.org/html/2410.21258v2), PRX Quantum 7, 020361, June 2026 | Weighted clique complexes, succinctly preparable initial harmonic, final Laplacian gap and overlap promise. Theorem 1: BQP1-hard and in BQP. | This tests harmonic overlap, not arbitrary exact class survival, generalized rank, or a barcode. Section IV explicitly discusses exponential deformation. |
| Lowe-Kim-Bondesan-Hayakawa, [Normalized Persistence](https://arxiv.org/html/2607.03278v1), July 2026 preprint | Theorem 8 proves DQC1-hardness for quasi-harmonic persistence. Lemma 7 places true beta-persistent / beta-initial estimation in BQP with uniform harmonic-mixture preparation and nonzero-overlap promises. | True normalized persistence hardness remains Conjecture 1. Section 7 identifies exact-kernel multiplicity and filtration-compatible encoding as missing ingredients. The quasi hardness uses even G1 = G2, with different spectral thresholds. |
| Hayakawa, [Unweighted Gapped Clique Homology](https://arxiv.org/html/2608.02726v1), August 2026 preprint | Clique multiplicity blow-up, symmetric-sector weighted Laplacian, asymmetric-sector exclusion; QMA1 hardness in a stated exact gate set. | Removing weights for a single complex is already studied. Section 8 expressly leaves filtered/harmonic-persistence extensions open. |
| Black-Maxwell, [Effective Resistance and Capacitance](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2021.31), ISAAC 2021 | Quantum null-homology test and torsion-sensitive resistance/capacitance bounds; exponential examples. | Important collision with the obstruction mechanism. |
| Filakovsky-Franek-Wagner-Zhechev, [Computing Simplicial Representatives](https://arxiv.org/abs/1706.00380), SODA 2018 / JACT | Degree-two mapping-cylinder/Mobius telescope gadgets create exponentially large integral representatives. | The telescope is not a new gadget. The exact native-zigzag two-projector specialization below is a local derivation, not a novelty claim. |

Primary full-text sections checked: AIDA Sections 3-6; Dey-Xin introduction, definitions and special-case statements; PRX Quantum Sections I.3-I.4, II.1, III, IV; normalized-persistence Sections 4.6-4.7, 6.2 and 7; unweighted paper Sections 4.2 and 8. A literature search without a collision does not establish priority.

## 2. Analytic theorem: constant-size unweighted simplicial zigzag

**Status: LOCAL DERIVATION, analytic proof below; fixture independently checked by exact rational arithmetic.** This concerns real/complex homology, not F2.

### Construction and inclusion model

Take a triangulated Mobius band M with disjoint embedded boundary and core circles A and C, both having six edges, with orientations satisfying

    [z_A] = 2 [z_C] in H1(M; R).

One explicit triangulation: triangulate the 3-by-2 rectangle grid, identify its vertical ends by (3,j) ~ (0,2-j), and subdivide each of the three middle-circle edges once, splitting its two incident triangles. This has 12 vertices, 30 edges, 18 triangles. The outer boundary has six edges and the subdivided middle circle has six edges.

For m bands, use distinct copies M_i, with the core of M_i identified simplicially with the boundary of M_(i+1), and no other identifications. Let C_i denote the intervening six-edge circles. The diagram is

    C_0 -> M_0 <- C_1 -> M_1 <- ... -> M_(m-1) <- C_m.

Every arrow is a literal simplicial inclusion between subcomplexes of the glued ambient complex. This is a zigzag with O(m) total simplices and 2m+1 poset vertices. It is not claimed simplex-wise in its displayed form. Each individual object is a fixed-size complex, so every local nonzero boundary/Laplacian gap has a positive constant lower bound independent of m.

In normalized harmonic H1 bases, the two maps into every band are multiplication by a and b, where

    a = 2b > 0,   a^2 = 41/86,   b^2 = 41/344.

The ratio follows topologically from [z_A] = 2[z_C] and equal circle lengths. The exact numerical squares are fixture-specific and are not needed for the asymptotic theorem.

**Flag-complex extension (analytic corollary, not separately executed):** apply barycentric subdivision functorially to every object. Every object becomes flag and each circle again has the same length as the other. The homology ratio remains two; the fixed constants a,b may change. Consequently the same proof applies to a family of unweighted clique complexes. This does not assert that the entire glued union is supplied as one clique complex.

### Kernels and overlap

Write x_i for the circle coordinates and y_i for the band coordinates. The limit constraints are

    y_i - a x_i = 0,   y_i - b x_(i+1) = 0.

The relation-matrix adjoint constraints for the colimit orthogonal complement are

    -k_(C_i) + a k_(M_i) = 0,
    -k_(C_(i+1)) + b k_(M_i) = 0.

Thus the two kernels L = ker D and K = ker B* are one-dimensional, with unnormalized generators

    L: x_i = 2^i,       y_i = a 2^i,
    K: k_(C_i) = 2^-i,  k_(M_i) = 2^-i / a.

All maps are nonzero between one-dimensional spaces, so the module is a full interval and its generalized rank is one. The inner product of these generators is 2m+1. Their squared norms are

    S_L = (4^(m+1) - 1 + a^2 (4^m - 1))/3,
    S_K = (1 - 4^(-m-1) + a^-2 (1 - 4^-m))/(1 - 1/4).

Consequently the unique nonzero singular value of P_K P_L is exactly

    gamma_m = (2m+1)/sqrt(S_L S_K) = Theta(m 2^-m).

The trace Tr(P_L P_K) is gamma_m^2, whereas generalized rank is one.

### Uniform constraint gaps

Order the two constraint rows band by band. The Gram matrices DD* and B*B are finite block-Toeplitz matrices with diagonal block diagonals 1+a^2 and 1+b^2. Their off-diagonal Fourier entries respectively have forms

    1 + ab exp(i theta),     ab + exp(i theta).

Both symbols have trace T = 2+a^2+b^2 and determinant

    a^2 + b^2 - 2ab cos(theta) >= (a-b)^2.

Their smallest eigenvalue is at least determinant / trace, hence at least (a-b)^2/T. Extending a finite vector by zero and integrating its Fourier quadratic form transfers this lower bound to each finite Gram matrix. Therefore

    sigma_min(D), sigma_min(B) >= (a-b)/sqrt(T) > 0.

The largest singular values are at most sqrt(T). Both normalized constraint gaps are therefore bounded below by a constant, yet gamma_m decays exponentially. The counterexample is stronger than assuming only constant local maps, bounded degree, path-shaped poset, bounded dimension, or constant local homology dimension: it satisfies all of them.

### What is and is not refuted

Refuted: obtaining polynomial conditioning of the raw module-level P_K P_L construction from local unweighted simplicial geometry plus the two constraint gaps alone.

Not refuted: every quantum generalized-rank algorithm; a global preconditioner with a new structural guarantee; or a finite-field method. This explicit family has rank one for an elementary reason and is classically easy. It therefore is not a quantum query lower bound. It also does not establish constant gaps for the separate augmented chain-level operators A and A^vee in QuantumTDA; those operators are not D and B.

## 3. Bounded executable result

Run `python3 check_mobius_zigzag.py` from this directory. It verifies chain identities, equal circle lengths, one-dimensional harmonic H1, the filling relation, the two harmonic coefficients, and the closed-form overlap against direct vectors. No hardware or quantum circuit is simulated.

Exact rational fixture: a^2=41/86, b^2=41/344; rank(d2)=rank([d2 | z_A-2z_C])=18. Numerical local H1 Laplacian gap: 0.3526054033. The analytic uniform D/B singular-gap lower bound is approximately 0.21427238.

| Bands m | D gap | B gap | Quotient cosine |
|---:|---:|---:|---:|
| 4 | 0.294158 | 0.314793 | 0.227063 |
| 8 | 0.242485 | 0.246327 | 0.0267493 |
| 16 | 0.223780 | 0.224354 | 0.000202831 |
| 32 | 0.218238 | 0.218315 | 6.09612e-9 |

Finite numerical agreement supports implementation only. The infinite-family statement is supported by the analytic proof, not extrapolation from this table.

## 4. Two precise next candidates, with honest viability gates

### Candidate A: exact low-rank updates for AIDA extension splitting

**Closest positive mechanism to the user's decomposition work; NOT YET a viable speedup claim.** Work over F_q with an explicit minimal presentation. AIDA stores Hom information, and its repeated-grade/extension routines search subspaces of a k- or kappa-dimensional interface. The proposed change is a quantum walk over fixed-dimensional subspaces, maintaining the exact split-test certificate as one dimension is exchanged.

**Minimum new lemma:** for an ExtensionDecomp instance after the published preprocessing, construct a faithful split predicate and data structure such that adjacent Grassmann vertices induce a provably low-rank update of its consistency matrix. Give worst-case reversible update cost U, setup S, exact check C, space, and a method to recover actual admissible basis changes from a marked vertex. It must handle pivot failures without silently re-solving the full system.

Only after that lemma could a quantum walk use a bound of the form S + epsilon^-1/2 (delta^-1/2 U + C), where epsilon is marked fraction and delta the chosen walk's spectral gap. These are named parameters, not a promised speedup. Search state indexing and failure accumulation must be costed.

**Immediate falsification:** write the actual BlockReduce(**) coefficient matrix after substituting cached Hom^alpha bases; exchange a candidate subspace basis vector; determine the rank of the matrix difference. If the change is not low rank in the relevant representation, or validity requires globally changing all old blocks, stop this mechanism.

**Classical veto:** compare against Gray-code/low-rank-update enumeration and polynomial finite-dimensional-algebra decomposition after exact representation conversion. A second bounded lemma worth testing first is whether the split can be encoded in an alpha-local endomorphism algebra whose idempotents lift to admissible presentation decompositions. If that yields an efficient classical solution, discard the supposed quantum search advantage. An exp(kappa^2) AIDA branch is not classical hardness.

### Candidate B: functorial unweighting of harmonic persistence

**A more concrete quantum theorem target, but less directly tied to full decomposition.** Start from the June 2026 weighted harmonic-persistence hard family and the August 2026 clique-blow-up mechanism. Use a single common multiplicity assignment across the two filtration levels.

**Minimum theorem:** construct in polynomial time unweighted clique inclusions X'_1 -> X'_2 and an efficiently preparable lifted guide, with compatible symmetric-sector isometries at both levels, no extra zero modes outside the symmetric sectors, inverse-polynomial final gap, and preservation of the YES/NO harmonic-overlap promise. This would transfer the existing weighted hardness/containment theorem to an unweighted filtered setting. Novelty would be the functorial filtered construction and its gap/guide analysis, not phase estimation or unweighting one complex.

**First analytic check:** identical multiplicities make the one-copy-per-block isometries commute with inclusion on the symmetric subspace. However, this observation alone does not prove the asymmetric-sector bound simultaneously for both levels, guide encoding, or polynomial size under the needed scale hierarchy. Those are the next obstacles. The August paper itself identifies filtered extensions as open; its proof cannot simply be cited as already providing this result.

**More ambitious extension, not recommended first:** true normalized persistence requires exact kernel multiplicities and filtration-compatible embeddings, as isolated in Conjecture 2 of the July paper. Approximate low-energy simulation does not suffice. This is a substantive open ingredient, but a larger proof commitment than the two-level guide-preserving unweighting lemma.

## 5. Preferred decision

**Follow-up correction:** [UNWEIGHTING_FIRST_LEMMA.md](UNWEIGHTING_FIRST_LEMMA.md) proves the common-multiplicity transfer conditional on the August source theorems. Its asymmetric-sector bound already holds for arbitrary base clique complexes, and the June hard family's guide remains succinct after blow-up. Thus Candidate B may be a direct corollary, rather than a strong new theorem. The initial positive preference below is superseded by that novelty downgrade.

If remaining close to Dey-Xin / Dey-Jendrysiak-Kerber is mandatory, do the Candidate A consistency-matrix/update probe first and do not launch a quantum implementation. No positive theorem has survived enough checks to recommend committing a project yet.

If the objective permits a new quantum TDA complexity result rather than generalized-rank decomposition specifically, Candidate B is the sharper positive target. Its novelty boundary is explicit and its first functoriality check is tangible. The raw generalized-rank projector route under merely local gap promises is now a concrete NO-GO.
