# Exact finite certificates for the remaining active atoms

September 3, 2026. **SOURCE-PINNED INTEGER CERTIFICATES PASS; PALETTE INTEGRATION LOCALLY COMPLETE FOR THE EXPLICIT REAL-GATE SOURCE.** This note covers the one-qubit difference and both two-qubit two-term states left open after the Hadamard-orbit and selected-cycle guard results. It does not establish source priority, an unrestricted complexity-class equivalence, or end-to-end paper correctness.

## 1. Source and execution boundary

The primary code is Dorian Rudolph's **gadget_homology.py** at immutable commit
\[
\texttt{30ac70e5dacdecce97c38d801c128ec3ed93a96a},
\]
with pinned SHA-256
\[
\texttt{c8918f9e037ae79796bb65640170c8e60f31883625d24348f3476f7644dcd29a}.
\]
Its repository license is GPLv2-or-later. The upstream code is not copied here.

[certify_remaining_active_atoms.py](certify_remaining_active_atoms.py) fetches the pinned file in default mode, asserts its hash, evaluates only **make_graph**, **thicken**, **fill_cycle**, **join_keep_names**, and the three requested state functions, and captures each graph at its first **clique_complex** call. Capture happens before Sage homology, plotting, or later top-level calculations. All subsequent clique enumeration, oriented boundaries, modular ranks, rational reconstruction, filling equations, zero-weight pairs, and graph isomorphisms are computed independently with Python and NumPy.

The full graph data and filling chains are in [REMAINING_ACTIVE_ATOM_CERTIFICATES.json](REMAINING_ACTIVE_ATOM_CERTIFICATES.json), SHA-256
\[
\texttt{82c0ece72ef13c65dc882195feec5ea9f09610e3b0a524e4ddb48c498ae8b077}.
\]
An offline mode reconstructs all three graphs from that archive, recomputes every atom section, and checks exact equality. It passed with every external-command call replaced by an exception; [the small offline receipt](OFFLINE_REMAINING_ACTIVE_ATOM_CHECKS.json) records this. Offline mode verifies the supplied graphs and mathematics, not upstream provenance.

## 2. One-qubit difference

The source function **state_0m1** implements
\[
\phi_- = |0\rangle-|1\rangle.
\]
The recovered graph has 16 vertices and clique counts
\[
(16,40,24)
\]
in degrees 0,1,2. Exact boundary ranks over \(\mathbb Q\) are
\[
\operatorname{rank}\partial_1=15,\qquad
\operatorname{rank}\partial_2=24,
\]
certified by matching lower bounds modulo \(1000003\) and rational upper bounds. Thus the ordinary Betti numbers are \((1,1,0)\). A 24-term integer two-chain, with denominator one, has boundary exactly the difference of the two oriented bowtie petals. The complementary register cycle \(|0\rangle+|1\rangle\) is independent modulo boundaries. Hence
\[
B_1(Y)\cap Z_1(R)=\mathbb C\phi_-.
\]

At zero private-vertex weight, the target differential pair has rank 30 on a 40-dimensional target space. The two register cycles and eight central edges are exact kernel vectors, so matching dimensions prove
\[
\ker D_0^{(1)}=V\oplus Q,\qquad \dim V=2,\quad\dim Q=8.
\]
The projected central pair has zero constant term and annihilates both register cycles at first order. Its \(8\times8\) integer Gram determinant is nonzero modulo \(1000003\), with determinant residue 512 and infinity norm 8. This proves injectivity on Q and supplies an explicit rational singular-value floor. The safe weighted whole-gap exponent is \(2(1)+4=6\).

## 3. Two-qubit two-term state

The source function **state_00m11** implements
\[
\phi_{00,11}=|00\rangle-|11\rangle.
\]
Its graph has 33 vertices and clique counts
\[
(33,241,646,712,272)
\]
in degrees 0 through 4. Exact boundary ranks are
\[
32,\ 209,\ 437,\ 272.
\]
The ordinary Betti numbers are
\[
(1,0,0,3,0).
\]
A denominator-one 248-term integer four-chain fills \(\phi_{00,11}\). The three logical complement cycles
\[
|00\rangle+|11\rangle,\qquad |01\rangle,\qquad |10\rangle
\]
remain independent modulo boundaries. Therefore
\[
B_3(Y)\cap Z_3(R)=\mathbb C\phi_{00,11}.
\]

The zero-weight degree-three pair has rank 596 on 712 target coordinates. Four register cycles plus 112 central tetrahedra give the matching 116-dimensional kernel:
\[
\ker D_0^{(3)}=V\oplus Q,\qquad \dim V=4,\quad\dim Q=112.
\]
The projected first-order central pair annihilates V. Its \(112\times112\) Gram determinant is nonzero modulo \(1000003\), with residue 655970 and infinity norm 12. Thus it is injective on Q. The safe weighted whole-gap exponent is 10.

## 4. The second two-term state by exact relabeling

Swapping the two petals of the second bowtie is logical \(X\) on qubit two. Applied to the complete **state_00m11** graph, including every private layer vertex, this permutation gives exactly the separately recovered source graph **state_01m10**. It sends
\[
|00\rangle-|11\rangle
\longmapsto
|01\rangle-|10\rangle.
\]
The checker verifies equality of the mapped vertex and edge sets, hence all clique complexes, and transports the 248-term integer filling with orientation signs. Signed permutation chain isometries transport the zero-weight kernel, projected bulk pair, and all spectral constants. No second rank computation is needed.

## 5. Palette consequence

The explicit weighted unary circuit construction requires only the following rank-one atom types after splitting each Hadamard pair:

1. computational-basis projectors;
2. the one-qubit clock difference \(|0\rangle-|1\rangle\);
3. the flip differences \(|00\rangle-|11\rangle\) and \(|01\rangle-|10\rangle\);
4. the four rational three-term Hadamard atoms.

The basis cone gives type 1. Sections 2–4 give types 2–3. [ACTIVE_HADAMARD_ORBIT.md](ACTIVE_HADAMARD_ORBIT.md) gives type 4 from one source-pinned representative. [SELECTED_CYCLE_GUARD_CLOSURE.md](SELECTED_CYCLE_GUARD_CLOSURE.md), now conditionally accepted after bounded review and local rechecking, tensors any base atom with every needed computational-basis guard without adding private vertices. The maximal total support locality is six.

Therefore the finite local certificate obligation is locally complete for the explicitly stated real-gate source
\[
G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}
\]
and for the exact mixed-spectator extension to single \(H\) gates. A finite common minimum supplies uniform constants, and \(m\le6\) gives the conservative exponent
\[
\kappa=4m+2\le26.
\]

This conclusion avoids an unrestricted integer-state gadget theorem and does not rely on approximate gate compilation. It concerns the local palette only. The remaining research burden is now end-to-end theorem integration, a meaningful exact source-promise consequence, and novelty relative to prior whole-kernel and filtered-homology results. The very poor polynomial gap remains unsuitable as a practical algorithmic claim.
