# Completed prior hyperbolic Pro response

Collected September 2, 2026 PDT from the registered [Quantum Hyperbolic Navigation Review](https://chatgpt.com/c/6a98c210-7ff0-83e8-a292-71cd7b079bae). The same Chrome ChatGPT account had been visibly verified against the personal Pro channel registry. UI showed a completed answer, “Worked for 41m 54s”. This is the already authorized backup topic; no new hyperbolic request was sent during this collection.

Advisory model output only. The current local priority remains TDA. This archive is not an audit or update of the separate NaviGraph manuscript. Rendered text and displayed LaTeX were extracted from the response DOM; formatting is reconstructed, and multi-source citation pills may expose only their first link. No sidebar or account-settings content is included.

---

# Verdict

**I recommend stopping the standard-model direction.** I do not find a defensible hyperbolic-specific quantum advantage for worst-case nearest-neighbor retrieval or navigation once the classical algorithm receives the same static geometry, preprocessing space, and numerical access.

Three independent obstructions survive scrutiny:

- **The landmark reconstruction is correct, and stronger globally than locally.** All query-to-dataset distances factor through at most $s\le d+1$ query-dependent scalars. A quantum algorithm can accelerate a subsequent generic linear-score search, but it does not reduce the geometric information acquisition below a classical $s$-query reconstruction.

- **The supplied progress-cap calculation is correct only when the edge length is constrained to equal $R$.** Optimizing the edge length gives a much larger cap whose far-field size is independent of $R$. That destroys the hoped-for long-range, exponentially sparse “good direction” mechanism.

- **Growing dimension does not reveal a uniquely hyperbolic filter problem.** A common-radius shell is exactly spherical maximum-inner-product search, while a small hyperbolic ball approximates Euclidean ANN arbitrarily well. Existing quantum LSF work already includes coherent structured-filter sampling and QRAM bucket access, so “sample relevant filters coherently, then search” is not a new hyperbolic mechanism.  [source](https://arxiv.org/html/2410.15565v1)

What remains potentially publishable is a **no-go theorem package**, not a positive quantum ANN algorithm.

---

## 1. Audit of the landmark reconstruction

Let

$\mathbb H^d
=
\{x\in\mathbb R^{d+1}:B(x,x)=1,\ x_0>0\},
\qquad
B(x,y)=x_0y_0-\sum_{j=1}^d x_jy_j.$

For $Y\subset\mathbb H^d$, let $W=\operatorname{span}(Y)$ and $s=\dim W$.

### 1.1 The restricted Lorentz form really is nondegenerate

Pick any $a\in Y$. Since $B(a,a)=1$, $a$ is timelike. For every $w\in W$,

$w=B(w,a)a+\bigl(w-B(w,a)a\bigr),$

and the second term lies in $W\cap a^\perp$. Thus

$W=\operatorname{span}\{a\}\oplus (W\cap a^\perp).$

The form is positive on $\operatorname{span}\{a\}$ and negative definite on $a^\perp$. Hence $B|_W$ has signature $(1,s-1)$ and has zero radical. Therefore every linear basis $a_1,\ldots,a_s$ of $W$ has an invertible Lorentz Gram matrix

$G_{ij}=B(a_i,a_j)=\cosh d(a_i,a_j).$

So the core nondegeneracy argument is sound.

This is consistent with the established Lorentzian-Gramian treatment of hyperbolic distance matrices; the broad Gramian observation is not new distance geometry.  [source](https://arxiv.org/abs/2005.08672)

### 1.2 Exact global factorization

Write

$y=\sum_{i=1}^s\alpha_{y,i}a_i.$

For any query $q\in\mathbb H^d$, with no requirement that $q\in W$,

$\cosh d(q,y)
=
B(q,y)
=
\sum_{i=1}^s\alpha_{y,i}B(q,a_i)
=
\sum_{i=1}^s\alpha_{y,i}\cosh d(q,a_i).$

Define

$z(q)_i=\cosh d(q,a_i), \qquad
\alpha_y=(\alpha_{y,1},\ldots,\alpha_{y,s}).$

Then every dataset score is simply

$c_y(q)=\alpha_y^\top z(q).$

This gives the stronger global statement:

**Global landmark factorization.**

One basis for the span of the entire static dataset or graph suffices. Every comparison made anywhere along a route is a comparison between two fixed linear forms in the same $s$-dimensional query vector $z(q)$.

In particular,

$d(q,x)<d(q,y)
\quad\Longleftrightarrow\quad
(\alpha_x-\alpha_y)^\top z(q)<0.$

Thus the query dependence of the entire route is compressed into at most $s\le d+1$ real numbers.

There is one model distinction:

- In a normal static geometric data-structure model, use one global basis and evaluate its $s$ query distances once.

- In a deliberately local model forbidding nonlocal anchor access, a basis for $\operatorname{span}(N[v]\cup\{v\})$ still uses at most $d+1$ local query distances per vertex.

Either version invalidates a generic $\Delta$-distance-query classical baseline.

### 1.3 Pairwise-distance-only preprocessing

Once anchors are known,

$b_y=\bigl(B(a_1,y),\ldots,B(a_s,y)\bigr)^\top$

is obtainable from $s$ anchor-to-point distances, and

$G\alpha_y=b_y.$

An exact incremental basis can also be found from distance Gramians: an enlarged Gram determinant is nonzero exactly when the enlarged set is linearly independent, because every such span contains a timelike point and hence has nondegenerate restricted form.

A straightforward accounting is therefore:

$\begin{array}{ll}
\text{pairwise-distance calls in preprocessing} & O(ns),\\
\text{preprocessing arithmetic} & O(ns^2+s^3),\\
\text{coefficient storage} & O(ns),\\
\text{query-to-point distance calls} & s,\\
\text{explicit evaluation of all scores} & O(ns).
\end{array}$

The $O(ns)$ figure applies to stored coefficients and query-time evaluation; solving all dense systems is ordinarily $O(ns^2)$, not $O(ns)$.

### 1.4 The maximum-volume coefficient bound is correct

Suppose $A=[a_1|\cdots|a_s]$ maximizes

$|\det(A^\top J A)|$

over anchor bases drawn from $Y$, where $J=\operatorname{diag}(1,-1,\ldots,-1)$.

If $y=A\alpha_y$ and $A_i(y)$ denotes $A$ with column $i$ replaced by $y$, then

$A_i(y)=A M_i,
\qquad
\det M_i=\alpha_{y,i}.$

Consequently,

$\det\!\bigl(A_i(y)^\top J A_i(y)\bigr)
=
\alpha_{y,i}^2\det(A^\top J A).$

Maximality gives

$|\alpha_{y,i}|\le 1.$

Therefore, if every anchor score has additive error at most $\xi$,

$|\widehat c_y-c_y|
\le
\sum_i|\alpha_{y,i}|\xi
\le s\xi.$

That part is valid.

### 1.5 What maximum volume does **not** solve

It does not bound the condition number of $G$. The simplest counterexample already uses two anchors at distance $\varepsilon$:

$G=
\begin{pmatrix}
1&\cosh\varepsilon\\
\cosh\varepsilon&1
\end{pmatrix}.$

Its singular-value condition number is

$\kappa_2(G)
=
\frac{1+\cosh\varepsilon}{\cosh\varepsilon-1}
\sim \frac{4}{\varepsilon^2}.$

If those are the only available spanning points, that basis is maximum volume and is nevertheless arbitrarily ill-conditioned.

Thus there are two separate numerical problems:

- recovering $\alpha_y$ stably from an approximate Gram matrix;

- evaluating $\alpha_y^\top z(q)$ accurately enough to resolve a near tie.

The coefficient bound addresses only the second problem under exact preprocessing.

If $r_i=d(q,a_i)$ and the raw distance error is at most $\tau$, then

$|\cosh(r_i+\epsilon_i)-\cosh r_i|
\le
\tau\sinh(r_i+\tau),$

so maximum volume gives

$|\widehat c_y-c_y|
\le
s\tau \max_i\sinh(r_i+\tau).$

If $R_A=\max_i r_i$ and the score gap separating the winner from the runner-up is $\Gamma$, a sufficient scale is roughly

$\tau
=
O\!\left(\frac{\Gamma e^{-R_A}}{s}\right).$

Hence the required fractional precision can be

$b=\Omega\!\left(R_A+\log\frac{s}{\Gamma}\right)$

bits, before accounting for $\kappa(G)$. Without a gap or conditioning promise, neither the classical nor quantum version has a uniform low-precision guarantee.

### 1.6 Consequence for a quantum score oracle

Storing all coefficients to $b$ bits costs

$\Theta(nsb)$

classical or QRAM bits. A coherent oracle

$|y\rangle|0\rangle
\longmapsto
|y\rangle|\alpha_y^\top z(q)\rangle$

normally requires loading and combining $s$ coefficients, with gate cost at least

$\widetilde O(sb)$

per score evaluation under ordinary word-addressable QRAM.

A stronger row-state-preparation primitive may reduce address depth, but then normalized inner-product estimation must achieve additive overlap precision on the scale

$\frac{\Gamma}{\|\alpha_y\|\,\|z(q)\|},$

and $\|z(q)\|$ can grow exponentially in geometric radius. Amplitude encoding does not remove the precision issue.

So the quantum minimum-finding route becomes, at best,

$s\text{ geometric queries}
\;+\;
\widetilde O(sb\sqrt n)
\text{ gates/QRAM accesses},$

which is generic static linear-score minimum finding. It is not a hyperbolic query advantage.

---

## 2. A stronger obstruction: the optimal progress-shadow lemma

The equal-edge-length cap in the prompt is correct, but it is not the largest possible progress cap.

Let

$d(p,q)=R,
\qquad
d(p,u)=\ell,$

and let $\theta$ be the angle at $p$ between the directions to $q$ and $u$. The hyperbolic law of cosines gives

$\cosh d(u,q)
=
\cosh R\cosh\ell
-
\sinh R\sinh\ell\cos\theta.$

Requiring progress at least $\delta$,

$d(u,q)\le R-\delta,$

is equivalent to

$\cos\theta
\ge
C_{R,\delta}(\ell)
:=
\frac{\cosh R\cosh\ell-\cosh(R-\delta)}
{\sinh R\sinh\ell}.$

The cap is largest when $C_{R,\delta}(\ell)$ is minimized.

### Lemma: optimal edge length and cap

For $0<\delta<R$, the unique maximizing edge length satisfies

$\boxed{
\cosh\ell_*
=
\frac{\cosh R}{\cosh(R-\delta)}
}$

and the maximum progress-cap half-angle is

$\boxed{
\alpha_*
=
\arcsin\!\left(
\frac{\sinh(R-\delta)}{\sinh R}
\right).
}$

#### Proof

Differentiating $C_{R,\delta}$, the sign of its derivative is the sign of

$\cosh(R-\delta)\cosh\ell-\cosh R.$

It therefore vanishes exactly at the displayed $\ell_*$. At that point,

$\min_\ell C_{R,\delta}(\ell)
=
\frac{\sqrt{\cosh^2R-\cosh^2(R-\delta)}}{\sinh R}.$

Consequently,

$\sin^2\alpha_*
=
1-\min_\ell C_{R,\delta}(\ell)^2
=
\frac{\sinh^2(R-\delta)}{\sinh^2R}.$

Geometrically, $u$ is the tangency point of a geodesic from $p$ to the ball $B(q,R-\delta)$.

### Far-field asymptotics

For fixed $\delta$ and $R\to\infty$,

$\boxed{
\ell_*\longrightarrow\operatorname{arcosh}(e^\delta),
\qquad
\sin\alpha_*\longrightarrow e^{-\delta}.
}$

Thus the optimal progress edge is a **short tangent edge**, not an edge of length $R$, and its angular success region does not shrink with $R$.

By contrast, when one artificially fixes $\ell=R$, the prompt’s formula gives

$\theta_R
\sim
2e^{-(R+\delta)/2}.$

So the exponential dependence on $R$ is an artifact of the equal-length restriction.

This directly removes the apparent mechanism in which negative curvature creates an increasingly sparse long-range set of improving directions that quantum search could exploit.

I would not claim novelty for this formula without a dedicated geometric-literature check; here it is an audit lemma.

---

## 3. What the optimal cap does to the whole-route accounting

Let $p_d(\delta)$ be the normalized measure of the optimal cap. For fixed $d$ and fixed $\delta$,

$p_d(\delta)
\longrightarrow
\mu_{S^{d-1}}
\left\{
x_1\ge\sqrt{1-e^{-2\delta}}
\right\},$

a positive constant independent of $R$.

Therefore increasing source-target distance does **not** force the list of candidate directions to grow. There is no $R$-driven $\Delta$-versus-$\sqrt\Delta$ separation.

For growing $d$ and fixed $\delta$, the spherical-cap exponent is

$p_d(\delta)
=
\operatorname{poly}(d)\,
e^{-(d-1)\delta}$

at exponential accuracy. This is now a standard spherical cap problem, not a specifically hyperbolic one.

Within the optimistic independent-direction proxy, take

$\Delta\asymp \frac1{p_d(\delta)}$

so that a constant expected number of neighbors make $\delta$ progress. Since the route has approximately $R/\delta$ steps,

$T_{\rm scan}
\asymp
\frac{R}{\delta\,p_d(\delta)},
\qquad
T_{\rm Grover}
\asymp
\frac{R}{\delta\sqrt{p_d(\delta)}}.$

Using the exponential approximation, the respective optimizers occur around

$\delta_{\rm C}\asymp\frac1{d-1},
\qquad
\delta_{\rm Q}\asymp\frac2{d-1}.$

At the correct scaling $\delta=c/d$,

$\cos\alpha_*
\sim\sqrt{\frac{2c}{d}},$

and for a random direction,

$p_d(c/d)\longrightarrow
\overline\Phi(\sqrt{2c}),$

a dimension-independent constant. Hence both optimized proxies have order

$\boxed{\Theta(dR)}$

up to constants and reliability overheads.

This is not a routing theorem—the adaptive-density and graph-construction issues remain—but it proves something useful:

**The supplied cap-density proxy cannot by itself yield an asymptotic whole-route quantum advantage once the graph’s progress scale is optimized.**

On one fixed, unindexed list, Grover still changes $1/p$ to $1/\sqrt p$. That is precisely the generic neighbor-list substitution the project is trying to avoid.

---

## 4. Fixed-dimensional classical preprocessing is already stronger

For fixed $d$ and approximation, the SoCG 2024 data structure provides linear space and logarithmic query time, with constants depending on $d$ and the approximation factor. Thus any $n^\gamma$ quantum query bound loses for ordinary fixed-dimensional ANN.  [source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2024.68)

The SoCG 2026 hyperbolic LSH paper also notes that exact nearest neighbor in $\mathbb H^2$ can be handled with a hyperbolic Voronoi diagram in linear space and $O(\log n)$ query time.  [source](https://drops.dagstuhl.de/storage/00lipics/lipics-vol367-socg2026/LIPIcs.SoCG.2026.39/LIPIcs.SoCG.2026.39.pdf)

This applies locally as well. At a graph vertex $v$, preprocess a Voronoi diagram for $N^+(v)$. In $\mathbb H^2$,

$\text{space at }v=O(\Delta_v),
\qquad
\text{nearest outgoing neighbor query}=O(\log\Delta_v).$

Summed over the graph, this is only linear in the stored adjacency size. Thus

$\sqrt{\Delta_v}$

quantum list search is not the correct same-access benchmark even before using landmarks.

### The specified priority policy can also be compiled

Suppose the local rule chooses the minimum-priority outgoing neighbor satisfying

$d(q,u)<d(q,v).$

Using the global landmark coordinates, each eligibility condition is the halfspace test

$(\alpha_u-\alpha_v)^\top z(q)<0.$

For a vertex of degree $\Delta$, the arrangement of these $\Delta$ hyperplanes has $O(\Delta^s)$ cells. On each cell, the set of eligible neighbors—and therefore the minimum-priority eligible neighbor—is fixed.

For fixed $s$, one can preprocess:

$\begin{array}{ll}
\text{local space} & \Delta^{O(s)},\\
\text{local query} & O(\log\Delta)
\end{array}$

using fixed-dimensional point location. When $\Delta=O(\log n)$, total graph space is

$n\log^{O(d)}n$

and each policy step costs $O(\log\log n)$, after the global $s$ landmark measurements.

This does not improve the proved hop count, but it destroys neighbor-list scanning as the correct per-hop classical baseline.

Finally:

- If the complete route must be returned or physically traversed, any algorithm pays $\Omega(h)$ for $h$ adaptive hops.

- If only the endpoint is wanted, global fixed-dimensional ANN is the fair comparator, not execution of a particular classical route.

---

## 5. Growing dimension reduces to already-known nonhyperbolic cores

Two exact reductions are particularly damaging to a hyperbolic-specific claim.

### 5.1 Common-radius shell equals spherical search

Fix an origin. Write data and query points as

$y=(\cosh r,\sinh r\,u_y),
\qquad
q=(\cosh R,\sinh R\,v),$

where $u_y,v\in S^{d-1}$. Then

$B(q,y)
=
\cosh R\cosh r
-
\sinh R\sinh r\,\langle v,u_y\rangle.$

If all data points have the same radius $r$, nearest-neighbor ordering is exactly the reverse ordering of

$\langle v,u_y\rangle.$

Therefore:

Hyperbolic ANN restricted to a single radial shell is exactly spherical maximum-inner-product/nearest-direction search.

Any worst-case hyperbolic quantum advantage must therefore also improve the corresponding spherical problem under the same storage, coherent access, and precision assumptions.

The existing product-code quantum LSF work already constructs a coherent sampler for structured close filters after preprocessing, then accesses buckets through QRAM and applies quantum search. It also discusses the strength and realism of the QRAM assumptions.  [source](https://arxiv.org/html/2410.15565v1)

So coherent structured filtering is not the missing hyperbolic ingredient.

### 5.2 Small hyperbolic balls approximate Euclidean ANN quantitatively

For $x\in\mathbb R^d$, define

$\phi_\lambda(x)
=
\left(
\sqrt{1+\lambda^2\|x\|^2},
\lambda x
\right)\in\mathbb H^d.$

For $\|x\|,\|y\|\le R_0$,

$\boxed{
\frac{\lambda\|x-y\|}{1+\lambda^2R_0^2}
\le
d_{\mathbb H}\bigl(\phi_\lambda(x),\phi_\lambda(y)\bigr)
\le
\lambda\|x-y\|.
}$

For the upper bound, AM–GM gives

$B(\phi_\lambda(x),\phi_\lambda(y))-1
\le
\frac{\lambda^2\|x-y\|^2}{2}.$

For the lower bound, rationalization gives

$B(\phi_\lambda(x),\phi_\lambda(y))-1
\ge
\frac{\lambda^2\|x-y\|^2}
{2(1+\lambda^2R_0^2)},$

and the stated distance bound follows from

$\operatorname{arcosh}(1+t)=2\operatorname{asinh}\sqrt{t/2}.$

Taking $\lambda R_0$ small makes the distortion arbitrarily close to $1$.

Therefore a worst-case hyperbolic ANN class contains:

- exact spherical-search instances on shells;

- nearly Euclidean ANN instances in small balls.

The SoCG 2026 analysis similarly obtains a lower-bound transfer from local Euclidean behavior rather than a universal hyperbolic improvement.  [source](https://drops.dagstuhl.de/storage/00lipics/lipics-vol367-socg2026/LIPIcs.SoCG.2026.39/LIPIcs.SoCG.2026.39.pdf)

A proposed hyperbolic filter advantage must explicitly exclude both subclasses through a meaningful radial-distribution promise.

---

## 6. Audit of the native hyperbolic LSH accounting

For the $\mathbb H^2$ hash in the bounded ball $B(0,R)$, the collision law is

$p_R(r)=1-\frac{r}{\pi\sinh R}.$

The bounded-domain dependence on $R$ is part of the theorem, not an ignorable implementation detail.  [source](https://drops.dagstuhl.de/storage/00lipics/lipics-vol367-socg2026/LIPIcs.SoCG.2026.39/LIPIcs.SoCG.2026.39.pdf)

To make a far collision probability approximately $n^{-\gamma}$, concatenation requires

$k
\ge
\frac{\gamma\log n}
{-\log\left(1-\frac{cr}{\pi\sinh R}\right)}.$

When $cr\ll\sinh R$,

$\boxed{
k
=
\Theta\!\left(
\frac{\sinh R}{cr}\log n
\right).
}$

Thus if $R=\Theta(\log n)$, merely materializing the concatenated hash can already require polynomially many bit evaluations. The term $kL\tau_{\rm hash}$ cannot be suppressed as subpolynomial without a new compact sampler theorem.

But such a theorem would then have to overcome two collisions:

- shell instances reduce to spherical structured filtering;

- coherent structured spherical-filter samplers are already known.

For higher-dimensional projection-based imports, the domain and tail conditions still need an explicit proof. Nothing here shows the source result is false; it shows that its collision exponent alone does not imply a usable quantum query exponent.

---

## 7. The three candidate questions

### 1. Growing-dimensional coherent hyperbolic filters

**Current verdict: stop.**

A sufficient positive result would need all of the following simultaneously:

$\begin{array}{ll}
\text{geometry} &
\text{a radial, non-shell overlap law strictly better than spherical LSF},\\
\text{sampler} &
\text{a coherent sampler whose gate cost is subexponential in the hash length},\\
\text{space} &
\text{the same exponent charged to classical and quantum preprocessing},\\
\text{QRAM} &
\text{explicit read/write or create/connect model},\\
\text{precision} &
\text{radius and near-tie dependence included},\\
\text{baseline} &
\text{best spherical/Euclidean quantum LSF at the same space}.
\end{array}$

No such geometric lemma currently appears. Without it, the mechanism is generic quantum LSF.

### 2. Query-independent multiscale navigable graph

**Current verdict: stop the cap-based route.**

The optimized progress shadow is produced by short tangent edges and loses its $R$-dependence. In fixed dimension, local Voronoi/range-min preprocessing defeats list search. In growing dimension, the directional problem becomes spherical.

The logarithmic-degree, $O(\log^2n)$-expected-hop theorem may still be useful classically, but quantizing its local scan is not a whole-route geometric advantage. Moreover, if its specified policy is based on fixed priorities and distance comparisons, the policy is a fixed-dimensional halfspace range-min problem after landmark factorization.

### 3. Comparison-only or restricted-local model

**This can manufacture a separation, but it changes the problem.**

A Grover advantage can be obtained by stipulating that:

- the query reveals no coordinates or numerical distances;

- preprocessing cannot store landmarks, Voronoi diagrams, or arrangements;

- a node exposes only a coherent black-box predicate over its outgoing edges.

That is not the usual static geometric ANN model. It suppresses exactly the information a classical geometric index would exploit while granting a stronger coherent oracle to the quantum algorithm.

A more natural variant might be a genuinely decentralized network:

- each node stores only local state;

- the packet has bounded working memory;

- nonlocal landmarks are forbidden for communication reasons;

- target access is specified as a coherent local oracle;

- the cost is communication or node probes, not standard ANN query time.

That could be a legitimate quantum-network problem. Hyperbolicity would then be a graph promise, not the source of the quantum primitive.

---

## 8. Resource comparison for the surviving generic quantum attempt

| Component | Same-access classical | Quantum |
| --- | --- | --- |
| Static coefficient storage | $O(nsb)$ bits | $O(nsb)$ QRAM bits |
| Query geometry | $s$ anchor distances | $s$ anchor distances |
| One candidate score | $O(sb)$ arithmetic, or indexed lookup structure | $\widetilde O(sb)$ reversible gates/QRAM |
| Global fixed-$d$ ANN | $O_{d,\varepsilon}(\log n)$ | Generic minimum finding loses |
| Local $\mathbb H^2$ choice | $O(\log\Delta)$ after linear local preprocessing | $O(\sqrt\Delta)$ score calls |
| Fixed-priority local policy | Fixed-dimensional arrangement/range-min | Grover over list is not competitive |
| Full route of $h$ moves | At least $h$ outputs/moves | At least $h$ outputs/moves |
| Near-tie precision | Depends on $\Gamma,\kappa(G),R_A$ | Same dependence, plus reversible arithmetic |

The IJCAI 2025 quantum-HNSW paper already occupies the broad “quantum HNSW” label. Its construction uses quantum state preparation/comparison within an HNSW-style traversal, but it does not establish the same-access, whole-route asymptotic separation required here.  [source](https://arxiv.org/html/2505.23066v1)

---

# Precise stopping reason

I would state the conclusion as follows:

**Under standard static geometric preprocessing, hyperbolic nearest-neighbor retrieval and navigation do not presently expose a uniquely hyperbolic quantum speedup mechanism.** Query geometry factors through $s\le d+1$ landmark scores; fixed-dimensional search admits logarithmic classical indexing; the optimized progress condition is a spherical-cap condition independent of source-target radius in the far field; and growing-dimensional worst cases contain exact spherical and arbitrarily near-Euclidean subclasses. The remaining quantum primitives are generic minimum finding, halfspace/filter search, or spherical LSF.

This is not a universal impossibility theorem for every restricted model. It is a precise reason to stop the current standard-model program.

A credible reopening would require a distributional or promise class with **provable radial heterogeneity** that excludes both common-radius shells and small Euclidean balls, together with a hyperbolic filter sampler whose complete time-space-QRAM-precision tradeoff beats the corresponding spherical quantum LSF tradeoff. Without that, a claimed advantage will collapse either to generic Grover search or to an already studied quantum filtering mechanism.

