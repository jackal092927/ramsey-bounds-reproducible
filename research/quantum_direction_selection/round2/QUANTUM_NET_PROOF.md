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
