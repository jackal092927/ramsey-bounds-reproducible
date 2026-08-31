# Proof Package

## Claim

Let \(H\) be the fixed graph on vertex set \(V\), let

\[
\mathcal F=\{F\text{ on }V:F\text{ is triangle-free and }\alpha(F)<18\},
\]

and let \(d_H(F)=|E(H)\setminus E(F)|\). Assume the already certified theorem

\[
\rho(H):=\inf_{F\in\mathcal F}d_H(F)\ge 7.
\]

Fix a seed edge \(f\in E(H)\), and define the exact-seven branch

\[
\mathcal B_f=\{F\in\mathcal F:d_H(F)=7,\ f\notin E(F)\}.
\]

The claims under adversarial review are:

1. If \(\mathcal B_f\ne\varnothing\), then some \(F^*\in\mathcal B_f\) is
   maximal triangle-free. More strongly, \(F^*\) can be obtained from any
   \(F\in\mathcal B_f\) by adding only pairs outside \(E(H)\); in particular,
   the full seven-edge deletion support and the fixed branch edge are
   preserved.
2. For a primary graph \(G\), the all-pair selector clauses used in the paper
   have an auxiliary satisfying assignment if and only if \(G\) is maximal
   triangle-free, provided the triangle clauses are also imposed.
3. Consequently, every genuine exact-seven branch-1 repair extends to a model
   of the frozen maximal-union CNF. Therefore a checked UNSAT proof for that
   CNF would close branch 1. A SAT result for the finite-bank CNF need not be a
   repair, and an UNKNOWN result implies neither existence nor nonexistence.

## Status

**PROVABLE AS STATED.**

The claims survive unchanged. The first and third claims depend on the already
certified premise \(\rho(H)\ge7\); they are not independent alternative proofs
of that premise.

## Assumptions

- \(H\) and \(F\) are finite simple graphs on the same finite labelled vertex
  set \(V\).
- Additions of pairs outside \(E(H)\) do not change \(d_H\).
- Adding an edge to a graph cannot increase its independence number.
- The theorem \(\rho(H)\ge7\) has already been established independently of
  the maximality argument by the budget-five and exact-six proof packages.
- The branch-1 common CNF is a sound relaxation: every genuine branch-1 target
  extends to a model of it.
- Each of the four positive retention units is a proved consequence of that
  common CNF.
- Every installed mask is an actual 18-vertex subset, and its positive
  pair-hitting clause is therefore necessary for \(\alpha(F)<18\).

## Notation

- \(N_G(v)\) is the open neighbourhood of \(v\) in \(G\).
- A missing pair \(uv\notin E(G)\) is *safe* if
  \(N_G(u)\cap N_G(v)=\varnothing\). Equivalently, adding \(uv\) creates no
  triangle.
- A triangle-free graph is *maximal triangle-free* if adding any missing pair
  creates a triangle.
- \(x_{uv}\) is the primary variable saying that \(uv\in E(G)\).
- \(y_{uv,w}\) is an existential auxiliary variable selecting \(w\) as a
  common neighbour of the missing pair \(uv\).

## Proof Strategy

First saturate a target using only safe additions of original nonedges. The
certified radius lower bound then shows that every still-deleted seed edge is
already triangle-blocked: otherwise restoring it would produce a target at
distance six. This proves the maximal-triangle-free normal form without
altering the branch. Next prove the selector encoding by direct projection on
the primary variables. Finally compose the normal form with the soundness of
the common relaxation, retention entailments, and mask clauses.

## Dependency Map

1. The maximality normal form depends on the safe-edge lemma, finite
   termination, and \(\rho(H)\ge7\).
2. The safe-edge lemma depends only on the definition of a triangle and the
   monotonicity of independence number under edge addition.
3. The selector projection is a direct Boolean equivalence and does not depend
   on \(\rho(H)\ge7\).
4. The maximal-union implication depends on the normal form, common-CNF
   soundness, the four singleton entailments, mask validity, and selector
   projection.
5. The implication from formula UNSAT to branch nonexistence is the
   contrapositive of item 4. No reverse target-to-SAT equivalence is claimed for
   arbitrary SAT models because the independent-set bank is finite.

## Proof

### Step 1. Safe additions preserve the target conditions

Let \(G\in\mathcal F\), and suppose \(uv\notin E(G)\) satisfies

\[
N_G(u)\cap N_G(v)=\varnothing.
\]

Any triangle newly created by adding \(uv\) would have a third vertex \(w\)
adjacent to both \(u\) and \(v\) before the addition. This contradicts the
displayed condition. Hence \(G+uv\) remains triangle-free.

Every independent set of \(G+uv\) is also an independent set of \(G\), because
\(G+uv\) has all edges of \(G\) and one additional edge. Therefore

\[
\alpha(G+uv)\le\alpha(G)<18.
\]

If additionally \(uv\notin E(H)\), then

\[
E(H)\setminus E(G+uv)=E(H)\setminus E(G),
\]

so both the deletion distance and the complete deletion support are unchanged.

### Step 2. Saturate only original nonedges

Take \(F\in\mathcal B_f\). While there is a safe pair

\[
uv\notin E(H)\cup E(F),
\]

add it. The finite set \(\binom{V}{2}\) guarantees termination. By Step 1,
every intermediate graph remains in \(\mathcal B_f\), and the final graph
\(F_0\) satisfies

\[
uv\notin E(H)\cup E(F_0)
\quad\Longrightarrow\quad
N_{F_0}(u)\cap N_{F_0}(v)\ne\varnothing.
\]

No seed edge was added in this process, so \(E(H)\setminus E(F_0)\) is exactly
the deletion support of \(F\), including the fixed edge \(f\).

### Step 3. Every deleted seed edge is triangle-blocked

Let \(e\in E(H)\setminus E(F_0)\). Suppose for contradiction that \(e\) is
safe in \(F_0\). By Step 1, \(F_0+e\) is triangle-free and has independence
number below 18. Restoring one seed edge changes the one-sided distance by
exactly one, so

\[
d_H(F_0+e)=d_H(F_0)-1=6.
\]

Thus \(F_0+e\in\mathcal F\), contradicting \(\rho(H)\ge7\). Therefore every
deleted seed edge has a common neighbour in \(F_0\).

This includes the fixed branch edge. In the concrete branch
\(f=(97,99)\), if both other edges of the seed triangle were present,
restoring \(f\) would not be safe because it would create that triangle. If
restoring \(f\) were safe, then at least one other triangle edge would remain
absent, and the resulting distance-six graph would still fall under the
previously certified global three-branch exclusion. No assumption that the
restored graph remains in branch 1 is used.

Combining Steps 2 and 3, every missing pair of \(F_0\) has a common neighbour.
For a triangle-free graph this is equivalent to maximal triangle-freeness:
adding a missing pair creates a triangle exactly when its endpoints already
have a common neighbour. Set \(F^*=F_0\). This proves Claim 1.

### Step 4. Project the selector clauses exactly

For each unordered pair \(uv\), introduce \(y_{uv,w}\) for all
\(w\in V\setminus\{u,v\}\) and impose

\[
x_{uv}\vee\bigvee_{w\notin\{u,v\}}y_{uv,w},
\]

\[
\neg y_{uv,w}\vee x_{uw},
\qquad
\neg y_{uv,w}\vee x_{vw}.
\]

Fix an assignment of the primary variables. If the selector clauses have an
auxiliary satisfying assignment and \(x_{uv}=0\), the long clause forces some
\(y_{uv,w}=1\). The two binary clauses then force
\(x_{uw}=x_{vw}=1\), so \(w\) is a common neighbour of \(u\) and \(v\).

Conversely, if \(x_{uv}=1\), assign all \(y_{uv,w}=0\). If \(x_{uv}=0\) and
\(u,v\) have a common neighbour \(w\), assign \(y_{uv,w}=1\) and all other
selectors for that pair to zero. In either case all displayed clauses for the
pair are satisfied. The auxiliary blocks for distinct pairs are disjoint, so
these pairwise extensions combine into one global extension.

Therefore the selector block projects exactly to the condition that every
missing pair has a common neighbour. Together with the triangle clauses, this
is exactly maximal triangle-freeness. This proves Claim 2. Reverse Tseitin
implications are unnecessary because the \(y\)-variables are existential
witnesses rather than definitions required to be unique.

### Step 5. Compose the normal form with the maximal-union CNF

Assume a genuine branch-1 exact-seven repair exists. By Claim 1, there is such
a repair \(F^*\) that is maximal triangle-free and has the same seven deleted
seed edges. Its primary assignment satisfies the common branch-1 relaxation.
Because the four positive units are consequences of that relaxation, it
satisfies those units. Since \(\alpha(F^*)<18\), every installed 18-set has at
least one present pair, so every installed hitting clause is satisfied.
Finally, Claim 2 supplies an auxiliary assignment for all maximality selectors.
Thus \(F^*\) extends to a model of the maximal-union CNF.

Taking the contrapositive, if that exact CNF is UNSAT, no genuine branch-1
exact-seven repair exists. This proves the first implication in Claim 3.

The reverse implication from an arbitrary CNF model to a target is not valid:
the finite mask bank need not contain every independent 18-set. A model must
undergo a complete independence-number check before it can be called a repair.
Likewise, a timeout or UNKNOWN result supplies neither a model nor a
refutation and therefore implies nothing about branch existence. This proves
the remaining claim boundaries in Claim 3. \(\square\)

## Corrections or Missing Assumptions

- No correction to the maximality proposition is required.
- The paper should keep the phrase “a feasible branch-1 repair exists if and
  only if one exists that is maximal triangle-free.” It must not say that every
  raw repair is already maximal.
- The use of \(\rho(H)\ge7\) must remain explicit. Omitting it would prove only
  saturation on original nonedges, not blocking of deleted seed edges.
- An UNSAT result for branch 1 would not close the other two triangle-edge
  branches. The certified trivial seed automorphism group prevents a symmetry
  transfer.

## Open Risks

- The mathematical implication is conditional on the independently certified
  computational theorem \(\rho(H)\ge7\) and on the authenticated singleton
  entailments. This is a proof-carrying trust boundary, not a gap in the
  graph-theoretic argument.
- The current maximal-union endpoint is UNKNOWN. Its conflict count, memory
  use, elapsed time, and deleted incomplete proof prefix have no mathematical
  evidentiary value.
- No current result proves \(\rho(H)=7\), \(\rho(H)\ge8\), the existence of a
  100-vertex \((3,18)\)-Ramsey graph, or \(R(3,18)\ge101\).

---

# Proof Package II: Quantum Implicit-Majority Ramsey Search

## Claim

Let $K\ge2$, let $N\ge4^K$, and let

$$
O_G\lvert u,v,b\rangle
=\lvert u,v,b\oplus G(u,v)\rangle
$$

be coherent edge-oracle access to a promised simple undirected graph on
$[N]$.  For every $0<\eta<1/2$, there is a quantum algorithm that, with
probability at least $1-\eta$, outputs a $K$-clique or a $K$-vertex
independent set and makes at most

$$
O\!\left(2^K K^3\log\frac K\eta\right)
$$

edge queries in the worst case.  It may output $\bot$ on the exceptional
event and verifies every non-$\bot$ witness before returning it.

## Status

**PROVABLE AS STATED** in the promised valid-graph edge-oracle model.

The theorem survived three independent hostile mathematical reconstructions.
Its clean statement assumes a valid graph; a canonicalization corollary below
also solves the standard locally verifiable relation for arbitrary adjacency
encodings.  It is not a theorem about numerical Ramsey numbers or separation
from every randomized classical algorithm.

## Assumptions

- $G$ is a finite simple undirected graph and $O_G$ is available coherently.
- Edge-oracle calls are the charged resource.  Reversible operations on
  $O(\log N)$-bit vertex labels are charged only in the separate gate bound.
- The capped unknown-solution search primitive is the standard
  Boyer--Brassard--Høyer--Tapp construction: under marked density at least
  $\lambda$, one block uses $O(\lambda^{-1/2})$ membership calls, has constant
  success probability, and terminates even when the density promise fails.
- All measured search outputs are checked by the exact membership predicate.

## Notation

- $M=4^K$ is the number of vertices actually used.
- $r=2K-3$ is the number of pivot rounds.
- $\varepsilon=1/(16r)$ and
  $a=1/2-\varepsilon=(1/2)(1-1/(8r))$.
- $S_i$ is the candidate set before pivot $i$, and $s_i=|S_i|$.
- $v_i$ is pivot $i$, $c_i\in\{0,1\}$ is its retained colour, and
  $w\in S_r$ is the final vertex.

## Proof Strategy

Restrict to $M=4^K$ vertices.  Represent every candidate set by the exact
edge constraints accumulated from earlier pivots.  Use capped quantum search
to obtain independent uniform samples from the implicit set.  Conditional
Hoeffding bounds show that every retained colour is within $\varepsilon$ of a
majority.  An exact affine recurrence proves that all candidate sets retain a
constant number of vertices.  The pivot constraints then make the final
output exactly homogeneous.  Predetermined density lower bounds cap every
search even after a bad random event, and a geometric summation gives the
query bound.

## Dependency Map

1. The search/sampling implementation depends on the capped unknown-solution
   search lemma and exact membership verification.
2. Simultaneous near-majority selection depends on conditional uniformity,
   Hoeffding's inequality, the tower property, and a union bound.
3. Nonemptiness depends on the affine recurrence and Bernoulli's inequality.
4. Output homogeneity depends only on the exact definition and nesting of the
   sets $S_i$; estimation errors affect size, not edge consistency.
5. The worst-case query bound depends on the deterministic density bounds,
   negative-binomial/Chernoff batch truncation, and a geometric series.

## Proof

### Step 1. Capped uniform search

For a marked set $T$ of density at least $\lambda$, truncate the geometrically
increasing BBHT schedule after $O(\lambda^{-1/2})$ membership calls.  The
standard BBHT analysis supplies an absolute lower bound $p_0>0$ on the block's
success probability.  A cap is imposed before the block starts, so it also
terminates if $T$ is empty.

For every fixed Grover iteration count, all marked basis states have the same
amplitude.  Randomizing the iteration count preserves this symmetry.
Therefore, after measurement and exact membership verification, the output
conditioned on success is uniform on $T$.  Reinitializing all registers and
random choices makes different successful blocks independent.

Run $B=C_0(m+\log(r/\eta))$ independent blocks to collect $m$ successes.
For a sufficiently large absolute constant $C_0$, a Chernoff bound for the
number of successful blocks gives failure probability at most $\eta/(4r+4)$.
Conditional on the success pattern, the first $m$ successful identities are
independent and uniform on $T$.

### Step 2. Define the nested candidate sets

At level $i$, define

$$
S_i=\left\{
u\in[M]\setminus\{v_0,\ldots,v_{i-1}\}:
G(v_j,u)=c_j\text{ for all }j<i
\right\}.
$$

The predicate costs $i$ edge queries to compute and $i$ to uncompute, which
is $O(i)$ edge queries.  Use the capped primitive first to obtain
$v_i\in S_i$, and then to obtain $m$ independent uniform samples from
$S_i\setminus\{v_i\}$.  Let $\widehat p_i$ be the sampled fraction of
colour-$1$ edges from $v_i$.  Retain colour $c_i=1$ when
$\widehat p_i\ge1/2$ and colour $c_i=0$ otherwise.

### Step 3. Control adaptive estimation errors

Let $\mathcal H_i$ be the complete transcript before level $i$'s samples are
drawn.  Conditional on $\mathcal H_i$ and successful capped sampling, the
graph, $S_i$, and $v_i$ are fixed and the samples are independent and uniform.
Thus Hoeffding's inequality gives

$$
\Pr\!\left[
|\widehat p_i-p_i|>\varepsilon\mid\mathcal H_i
\right]
\le2e^{-2m\varepsilon^2}.
$$

Choose

$$
m=\left\lceil128r^2\log\frac{C_1r}{\eta}\right\rceil
$$

with a sufficiently large absolute $C_1$.  Apply the conditional bound at the
first inaccurate level while all earlier levels were accurate.  The tower
property and a union bound over the $r$ levels give total estimation-error
probability at most $\eta/2$.  The conditional Chernoff bounds from Step 1,
union-bounded over all levels and the final search, contribute at most the
remaining $\eta/2$.  Hence every required good event occurs with probability
at least $1-\eta$.

### Step 4. Prove the size recurrence and predetermined density promises

On an accurate level, whichever colour is selected occupies at least the
fraction $a=1/2-\varepsilon$ of $S_i\setminus\{v_i\}$.  Hence

$$
s_{i+1}\ge a(s_i-1).
$$

Define $L_0=M$ and $L_{i+1}=a(L_i-1)$.  With
$c=a/(1-a)<1$, direct substitution gives

$$
L_i=a^i(M+c)-c>a^iM-1.
$$

Since $r=2K-3$, Bernoulli's inequality yields

$$
Ma^r
=4^K2^{-r}\left(1-\frac1{8r}\right)^r
\ge8\left(1-\frac18\right)=7.
$$

Therefore $s_i\ge L_i>6$ for every $i\le r$ on a good prefix.  Since $s_i$
is an integer, $s_i\ge7$.  Furthermore,

$$
|S_i\setminus\{v_i\}|=s_i-1>a^iM-2
\ge\frac57a^iM.
$$

Thus the predetermined promise $\lambda_i=(5/7)a^i$ is valid for each
sampling batch on a good prefix and is also a conservative bound for pivot
search.  If a prior estimate was bad, the capped primitive still terminates;
failure to verify enough marked outputs causes $\bot$ rather than an infinite
run.

### Step 5. Prove that the returned set is homogeneous

For $i<j$, the exact nesting $v_j\in S_{i+1}$ implies
$G(v_i,v_j)=c_i$.  Likewise $w\in S_r\subseteq S_{i+1}$ implies
$G(v_i,w)=c_i$.  Among $r=2K-3$ branch colours, one value occurs at least
$\lceil r/2\rceil=K-1$ times.  Choose those $K-1$ pivots and add $w$.  Every
edge among these $K$ vertices has the selected colour.  A final
$\binom K2$-query verification prevents an invalid witness from being
returned on any exceptional path.

### Step 6. Sum the edge queries

A capped block at level $i$ costs

$$
O\!\left((i+1)\lambda_i^{-1/2}\right)
=O\!\left((i+1)a^{-i/2}\right)
$$

edge queries.  Since the batch cap uses $O(m)$ blocks at each level,

$$
Q=O\!\left(
m\sum_{i=0}^{r}(i+1)a^{-i/2}+K^2
\right).
$$

The summands grow geometrically, so the sum is
$O(r a^{-r/2})$.  Moreover,

$$
a^{-r/2}
=2^{r/2}\left(1-\frac1{8r}\right)^{-r/2}
=O(2^K).
$$

Together with $m=O(r^2\log(r/\eta))$ and $r=\Theta(K)$, this gives

$$
Q=O\!\left(2^K K^3\log\frac K\eta\right).
$$

This proves the claim. $\square$

## Corrections or Missing Assumptions

- The valid-simple-graph promise is used by the clean theorem statement, but
  not required for the usual local TFNP relation.  For an arbitrary circuit
  $C$, define the canonical graph
  $A(u,v)=C(\min\{u,v\},\max\{u,v\})$ off the diagonal.  Run the theorem on
  $A$ and inspect both orientations and the diagonal only on the returned
  vertices.  A local defect is an accepted invalidity certificate; otherwise
  the homogeneous set is valid for $C$.  This costs $O(K^2)$ extra queries.
- Uncapped repeat-until-success BBHT is not sufficient: after an exceptional
  estimate a later candidate set might be empty.  Predetermined caps and
  aborts are part of the theorem.
- Per-sample high-confidence amplification would add a second logarithm.
  Batching a fixed number of constant-success blocks gives the stated bound.

## Open Risks

- Jain--Li--Robere--Xun print an incompatible $N^{1-o(1)}$ quantum lower bound
  for their Ramsey query problem.  Their formal Definition 2.6 uses
  $N=2^n$, and the sentence following Definition 2.7 sets the default target
  to $K=n/2$; the different shorthand in their introduction is internally
  inconsistent and is not used here.  Direct substitution into the two
  results they cite yields at most an $N^{1/24}$ exponent, not $1-o(1)$, but
  author clarification remains a publication gate.
- A targeted search found no direct prior implementation of the
  Erdős--Szekeres recursion by implicit-set quantum sampling.  Because the
  construction is elementary, an unrecorded folklore collision remains
  possible.
- The theorem improves the standard $O(4^K)$ constructive recursion.  No
  matching lower bound against every randomized classical algorithm is known,
  so a general quantum-versus-classical separation is not established.
- The proof changes the algorithmic query complexity of finding the witness;
  it does not change any Ramsey-number bound.

---

# Proof Package III: Scale-Aware Query Bound

## Claim

Under the same valid-simple-graph oracle model as Proof Package II, assume
$N\ge4^{K-1}$ rather than $N\ge4^K$.  Then the query bound is

$$
O\!\left(2^K K\log\frac K\eta\right).
$$

For $N=2^n$ and $K=\lfloor n/2\rfloor+1$, this is

$$
O\!\left(\sqrt N\log N\log\frac{\log N}{\eta}\right).
$$

## Status

**PROVABLE AS STATED.**

This strengthening changes only the allocation of the per-level estimation
errors and sample counts. The exact candidate predicates, capped uniform
search, adaptive conditioning, homogeneous-output argument, and abort
semantics are those proved in Proof Package II.

## Assumptions

- All assumptions of Proof Package II hold.
- Sampling is with replacement, so a level may request more samples than the
  cardinality of its candidate set.
- Capped BBHT blocks are reinitialized independently; conditional on verified
  success, their marked outputs are independent and uniform.

## Notation

Let $M=4^{K-1}$, $r=2K-3$, and $E=1/16$. For $0\le i<r$, set

$$
d_i=\left\lceil\frac{r-1-i}{6}\right\rceil,
\qquad z_i=2^{-d_i},
\qquad Z=\sum_{j=0}^{r-1}z_j,
$$

$$
\varepsilon_i=E\frac{z_i}{Z},
\qquad a_i=\frac12-\varepsilon_i,
\qquad A_i=\prod_{j=0}^{i-1}a_j.
$$

Take

$$
m_i=\left\lceil
\frac{1}{2\varepsilon_i^2}\log\frac{4r}{\eta}
\right\rceil
$$

uniform samples at level $i$.

## Proof Strategy

The total error budget $\sum_i\varepsilon_i=1/16$ keeps the product of all
retained fractions within a constant factor of $2^{-i}$. The dyadic schedule
allows larger error at expensive deep levels: moving six levels toward the
root halves $\varepsilon_i$. This exactly offsets the square-root growth in
implicit-set sampling. Summing the resulting geometric blocks removes two
unnecessary factors of $K$ from the uniform-error proof.

## Dependency Map

1. Product retention depends on the total error budget and
   $\prod_j(1-x_j)\ge1-\sum_jx_j$ for $x_j\in[0,1]$.
2. The variable affine recurrence depends on $a_i<1/2$.
3. Predetermined search densities depend on the product retention,
   $M2^{-(r-1)}=4$, and $M2^{-r}=2$.
4. Per-level sample counts depend on conditional Hoeffding.
5. The optimized total depends on the six-level dyadic schedule and a
   convergent geometric sum.

## Proof

### Step 1. Bound the retained product

By construction,

$$
\sum_{i=0}^{r-1}\varepsilon_i=E=\frac1{16}.
$$

For every prefix, use $a_j=(1/2)(1-2\varepsilon_j)$ and the product
inequality to obtain

$$
A_i
=2^{-i}\prod_{j<i}(1-2\varepsilon_j)
\ge2^{-i}\left(1-2\sum_{j<i}\varepsilon_j\right)
\ge\frac78\,2^{-i}.
\tag{Q1}
$$

All factors lie in $[0,1]$ because
$0<\varepsilon_i\le E<1/2$.

### Step 2. Solve the variable recurrence sufficiently sharply

On the event that level $i$'s empirical fraction is within
$\varepsilon_i$ of its true value, the empirically selected colour occupies
at least fraction $a_i$ of $S_i\setminus\{v_i\}$. Hence

$$
s_{i+1}\ge a_i(s_i-1).
\tag{Q2}
$$

We prove by induction that

$$
s_i>MA_i-1.
\tag{Q3}
$$

At $i=0$, $s_0=M>M-1$. If (Q3) holds at $i$, then (Q2) gives

$$
s_{i+1}>a_i(MA_i-2)=MA_{i+1}-2a_i
>MA_{i+1}-1,
$$

because $a_i<1/2$. This completes the induction.

Since $M2^{-r}=2$, (Q1)--(Q3) imply $s_r>3/4$, so the integer $s_r$ is
positive. For a sampling round $i\le r-1$, $M2^{-i}\ge4$ and

$$
\begin{aligned}
|S_i\setminus\{v_i\}|
&=s_i-1\\
&>MA_i-2\\
&\ge\frac78M2^{-i}-2\\
&\ge\frac38M2^{-i},
\end{aligned}
\tag{Q4}
$$

where the last inequality uses $M2^{-i}\ge4$.
Thus $\lambda_i=(3/8)2^{-i}$ is a deterministic density promise for all
good-prefix pivot and sampling searches.  At the final level, $s_r\ge1$ and
$s_r/M\ge2^{-(r+1)}\ge(3/8)2^{-r}$, so the same form also covers the search
for $w$.

### Step 3. Control all adaptive estimates

Conditional on the full history before level $i$, successful capped sampler
outputs are independent and uniform on the now-fixed set
$S_i\setminus\{v_i\}$. Therefore Hoeffding's inequality gives

$$
\Pr\!\left[
|\widehat p_i-p_i|>\varepsilon_i
\mid\mathcal H_i
\right]
\le2e^{-2m_i\varepsilon_i^2}
\le\frac{\eta}{2r}.
$$

Apply this conditional inequality at the first inaccurate level after a good
prefix and use the tower property. A union bound makes the total estimation
error at most $\eta/2$. At level $i$, run a predetermined
$O(m_i+\log(r/\eta))$ capped BBHT blocks. Under (Q4), a Chernoff bound gives
the requested $m_i$ verified successes except with conditional probability
at most $\eta/(4r+2)$ after the absolute cap constant is fixed. Give the same
bound to each of the $r$ pivot searches and the final search. There are
$2r+1$ such search events, so their union has probability at most $\eta/2$;
together with the estimation budget, total failure is at most $\eta$. On a
bad prefix, the same fixed caps force an abort and preserve the worst-case
query bound.

### Step 4. Sum the scale-aware work

One capped search block at level $i$ uses
$O(2^{i/2})$ membership tests by (Q4). Computing and uncomputing membership,
and checking the sampled edge, costs $O(i+1)$ edge queries. Define

$$
b_i=(i+1)2^{i/2}.
$$

Since every $m_i$ dominates a constant multiple of $\log(r/\eta)$, the
sampling work is

$$
O\!\left(
\log\frac r\eta
\sum_{i=0}^{r-1}b_i\varepsilon_i^{-2}
\right).
\tag{Q5}
$$

There are at most six indices at each value of $d_i$, so

$$
Z=\sum_i2^{-d_i}<6\sum_{d=0}^{\infty}2^{-d}=12.
$$

Consequently

$$
\sum_{i=0}^{r-1}b_i\varepsilon_i^{-2}
=O\!\left(
\sum_{i=0}^{r-1}(i+1)2^{i/2}4^{d_i}
\right).
\tag{Q6}
$$

Put $h=r-1-i$. Since
$4^{\lceil h/6\rceil}\le4\cdot2^{h/3}$, the last sum is at most a constant
multiple of

$$
2^{r/2}
\sum_{h=0}^{r-1}(r-h)2^{-h/6}
=O(r2^{r/2}).
\tag{Q7}
$$

The high-confidence pivot searches and final search contribute
$O(r2^{r/2}\log(r/\eta))$, and final verification costs $O(K^2)$. Combining
(Q5)--(Q7) and $r=2K-3$ gives

$$
Q=O\!\left(2^K K\log\frac K\eta\right).
$$

The exact homogeneous-output proof from Proof Package II is independent of
the error schedule and completes the theorem. $\square$

## Corrections or Missing Assumptions

- The samples must be drawn with replacement. This is both permitted by the
  quantum sampler and required by the stated iid Hoeffding calculation.
- The displayed dyadic schedule, not a uniform $1/K$ schedule, is responsible
  for the improved factor $K$ rather than $K^3$.
- Conditional uniformity is used only after exact membership verification;
  no unconditional uniformity claim is made for failed search blocks.

## Open Risks

- The literature and classical-lower-bound risks listed in Proof Package II
  are unchanged.
- The scale-aware improvement has been reconstructed independently, but the
  unresolved Jain--Li--Robere--Xun conflict remains the principal submission
  gate.

---

# Proof Package IV: Estimation-Free Size-Biased Recursion

## Claim

Let $K\ge2$, $N\ge4^{K-1}$, and $0<\eta<1/2$.  In the coherent edge-query
model, there is a one-sided bounded-error algorithm that returns a verified
$K$-clique or $K$-vertex independent set using

$$
O\!\left(2^K K^2\log K\log\frac1\eta\right)
$$

edge queries in the worst case.  Unlike Proof Packages II and III, this
algorithm estimates no neighbourhood majority.

## Status

**PROVABLE AS STATED.**

Two independent hostile reconstructions checked the adaptive recurrence,
conditional uniformity, distinct-vertex condition, fixed-cap failure
accounting, exact witness extraction, and worst-case query sum.  An exact
dynamic program exhausts all two-colour split trees through nine rounds and
all three-colour split trees through four rounds as a finite diagnostic.

## Algorithm

Restrict to the first $M=4^{K-1}=2^{2K-2}$ vertices and set $r=2K-3$.
Let $S_0=[M]$ and choose a fixed $v_0\in S_0$.  For
$i=0,\ldots,r-1$, write $T_i=S_i\setminus\{v_i\}$.  Use the
permutation-symmetric capped search of Proof Package II with density promise
$1/M$, repeated $O(\log(2r))$ times, to obtain an exactly uniform
$x_i\in T_i$ conditional on verified success.  If all repetitions fail,
abort.  Set

$$
c_i=G(v_i,x_i),
\qquad
S_{i+1}=\{x\in T_i:G(v_i,x)=c_i\},
\qquad
v_{i+1}=x_i.
$$

The coherent predicate for $T_i$ checks all prior colour constraints and all
inequalities $x\ne v_0,\ldots,v_i$.  It uses $O(i+1)$ edge queries to compute
and uncompute; the inequalities use reversible label comparisons and no edge
queries.  The exclusions are essential to keep all pivots distinct.

After the last step put $w=v_r$.  Select $K-1$ pivots whose labels $c_i$
agree, add $w$, and verify every induced edge before returning.

## Survival Lemma

Let $P_d(s)$ be the infimum, over all graphs, all candidate sets of size $s$,
and all distinguished pivots in them, of the ideal process's probability of
completing $d$ further steps.  Define $P_0(s)=1$ for $s\ge1$, and
$P_d(0)=P_d(1)=0$ for $d\ge1$.  Then

$$
P_d(s)\ge F_d(s):=\frac{(s-2^d+1)_+}{s}.
\tag{SB1}
$$

The proof is by induction.  If the two colour classes of the $s-1$
non-pivot vertices have sizes $a,b$, the exact uniform sample follows them
with probabilities $a/(s-1),b/(s-1)$.  Hence

$$
P_d(s)\ge
\frac{aP_{d-1}(a)+bP_{d-1}(b)}{s-1}.
$$

By induction, $tP_{d-1}(t)\ge(t-2^{d-1}+1)_+$.  Therefore the numerator is
at least

$$
(a-2^{d-1}+1)_+ +(b-2^{d-1}+1)_+
\ge(s-2^d+1)_+.
$$

Dividing by $s-1$ and then weakening the denominator to $s$ proves (SB1),
including empty colour classes.  Because $M=2^{r+1}$,

$$
P_r(M)\ge\frac{M-2^r+1}{M}=\frac12+\frac1M.
\tag{SB2}
$$

## Implementation Failure and Amplification

Give each nonempty-set search failure probability at most $1/(100r)$.
Every capped block has a predetermined worst-case query limit.  Conditional
on success, permutation symmetry of the initial state, Grover iterations,
and verification makes the output exactly uniform on $T_i$.  We may therefore
couple the implemented path with the ideal path until the first search
failure.  A union bound and (SB2) give one-run success probability at least
$1/2-1/100=0.49$.  Empty sets cause a bounded abort, not an incorrect output.
Running a fixed $O(\log(1/\eta))$ independent copies and accepting the first
verified witness gives failure probability at most $\eta$.

## Exact Witness

For $i<j\le r$, nesting gives $v_j\in S_{i+1}$ and therefore
$G(v_i,v_j)=c_i$.  Among $r=2K-3$ binary labels, one value occurs at least
$K-1$ times.  The associated pivots and $w=v_r$ are distinct and every edge
among them has that value.  Final verification makes the algorithm
one-sided on every exceptional path.

## Worst-Case Query Bound

A capped search with density promise $1/M$ costs $O(\sqrt M)$ membership
tests.  Repetition to error $O(1/r)$ costs another $O(\log(2r))$ factor.
Consequently one complete fixed-cap run uses

$$
O\!\left(
\sqrt M\log(2r)\sum_{i=0}^{r-1}(i+1)
\right)
=O(2^K K^2\log K)
$$

edge queries.  The fixed number of amplification runs proves the claimed
$O(2^K K^2\log K\log(1/\eta))$ worst-case bound.

## Multicolour Extension

For $q\ge2$, put

$$
r=q(K-2)+1,
\qquad
B_d=1+q+\cdots+q^{d-1}=\frac{q^d-1}{q-1},
$$

and let $L_q$ be the least power of two at least $2B_r$.  For $d\ge1$ and
$s\ge2$, the $q$-colour ideal process satisfies

$$
P_d^{(q)}(s)\ge\frac{(s-B_d)_+}{s-1}.
\tag{SB3}
$$

Indeed, for a split $a_1+\cdots+a_q=s-1$, induction and the positive-part
inequality give

$$
\begin{aligned}
(s-1)P_d^{(q)}(s)
&\ge\sum_{j=1}^q(a_j-B_{d-1})_+\\
&\ge\left(s-1-qB_{d-1}\right)_+
=(s-B_d)_+.
\end{aligned}
$$

Starting from $L_q\ge2B_r$ makes (SB3) greater than $1/2$.  The chosen depth
is the least one for which the pigeonhole principle forces one of the $q$
labels to occur $K-1$ times.  Thus a $q$-edge-coloured complete graph on at
least $L_q$ vertices admits a one-sided algorithm using

$$
O\!\left(r^2\sqrt{L_q}\log(2r)\log\frac1\eta\right)
$$

colour queries.  This is an algorithmic extension, not a new competitive
multicolour Ramsey-number bound or a quantum--classical separation.

## Open Risks

- The priority claim remains ``to our knowledge'' because the recurrence is
  elementary and may be unpublished folklore.
- Proof Package III has the better two-colour polynomial factor and remains
  the headline query bound.  Package IV supplies the cleaner mechanism and
  the multicolour extension.
- The Jain--Li--Robere--Xun parameter conflict and absence of a matching
  randomized classical lower bound remain unchanged.
