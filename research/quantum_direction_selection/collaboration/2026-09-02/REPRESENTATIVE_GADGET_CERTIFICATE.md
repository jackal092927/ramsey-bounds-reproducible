# Exact certificate for one Rudolph three-term gadget

2026-09-03. **ONE SOURCE GRAPH CERTIFIED; COMPLETE PALETTE OPEN.** The integer calculations below establish the finite inputs of [the zero-weight concentration theorem](FINITE_CERTIFICATE_CONCENTRATION.md) for one actual active gadget. They do not certify all guarded products or the full circuit reduction.

## Provenance and reproduction boundary

The primary code is [Dorian Rudolph, QMA1-gateset-paper, gadget_homology.py](https://github.com/DorianRudolph/QMA1-gateset-paper/blob/30ac70e5dacdecce97c38d801c128ec3ed93a96a/gadget_homology.py), immutable commit
\[
\texttt{30ac70e5dacdecce97c38d801c128ec3ed93a96a}.
\]
The fetched file SHA-256 is
\[
\texttt{c8918f9e037ae79796bb65640170c8e60f31883625d24348f3476f7644dcd29a}.
\]
The upstream license is GPLv2-or-later; its graph construction and original algebraic checks are credited to that source.

[Our checker](certify_representative_bulk.py) fetches the pinned source, checks its hash, and evaluates only the inspected graph-building definitions make_graph, thicken, fill_cycle, join_keep_names, and state_00m10m11. A simple undirected Graph shim implements the called operations. It captures the finished graph at the first clique_complex call, before Sage homology, plotting, or top-level upstream routines execute. Sage was not run. The upstream program is not copied into this repository.

Graph construction itself therefore remains tied to this explicit replay rather than an independent run of Sage. The replayed operations have been compared with the inspected source: sorted undirected edges, thickened layers, specified attaching-map merges, and central coning. After capture, clique enumeration, oriented boundaries, ranks and fillings are independently computed. The complete graph and certificate data are in [RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json](RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json).

Reproduce with Python, NumPy and a configured GitHub CLI:

    python research/quantum_direction_selection/collaboration/2026-09-02/certify_representative_bulk.py

The output certificate includes the graph, orientation/order conventions, prime, integer filling chain, and matrix hash. It does not require trusting a floating-point eigenvalue threshold.

## 1. Exact topology and intended logical projector

The source function encodes
\[
\phi=|00\rangle-|10\rangle-|11\rangle.
\]
Its sign is opposite to the requested representative a=|10>+|11>-|00>, hence the same rank-one projector. Four register cycles are tensor joins of oriented four-edge bowtie petals. They have disjoint edge-simplex support and norm 4; division by 4 gives the explicit isometric logical basis.

| Quantity | Exact result |
| --- | --- |
| Vertices / edges | 41 / 322 |
| Numbers of simplices, degrees 0 through 5 | 41, 322, 914, 1082, 477, 30 |
| Boundary ranks, degrees 1 through 5 | 40, 282, 632, 447, 30 |
| Ordinary rational Betti numbers, degrees 0 through 5 | 1, 0, 0, 3, 0, 0 |
| Target degree | 3 |
| Nonzero terms in an integer filling of phi | 382 |
| Filling denominator | 1 |

The boundary compositions are checked as exact integer zero matrices. Gaussian elimination modulo p=1,000,003 supplies lower bounds on rational ranks. Adjacent chain dimensions and these adjacent lower bounds supply upper bounds:
\[
\operatorname{rank}_{\mathbb Q}\partial_k
\le\min\{n_{k-1}-\operatorname{rank}_{\mathbb F_p}\partial_{k-1},
         n_k-\operatorname{rank}_{\mathbb F_p}\partial_{k+1}\}.
\]
Every recorded lower and upper bound agrees. This proves the ranks over Q; modular rank alone would not give equality.

An integer chain c in C_4, with all 382 nonzero coefficients archived, satisfies
\[
\partial_4 c=\phi
\]
by an exact integer multiplication. The register cycles
\[
|00\rangle+|11\rangle,\quad |10\rangle-|11\rangle,\quad |01\rangle
\]
increase the boundary rank by three modulo p. Since the boundary rank over Q has already been certified, their cosets are independent over Q as well. Thus
\[
B_3(Y)\cap V=\operatorname{span}\{\phi\},\qquad \beta_3(Y)=3.
\]
This conclusion is reproduced from the finite graph. The source already proves the intended topology algebraically; this is verification and a reusable certificate, not a new homology gadget.

For lambda>0, the invertible diagonal weight gauge preserves homology and fixes the weight-one register coordinates, so the boundary intersection is unchanged.

## 2. Central relative bulk

The central vertex v0 has only new neighbors. Its link has simplex counts 26, 114, 176, 88 in degrees 0,1,2,3. Central degree-3 chains correspond to link degree-2 chains. After retaining central output simplices, the local boundary/coboundary pair on this bulk is lambda times
\[
A=\begin{bmatrix}\partial^{link}_2\\(\partial^{link}_3)^*\end{bmatrix}
\]
up to orientation signs.

For the 176-by-176 integer Gram matrix G=A^*A:
\[
\det(G)\equiv797443\ne0\pmod{1000003},\qquad
\|G\|_\infty=14.
\]
Thus G is positive definite over R. Since its determinant is a positive integer and every eigenvalue is at most 14,
\[
\lambda_{\min}(G)\ge14^{-175}.
\]
The archive records the deliberately conservative rational bound
\[
\sigma_{\min}(A)\ge14^{-176}.
\]
Therefore the weighted projected pair is injective with singular value at least lambda times that fixed constant. Padding this pair with outside harmonics preserves this bound; padding with all outside coordinates does not establish the required O(lambda) estimate.

## 3. Zero-weight kernel and elementary positive-gap floor

Set all 14 register vertex weights to one and all 27 new weights to zero. At target degree 3, write the differential pair as D(lambda)=D_0+lambda D_1.

Exact integer checks show:

- D_0 annihilates all four register cycles and all 176 central bulk coordinates.
- These subspaces are independent; the register basis Gram matrix is 16I.
- D_0 has rank 902 modulo p. The explicit 180-dimensional kernel gives the matching rational upper bound 1082-180=902.
- The projected central pair has zero constant term and its lambda coefficient annihilates the register cycles.

Consequently
\[
\ker D_0=V\oplus Q,\qquad \dim V=4,\quad \dim Q=176.
\]
No additional zero-weight sectors are hidden in the full target chain space.

The integer Gram norm bounds are
\[
\|D_0^*D_0\|_\infty=12,\quad
\|D_1^*D_1\|_\infty=15,\quad
\|\Delta_3(1)\|_\infty=21.
\]
The first Gram has rank 902, so its least positive eigenvalue is at least 12^-901. The unweighted Laplacian has rank 1082-3=1079, so its least positive eigenvalue is at least 21^-1078. Section 2 of the concentration theorem's weight-scaling argument then gives
\[
\gamma_+(\Delta_3(\lambda))\ge21^{-1078}\lambda^{10},
\qquad 0<\lambda\le1.
\]
This proves a finite positive-gap lower bound adequate for the new route. It does not prove that lambda^10 is the optimal asymptotic order or compute its leading coefficient. The new proof does not need either fact.

## 4. A genuine correction exposed by the graph

The graph has 30 degree-5 simplices, although its logical target is degree 3. The earlier padding note asserted that only bidegrees (2m-1,q) and (2m,q-1) occur. That enumeration is false for this representative.

The repair is to quantify over every actual bidegree. The outside register has harmonics only in top degree q; consequently the only outside-harmonic summand at the target total degree is (2m-1,q). Every other summand, however high the local dimension, has a positive outside gap. The repaired argument supports the same intended conclusion. This is a mathematical correction to the local exposition, not a counterexample to the repaired padding theorem.

The mutable round-2 note is corrected and cross-linked. The previously transmitted PRO_CONTEXT_PACKET.md remains frozen, so the follow-up explicitly tells Pro about the change.

## 5. Remaining gates

This graph passes the exact topology, zero-weight kernel and projected-bulk injectivity requirements of the new conditional theorem. Still open:

- the other active atom types and their allowed signed/relabeling symmetries;
- a proof of closure under joins of the implementing spheres and attaching maps with computational-basis guards, or finite certificates for every required guarded graph through locality six;
- a complete literature comparison for the all-chain theorem and improved gap dependence;
- a meaningful exact circuit-source complexity consequence beyond the conditional D=1, perfect-completeness specialization.

The certificate and the abstract proof must survive independent review before stronger claims are promoted. No full reduction, unrestricted SDQC1 equivalence, or paper-readiness conclusion is recorded.

