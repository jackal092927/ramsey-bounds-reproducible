# Bounded concentration review — independent disposition

September 3, 2026. **CONDITIONAL IMPLICATION ACCEPTED AFTER LOCAL PROOF CHECK.** [The full external response](PRO_BOUNDED_PROOF_REVIEW_2026-09-03.md) is preserved separately with its 138 displayed equation sources. This disposition concerns the explicit finite hypotheses at source commit f4ec1b73ca99fa909b728e8165fb3e87fa9214b3. It is not complete-palette, source-priority, complexity-class, or paper certification.

## 1. Outcome and actual corrections

No invalid inference was found in the stated all-chain concentration implication. Pro supplied a correct distance-to-kernel proof for singular-value scaling when the boundary has nontrivial kernel. The canonical note now spells it out. This is an exposition completion, not a repaired false inequality.

The all-bidegree padding repair was already present in the submitted note. Pro's explanation confirms that repair; it does not discover it for the first time. The older two-bidegree truncation remains an archived mathematical error, already corrected before this request.

The logical and geometric operators remain distinct. No estimate against the unknown geometric kernel is used before dimension comparison.

## 2. Independent algebraic checks

| Inference | Checked argument | Disposition |
| --- | --- | --- |
| Nonzero singular value under invertible scaling | For K=ker A and x perpendicular to R^-1 K, dist(Rx,K)>=sigma_min(R)||x||. Apply A and then L. This works for rectangular, rank-deficient A; omit rank-zero blocks. | Accepted; detailed proof added |
| Local gap floor | Weight products give sigma_min(W_k)>=lambda^(k+1), sigma_min(W_(k-1)^-1)>=1. Hodge separates the nonzero spectra of the two adjacent boundaries. For d_a=2m_a-1, the safe squared exponent is 2d_a+4=4m_a+2. | Accepted; not an optimal valuation |
| Outside padding | On every reduced join bidegree, Laplacians add as tensor sums. Only s=q has outside harmonics, forcing r=d_a at the target degree. Other actual bidegrees retain the outside positive gap. Lambda derivatives act only on the fixed active factor. | Accepted, including higher local simplices |
| Shared register outputs | The exact sum identity is (t-2)||y||^2+sum_i||y_i||^2, including t=1. The horizontal interface Gram is sum_i L_i L_i*. The retained factor U is the actual private mass. | Accepted; no L_i-output orthogonality |
| Zero-weight leakage | D_0 coercivity bounds S_A. The private projected pair bounds S_Q by C(e/lambda^2+S_A). Since U<=N<=S_A+S_Q, the chi lambda^2 N term can be absorbed for lambda<=c/t. | Accepted for arbitrary chains |
| Exact-filling logical coercivity | A boundary is a cycle. The local up Laplacian is bounded below on its boundary space and vanishes on the orthogonal complement. Inclusion ran Pi_i in B_d(Y_i) therefore gives the global PSD order after exact up-column partition. | Accepted; no extra t factor |
| Logical distance | Split N plus <x,(P-P_K)x>. Only the latter uses g. With 0<g<=1, kappa>=2 and lambda<=c/t<=1, (t+lambda^-2)e is absorbed into C e/(g lambda^kappa). | Accepted; linear dependence on g |
| Multiplicity and whole gap | Projection into logical K is injective on the entire geometric spectral subspace below E. Independent private boundaries give V/W injection into homology. The two dimension bounds coincide. | Accepted, including K=0 |
| Natural persistence rank | The isomorphism is induced by v -> [v], not an arbitrarily chosen harmonic basis. Compatible inclusions produce the quotient surjection. | Accepted when both levels satisfy the stated hypotheses |
| Conservative scales | Choose a dyadic lambda within a fixed factor of c eta/t and E a fixed small multiple of eta^2 g lambda^26. The separate common-copy factor is F=lambda^-2. | Weighted Omega(eta^28 g/t^26), unweighted Omega(eta^26 g/t^24), as attainable floors |

For completeness, if a global boundary in V splits as sum_i partial c_i, every private component of each partial c_i must vanish separately. Each remaining register chain is a cycle by partial^2=0 and therefore belongs to the full space V=Z_d(R). This proves the boundary intersection used in the injection. An arbitrary proper logical subspace of Z_d(R) would not justify this argument.

The equal-dimensional projector bound uses the standard principal-angle identity. It is a norm-closeness statement, not literal equality of embedded logical and geometric harmonic vectors.

## 3. Constants and the optional interface refinement

All constants depend only on the fixed active graph matrices, their certified zero-weight positive gaps, private-pair bounds, and the uniform outside gap. They do not depend on the number of outside qubits, logical dimension, t, g, or lambda. Norms after padding are controlled by the finite direct sum of active degrees and tensoring with identities/projections.

The proof actually needs chi lambda^2 below a fixed constant. If an instance has a certified smaller chi, one may choose
\[
\lambda\le c\min\{1,(1+\chi)^{-1/2},\eta/\sqrt t\}.
\]
The last restriction also implies t<=C lambda^-2 for eta<=1, so the final energy absorption still works. This is a parameterized corollary of the existing proof. No improved interface bound for the circuit family has been established.

A certificate subspace Q need only be supported on private coordinates; the proof never requires it to be spanned by individual simplices. Outside-harmonic padding already produces such a non-coordinate subspace. The canonical statement now makes this scope explicit. This proof-level relaxation will be used in the next guard construction, which is separately reviewed.

## 4. Evidence and next gate

The response was requested to use only the supplied note. Its four visible citation markers refer to that attachment; no external links appear. Collection did not perform new primary literature checking. The response's approval is model feedback; the algebraic checks above are the local basis for adoption.

The previously certified unguarded Hadamard orbit remains unchanged. Complete basis/two-term/guard integration remains open. The next bounded question is an explicit selected-cycle guard attachment and its finite zero-weight data, not another broad request to approve the entire reduction. Novelty and a meaningful exact-source complexity consequence remain separate gates.
