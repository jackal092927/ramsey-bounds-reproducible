# Proof Package: transverse encoding after the rank-two obstruction

Date: 2026-08-12  
Primary source: Bradač, [arXiv:2605.28793v3](https://arxiv.org/abs/2605.28793v3),
Claim 2.13.

## Claim

Let $t\geq2$ be fixed, let $q$ be a sufficiently large prime power, and put

$$
[d]_q=\frac{q^d-1}{q-1},\qquad
N=[t+1]_q,\qquad
p=\frac{[t]_q}{[t+1]_q},
$$

so $N$ is the number of points of $PG(t,q)$ and $p$ is the proportion of
those points in a projective hyperplane.  Define

$$
k_q=\left\lfloor\frac{(t-1)q\log q}{12}\right\rfloor,
\qquad
\alpha=1-\frac{3}{2q}.
\tag{1}
$$

The following two statements are proved.

1. **Rank-zero saturation lemma.**  The forward-independent-tuple tree of
   $D^*(t,q)$ has at least

   $$
   L_q=\left(\frac{pN^2}{4}\right)^{k_q}
   \alpha^{k_q(k_q-1)/2}
   \tag{2}
   $$

   paths of length $k_q$ for which every non-root vertex is unmarked under
   the marking rule of Claim 2.13 and every extension has

   $$
   r^{\sigma_{i-1}}(b_i)=\ell_i=0.
   \tag{3}
   $$

   In particular,

   $$
   L_q^{1/k_q}\geq
   \frac{3}{16}q^{\,t+9(t-1)/10}.
   \tag{4}
   $$

   Consequently, for every fixed $C_t>0$ and all sufficiently large $q$,

   $$
   \overrightarrow i_{k_q}(D^*(t,q))
   \geq L_q>(C_tq^t)^{k_q}.
   \tag{5}
   $$

2. **Fixed-first-coordinate lemma.**  Along any path in the same tree, a
   fixed projective first coordinate $a$ can occur in at most $t$ unmarked
   extensions $(a,b)$.  More precisely, the second coordinates at those
   occurrences are linearly independent inside the $t$-dimensional vector
   hyperplane $a^\perp$.

Statement (2) is a stronger obstruction than the $q$-singleton/rank-two
history in
[NEXT_LOWER_BOUND.md](./NEXT_LOWER_BOUND.md): there can be
$\Theta_t(q\log q)$, rather than merely $O_t(q)$, low-layer exceptional
steps.  Moreover, (2)--(5) disprove the scale-free record-map proposal made
there, which allowed only $\exp(O_t(q\log q))$ records and at most
$(C_tq^t)^u$ preimages for an all-unmarked signature with $u$ positions.

## Status

- **Rank-zero saturation lemma:** **PROVABLE AS STATED**.
- **Tuple-count lower bound (2) and comparison (4)--(5):**
  **PROVABLE AS STATED**.
- **Fixed-first-coordinate lemma:** **PROVABLE AS STATED**.
- **There are only $O_t(q)$ low-rank or low-layer exceptional steps:**
  **FALSE AS STATED**.
- **The record-map proposal in `NEXT_LOWER_BOUND.md`, uniformly over all
  lengths and signatures:** **FALSE AS STATED**.
- **A new Ramsey lower bound with one fewer logarithm:**
  **NOT CURRENTLY JUSTIFIED**.

The counterexample is to this particular local encoding target.  It does not
exclude a bound that uses a sufficiently long tail, a non-uniform weighting
of forward tuples, a different conversion from $D^*$ to a graph, or a
modified algebraic construction.

## Assumptions

- $q$ is a prime power and $t\geq2$ is fixed.
- Projective points are the $1$-spaces of
  $V=\mathbb F_q^{t+1}$.
- Orthogonality is with respect to the nondegenerate standard bilinear form.
- The definitions of consistency, $W^\sigma(y)$, $r^\sigma(y)$,
  $U_j^\sigma$, $Z_j^\sigma$, popular, poor, and unmarked are exactly those
  of Bradač Claim 2.13.
- As in the source, forward-independent tuples may repeat vertices.  The
  paths counted below happen to use distinct first and second coordinates.

## Notation

- For a projective point $a$, let

  $$
  H_a=\{y\in PG(t,q):a\perp y\}.
  $$

  Nondegeneracy gives a bijection between projective points $a$ and
  projective hyperplanes $H_a$.
- For a partial history $\sigma_i$, let

  $$
  S_i=PG(t,q)\setminus\bigcup_{j=1}^i H_{a_j}.
  \tag{6}
  $$

- A hyperplane is *balanced for* $S$ if, with
  $\mu=p|S|$,

  $$
  \frac\mu2\leq |H\cap S|\leq\frac{3\mu}{2}.
  \tag{7}
  $$

## Proof Strategy

First, use the exact two-point incidence probabilities of projective
hyperplanes to prove that at least half of all hyperplanes are balanced for
every set $S$ with $p|S|\geq8$.  Starting with all projective points, choose
a balanced $H_{a_i}$ and then any
$b_i\in H_{a_i}\cap S_{i-1}$.  The uncovered set is exactly the current
$Z_0$, so every such choice is a consistent unmarked extension of type zero.
The upper half of (7) keeps the uncovered set large for $k_q$ rounds; the
lower half supplies many choices of $b_i$.  Multiplying the branching lower
bounds proves (2).

The fixed-first-coordinate lemma uses a different, local argument: the
literal removal block at an unmarked occurrence of $a$ contains a point
$y\perp a$.  Every earlier second coordinate paired with the same $a$ lies
in $W(y)$, whereas the new one does not, forcing a new vector dimension.

## Dependency Map

1. Lemma 1 uses only the exact point and two-point incidence counts in
   $PG(t,q)$ and Chebyshev's inequality.
2. Lemma 2 uses Lemma 1, the definition of a consistent history, and the
   source definitions of poor and popular.
3. Lemma 3 multiplies the per-prefix choices supplied by Lemma 2.
4. Corollary 4 uses elementary estimates on $p$, $N$, and $\alpha$.
5. Lemma 5 uses the nonempty literal removal block proved in Claim 2.13 and
   rederived in `NEXT_LOWER_BOUND.md`.
6. The obstruction to the record map follows by comparing its proposed
   total capacity with Corollary 4.

## Proof

### Step 1: balanced projective hyperplanes

**Lemma 1.**  Let $S\subseteq PG(t,q)$ have size $s$, let $H$ be a uniformly
random projective hyperplane, and put $X=|H\cap S|$ and $\mu=ps$.  Then

$$
\operatorname{Var}X\leq\mu.
\tag{8}
$$

If $\mu\geq8$, at least $N/2$ of the $N$ projective hyperplanes satisfy
(7).

**Proof.**  A fixed point belongs to $[t]_q$ of the $N=[t+1]_q$
hyperplanes, so its inclusion probability is $p=[t]_q/N$.  Two distinct
projective points impose two independent linear equations on the normal of
a hyperplane, so their joint inclusion probability is

$$
p_2=\frac{[t-1]_q}{[t+1]_q}.
$$

The pair covariance is nonpositive.  Indeed, $p_2\leq p^2$ is equivalent to

$$
(q^{t-1}-1)(q^{t+1}-1)\leq(q^t-1)^2,
$$

and the right side minus the left side equals
$q^{t-1}(q-1)^2\geq0$.  Writing $X$ as a sum of the $s$ point-indicator
variables gives

$$
\operatorname{Var}X
=sp(1-p)+s(s-1)(p_2-p^2)
\leq sp=\mu,
$$

which proves (8).  Chebyshev's inequality now gives

$$
\Pr\left(|X-\mu|\geq\frac\mu2\right)
\leq\frac{4\operatorname{Var}X}{\mu^2}
\leq\frac4\mu\leq\frac12.
$$

Hence at least half of the hyperplanes are balanced. $\square$

### Step 2: every balanced choice is an unmarked type-zero extension

**Lemma 2.**  Suppose a history
$\sigma_{i-1}=(a_1,b_1,\ldots,a_{i-1},b_{i-1})$ has been constructed by
the following rule: at round $j$, choose

$$
b_j\in H_{a_j}\cap S_{j-1}.
\tag{9}
$$

Then $\sigma_{i-1}$ is consistent and

$$
Z_0^{\sigma_{i-1}}=S_{i-1}.
\tag{10}
$$

If $H_{a_i}$ is balanced for $S_{i-1}$ and
$b_i\in H_{a_i}\cap S_{i-1}$, then $(a_i,b_i)$ is an unmarked extension,
its source parameters satisfy $r=\ell=0$, and

$$
Z_0^{\sigma_i}=S_i=S_{i-1}\setminus H_{a_i}.
\tag{11}
$$

**Proof.**  The assertion is proved by induction.  It is true at the empty
history because every $W^{\sigma_0}(y)$ is the zero space.

Assume it holds through round $i-1$.  Since
$b_i\in S_{i-1}$, for every $j<i$ one has
$a_j\not\perp b_i$.  Thus every old-to-new consistency implication has a
false antecedent.  Also $a_i\perp b_i$ by (9), so $(a_i,b_i)$ is a vertex
of $D^*$ and extends the history consistently.

The same avoidance condition gives

$$
W^{\sigma_{i-1}}(b_i)=\{0\},
$$

so $r^{\sigma_{i-1}}(b_i)=0$ and necessarily $\ell=0$.  For every
$y\in Z_0^{\sigma_{i-1}}=S_{i-1}$, the old space $W(y)$ is zero.  Therefore
$b_i$ is contained in none of the spaces $W(y)$ and is not popular.

Let $s=|S_{i-1}|$ and $\mu=ps$.  Balancedness and the elementary estimate

$$
p=\frac{q^t-1}{q^{t+1}-1}>\frac{3}{4q}
\tag{12}
$$

give

$$
|N_G(a_i)\cap Z_0^{\sigma_{i-1}}|
=|H_{a_i}\cap S_{i-1}|
\geq\frac{ps}{2}>\frac{s}{8q}.
$$

Thus $a_i$ is not poor.  Since neither marking rule applies, the child is
unmarked.

Finally, for $y\in S_{i-1}$, appending $(a_i,b_i)$ changes $W(y)$ from zero
to $\langle b_i\rangle$ exactly when $y\in H_{a_i}$.  Points outside
$S_{i-1}$ already have positive rank and ranks never decrease.  This proves
(11).  A previously selected hyperplane is disjoint from the current
$S_{i-1}$, so balancedness prevents a repeated first coordinate.  Every
selected $b_j$ leaves $S$ at its own round, so no second coordinate is
repeated either.  This completes the induction. $\square$

### Step 3: the construction lasts for $\Theta(q\log q)$ rounds

For a balanced hyperplane, (7), $p<1/q$, and (11) imply

$$
|S_i|\geq\left(1-\frac{3}{2q}\right)|S_{i-1}|
=\alpha|S_{i-1}|.
\tag{13}
$$

Thus $|S_i|\geq\alpha^iN$.  For $q\geq4$,

$$
-\log\alpha
=-\log\left(1-\frac{3}{2q}\right)
\leq\frac{12}{5q}.
\tag{14}
$$

Here we used $-\log(1-x)\leq x/(1-x)$ with $x=3/(2q)$; for
$q\geq4$ its right side is at most $12/(5q)$.

Using $k_q\leq(t-1)q\log q/12$, (12), $N\geq q^t$, and (14), for every
$i<k_q$ we have

$$
p|S_i|
\geq \frac{3}{4q}\alpha^{k_q}q^t
\geq\frac34q^{4(t-1)/5}.
\tag{15}
$$

The last expression is at least $8$ for all sufficiently large $q$.
Consequently Lemma 1 applies at every one of the first $k_q$ rounds.  This
proves, in particular, that one cannot absorb all low-layer steps into an
$O_t(q)$ exceptional set.

### Step 4: count the all-unmarked paths

At a prefix of length $i<k_q$, Lemma 1 supplies at least $N/2$ balanced
choices for $a_{i+1}$.  For each such choice, (7) supplies at least

$$
\frac{p|S_i|}{2}\geq\frac{p\alpha^iN}{2}
$$

choices for $b_{i+1}$.  Hence every prefix in this recursively constructed
family has at least

$$
\frac{pN^2}{4}\alpha^i
$$

children in the family.  Multiplication for $0\leq i<k_q$ yields exactly
the lower bound (2).

To compare its exponential base, (12), $N\geq q^t$, and (14) give

$$
\begin{aligned}
L_q^{1/k_q}
&\geq\frac{pN^2}{4}\alpha^{(k_q-1)/2}\\
&\geq\frac{3}{16}q^{2t-1}
   \exp\left(-\frac{6k_q}{5q}\right)\\
&\geq\frac{3}{16}q^{2t-1-(t-1)/10}
=\frac{3}{16}q^{t+9(t-1)/10}.
\end{aligned}
$$

This proves (4), and (5) follows because $t\geq2$ is fixed. $\square$

### Step 5: a genuine bounded-multiplicity fact

**Lemma 5.**  Fix a projective point $a$.  Suppose the unmarked occurrences
along a path having first coordinate $a$ have second coordinates
$b_1,\ldots,b_m$ in chronological order.  Then
$b_1,\ldots,b_m$ are linearly independent and $m\leq t$.

**Proof.**  At the $j$-th such occurrence, the literal removal set of Claim
2.13 is nonempty.  Choose a point $y$ in it.  Then $y\perp a$ and

$$
b_j\not\subseteq W^{\sigma}(y),
$$

where $\sigma$ is the history immediately before this occurrence.  For
every $h<j$, the earlier pair $(a,b_h)$ contributes $b_h$ to
$W^\sigma(y)$ because the same relation $y\perp a$ holds.  Therefore

$$
\operatorname{span}(b_1,\ldots,b_{j-1})
\subseteq W^\sigma(y),
$$

and $b_j$ is outside the span of its predecessors.  All the $b_j$ lie in
$a^\perp$ because $(a,b_j)$ is a vertex of $D^*$.  The vector hyperplane
$a^\perp$ has dimension $t$, proving $m\leq t$. $\square$

This lemma is useful but does not close the encoding: the construction in
Steps 2--4 uses many distinct first coordinates, so it survives the
multiplicity bound.

### Step 6: why the proposed record map is impossible

For the all-unmarked signature in Steps 2--4 there are no marked-child
indices to specify.  Suppose the record proposal from
`NEXT_LOWER_BOUND.md` held with at most
$\exp(B_tq\log q)$ record values and at most $(C_tq^t)^{k_q}$ paths per
record.  It would give

$$
L_q\leq \exp(B_tq\log q)(C_tq^t)^{k_q}.
\tag{16}
$$

But (4) implies

$$
\log\frac{L_q}{(C_tq^t)^{k_q}}
\geq
k_q\left(\frac{9(t-1)}{10}\log q
+\log\frac{3}{16C_t}\right)
=\Omega_t(q\log^2q),
$$

which contradicts (16) for large $q$.  Thus a record consisting of the full
$U_j$ transition, or any other local record, cannot satisfy the proposed
record-count and preimage bounds uniformly over all signatures. $\square$

## Corrections or Missing Assumptions

- The earlier proposed record lemma must at least exclude or separately
  reweight the rank-zero hyperplane-cover histories above.  Merely declaring
  $O_t(q)$ low-rank steps exceptional is impossible.
- A repaired target could be restricted to histories with a sufficiently
  long marked tail, but then the proof must exhibit a quantitative entropy
  cancellation between that tail and the initial rank-zero family.  Claim
  2.13 supplies no such cancellation.
- Alternatively, one would need a weighted/non-uniform conversion in which
  the paths counted here have total weight exponentially below their raw
  cardinality, or a different $D^*$-type construction.

## Executable Check

Run

```bash
python3 routes/lower/transverse_encoding_check.py
```

The script verifies the exact negative pair covariance, the elementary
finite-$q$ inequalities used above, the $k_q$-round lower bound on
$p|S_i|$, and the logarithmic lower bound for $L_q^{1/k_q}$.  It checks
arithmetic consequences of the proof; it is not used in place of the
projective-incidence argument.

## Open Risks

- The lower bound (5) is at the specific constant
  $k_q\sim(t-1)q\log q/12$.  It does not disprove an upper bound stated only
  for $k\geq A_tq\log q$ with a sufficiently large $A_t$; in particular,
  the argument here must not be cited as a counterexample to every possible
  thresholded long-tail version.
- Raw forward-tuple abundance does not rule out a more selective permutation
  or a direct graph construction that suppresses precisely these histories.
- No improvement to a published Ramsey-number bound is claimed here.  The
  result is a proof-level obstruction that narrows what the next successful
  lemma must accomplish.
