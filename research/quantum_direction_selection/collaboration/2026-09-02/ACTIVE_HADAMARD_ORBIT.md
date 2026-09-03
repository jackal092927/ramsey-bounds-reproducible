# One certified gadget covers all four active Hadamard atoms

September 3, 2026. **LOCAL PROOF WITH EXACT CHAIN-MAP CHECKS.** This reduces the remaining finite-family work; it does not certify the guarded attaching-sphere products or the other atom types.

## 1. The four states

Use basis order 00,01,10,11, with clock qubit c first and work qubit w second. The normalized active vectors are
\[
\begin{aligned}
d_0&=(|00\rangle-|10\rangle-|11\rangle)/\sqrt3,\\
d_1&=(|01\rangle-|10\rangle+|11\rangle)/\sqrt3,\\
u_0&=(|00\rangle+|01\rangle-|10\rangle)/\sqrt3,\\
u_1&=(|00\rangle-|01\rangle-|11\rangle)/\sqrt3.
\end{aligned}
\]
The [existing actual source certificate](REPRESENTATIVE_GADGET_CERTIFICATE.md) covers d_0. Exactly,
\[
d_1=-Z_cZ_wX_wd_0,\qquad
u_0=-X_cd_0,\qquad
u_1=X_cZ_cZ_wX_wd_0.
\tag{1}
\]
Operators act from right to left. Global signs do not affect rank-one projectors.

Here X and Z denote actions on the encoded cycle basis. This is a graph relabeling argument for the constraint palette, not an extension of the verifier's allowed gate set.

## 2. Realize the actions by register relabeling

Each register qubit is the seven-vertex bowtie of two four-edge cycles, with oriented petals
\[
(xx,a3,a2,a4,xx),\qquad(xx,b3,b2,b4,xx).
\]
The cycles have disjoint edge support.

- Swapping a2 with b2, a3 with b3, and a4 with b4 exchanges the two oriented cycles. Its logical action is X.
- Swapping b3 with b4 reverses the orientation of the second cycle while fixing the first. Its logical action is Z.

Both permutations preserve the register graph and all register weights. Extend each permutation to the entire active gadget by fixing every private vertex, including its central vertex. Let Y' be the graph obtained by relabeling every edge of Y with that permutation. It is a weighted graph isomorphic to Y, with the same canonically labeled register subgraph.

The induced maps S_k on oriented chain coordinates are signed permutation isometries and satisfy
\[
\partial'_k(\lambda)S_k=S_{k-1}\partial_k(\lambda)
\quad\text{for every }\lambda\ge0.
\tag{2}
\]
Consequently the Laplacians are unitarily conjugate. The zero-weight differential pair, its kernel, and the central private input/output subspaces are transported exactly. In particular, if Y satisfies the finite criterion for Pi, then Y' satisfies it for U Pi U*, with the same constants.

This transports:

1. the exact register boundary intersection and target Betti number;
2. ker D_0=V direct-sum Q;
3. T=lambda T_1, annihilation on V and injectivity on Q;
4. the entire positive-weight spectrum and the sufficient gap floor.

Outside harmonic padding tensors (2) with the identity on the outside harmonic space, preserving these conclusions. Constructing an active computational-basis guard by joining implementing spheres is a different operation and is not covered by this relabeling proof.

## 3. Exact finite evidence

[check_active_hadamard_orbit.py](check_active_hadamard_orbit.py) uses the already archived graph and integer filling. It makes no network call and pins the input certificate SHA-256 to
\[
\texttt{916819fb8a9e371b322a1fab1161b1fc2686ad7fdaf9cf785f52fc2fcb0cae3a}.
\]

For all four cases it verifies:

- a bijective image of every clique in every actual degree, including degrees above the logical target;
- preservation of the register graph and fixation of every private vertex;
- the signed action on the four encoded register cycles, whose Gram matrix is 16I;
- each identity in (1) over integers;
- an explicitly transported 382-term integer filling satisfying the target boundary equation.

The complete permutations, logical matrices, phases and graph hashes are recorded in [ACTIVE_HADAMARD_ORBIT_CERTIFICATE.json](ACTIVE_HADAMARD_ORBIT_CERTIFICATE.json). All four cases pass. Ranks and bulk singular bounds do not need to be recomputed for isomorphic graphs; equation (2) transports them. This is an exact reduction to the original certificate, not four independent source-graph reconstructions.

Reproduce with Python and NumPy:

    PYTHONDONTWRITEBYTECODE=1 python research/quantum_direction_selection/collaboration/2026-09-02/check_active_hadamard_orbit.py

## 4. Consequence and boundary

The unguarded three-term portion of the split-Hadamard palette requires only the original representative certificate plus these explicit register symmetries. This is a standard chain-isometry consequence and a useful reduction of finite verification work, not a new gadget construction or the main novelty claim.

Still open: the basis and one-/two-term active atoms under the new finite criterion, and computational-basis guard closure or finite certificates for the guarded attaching-sphere family through locality six. The general concentration theorem remains conditional on that completed family and independent proof review.

