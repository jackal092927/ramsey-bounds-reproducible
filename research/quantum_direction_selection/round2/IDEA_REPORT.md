# Quantum TDA: round-2 direction decision and proof progress

Date: September 2, 2026 PDT. This report supersedes the exploratory rankings in the first-round decision and in `IDEA_GENERATION_54.md`. It is a research milestone, not a submission-ready paper or a claim of priority.

## Decision

Focus on **true normalized persistence**, with a bounded secondary track on quantum geometric sampling for barcode approximation. Keep direct Dey–Xin / AIDA quantization as a structural question rather than forcing a generic quantum linear-algebra wrapper.

| Priority | Concrete target | Current evidence | Principal unresolved issue |
|---|---|---|---|
| Main | Exact conversion from a specified circuit's perfect-acceptance fraction to a filtration's surviving-homology fraction | Abstract transfer proof, padded-gadget repair, explicit supported history palette, two finite fixtures | Full literature dependency integration, precise hardness scope, novelty |
| Secondary | Quantum epsilon-net followed by additive barcode approximation | Query upper-bound proof and a matching fixed-scale one-dimensional lower-bound family | Likely close to known quantum clustering / classical TDA composition |
| Hold | Quantizing Dey–Xin / Dey–Jendrysiak–Kerber decomposition | Existing counterexamples eliminate two naive speedup mechanisms | A natural bounded evaluated-Hom-width class, not an assumed condition number |

## 1. Main direction in plain language

A persistent topological feature is a hole that remains when more simplices are added. The target statistic is the fraction of the initial holes that survive. We want to encode a quantum circuit so that this fraction equals the fraction of inputs it accepts with certainty.

The important distinction is **actual holes, represented by exact zero modes**, versus merely small positive eigenvalues. Good low-energy approximation by itself does not establish the desired topological count. The construction below obtains exact classes topologically first and then uses a dimension argument to exclude extra low-energy modes.

The July [normalized-persistence preprint](https://arxiv.org/html/2607.03278v1) already defines this normalization and identifies a hardness conjecture. We are not inventing the statistic. Its proved quasi-persistence result does not immediately give the true statistic: its equal-complex hard family has true survival fraction one. Our target is the missing exact rank-transfer step, under a narrower, explicit circuit promise.

## 2. Candidate theorem, with its exact scope

Use the fixed real gate set $G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}$. Let $M$ be the acceptance operator on a valid input space of dimension $D>0$, and $S=\ker(I-M)$. Assume $M|_{S^\perp}\preceq I/3$. The source decision promise is specifically

$$\operatorname{Tr}(M)/D\ge2/3\quad\text{or}\quad\operatorname{Tr}(M)/D\le1/3.$$

The proposed construction gives a nested pair of weighted clique complexes $X_1\subseteq X_2$, in a degree that grows with circuit size, for which

$$\beta_d(X_1)=D,\qquad
\operatorname{rank}[H_d(X_1)\to H_d(X_2)]=\dim S.$$

Both Laplacians have inverse-polynomial positive gaps. Their normalized true persistence is therefore

$$q=\frac{\beta_d^{1,2}}{\beta_d(X_1)}=\frac{\dim S}{D}.$$

YES implies $q\ge1/2$ and NO implies $q\le1/3$. An additive $1/24$ estimate distinguishes them. An efficiently preparable approximate initial harmonic mixture is provided with an explicit error budget; exact free preparation of an arbitrary harmonic space is not assumed.

**Status:** local proofs are written for the transfer, interference repair, weighted history, and threshold inference. The concrete local gadget spectral/nullity package is imported from the stated sources. This is not an independently re-proved topology package, an unrestricted SDQC1-hardness result, or an established exponential separation from classical computation. We have not shown that this restricted circuit promise is outside BPP.

## 3. What changed mathematically this round

### 3.1 Exact quotient plus dimension, rather than exact harmonic representatives

For logical projectors $P_j$, independent gadget attachments kill exactly $W_A=\sum_{j\in A}\operatorname{ran}P_j$ among register cycles. The register quotient $V/W_A$ injects into geometric homology. A low-energy concentration estimate for the **geometric** Laplacian toward the **logical** kernel bounds the whole geometric low-energy dimension by $\dim\ker\sum_jP_j$.

The topological injection supplies that many exact zero modes. Hence it is an isomorphism, and all other eigenvalues lie above the chosen threshold. Under adding more projectors the maps are the natural quotient maps; one need not preserve particular harmonic representatives exactly. Full proof: [NORMALIZED_PERSISTENCE_PROBE.md](NORMALIZED_PERSISTENCE_PROBE.md).

This is the candidate new organizing argument. Its novelty still requires comparison with all relevant proofs, not merely absence of the same wording.

### 3.2 A padding estimate needed repair

The literal coordinate-bulk estimate in [King–Kohler arXiv v2](https://arxiv.org/html/2311.17234v2) allows a weight-one outside boundary term. We replaced it by local bulk tensored with **outside harmonics**, where that term vanishes. We also bounded interference among different gadgets by $O(\lambda\sqrt t)$ and retained term-count-dependent errors throughout.

This yields the usable remainder

$$C\bigl(t\lambda+t^2\lambda^2+tE/\lambda^{4m+2}\bigr),$$

conditional on the fixed-size local spectral package. The earlier argument in the June [published quantum-persistence paper](https://journals.aps.org/prxquantum/pdf/10.1103/gvys-hl8h) also invokes a simulated-register estimate outside its stated domain. We do not use that invocation as a substitute for the arbitrary-state argument. These are precise proof-scope observations, not a claim that the published theorems are false.

### 3.3 Replaced an unsupported generic gadget assumption

Integer amplitudes alone do **not** justify every constant-local gadget. Instead, consecutive transitions $\sqrt2H$ and $H/\sqrt2$ reproduce $H\otimes H$ while using only explicitly supported three-term states and fixed-basis guards.

The factorization and product-gadget technique are **Rudolph's existing ideas**, credited to [Appendix D.1 of arXiv v2](https://arxiv.org/html/2411.02681v2#A4.SS1), not inventions of this exploration. Our use adapts them to the exact-kernel counting construction and its weighted unary history. Its maximum locality is six, so the safe gadget exponent is **26**, not the exponent 18 from a different four-local construction.

Complete weighted variance and anchored-path proofs give

$$g_1\ge1/(8L^2),\qquad g_2\ge1/(120L^3),$$

including zero final kernel. See [UNARY_PALETTE_ADDENDUM.md](UNARY_PALETTE_ADDENDUM.md).

### 3.4 Restricted a threshold inference that does not hold in general

For an off-perfect acceptance bound $r$, the exact inequality is $f\le p\le r+(1-r)f$. Arbitrarily separated trace thresholds do not automatically separate $f$. The example $M=I/4$ versus $M=0$ has different trace fractions but identical perfect-acceptance fraction zero. The standard $2/3$ versus $1/3$ promise avoids this issue directly, without an exact-gate amplification claim. See [FIXTURE_AND_SOURCE_GATES.md](FIXTURE_AND_SOURCE_GATES.md).

### 3.5 Unweighting is available downstream, not the main novelty claim

Using fixed dyadic weights and the same multiplicities at both filtration levels preserves both Betti counts and the induced rank under the local common-copy lemma. Thus it preserves their ratio. Changing a vertex's multiplicity between levels does not automatically preserve the normalized inclusion map. The [August unweighted-homology preprint](https://arxiv.org/html/2608.02726v1) is a close source; a standalone weighted-to-unweighted claim is likely much less novel than the exact-kernel transfer.

## 4. Secondary algorithm: quantum net to barcode

In the coherent whole-point oracle model, with a known bound $K$ on the size of an epsilon-packing, adaptive quantum search finds an epsilon-net using expected

$$\widetilde O(\sqrt{nK})$$

point queries. Compute persistence classically on those at most $K$ points. For the Rips convention using pairwise-distance threshold $r$, the bottleneck error is at most $2\epsilon$. The non-query arithmetic depends polynomially on dimension, coordinate precision and $K$; full-data quantum-memory construction is not free.

For bounded one-dimensional geometry and constant error, $K$ is constant. A single hidden outlier changes the longest finite $H_0$ bar by a constant. This gives classical $\Omega(n)$ versus quantum $\Theta(\sqrt n)$ query complexity up to logarithms, in the same no-preprocessing point-oracle model. The reduction uses **bar length**, not the largest death coordinate of an arbitrary approximate output.

This is a concrete algorithmic candidate, but its building blocks have close precedents:

- [Kolbe–Mayr, ICALP 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.131/LIPIcs.ICALP.2026.131.html): classical covers and additive barcode approximation in bounded low-dimensional geometry.
- [Aïmeur–Brassard–Gambs, Machine Learning](https://link.springer.com/article/10.1007/s10994-012-5316-5): early quantum center-selection/clustering methods; we do not claim first quantum farthest-first sampling.
- [Xue–Chen–Li–Jiang, ICML 2023](https://proceedings.mlr.press/v202/xue23a.html): quantum clustering coresets with square-root input-size dependence.
- [Fukuzawa–Goodrich–Irani, SoCG 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.51): output-sensitive quantum geometric algorithms with a related complexity form.

Full proof and model boundaries: [QUANTUM_NET_PROOF.md](QUANTUM_NET_PROOF.md). A new parameter tradeoff, geometric structure theorem, or matching multi-parameter lower bound would be needed before relying on this as a strong conference contribution.

## 5. Relation to the user's existing work

[Dey–Xin generalized persistence](https://arxiv.org/abs/1904.03766v7), [Dey–Xin unfolding](https://arxiv.org/html/2403.08110v4), and [Dey–Jendrysiak–Kerber decomposition](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.41/LIPIcs.SoCG.2025.41.html) remain the most direct intellectual continuation. We have not quantized those full algorithms.

Two cheap tests already excluded naive paths: a native simplicial zigzag has well-conditioned local constraints but exponentially small global projector overlap; and a one-direction candidate exchange can have large evaluated update rank after the actual AIDA quotient. The next useful direct-follow-up question is a natural module family with bounded **evaluated Hom width**, not another assumed low-rank-update wrapper. No claim is made that the entire Dey–Xin route is impossible.

## 6. Executed checks and their limits

| Check | Observed result | What it checks |
|---|---|---|
| Independent cone-filling filtration, 16 vertices | Degree-three Betti counts $4\to2\to1$; successive map ranks $2,1$ for four positive weights | Quotient topology and weighted numerical implementation |
| Two weighted-history circuits | Kernel pairs $(4,1)$ and $(4,3)$; fractions $1/4,3/4$ | Projectors, history isometry, output compression and finite gaps |
| Padded-bulk exact arithmetic | Outside unit-weight contribution survives in coordinate bulk but cancels on outside harmonics | Specific failed estimate and the replacement projection |
| One-dimensional barcode lower-bound fixture | All 2080 singleton positions for sizes 1 through 64 pass the exact bar-length separation | Boundary cases, correct stable statistic and hidden-outlier construction |

Analytic proofs are separate from the numerical checks. These are classical linear-algebra fixtures, not quantum hardware runs, not full large clique-gadget simulations, and not timing evidence of quantum speedup. The probes run locally in less than a second each; Sirius would add overhead at this stage and was not used for this round.

## 7. Review and communication state

Both previously approved personal ChatGPT Pro packets were **sent**, and their tabs handed off: [TDA audit](https://chatgpt.com/c/6a98c05a-ecf4-83e8-b356-4e20dc3fde3f), [backup hyperbolic discussion](https://chatgpt.com/c/6a98c210-7ff0-83e8-a292-71cd7b079bae). The new round-2 proofs were not included. No completed Pro response has been collected.

The first broad independent Claude review timed out with no verdict. A narrower mathematical review completed and its objections were evaluated individually. It led to writing out the weighted path constants and clarifying the two operators; it did not certify the whole reduction. See [raw response](CLAUDE_NARROW_REVIEW.md) and [resolution](REVIEW_RESOLUTION.md).

Nothing here has been submitted, publicly pushed, or merged into the existing quantum Ramsey or NaviGraph manuscripts.

## 8. Next finite milestone

Prepare a single self-contained restricted normalized-persistence theorem with an explicit table mapping every imported local gadget fact to its source, and check whether this is a new consequence rather than already contained in the sources. Compare the completed Pro response when retrieved; a new packet containing these substantially newer proofs requires its own sending confirmation. If the restricted circuit source is too weak to support a meaningful hardness conclusion, retain the transfer theorem as structural progress and redirect effort to the geometric algorithm's nontrivial parameter regime. Do not label either route submission-ready before those checks.
