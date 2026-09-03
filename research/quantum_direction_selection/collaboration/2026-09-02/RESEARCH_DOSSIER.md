# True normalized persistence: research dossier and forward program

Prepared September 2, updated September 3, 2026 PDT. This dossier consolidates the conversation, round-2 derivations, source ledger, failed approaches, and the collected Pro responses. The September 3 continuation below supersedes the older parameter choice retained in Section 2. This is handoff context, not a submitted manuscript or a certificate of the full reduction.

## 1. Objective and evidence standard

The intended statistic is
\[
q(X_1,X_2)=\frac{\operatorname{rank}[H_d(X_1)\to H_d(X_2)]}{\dim H_d(X_1)},\qquad \dim H_d(X_1)>0.
\]
It is the fraction of initial homology that survives. The target concerns exact zero modes. Neither simplex-normalized Betti numbers nor quasi-low-energy counts substitute for this statistic.

The aim is a high-quality, impactful theoretical computer science paper. The strongest current candidate is a global geometric concentration theorem for a fixed supported gadget palette, leading to exact multiplicities, whole-positive-spectrum gaps, and natural filtered rank transfer. It has a mathematically valid consequence for an explicit separated exact-real-gate circuit promise. The later eight-label construction has now passed local and bounded Pro interface audits and upgrades the conditional weighted result to gate-dependent \(\mathsf{BQP}_1^{G_2}\)-hardness. Equivalence with unrestricted \(\mathsf{SDQC}_1\) is not established, and novelty of the geometric package remains open. Quantum persistence and parsimonious homology encodings already exist according to the supplied ledger.

Evidence labels used throughout:

- **LOCAL DERIVATION:** a written mathematical argument; its explicit hypotheses remain part of the statement.
- **IMPORTED:** a cited local gadget or literature theorem; not re-proved by this session.
- **FIXTURE:** a finite exact or numerical implementation check, never an asymptotic proof.
- **FINITE CERTIFICATE:** exact integer/modular evidence proving specified properties of a recorded finite source graph; its complete-palette extension is a separate obligation.
- **ADVISORY:** an external model's proposal or review, requiring independent evaluation.
- **OPEN / RETRACTED:** an unmet obligation or a conclusion explicitly withdrawn.

The primary source ledger was supplied as previously checked locally. This consolidation has read the local reports; it has not independently reread all six primary sources. A completed Pro answer is also not independent source verification by this agent.

### September 3: strongest current conditional theorem

The new Pro response is [collected in full](PRO_REVIEW_2026-09-03.md) and has a [separate disposition](PRO_REVIEW_DISPOSITION_2026-09-03.md). Independent continuation gives two proofs of the stronger bound
\[
\|(I-P_{K_A})x\|^2\le C\left[t\lambda^2+
\frac{\langle x,\Delta_Ax\rangle}{g\lambda^{4m+2}}\right].
\]
The [first proof](EXACT_FILLING_COERCIVITY.md) uses the older local spectral package. The [simpler finite-certificate proof](FINITE_CERTIFICATE_CONCENTRATION.md) instead uses exact filling, a zero-weight kernel identity, and an injective projected central-bulk pair. A diagonal boundary-scaling argument supplies a sufficient positive-gap floor without computing its optimal spectral valuation.

Choose \(\lambda\le c\min(t^{-1},\eta/\sqrt t)\), independently of \(g\), and \(E\le c'\eta^2g\lambda^{4m+2}\). The same injection/min-max and natural quotient conclusions follow. For \(m\le6\), a conservative dyadic \(\lambda=\Theta(\eta/t)\) yields the attainable lower-bound scales
\[
E=\Omega(\eta^{28}g/t^{26}),\qquad
FE=\Omega(\eta^{26}g/t^{24}),\quad F=\lambda^{-2},
\]
the second under the separate common-copy unweighting theorem. Neither expression is an assertion that the actual gap equals the floor.

One [actual Rudolph representative](REPRESENTATIVE_GADGET_CERTIFICATE.md) first supplied an exact source-pinned certificate: target Betti number 3; an integer filling of the intended three-term cycle; zero-weight kernel dimension \(180=4+176\); and an injective central bulk pair. The graph also exposed and repaired a false two-bidegree enumeration in the old padding note. Subsequent source-pinned atom checks, orbit transports and selected-cycle guards now cover the complete fixed real-gate palette through locality six.

Later the same day, [explicit register relabelings](ACTIVE_HADAMARD_ORBIT.md) transported this certificate to all four unguarded active Hadamard three-term states; four integer filling equations were checked. A new offline verifier recomputes the archived graph certificate without gh/network access. The broad follow-up Pro attempt ended with “Thinking failed,” so it supplies no final mathematical verdict; [its visible activity and concrete reproduction errors](PRO_FAILED_ATTEMPT_2026-09-03.md) are preserved. The successor is narrowed to a completed audit of the conditional all-chain proof.

The bounded successor is now [completed and fully collected](PRO_BOUNDED_PROOF_REVIEW_2026-09-03.md), with UI duration 8m 39s. The [independent disposition](PRO_BOUNDED_PROOF_DISPOSITION_2026-09-03.md) accepts the explicit conditional all-chain implication and expands its rank-deficient scaling justification. This is not source or full-palette certification.

A new [selected-cycle guard construction](SELECTED_CYCLE_GUARD_CLOSURE.md) uses Z=(Y*S_beta) union (R*B): private vertices connect only to the selected guard petal. Relative chains prove the intended filling relation; the zero-weight private complex tensors with the selected cycle, giving Q'=Q tensor span(gamma_beta). A private-supported subspace suffices; it need not be a coordinate span. The [completed bounded review](PRO_SELECTED_GUARD_REVIEW_2026-09-03.md) and [independent disposition](PRO_SELECTED_GUARD_DISPOSITION_2026-09-03.md) accept the lemma after three scope clarifications. On one guarded source atom, [46,998 exact boundary identities and a 1,528-term integer filling](SELECTED_CYCLE_GUARD_CHECKS.json) pass, including all-domain projected T0 cancellation and exact normalized bulk-pair transfer.

The [remaining active-atom certificate](REMAINING_ACTIVE_ATOM_CERTIFICATES.md) now supplies source-pinned integer proofs for the one-qubit difference and both two-qubit two-term states. Together with the basis cone, Hadamard orbit and guard lemma, this locally closes the finite palette for the explicit real-gate history. The strongest integrated statement is [the clean restricted reduction theorem](CLEAN_RESTRICTED_REDUCTION_THEOREM.md). Its exact source promise has no established standard-class hardness in this archive; novelty of the combined whole-kernel and normalized filtered-rank theorem also remains open.

The [completed end-to-end Pro audit](PRO_RESTRICTED_THEOREM_REVIEW_2026-09-03.md) and [independent disposition](PRO_RESTRICTED_THEOREM_DISPOSITION_2026-09-03.md) accept the integration after restricting the source interface to maximally mixed inputs, computational-basis clean ancillas and a fixed-local computational-basis output measurement. The theorem now separately states the output Betti number and the induced rank. No local mathematical gap remains under the displayed finite hypotheses.

A [targeted source-complexity check](SOURCE_COMPLEXITY_GATE.md) identifies the next obstruction. The fixed constants \((a,b,r)=(2/3,1/3,1/3)\) give a valid perfect-space fraction gap \(1/6\), but arbitrary inverse-polynomial trace thresholds do not: \(M=I/4\) and \(M=0\) have different traces and the same zero perfect-space fraction. The checked arXiv v1 definition of \(\mathsf{SDQC}_1\) permits arbitrary thresholds and explicitly depends on its exact gate set. The present result therefore supports a separated real-gate source promise; unrestricted \(\mathsf{SDQC}_1\)-hardness still requires a threshold-preserving, exact-gate reduction.

The [completed source-complexity Pro audit](PRO_SOURCE_COMPLEXITY_REVIEW_2026-09-03.md) and [independent disposition](PRO_SOURCE_COMPLEXITY_DISPOSITION_2026-09-03.md) close this gate at the restricted boundary. For general thresholds, the guaranteed exact-fraction gap is
\[
\delta_f=\max\!\left\{0,\frac{a-r}{1-r}\right\}-b.
\]
The response gives admissible YES and NO operators with the same exact perfect-space fraction whenever these intervals overlap, so \(\delta_f>0\) is necessary as well as sufficient for a reduction that realizes only that fraction. Perfect-subspace-preserving amplification cannot repair an arbitrary trace promise. The accepted source statement is therefore \(\operatorname{SepPerfectFraction}^{\mathcal G_R}(a,b,r)\), stated directly as a circuit promise; a restricted class name is optional and carries no standard-class equivalence. Pro performed no source checking in this round.

After that review, a separate [eight-label source construction](NORMALIZED_BQP1_SOURCE_GATE.md) supplied a stronger route. Starting from an exact \(G_2\) BQP verifier with perfect completeness and soundness at most \(1/3\), one mixed three-bit label produces
\[
M_x=\operatorname{diag}(1,p_x,p_x,p_x,p_x,p_x,0,0)\otimes I_{\rm dummy}.
\]
The perfect-space fraction is therefore \(3/4\) in YES instances and \(1/8\) in NO instances, while the latter has off-perfect ceiling at most \(1/3\). The construction runs the verifier unconditionally, so it introduces no controlled-Hadamard requirement. The local algebra and the clean-input/output interface in Rudolph's Definition 2.2, exact \(G_2\) soundness reduction in Theorem 2.3, and cyclotomic inclusion in Theorem 3.4 were checked. The [bounded Pro audit](PRO_BQP1_SOURCE_REVIEW_2026-09-03.md) and [independent disposition](PRO_BQP1_SOURCE_DISPOSITION_2026-09-03.md) accept the exact source composition. This supports gate-dependent \(\mathsf{BQP}_1^{G_2}\)-hardness for the weighted target, conditional on the geometric theorem. The denominator growth is padding-generated, which is mathematically valid but weakens the conceptual impact claim.

## 2. Core finite-palette transfer theorem (original conservative parameters)

Work over \(\mathbb C\), or over \(\mathbb R\) for the real construction. Let \(R\) be a top-dimensional register complex with \(\dim R=d\ge1\), and let
\[
V=Z_d(R)\subset C_d(R).
\]
The entire top cycle space is used. The logical register is identified isometrically with \(V\), using normalized edge-disjoint bowtie cycles and their tensor joins. Write \(H_A=\sum_{j\in A}P_j\) for the logical positive-projector Hamiltonian and \(\Delta_A\) for the full geometric degree-\(d\) Laplacian on \(X_A\). These are different operators on different spaces.

Each \(Y_j\supset R\) belongs to a fixed finite family of correctly implementing clique gadgets. Distinct interiors have independent chain-coordinate supports; intersections lie in \(R\), with no cross-interior simplices. Assume the single-gadget exact filling relation
\[
B_d(Y_j)\cap V=\operatorname{ran}P_j.
\]
For \(X_A=\bigcup_{j\in A}Y_j\), independent boundaries then prove
\[
B_d(X_A)\cap V=W_A:=\sum_{j\in A}\operatorname{ran}P_j.
\]
Indeed, a filling \(\partial c\in V\) decomposes as \(\sum_j\partial c_j\). There are no register \((d+1)\)-chains, and off-register coordinates from different interiors cannot cancel. Each \(\partial c_j\) is therefore in \(V\), where the single-gadget hypothesis applies. Thus \(V/W_A\) injects into \(H_d(X_A)\), and its dimension is \(r_A=\dim K_A\), with \(K_A=\ker H_A\).

The substantive global estimate is for **every** normalized geometric chain \(x\) of energy below \(E\):
\[
1\le \langle x,\Pi_Vx\rangle-\langle x,H_A^{\rm emb}x\rangle+
C\left(t\lambda+t^2\lambda^2+\frac{tE}{\lambda^{4m+2}}\right).
\]
Here \(H_A^{\rm emb}\) is zero off \(V\); \(t\) bounds the number of terms; \(m\) is fixed; \(C\) is independent of the exponentially large register dimension. This is concentration toward the embedded **logical** kernel, not toward \(\ker\Delta_A\), whose dimension is initially unknown.

Assume
\[
H_A\succeq g(I_V-P_{K_A}),\qquad 0<g\le1.
\]
Let \(\mathcal R\) be the displayed error remainder and embed \(P_{K_A}\) into the chain space. Since
\[
g(1-\langle x,P_{K_A}x\rangle)
\le1-\langle x,\Pi_Vx\rangle+\langle x,H_A^{\rm emb}x\rangle
\le\mathcal R,
\]
choose common parameters
\[
0<\lambda\le c\eta^2g/t,\qquad
0<E\le c\eta^2\lambda^{4m+2}g/t,\qquad 0<\eta<1.
\]
The constant \(c\) depends only on the finite palette constants. Every unit vector in the geometric spectral subspace below \(E\) then has nonzero projection onto \(K_A\). Consequently that subspace has dimension at most \(r_A\). The quotient injection supplies \(r_A\) exact zeros, proving
\[
\dim\ker\Delta_A=r_A,\qquad \operatorname{spec}(\Delta_A)\cap(0,E)=\varnothing.
\]
When \(r_A=0\), the entire spectrum lies in \([E,\infty)\).

This establishes whole-kernel **multiplicity** and a quotient isomorphism. It does not assert literal equality between geometric harmonic vectors and embedded logical vectors. No additional global relative-acyclicity assumption is needed once the full concentration estimate and injection hold.

For \(A\subseteq B\), common register, weights, and labels identify the induced homology map with the natural surjection
\[
V/W_A\twoheadrightarrow V/W_B.
\]
Hence its rank is \(\dim K_B\). For a finite chain of term sets, the same argument applies simultaneously using a common lower gap bound and maximum term count. No new births occur in this degree in this quotient filtration; that restricted barcode behavior is a consequence, not arbitrary persistence-module universality.

**Status:** the boundary, dimension, and naturality arguments are written local derivations and standard linear algebra once the hypotheses hold. The global concentration proof and exact source integration carry the research burden. See ../../round2/NORMALIZED_PERSISTENCE_PROBE.md and ../../round2/UNWEIGHTING_AUDIT.md.

## 3. What the padding repair actually uses

For gadget \(j\), use central **local bulk tensored with outside harmonics**, not all padded central coordinates. The outside boundary and coboundary vanish on those harmonic factors. This removes the weight-one outside differential that invalidates the unrestricted coordinate-bulk estimate.

The interface maps \(L_j\) have mutually orthogonal gadget input blocks and a shared register output. Thus
\[
L_{\rm tot}=[L_1\ \cdots\ L_t],\qquad
L_{\rm tot}L_{\rm tot}^{\dagger}=\sum_jL_jL_j^\dagger
\preceq\lambda^2\Big(\sum_jN_j\Big)I.
\]
For the fixed palette \(N_j=O(1)\), giving \(\|L_{\rm tot}\|=O(\lambda\sqrt t)\). Output orthogonality is unnecessary. The \(t\lambda\) concentration term instead comes from summing local kernel-projector errors.

The original local package includes exact nullity, local kernel convergence, lifted-sector spectral bounds, and a central-relative-bulk singular-value bound. These assumptions belong to the original proof route. The September 3 finite-certificate route replaces the perturbative spectral-sector inputs, as stated above. Neither route adds a global relative-acyclicity hypothesis. Basiswise closeness in exponentially growing dimension cannot replace an operator-norm estimate. At the target degree only the outside-harmonic bidegree is fixed; all other actual bidegrees are handled by the outside gap, with no upper-dimension truncation of the active graph.

## 4. Exact verifier implementation and denominator

Use \(G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}\). Following Rudolph's credited construction, replace a Hadamard pair by consecutive gain/loss propagation \(\sqrt2H\) and \(H/\sqrt2\). The active three-term projectors are rational, and tensoring fixed basis guards keeps total locality at most six. The guarded Toffoli terms factor into fixed controls and an active one- or two-qubit state. An unrestricted integer-state gadget theorem is not assumed.

The legal history has
\[
\mathcal V=Z^{-1/2}\sum_{t=0}^{L-1}s_t|t\rangle U_tJ,\qquad
s_t\in\{1,\sqrt2\},\quad Z=\sum_ts_t^2,\quad \mathcal V^\dagger\mathcal V=I_D.
\]
Thus the **squared** clock weights are one or two. The clean-input anchor and propagation characterize the entire initial kernel as \(\operatorname{ran}\mathcal V\), of known positive dimension \(D\). The initial term set need not be empty. Both the isometry and the no-extra-initial-kernel argument are written in ../../round2/UNARY_PALETTE_ADDENDUM.md.

Weighted variance on the valid-input sector and an anchored telescoping estimate on its complement give
\[
g_1\ge\frac1{8L^2},\qquad g_2\ge\frac1{120L^3}
\]
under the stated \(r=1/3\) off-perfect-acceptance promise. The final-kernel-zero case is included.

The independently checked sharper two-projection bound now improves the second certified floor to \(g_2\ge1/[3L(8L^2+1)]\ge1/(27L^3)\); see the September 3 disposition. The original \(1/(120L^3)\) remains a valid conservative bound.

For an arbitrary positive coefficient family, replacing \(\sum_ja_jP_j\) by \(\sum_jP_j\) preserves the kernel and lowers the positive gap by at most \(a_{\max}\). This supports exact rank transfer without a small output coefficient, provided the coefficient bound is polynomial.

With \(m=6\), the geometric exponent is \(4m+2=26\). At the original Section 2 parameter scale,
\[
E=\Theta\!\left(\eta^{54}g^{27}/t^{27}\right)
\]
up to the fixed choice of constants. This historical floor is superseded by the stronger conditional bound near the beginning of the dossier. Both have poor polynomial exponents; there is no near-term performance claim.

## 5. Exact single-Hadamard extension

For a circuit \(U\) over \(\{X,\mathrm{CX},\mathrm{CCX},H\}\), add one mixed, unmeasured spectator \(a\), and replace every \(H_j\) by \(H_j\otimes H_a\). With \(h\) the number of Hadamards,
\[
U'=U\otimes H_a^h,\quad P_{\rm acc}'=P_{\rm acc}\otimes I_a,\quad J'=J\otimes I_a.
\]
The acceptance operator is therefore
\[
M'=(J^\dagger\otimes I)(U^\dagger\otimes(H^h)^\dagger)
(P_{\rm acc}\otimes I)(U\otimes H^h)(J\otimes I)=M\otimes I.
\]
This holds for odd and even \(h\). Initial mixed-input dimension and perfect-acceptance multiplicity both double; their fraction and the acceptance spectral separation are unchanged. Existing clean work stays in \(J\). This is an exact gate extension for that explicit clean-work/mixed-input model, not a class-equivalence theorem. The numerical spectra of differently constructed history Hamiltonians are not asserted identical; the same proved gap bounds apply with the appropriate clock length.

An extension covering arbitrary complex phase gates has not been established. Approximate compilation does not preserve exact perfect acceptance.

## 6. Source promise and minimal defensible consequence

Let \(M=J^\dagger U^\dagger P_{\rm acc}UJ\), \(0\preceq M\preceq I\), \(S=\ker(I-M)\), and \(M|_{S^\perp}\preceq rI\), \(r<1\). Set \(p=\operatorname{Tr}(M)/D\), \(f=\dim S/D\). Exactly,
\[
f\le p\le r+(1-r)f.
\]
Consequently trace promises \(p\ge a\) and \(p\le b\) give the exact guaranteed ranges
\[
f_{\rm YES}\ge\ell:=\max\{0,(a-r)/(1-r)\},
\qquad f_{\rm NO}\le b.
\]
Define \(\delta_f=\ell-b\). The exact-fraction target separates the promise cases if \(\delta_f>0\). Conversely, whenever the intervals overlap, a rational \(q\in[\ell,b]\) supports admissible YES and NO operators with the same fraction: use \(M_N=I_{qD}\oplus0\) and \(M_Y=I_{qD}\oplus[(a-q)/(1-q)]I\). Thus positive \(\delta_f\) is necessary as well as sufficient for a reduction that realizes only \(f\).

For \(a=2/3,b=1/3,r=1/3\): YES gives \(f\ge1/2\), NO gives \(f\le1/3\). Additive error must be below \(1/12\); \(1/24\) with decision threshold \(5/12\) works. A trace gap alone fails, as \(M=I/4\) versus \(M=0\) both have \(f=0\).

The minimal theorem is a polynomial transformation from the explicitly specified separated real-gate circuit promise \(\operatorname{SepPerfectFraction}^{\mathcal G_R}(a,b,r)\), with \(\delta_f\ge1/\operatorname{poly}(n)\), to a nested weighted clique pair with
\[
\beta_d(X_1)=D,\qquad \beta_d(X_1\to X_2)=\dim S,\qquad q=f,
\]
both whole-positive-spectrum gaps, and an explicitly costed approximate initial harmonic mixture. Additive target error below \(\delta_f/2\) decides the source. After the spectator extension both dimensions double, with \(q\) unchanged. A common-copy unweighting corollary is available under its own exact, polynomial multiplicity assumptions.

This transfers the **explicit circuit promise problem**. The subsequent eight-label lemma composes that theorem with \(\mathsf{BQP}_1^{G_2}\), and its bounded interface review is complete. It does not establish ordinary BQP-hardness, DQC1-hardness, unrestricted \(\mathsf{SDQC}_1\)-hardness, or that the separated trace promise itself is outside BPP. The arbitrary-threshold boundary is documented, and novelty remains a separate gate.

## 7. Preparation and unweighting

Concentration and equal ranks give operator-norm closeness of initial harmonic and embedded logical-kernel projectors. Their normalized mixtures are within trace distance \(\eta\). Prepare the known history mixture to error \(\epsilon\), yielding harmonic-mixture error at most \(\eta+\epsilon\). State the permissible approximation convention; exact free harmonic preparation is not assumed.

For fixed weights choose \(F>0\) with \(f_v=F w(v)^2\) positive integers and polynomial total multiplicity. Use exactly the same labeled copy block for each vertex throughout the filtration. The normalized copy isometries satisfy
\[
\widehat J U_1=U_2J,\qquad \widehat\Delta_iU_i=F U_i\Delta_i.
\]
The imported asymmetric-sector bound excludes extra harmonic vectors. Counts and induced ranks, hence their ratio, are preserved. Arbitrary simplex-count normalization need not be preserved. Variable copy multiplicities across levels already fail a one-vertex commuting-square test.

The previous Pro response proposed extending this to the persistent Laplacian itself. The new conditional local derivation is in PERSISTENT_LAPLACIAN_EXTENSION.md. Its novelty has not been certified; the stronger structural statement still uses the same imported single-level decomposition.

## 8. Promising directions, negative results, and stopping criteria

| Priority | Direction | What exists | What would justify further investment |
| --- | --- | --- | --- |
| Main | True normalized persistence through finite-certificate concentration | Conditional proof accepted; complete fixed real-gate palette certified; end-to-end restricted transfer theorem reviewed; eight-label \(\mathsf{BQP}_1^{G_2}\) source accepted after local and bounded Pro audits | Establish that the instance-uniform finite-certificate estimate and its \(g\)-linear gap dependence exceed the repaired King--Kohler/Hayakawa analysis; the qualitative degenerate-kernel dimension closure is only a short corollary |
| Secondary structural | Simultaneous persistent-Laplacian spectral unweighting | Pro proposal and independent conditional derivation | Source-check the restricted-domain/adjoint step and novelty; seek an additional nontrivial consequence |
| Secondary algorithmic | Quantum epsilon-net and additive barcode approximation | Expected \(\widetilde O(\sqrt{nK})\) point-query upper bound; fixed-scale 1D lower bound | A new parameter tradeoff or matching multi-parameter lower bound beyond known sampling plus stability |
| Direct continuation | Bounded evaluated-Hom width for decomposition | Exact update-rank formula and arbitrary-rank obstruction | A natural non-interval class with provably small evaluated rank and an improved fully charged classical comparison |
| Backup | Quantum hyperbolic structured filtering | Landmark and shell-law obstructions; earlier separate Pro channel | A geometry-specific whole-route or filtering theorem surviving preprocessing and precision costs |

The net theorem assumes coherent whole-point access, a packing bound \(K\), charged predicates and uncomputation, and a classical persistence computation on the net. Barcode error is \(2\epsilon\) in the diameter-threshold Rips convention. A fixed-scale one-dimensional OR construction yields classical \(\Omega(n)\) and quantum \(\Omega(\sqrt n)\) query lower bounds. This is an oracle result; building the input oracle is not free. Novelty against known quantum clustering and classical cover-to-barcode methods is unresolved.

Negative results worth retaining:

- Native Möbius inclusion zigzags have constant local and module-constraint gaps but overlap \(\Theta(m2^{-m})\), while generalized rank is one. This rejects a particular local-gap-to-global-projector inference, not all quantum generalized-rank algorithms.
- A one-direction AIDA candidate exchange can induce rank \(t\) after the actual evaluated Hom quotient, inside a minimal graded presentation with an indecomposable target. The correct parameter is evaluated update rank.
- Equal-complex quasi-persistence hard instances have true normalized persistence one when defined.
- A small guide does not determine the uniform whole-homology survival fraction.
- Positive regularization can erase every exact zero. Uniform replication does not amplify the fraction.
- Fixed-dimensional hyperbolic neighbor-Grover claims lose to appropriate classical indexing or landmark-distance reconstruction; this is not an impossibility theorem for all quantum geometry.
- Largest death coordinate is unstable for an arbitrary approximate barcode; maximum finite bar length is the correct statistic in the outlier reduction.

All seven existing probes were rerun successfully during this consolidation. Their raw outputs are in REPRODUCTION_RESULTS.json. These checks do not certify the imported clique-gadget spectrum, full reduction, source-class hardness, or novelty.

## 9. Requested next research milestone

The source-interface milestone is complete. A targeted local primary-source collision pass is now recorded in [NOVELTY_COLLISION_AUDIT_2026-09-03.md](NOVELTY_COLLISION_AUDIT_2026-09-03.md). It rates the direction **MEDIUM, conditional**. Exact multiplicity and the normalized-persistence definition are prior. King--Kohler already contains much of the arbitrary-geometric-chain machinery, and Gyurik et al. already states a whole-kernel gap in a particular guided construction. The possible novelty is therefore the finite-certificate degenerate-kernel transfer theorem as a reusable result, together with its exact natural filtered-rank application; quotient dimension counting, ordinary min--max, fixed gadgets and the eight-label combiner are excluded from the novelty claim.

The equation-level local comparison in [KING_COROLLARY_BOUNDARY_2026-09-03.md](KING_COROLLARY_BOUNDARY_2026-09-03.md) now shows that the King--Kohler proof yields the qualitative degenerate-kernel theorem by a short final projection argument if its all-chain estimates are uniform. The surviving technical candidate is narrower and sharper: a finite-certificate proof that avoids the growing-rank basiswise-perturbation inference and the padded coordinate-bulk obstruction, while allowing the gadget scale to be chosen independently of the logical gap and producing a final gap linear in \(g\). The running external audit must decide whether Hayakawa's fixed-family repair already supplies an equivalent estimate, whether the Gyurik et al. arbitrary-chain passage is complete, and whether the quotient route materially resolves a restricted case of Lowe et al.'s conjecture. The common-copy unweighting diagram has no identified local obstruction and may upgrade the output to unweighted clique complexes, but it is likely a direct Hayakawa corollary rather than a new mechanism. Padding-generated denominator growth remains the principal impact objection.

Every response, useful failed derivation, correction, dependency change, and verified milestone should be archived before updating conclusions. Raw Pro outputs and adopted results remain separate. MILESTONES.md records the current lifecycle state.
