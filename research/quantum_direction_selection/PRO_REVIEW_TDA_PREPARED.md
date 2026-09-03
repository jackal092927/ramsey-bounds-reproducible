# Prepared Pro discussion: functorial unweighting and new TDA theorem mechanisms

Status: SENT after explicit user confirmation, September 2 PDT. The metadata line was not included in the transmitted payload. See PRO_DISPATCH_2026-09-02.md for the verified working-state receipt; no completed response has been collected.

## Request

This is a focused problem distinct from a separate ongoing broad brainstorm on a single generalized-rank/zigzag interval query. Here prioritize Candidate B below: audit the functorial unweighting transfer, determine whether it is merely a corollary, and seek a genuinely nontrivial extension. The decomposition and projector examples are background that rules out repeated dead ends, not a request to restart that broad brainstorm.

Act as an adversarial mathematical collaborator. We need to choose a concrete quantum TDA theorem, preferably extending Cheng Xin and Tamal Dey's generalized persistence work and Dey–Jendrysiak–Kerber's subsequent decomposition algorithm. Do not optimize presentation or engineering. First find mathematical errors, missing assumptions, and classical algorithms that destroy the proposed advantage. Then try to prove the smallest genuinely useful positive lemma.

We have not established a new quantum speedup. Distinguish a conjecture, an elementary local lemma, an existing theorem, and a publishable new result. Do not claim a full barcode/decomposition algorithm from a harmonic-overlap estimator.

## Sources and exact distinctions

- Dey–Xin, Generalized Persistence Algorithm, JACT 2022: https://arxiv.org/abs/1904.03766v7 . Indecomposable decomposition of graded presentations, not merely a generalized-rank query.
- Dey–Jendrysiak–Kerber, Decomposing Multiparameter Persistence Modules, SoCG 2025: https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.41/LIPIcs.SoCG.2025.41.html . Repeated grades, cached Hom information and extension splitting. The enumeration term in one algorithm is not a classical lower bound; the paper discusses polynomial finite-dimensional-algebra methods.
- Dey–Xin, Generalized Ranks via Unfolding: https://arxiv.org/html/2403.08110v4 . UNREVIEWED PREPRINT, correctness unverified per the author's explicit warning. It claims unfolding/fold-back and a linear-time graph H1 case. Independently check any theorem before relying on it; our direct projector/corollary arguments do not require this preprint.
- Gyurik et al., Provable quantum speedups for computing persistence in topological data analysis, PRX Quantum 2026: https://arxiv.org/html/2410.21258v2 . Weighted, guided harmonic persistence, with preparation and gap promises; not full generalized rank.
- Lowe et al., normalized persistence, July 2026: https://arxiv.org/html/2607.03278v1 . Quasi-harmonic hardness and true normalized persistence must be separated. The latter hardness is conjectural in this version.
- Hayakawa, Unweighted Gapped Clique Homology, August 2026: https://arxiv.org/html/2608.02726v1 . Single-complex clique blow-up. Section 8 identifies filtered extensions as a further question.
- Finite-field matrix-vector query lower bounds: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2021.55 . Do not introduce a free exact quantum rank oracle.
- Known topological telescope background: https://arxiv.org/abs/1706.00380 and https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2021.31 . Our use of a Möbius telescope is not claimed as a new gadget.

## Routes already explored: do not repeat these as fresh ideas

1. For a connected diagram of finite-dimensional real inner-product spaces, let U be their direct sum. For every arrow u -> v with map A, define a limit constraint x_v-Ax_u and a colimit relation -J_u y+J_v Ay. Write L=ker D and K=ker B*. The generalized rank is rank(P_K P_L), not Tr(P_L P_K). The trace sums squared cosines and can be arbitrarily smaller than the rank.
2. A chain with scalar maps 1/2 has rank one and good local gaps, but exponentially small overlap. Rescaling bases is not free: it moves the conditioning problem into coordinates/preparation.
3. An augmented chain-level expression removes explicit homology bases, but its operator norms, filling costs, and nonzero singular gaps are not controlled merely by local Laplacian gaps.
4. Grover over AIDA's subspaces is not by itself a novelty or advantage argument. Classical incremental enumeration and algebra decomposition are compulsory baselines.

## New native topological obstruction: inspect the proof

Use a fixed triangulated Möbius band M with disjoint boundary A and core C, each a six-edge circle. It has 12 vertices, 30 edges and 18 triangles. Over R, [z_A]=2[z_C]. In normalized harmonic H1 bases, the inclusion coefficients are a=2b>0, with exact fixture values a^2=41/86 and b^2=41/344.

Glue m copies along core/boundary circles to obtain the actual simplicial-inclusion zigzag

    C_0 -> M_0 <- C_1 -> M_1 <- ... -> M_(m-1) <- C_m.

Every homology space is one-dimensional. Limit constraints are y_i-a x_i=0 and y_i-b x_(i+1)=0. Colimit-adjoint constraints are -k_Ci+a k_Mi=0 and -k_C(i+1)+b k_Mi=0.

Kernel generators are

    L: x_i=2^i, y_i=a 2^i;
    K: k_Ci=2^-i, k_Mi=2^-i/a.

Their inner product is 2m+1. Their squared norms are

    S_L=(4^(m+1)-1+a^2(4^m-1))/3,
    S_K=(1-4^(-m-1)+a^-2(1-4^-m))/(1-1/4).

Thus the unique nonzero singular value of P_K P_L is (2m+1)/sqrt(S_L S_K)=Theta(m 2^-m), while generalized rank remains one. The two constraint Gram symbols have trace T=2+a^2+b^2 and determinant a^2+b^2-2ab cos(theta). Hence both nonzero constraint gaps are at least (a-b)/sqrt(T)>0, uniformly in m. Zero-extension and Fourier integration transfer this bound to finite block-Toeplitz sections.

Exact rational checks verify the fixed complex and filling relation. Numeric checks through m=32 agree; the overlap there is approximately 6.09612e-9. These are mathematical sanity checks, not quantum-device or circuit simulations. Functorial barycentric subdivision should give a flag-complex version. This refutes one raw-projector gap inference, not all quantum generalized-rank algorithms or a complexity lower bound.

## Candidate A: stay closest to AIDA

Work over a specified finite field with the explicit minimal presentation and published Hom preprocessing. Try to prove that exchanging one direction of a candidate splitting subspace yields a cheap exact reversible update of the actual ExtensionDecomp/BlockReduce consistency system. The equations include

    Q_c M_c + M_b P_c = 0,
    N_b + sum_c Q_c N_c + M_b U = 0.

Determine the rank of the change after vectorization and after cached-Hom substitution. A rank-one change of an input block may induce rank proportional to another dimension via a Kronecker product, so do not assume rank one. Give setup, worst-case update, check, reconstruction, field and storage costs. A quantum-walk expression S+epsilon^(-1/2)(delta^(-1/2)U+C) is only useful after proving these quantities and beating the best classical algorithm. Can an alpha-local endomorphism algebra eliminate the search classically?

Update from an exact local check: the changed cached-Hom columns are vec(Q_i N_c T), so for T'=T+u e_j^T their update rank is rank[Q_i N_c u]_i, or the quotient evaluation rank after old relations are removed. This rank is unbounded even for an indecomposable target. For arbitrary t, take t+1 generators at incomparable bidegrees (i,t+2-i), one all-ones relation at (t+2,t+2), a free block born at (t+3,t+3), and two new columns at (t+4,t+4) with N_b=(e1,0), N_c=(0,1). Exchange T=e1 for e1+e2. The old target has only scalar endomorphisms, its relevant fibre dimension is t, and Hom from the later free block evaluates surjectively. Thus the reduced update rank is t while the right-hand side is unchanged. Inspect this counterexample; do not propose the same unsupported constant-rank update again.

## Candidate B: a more focused quantum complexity target

Can one make the weighted harmonic-persistence hard family unweighted by using one common vertex-multiplicity assignment across both filtration levels?

For each vertex v choose an integer f_v and replace v by a clique of f_v copies. In the normalized simplex basis, map sigma to the normalized average of one-copy-per-block lifts. If shared vertices use identical multiplicities, this appears to commute exactly with simplex inclusion. The symmetric-sector weighted incidence coefficient is sqrt(f_v). For f_v=M w(v)^2, Laplacians should scale by M.

Follow-up now gives the full conditional transfer: the source's Theorem 4.3 already applies to arbitrary base clique complexes. Therefore P_hat=U P U* with no extra kernels, nonzero gap at least min(M gamma,min f), and all harmonic maps are unitarily equivalent. Common-weight inclusion has no factor; boundary/coboundary have sqrt(M), and Laplacians M. This preserves guided overlap and generalized ranks, not normalization by total simplex count.

The June source's actual guide is entirely on weight-one register vertices; gadget weights are lambda. Choose sufficiently small dyadic lambda=2^-L and M=2^(2L). Register blocks have M copies and gadget blocks one. Each guide p-simplex has exactly M^(p+1) lifts, so the state remains a uniform subset state with compact product-copy description. The source hard family's NO overlap is exactly zero, avoiding the general issue that exp(-n) is not exp(-N) after graph-size blow-up. Its promise only requires the final-level gap. Do not import the August paper's different QMA gate-set convention; only its graph-theoretic lemmas are used.

A seven-vertex path-to-triangle check has zero inclusion residuals and operator residuals below 8e-16. The tiny counterexample of one vertex with one copy at the first level and two at the second shows that common multiplicities really are essential. Root and a second independent agent checked the argument.

Our current assessment is that the special two-weight hardness transfer may be a SHORT DIRECT COROLLARY, not a new deep mechanism. Verify the precise imported gap hypotheses and dyadic parameter substitution, challenge this conclusion, and identify whether any substantive additional theorem remains. Do not manufacture a missing lemma or inflate a corollary's novelty.

Independent audit caveat to check explicitly: the June guide's positive amplitudes are specified relative to its source simplex orientations. Lift those orientations consistently. If the target instead fixes globally sorted vertex orientations, coherent preparation may need efficiently computable signs, so the guide is not automatically a strictly positive subset state in that different basis. The spectral identities are basis-invariant but the input promise must not silently change. The intended complexity conclusion, if verified, is BQP1-hard and in BQP, not automatically BQP-complete.

## Desired response

1. Strongest error or collision first, with exact source/theorem if available.
2. Audit the Möbius obstruction and common-multiplicity commutation lemma independently.
3. Choose at most one candidate whose next nontrivial lemma is worth attempting. Explain whether it is an algorithm, complexity classification, or merely a structural obstruction.
4. Attempt that lemma in detail. If it fails, give the smallest counterexample or specific missing hypothesis.
5. State what quantum advantage, if any, follows and against which classical input/access model. UNKNOWN is better than an invented separation.
