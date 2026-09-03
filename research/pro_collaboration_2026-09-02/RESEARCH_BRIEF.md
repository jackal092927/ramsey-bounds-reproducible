# Research brief: verified progress, promising directions, and next theorem targets

Prepared 2026-09-02 PDT; integrated with the parallel collaboration record on 2026-09-03. Repository: [ramsey-bounds-reproducible](https://github.com/jackal092927/ramsey-bounds-reproducible), research branch `codex/fill-ramsey-gaps`. This report consolidates the existing project; it does not retroactively certify every imported proof or historical computation. The [canonical TDA packet](../quantum_direction_selection/collaboration/2026-09-02/PRO_CONTEXT_PACKET.md) was sent through the existing Pro channel; this broader report supplies portfolio context and additional independent audit evidence.

## 1. Objective and present decision

Develop a high-quality, impactful TCS submission from an actual new theorem. The current priority is **exact kernel multiplicity and natural rank transfer for true normalized persistence**. The largest remaining risk is the gap between a restricted exact circuit promise and a robust, meaningful hardness statement. A second, concrete structural result is simultaneous unweighting of persistent Laplacians. A secondary algorithmic route is quantum geometric sampling followed by barcode approximation. Direct generalized-rank quantization remains a structural problem after explicit conditioning counterexamples. Standard-model hyperbolic neighbor search is on hold.

We seek complete proofs, counterexamples, or sharply delimited reductions. The target venue is an ambition, not a claim of readiness. Numerical agreement, a model's review, and a submitted abstract do not establish a theorem or significance.

## 2. Established project results and their boundaries

| Component | Current scoped result | Evidence and limitation |
|---|---|---|
| Diagonal Ramsey upper bound | $R(k,k)\le(3.780685290)^{k+o(k)}$; certified unrounded base below `3.780685288379640114` | Six-stage interval chain and outer transfer; conditional/source-relative to pinned retained-spine/book interfaces and interval semantics. No effective finite-$k$ threshold, global optimum, or current world-best claim. |
| Fixed-ratio Ramsey lower bound | Source-relative addition $\widehat H_*(C)=(1+o(1))/(64\log C)$ after fixing source constant $K$ and taking sufficiently large fixed $C$ | Local triangular ledger and weighted reverse propagation S3; S1, S2, S4, S5 remain imported. Quantifiers: fix $C,w$, then $\ell\to\infty$, then $w\downarrow\omega_0$, finally $C\to\infty$. No cross-normalization priority claim. |
| Finite fixed-seed theorem | One-sided deletion repair radius $\rho(H)\ge7$ for a labelled 100-vertex near miss with free additions | Historical record contains six checked DRAT refutations and semantic reconstruction. Local edit obstruction; no new global Ramsey bound. Exact seven remains `UNKNOWN`. |
| Exact-seven structural progress | Necessary degree cap; four branch-1 singleton preservation clauses; combined filters exclude 87.88321365513743% of raw residual supports | These are necessary conditions on a frozen relaxation. A checked relaxation model contains an independent 18-set and is not a repair. The maximal-union gate timed out without a proof or model. |
| Quantum Ramsey search | For $N\ge4^{K-1}$, verified homogeneous $K$-set with $O(2^K K\log(K/\eta))$ coherent edge queries | Main scale-aware implicit-majority proof; alternative size-biased bound $O(2^K K^2\log K\log(1/\eta))$, with multicolour extension. No numerical Ramsey improvement or separation from all randomized classical algorithms. |

The quantum classical lower bound in the manuscript is only $\Omega(2^{(2-\sqrt2)K})$, below the quantum exponent. The discrepancy with the JLRX side remark is scoped in the manuscript and is not used in its proof. The repository's submission receipt records the revised anonymous ITCS quantum PDF as resubmitted and ready for review; this consolidation did not operate HotCRP. A submission is not an acceptance.

Authoritative local pointers: [root status](../../STATUS.md), [upper scope](../../papers/upper/sections/07_limitations.tex), [lower scope](../../papers/lower/sections/08_scope.tex), [finite scope](../../papers/finite/sections/08_scope.tex), [quantum paper](../../papers/quantum/main.tex), [JLRX parameter audit](../../reviews/JLRX_PARAMETER_AUDIT_2026-09-01.md), [submission receipt](../../papers/quantum/SUBMISSION_CHECKLIST.md).

The historic finite certificates and full interval chain were not rerun wholesale during this consolidation. Their statuses are attributed to the recorded checkers. The current theorem-specific quantum self-check, thirteen-file integrity check, and two materialization tests passed again.

## 3. Main candidate: true normalized persistence

The target is

$$q=\frac{\operatorname{rank}[H_d(X_1)\to H_d(X_2)]}{\dim H_d(X_1)}.$$

Lowe--Kim--Bondesan--Hayakawa already define this normalization and conjecture hardness. Their quasi-persistence result is a different statement. In particular, an equal-complex construction with two energy cutoffs has true persistence ratio one whenever its initial Betti number is nonzero; relabeling cutoffs does not produce a nontrivial inclusion.

### 3.1 Exact abstract transfer

Work over $\mathbb C$ with a finite top-dimensional register $R$, $V=Z_d(R)$, and $C_{d+1}(R)=0$. Independent gadgets $Y_j$ intersect only inside $R$ and satisfy

$$B_d(Y_j)\cap V=\operatorname{ran}P_j.$$

For $X_A=\bigcup_{j\in A}Y_j$, set $W_A=\sum_{j\in A}\operatorname{ran}P_j$, $H_A=\sum_{j\in A}P_j$, and $r_A=\dim\ker H_A$. Disjoint off-register chain coordinates imply

$$B_d(X_A)\cap V=W_A,\qquad V/W_A\hookrightarrow H_d(X_A).$$

Let $\Delta_A$ be the **geometric** Laplacian on all $C_d(X_A)$, and $P_A$ the projector onto the embedded **logical** kernel $\ker H_A$. Assume every normalized full-chain vector of $\Delta_A$-energy below $E>0$ obeys

$$\|(I-P_A)x\|\le\eta<1.$$

Projection injects the entire $[0,E)$ spectral subspace into an $r_A$-dimensional space. The homological injection already gives at least $r_A$ exact zero modes. Thus the nullity is exactly $r_A$, the positive spectrum is at least $E$, and the register map is an isomorphism. For nested term sets these isomorphisms commute with the natural surjective quotient maps. Therefore the persistence numerator is $\dim\ker H_B$. The normalized ratio requires $r_A>0$; the anchored-history construction below fixes that denominator to a known input dimension $D>0$.

This conditional argument excludes extra gadget homology without a separate relative-acyclicity assumption. A torus attachment refutes independence alone, but violates the full-chain concentration hypothesis. An earlier short audit conflated $H_A$ and $\Delta_A$; its purported counterexample to the full conditional lemma is withdrawn. The substantive work is proving concentration with polynomially uniform constants, not the elementary dimension argument.

Positive coefficients can be erased: for $a_j>0$, $\ker\sum a_jP_j=\ker\sum P_j$, and the latter gap is at least the former gap divided by $\max a_j$. Negative coefficients or an energy shift are not covered.

### 3.2 Padded concentration and exact filling

The local derivation uses the fixed-size gadget spectral/nullity package, constant locality $m$, $t$ terms, and small common weight $\lambda$. It yields

$$1-\langle x,\Pi_Vx\rangle+\langle x,H_A^{\rm emb}x\rangle
\le C\left(t\lambda+t^2\lambda^2+tE/\lambda^{4m+2}\right).$$

For logical positive gap $g\le1$, this bounds $\|(I-P_A)x\|^2$ by the right-hand side divided by $g$. Choose $\lambda\le c\eta^2g/t$ and $E\le c\eta^2\lambda^{4m+2}g/t$. Common dyadic choices are polynomially encoded for fixed locality and inverse-polynomial $g,\eta$.

The key repair projects local central bulk onto **outside harmonics**. An unrestricted outside edge contributes a weight-one boundary and refutes the literal coordinate-bulk $O(\lambda)$ estimate. Each interface $L_j$ deletes a gadget's unique new vertex and satisfies $L_jL_j^\dagger\preceq\lambda^2N_jI$. Its input comes from the orthogonal off-register chain block of that gadget. Thus the combined map is the block row $L=[L_1\ \cdots\ L_t]$, with $LL^\dagger=\sum_jL_jL_j^\dagger$ and $\|L\|\le\lambda\sqrt{\sum_jN_j}\le\lambda\sqrt{N_*t}$. The output register may be shared; output orthogonality and one global tensor decomposition are unnecessary.

Exact filling can be deduced from the same local package: positive weight conjugation makes $B_d(Y_j,w)\cap V$ independent of $\lambda$; the harmonic projector limit places it inside the intended forbidden subspace; the known single-gadget nullity gives equality by dimension. This is a local deduction from explicit source facts, not an independent reproof of the spectral-sequence theorem.

Full derivations: [transfer and padding](../quantum_direction_selection/round2/NORMALIZED_PERSISTENCE_PROBE.md), [source and unweighting audit](../quantum_direction_selection/round2/UNWEIGHTING_AUDIT.md). The superseded ordinary-Hadamard implementation in the former is retained only as history; use the next addendum.

### 3.3 Rational weighted history and actual gate scope

Use the exact real gate set $G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}$. Replace an $H\otimes H$ gate by consecutive $\sqrt2H$ and $H/\sqrt2$ steps on the two work bits. The normalized three-term forbidden vectors give rational orthogonal projector matrices. The intermediate norm scale is $\sqrt2$ and returns to one; gain/loss pairs are consecutive and never terminate halfway.

This factorization and the supported gadget states are credited to Rudolph's Appendix D.1. Products with fixed basis guards use joins of implementing spheres and attaching maps. Arbitrary integer amplitudes alone do not prove a gadget exists. The maximum support locality of the explicit unary construction is six, so the safe exponent is $4m+2=26$, not eighteen.

The parallel source-gate audit also removes the restriction to paired Hadamards for exact real $\{X,\mathrm{CX},\mathrm{CCX},H\}$ circuits. Add one unmeasured **mixed** spectator qubit $a$, and replace every $H_j$ by $H_j\otimes H_a$. The resulting circuit factors as $U'=U\otimes H_a^h$, where $h$ counts Hadamards. With input isometry $J'=J\otimes I_a$ and output acceptance projector $P_{\rm acc}'=P_{\rm acc}\otimes I_a$, the acceptance sandwich gives $M'=M\otimes I_a$ for either parity of $h$. Input dimension and perfect multiplicity both double; their fraction and the acceptance spectral promise are unchanged. Existing clean work is retained. This elementary algebra does not establish an unrestricted complex-phase gate or promise-class equivalence.

For $L$ **clock positions**, $w_t=s_t^2\in[1,2]$ and $Z=\sum w_t\le2L$. In coordinates $\psi_t=s_tU_t\xi_t$, ordinary edges have energy $\frac12\|\xi_t-\xi_{t-1}\|^2$, and split edges have $\frac23\|\xi_t-\xi_{t-1}\|^2$. Weighted variance on the clean sector and telescoping from the input anchor on the dirty sector prove

$$g_1\ge\frac1{8L^2}.$$

If the acceptance operator $M$ has perfect subspace $S=\ker(I-M)$ and $M|_{S^\perp}\preceq I/3$, the final penalty compresses to $(I-M)/Z$, with off-perfect gap at least $1/(3L)$. The direct kernel/complement decomposition gives

$$g_2\ge\frac1{120L^3},\quad
\dim\ker H_1=D,\quad\dim\ker H_2=\dim S.$$

These bounds allow $S=0$. Nonempty final kernel is not required. Illegal unary clocks must be invariantly separated and penalized by at least one. The existing addendum supplies these guards and the weighted mean-zero calculation; an extra $L^{-1}$ loss from a generic geometric lemma is unnecessary.

For $f=\dim S/D$ and $p=\operatorname{Tr}M/D$,

$$f\le p\le\tfrac13+\tfrac23f.$$

Standard $p\ge2/3$ versus $p\le1/3$ thresholds yield $f\ge1/2$ versus $f\le1/3$. An additive $1/24$ estimate distinguishes them. Arbitrary separated trace thresholds do not suffice: $M=I/4$ and $M=0$ have different trace probabilities and the same zero perfect-space dimension. Approximate gate compilation cannot be used to preserve exact perfect acceptance.

The initial weighted-history mixture is efficiently approximately preparable from a maximally mixed valid input. Equal-rank projector distance at most $\eta$ implies normalized-mixture trace distance at most $\eta$; add actual preparation error explicitly. This does not assert exact free preparation of arbitrary harmonic mixtures.

Full proof: [weighted unary palette](../quantum_direction_selection/round2/UNARY_PALETTE_ADDENDUM.md), [fixture and threshold gates](../quantum_direction_selection/round2/FIXTURE_AND_SOURCE_GATES.md).

### 3.4 The decisive remaining question

Can the source be tied to a natural established quantum class, with exact gate and standard-threshold conventions, without importing an unproved perfect-completeness amplification? Until then the conclusion is a reduction from a **specified restricted circuit promise**, conditional on the fixed local gadget package. No unrestricted SDQC1 hardness or separation from BPP has been proved here.

A strong next paper needs either that precise complexity bridge, an independently source-complete general exact-kernel simulation theorem, or a materially stronger structural consequence. Calling the existing elementary min--max observation a new general method would not by itself justify a major-conference submission.

## 4. New Pro proposal: persistent-Laplacian spectral transfer

The retrieved TDA response proposes extending common-copy unweighting beyond ordinary harmonic spaces to all persistent Laplacians of a filtration. With shared copies $f_v=Mw(v)^2\in\mathbb N$, its candidate statement is

$$\widehat\Delta_k^{a,b}\cong M\Delta_{k,w}^{a,b}\oplus R_{a,b,k},
\qquad R_{a,b,k}\succeq\min_{v\in K_a} f_v I.$$

The local reconstruction identifies the restricted persistent-boundary domain with the block-fixed part of its blow-up. Group symmetry gives reducing sectors. Persistent domination $\Delta^{K,L}\succeq\Delta^K$ then transfers the ordinary asymmetric gap. That domination argument is already contained in Mémoli--Wan--Wang's monotonicity proof; it is not a new inequality. The combined low-spectrum transfer remains a candidate corollary whose exact novelty requires comparison.

See [self-contained reconstruction](PERSISTENT_SPECTRAL_TRANSFER.md) and [Pro original](responses/TDA_INITIAL.md). This structural result does not create a quantum algorithm or resolve exact normalized-counting hardness by itself.

## 5. Secondary and blocked directions

| Direction | Positive content retained | Obstruction / next gate |
|---|---|---|
| Quantum net to barcode | In a coherent whole-point oracle, expected $\widetilde O(\sqrt{nK})$ queries for an $\epsilon$-net of packing size at most $K$; classical PH on the net gives $2\epsilon$ bottleneck error | Non-query gates include $\operatorname{poly}(d,b)K\sqrt{nK}$ and $T_{PH}(K)$. Generic sampling/clustering collision is strong. Seek a new multiparameter tradeoff, not just composition. |
| One-dimensional barcode lower bound | Hidden-outlier OR family gives classical $\Omega(n)$ and quantum $\Omega(\sqrt n)$ point-query lower bounds at constant error | Use longest finite **bar length**, not maximum death coordinate of arbitrary approximate output. No preprocessing is free. |
| Generalized-rank projector method | Native Möbius zigzag: generalized rank one, uniformly positive module constraint gaps, overlap $\Theta(m2^{-m})$ | Local geometry/gaps do not imply usable global projector overlap. This is a conditioning counterexample, not a lower bound against every quantum algorithm. |
| AIDA local updates | Exact update rank equals the rank of the evaluated Hom images after the actual quotient | A one-direction candidate exchange can produce rank $t$ on a minimal presentation with indecomposable target. Need a natural bounded-evaluation-width class and a strong classical algebra baseline. |
| Compressed zigzag comparison complexes | Pro proposes a linear-size compiler and a global conditioning theorem | External proposal only. Check repeatable degree-transfer gadgets, space-time minors/torsion, output model, and same-access classical algorithms before using QSVT. |
| Reflection recompression | Pro suggests fresh compact representations after local kernel/cokernel reflections | External proposal only. One- and two-step recompression must avoid implicit basis output and multiplicative condition loss. |
| Hyperbolic neighbor search | Exact $d+1$ landmark-distance reconstruction; shell progress formula; same-access model audit | Fixed-dimensional classical indexing and landmarks defeat a naive list-scan baseline. Pro's optimized tangent cap is an additional proxy calculation, not a graph-routing impossibility theorem. |
| Hyperbolic LSH | Generic QRACM tradeoff exponent $\rho/(1+\rho)$ under explicit assumptions | Hash evaluation, radius, preprocessing, coherent bucket access, and growing dimension all matter. Known spherical filtering is a close collision. No positive whole-route quantum theorem currently survives. |

Detailed proofs and historical alternatives remain in [direction-selection README](../quantum_direction_selection/README.md). The four registered candidate abstracts are research intentions, not four completed papers; later kill tests and this ranking supersede their initial optimism.

## 6. Request to the collaborator

First review the exact transfer, padded concentration, supported palette, whole-kernel gap, state preparation, threshold restriction, and persistent spectral extension. Give the strongest counterexample or first unproved implication, not generic caution. Then push the strongest surviving direction as far as possible: prove a sharper theorem, resolve a dependency, identify a real classical collapse, or give a decisive counterexample. Separate locally derived lemmas, cited theorems, conjectures, negative findings, and novelty opinions. Preserve useful failed attempts with the exact point of failure.

Prioritize the current TDA problem in this conversation; the Ramsey portfolio is context, not a request to bundle unrelated theorems into one submission. Return an explicit manuscript-sized theorem package only if its correctness and significance can be defended. Otherwise give the strongest honest milestone and the smallest next falsification or proof target.
