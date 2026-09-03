# Frozen context for the TDA Pro review and advancement

Repository: https://github.com/jackal092927/ramsey-bounds-reproducible

Prepared for the same existing TDA Pro conversation. The exact Git commit is provided in the dispatch message. Appendix source hashes refer to the original files; relative links in this combined packet are rebased for readability. Current dossier/corrections govern current claims. Later appendices are dated local reports: any original source-check or communication-status wording describes its earlier writing time. The six primary sources still require independent verification as stated in the current ledger.


---

# CURRENT COLLABORATION REQUEST

Repository file: `research/quantum_direction_selection/collaboration/2026-09-02/PRO_REQUEST.md`

SHA-256: `21b7a0086ac499158ad5d688dfe25242a01d5bd775e1573539ae6779f3ef7025`

# Pro collaboration request: first review, then advance the mathematics

Please continue this same TDA collaboration. Our work has progressed substantially beyond the earlier functorial-unweighting packet you reviewed. The attached dossier and appendices supersede that packet on current status. Your earlier response has been preserved verbatim in substance, including your persistent-Laplacian proposal; it is not treated as a correctness certificate.

Our objective is to push the strongest genuine result as far as possible toward a high-quality, impactful theoretical computer science paper. Please do substantive research and proof development, not only recommend future work.

1. **First conduct an adversarial mathematical and novelty review.** Read the exact hypotheses and written derivations. Distinguish actual mathematical failures from source-integration obligations and novelty risk. Check the six primary source claims where they matter and report precisely what you read, versions/sections, and what could not be checked. Do not infer that a theorem is absent merely from its title or abstract.

2. **Then advance the surviving result within this response.** Develop the strongest defensible theorem statement, prove additional useful lemmas or give explicit counterexamples, and investigate a meaningful complexity consequence for the exact supported circuit source. Explore alternatives if the current source is too weak. Treat the target of a strong TCS paper as an ambition, never as an assumed achievement.

3. **Prioritize the load-bearing global concentration theorem.** It concerns arbitrary low-energy geometric chains and proximity to a separate logical kernel. The quotient injection and standard dimension argument then give all zero-mode multiplicities and gaps; no extra global relative-acyclicity assumption is required once those hypotheses hold. Review the actual padding/interface proof and local finite-palette dependencies. Do not certify unseen gadget estimates.

4. **Respect the corrected definitions.** The mixed spectator gives \(U'=U\otimes H^h\) but \(M'=M\otimes I\) for odd and even \(h\). An \(HH\) pair does not change parity. Interface inputs are orthogonal blocks, outputs may be shared. The initial denominator \(D>0\) is fixed by the complete anchored-history construction. Error \(1/24\), not \(1/6\), distinguishes fraction thresholds \(1/2\) and \(1/3\). The NO bound follows from \(f\le p\). Exact logical isometries must not be confused with a demand for exactly compatible geometric harmonic representatives.

5. **Seek stronger consequences without inflating the source class.** The baseline transfers an explicit real-gate, clean-work/mixed-input, off-perfect-eigenvalue-separated promise. Unrestricted SDQC1 equivalence, BQP-hardness from threshold constants, and complex-phase extension are unproved. Investigate an exact reduction or a rigorous boundary. Do not use approximate gate synthesis to preserve exact kernels.

6. **Re-evaluate your persistent-Laplacian proposal and alternatives.** We independently derived the clique-only conditional restricted-domain/direct-sum statement. Assess whether this is new and useful beyond a short corollary, and push it if promising. Consider parameter-sensitive quantum net/barcode theorems or natural bounded evaluated-Hom-width classes only if they offer more substance. Preserve the native Möbius, AIDA update-rank, normalization, and oracle-model obstructions.

Please return (a) a precise status/claim table; (b) a dependency and novelty collision table with primary links; (c) self-contained proofs or counterexamples for real progress achieved; (d) the strongest clean theorem and exact computational model; (e) ranked next steps with finite stopping criteria; and (f) all useful intermediate milestones, including failed approaches and corrected claims. Separate conjectures, conditional theorems, established imported results, and derivations completed here.

No “first quantum persistence”, new-gadget credit for Rudolph's construction, practical/near-term claim, or paper-readiness certification is requested. The geometric gap polynomial is poor. If the best result is only a corollary or an uninformative promise reduction, say that plainly and explain whether a stronger mechanism can actually be proved.

The repository snapshot and file paths are supplied in the dispatch header. Use the attached context if repository access is unavailable; do not claim to have read files you could not access. We will independently evaluate and archive your complete response and useful intermediate conclusions.


---

# CURRENT RESEARCH DOSSIER

Repository file: `research/quantum_direction_selection/collaboration/2026-09-02/RESEARCH_DOSSIER.md`

SHA-256: `6b837473990561de759e5d6517db142dfc70937c7e27993d393e598382e8d949`

# True normalized persistence: research dossier and forward program

Prepared September 2, 2026 PDT. This dossier consolidates the current conversation, the written round-2 derivations, the source ledger, prior failed approaches, and the completed first TDA Pro response. It is the current handoff context, not a submitted manuscript or a certificate of the full reduction.

## 1. Objective and evidence standard

The intended statistic is
\[
q(X_1,X_2)=\frac{\operatorname{rank}[H_d(X_1)\to H_d(X_2)]}{\dim H_d(X_1)},\qquad \dim H_d(X_1)>0.
\]
It is the fraction of initial homology that survives. The target concerns exact zero modes. Neither simplex-normalized Betti numbers nor quasi-low-energy counts substitute for this statistic.

The aim is a high-quality, impactful theoretical computer science paper. The strongest current candidate is a global geometric concentration theorem for a fixed supported gadget palette, leading to exact multiplicities, whole-positive-spectrum gaps, and natural filtered rank transfer. Whether this is new and whether the restricted source yields a meaningful complexity consequence remain open. Quantum persistence and parsimonious homology encodings already exist according to the supplied ledger.

Evidence labels used throughout:

- **LOCAL DERIVATION:** a written mathematical argument; its explicit hypotheses remain part of the statement.
- **IMPORTED:** a cited local gadget or literature theorem; not re-proved by this session.
- **FIXTURE:** a finite exact or numerical implementation check, never an asymptotic proof.
- **ADVISORY:** an external model's proposal or review, requiring independent evaluation.
- **OPEN / RETRACTED:** an unmet obligation or a conclusion explicitly withdrawn.

The primary source ledger was supplied as previously checked locally. This consolidation has read the local reports; it has not independently reread all six primary sources. A completed Pro answer is also not independent source verification by this agent.

## 2. Core finite-palette transfer theorem

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

The local package still includes exact nullity, local kernel convergence, lifted-sector spectral bounds, and a central-relative-bulk singular-value bound. These local assumptions must be source-mapped or proved. They are distinct from adding a global relative-acyclicity hypothesis after the transfer argument. Basiswise closeness in exponentially growing dimension cannot replace an operator-norm estimate; use the fixed local dimension before tensoring.

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

For an arbitrary positive coefficient family, replacing \(\sum_ja_jP_j\) by \(\sum_jP_j\) preserves the kernel and lowers the positive gap by at most \(a_{\max}\). This supports exact rank transfer without a small output coefficient, provided the coefficient bound is polynomial.

With \(m=6\), the geometric exponent is \(4m+2=26\). At the stated parameter scale,
\[
E=\Theta\!\left(\eta^{54}g^{27}/t^{27}\right)
\]
up to the fixed choice of constants. This is a very poor inverse polynomial. Substituting \(g=\Theta(L^{-3})\) still leaves the \(t^{-27}\) factor; no favorable \(L^{-81}\)-only bound is claimed. There is no near-term performance claim.

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
Consequently trace promises \(p\ge a\) and \(p\le b\) yield separated guaranteed fraction ranges only if
\[
\max\{0,(a-r)/(1-r)\}>b.
\]
For \(a=2/3,b=1/3,r=1/3\): YES gives \(f\ge1/2\), NO gives \(f\le1/3\). Additive error must be below \(1/12\); \(1/24\) with decision threshold \(5/12\) works. A trace gap alone fails, as \(M=I/4\) versus \(M=0\) both have \(f=0\).

The minimal theorem is a polynomial transformation from the explicitly specified real-gate circuit promise to a nested weighted clique pair with
\[
\beta_d(X_1)=D,\qquad \beta_d(X_1\to X_2)=\dim S,\qquad q=f,
\]
both whole-positive-spectrum gaps, and an explicitly costed approximate initial harmonic mixture. After the spectator extension both dimensions double, with \(q\) unchanged. A common-copy unweighting corollary is available under its own exact, polynomial multiplicity assumptions.

This transfers the **explicit circuit promise problem**. It does not by itself establish BQP-hardness, unrestricted SDQC1 hardness, or that this restricted problem is outside BPP. Identifying a defensible source-class consequence is a central next task, not a consequence of the numerical thresholds.

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
| Main | True normalized persistence through global concentration | Full abstract quotient argument, written padding repair, supported exact palette, history-gap derivation | Complete the finite-palette dependency audit; isolate a theorem absent from sources; establish a meaningful explicit source reduction |
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

First audit the strongest theorem with the actual written hypotheses and source dependencies. Retract incorrect objections explicitly. Then develop the best surviving route as far as possible: prove additional lemmas, identify counterexamples, sharpen the source model, and deliver a theorem/proof package that could justify a substantial TCS submission. If the main direction collapses to an elementary corollary or an uninformative promise reduction, say so and develop the strongest alternative rather than embellishing the claim.

Every response, useful failed derivation, correction, dependency change, and verified milestone should be archived before updating conclusions. Raw Pro outputs and adopted results remain separate. MILESTONES.md records the current lifecycle state.


---

# SOURCE LEDGER AND DEPENDENCIES

Repository file: `research/quantum_direction_selection/collaboration/2026-09-02/SOURCE_LEDGER.md`

SHA-256: `a7bc7cd0a5edf6368d6728225836aabe62d2c066cf2b11e67a4f203dcae2b44b`

# Source ledger and dependency map

The six-item ledger below was supplied by the user as checked locally. Existing local reports contain prior section-level reading notes. This consolidation read those reports; it did not independently reopen and verify every primary source. The wording below records claims to check, not a newly completed literature audit.

| Source | Reported established content | Boundary for the present work |
| --- | --- | --- |
| [Crichigno–Kohler, Nature Communications 2024](https://www.nature.com/articles/s41467-024-54118-z) | Parsimonious quantum-kSAT-to-clique-homology reduction; satisfying states correspond to holes; #BQP counting hardness | Exact multiplicity by itself is old. No inverse-polynomial gap above a degenerate whole kernel is imported from this item. |
| [King–Kohler, arXiv 2311.17234v2](https://arxiv.org/html/2311.17234v2), FOCS 2024 / [SIAM DOI](https://doi.org/10.1137/24M1710243) | Fixed local spectral gadget and many-gadget NO-case gap when logical \(H\succeq gI\) | A general whole-positive-gap theorem over arbitrary degenerate kernels was not located in the supplied reading. This is not proof of absence. The padded coordinate-bulk estimate has the reported outside-weight-one problem. Use only an explicit supported finite palette. |
| [Gyurik et al., PRX Quantum 7, 020361 (2026)](https://journals.aps.org/prxquantum/pdf/10.1103/gvys-hl8h), [arXiv 2410.21258v2](https://arxiv.org/html/2410.21258v2) | BQP1-hard harmonic survival for a specified pure guide; a particular whole-kernel gap argument | This is not uniform-initial-homology survival fraction. A simulated-register estimate is reportedly invoked on an arbitrary low-energy vector; the independent all-chain proof is intended to avoid relying on that invocation. Do not call the published theorem false without a full audit. |
| [Rudolph, arXiv 2411.02681v2, Appendix D.1](https://arxiv.org/html/2411.02681v2#A4.SS1) | Gain/loss Hadamard split, concrete three-term two-qubit states, and sphere-join closure for fixed guards | These are credited prior ingredients. General integer-state correctness is not inferred. Source-match the concrete displayed vectors and attaching maps. |
| [Lowe–Kim–Bondesan–Hayakawa, arXiv 2607.03278v1](https://arxiv.org/html/2607.03278v1) | NHP Problem 9 and Conjecture 1; Conjecture 2 asks multiplicity, compatible exact harmonic isometries and small output coefficient; exact Hamiltonian result under SDQC1; quasi-TDA DQC1 hardness | The normalization itself is old. Equal-complex quasi hard instances have true NHP one when defined. Definition 2 allows arbitrary thresholds and has explicit gate-set dependence; the trace-to-fixed-space-rank inference needs the threshold restriction described in the dossier. No claim to resolve the unrestricted conjecture. |
| [Hayakawa, arXiv 2608.02726v1](https://arxiv.org/html/2608.02726v1) | Common clique-copy unweighting; Lemma 5.4 register quotient for one projector; Lemma 6.1 outside harmonic tensors; Theorem 6.2 NO-case gap | Those local ingredients are not new. Filtered applications were listed as future work. The proposed extension concerns the full persistent-Laplacian restricted domain and low spectrum, subject to checking priority. |

## Local proof obligations, with owning artifacts

| Obligation | Owner / evidence | Current state |
| --- | --- | --- |
| Independent interior-chain decomposition | ../../round2/NORMALIZED_PERSISTENCE_PROBE.md, abstract proof | Local derivation under exact intersections |
| Exact filling for each palette member | Same file, final weight-gauge/nullity argument; Rudolph and Hayakawa input gadgets | Conditional on exact local nullity and kernel convergence |
| All-chain concentration with term-count-uniform constants | Same file, padding appendix; ../../round2/UNWEIGHTING_AUDIT.md | Written local repair; full independent integration review pending |
| Correct central relative-bulk singular bound and lifted-cycle sector | King–Kohler fixed-size package with explicit palette | Imported dependencies to check line by line |
| Rational projector palette and tensor guards | ../../round2/UNARY_PALETTE_ADDENDUM.md | Explicit local source matching and derivation; imported gadget facts remain |
| Weighted history and both logical gaps | Same addendum, Section 3 | Complete written elementary proof; finite fixtures rerun |
| Mixed-spectator exact single-H extension | RESEARCH_DOSSIER.md, Section 5 | Direct algebra from the supplied definitions |
| Exact positive denominator, preparation error | Palette addendum Sections 3–4 | Construction and explicit approximation budget |
| Natural filtered unweighting | ../../tda_probe/UNWEIGHTING_FIRST_LEMMA.md | Conditional on the stated symmetric/asymmetric spectral package |
| Persistent-Laplacian extension | PERSISTENT_LAPLACIAN_EXTENSION.md | New local conditional synthesis of Pro proposal; priority open |
| Standard-class hardness / impact | Explicit restricted circuit source | Open; not implied by gate names or threshold constants |

Additional sources already identified in the local portfolio include Dey–Xin generalized ranks/unfolding, Dey–Jendrysiak–Kerber decomposition, classical algebraic module-decomposition algorithms, quantum clustering/coreset methods, and cover-based barcode approximation. Their links and exact local model comparisons are retained in the original reports. Pro is asked to verify relevant primary statements, not merely repeat this table.

The completed first Pro response additionally cites [Mémoli–Wan–Wang, persistent Laplacians](https://arxiv.org/abs/2012.02808) and [SIAM DOI](https://doi.org/10.1137/21M1435471). Its claim that the proposed filtered spectral theorem was not found in the literature remains an advisory search report, not established priority.


---

# CORRECTED AUDIT DISPOSITION

Repository file: `research/quantum_direction_selection/collaboration/2026-09-02/AUDIT_CORRECTIONS.md`

SHA-256: `a129006d6eaa94830187c051c9340a6965963023defb2fc6abb02149c5c1c4a8`

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


---

# FULL TRANSFER AND ALL-CHAIN PADDING ARGUMENT

Repository file: `research/quantum_direction_selection/round2/NORMALIZED_PERSISTENCE_PROBE.md`

SHA-256: `e24c51194e75c8810408a7ce823bec391a51d5c3fba10a12d8d00693787b8446`

# True normalized persistence: an exact-kernel transfer lemma

Date: 2026-09-02. Bounded independent probe; no manuscript or external service changed.

**Reading order after the round-2 audit:** the abstract lemma and padding proof below are retained. The unsupported general-integer-palette inference and the ordinary Hadamard-pair implementation in Section G are superseded by [the explicit weighted-history palette addendum](../../round2/UNARY_PALETTE_ADDENDUM.md). Use its bounds $1/(8L^2)$ and $1/(120L^3)$ for that implementation. [Review resolution](../../round2/REVIEW_RESOLUTION.md) separates the logical Hamiltonian from the geometric Laplacian and records the independent review's objections. The final scope is a restricted fixed-gate, standard-threshold reduction, not unrestricted SDQC1 hardness.

## Verdict

**NARROW / pursue one dependency audit, not a new gadget program yet.** There is a concrete route to true normalized persistence that does not require coefficient-sensitive output gadgets or exact equality of harmonic representatives. The key is an exact topological injection plus a low-energy **dimension** bound. Below is a complete abstract proof; applying it to every gadget in the required verifier palette remains to be certified. The follow-up appendix supplies an independent padding repair and restricts the source to a supported exact finite gate set with standard thresholds; it does **not** establish the July paper's unrestricted conjecture or novelty.

The June gap argument contains a stated-domain mismatch: its Lemma 11 concerns simulated-register states, while Lemma 7 invokes it for an arbitrary low-energy state. The argument below is a potential repair using the original arbitrary-state estimates, not an assumption that this mismatch is harmless.

## Source target, precisely

In [Lowe–Kim–Bondesan–Hayakawa, July 2026](https://arxiv.org/html/2607.03278v1), Problem 9 estimates

$$q=\beta_d^{1,2}/\beta_d^1,$$

for a weighted clique filtration, with nonzero initial Betti number and inverse-polynomial gaps above zero at both levels. **Conjecture 1:** this problem is SDQC1-hard. **Conjecture 2:** a polynomial construction transfers nested history Hamiltonians to a clique filtration, preserves whole kernel multiplicities and gaps, and supplies compatible isometries that identify surviving harmonic vectors exactly. Theorem 7 establishes hardness for the Hamiltonian version. Its kernels have dimensions $2^{N-1}$ and $\dim S$, where $S$ is the perfectly accepted input subspace.

Thus normalization by the initial Betti number is **already the source problem**, not a proposed new normalization. Common-multiplicity unweighting preserves both counts and their ratio. The July quasi-hardness construction uses the same complex at both levels and different energy cutoffs; that family has true persistence ratio exactly one whenever its initial Betti number is nonzero.

## Claim and status

**Claim.** For fixed-locality, finite-palette positive-projector Hamiltonians, independent exact-filling gadgets plus a dimension-uniform low-energy estimate imply exact kernel multiplicity, a gap above the entire kernel, and a natural quotient filtration. Consequently the stronger isometric condition in July Conjecture 2 is unnecessary for this rank-transfer step. Establishing its unrestricted rank-hardness Conjecture 1 would additionally require the full source-promise and gate-set reduction, which is not established here.

**Status: PROVABLE AFTER EXPLICIT SOURCE ASSUMPTIONS.** The abstract lemma and its consequences below are proved. The finite-palette gadget assumptions are the remaining source-integration obligation. They must be checked, not replaced by the published decision-hardness theorem.

## Assumptions and notation

Work over $\mathbb C$, in degree $d\geq1$. Let $R$ be a register complex of dimension $d$, and let

$$V=Z_d(R)=H_d(R)\subset C_d(R)$$

have an isometric identification with the simulated Hilbert space. The equality uses $C_{d+1}(R)=0$.

For each index $j$, a gadget complex $Y_j\supset R$ corresponds to an orthogonal projector $P_j$ on $V$, of constant locality. For a term set $A$, form $X_A=\bigcup_{j\in A}Y_j$. Assume:

1. **Independent supports.** Distinct gadgets intersect only inside $R$. In every degree, the chain space is the register plus mutually disjoint non-register gadget coordinates. No simplex uses vertices from two different gadgets.
2. **Exact single-gadget filling.**

   $$B_d(Y_j)\cap V=\operatorname{ran}P_j.$$

3. **Uniform low-energy estimate.** With $t=|A|$, $H_A=\sum_{j\in A}P_j$, and $\Delta_A$ the constructed degree-$d$ Laplacian, every normalized $\sigma$ satisfying $\langle\sigma,\Delta_A\sigma\rangle<E$ obeys

   $$1\leq\langle\sigma,\Pi_V\sigma\rangle-\langle\sigma,H_A^{\rm emb}\sigma\rangle+R(E),$$

   $$R(E)\leq C\left(t\lambda+t^2\lambda^2+tE/\lambda^{4m+2}\right).$$

   Here $H_A^{\rm emb}$ is zero outside $V$, $m$ is a fixed locality bound, and $C$ is independent of the exponentially large register dimension. Polynomial dimension dependence would also suffice after explicitly adjusting parameters.
4. **Hamiltonian promise.** $H_A\succeq g(I_V-P_A)$, where $P_A$ projects onto $K_A=\ker H_A$, and $0<g\leq1$ is a known inverse-polynomial lower bound. This includes $K_A=0$.

The same vertex weights and gadget labels are used at every level. Absent gadget vertices may be isolated initially to obtain a common vertex set; this does not alter degree-$d\geq1$ homology.

**Operator distinction essential to the claim.** $H_A$ acts on the logical register space $V$; $\Delta_A$ acts on the full, larger chain space $C_d(X_A)$. The low-energy assumption concerns *all* vectors of the latter space and their distance to the embedded logical kernel, not their distance to $\ker\Delta_A$, which is initially unknown. The energy threshold depends on $t$, the promised logical gap $g$, and the chosen weight $\lambda$. No term-count-independent gap is asserted.

## Proof strategy and dependency map

Independent gadget boundaries give an exact quotient on register cycles. Low energy forces proximity to the *Hamiltonian* kernel. A subspace larger than that kernel necessarily contains an orthogonal vector; this converts proximity into an exact multiplicity and gap statement. Naturality then follows from quotient maps, without identifying harmonic representatives.

Source facts to audit are limited to assumptions 1–3 and the verifier's fixed projector palette. The remaining linear algebra is below. In [King–Kohler, Sections 8–10](https://arxiv.org/html/2311.17234v2), Section 10.3 explicitly omits inter-gadget edges; the single-gadget construction targets one forbidden subspace; Lemmas 10.2–10.4 state arbitrary-state low-energy bounds. Their combination would imply assumption 3. However, the padding caveat below prevents treating those estimates as independently certified here. That theorem's statement itself only gives a zero-versus-positive-minimum guarantee, not our full multiplicity conclusion.

## Proof

### 1. Positive coefficients can be erased

Let $H_A(a)=\sum_{j\in A}a_jP_j$, with every $a_j>0$, and let $a_{\max}=\max_j a_j$. Positivity gives

$$\ker H_A(a)=\bigcap_{j\in A}\ker P_j=\ker H_A.$$

Indeed, zero energy is equivalent to $\sum_j a_j\|P_jx\|^2=0$. Moreover,

$$H_A\succeq H_A(a)/a_{\max}.$$

The operators have the same kernel, so their positive gaps satisfy

$$\gamma_+(H_A)\geq\gamma_+(H_A(a))/a_{\max}.$$

Therefore polynomially bounded penalty coefficients can be replaced by one without changing kernel counts or destroying an inverse-polynomial gap. No approximation of a small output coefficient is required for exact rank persistence. This argument does not cover negative coefficients or subtraction of an energy shift.

### 2. Independent gadgets give the exact register quotient

Put $W_A=\sum_{j\in A}\operatorname{ran}P_j$. We claim

$$B_d(X_A)\cap V=W_A.$$

The inclusion $\supseteq$ follows from assumption 2. Conversely, if $v\in V$ and $v=\partial c$, decompose $c=\sum_j c_j$ among the non-register $(d+1)$-chains. There are no register $(d+1)$-chains. Since $\partial c$ has no non-register coordinate and those coordinates are disjoint among gadgets, every $\partial c_j$ is supported entirely in $R$. It is a cycle and hence lies in $V$. Assumption 2 yields $\partial c_j\in\operatorname{ran}P_j$, so $v\in W_A$.

Consequently the map $V\to H_d(X_A)$ induced by inclusion has kernel exactly $W_A$. Since

$$K_A=W_A^\perp,$$

this already supplies $r_A=\dim K_A$ linearly independent exact homology classes. By Hodge theory,

$$\dim\ker\Delta_A\geq r_A.$$

This step does **not** assert that the register representatives remain harmonic.

### 3. Low-energy overlap bounds the entire subspace dimension

For any normalized low-energy $\sigma$, assumption 3 gives

$$1-\langle\sigma,\Pi_V\sigma\rangle+\langle\sigma,H_A^{\rm emb}\sigma\rangle\leq R(E).$$

Write $P_A$ also for its embedding into the full chain space. The Hamiltonian gap and $g\leq1$ imply

$$g\bigl(1-\langle\sigma,P_A\sigma\rangle\bigr)\leq R(E).$$

Choose a target $0<\eta<1$, a sufficiently small constant $c$ depending only on $C$, and common parameters satisfying

$$0<\lambda\leq c\eta^2g/t,\qquad E\leq c\eta^2\lambda^{4m+2}g/t.$$

Then $R(E)/g\leq\eta^2$. Every normalized vector in the spectral subspace

$$L_E=\operatorname{ran}{\bf1}_{[0,E)}(\Delta_A)$$

has squared projection at least $1-\eta^2>0$ onto the $r_A$-dimensional space $K_A$. Thus $P_A|_{L_E}$ is injective and

$$\dim L_E\leq r_A.$$

Step 2 supplies at least $r_A$ exact zero modes inside $L_E$. Hence

$$\boxed{\dim\ker\Delta_A=r_A,\qquad\gamma_+(\Delta_A)\geq E.}$$

For $r_A=0$, the same argument says $L_E=0$. This is an exact counting argument; **no near-zero eigenvalue has been relabelled as zero**.

### 4. Nested term sets produce the required true persistence

Step 2's injection $V/W_A\to H_d(X_A)$ is now an isomorphism by the dimension equality. For $A\subseteq B$, the inclusion map therefore fits the natural quotient map

$$V/W_A\longrightarrow V/W_B.$$

It is surjective. In particular,

$$\beta_d(X_A)=\dim K_A,\qquad\beta_d^{A,B}=\dim K_B,$$

and, when $K_A\ne0$,

$$\boxed{\frac{\beta_d^{A,B}}{\beta_d(X_A)}=\frac{\dim\ker H_B}{\dim\ker H_A}.}$$

This is the exact quantity in July's Hamiltonian hardness reduction. Shared parameters may use the maximum number of terms and the minimum promised gap over both levels. A dyadic $\lambda$ within a constant factor of the bound suffices; its denominator is polynomial for fixed locality and inverse-polynomial $\eta,g$.

### 5. Harmonic angles need not be exact, but are controllable

Let $Q_A$ project onto $\ker\Delta_A$. Step 3 implies $\|(I-P_A)Q_A\|\leq\eta$; equal ranks imply $\|Q_A-P_A\|\leq\eta$. For nested term sets, $P_B\leq P_A$. Thus every unit $y\in\operatorname{ran}Q_B$ satisfies

$$\|(I-Q_A)y\|\leq2\eta.$$

Consequently all eigenvalues of $Q_BQ_AQ_B$ on $\operatorname{ran}Q_B$ are at least $1-4\eta^2$. This supplies the large-overlap promise for constant $\eta<1/2$ without asserting $J E_A=E_B$ on surviving vectors.

Efficient preparation of a maximally mixed *harmonic* subspace is a separate input-access promise. A circuit preparing the simulated history mixture is not literally the same circuit. Because $\|Q_A-P_A\|\leq\eta$, their normalized maximally mixed states have trace distance at most $\eta$; choosing inverse-polynomial $\eta$ allows the usual approximate state-preparation convention. An exact-preparation formulation needs an additional construction or a revised promise, and is not silently assumed here.

## Strongest remaining checks

1. **Exact single-gadget kernel, for the complete fixed verifier palette.** Verify $B_d(Y_j)\cap V=\operatorname{ran}P_j$ rather than merely existence/nonexistence of one hole. Tensor padding and the complete gate set must be covered. This is the smallest topological obligation; the many-gadget part is proved above.
2. **Uniform constants and a padding flaw in the local spectral estimates.** The general basiswise perturbation definition in KK Definition 7.7 does not, in growing dimension, by itself imply a dimension-free projector-norm estimate. The fixed-size gadget can avoid that problem: establish the bound in constant dimension and then use $\|A\otimes I\|=\|A\|$. More seriously, the parallel TDA audit found that KK Claim 10.2's literal $O(\lambda)$ bound for the padded coordinate-bulk boundary fails: removing a weight-one outside-register vertex can remain inside that bulk. The candidate repair replaces coordinate bulk by **local bulk tensored with the outside-register harmonic subspace**, so the outside boundary and coboundary vanish. The parallel derivation proposes the slightly weaker remainder $C(t\lambda+t^2\lambda^2+tE/\lambda^{4m+2})$ used above. That repair, including its cross-gadget interface bound, still needs line-by-line certification. The present lemma deliberately assumes the estimate and does not certify it.
3. **Exact source palette and realification.** Coefficient erasure preserves kernels but does not turn arbitrary complex irrational local states into the supported integer-state projectors. Check the SDQC1 verifier construction against the gadget palette, with any multiplicity-doubling realification accounted for in numerator and denominator.
4. **June source repair.** [Lemma 11 and Lemma 7](https://arxiv.org/html/2410.21258v2) have the domain mismatch identified above. The present argument needs the arbitrary-state KK estimates directly, not the restricted Lemma 11. No unreviewed unfolding manuscript was used as a theorem.
5. **Unweighting is downstream.** If the weighted family passes these checks, apply the shared-multiplicity lemma in the local `UNWEIGHTING_FIRST_LEMMA.md`: fixed dyadic weights, common multiplicities, and polynomial blowup preserve the exact harmonic ranks and persistence maps. It cannot repair a failed weighted construction.

## Cheap obstructions to alternative shortcuts

- **Quasi to true by threshold adjustment:** on the existing equal-complex quasi-hard family, true normalized persistence is identically one. Unweighting or duplication does not create a nontrivial filtration map.
- **Low-rank guide in place of a uniform initial mixture:** in $\mathbb C^D$, a guide supported on an $r$-dimensional subspace $G$ gives identical unit overlap with target kernels $G$ and $\mathbb C^D$, whereas their normalized ranks are $r/D$ and $1$. This is an information-theoretic obstruction to recovering the whole rank from those guide overlaps alone, not a graph-oracle lower bound.
- **Positive regularization:** replacing $H$ by $H+\epsilon I$ for any $\epsilon>0$ erases every zero mode. Approximation quality in operator norm does not preserve Betti numbers.
- **Uniform multiplicity replication:** multiplying both kernel counts by the same factor leaves their ratio unchanged. It does not amplify a small normalized counting signal.

## Exact classical baseline

This problem is polynomial-time in the explicitly listed relevant simplices. Let $Z_1$ be a matrix whose columns form a basis of $\ker\partial_d^{X_1}$, embedded in $C_d(X_2)$, and let $B_2$ be the matrix of $\partial_{d+1}^{X_2}$. Then

$$\beta_d^{1,2}=\operatorname{rank}[Z_1\ B_2]-\operatorname{rank}B_2,$$

$$\beta_d^1=\dim\ker\partial_d^{X_1}-\operatorname{rank}\partial_{d+1}^{X_1}.$$

Gaussian elimination gives an unconditional exact $O(S^3)$ arithmetic-operation baseline, with $S$ the total number of relevant simplices; bit complexity must be added for exact arithmetic. For an $n$-vertex graph, enumeration and this linear algebra cost $n^{O(d)}$, so fixed $d$ is polynomial. These are transparent baselines, not a claim to the fastest known classical implementation. Quantum hardness concerns the succinct graph input with growing $d$, and any algorithmic advantage must state its gap, guide-access, and accuracy promises.

## Smallest next lemma / stop rule

Ask for a source-certified **finite-palette register-boundary lemma**:

> For every constant-local projector in the exact SDQC1 verifier palette, the KK gadget has $B_d(Y_j)\cap H_d(R)=\operatorname{ran}P_j$, and its padded arbitrary-state low-energy estimate has polynomially uniform constants.

If this holds, the proof above supplies multiplicity, two-level gaps, natural rank persistence, and a constant harmonic-angle promise. If it fails, isolate one explicit unsupported projector or boundary relation before designing a replacement. Do not spend a new project on coefficient-sensitive gadgets until this cheaper route is ruled out. If all dependencies already appear explicitly in the published KK version, the result may be a short corollary resolving the July conjecture rather than a new general mechanism; novelty remains unassessed.

## Follow-up: independent identity-padding repair

Status: **PROVABLE AFTER THE FIXED-SIZE LOCAL GADGET HYPOTHESES.** This section independently checks the many-gadget interference step in the companion `UNWEIGHTING_AUDIT.md`. No simultaneous global outside-register decomposition is assumed. The normalized-persistence conclusion remains conditional on the exact finite projector palette and single-gadget topology.

### A. Single-gadget invariant sectors, not a global decomposition

For gadget $i$ on $m_i$ qubits, put $Y_i=Y_i^{\rm loc}*R_i^{\rm out}$, with $r_i=n-m_i$, $q_i=2r_i-1$, and $p=2n-1$. On augmented chains,

$$C_k(Y_i)=\bigoplus_{a+b=k-1}C_a(Y_i^{\rm loc})\otimes C_b(R_i^{\rm out}),$$

$$\partial(x\otimes y)=\partial_{\rm loc}x\otimes y+(-1)^{a+1}x\otimes\partial_{\rm out}y,$$

$$\Delta_{Y_i}=\Delta_{\rm loc}\otimes I+I\otimes\Delta_{\rm out}.$$

The fixed register factor has augmented harmonic space only in degree one, and has a positive spectral gap $\delta_R>0$ on its orthogonal complement. Tensor-sum positivity shows that the $r_i$-fold register join has harmonics only in degree $q_i$, with the same lower bound $\delta_R$ on every nonharmonic mode, independent of $r_i$. For $r_i=0$, use the augmented join unit in degree $-1$.

In degree $p$, the only possible bidegrees are $(2m_i-1,q_i)$ and $(2m_i,q_i-1)$. Thus every outside-nonharmonic mode belongs to a constant-gap single-gadget sector $A_i$, regardless of its local energy. This assertion concerns $\Delta_{Y_i}$ only. The full many-gadget Laplacian need not commute with gadget $i$'s outside harmonic projector.

### B. Exact interface bound controls every other gadget

Let $\Pi_0^k$ project onto register coordinates and $\Pi_j^k$ onto coordinates containing new vertices of gadget $j$. Define

$$L_j=\Pi_0^{p-1}\partial\Pi_j^p.$$

Only a simplex containing **exactly one** new gadget vertex $u$ can contribute to $L_j$: the boundary must delete $u$ to land in the register. This has coefficient $\lambda$. For a fixed $u$, deletion is a signed partial isometry $D_u$ from an orthogonal input block. Therefore, writing $N_j$ for the number of new vertices of gadget $j$,

$$L_j=\lambda[\,D_u\,]_{u\in V_j^{\rm new}},\qquad
L_jL_j^\dagger=\lambda^2\sum_u D_uD_u^\dagger\preceq\lambda^2N_j I.$$

The fixed finite palette has $N_j\leq N_*$, a constant. Even with overlapping qubit supports and all outside bidegrees present,

$$\left\|[\,L_j\,]_{j\ne i}\right\|\leq\lambda\sqrt{\sum_{j\ne i}N_j}\leq\lambda\sqrt{N_*t}.$$

For a normalized full state $\sigma$ with energy at most $E$, let $x_i=(\Pi_0^p+\Pi_i^p)\sigma$. Up-boundary outputs split by gadget, and non-register down-boundary outputs are disjoint. The register down-boundary discrepancy is exactly $\sum_{j\ne i}L_j\Pi_j^p\sigma$. Hence

$$\langle x_i,\Delta_{Y_i}x_i\rangle\leq C(E+t\lambda^2),\qquad
\|A_i x_i\|\leq C(\sqrt E+\lambda\sqrt t).\tag{A1}$$

This proves the needed control of outside-nonharmonic modes despite cross-gadget mixing; it does not try to rule out that mixing.

### C. Correct projected bulk estimate

Let $P_{{\rm out},i}$ project onto outside harmonics in degree $q_i$. Let $P_{{\rm bulk},i}^{a}$ be the coordinate projector onto local simplices containing the gadget's central vertex. Define

$$Q_i^k=P_{{\rm bulk},i}^{\,k-q_i-1}\otimes P_{{\rm out},i}$$

on that bidegree and zero elsewhere, and put

$$T_i=(Q_i^{p-1}\partial_i,\ Q_i^{p+1}d_i).$$

Harmonicity gives $P_{{\rm out},i}\partial_{\rm out}=P_{{\rm out},i}d_{\rm out}=\partial_{\rm out}P_{{\rm out},i}=d_{\rm out}P_{{\rm out},i}=0$, with degrees understood. Thus the outside differential disappears on both sides. All remaining local matrix entries entering the central bulk have a factor $\lambda$; the local matrix dimension is constant. Consequently

$$\|T_i\|\leq C\lambda.$$

The local central-bulk relative chain complex has no degree-$(2m_i-1)$ homology. Its projected boundary/coboundary pair is therefore injective in that degree. For the fixed palette its least singular value before multiplying by $\lambda$ is a positive constant. Tensoring with outside harmonics preserves singular values, giving

$$\|T_iQ_i^p x\|\geq c\lambda\|Q_i^p x\|.\tag{A2}$$

The ranges of $Q_i^{p\pm1}$ contain a new vertex of gadget $i$. Other gadget chains cannot contribute to them under either differential. Therefore

$$T_i x_i=(Q_i^{p-1}\partial\sigma,\ Q_i^{p+1}d\sigma),\qquad \|T_i x_i\|\leq\sqrt E.$$

This is the exact reason the corrected projection works even when $P_{{\rm out},i}$ and $P_{{\rm out},j}$ refer to different qubit sets.

### D. Closing the bulk and concentration bounds

Use the fixed-size spectral projectors $A_i,B_i,F_i$ for high, bulk, and low sectors, respectively. Here $F_i$ combines the harmonic and lifted-constraint sectors. After padding,

$$A_i+B_i+F_i=I_i,\quad \|B_i-Q_i^p\|\leq C\lambda,\quad
\|Q_i^pF_i\|\leq C\lambda,\quad \|T_iF_i\|\leq C\lambda^{2m_i+1}.$$

The last estimate follows from the full single-gadget low-sector energy, not an assumption that all low vectors are harmonic. Write $Q=Q_i^p$. The identity

$$I_i=Q+(I_i-Q)A_i+(I_i-Q)B_i+F_i-QF_i$$

together with (A1)–(A2) yields

$$c\lambda\|Qx_i\|\leq\sqrt E+C\lambda\|A_ix_i\|+C\lambda^2,$$

$$\|B_ix_i\|\leq C(\sqrt E/\lambda+\lambda\sqrt t).$$

Thus

$$\sum_i\|A_ix_i\|^2\leq C(tE+t^2\lambda^2),\qquad
\sum_i\|B_ix_i\|^2\leq C(tE/\lambda^2+t^2\lambda^2).$$

For the lifted constraint sector, use the exact local cycle property: the one-dimensional first lifted eigenspace has nonzero overlap with the register constraint cycle; its spectral projector preserves cycles, so it consists of cycles. Padding with outside harmonics retains that property. Its energy is therefore entirely up energy. Since up energy splits over gadgets, the sum of lifted-sector masses is at most $CE/\lambda^{4m+2}$, with $m=\max_i m_i$ and $\lambda\leq1$.

Finally the kernel projector for gadget $i$ is within $C\lambda$ of the embedded projector onto $\ker P_i$. This is proved locally in constant dimension and then tensored, never inferred from basiswise closeness in exponential dimension. Summing the complete-projector identity gives exactly

$$1\leq\langle\sigma,\Pi_V\sigma\rangle-\langle\sigma,H^{\rm emb}\sigma\rangle
+C(t\lambda+t^2\lambda^2+tE/\lambda^{4m+2}).$$

This independently establishes assumption 3 from the fixed-size local spectral and relative-bulk hypotheses. The literal full-coordinate padded Claim 10.2 is unnecessary and remains false. No additional global sector-invariance assumption was introduced.

## Follow-up: restrict the hardness source and remove amplification

The exact gate set matters. For the normalized-counting target, fix the rational real set $G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}$ and the corresponding finite integer-state projector palette. Do not conclude hardness for every gate-set-dependent formulation of SDQC1. This is distinct from the June harmonic-guide reduction's four-local Pythagorean palette. The construction below has locality at most six; use $4m+2$, not the June exponent $18$.

### E. The correct acceptance-to-rank thresholds

Let $M$ be the acceptance operator on the $D$-dimensional valid input space. Assume $S=\ker(I-M)$ is its perfectly accepted subspace, and that $M|_{S^\perp}\preceq rI$. Put $f=\dim S/D$ and $p=\operatorname{Tr}M/D$. Then

$$f\leq p\leq r+(1-r)f.$$

If YES has $p\geq a$ and NO has $p\leq b$, exact kernel fractions separate only when

$$\frac{a-r}{1-r}>b.$$

An inverse-polynomial $a-b$ by itself is insufficient. In particular, with the standard promise

$$a=2/3,\quad b=1/3,\quad r=1/3,$$

we get YES $f\geq1/2$ and NO $f\leq1/3$, a gap of $1/6$. An additive rank-ratio estimate with error less than $1/12$ decides this restricted source promise. No amplification or gate-palette change is needed. For thresholds below $r$, two distinct acceptance probabilities can both have $S=0$ and identical zero kernel fraction.

### F. Direct both-kernel gap for the history Hamiltonians

Here is an elementary general lemma. Suppose $H_1\succeq g_1(I-P_K)$ with $0<g_1\leq1$, $Q$ is an orthogonal projector, $S=K\cap\ker Q$, and

$$P_KQP_K\succeq\alpha(P_K-P_S),\qquad 0<\alpha\leq1.$$

Then

$$\ker(H_1+Q)=S,\qquad
\gamma_+(H_1+Q)\geq\frac{\alpha g_1}{2g_1+3}\geq\frac{\alpha g_1}{5}.$$

Proof: for a unit $\psi\perp S$, write $\psi=x+y$ with $x\in K\ominus S$, $y\perp K$, and set $e=\langle\psi,(H_1+Q)\psi\rangle$. Then $g_1\|y\|^2\leq e$ and $\|Q\psi\|^2\leq e$. Also

$$\alpha\|x\|^2\leq\|Qx\|^2\leq2\|Q\psi\|^2+2\|Qy\|^2\leq2e+2e/g_1.$$

Thus $1\leq e(2g_1+2+\alpha)/(\alpha g_1)$, giving the displayed bound. Positivity gives the exact kernel identity.

For a uniform history encoding with $L$ legal clock positions, $K$ is the space of valid input histories and

$$P_K H_{\rm out}P_K\cong (I-M)/L.$$

The restricted source promise gives $\alpha=(1-r)/L=2/(3L)$ off $S$, so the second Hamiltonian has an inverse-polynomial positive gap whenever $H_1$ does, regardless of $\dim S$. The following explicit implementation supplies the needed locality and first gap.

### G. Explicit six-local unary-clock implementation

**Superseded as a source-certified palette.** This ordinary unitary-clock calculation explains locality but the fact that its vectors have integer amplitudes does not prove that all needed gadgets exist. Use `UNARY_PALETTE_ADDENDUM.md` for the certified replacement: consecutive gain/loss Hadamard steps from Rudolph's construction, explicit supported three-term states, and the adjusted weighted-path bounds. Do not use the unmodified Hadamard-pair vectors as an imported gadget theorem.

For $T$ circuit gates, let $L=T+1$ and use legal clock strings $|t\rangle=|1^t0^{T-t}\rangle$, $0\leq t\leq T$. Set

$$H_{\rm clock}=\sum_{j=1}^{T-1}|01\rangle\langle01|_{j,j+1}.$$

For interior transition $t$, the clock block on positions $(t-1,t,t+1)$ changes from $100$ to $110$. Introduce rank-one local propagation projectors onto

$$|\phi_{t,z}\rangle=\frac{|100\rangle|z\rangle-|110\rangle U_t|z\rangle}{\sqrt2},$$

for every computational basis string $z$ on the at-most-three work qubits of gate $U_t$. At the ends, fix sentinel clock bits $b_0=1$, $b_{T+1}=0$ and omit them from the actual support. The vectors are orthonormal for fixed $t$, so their sum gives the usual positive propagation term. The legal clock span is invariant under each term; Hermiticity makes its orthogonal complement invariant as well. Illegal strings have clock energy at least one.

All matrices in $G_2$ have rational entries. The finitely many vectors $\phi_{t,z}$ therefore become integer-amplitude vectors after multiplying by a common denominator and renormalizing. Their locality is at most three clock plus three work qubits, hence $m\leq6$. Clock, input, and output terms are computational-basis projectors of smaller locality. The resulting gadget palette is finite and independent of circuit length.

Penalize each invalid initially fixed work bit, conditioned on clock bit one being zero; within the legal clock span this is exactly time zero. Penalize rejection conditioned on the last clock bit being one; within the legal span this is exactly time $T$. These terms are diagonal in the clock and preserve the legal/illegal split.

After conjugating the legal block by $\sum_t|t\rangle\langle t|\otimes U_t\cdots U_1$, the first Hamiltonian is

$$H_1^{\rm legal}=\frac12\sum_{t=1}^{T}(|t\rangle-|t-1\rangle)(\langle t|-\langle t-1|)\otimes I
+|0\rangle\langle0|\otimes A_{\rm in},$$

where $A_{\rm in}$ is the sum of invalid-input-bit projectors and has eigenvalues zero or at least one. Its zero space is precisely the uniform clock tensored with valid inputs. The unanchored path has positive gap at least $c/L^2$. On an invalid-input sector, for any clock-vector sequence $f_t$,

$$\sum_{t=0}^{T}\|f_t\|^2\leq2L\|f_0\|^2+2LT\sum_{t=1}^{T}\|f_t-f_{t-1}\|^2
\leq4L^2\left(\|f_0\|^2+\frac12\sum_{t=1}^{T}\|f_t-f_{t-1}\|^2\right).$$

Together with the illegal sector bound this gives the explicit safe lower bound

$$g_1\geq\frac1{4L^2}.$$

Using the lemma in Section F with $\alpha=2/(3L)$ gives

$$g_2\geq\frac1{30L^3}.$$

Both bounds hold above the entire kernel, including exponentially degenerate kernels. The exact kernel fractions distinguish the restricted source thresholds in Section E without amplification. For the unweighting/concentration step one may take $m=6$, producing the safe exponent $4m+2=26$; a smaller locality should be claimed only after an explicit alternate clock construction.

### H. Exact filling follows from the same local spectral package

The parallel TDA audit supplied the following additional observation, independently checked here. It removes a separate surgery-proof obligation from assumption 2, conditional on the same fixed-size nullity and kernel-limit facts already used for the spectral argument.

For one padded gadget, write $W_k(\lambda)$ for the diagonal operator multiplying a simplex by the product of its vertex weights. Weighted boundary matrices satisfy

$$\partial_w=W_{p-1}^{-1}\partial_1W_p,\qquad B_p(w)=W_p^{-1}B_p(1).$$

All register weights are one, so $W_p|_V=I$. Thus the subspace

$$Z_j=B_p(w)\cap V$$

is independent of $\lambda>0$. Every $v\in Z_j$ is orthogonal to the single-gadget harmonic space for every $\lambda$. The fixed-size kernel convergence, padded with outside harmonics, is

$$P_{\ker\Delta_j(\lambda)}\longrightarrow\Pi_V-\Phi_j\quad\text{as }\lambda\to0,$$

where $\Phi_j$ is the embedded forbidden projector. Passing to the limit shows $Z_j\subseteq\operatorname{ran}\Phi_j$. On the other hand, the known single-gadget nullity is $\dim V-\operatorname{rank}\Phi_j$. The inclusion map $V\to H_p(Y_j)$ must therefore have a kernel of dimension at least $\operatorname{rank}\Phi_j$. Its kernel is exactly $Z_j$. Hence

$$Z_j=\operatorname{ran}\Phi_j,$$

and the register map is surjective. This proves exact single-gadget filling from local nullity, local kernel convergence, and the weight gauge. It neither sets $\lambda=0$ in the graph problem nor labels any positive eigenvalue as zero.

**Final round-2 boundary:** the companion weighted-history addendum replaces the unsupported generic palette by explicitly supported small states and their product guards. The fixed-gadget spectral/nullity/relative-bulk results remain cited literature dependencies; the many-gadget repair and exact filling deduction are local arguments. The arbitrary-threshold/gate-set extension remains explicitly excluded. This is a reduction from a precisely stated fixed-gate circuit promise, conditional on those imported local results, not an assertion of the unrestricted SDQC1-hardness conjecture. Novelty and full source integration remain to be independently reviewed.


---

# SUPPORTED PALETTE AND WEIGHTED HISTORY PROOF

Repository file: `research/quantum_direction_selection/round2/UNARY_PALETTE_ADDENDUM.md`

SHA-256: `3583f697747ec81793d15130803c7e50fe9586a23c8bec7c9dc4b30ec28947e1`

# Certified local palette for a weighted unary history

2026-09-02. Bounded source audit and local derivation. This addendum replaces the unsupported “finite integer palette implies a proved gadget” inference in Section G of `NORMALIZED_PERSISTENCE_PROBE.md`. It does not replace the fixed-gadget spectral theorem or claim unrestricted gate-set hardness.

## Verdict and exact source boundary

The unary construction **survives after replacing each Hadamard-pair transition by two explicitly specified transitions**. Every resulting rank-one constraint is a product of computational-basis factors with a previously checked one- or two-qubit state. No general integer-state gadget theorem is needed.

**VERIFIED SOURCE.** [King–Kohler, Section 5 and Lemma 9.1](https://arxiv.org/html/2311.17234v2) distinguishes the conjectural general integer-state construction from the spectral theorem for a correctly implementing Section-8.2 gadget. [Rudolph, Appendix D.1](https://arxiv.org/html/2411.02681v2#A4.SS1) supplies concrete two-qubit states, reports their algebraic homology checks, and proves closure under tensor products by joining the implementing spheres and their maps. Its footnote 17 explicitly warns that the more general construction lacks a correctness proof. [Hayakawa, Lemma 5.4](https://arxiv.org/html/2608.02726v1#S5) likewise uses the concrete family and join closure. These statements support the restricted palette below, not all six-qubit integer states.

Version status: Rudolph was checked in arXiv v2, 11 April 2025. The [current arXiv record](https://arxiv.org/abs/2411.02681) displays no journal reference; no claim of journal-publication verification is made. The August source is a preprint. The published June source and its separate proof-domain issue are audited in `UNWEIGHTING_AUDIT.md`.

## 1. Explicit positive local terms

Write $H=2^{-1/2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ and $K=\sqrt2H$, so $K=K^\dagger$ and $K^2=2I$. The two active registers below are the changing unary clock bit $c$ and one work bit. Define four normalized forbidden vectors

$$
\begin{aligned}
u_0&=(|00\rangle+|01\rangle-|10\rangle)/\sqrt3,\\
u_1&=(|00\rangle-|01\rangle-|11\rangle)/\sqrt3,\\
d_0&=(|00\rangle-|10\rangle-|11\rangle)/\sqrt3,\\
d_1&=(|01\rangle-|10\rangle+|11\rangle)/\sqrt3.
\end{aligned}
$$

Equivalently,

$$u_z=(|0\rangle K|z\rangle-|1\rangle|z\rangle)/\sqrt3,
\qquad d_z=(|0\rangle|z\rangle-|1\rangle K|z\rangle)/\sqrt3.$$

Each pair is orthonormal: its Gram matrix is $(K^2+I)/3=I$. Therefore $P_\uparrow=\sum_z|u_z\rangle\langle u_z|$ and $P_\downarrow=\sum_z|d_z\rangle\langle d_z|$ are orthogonal projectors, not an indefinite formal propagation expression.

For a two-time state $|0\rangle f_0+|1\rangle f_1$,

$$\langle P_\uparrow\rangle=\|Kf_0-f_1\|^2/3,
\qquad \langle P_\downarrow\rangle=\|f_0-Kf_1\|^2/3.$$

Thus the up edge enforces $f_1=\sqrt2Hf_0$, and the down edge enforces $f_1=Hf_0/\sqrt2$. Apply the up edge on work bit one and then the down edge on work bit two. The composite transfer is exactly $H\otimes H$; the intermediate norm is multiplied by $\sqrt2$ and the final norm returns to its initial value. These are exact identities over rational projector matrices. The gain/loss factorization itself already appears in Rudolph's Appendix D.1 and is credited to that source; our contribution here is its explicit adaptation and analysis for this weighted unary counting history.

For an interior unary transition, tensor the active forbidden vector with $|1\rangle$ on the preceding clock bit and $|0\rangle$ on the following clock bit, and permute tensor factors into the register order. End sentinels are omitted. The resulting Hadamard terms have locality at most four.

For $X$, $\mathrm{CX}$, and $\mathrm{CCX}$, retain the usual vectors

$$ (|0,z\rangle-|1,Uz\rangle)/\sqrt2.$$

For each individual basis string $z$, these gates either leave all work bits unchanged or flip only the target bit. Consequently the vector factors into fixed basis bits and a one-qubit difference, or an active two-qubit two-term state. In particular, a Toffoli term does not require an arbitrary entangled six-qubit gadget. Its fixed controls and two unary guards give total locality at most six. Clock, input, and output penalties are basis projectors.

## 2. Exact match to the checked states; what is being joined

After its fixed factor is removed, Rudolph's displayed $h_{23}$ pair is

$$a=|10\rangle+|11\rangle-|00\rangle,
\qquad b=|10\rangle-|11\rangle-|01\rangle.$$

Our down pair is $-a,-b$, and our up pair is $X_c a,X_c b$, with common normalization $\sqrt3$. Exchanging a logical register's zero and one cycles is a relabeling of its two bowtie petals; a global sign does not change a projector. This identification uses the $h_{23}$ pair and does **not** depend on the apparently inconsistent second vector in the source's displayed $h_{12}$ list.

The tensor-product operation applies to the **implementing spheres and attaching maps**, not to a disjoint union of already filled graphs. If $K_i$ triangulates $S^{2m_i-1}$ and maps to the encoded cycle for $\phi_i$, then $K_1*K_2$ is a clique sphere of dimension $2(m_1+m_2)-1$ and maps to the cycle for $\phi_1\otimes\phi_2$. Applying the standard thickening/coning construction to this joined input implements the product constraint. Basis factors use the elementary one-qubit cycle sphere. Only a constant number of joins is needed for any term.

Therefore this is a fixed, constructible finite family of correctly implementing Section-8.2 gadgets. The imported single-gadget spectral package applies with the **total support locality**, not merely the active two-qubit size. The safe common exponent remains

$$\kappa=4m_{\max}+2=26.$$

This closes the palette-scope gap. It is not a new independent proof of King–Kohler's spectral-sequence theorem or of the source's finite algebraic gadget calculations. Those are explicit literature dependencies, as in the preceding audit.

## 3. Weighted-path gaps and unchanged kernel fractions

This section is a **LOCAL DERIVATION**, algebra-checked independently by the root. Let $L$ count legal clock positions after the split. Let $s_t=\sqrt2$ immediately after an up edge and $s_t=1$ otherwise; no other gate is inserted between the paired up and down edges. Put $Z=\sum_t s_t^2$, so $L\leq Z\leq2L$ and $s_0=s_{L-1}=1$.

Let $V_t$ be the unitary prefix with the scalar factors removed. A history for valid input $v$ is

$$\mathcal Vv=Z^{-1/2}\sum_{t=0}^{L-1}s_t|t\rangle V_tv.$$

This is an isometry because every $V_t$ is unitary and $Z$ is input-independent. Its final prefix equals the original $G_2$ verifier exactly.

For a general legal-clock state write $f_t=s_tV_t\xi_t$. This is a change of variables, not a unitary similarity: the norm becomes weighted. Every split-Hadamard edge contributes $(2/3)\|\xi_t-\xi_{t-1}\|^2$; every ordinary unitary edge contributes $(1/2)\|\xi_t-\xi_{t-1}\|^2$. Indeed, an up edge starts with $s_{t-1}=1$ and ends with $s_t=\sqrt2$, whereas its immediately following down edge starts with $s_{t-1}=\sqrt2$ and ends with $s_t=1$. The gain/loss pair is consecutive, so every ordinary edge has both endpoint scales one. This proves the asserted coefficients without assuming that scalar factors commute with an arbitrary clock reordering.

Put $w_t=s_t^2\in[1,2]$, $W=\sum_tw_t=Z$, and let $A_{\rm in}$ be the sum of invalid initially fixed-bit projectors. For any legal state, its squared norm and quadratic-form energy are exactly

$$N(\xi)=\sum_tw_t\|\xi_t\|^2,\qquad
E(\xi)=\sum_{t=1}^{L-1}c_t\|\xi_t-\xi_{t-1}\|^2
       +\langle\xi_0,A_{\rm in}\xi_0\rangle,
\qquad c_t\in\{1/2,2/3\}.$$

Let $C=\ker A_{\rm in}$ be the clean input subspace and let $B=C^\perp$ be its dirty complement. The input penalty satisfies $A_{\rm in}|_B\succeq I_B$. In these prefix-rotated coordinates, the projectors onto $C$ and $B$ are the same at every time. Thus $\xi_t=\xi_t^C+\xi_t^B$ gives an orthogonal splitting of both $N$ and $E$, although the corresponding work subspaces in the original coordinates are $V_tC$ and $V_tB$.

The zero-energy states are precisely the histories of $v\in C$: every edge forces $\xi_t=v$ and the anchor forces $v\in C$. A legal state orthogonal to all these histories satisfies the **weighted** clean-sector mean condition

$$\sum_tw_t\xi_t^C=0,$$

since its inner product with $\mathcal Vv$ is $W^{-1/2}\langle v,\sum_tw_t\xi_t\rangle$.

For the clean sector, set $D_C=\sum_{t=1}^{L-1}\|\xi_t^C-\xi_{t-1}^C\|^2$. Weighted variance and the path Cauchy--Schwarz inequality give

$$\begin{aligned}
N_C
 &=\frac1{2W}\sum_{i,j}w_iw_j\|\xi_i^C-\xi_j^C\|^2\\
 &\leq\frac{W(L-1)}2D_C
 \leq L^2D_C\leq2L^2E_C.
\end{aligned}$$

Here $\|\xi_i^C-\xi_j^C\|^2\leq |i-j|D_C\leq(L-1)D_C$ and $W\leq2L$. The identity uses the weighted mean condition; ordinary unweighted orthogonality would not suffice.

For the dirty sector put $D_B=\sum_{t=1}^{L-1}\|\xi_t^B-\xi_{t-1}^B\|^2$ and $a=\|\xi_0^B\|^2$. For every $t$,

$$\|\xi_t^B\|^2\leq2a+2(L-1)D_B.$$

Consequently, for $L\geq1$,

$$N_B\leq4La+4L(L-1)D_B
       \leq8L^2(a+D_B/2)\leq8L^2E_B.$$

No mean condition is used here. Adding the two sectors proves $N\leq8L^2E$ on the orthogonal complement of the entire legal kernel, including if $C=0$. Hence the safe bound is

$$\gamma_+(H_1)\geq1/(8L^2).$$

The local clock guards preserve the legal-clock subspace; Hermiticity preserves its orthogonal complement. Illegal clock strings have energy at least one from the clock penalty, so they cannot weaken this bound or supply extra zeros.

Let $D$ be the valid input dimension, $M$ its acceptance operator, and $S=\ker(I-M)$. Then

$$\dim\ker H_1=D,\qquad \dim\ker H_2=\dim S,
\qquad \mathcal V^\dagger H_{\rm out}\mathcal V=(I-M)/Z.$$

Under $M|_{S^\perp}\preceq I/3$, the latter has positive eigenvalues at least $\alpha=1/(3L)$. For completeness, the following argument proves the required two-kernel bound and does not assume $S\neq0$.

Let $\mathcal K=\ker H_1$, let $R=H_{\rm out}$ be the output-penalty orthogonal projector, and put $\mathcal S=\mathcal K\cap\ker R=\mathcal V S$. Positivity gives $\ker(H_1+R)=\mathcal S$ exactly. Write $g_1=1/(8L^2)\leq1$. For any unit $\psi\perp\mathcal S$, decompose $\psi=x+y$ with $x\in\mathcal K\ominus\mathcal S$ and $y\perp\mathcal K$, and put $e=\langle\psi,(H_1+R)\psi\rangle$. Then

$$\|y\|^2\leq e/g_1,\qquad \|R\psi\|^2\leq e,$$

$$\alpha\|x\|^2\leq\|Rx\|^2
 \leq2\|R\psi\|^2+2\|Ry\|^2
 \leq2e+2e/g_1.$$

Therefore

$$1\leq e\frac{2g_1+2+\alpha}{\alpha g_1}
 \leq e\frac{2g_1+3}{\alpha g_1},\qquad
e\geq\frac{\alpha g_1}{2g_1+3}\geq\frac{\alpha g_1}{5}.$$

If $S=0$, the same argument applies to every unit $\psi$ and gives a lower bound on the minimum eigenvalue, not merely a gap above an existing zero eigenvalue. Thus

$$\gamma_+(H_2)\geq1/(120L^3).$$

The source's initial valid input dimension $D$ is positive, as required to normalize the initial guide. The final common kernel may have dimension zero; neither the spectral proof nor the persistence numerator requires it to be nonzero.

Hence the rank-fraction thresholds from that note are unchanged: if $p=\operatorname{Tr}M/D$, then $f\leq p\leq1/3+(2/3)f$ for $f=\dim S/D$. The promises $p\geq2/3$ and $p\leq1/3$ imply respectively $f\geq1/2$ and $f\leq1/3$.

## 4. Guide preparation and error budget

The normalized initial-history projector is prepared by taking the maximally mixed valid input, preparing the known clock amplitudes $s_t/\sqrt Z$, and coherently applying the unitary prefixes $V_t$. There are only polynomially many clock positions; clock weights are the integers one and two. This yields polynomial-size BQP preparation to arbitrary inverse-polynomial trace-distance error. The intermediate unitary prefixes contain individual Hadamards; that is harmless for this **approximate BQP preparation circuit**. The original verifier and all Hamiltonian constraints remain the exact fixed-$G_2$ construction. No approximate compilation is used to infer perfect acceptance or exact kernel dimension.

The logical register-to-chain encoding is a tensor product of fixed-size oriented-cycle isometries; orientation signs and register permutations are efficiently computable. Common-copy unweighting is an additional efficiently implemented isometry. Both preserve trace distance.

More explicitly, let $Q$ be the encoded initial-history projector and $P$ the actual initial harmonic projector. The concentration/min--max repair gives equal rank $D$ and $\|P-Q\|\leq\eta$. Principal angles then give

$$\tfrac12\|P/D-Q/D\|_1\leq\eta.$$

Preparing $Q/D$ to trace distance $\varepsilon$ therefore gives distance at most $\eta+\varepsilon$ from $P/D$, before and after the common blow-up. Every measurement probability changes by at most this amount. Choose this sum comfortably below the rank-fraction separation. This is the mixed-guide input for normalized harmonic persistence, **not** a claim that an arbitrary history mixture is the June theorem's pure signed subset guide.

## 5. Honest final scope

The unproved arbitrary-integer-state step is avoidable; the explicit weighted unary construction above provides the missing source-compatible palette while retaining exact multiplicities and polynomial spectral gaps. Combined with the preceding local concentration, filling, and functorial unweighting derivations, it supports a reduction from the precisely specified fixed-$G_2$, perfect-eigenspace-separated circuit promise. It does not establish that an unrestricted formulation of SDQC1 reduces to that source, nor does it establish novelty against the July normalized-persistence paper. No full new clique-gadget simulation was run for this addendum.

**BOUNDED NUMERICAL CHECK, NOT PROOF:** reran the root's `check_weighted_history.py`. Both valid-clock fixtures passed the projector, history-isometry, output-compression, kernel-dimension, and displayed gap checks. They have kernel dimensions $(4,1)$ and $(4,3)$, respectively, with $Z=5,6$. This verifies those small matrix implementations only, not the clique-gadget topology or asymptotic theorem.

A separate 12-dimensional check of the abstract zero-common-kernel case used two work bits, three clock positions, the up/down Hadamard pair, and the projector onto the entire final-time slice. Its initial nullity was four, final nullity zero, and final minimum eigenvalue approximately $0.11808$, above $1/(120\cdot3^3)\approx0.00030864$. This check is included as `check_zero_final_kernel()` in `check_weighted_history.py`. The proof covering this case is Section 3's argument, not that numerical example.


---

# COMPANION SOURCE AND UNWEIGHTING AUDIT

Repository file: `research/quantum_direction_selection/round2/UNWEIGHTING_AUDIT.md`

SHA-256: `021b0851b938bda1a099aae5520d7d277eb1f4fb17ceee423e1cd6035ceb42a4`

# Round 2: unweighting, source parameters, and a proposed gap-proof repair

2026-09-02. Author: bounded independent TDA probe. Other projects were read-only. No external submission was made by this agent.

## Outcome and proof status

**PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION:** the precise target is harmonic survival with a source-compatible **signed** succinct subset guide, not a strictly positive guide in globally sorted simplex coordinates, and not normalized persistent Betti number. The common-multiplicity transfer is proved below. A BQP1-hardness corollary follows from the weighted source theorem; this audit additionally supplies a local repair of its gap argument, reducing its dependencies to the fixed-size King--Kohler gadget package. The repair is a LOCAL DERIVATION, independently algebra-checked by the root and the companion audit in this session; it must not be represented as wording already present in either source. The fixed-gadget source theorem itself remains an imported theorem, not a from-scratch proof completed here.

There is no identified functoriality, integer-parameter, or guide-preparation obstruction for the source hard family. However, the June proof has a real domain mismatch, present in the published PDF, and a literal padded-bulk estimate in the older preprint also needs correction. A bare assertion that the complete imported proof has been independently verified would be inaccurate.

## Sources and dependency boundary

1. Gyurik--Schmidhuber--King--Dunjko--Hayakawa, [PRX Quantum 7, 020361 (16 June 2026)](https://journals.aps.org/prxquantum/pdf/10.1103/gvys-hl8h), DOI **10.1103/gvys-hl8h**; [arXiv v2](https://arxiv.org/html/2410.21258v2). Checked Lemmas 5--9 and Appendix B. In the journal the overlap lemma is B1; in the arXiv HTML it is 11.
2. King--Kohler, [arXiv:2311.17234v2](https://arxiv.org/html/2311.17234v2), especially the fixed-gadget Lemma 9.1, padded Lemma 10.1, Claims 10.1--10.4, and Appendix B. The [journal landing page](https://epubs.siam.org/doi/10.1137/24M1710243) identifies the 2026 SIAM publication, but its full text was not accessible in this bounded check. Do not attribute an arXiv-only defect to the SIAM version without checking that version.
3. Hayakawa, [arXiv:2608.02726v1](https://arxiv.org/html/2608.02726v1), Lemma 4.2 and Theorem 4.3, August 2026 preprint. Its fixed-sector and asymmetric-gap proofs were checked at the operator level, independently of its QMA1 gate-set reduction.

No step uses Dey--Xin arXiv:2403.08110v4. The current QuantumTDA instructions explicitly classify that unfolding preprint as unreviewed and correctness-unverified.

Dependency map:

    fixed finite gadget palette + its local spectral/topological facts
           -> corrected arbitrary-state concentration estimate
           -> min--max YES gap + harmonic/history closeness
    circuit-history Hamiltonian + register product guide
           -> weighted harmonic-survival hardness
    common integer copies + fixed/asymmetric sectors
           -> signed-guide unweighted harmonic-survival hardness

## 1. Precisely specified target

Let UHS denote the following promise problem over real chains (complexification is harmless).

Input: explicit finite graphs $G_1\subseteq G_2$, degree $p\geq1$, an inverse-polynomial lower bound $\gamma_0$ for the nonzero spectrum of $\Delta_p(\mathrm{Cl}(G_2))$, and a polynomial-size classical description/preparation procedure for a unit vector

$$|\psi\rangle=|S|^{-1/2}\sum_{\sigma\in S}\epsilon(\sigma)|\sigma\rangle,
\qquad \epsilon(\sigma)\in\{-1,1\}.$$

Simplex coordinates use globally increasing vertex order; $\epsilon$ is efficiently computable. The guide is promised harmonic in the first clique complex. The source-compatible restricted descriptor is a polynomial-size disjoint union of equal-cardinality products of oriented edge families on disjoint vertex blocks, with copy labels allowed in those families. It permits polynomial-time quantum preparation to any inverse-polynomial error; a mere efficient membership oracle for $S$ is NOT the input model.

Promise: the squared final harmonic overlap is at least $2/3$ or at most $1/3$. Output the corresponding bit. The reduction below has YES overlap at least $0.9$ and NO overlap exactly zero. Equivalently, one may keep the source's inverse-polynomial-versus-exponentially-small norm thresholds, because this special reduction has zero NO overlap even after polynomial graph-size expansion.

**Claim:** UHS is BQP1-hard for the June source's fixed gate set $\{\mathrm{CNOT},U_{\rm Pyth},I\}$, and belongs to BQP. This does not say BQP-complete or BQP1-complete. Its unconditional source-level status is a corollary of the cited weighted theorem and August graph lemmas; its independently repaired proof is conditional on the fixed-gadget facts isolated in Section 3 below.

Membership is standard, not a new algorithm. The explicit graph gives polynomial-time clique and boundary access. In degree $p$, the boundary has at most $p+1$ entries per column and at most $|V|$ cofaces per row; the Hodge Laplacian has polynomial sparsity and polynomial norm. Rescaled Hamiltonian simulation and phase estimation separate zero from $[\gamma_0,\infty)$, and repeated measurement estimates the guide's zero-eigenspace weight to constant error. Preparation and orientation phases are included in the running time. No uniform state over all cliques is needed.

## 2. June audit: exact issue and parameter choices

**Verified version mismatch, not a counterexample to the theorem.** Journal Lemma 7, printed p. 9, applies Appendix-B Lemma B1 to an arbitrary low-energy state orthogonal to the harmonic space. B1, printed p. 16, assumes the state lies in the simulated-qubit subspace. The arXiv version has the same mismatch. The subsequent global subspace-closeness assertion is not supplied merely by its citation to a definition. Replace both steps by the concentration/min--max argument below.

For the source circuit, the history Hamiltonian has a unique zero vector in YES and no zero vector in NO, with a known inverse-polynomial spectral lower bound $g_0\leq1$ after polynomial pre-idling. Lemma 5's YES argument is valid: positive addition of the output penalty preserves the already unique, perfectly accepting history kernel. One need not compute the actual spectral gap.

Let $t$ be the number of local projector terms, all from the fixed finite integer-state palette with locality at most four. For a chosen overlap-error parameter $\eta\in(0,1/10)$, take a sufficiently small fixed constant $c$ and choose a dyadic number

$$\frac{c\eta^2g_0}{2t}<\lambda=2^{-b}\leq\frac{c\eta^2g_0}{t},
\qquad E=c\eta^2\lambda^{18}g_0/t.$$

For constant or inverse-polynomial $\eta$, $b=O(\log n)$, $\lambda$ and $E$ are inverse polynomial, and both are computable from the reduction's known lower bound. The inequalities, rather than equality with an unknown actual gap, justify the dyadic choice. Distinct sufficiently small constants in $\lambda$ and $E$ may be used.

The source guide is the encoded prehistory: a uniform union of $2L$ distinct computational-clock strings, each mapped to a product of $N$ four-edge register cycles. The $2L$ products have disjoint supports and equal size $4^N$; their signs in sorted coordinates are computable from the edge orientations and permutation parity. All support vertices have weight one. It is harmonic because it is a cycle in the top degree $p=2N-1$ of the register join. These facts are independent of the subsequent gap repair.

Pre-idling gives squared prehistory/history overlap $L/(L+T)$. Choose, for example, $L\geq100T$, then choose $\eta$ small enough in the displayed parameter bounds. The resulting final overlap is comfortably above $2/3$. To obtain $1-1/\mathrm{poly}(n)$ overlap, enlarge $L/T$ and decrease $\eta$ inverse-polynomially; both changes preserve polynomial reduction size.

## 3. Fixed-gadget hypotheses and corrected padding

This section states exactly the local source package used. All constants depend only on the finite palette, not on the number of qubits, number of terms, or an exponential chain dimension.

For the gadget on $m_i\leq4$ qubits, write $d_i=2m_i-1$. Its degree-$d_i$ spectrum splits into a harmonic sector, a one-state lifted-constraint sector of energy $\Theta(\lambda^{4m_i+2})$, a bulk sector of energy $\Theta(\lambda^2)$, and a remaining sector bounded below by a constant. The first two sectors together are $O(\lambda)$-close in projector norm to the local simulated-qubit space. The bulk sector is $O(\lambda)$-close to the local degree-$d_i$ central-bulk space. The lifted constraint is a cycle. The central-bulk projected boundary/coboundary pair is injective in this degree, with singular values bounded below by $c\lambda$.

These are the fixed-gadget Lemma 9.1 and its local bulk/cycle consequences. Since the local matrices have constant dimension, basiswise $O(\lambda)$ perturbation implies projector-norm $O(\lambda)$ without an input-size-dependent factor. This argument must be made BEFORE padding; basiswise closeness alone does not give a dimension-free projector bound for arbitrary growing-rank subspaces.

For gadget $i$, let $q_i=2(N-m_i)-1$ and let $P_{\rm out,i}$ project onto top-degree harmonics of the unaffected-qubit register join. Use augmented chains if there are no unaffected qubits. Its positive spectrum, including all lower-degree sectors, is bounded below by a constant: the augmented join Laplacian is a sum of fixed bowtie Laplacians.

The full join decomposition is

$$C_k(Y_i)=\bigoplus_{r+s=k-1} C_r(Y_i^{\rm loc})\otimes C_s(R_i^{\rm out}).$$

One must not replace this by a single tensor summand. In degree $p=2N-1$, the possible summands are $(r,s)=(2m_i-1,q_i)$ and $(2m_i,q_i-1)$. All modes outside the local-low-energy sectors tensored with $P_{\rm out,i}$ have a constant spectral lower bound and belong to the high sector $A_i$.

Define corrected bulk projections in every relevant degree by

$$Q_i^k=P_{\rm bulk,loc}^{\,k-q_i-1}\otimes P_{\rm out,i},$$

zero on the other bidegrees. The local bulk estimate now pads correctly. In fact,

$$R_i=(Q_i^{p-1}\partial_i,\;Q_i^{p+1}d_i),
\qquad \|R_i\|\leq C\lambda,
\qquad \|R_i Q_i^p x\|\geq c\lambda\|Q_i^p x\|.\tag{1}$$

Proof: the outside harmonic projector annihilates both outside differentials on either side. In the join differential only the local differential survives, and the local bulk vertices all have weight $\lambda$. The lower bound is the fixed local injectivity bound tensored with an orthogonal projector. In particular it is uniform even when the outside harmonic rank is exponential. Although $Q_i^k$ need not be a coordinate projector, its range is supported on simplices in gadget $i$; projected boundary/coboundary outputs cannot receive contributions from a different gadget.

**Why this correction matters.** KK arXiv Claim 10.2 literally asserts (1)'s upper bound with the full coordinate bulk projector and arbitrary padded inputs. Take a normalized local bulk simplex $\tau$ and join it with a single outside unit-weight register edge $[u,v]$. The boundary has terms $\tau*[v]-\tau*[u]$ of norm $\sqrt2$, still supported in the bulk. It is not $O(\lambda)$ as $\lambda\to0$. This is an analytic counterexample to the literal padded claim, not to the corrected harmonic-outside projection nor to the hardness theorem.

## 4. Arbitrary-state concentration: detailed proposed repair

Let $\Pi_0$ project onto register chains, $\Pi_i$ onto chains containing vertices of gadget $i$, and $P$ onto the embedded $N$-qubit harmonic space. There are no edges between different gadgets, so $\Pi_0+\sum_i\Pi_i=I$. Put $x_i=(\Pi_0+\Pi_i)\sigma$ for any normalized full-chain state of energy at most $E$.

Write $A_i,B_i,\widehat\Phi_i,K_i$ for the mutually orthogonal single-gadget high, bulk, lifted-constraint, and kernel projectors. Thus

$$A_i+B_i+\widehat\Phi_i+K_i=\Pi_0+\Pi_i,
\quad \|K_i-(P-\Phi_i)\|\leq C\lambda,
\quad \|B_i-Q_i^p\|\leq C\lambda,\tag{2}$$

where $\sum_i\Phi_i=sHs^\dagger$. All projector differences in (2) follow in constant dimension and then tensor with $P_{\rm out,i}$.

1. **High-sector bound.** Up-Laplacian energy splits by gadgets. The off-register part of $\partial_i x_i$ also has norm at most $\sqrt E$. The only discrepancy in the register boundary is interference from the other gadgets. The interface map

   $$T_j=\Pi_0^{p-1}\partial\Pi_j^p$$

   removes the unique gadget vertex of a simplex; its coefficient is $\lambda$. More explicitly, partition the domain by that vertex $u$. On each orthogonal piece the deletion is a signed partial isometry $\lambda D_u$, so $T_jT_j^\dagger=\lambda^2\sum_uD_uD_u^\dagger\preceq\lambda^2N_jI$, where $N_j$ is the constant number of new vertices of that palette gadget. This verifies the bound on every outside bidegree without requiring a common tensor decomposition across gadgets. Cauchy--Schwarz and $\sum_j\|\Pi_j\sigma\|^2\leq1$ give

   $$\left\|\sum_{j\ne i}T_j\Pi_j\sigma\right\|\leq C\lambda\sqrt t.$$

   Therefore the single-gadget energy of $x_i$ is at most $C(E+\lambda^2t)$, and

   $$\|A_ix_i\|\leq C(\sqrt E+\lambda\sqrt t).\tag{3}$$

2. **Bulk-sector bound.** Let $F_i=\widehat\Phi_i+K_i$ and $Q=Q_i^p$. The identity

   $$I=Q+(I-Q)A_i+(I-Q)B_i+F_i-QF_i$$

   holds on the single-gadget chain space. Apply $R_i$ and use (1)--(3). The full-state energy controls $\|R_ix_i\|\leq\sqrt E$. Further, $\|(I-Q)B_i\|,\|QF_i\|\leq C\lambda$ and $\|R_iF_i\|\leq C\lambda^{2m_i+1}$, by the local low-energy spectrum. Consequently

   $$c\lambda\|Qx_i\|\leq\sqrt E+C\lambda\|A_ix_i\|+C\lambda^2,
   \qquad
   \|B_ix_i\|^2\leq C(E/\lambda^2+\lambda^2t).\tag{4}$$

3. **Lifted constraints.** Each lifted-constraint sector is a cycle and has up energy at least $c\lambda^{18}$. Since the global up Laplacian is the sum of the single-gadget up Laplacians,

   $$\sum_i\langle\sigma,\widehat\Phi_i\sigma\rangle\leq CE/\lambda^{18}.$$

   The weaker bound $CtE/\lambda^{18}$ is sufficient and matches the following uniform bookkeeping.

4. **Concentration inequality.** Sum (2) in the complete-projector identity, then insert (3)--(4). Dropping the nonpositive term $-(t-1)\langle\Pi_0-P\rangle$ gives

   $$1\leq\langle\sigma,P\sigma\rangle-\langle\sigma,sHs^\dagger\sigma\rangle
      +C\left(t\lambda+t^2\lambda^2+tE/\lambda^{18}\right).\tag{5}$$

   Let $S$ project onto $s(\ker H)$, allowing $S=0$ in NO. If the nonzero spectrum of $H$ is at least $g_0\leq1$, then

   $$\boxed{\quad\|(I-S)\sigma\|^2
   \leq \frac C{g_0}\left(t\lambda+t^2\lambda^2+tE/\lambda^{18}\right).\quad}\tag{6}$$

   Indeed, with $a=\|(I-P)\sigma\|^2$ and $b=\|(P-S)\sigma\|^2$, (5) implies $a+g_0b\leq R$, whence $a+b\leq R/g_0$. No assumption $\sigma\in\operatorname{im}s$ is used.

5. **Gap and guide.** Choose parameters in Section 2 so the right side of (6) is at most $\eta^2<1$. Every vector in the spectral subspace $L_{<E}$ satisfies (6), so restriction of $S$ to that space is injective and $\dim L_{<E}\leq\dim\ker H$. In NO, this excludes both zero and sub-$E$ eigenvalues. In the source YES family $\dim\ker H=1$, while the exact gadget topology supplies at least one nonzero surviving homology class; hence $\dim\ker\Delta=1$ and the next eigenvalue is at least $E$. Applying (6) to its unit harmonic vector gives projector distance from the encoded history line at most $\eta$. Thus for the prehistory guide $\psi$,

   $$\langle\psi,P_{\ker\Delta}\psi\rangle
       \geq |\langle\psi,\sigma_{\rm hist}\rangle|^2-\eta
       =L/(L+T)-\eta.$$

This repairs the specific domain/closeness steps without assuming exact equality of encoded and harmonic vectors. It also avoids a general many-dimensional global topology assertion for the June hard family: the one-dimensional case needs only existence of one surviving class. The independent companion note analyzes the more general dimension-$r$ version.

## 5. Unweighting proof and exact size/gap bookkeeping

Set $M=\lambda^{-2}=2^{2b}$. Replace every register vertex by a clique of size $M$, and every added gadget vertex by a singleton. Across both filtration levels use the same copies. More generally, for a finite inclusion diagram with common positive weights and common integers $f_v=Mw(v)^2$, replace $v$ by a clique of $f_v$ copies.

On normalized weighted simplex coordinates define

$$U_{i,k}|\sigma\rangle_w
   =\left(\prod_{v\in\sigma}f_v\right)^{-1/2}
      \sum_{\text{one copy of each }v\in\sigma}|\widehat\sigma\rangle.$$

Orient each lift consistently with its base simplex. Distinct base simplices have disjoint lift supports. Termwise counting proves

$$U_i^\dagger U_i=I,\qquad \widehat J_{ij}U_i=U_jJ_{ij},
\qquad \widehat dU=\sqrt M\,Ud_w,\qquad
\widehat\Delta U=M U\Delta_w.$$

There is no inclusion normalization factor. The $\sqrt M$ factor belongs to the differential and becomes $M$ for the Laplacian. In raw weighted coordinates the isometry carries the degree factor $M^{-(k+1)/2}$, which cancels between same-degree inclusions.

The block-permutation fixed space consists exactly of these orbit averages: a simplex with two vertices in one block changes orientation under their transposition and contributes no fixed vector. Repeated-block coboundary contributions cancel. The asymmetric gap follows by orthogonally splitting according to the first block whose averaging projector vanishes. Such vectors live in the expanded star of that block. The augmented join Laplacian splits as the complete-block Laplacian plus the nonnegative link Laplacian; the former is $f_vI$ away from its empty-block component, which is absent in that asymmetric sector. In degree zero, the augmentation correction vanishes on the asymmetric sector. This proves, for an arbitrary base clique complex,

$$\widehat\Delta|_{T^\perp}\succeq\min_v f_v,
\quad \widehat P_i=U_iP_iU_i^\dagger,
\quad \gamma_+(\widehat\Delta_i)\geq
\min\{M\gamma_+(\Delta_i),\min_vf_v\}.$$

For the hard family, $\min f_v=1$ and the final gap is at least $\min\{ME,1\}$. The graph has $N_{\rm reg}M+N_{\rm gadget}$ vertices, polynomial in the original instance length; the lower bound is inverse polynomial in this new size as well. Ordinary Hamiltonian normalization adds only polynomial factors.

Every guide simplex uses $p+1$ register vertices, so it has exactly $M^{p+1}$ lifts and the lifted amplitudes have equal magnitude. Append $p+1$ independent $[M]$ copy coordinates and retain the source orientation sign. Since $M$ is a power of two, this adds $(p+1)\log_2M$ Hadamards and copy bits, plus polynomial reversible relabeling. Alternatively expand each four-edge factor to its $4M^2$ copied oriented edges; this still has polynomial description size. No exponential simplex listing is performed.

The initial guide is still exactly harmonic: both differential identities apply even though the blown-up initial complex now contains many higher-dimensional simplices inside copy blocks. Their symmetric coboundary contributions cancel. If a target requires equal vertex sets, absent future gadget vertices can be inserted initially as isolated vertices; $p\geq1$ makes them irrelevant to the guide and its degree-$p$ Laplacian.

## 6. Whole-diagram preservation and limits on novelty

For each arrow, the harmonic map $A_{ij}=P_jJ_{ij}|_{\ker\Delta_i}$ satisfies

$$\widehat A_{ij}U_i=U_jA_{ij}.$$

Thus the entire harmonic representation is unitarily naturally isomorphic: every arrow singular value, guided overlap, and algebraic rank invariant is preserved. This holds for an arbitrary finite inclusion diagram, including zigzags and finite-poset diagrams with compatible fixed weights. It is not an algorithm for efficiently reading all those invariants.

This extension beyond one pair is useful but elementary. Enlarging every multiplicity by the same factor scales the symmetric Laplacian and the asymmetric lower bound while also enlarging the graph; it does not by itself improve a normalized computational condition parameter. Routine perturbation theory could add weight-rounding tolerance under all-level gap promises, but exact rank and a strictly harmonic uniform guide need additional care. No substantial new robustness theorem was proved here.

**Novelty assessment:** likely a short functorial corollary to June plus August, with a technically worthwhile source-proof repair, not presently a strong standalone ITCS direction. The August paper itself discusses harmonic-persistence unweighting as an outlook; this bounded audit has not established the absence of a later resolution. Distinguish two normalizations: dividing by the full simplex count can change exponentially after blow-up, whereas the July normalized harmonic-persistence ratio $\beta^{1,2}_p/\beta^1_p$ IS preserved by this natural isomorphism when its denominator is nonzero. Nevertheless, the guided hard family alone is not a hardness reduction for that rank ratio; unweighting cannot turn an equal-complex quasi-hard instance into a nontrivial rank-ratio instance. Do not claim an algorithm for generalized rank or full indecomposable decomposition from this corollary.

The exponent $18$ in Sections 2--5 is specific to the June finite palette with $m\leq4$. A different circuit-Hamiltonian construction of locality $m$ must instead use $\kappa=4m+2$ throughout the lifted-constraint and energy bounds; locality five or six cannot silently inherit exponent eighteen.

## 7. Remaining checks and completed checks

Completed: exact normalized-chain convention; common-copy inclusion; fixed/asymmetric-sector argument; source weights and guide support; dyadic computability; polynomial graph/preparation size; complex-versus-real compatibility; NO-overlap threshold bookkeeping; published June domain mismatch. The proof-writer discipline led to isolating the fixed-size gadget assumptions and writing the concentration inequality instead of repeating the unsupported global-closeness citation.

Independent session checks: the root checked the Section 4 concentration/min--max algebra; the companion audit checked the interface bound and the spectral-to-exact-filling argument in Section 8. No remaining cross-support interference flaw was identified, conditional on the isolated local facts. Pending: source-version comparison against the inaccessible SIAM full text and a from-first-principles audit of the single-gadget spectral-sequence theorem, which was inspected and imported rather than fully re-proved here. These are explicit source dependencies, not a demonstrated fatal obstruction to the unweighted theorem.

Earlier tiny numerical conventions check: `tda_probe/check_common_blowup.py` verifies path-to-triangle inclusions with unequal fixed copy multiplicities. The new `round2/check_padded_bulk.py` checks the exact rational coefficients in Section 3's counterexample and their cancellation for a harmonic outside cycle. It is not a check of the global gadget spectrum. No large simulation was run.

## 8. Exact filling follows from the same single-gadget package

**LOCAL DERIVATION; a stronger dependency simplification.** A new Section-8 relative-homology theorem is unnecessary for the exact relation $B_p(Y_j)\cap V=\operatorname{ran}\Phi_j$. It follows from the already used single-gadget nullity and kernel-projector limit. Here $R$ is the register complex, $V=Z_p(R)=H_p(R)$ is its top-degree cycle space, and $Y_j$ is the register with just gadget $j$ added and padded.

1. **Weight invariance on register boundaries.** Identify each normalized chain basis with the ordinary coordinate basis. Let $W_k(\lambda)$ be diagonal with entry $\prod_{v\in\sigma}w(v)$ on simplex $\sigma$. The stipulated boundary convention gives

   $$\partial_{w,k}=W_{k-1}^{-1}\partial_{1,k}W_k,
   \qquad B_p(Y_j,w)=W_p^{-1}B_p(Y_j,1).$$

   Since every register vertex has weight one, $W_pv=v$ for every $v\in V$. Consequently

   $$\mathcal W_j:=B_p(Y_j,w)\cap V=B_p(Y_j,1)\cap V$$

   is exactly independent of $\lambda>0$ on the fixed gadget graph.

2. **The kernel limit excludes unintended filled directions.** Every $v\in\mathcal W_j$ is orthogonal to every harmonic vector of $Y_j$ for all sufficiently small positive $\lambda$. The fixed-gadget spectral package, padded by the unaffected harmonic factor, gives

   $$P_{\ker\Delta_p(Y_j,w)}\longrightarrow P_V-\Phi_j\qquad(\lambda\to0).$$

   Therefore $(P_V-\Phi_j)v=0$ and $\mathcal W_j\subseteq\operatorname{ran}\Phi_j$. This argument does not require an exact equality of harmonic vectors at any finite $\lambda$.

3. **Nullity supplies the reverse inclusion by dimension.** The inclusion map from $V$ into $H_p(Y_j,w)$ has kernel exactly $\mathcal W_j$. The same local package gives

   $$\dim H_p(Y_j,w)=(2^{m_j}-1)2^{N-m_j}
      =\dim V-\operatorname{rank}\Phi_j.$$

   Hence rank-nullity implies $\dim\mathcal W_j\geq\operatorname{rank}\Phi_j$. Together with Step 2,

   $$\boxed{B_p(Y_j,w)\cap V=\operatorname{ran}\Phi_j.}$$

4. **Several gadgets and naturality.** Let $Y_A$ contain a subset $A$ of the gadgets. No simplex contains new vertices from different gadgets. Since the register has no $(p+1)$-simplices, any $(p+1)$-chain splits as $b=\sum_{j\in A}b_j$. If $\partial b\in V$, its off-register part vanishes separately in each gadget; thus each $\partial b_j$ is a register cycle, and belongs to $\operatorname{ran}\Phi_j$ by Step 3. The reverse containment is immediate from the individual fillings. Therefore

   $$B_p(Y_A,w)\cap V=\sum_{j\in A}\operatorname{ran}\Phi_j,
   \qquad
   V\big/\sum_{j\in A}\operatorname{ran}\Phi_j\hookrightarrow H_p(Y_A,w).$$

   The injected quotient has dimension $\dim\ker H_A$, where $H_A=\sum_{j\in A}\Phi_j$ on $V$. Under the concentration estimate for $H_A$, min--max gives the reverse dimension inequality, so the injection is an isomorphism and excludes all extra harmonics. For $A\subseteq B$, the same register cycle represents both images; hence these isomorphisms commute exactly with inclusions and the corresponding quotient maps.

This closes the exact-filling/naturality dependency conditional only on the fixed-gadget spectral package and the checked absence of edges between distinct gadgets. It does not validate an arbitrary-gate-set gadget palette: each additional finite palette must satisfy that package, and its maximum locality determines $\kappa=4m+2$. It also does not on its own construct a promise-hard normalized-rank instance; that is a separate reduction task.


---

# CONDITIONAL PERSISTENT-LAPLACIAN EXTENSION

Repository file: `research/quantum_direction_selection/collaboration/2026-09-02/PERSISTENT_LAPLACIAN_EXTENSION.md`

SHA-256: `7c291ffe5303d40f5141b022bca4c75dd146f1fb9fdedba4d9505efd5dada94e`

# Conditional simultaneous unweighting of persistent Laplacians

September 2, 2026 PDT. Origin: Section 6 of the [completed first Pro response](PRO_PREVIOUS_TDA_RESPONSE.md). The derivation below was independently checked algebraically during consolidation. It is conditional on the stated single-complex symmetric-sector identity and asymmetric gap. It does not certify novelty or re-prove Hayakawa's local spectral package.

We restrict the formal statement to clique complexes, the domain of the imported result. Pro's proposed extension to arbitrary simplicial block substitutions is retained in its raw response but is not adopted here without checking the star/link argument.

## Statement

Let \(K_\alpha\subseteq K_\beta\) be a finite diagram of weighted clique complexes with a fixed positive weight \(w(v)\) for every shared vertex. Choose one \(F>0\) such that \(f_v=Fw(v)^2\) are positive integers. Use the same labeled clique block of \(f_v\) copies at every level containing \(v\). Write \(\widehat K_\alpha\) for the resulting unweighted blow-ups.

For each level and degree, the normalized one-copy-per-block lift \(U_{\alpha,k}\) is an isometry onto the subspace fixed by the product of block permutation groups (acting on oriented chains). Assume the imported single-complex identities
\[
\widehat\partial U_{\alpha,k}
=\sqrt F\,U_{\alpha,k-1}\partial_w,\qquad
\widehat\Delta_{\alpha,k}|_{T_{\alpha,k}^{\perp}}
\succeq f_{\min}(\alpha)I,
\]
where \(T_{\alpha,k}=\operatorname{ran}U_{\alpha,k}\) is reducing and
\(f_{\min}(\alpha)=\min_{v\in K_\alpha}f_v\). The source and blow-up use the same compatible orientation convention. Empty chain spaces have vacuous assertions; take nonempty initial vertex sets when defining \(f_{\min}\).

Equip the persistent chain domain with its **inherited** Hilbert-space inner product:
\[
D_{k+1}^{\alpha,\beta}
=\{z\in C_{k+1}(K_\beta):\partial_wz\in C_k(K_\alpha)\},
\quad b^{\alpha,\beta}=\partial_w|_{D_{k+1}^{\alpha,\beta}}.
\]
Its adjoint is computed relative to that inherited metric, not an arbitrary nonorthonormal nullspace basis. Define
\[
\Delta_k^{\alpha,\beta}
=b^{\alpha,\beta}(b^{\alpha,\beta})^\dagger
+(\partial_{w,k}^{\alpha})^\dagger\partial_{w,k}^{\alpha}.
\]

Then for every comparable pair,
\[
\widehat\Delta_k^{\alpha,\beta}
\cong F\Delta_k^{\alpha,\beta}\oplus R_{\alpha,\beta,k},
\qquad
R_{\alpha,\beta,k}\succeq f_{\min}(\alpha)I.
\]
The identification of the first summand is \(U_{\alpha,k}\). Consequently, for
\(0<\Lambda\le f_{\min}(\alpha)\),
\[
\mathbf1_{[0,\Lambda)}(\widehat\Delta_k^{\alpha,\beta})
=U_{\alpha,k}\mathbf1_{[0,\Lambda/F)}(\Delta_k^{\alpha,\beta})
U_{\alpha,k}^\dagger.
\]
This preserves all low eigenvalues in that interval with the stated scaling and multiplicities, including the kernel. It gives a conditional gap bound
\[
\widehat\gamma_+\ge
\min\{F\gamma_+(\Delta_k^{\alpha,\beta}),f_{\min}(\alpha)\}.
\]

## Proof

**Common sectors and the persistent domain.** Let \(G\) be the product of the permutation groups of all copy blocks in the diagram. It acts orthogonally on oriented chains and preserves each complex and each inclusion. Therefore the persistent domain is \(G\)-invariant and decomposes orthogonally into its fixed and complementary parts.

The fixed part is exactly
\[
(\widehat D_{k+1}^{\alpha,\beta})^G
=U_{\beta,k+1}D_{k+1}^{\alpha,\beta}.
\]
Indeed, for \(U_{\beta,k+1}z\), its boundary is
\(\sqrt F U_{\beta,k}\partial_wz\). Different base simplices have disjoint lift supports; this boundary lies in \(C_k(\widehat K_\alpha)\) precisely when \(\partial_wz\) is supported in \(K_\alpha\).

Hence the restricted persistent boundary on fixed sectors is \(\sqrt F\,b^{\alpha,\beta}\) in the two isometric coordinates. Its adjoint has the same factor. The down term also scales by \(F\). Equivariance prevents mixing between fixed vectors and their orthogonal complement. This proves the exact symmetric summand.

**Persistent domination.** The isometric inclusion
\(J:C_{k+1}(K_\alpha)\hookrightarrow D_{k+1}^{\alpha,\beta}\)
satisfies \(bJ=\partial_{k+1}^{\alpha}\). Since \(JJ^\dagger\preceq I\),
\[
bb^\dagger-bJJ^\dagger b^\dagger
=b(I-JJ^\dagger)b^\dagger\succeq0.
\]
The down terms are equal, so
\[
\Delta_k^{\alpha,\beta}\succeq\Delta_k^{\alpha,\alpha}.
\]
Apply this inequality to the blow-up and restrict to its reducing asymmetric sector. The imported ordinary-Laplacian gap supplies \(R\succeq f_{\min}I\). Functional calculus gives the spectral-projector statement. \(\square\)

## Scope and checks

This is a short conditional structural theorem. Its newness and independent paper value remain unknown. The standard domination inequality is not advertised as novel.

The argument does not deduce a persistent positive gap from the two endpoint positive gaps: shrinking a kernel can introduce new, small positive eigenvalues. It uses domination only to transfer the **already positive asymmetric sector** bound. It does not turn a low-energy approximation into an exact homology count, solve the unrestricted normalized-persistence conjecture, or provide a barcode algorithm.

Polynomial-size conversion additionally requires computable polynomial total multiplicity. Changing the copy counts across levels breaks the natural fixed sectors, as the existing one-vertex fixture shows.

The accompanying check_persistent_laplacian.py tests an actual persistent domain, computed using an orthonormal nullspace basis, for a four-cycle filled by two triangles sharing a later diagonal. Neither triangle alone has boundary supported on the initial cycle, but their linear combination does. It checks the induced metric/adjoint, exact symmetric-block identity numerically, cross-sector reduction, persistent domination, the asymmetric lower bound, and the persistent rank by independent cycle/boundary ranks. A finite check supports that implementation only.


---

# SECONDARY QUANTUM NET AND BARCODE PROOF

Repository file: `research/quantum_direction_selection/round2/QUANTUM_NET_PROOF.md`

SHA-256: `88155ebe6443186c57e53dc55dd334fc7d3b686a72b75f0356c713ada45d7b0a`

# Quantum epsilon-nets and additive barcode approximation

September 2, 2026 PDT. Consolidated by the root from the GPT-5.4 brainstorming/proof agent's candidate, with the mathematical corrections in `REVIEW_RESOLUTION.md`. This is a secondary candidate, not a claim of priority or a submission-ready contribution.

## Theorem and access model

Let $X=\{x_1,\ldots,x_n\}\subset\mathbb R^d$, $n\ge1$, with $b$-bit coordinates, accessed through a coherent whole-point oracle

$$O_X:|i\rangle|0\rangle\longmapsto|i\rangle|x_i\rangle.$$

Its clean inverse is available at the same query cost. Building this oracle from raw memory is **not free**; the theorem is in a black-box point-query model, not an end-to-end QRAM construction theorem. Classical comparison uses the same point records and no free preprocessing.

Fix $\epsilon>0$ whose squared threshold is rational with polynomially bounded bit length, so squared Euclidean distances can be compared exactly in $\operatorname{poly}(d,b)$ arithmetic gates, with threshold precision included in $b$. Suppose every subset with pairwise distances $>\epsilon$ has at most $K$ points. Replace any supplied bound by $K\leftarrow\min(K,n)$.

For $0<\delta\le1/3$, a quantum algorithm returns $S\subseteq X$ of size at most $K$ on every run, and with probability at least $1-\delta$,

$$\max_{x\in X}d(x,S)\le\epsilon.$$

Its expected point-query cost is $\widetilde O(\sqrt{nK})$, and its expected non-query search-gate cost is $\widetilde O(\operatorname{poly}(d,b)K\sqrt{nK})$. Tildes hide logarithms in $n,K,1/\delta$. Memory is polynomial in $K,d,b,\log n$.

Computing degree-$q$ persistence exactly on $S$ adds time $T_{\rm PH}(K,q)$, a monotone upper bound for the chosen classical algorithm, and returns a Rips barcode at bottleneck distance at most $2\epsilon$ from that of $X$. The convention is that a simplex enters at parameter $r$ when its diameter is at most $r$.

For fixed error, dimension and bounded packing number, with $b=O(\log n)$, the point-query cost is $\widetilde O(\sqrt n)$. Already in one dimension and degree zero, a promised family requires $\Omega(n)$ classical point queries and $\Omega(\sqrt n)$ quantum queries for constant-additive barcode approximation. These statements include worst-case expected query complexity.

**Status:** the local argument below proves these query-model statements using standard quantum search and persistence stability. It does not prove novelty, an exponential separation, or a practical speedup including loading a previously unindexed dataset.

## 1. Search with an unknown number of uncovered points

Use [Boyer–Brassard–Høyer–Tapp search](https://arxiv.org/abs/quant-ph/9605034). For $m>0$ marked indices, its verified search-until-success routine has expected cost at most $C\sqrt{n/m}$. Truncate one run after a sufficiently large constant times $\sqrt n$ queries. Markov's inequality gives a uniformly constant success probability whenever $m>0$, and its expected truncated cost is still at most $C\sqrt{n/m}$. If $m=0$, the run necessarily ends without a verified output in $O(\sqrt n)$ queries.

Repeat independent truncated runs $O(\log(1/\zeta))$ times, stopping on a verified output. Otherwise return NONE. This `SearchOrNone` routine has no false positive, misses a nonempty marked set with probability at most $\zeta$, and has expected cost

$$O\left(\sqrt{\frac{n}{m+1}}\log(1/\zeta)\right).$$

No up-front $\Theta(\sqrt n)$ counting step is made on every round.

## 2. Net construction and correctness

Load $x_1$ and set $S_1=\{x_1\}$. At round $t$, search for

$$P_t(i)=1\quad\Longleftrightarrow\quad d(x_i,S_t)>\epsilon,$$

with error budget $\zeta_t=\delta/[2(t+1)^2]$. A phase predicate loads $x_i$, compares its squared distance to every stored center, marks the result, and uncomputes. This uses $O(1)$ point-oracle calls, typically two including the inverse, and $\operatorname{poly}(d,b)t$ arithmetic gates. The centers are stored classical values; their input access is charged when selected.

If a verified point is found, append it and continue; if NONE is returned, stop. Every selected pair is more than $\epsilon$ apart, so the number $h$ of returned centers is always at most $K$. On the event that no invocation falsely returns NONE, the output covers all points. A union bound using $\sum_t\zeta_t<\delta$ gives the claimed correctness probability, including the $n=1$ case.

## 3. Unconditional expected complexity

Let $m_t$ be the number of uncovered points when round $t$ is reached. On **any** execution path returning $h$ centers, every subsequently selected center was uncovered already at each earlier round. Thus $m_t\ge h-t$ for $t<h$, regardless of whether the final NONE was erroneous. The final round has $m_h\ge0$. Consequently, pathwise,

$$\sum_{t=1}^h(m_t+1)^{-1/2}
\le\sum_{u=1}^h u^{-1/2}\le2\sqrt h\le2\sqrt K.$$

Let $Q_t=0$ on unreached rounds, and let $\mathcal F_t$ be the history before round $t$. The conditional search bound applies given $\mathcal F_t$. The tower property, followed by the pathwise inequality, therefore gives

$$\mathbb E\sum_tQ_t
\le C\sqrt n\log(K/\delta)\,
\mathbb E\sum_{t\text{ reached}}(m_t+1)^{-1/2}
\le 2C\sqrt{nK}\log(K/\delta).$$

This does **not** condition on the eventual value of $h$ or on eventual success. The at most $K$ additional center-loading calls are dominated by $\sqrt{nK}$ because $K\le n$. Each predicate costs at most $\operatorname{poly}(d,b)K$ non-query gates, so multiplying the unconditional expected query bound gives the stated gate bound. No random final-size expression is substituted into an expectation without this argument.

## 4. Barcode approximation

On success, $S\subseteq X$ and $d_H(X,S)\le\epsilon$. Choose a nearest-center map $p:X\to S$ fixing centers. If a simplex in $X$ has diameter at most $r$, its image under $p$ has diameter at most $r+2\epsilon$. The inclusion $S\to X$ does not increase diameter. The compositions are contiguous to the corresponding filtration-shift maps: the union of a simplex with its center images has diameter at most $r+2\epsilon$. After padding the inclusion shift to the same amount this yields a $2\epsilon$ interleaving, and hence bottleneck distance at most $2\epsilon$ for finite Rips persistence over a field. Essential bars are matched under the usual extended bottleneck convention.

This is the standard cover/stability argument, not a new persistence theorem. [Kolbe–Mayr, ICALP 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.131/LIPIcs.ICALP.2026.131.html) already develops the classical additive-approximation route via covers. To achieve barcode error $\epsilon_0$, use net radius $\epsilon_0/2$.

## 5. A one-dimensional OR reduction with finite precision

Fix $0<\epsilon_0<1/10$. Let $z\in\{0,1\}^n$ have weight zero or one. Set

$$L=\lceil\log_2 n\rceil+10,\quad M=2^L,\qquad
p_i=\frac{i}{M}+\frac{z_i}{2}\ (1\le i\le n),\quad p_{n+1}=1.$$

These are distinct dyadic points in $[0,1]$, encoded with $O(\log n)$ bits. A point-oracle call can be implemented with a constant number of coherent bit-oracle calls, including clean uncomputation. The anchor is fixed.

For Rips persistence on a line, the finite $H_0$ death times are the consecutive sorted gaps: the one-dimensional minimum spanning tree connects consecutive points. All these bars are born at zero.

- If $z=0$, the last gap has length $1-n/M\ge1023/1024$.
- If $z_j=1$, within the remaining cluster near zero gaps are at most $2/M$. If that cluster is nonempty, its gap to the moved point is at most $1/2+j/M\le1/2+1/1024$. The moved-point-to-anchor gap is below $1/2$. For $n=1$ only the last gap is present. Thus the largest finite bar length is at most $1/2+1/1024<0.501$.

This coarse bound remains valid when the removed point was the original largest cluster point. It does not incorrectly assume $n/M$ remains in the left cluster.

For any barcode $\mathcal B$, define $\ell(\mathcal B)$ as its maximum **finite bar length**, or zero when there are no finite bars, ignoring essential bars. In a matching of cost at most $\epsilon_0$, paired finite lengths differ by at most $2\epsilon_0$, and a bar matched to the diagonal has length at most $2\epsilon_0$. Applying this in both directions gives

$$|\ell(\widehat{\mathcal B})-\ell(\mathcal B)|\le2\epsilon_0.$$

Therefore a valid approximate barcode has $\ell>0.799$ in the zero case and $\ell<0.701$ in the singleton case. Threshold $3/4$ decides the promised OR instance. The maximum **death coordinate** would not work for arbitrary approximate outputs: an extra very short bar far from zero can match to the diagonal while having arbitrarily large death.

## 6. Classical and quantum lower bounds

For deterministic algorithms making at most $q$ queries, use the distribution with probability $1/2$ on zero and $1/(2n)$ on each singleton. On the zero-response transcript only the at most $q$ queried indices can reveal a singleton. Optimal success is at most $1/2+q/(2n)$. Yao's principle gives $q\ge n/3$ for bounded-error randomized algorithms. A distribution containing only singleton inputs would not establish a lower bound.

For expected classical queries, couple the zero run and a uniformly random singleton run with the same coins. They agree until the marked index is queried. Their output-YES probabilities differ by at least $1/3$ under bounded-error correctness, while coupling bounds this difference by the expected number of distinct indices queried on the zero run divided by $n$. Hence that expected number is at least $n/3$.

The quantum lower bound is standard promised unstructured search, $\Omega(\sqrt n)$, under the constant-query simulation above; see [Bennett–Bernstein–Brassard–Vazirani](https://arxiv.org/abs/quant-ph/9701001) and the BBHT source. For a worst-case expected-cost algorithm, truncate at a sufficiently large constant times its expectation. Markov's inequality preserves constant success bias above $1/2$; constant repetition restores error at most $1/3$. The standard worst-case bound then yields the expected-cost bound as well.

Every $\epsilon$-packing in $[0,1]$ has size at most $\lfloor1/\epsilon\rfloor+1$. With $\epsilon=\epsilon_0/2$, this is a constant. The upper bound is therefore $\widetilde O(\sqrt n)$ on the same bounded-geometry family where the classical lower bound is $\Omega(n)$. More generally, bounded dimension and diameter give a constant packing bound at fixed accuracy. This does not claim a lower bound matching every dependence on $K,d,\epsilon$.

## 7. Corrections, reproduction and novelty boundary

The initial proof draft required substantive corrections: unconditional expectation rather than conditioning on final output size; oracle uncomputation and exact threshold costs; dyadic coordinates; matching net radius to barcode error; maximum bar length rather than maximum death; and a lower-bound argument including the zero input. These are incorporated above.

`check_barcode_outlier.py` uses exact fractions for all 2080 singleton positions at sizes $1,\ldots,64$, including $n=1$, non-powers of two and a moved final cluster point. All passed the length separation. An appended bar $(100,100.001)$ has diagonal cost $1/2000$ and confirms why maximum death is unsafe. These are finite classical checks, not quantum simulation or proof of an asymptotic lower bound.

Important prior art:

- [Aïmeur–Brassard–Gambs](https://link.springer.com/article/10.1007/s10994-012-5316-5) already use quantum search in center selection and clustering. Do not claim the first quantum farthest-first technique. Their exact objective and guarantees must be compared before importing a clustering approximation factor.
- [Xue–Chen–Li–Jiang, ICML 2023](https://proceedings.mlr.press/v202/xue23a.html) already give square-root-input-size quantum clustering coresets.
- Kolbe–Mayr already supply the classical cover-to-barcode approximation mechanism.
- [Fukuzawa–Goodrich–Irani, SoCG 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.51) already obtain related output-sensitive quantum geometric query bounds for different problems.

The potentially new statement is the precise epsilon-net/barcode/query-separation combination, not its standard search or stability ingredients. The current literature pass is enough to identify strong collisions, not to establish definitive priority or a conference-level novelty claim.
