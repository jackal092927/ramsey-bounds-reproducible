# Hyperbolic navigation: quantum-query feasibility probe

Date: 2026-09-02. Scope: read-only audit of the current NaviGraph sources plus a standalone mathematical probe. No manuscript, shared issue index, online Overleaf, or external account was changed. This is not a proof of the current paper or a claim of end-to-end quantum novelty.

## Outcome

**Do not pursue “Grover over the neighbors of the current fixed-dimensional graph” as the main theorem.** Its comparison to a classical exhaustive scan misses two stronger baselines: random-first-improving search, and finite-dimensional landmark reconstruction. The latter gives a classical $d+1$ exact-distance-query bound for an arbitrary neighbor list, after query-independent geometric preprocessing. This is the strongest local obstruction found in the probe.

Two possible follow-on directions are given below, but neither currently has a justified novel end-to-end quantum speedup. The recommended narrow target is to settle the access-model boundary first, using the proved landmark lemma and the shell calculation as cheap falsification gates.

## Current source boundary

Read the current NaviGraph workspace's `AGENTS.md`, the full `GAP_FIX_INDEX.md`, and active W1 files in `manuscript-repair-2026-09-02/`. The June Overleaf clone was not used as the current paper. The machine-specific workspace prefix was removed when preparing the GitHub research archive.

Observed SHA-256 source fingerprints (version identifiers, not proof certificates):

```text
GAP_FIX_INDEX.md  8e438fbddd724949e593f544755b7523a85f4688c7cc93e5bf8289d6c3d0e063
yao.tex          efde09979b30be52ec7f1a925fca6e939869c0a79ed8166879d8c45f7c657035
ANNS.tex         a111fcb8f9dc2cbc6638045dd9deb46749eadcf0792af43dcf7fefcfd6c2db3e
steiner.tex      a27244347e0802d2f0fe0879bc5f81a5734e5ebe56e1944ed351e9c4dc64ce4d
```

| Active W1 statement | Actual assumptions and guarantee | Quantum implication |
|---|---|---|
| `yao.tex`, `thm:yao` | Fixed $d,D$; a nearest-in-cone graph; $O_{d,D}(n)$ edges; exact data-point targets at source-target distance at most $D$; no short-hop guarantee | Constant local degree already makes per-neighbor Grover irrelevant to $n$ |
| `yao.tex`, `thm:local-yao-hop` | Fixed common local set $X_C\subset B(o,r)$; cutoff $2r$; one shared permutation; labeled cones; specified frozen-cap/minimum-priority phases; expected $O_{d,D,r}(\log^2 n)$ hops; rejected-permutation variant has maximum out-degree $O_{d,D,r}(\log n)$ | Replacing each exact prescribed minimum with quantum minimum-finding is a generic conditional wrapper, not a geometry-derived hop improvement |
| `steiner.tex`, `thm:steiner-hops` | $O_d(n)$ Steiner vertices; $O_d(n\log n)$ arcs; degree $O_d(\log n)$; specified route, not every closer-neighbor choice; independent local permutations after deterministic global entry | A hop theorem does not imply its neighbor-inspection cost; quantum random-improving choices do not automatically preserve the prescribed route |
| `ANNS.tex`, `thm:ann-corrected` | Fixed $d,\epsilon$; additive-AVD entry; linear storage; maximum out-degree $O_{d,\epsilon}(1)$; at most $n-1$ strict local moves and $O_{d,\epsilon}(n)$ local work | Grover does not shorten the possible chain; there is no asymptotic degree dependence on $n$ to remove |

The index marks W1 local routing as locally reviewed. It explicitly leaves the original fast greedy ANN and arbitrary-diameter general non-Steiner conclusions unresolved/withdrawn. These observations identify which hypotheses are available; they are not an independent reproof of W1.

## Primary-source literature collisions

| Source | Verified relevance |
|---|---|
| [Malkov and Yashunin, HNSW](https://arxiv.org/abs/1603.09320), section 4.2.1 | The rigorous scaling discussion assumes exact Delaunay graphs and bounded average degree; actual HNSW uses approximate pruning and empirical robustness. Do not import universal logarithmic HNSW guarantees. |
| [Xia, Tian, Yuan, Deng, IJCAI 2025](https://www.ijcai.org/proceedings/2025/739), sections 4.3–4.4 | Explicit quantum HNSW construction and search already exist. “First quantum HNSW” is unavailable. Their work also invokes QRAM, angle encoding and swap tests; the broad title collision is decisive without accepting every complexity claim. |
| [Dürr and Høyer, minimum finding](https://arxiv.org/abs/quant-ph/9607014) | Searching an unstructured list for its minimum costs $O(\sqrt{\Delta})$ queries at constant success probability. Applying this at each visited vertex is a known primitive. |
| [Boyer, Brassard, Høyer, Tapp](https://arxiv.org/abs/quant-ph/9605034) | If exactly $m>0$ of $\Delta$ unstructured neighbors meet a progress predicate, quantum search costs $O(\sqrt{\Delta/m})$ expected queries, including unknown $m$. |
| [Prokhorenkova et al., ICLR 2022](https://openreview.net/pdf/2b964b236bad8988bed9b9b8c8ec33f189b77f1b.pdf) | Prior work already analyzes graph-based hyperbolic NNS under a uniform-in-ball data model and radius/dimension conditions. The abstract and introduction were read; the complete theorem proof was not audited. |
| [Kisfaludi-Bak and van Wordragen, SoCG 2024](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2024.68) | For fixed $d,\epsilon$, unrestricted geometric ANN already has $O_{d,\epsilon}(n)$ space and $O_{d,\epsilon}(\log n)$ query time. Any broader ANN claim must beat or distinguish this model, not just HNSW scanning. |
| [Tabaghi and Dokmanić, KDD 2020](https://arxiv.org/abs/2005.08672) | Hyperbolic distance Gramians and Lorentzian factorization are established. The landmark result below is an elementary consequence used here as a model audit, not claimed as novel distance geometry. |
| [Deng, Gao, Lu, Luo, Xin, SoCG 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2026.39) | The user's own hyperbolic LSH line provides a more direct adjacent time-space tradeoff target. The paper gives native hyperbolic hashing and, in $\mathbb H^2$, $\rho\le1/c$. A quantum extension still needs its own collision audit. |

These were bounded targeted searches, not an exhaustive novelty review.

## Claim A: landmark obstruction to a distance-query speedup

### Status

**PROVABLE AS STATED**, under the explicit exact-real oracle and preprocessing model below. This is a standalone classical upper bound, not a quantum algorithm and not a new-paper novelty claim.

### Assumptions and notation

Let $Y\ne\varnothing$ be a finite set in curvature-$-1$ hyperbolic space $\mathbb H^d$. Data geometry is available during query-independent preprocessing, either as coordinates or through exact pairwise distance queries. At query time an oracle returns the exact distance $d(q,y)$ for a requested $y\in Y$. Only calls to this oracle are charged. Arithmetic and access to preprocessed coefficients are separately accounted for, not claimed free in an actual runtime model.

Use the hyperboloid representation

$$B(x,y)=x_0y_0-\sum_{j=1}^d x_jy_j,\qquad B(x,x)=1,\quad x_0>0,$$

so $B(x,y)=\cosh d(x,y)$. Let $W=\operatorname{span}(Y)$ and $s=\dim W\le d+1$.

### Exact claim

There are anchors $a_1,\ldots,a_s\in Y$ and query-independent coefficients $\alpha_y\in\mathbb R^s$ such that for every $q\in\mathbb H^d$,

$$\cosh d(q,y)=\sum_{i=1}^s\alpha_{y,i}\cosh d(q,a_i)\quad(y\in Y).$$

Thus all query-distance comparisons, the exact nearest neighbor, or a minimum-priority member of any distance-threshold subset can be computed with at most $d+1$ exact query-distance oracle calls and $O(d|Y|)$ additional arithmetic operations. Coefficient storage is $O(d|Y|)$. If coordinates are initially unknown, $O(d|Y|)$ query-independent pairwise distance calls suffice to obtain such a representation.

### Strategy and dependency map

1. The hyperboloid distance formula converts distances to bilinear scores.
2. A span containing a timelike vector has nondegenerate restricted Lorentz form.
3. A basis Gram matrix therefore recovers each data vector's coefficients.
4. Bilinearity reconstructs its query score, even if $q\notin W$.

### Proof

1. Choose a basis $a_1,\ldots,a_s$ of $W$ from $Y$. A Lorentz isometry sends the timelike vector $a_1$ to $(1,0,\ldots,0)$. In these coordinates, $W$ is the direct sum of its time axis and a spatial subspace. The restriction of $B$ is positive on the time axis and negative definite on that spatial subspace. Hence it is nondegenerate.

2. Therefore the Gram matrix $G_{ij}=B(a_i,a_j)=\cosh d(a_i,a_j)$ is invertible. For any $y\in Y$, define $g_y=(\cosh d(a_i,y))_{i=1}^s$. Since $y\in W$, its unique coefficients satisfy

$$y=\sum_i\alpha_{y,i}a_i,\qquad G\alpha_y=g_y,$$

so $\alpha_y=G^{-1}g_y$ is computable before the query.

3. At query time obtain $b_i=\cosh d(q,a_i)$ using $s$ distance calls. Bilinearity gives $B(q,y)=\alpha_y^Tb$, proving the formula. The monotonicity of $\cosh$ on $[0,\infty)$ preserves distance order and thresholds. Reconstructing all scores uses $O(s|Y|)$ arithmetic.

4. With pairwise-distance-only preprocessing, grow a basis greedily. Test a point by obtaining its distances to the current anchors and checking the enlarged Gram determinant. The enlarged Gram is nonsingular exactly when the point increases the span: every tested span still contains a timelike anchor, so the preceding nondegeneracy argument applies. At most $d+1$ anchors are added. Fill missing distances from each final anchor to all data points. At most $O(d|Y|)$ distinct pairwise queries are needed. This proves the claimed preprocessing/query/storage bounds. $\square$

### Stable-score refinement

Choose, among bases of $W$ drawn from $Y$, one maximizing absolute coordinate determinant in any fixed basis of $W$. For any $y\in Y$, replacing anchor $i$ by $y$ multiplies that determinant by $\alpha_{y,i}$. Maximality therefore implies $|\alpha_{y,i}|\le1$ for every $i,y$. Consequently

$$\|\alpha_y\|_1\le s.$$

If the oracle gives scores $\widetilde b_i$ with $|\widetilde b_i-\cosh d(q,a_i)|\le\xi$, then reconstructed scores have error at most $s\xi$. An exact score gap larger than $2s\xi$ therefore suffices to preserve a pairwise ordering. This assumes exact preprocessing; it does not bound errors in the geometry itself. A maximum-volume basis may be found after the representation above is constructed, without new oracle calls; no efficient high-dimensional maximum-volume algorithm is claimed.

For distance noise $|\widetilde r_i-r_i|\le\tau$ with nonnegative distances, the induced score error is at most $\tau\sinh(r_i+\tau)$. Thus a statement for bounded additive score error is not silently a uniform statement for bounded additive distance error at arbitrary radii.

### Implication for local graph search

Apply the lemma separately to $Y=\mathcal N(p)\cup\{p\}$. All anchors are locally available points. This uses only constant-factor additional storage per adjacency list when $d$ is fixed. It defeats a $\Theta(\Delta)$ classical distance-query lower bound for selecting an improving neighbor, if such local geometric preprocessing is allowed. It does **not** prove constant total runtime, few graph hops, low precision cost, or a lower bound against arbitrary quantum algorithms. If one instead forbids access to neighbor geometry and pairwise-distance preprocessing, that is a different oracle model which must be stated and motivated.

## Claim B: progress-density law on a hyperbolic shell

### Status and assumptions

**PROVABLE AS STATED as a one-step geometric statement.** A multi-step graph-routing theorem is **NOT CURRENTLY JUSTIFIED** by this statement.

Let $d(p,q)=R>0$. Draw a candidate $u$ uniformly in direction on the radius-$R$ sphere about $p$. Fix $0\le\delta<R$. Let $\gamma$ be the angle at $p$ between $q$ and $u$.

### Exact law and proof

The hyperbolic cosine law gives

$$\cosh d(u,q)=\cosh^2R-\sinh^2R\cos\gamma.$$

Hence $d(u,q)\le R-\delta$ is exactly the spherical cap

$$\gamma\le\theta_{R,\delta},\qquad
\theta_{R,\delta}=2\arcsin\sqrt{\frac{\cosh(R-\delta)-1}{2\sinh^2R}}.$$

Its probability in $\mathbb H^d$, for $d\ge2$, is

$$p_d(R,\delta)=\frac{\int_0^{\theta_{R,\delta}}\sin^{d-2}t\,dt}{\int_0^\pi\sin^{d-2}t\,dt}.$$

For fixed $d,\delta$ as $R\to\infty$,

$$\theta_{R,\delta}\sim2e^{-(R+\delta)/2},\quad
p_d(R,\delta)\sim C_de^{-(d-1)(R+\delta)/2},\quad
C_d=\frac{2^{d-1}}{(d-1)\int_0^\pi\sin^{d-2}t\,dt}.$$

The first asymptotic follows by substituting $\cosh(R-\delta)\sim e^{R-\delta}/2$, $\sinh R\sim e^R/2$, and $\arcsin z\sim z$. The second follows from $\sin t\sim t$ in the cap integral. These are positive-radius, fixed-progress asymptotics, not uniform estimates as $\delta$ approaches $R$.

### Same-access random classical comparison

For a fixed list with $m$ qualifying neighbors out of $\Delta$, random sampling with replacement finds one in expected $\Delta/m$ tests; a random order without replacement takes $(\Delta+1)/(m+1)$ tests. BBHT quantum search takes $O(\sqrt{\Delta/m})$ expected predicate calls. It is wrong to compare this only to exhaustive $\Delta$ scanning when $m\gg1$.

In the ideal shell sampling proxy, expected guaranteed progress per predicate call is proportional to $\delta p_d(R,\delta)$ classically and $\delta\sqrt{p_d(R,\delta)}$ quantumly. Maximizing the leading asymptotic functions gives

$$\delta_C=\frac{2}{d-1},\qquad \delta_Q=\frac{4}{d-1}.$$

These optimize a **one-step guaranteed-progress proxy**. They are not optimal routing policies. A fixed-degree random graph may have no qualifying neighbor at all, and subsequent neighborhoods are neither fresh independent shells nor necessarily centered at the current query scale. No adaptive-density lemma has been proved here.

### Additional obstructions

- Hyperbolic geometry alone imposes no useful-neighbor density: an arbitrary number of candidates can lie in the bad angular region while one lies in the good cap.
- In $\mathbb H^2$, an equal-radius shell whose directions are sorted can be searched classically by taking the angular predecessor/successor of the target direction, in $O(\log\Delta)$ comparisons and $O(\Delta)$ storage. The raw $\Delta/m$ benchmark is not the best geometrically indexed benchmark.
- Claim A gives the stronger exact-distance-query obstruction even without equal radii or sorted directions.

## Two candidate directions and stop/go gates

### 1. Oracle-aware hyperbolic routing: a separation only when geometric information is genuinely limited

Target a rigorously specified local, comparison-only or finitely encoded/coherently accessed oracle model. Prove a separation for a whole route, not just one call to minimum finding; both algorithms receive identical preprocessing, local labels, precision and point access. The graph must be generated independently of the query, and good-neighbor density must hold along adaptive histories.

**Current evidence:** only the known quantum search primitive plus the shell lemma. **Fatal gate:** if exact geometric landmarks or query coordinates are available without charge, the claimed distance-query separation collapses. If only fixed $d,\epsilon$ ANN is intended, existing classical $O(\log n)$ ANN is an additional baseline. **GO only if** a natural resource restriction survives both tests and yields a non-logarithmic end-to-end improvement. **Otherwise NO-GO.**

### 2. Robust multiscale progress versus degree, using the shell law

Target the explicit radius/accuracy dependence rather than the dataset-size dependence: construct a query-independent sparse multiscale graph, prove an adaptive lower bound on useful-neighbor density with a specified progress margin, and optimize the quantum versus classical random-progress policies. The quantum preference for a larger progress threshold is a concrete mechanism to test; it is not present in a literal “same path, faster scan” wrapper.

**Current evidence:** exact shell probability and proxy-optimal thresholds. **Main missing theorem:** a fixed graph construction preserving the required density after conditioning on its actual route, while not admitting a better classical angular/range index or landmark reconstruction. **GO only if** the advantage survives the best same-access geometric index and the graph's storage/precision costs. **Otherwise NO-GO.**

### Recommendation

Do the short access-model theorem first, not a new large navigation experiment. Claim A is already a complete local obstruction. A credible positive project must specify why it does not apply. If the desired task is ordinary low-dimensional hyperbolic ANN with standard preprocessing, the present evidence favors stopping the quantum-neighbor wrapper and considering the user's hyperbolic LSH time-space/precision line instead. No claim is made here that quantum LSH is novel or solved.

## Reproducible checks

`probe.py` uses only the Python standard library and fixed seeds. Command:

```text
python3 research/quantum_direction_selection/hyperbolic_probe/probe.py
```

Observed: **PASS**. Score reconstruction errors were at most $1.78\times10^{-15}$ for full-dimensional $\mathbb H^2$ and $\mathbb H^3$ point sets and for a geodesic embedded in $\mathbb H^5$. Maximum-volume coefficients obeyed $|\alpha_i|\le1$ in all checked cases; adversarial score perturbations obeyed the $s\xi$ bound. At $R=12$, grid-optimized shell proxy thresholds were $(2,4)$ for $d=2$ and $(1,2)$ for $d=3$, matching the asymptotic calculations. These finite numerical checks are sanity tests, not replacements for the proofs or evidence for a complete quantum routing theorem.

## Open risks

- The landmark lemma is elementary and likely overlaps standard distance-geometry techniques; no novelty is claimed.
- Exact-real query complexity and bit/gate complexity are different resources. Coherent state preparation, comparisons, QRAM/preprocessing, precision and failure probability must be charged in a positive quantum theorem.
- The numerical probe checks only the isolated statements above, not W1 construction, its random permutation argument, or any ANN result.
- Neither candidate is presently a publishable end-to-end quantum theorem. The main useful deliverable is a strong falsification result for the generic neighbor-search direction.
