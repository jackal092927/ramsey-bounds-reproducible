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

A submission-focused ChatGPT Pro review of source commit `586811c` was received
as a preserved artifact and dispositioned against this later candidate. Its
verdict was submission-candidate after formalization and integration fixes; no
counterexample to the core chain was found. The target definition, finite
palette proposition and anonymous supplement, exact gate-dependent source,
encoded reduction outputs, clock sectors, field bridge, size bounds, source
scope, bibliography, and disclosure have since been repaired. See the dated
review and disposition records one directory above.

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
- The anonymous supplement was replayed cleanly on 2026-09-03; it is locally
  prepared but has not yet been uploaded to a submission system.


## Independent review, 2026-09-04

A full independent read of every section and appendix re-derived the
load-bearing chain: the affine decomposition \(D(\lambda)=D_0+\lambda D_1\)
and the chain-complex property of \(D_0\); the diagonal-scaling gap
\(\gamma_+\ge c\lambda^{2d_a+4}\); the join tensor-sum Laplacian, the
outside-harmonic padding and the relative-join identification of the padded
connecting map; the interface identity \(LL^*=\sum_jL_jL_j^*\) and the
elementary identity \(\sum_j\|y-y_j\|^2=(t-2)\|y\|^2+\sum_j\|y_j\|^2\);
the \(S_A\), \(S_Q\), and absorption steps of the leakage estimate; the
logical domination \(\Delta^\uparrow\succeq c\lambda^\kappa H^{\rm emb}\);
the injectivity/dimension closure including \(K_A=0\); independent filling and
quotient naturality; the weighted path Poincar\'e bound \(N\le8L^2E\); the
two-projector block computation and the value \(1/[3L(8L^2+1)]\); the
eight-label compression; the selected-cycle guard closure; and the common-copy
intertwining with \(f_v=Fw(v)^2\).  No mathematical error or counterexample
was found.

Rigor gaps closed in the manuscript:

1. *Independent private interiors* (no adjacency between private vertices of
   distinct gadgets) is now a named hypothesis (Definition 2.2); the proofs of
   Lemma 4.1 and Appendix A.4 use it and previously relied on the phrase
   "disjoint interiors".
2. Lemma 3.2 and Theorem 3.3 now require \(0<\lambda\le1\), which the scaling
   estimate \(\sigma_{\min}(W_k)\ge\lambda^{k+1}\) needs.
3. Appendix A now states the padded form of the local gap (only the bidegree
   \((d_a,s_{\rm top})\) lacks outside energy), which is the form that the
   logical-coercivity step actually uses.
4. The interface bound (7) is shown to hold automatically with
   \(N_j\le p_j\), the number of private vertices, rather than being an
   extra certified assumption.
5. The harmonic-projector formulation of the persistent Betti number used by
   Lowe et al. is proved equal to the induced-map rank, so Definition 2.1 is
   literally their Problem 9.
6. Remark 5.4 records the integer-weight rescaling, matching the
   polynomially-bounded-weight convention of Lowe et al.
7. The notation \(Q_j\) for the padded projector in Appendix A.3 is now
   explicit.

Presentation changes made for submission: new title; result-first abstract;
restructured introduction with informal Theorems 1.1--1.3, a technical
overview, one scope paragraph, and an organization paragraph; Section 7
rewritten around Lowe et al.'s Problem 9, Conjectures 1--2, Lemma 7 and Lemma
11, with a neutral technique comparison to the arXiv version of King--Kohler;
Section 8 rewritten as limitations plus five open problems; Remark 5.5 on
gate sets covered by Rudolph's Theorem 3.4; twelve standard references added;
footnote fixing Rudolph's numbering to the arXiv full version.

Remaining evidence boundary: unchanged from above (no equation-level
comparison with the published SIAM King--Kohler proof; no containment in BQP
claimed; the anonymous supplement is unchanged).  Venue note: the ITCS 2027
HotCRP site lists the registration deadline as September 2, 2026, 7:59:59 PM
EDT and the submission deadline as September 4, 2026, 7:59:59 PM EDT; a new
submission can be uploaded only if it was registered before the first date.
