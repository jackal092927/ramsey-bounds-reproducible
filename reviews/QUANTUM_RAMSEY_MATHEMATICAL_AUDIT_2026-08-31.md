# Adversarial Mathematical Audit: Quantum Ramsey Search

Date: 2026-08-31  
Scope: mathematical correctness of the query theorems, not software quality  
Verdict on the two-colour upper bounds: **PROVABLE AS STATED**  
Verdict on the multicolour extension: **PROVABLE AS STATED**  
Publication verdict: **positive theorem present; priority and one literature
conflict remain open**

## Claims audited

For a coherently queried simple graph on at least $4^{K-1}$ vertices:

1. the scale-aware implicit-majority algorithm outputs a verified
   homogeneous $K$-set with failure probability at most $\eta$ using
   $O(2^K K\log(K/\eta))$ edge queries in the worst case;
2. the estimation-free size-biased algorithm does the same using
   $O(2^K K^2\log K\log(1/\eta))$ queries;
3. for $q$ colours, with $r=q(K-2)+1$,
   $B_r=(q^r-1)/(q-1)$, and $L_q$ the least power of two at least $2B_r$,
   the size-biased algorithm uses
   $O(r^2\sqrt{L_q}\log(2r)\log(1/\eta))$ colour queries; and
4. the locally verifiable arbitrary-circuit Ramsey relation follows by
   canonical symmetrization plus $O(K^2)$ local checks.

These are algorithmic query upper bounds. They do not improve a numerical
Ramsey number and do not establish a separation from every randomized
classical algorithm.

## Hostile checks and dispositions

### 1. Uniformity is theorem-critical

An arbitrary quantum routine that merely finds some marked vertex would not
support the size-biased recurrence. The proof uses permutation-symmetric
capped Grover/BBHT search from the uniform state. At any fixed iteration
count, all marked basis states have equal amplitude. Randomizing iteration
counts, restarting, measuring, and then verifying membership preserve exact
uniformity conditional on success. Independent reinitialization gives
independent successful samples. **No defect found.**

### 2. Every execution has a fixed worst-case cap

The analysis never relies on repeat-until-success or expected stopping time.
Each search block is truncated after its prescribed query budget. If its
density promise is false or the set is empty, verification fails and the
algorithm aborts. Repeating a fixed number of blocks gives the stated failure
probability and a deterministic worst-case query count. **No defect found.**

### 3. Candidate predicates preserve distinct vertices

The size-biased predicate at level $i$ checks both all earlier colour
constraints and $x\ne v_0,\ldots,v_i$. Therefore a prior pivot cannot
re-enter through a diagonal oracle value. Computing and uncomputing the edge
constraints costs $O(i+1)$ edge queries. **Potential fatal loophole closed in
the statement and algorithm.**

### 4. Size-biased survival under adaptive splits

For a two-colour split $a+b=s-1$,

$$
P_d(s)\ge
\frac{aP_{d-1}(a)+bP_{d-1}(b)}{s-1}.
$$

The induction
$P_d(s)\ge(s-2^d+1)_+/s$ follows from
$(x)_++(y)_+\ge(x+y)_+$. It permits empty colour classes and remains valid
when the next pivot is the sampled vertex. At $s=4^{K-1}$ and
$d=2K-3$, it gives $1/2+1/s$. An independent exact dynamic program checked
every binary split tree through nine rounds. **No defect found.**

### 5. Multicolour constants and depth

The correct loss threshold is the geometric sum
$B_d=1+q+\cdots+q^{d-1}$, not $q^d$. For a split
$a_1+\cdots+a_q=s-1$,

$$
\sum_j(a_j-B_{d-1})_+
\ge(s-B_d)_+,
$$

so $P_d^{(q)}(s)\ge(s-B_d)_+/(s-1)$ for $d\ge1$. The depth
$q(K-2)+1$ is the least depth at which a colour must occur $K-1$ times.
An exact ternary split-tree dynamic program checked four rounds. **A weaker
initial constant was sharpened; no remaining defect found.**

### 6. Exact witness extraction

Nested exact constraints give $G(v_i,v_j)=G(v_i,w)=c_i$ for all $j>i$.
The pigeonhole principle supplies $K-1$ pivots with one label, and their edges
to each other and to $w$ all have that colour. Every proposed witness is then
queried directly. Estimation errors can reduce survival probability but
cannot change the edge identities. **No defect found.**

### 7. Scale-aware recurrence and adaptive concentration

Conditional on the history before round $i$, the graph, pivot, and candidate
set are fixed, so Hoeffding applies to the independent uniform samples. The
first-bad-level argument and tower property require no independence between
rounds. The $r$ pivot searches, $r$ sampling batches, and final search each
receive failure budget $\eta/(4r+2)$, totaling at most $\eta/2$; Hoeffding
uses the other $\eta/2$. With $\sum_i\varepsilon_i=1/16$,

$$
A_i=\prod_{j<i}(1/2-\varepsilon_j)\ge(7/8)2^{-i},
\qquad
s_i>MA_i-1.
$$

For $M=4^{K-1}$ and $r=2K-3$, this proves $s_r\ge1$ and the deterministic
density promises used by all good-prefix searches. **No defect found.**

### 8. Optimized query sum

For
$d_i=\lceil(r-1-i)/6\rceil$ and
$\varepsilon_i\propto2^{-d_i}$, the theorem-critical sum is

$$
\sum_i(i+1)2^{i/2}\varepsilon_i^{-2}
=O(r2^{r/2}).
$$

Writing $h=r-1-i$ reduces it to
$2^{r/2}\sum_h(r-h)2^{-h/6}$. This yields
$O(2^K K\log(K/\eta))$, including the batch concentration factor, pivot
searches, final search, and output verification. **No missing polynomial
factor found.**

### 9. Promise and arbitrary-circuit model alignment

For an arbitrary adjacency circuit $C$, define
$A(u,v)=C(\min\{u,v\},\max\{u,v\})$ off the diagonal and $A(u,u)=0$.
Run the graph algorithm on $A$. On the returned vertices, inspect both
ordered entries and all diagonals. A discrepancy is a valid local invalidity
certificate; otherwise the homogeneous set is also valid for $C$. This
avoids any unsupported global validity test. **No defect found.**

### 10. Classical comparison

The random-Painter/Yao calculation gives only

$$
\Omega(2^{(2-\sqrt2)K})
=\Omega(M^{1-1/\sqrt2}),
$$

which is below the quantum exponent $1/2$. The manuscript therefore does not
claim a quantum separation against all randomized classical algorithms. It
does improve the previously recorded $M^{1/4}$ black-box lower bound in this
parameterization.
**Overclaim avoided.**

## Unresolved publication gates

1. Jain--Li--Robere--Xun print an $N^{1-o(1)}$ quantum lower-bound remark for
   a closely matching Ramsey relation. Their formal Definition 2.6 uses
   $N=2^n$ and the text following Definition 2.7 sets the default target to
   $K=n/2$; the different introductory shorthand is internally inconsistent
   and is not used for this audit. Direct substitution of their stated
   graph-hash reduction into the cited Liu--Zhandry exponent gives at most
   an $N^{1/24}$ exponent. Their hard instances are valid symmetric graphs,
   so canonicalization does not explain the conflict. Author clarification is
   required; this audit records an incompatibility, not an accusation.
2. Targeted searches found no prior quantum implementation of the
   constructive Erdős--Szekeres recursion by implicit-set uniform sampling.
   Because the idea is elementary, the novelty language must remain ``to our
   knowledge'' until expert literature review is complete.
3. The result is a new query upper bound and a near-quadratic improvement over
   the standard deterministic construction. It is not yet a proved
   quantum-versus-randomized-classical speedup.

## External AI review state

A public-only collaboration packet was sent to ChatGPT Pro at
<https://chatgpt.com/c/6a9600fb-e158-83e8-b741-d979176a5d2b>. At the time of
this audit its review was still running, so no conclusion from that reviewer
is counted here. Two separate background review attempts timed out without a
verdict and are likewise not mathematical evidence either for or against the
claims.
