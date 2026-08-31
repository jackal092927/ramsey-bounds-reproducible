# Quantum Implicit-Majority Ramsey Search

Date: 2026-08-31  
Proof status: **PROVABLE AS STATED in the promised valid-graph edge-oracle model**  
Publication status: **novelty and conflicting-literature clarification still open**

## Executive finding

Let an unknown simple graph on at least $4^{K-1}$ vertices be supplied by a
coherent edge oracle. There is a bounded-error quantum algorithm that returns
a $K$-clique or a $K$-vertex independent set using

$$
O\!\left(2^K K\log\frac K\eta\right)
$$

edge-oracle queries, where $\eta$ is the allowed failure probability. In the
standard succinct Ramsey parameterization $N=2^n$ and
$K=\lfloor n/2\rfloor+1$, this is

$$
O\!\left(\sqrt N\log N\log\frac{\log N}{\eta}\right).
$$

The algorithm quantizes the elementary Erdős--Szekeres
majority-neighborhood recursion. It stores each current candidate set as a
short predicate and uses capped quantum search to sample uniformly from that
implicit set. A scale-aware error budget estimates cheap early levels more
accurately and expensive deep levels less accurately. The accumulated loss
is only a constant factor while the query work is balanced across scales.

There is also a simpler estimation-free implementation. It samples one
uniform vertex from the current non-pivot set and follows the colour of that
edge, thereby choosing a branch with probability proportional to its size.
A size-biased survival lemma gives a one-run structural success probability
greater than $1/2$ and an independently useful bound

$$
O\!\left(2^K K^2\log K\log(1/\eta)\right).
$$

The same lemma extends to $q$ edge colours. This route is slower by one
polynomial factor in $K$ than the scale-aware headline theorem, but its proof
uses no majority estimation or concentration inequality.

This is an algorithmic upper bound. It is not a new numerical or asymptotic
Ramsey-number bound, does not produce an $R(3,18)\ge101$ witness, and does not
yet prove a separation from the best possible randomized classical query
algorithm.

## 1. Model and theorem

Let

$$
O_G\lvert u,v,b\rangle
=\lvert u,v,b\oplus G(u,v)\rangle
$$

give coherent access to the adjacency matrix of a promised simple undirected
graph. The cost measure is the number of calls to $O_G$. Vertex labels and
ordinary reversible gates are not free in a time analysis; their cost is
discussed separately below.

**Theorem.** Let $K\ge2$, $N\ge4^{K-1}$, and $0<\eta<1/2$. Given coherent
edge-oracle access to a simple graph on $N$ vertices, a quantum algorithm can,
with probability at least $1-\eta$, output a $K$-clique or a $K$-vertex
independent set using at most

$$
O\!\left(2^K K\log\frac K\eta\right)
$$

edge queries in the worst case. The algorithm may return $\bot$ on the
exceptional event, and it verifies every non-$\bot$ output before returning
it.

It is enough to use an arbitrary block of exactly $M=4^{K-1}$ vertices, so the
proof below assumes $N=M$.

The promised formulation is the clean graph-theoretic core.  It also extends
to the usual locally verifiable TFNP relation on an arbitrary adjacency
circuit $C$.  Define a canonical simple graph by
$A(u,v)=C(\min\{u,v\},\max\{u,v\})$ for $u\ne v$ and $A(u,u)=0$.
Run the theorem on $A$, then inspect both ordered entries and the diagonal on
the returned $K$ vertices.  A local asymmetry or self-loop is an accepted
invalidity certificate; otherwise $C$ agrees with $A$ on those vertices and
the homogeneous set is an accepted witness.  This costs only $O(K^2)$ extra
queries and does not require globally testing circuit validity.

## 2. A capped uniform-search primitive

Let $T\subseteq[M]$ be recognized by a coherent membership predicate and
suppose $|T|/M\ge\lambda>0$. A truncated block of the unknown-solution
search of Boyer--Brassard--Høyer--Tapp has the following properties:

1. it uses $O(\lambda^{-1/2})$ membership tests;
2. it returns an element of $T$ with probability at least an absolute
   constant $p_0>0$;
3. conditional on success, that element is exactly uniform on $T$; and
4. it terminates within the same cap even if the density promise is false or
   $T$ is empty.

The uniformity follows because every Grover iterate preserves equal
amplitudes on all marked basis states. Randomizing the iteration count,
measuring, verifying membership, and restarting preserves exact uniformity
conditional on success. Fresh blocks give independent outputs.

To collect $m$ independent samples, run
$O(m+\log(r/\eta))$ independent capped blocks and abort unless at least $m$
succeed. A Chernoff bound gives conditional abort probability $O(\eta/r)$
whenever the density promise holds. This batch amplification is important:
amplifying every individual sample separately would insert an unnecessary
second logarithmic factor.

## 3. Estimation-free size-biased recursion

Set $M=4^{K-1}$ and $r=2K-3$. Start with $S_0=[M]$ and any pivot
$v_0\in S_0$. At round $i$, use permutation-symmetric capped search to draw
an exactly uniform

$$
x_i\in T_i:=S_i\setminus\{v_i\}.
$$

If no verified sample is obtained within the predetermined cap, abort. Set
$c_i=G(v_i,x_i)$,

$$
S_{i+1}=\{x\in T_i:G(v_i,x)=c_i\},
\qquad v_{i+1}=x_i.
$$

The implicit membership predicate includes both every earlier colour
constraint and every exclusion $x\ne v_j$; hence old pivots cannot re-enter.
After $r$ rounds, put $w=v_r$. One of the two labels occurs at least $K-1$
times, and those pivots together with $w$ are homogeneous by exact nesting.

Let $P_d(s)$ denote the worst probability that the ideal process completes
$d$ more steps from a candidate set of size $s$ with a distinguished pivot.
If the two classes of the remaining $s-1$ vertices have sizes $a,b$, then

$$
P_d(s)\ge
\frac{aP_{d-1}(a)+bP_{d-1}(b)}{s-1}.
$$

With $P_0(s)=1$ for $s\ge1$, induction and
$(x)_++(y)_+\ge(x+y)_+$ give

$$
P_d(s)\ge\frac{(s-2^d+1)_+}{s}.
\tag{SB}
$$

Since $M=2^{r+1}$, (SB) gives structural completion probability at least
$1/2+1/M$. Give each capped sample failure probability at most $1/(100r)$;
the implemented run then succeeds with probability at least $0.49$. Fixed
independent repetition plus final exact verification raises this to
$1-\eta$. At level $i$ the predicate costs $O(i+1)$ edge queries, while a
worst-case capped sample from a nonempty subset of the $M$-element universe
costs $O(\sqrt M\log(2r))$ predicate queries. Thus the total is

$$
O\!\left(2^K K^2\log K\log(1/\eta)\right).
$$

For $q\ge2$ colours, put $r=q(K-2)+1$ and
$B_d=(q^d-1)/(q-1)$. The same induction gives
$P_d(s)\ge(s-B_d)_+/(s-1)$ for $d\ge1$. Restricting to the least power of
two $L_q\ge2B_r$ yields constant survival probability and a

$$
O\!\left(r^2\sqrt{L_q}\log(2r)\log(1/\eta)\right)
$$

query algorithm for a monochromatic $K$-clique in a $q$-edge-coloured
complete graph on at least $L_q$ vertices.

## 4. Algorithm and scale-aware accuracy

Set $r=2K-3$ and fix total error budget $E=1/16$. For
$i=0,\ldots,r-1$, define

$$
d_i=\left\lceil\frac{r-1-i}{6}\right\rceil,
\qquad z_i=2^{-d_i},
\qquad Z=\sum_{j=0}^{r-1}z_j,
$$

and

$$
\varepsilon_i=E\frac{z_i}{Z},
\qquad a_i=\frac12-\varepsilon_i.
\tag{1}
$$

Thus $\sum_i\varepsilon_i=E$. Moving six levels toward the root halves the
error allowance. This exact dyadic schedule is a convenient scale-aware
alternative to the optimizing choice
$\varepsilon_i\propto((i+1)2^{i/2})^{1/3}$; both yield the same asymptotic
query bound.

Maintain classical pivots $v_0,\ldots,v_{i-1}$, branch colours
$c_0,\ldots,c_{i-1}$, and the implicit set

$$
S_i=\left\{
u\in[M]\setminus\{v_0,\ldots,v_{i-1}\}:
G(v_j,u)=c_j\text{ for every }j<i
\right\}.
$$

At round $i=0,\ldots,r-1$:

1. use capped search to obtain a pivot $v_i\in S_i$;
2. obtain $m_i$ independent uniform samples, with replacement, from
   $S_i\setminus\{v_i\}$, where
   $$
   m_i=\left\lceil
   \frac{1}{2\varepsilon_i^2}\log\frac{4r}{\eta}
   \right\rceil;
   \tag{2}
   $$
3. query their edges to $v_i$ and let $\widehat p_i$ be the fraction of
   colour-$1$ edges;
4. set $c_i=1$ if $\widehat p_i\ge1/2$ and $c_i=0$ otherwise; and
5. append the exact constraint $G(v_i,u)=c_i$ to obtain $S_{i+1}$.

After $r$ rounds, find $w\in S_r$. Among the $r=2K-3$ branch colours, one
occurs at least $K-1$ times. Return $w$ together with any $K-1$ pivots
carrying that colour.

## 5. Correctness

### 5.1 Adaptive concentration

Let $\mathcal H_i$ be the entire classical transcript before estimating the
$i$th majority. Conditional on $\mathcal H_i$, the graph, set $S_i$, and
pivot $v_i$ are fixed. Conditional on the capped batch succeeding, its
successful outputs are independent and uniform on
$S_i\setminus\{v_i\}$. Hoeffding's inequality and (2) give

$$
\Pr\!\left[
|\widehat p_i-p_i|>\varepsilon_i\mid\mathcal H_i
\right]
\le2e^{-2m_i\varepsilon_i^2}
\le\frac{\eta}{2r}.
$$

Apply this bound only while the earlier rounds were good, then use the tower
property and a union bound. Conditional Chernoff bounds for the capped search
batches use the remaining failure budget: each of the $r$ pivot searches,
$r$ sampling batches, and one final search is assigned at most
$\eta/(4r+2)$, whose union is at most $\eta/2$. Therefore every required good
event occurs with probability at least $1-\eta$. No independence between
different rounds is assumed.

### 5.2 Variable candidate-set recurrence

Write $s_i=|S_i|$. On an accurate estimate, the selected colour occupies at
least an $a_i=1/2-\varepsilon_i$ fraction of the non-pivot vertices, so

$$
s_{i+1}\ge a_i(s_i-1).
\tag{3}
$$

Let $A_0=1$ and

$$
A_i=\prod_{j=0}^{i-1}a_j
=2^{-i}\prod_{j=0}^{i-1}(1-2\varepsilon_j).
$$

For $x_j\in[0,1]$, the elementary inequality
$\prod_j(1-x_j)\ge1-\sum_jx_j$ gives

$$
A_i\ge2^{-i}\left(1-2\sum_{j<i}\varepsilon_j\right)
\ge\frac78\,2^{-i}.
\tag{4}
$$

Induction in (3) gives

$$
s_i>MA_i-1.
\tag{5}
$$

Indeed, the claim is immediate for $i=0$; if it holds at $i$, then
$s_{i+1}>MA_{i+1}-2a_i>MA_{i+1}-1$ because $a_i<1/2$.
Since $M2^{-r}=2$, (4)--(5) imply $s_r>3/4$, and hence the integer $s_r$ is
positive.  At every sampling level $i\le r-1$, $M2^{-i}\ge4$, and

$$
|S_i\setminus\{v_i\}|>MA_i-2
\ge\frac38\,2^{-i}M.
\tag{6}
$$

Thus the predetermined density promise
$\lambda_i=(3/8)2^{-i}$ is valid for every capped sampling batch on a good
prefix.  The final integer bound $s_r\ge1$ also gives
$s_r/M\ge2^{-(r+1)}\ge(3/8)2^{-r}$, so the same form covers the search for
$w$. If an earlier estimate was inaccurate and a later set is too small or
empty, the cap still makes the algorithm terminate and return $\bot$ rather
than hang.

### 5.3 Homogeneous output

For $i<j$, nesting gives $v_j\in S_{i+1}$, so
$G(v_i,v_j)=c_i$. The same identity holds with $v_j$ replaced by $w$.
One colour occurs among $c_0,\ldots,c_{r-1}$ at least

$$
\left\lceil\frac{2K-3}{2}\right\rceil=K-1
$$

times. The corresponding pivots together with $w$ form a $K$-clique if that
colour is $1$, and a $K$-vertex independent set if it is $0$. A final
$\binom K2$-query check verifies the witness. Thus an exceptional execution
can cause an abort but cannot cause an unverified graph to be returned.

## 6. Query and gate complexity

Testing membership in $S_i$ costs $i$ edge queries. A capped search block at
level $i$ therefore costs $O((i+1)2^{i/2})$ edge queries by (6). Put
$b_i=(i+1)2^{i/2}$. The batch cap uses
$O(m_i+\log(r/\eta))=O(m_i)$ blocks, so the sampling cost is

$$
O\!\left(
\log\frac r\eta
\sum_{i=0}^{r-1}b_i\varepsilon_i^{-2}
\right).
\tag{7}
$$

The normalizing sum satisfies $Z<12$. Since
$d_i=\lceil(r-1-i)/6\rceil$,

$$
\begin{aligned}
\sum_{i=0}^{r-1}b_i\varepsilon_i^{-2}
&=O\!\left(
\sum_{i=0}^{r-1}(i+1)2^{i/2}4^{d_i}
\right)\\
&=O\!\left(r2^{r/2}\right).
\end{aligned}
\tag{8}
$$

For the last line, write $h=r-1-i$ and use
$4^{\lceil h/6\rceil}\le4\cdot2^{h/3}$; the remaining geometric sum is a
constant multiple of $r2^{r/2}\sum_{h\ge0}2^{-h/6}$.
The pivot searches, final search, and $K^2$ output verification fit the same
bound. Since $r=2K-3$, (7)--(8) prove

$$
Q=O\!\left(2^K K\log\frac K\eta\right).
$$

The gate complexity is safely stated as

$$
2^K\operatorname{poly}\!\left(
K,\log N,\log\frac1\eta
\right),
$$

plus the gate cost of one supplied edge-oracle evaluation. The algorithm
uses no QRAM assumption. It stores $O(K)$ classical pivot labels and branch
colours and uses reversible comparison, conjunction, and uncomputation to
evaluate the implicit membership predicates.

## 7. Classical comparison and lower-bound stop rule

The exact classical majority-neighborhood recursion queries every edge from
the current pivot to the explicit candidate set. Its geometric sum is less
than $2M=2\cdot4^{K-1}$. The quantum theorem is therefore a quadratic query
improvement, up to logarithmic factors, over this standard constructive
algorithm.

A Yao argument based on the random-Painter theorem of
Conlon--Fox--Grinshpun--He gives the best lower bound located in this audit:
for bounded-error randomized algorithms on $M=4^{K-1}$ vertices,

$$
R_{2/3}(\mathrm{Ramsey}_{M,K})
=\Omega\!\left(2^{(2-\sqrt2)K}\right)
=\Omega\!\left(M^{1-1/\sqrt2}\right).
$$

This is below the quantum upper exponent $1/2$, so it does not establish a
quantum-versus-classical separation. It does strengthen the earlier
$M^{1/4}$ black-box lower bound recorded by Komargodski--Naor--Yogev in this
parameterization. Improving the randomized lower bound
beyond $2^{(1+\delta)K}$ would also improve the long-standing exponential
lower bound for diagonal Ramsey numbers through the online Ramsey connection.
That is a major independent combinatorial problem, not a routine missing
lemma. The honest current claim is a new quantum upper bound and a quadratic
improvement over the standard constructive algorithm.

## 8. Collision with a published query-complexity aside

Jain--Li--Robere--Xun's formal Definition 2.6 uses $N=2^n$ vertices, and the
sentence following Definition 2.7 declares the default target to be $K=n/2$.
Their introduction instead prints $N=2^{n+1}$ and target $n$; that sentence
is internally inconsistent with the formal definition and is not used in the
comparison below. Their query-complexity discussion prints a quantum lower
bound $N^{1-o(1)}$, attributed to their Ramsey reduction and the Liu--Zhandry
multi-collision lower bound.

The theorem above gives
$O(\sqrt N\log N\log(\log N/\eta))$ edge queries in the valid-graph promise
regime, and the canonicalization argument gives the same asymptotic upper
bound for the locally verifiable full relation. The statements cannot both
hold under the printed parameterization.

The direct substitution into the cited reduction does not yield the printed
exponent. If the collision range has size $B$, the collision size is fixed
$t$, and the Ramsey host has size $M\asymp B^{4t}$, Liu--Zhandry's exponent in
$B$ is

$$
\alpha_t=\frac{2^{t-1}-1}{2^t-1}.
$$

In terms of $M$, the direct exponent is only $\alpha_t/(4t)$. For $t=2$
this equals $1/24$. For every $t\ge3$, it is less than
$1/(8t)\le1/24$. Thus these two cited ingredients alone do not establish
$M^{1-o(1)}$; they do yield a nontrivial $\Omega(M^{1/24})$ lower bound at
$t=2$, subject to the reduction's usual rounding and promise conventions.

This report records a precise inconsistency, not an accusation and not an
author-confirmed correction. The relevant authors should be asked to check
the parameter translation before submission. Until then, the manuscript
must state the conflict explicitly and must not cite the printed lower bound
as compatible with the theorem.

## 9. Prior-art boundary

Earlier quantum Ramsey work studies adiabatic Hamiltonians, QUBO/annealing,
global search over graph colourings, or computation of small Ramsey numbers.
Those tasks differ from the present problem: given one unknown valid graph at
the totality threshold, find the homogeneous set promised by the elementary
constructive proof. Dörn's quantum graph-query algorithms for independent
sets and cliques are closer in model, but do not use the Ramsey totality
promise or this majority recursion.

A targeted primary-source and forward-citation search found no earlier
implementation of the Erdős--Szekeres recursion by implicit-set quantum
sampling. This is positive novelty evidence, not a complete priority proof.
Because the construction is elementary, folklore collision remains possible.
The closest exact-model discussion is the conflicting
Jain--Li--Robere--Xun aside, so external author clarification and expert
literature review remain publication gates.

## 10. Reproducibility

Run:

```bash
python3 experiments/quantum_ramsey/implicit_majority_audit.py \
  --self-check --max-k 12 --simulate-k 3 --trials 20
```

The script:

- checks the dyadic error schedule and recurrence with exact rational
  arithmetic through $K=64$;
- compares the size-biased survival lemma with exact dynamic programs over
  every binary split tree through nine rounds and every ternary split tree
  through four rounds;
- independently verifies the product and variable-recurrence lower bounds;
- verifies that the final real lower bound is positive;
- emits the direct Jain-et-al./Liu--Zhandry exponent substitution;
- checks conditional marked-item uniformity with an explicit 16-state Grover
  evolution;
- runs deterministic-seed diagnostics on complete, empty, parity, and random
  graphs; and
- verifies every returned homogeneous set classically.

The Monte Carlo component is not a hardware or end-to-end state-vector
simulation. It replaces quantum search by an ideal uniform marked-item
sampler and checks the combinatorial invariant and concentration setup; only
the isolated sampler audit evolves a small state vector. Neither diagnostic
is empirical evidence of physical speedup. The theorem itself is the analytic
proof above, not the experiment.

## 11. Nonclaims and remaining gates

- No numerical Ramsey bound is improved.
- No $R(3,18)\ge101$ witness is produced.
- No classical lower bound matching the quantum upper bound is proved.
- No practical near-term speedup is claimed; the early-level sample counts
  and hidden concentration constants are large.
- No topology is used in the positive theorem. Separate topology routes
  produced only no-go diagnostics.
- The published lower-bound conflict requires clarification before an
  unconditional novelty or query-landscape claim is submission-safe.
