# Proof audit

## Verdict and scope

Status: **internally closed under the manuscript's explicit assumptions**.
No counterexample was found to the finite-certificate transfer,
kernel/min--max closure, or quotient naturality.  This is not a certification
of every archived gadget computation, an unrestricted complexity-class
equivalence, or the paper's final novelty against all published versions.

The load-bearing new statement is the arbitrary-chain concentration theorem
in Section 3 and Appendix A.  Exact kernel multiplicity and the positive gap
are standard dimension/min--max consequences once concentration and exact
filling are both available.  The quotient description is elementary linear
algebra once independent filling is established.

## Assumptions that must remain visible

1. The clique-gadget palette is fixed and finite.
2. Each local active constraint is rank one on its support.  After outside
   harmonic padding, the global logical projector may have higher rank.
3. Gadget interiors and their input coordinate blocks are disjoint; interfaces
   may share register outputs.
4. Each gadget has exact filling intersection
   \(B_d(Y_j)\cap V=\operatorname{ran}\Pi_j\), and the selected-cycle guard
   supplies the stated zero-weight kernel and coercive private pair.
5. The arbitrary-chain estimate is uniform over every normalized geometric
   chain, rather than only simulated-register vectors.
6. Common-copy unweighting is used through the sourced Hayakawa theorem and is
   applied consistently at every filtration level.

## Dependency audit

| Step | Claim used | Audit result |
|---|---|---|
| Local scaling | Finite weighted boundaries have positive gap at least \(c\lambda^{4m+2}\) | Closed by diagonal scaling and the finite palette |
| Padding | Only outside harmonic tensors cancel the unit-weight bulk boundary | Closed; the earlier all-coordinate formulation is not used |
| Interfaces | For \(L=[L_1\ \cdots\ L_t]\), \(LL^\dagger=\sum_jL_jL_j^\dagger\preceq\lambda^2\sum_jN_jI\) | Closed; output orthogonality is unnecessary |
| Concentration | Low geometric energy forces proximity to the embedded logical kernel | Closed under the local certificate; this is the load-bearing proof |
| Filling | \(B_d(X_A)\cap V=\sum_{j\in A}\operatorname{ran}\Pi_j\) | Closed by independent private chains |
| Kernel | Exact fillings inject \(V/W_A\), while concentration bounds the low spectral dimension | Closed, including the zero-dimensional logical-kernel case |
| Gap | No additional geometric zero vector exists, hence the next eigenvalue is at least the chosen threshold | Closed by the same dimension argument |
| Naturality | Inclusion sends \([v]_{W_A}\) to \([v]_{W_B}\) | Closed; this is the natural quotient epimorphism |
| History input gap | Legal weighted paths have gap \(1/(8L^2)\); illegal clocks cost at least one | Closed in Appendix B |
| History output gap | Two-projector block estimate gives at least \(1/[3L(8L^2+1)]\) | Closed by the explicit \(2\times2\) block calculation |
| Eight-label source | Initial kernel has dimension 8; final kernels have dimensions 6 and 1 | Closed for the stated fixed-input \(\mathrm{BQP1}^{G_2}\) promise |
| Unweighting | Common-copy blowup preserves Laplacians and inclusion maps | Closed conditional on the cited theorem |

## Four objections rechecked

1. **Spectator gate: retracted.**  With
   \(U'=U\otimes H^h\), \(P'_{\rm acc}=P_{\rm acc}\otimes I\), and
   \(J'=J\otimes I\), direct cancellation gives \(M'=M\otimes I\) for odd or
   even \(h\).  No \(M\otimes H\) term occurs, and adding an \(HH\) pair does
   not alter parity.
2. **Shared interface outputs: retracted.**  Horizontal concatenation gives
   \(LL^\dagger=\sum_jL_jL_j^\dagger\).  Orthogonality of output ranges is not
   required.  The separate \(t\lambda\) contribution comes from summing local
   kernel-projector errors.
3. **Ratio approximation: corrected.**  Distinguishing \(1/2\) from \(1/3\)
   requires additive error below \(1/12\); the manuscript uses \(1/24\).
   Complexity hardness is stated only for the explicit circuit promise.
4. **Initial homology: retracted.**  The normalized bow-tie cycle embedding
   and history isometry are explicit.  Therefore the initial dimension is
   constructed, rather than inferred from a hard counting problem or an empty
   initial term set.

## Remaining risks

- Equation-level novelty comparison with the final SIAM King--Kohler proof is
  unperformed.  This is a novelty risk, not a mathematical objection to the
  stated theorem.
- The very small inverse-polynomial gap is a theory guarantee and has no
  near-term practical interpretation.
- General integer-state or complex-phase gadget extensions are outside scope.
- The archived exact certificate scripts support the fixed palette; this audit
  does not independently reconstruct every simplicial incidence table by hand.
