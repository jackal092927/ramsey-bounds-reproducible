# Corrections to the conversational hostile audit

This records the final mathematical disposition of earlier assistant objections. Earlier raw reviews are historical criticism, not facts. These corrections supersede both the original audit and residual errors in its first retraction.

| ID | Earlier objection or assertion | Correct disposition |
| --- | --- | --- |
| C1 / A6 | Odd spectator Hadamard parity changes acceptance to \(M\otimes H\) | **Retracted.** The circuit unitary factors as \(U\otimes H^h\), but the acceptance sandwich yields \(M\otimes I\) for every \(h\). |
| C2 / A6 | Appending an \(HH\) pair fixes odd parity | **Retracted.** It adds two and preserves parity. No parity repair is needed. |
| C3 / A6 | Existing clean work prevents the mixed-spectator extension | **Retracted.** \(J'=J\otimes I\) retains all existing clean work and adds one mixed input qubit. Both input dimension and perfect multiplicity double. No unrestricted class equivalence follows. |
| C4 / A7 | The interface estimate needs output orthogonality or almost commutation | **Retracted.** Orthogonal input blocks make \(L=[L_1\cdots L_t]\) a block row, so \(LL^\dagger=\sum_jL_jL_j^\dagger\). A shared output is allowed. |
| C5 / A7 | \(O(\lambda\sqrt t)\) conflicts with \(t\lambda\) concentration | **Retracted.** They bound different terms: interface operator norm and the sum of projector errors. |
| C6 / theorem iv | Additive error \(1/6\) distinguishes \(1/2\) versus \(1/3\) | **Retracted.** The promise separation is \(1/6\); error must be \(<1/12\). Error \(1/24\), threshold \(5/12\), is valid. |
| C7 / theorem iv | These constants imply BQP-hardness | **Retracted.** They only transfer the explicitly defined circuit promise. A separate source reduction is needed for any class-hardness claim. |
| C8 / first retraction | The scalar argument supplies no NO-side bound | **Retracted as well.** Positivity gives \(f\le p\), so \(p\le1/3\) does imply \(f\le1/3\). The missing BQP conclusion concerns the source class, not this NO inequality. |
| C9 / A3 | Logical embedding is an unstated or nonisometric map | **Discharged by the supplied construction.** Normalized disjoint bowtie cycles and joins give the explicit register isometry; the weighted history map has \(\mathcal V^\dagger\mathcal V=I_D\). |
| C10 / A3 | A linear image might exceed its domain dimension | **Retracted.** This is impossible. The relevant task is to identify the target subspace and apply the stated concentration inequality, not invent a dimension-increasing failure. |
| C11 / A3 residues | Exact compatible harmonic isometries must additionally be proved for rank transfer | **Retracted as a requirement of this argument.** Register encoding and history isometry are distinct from exact harmonic representative compatibility. Quotient naturality and whole-kernel dimension equality suffice for the induced ranks. |
| C12 / A4 | Initial term set must be empty, or the denominator is an unknown hard count | **Discharged.** The anchored-history construction characterizes the whole initial kernel with known \(D>0\). An empty term set is unnecessary. Isometry alone would give only a lower bound, but the full construction includes the upper characterization. |
| C13 / relative acyclicity | Extra global relative-acyclicity is required after concentration and injection | **Retracted.** The all-chain geometric concentration bounds the entire low-energy dimension. A torus counterexample to injection alone fails that extra stated concentration hypothesis. Local bulk spectral assumptions used to prove concentration are still explicit dependencies. |
| C14 / A1 | Concentration is only a routine local check | **Rejected framing.** The arbitrary-chain global concentration theorem is the load-bearing proof and must be headlined. The quotient/min-max/naturality deductions are standard once it holds. |
| C15 / gap scaling | The final gap is simply \(L^{-81}\) | **Corrected bookkeeping.** For \(m=6\), the displayed scale is \(\eta^{54}g^{27}/t^{27}\); substituting \(g=\Theta(L^{-3})\) does not remove \(t^{-27}\). No near-term claim is warranted. |

The original assistant checked none of the six primary sources. Its conditional novelty verdict was advisory and does not establish priority. This consolidation has recovered written local reports and completed Pro feedback, but has not independently certified the complete gadget reduction or paper readiness.

A mathematically legitimate remaining objection must identify a failed explicit hypothesis, an invalid derivation, or a genuine model mismatch. A statement being elementary, anticipated, or already known is a novelty/value issue and should be labeled separately.
