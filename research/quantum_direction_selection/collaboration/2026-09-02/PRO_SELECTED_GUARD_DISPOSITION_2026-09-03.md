# Selected-cycle guard review — independent disposition

September 3, 2026. **CONDITIONAL GUARD LEMMA ACCEPTED AFTER LOCAL RECHECK.** [The complete external response](PRO_SELECTED_GUARD_REVIEW_2026-09-03.md) is preserved separately with all 124 displayed equation sources. This disposition concerns only the explicit alternative graph at source commit 9f2e0880db89fb570b439156e6926b664828dcee. It does not certify the source's different guard graph, the remaining active atoms, priority, complexity hardness, or the complete reduction.

## 1. Verdict

No mathematical counterexample was found under the written finite assumptions. The response identifies three exposition corrections, all accepted:

1. The equality ker D_Z,0 = V' direct-sum Q' is at the new target degree D. It is not an assertion about the kernel of a single ungraded differential over every chain degree.
2. The all-bidegree argument uses the augmented reduced Laplacian of the selected four-cycle in degrees -1, 0, and 1. Its only reduced harmonic degree is 1.
3. The output projection is the old private output projection tensored with the degree-one harmonic projection P_gamma, extended by zero in every other guard degree.

These changes do not alter the construction or the finite checks.

## 2. Independent checks

| Step | Local check | Disposition |
| --- | --- | --- |
| Clique union | A clique with an old private vertex can use only the selected guard petal; a clique without one lies in the full joined register. Inducedness of R and S_beta gives the claimed intersection. | Accepted |
| Relative chains | Modulo R'=R*B, every surviving simplex uniquely factors into an old relative simplex and a simplex of S_beta. The signed boundary is the reduced join tensor differential. | Accepted in every degree |
| Boundary intersection | Relative Kunneth leaves H_(d+1)(Y,R) tensor H_1(S_beta) at total degree D+1. Naturality of the connecting map sends [c] tensor [gamma] to [partial c] tensor [gamma]. Its image is the old exact boundary intersection tensored with the selected line. | Accepted; no assumption that all old homology comes from R |
| Zero-weight split | Any boundary entry that deletes an old private vertex carries lambda and vanishes at zero. Register and private chain blocks, including their adjoints, split. | Accepted |
| Target kernel | At total degree D=d+2, guard degrees 1,0,-1 pair with old degrees d,d+1,d+2. Only degree 1 is harmonic. The s=0,-1 augmented gaps remove possible higher-degree old private harmonics. | Accepted |
| Projected pair | Extend P_gamma by zero outside guard degree 1. Active terms give T_Y tensor P_gamma. Outside boundary/coboundary terms vanish because gamma is closed and orthogonal to im partial_S^*. | Accepted on the entire target domain |
| Logical annihilation | A top register cycle factors as v tensor z with v in V and z in Z_1(B). Apply T_Y,1 v=0 after projecting/restricting z to the selected harmonic line. | Accepted |
| Bulk lower bound | On Q'=Q tensor gamma, the normalized join isometry gives exactly the old T_Y,1 norm. | Accepted |
| Interface | Only a simplex with exactly one old private vertex can map into the full register. For each private vertex deletion is a signed partial isometry; their input blocks are disjoint. Thus LL* is at most N_priv lambda^2 I. | Accepted; no growth under guard iteration |
| Basis cone | The relative connecting image is the selected petal. Its target private zero-weight pair is the shifted augmented degree-zero pair of a connected cycle, so Q=0. | Accepted; independently rank-certified |
| Iteration | No guard step adds private vertices. Repeated construction tensors Q and the projector with selected harmonic lines. Finite locality at most six gives a finite constant family and the safe exponent at most 26. | Accepted |

The source-graph computation adds useful independent evidence rather than proving the abstract argument: 46,998 boundary identities cover all actual degrees, projected T0 vanishes on the full target domain, and the normalized bulk map equals the old 176-dimensional map. The raw-coordinate energy 2 is an explicit warning that all central coordinates cannot replace Q tensor gamma.

## 3. Scope consequence

Computational-basis guard closure is now proved locally for this selected-cycle construction, conditional on a base active gadget satisfying the finite criterion. Basis projectors have an elementary cone base case. Together with the previously checked graph relabelings, this closes guards for the four three-term Hadamard atoms.

This remains a structural lemma built from relative tensor products and harmonic padding. Its proof may be standard once the construction is stated; no novelty credit is assigned. No new primary literature was checked while collecting or disposing this response.

The exact finite palette is still incomplete. The next gate is one nontrivial base atom: either the one-qubit difference state or a two-qubit two-term state. Once those base atoms satisfy the finite criterion, this lemma supplies every fixed computational-basis guard needed through locality six.
