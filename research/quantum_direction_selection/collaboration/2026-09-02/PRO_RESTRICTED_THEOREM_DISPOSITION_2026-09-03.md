# Restricted-theorem integration review — independent disposition

September 3, 2026. **INTEGRATION ACCEPTED AFTER ONE SOURCE-INTERFACE CORRECTION.** The [complete external response](PRO_RESTRICTED_THEOREM_REVIEW_2026-09-03.md) is preserved separately with all 137 displayed equation sources. The review treated the finite atom calculations, the all-chain concentration theorem, and the selected-cycle guard theorem as hypotheses, exactly as requested. It performed no source-complexity proof, literature search, priority check, or independent recomputation.

## 1. Mathematical disposition

No counterexample was found under the corrected hypotheses. The one substantive objection is valid: the previous statement allowed an abstract isometry \(J\) and did not constrain \(P_{\rm acc}\), while the certified palette implements computational-basis anchors and guards. The source problem must therefore state
\[
J=I_{\rm mixed}\otimes |c\rangle_{\rm clean}
\]
for maximally mixed input qubits and a fixed computational-basis clean string, and must use a fixed-local computational-basis acceptance measurement. An arbitrary entangled input-code isometry or arbitrary global output projector is not covered.

This is a missing theorem hypothesis, not a failure of the reduction once that hypothesis is supplied. [CLEAN_RESTRICTED_REDUCTION_THEOREM.md](CLEAN_RESTRICTED_REDUCTION_THEOREM.md) has been corrected accordingly.

The response also correctly identifies an imprecise sentence: persistent rank is not itself the endpoint Betti number. The theorem now separately states
\[
\beta_d(X_{\rm out})=\dim S
\]
and
\[
\operatorname{rank}[H_d(X_{\rm in})\to H_d(X_{\rm out})]=\dim S.
\]
Both follow from the canonical quotient description, but they are logically distinct statements.

## 2. Integration checks

| Component | Independent disposition |
| --- | --- |
| Atom exhaustion | Accepted for the corrected circuit interface. Basis clock/input/output penalties, stationary and flipping reversible transitions, and the four gain/loss Hadamard atoms exhaust the stated exact gate history. Unacted-on qubits contribute identities and outside harmonics, not extra guarded atoms. |
| Common degree | Accepted under the reduced-join convention. An \(m\)-qubit target of degree \(2m-1\), joined with \(n-m\) outside bowties of degree \(2(n-m)-1\), lands in degree \(2n-1\). |
| Filtration | Accepted. The output graph adds rejection gadgets on fresh private vertices to the same register; no private-private cross edges are added. This gives the natural inclusion used by the quotient map. |
| Initial denominator | Accepted. Legal clock plus propagation gives one history per allowed input, and computational-basis input anchors restrict the seed exactly to the \(D=2^k\) mixed-input sector. The history map is an isometry and there are no additional logical zeros. |
| Output kernel and gap | Accepted. Positivity gives the kernel intersection, compression to history is \((I-M)/Z\), and the off-perfect promise supplies the positive principal-angle penalty. The two-positive-operator bound includes \(S=0\). |
| Whole geometric kernel | Accepted conditional on the stated all-chain concentration theorem. The register quotient injects \(\dim K_A\) exact zeros; concentration bounds the entire spectral subspace below \(E\) by the same dimension. This proves endpoint homology and a gap above the whole kernel, not an approximate-mode count. |
| Persistent rank | Accepted. The canonical endpoint identifications commute with register inclusion, so the induced map is the natural surjection \(V/W_A\to V/W_B\), including a zero target quotient. |
| Gap exponents | Accepted algebraically. With \(\lambda=\Theta(\eta/t)\) and \(\kappa=26\), the safe weighted floor is \(\Omega(\eta^{28}g/t^{26})\); multiplying by \(F=\lambda^{-2}\) gives the separate conditional unweighted floor \(\Omega(\eta^{26}g/t^{24})\). Polynomial-size unweighting requires fixed or inverse-polynomial \(\eta\) and common labeled copy blocks. |
| Spectator | Accepted exactly for a maximally mixed unmeasured spectator: \(M'=M\otimes I\), so both dimensions double and the fraction and off-perfect gap remain unchanged for either parity of the Hadamard count. |
| Fraction promise | Accepted. \(f\le p\le r+(1-r)f\) yields \(f\ge1/2\) versus \(f\le1/3\) at \((a,b,r)=(2/3,1/3,1/3)\). Additive error must be strictly below \(1/12\); \(1/24\) is safe. |

## 3. Surviving theorem and next obstruction

The surviving result is a polynomial representation/transfer theorem from one explicit exact real-circuit promise to true initial-homology-normalized persistence, with exact endpoint multiplicities, exact induced rank, and inverse-polynomial whole-kernel gaps. This is stronger than an exact multiplicity statement alone and does not use simplex normalization or a low-energy surrogate.

The first unresolved theorem-level obstacle is source complexity. The source promise simultaneously requires an exact eigenvalue-one subspace, an off-perfect spectral ceiling, and a trace gap over a growing maximally mixed sector. No reduction from a recognized standard source problem has yet been supplied. The \(D=1\) specialization loses the intended normalization content, so it is not an adequate substitute for an impactful normalized-persistence hardness result.

Novelty is a separate unresolved gate. The supplied ledger indicates collisions with parsimonious homology multiplicity and related harmonic-survival constructions, but neither this collection step nor the Pro review checked the underlying papers. No priority or paper-readiness conclusion is promoted here.
