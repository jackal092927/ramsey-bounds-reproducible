# Independent adversarial review: rank-zero transverse-encoding obstruction

Date: 2026-08-12  
Reviewed files:

- `TRANSVERSE_ENCODING_ATTEMPT.md`, SHA-256
  `abc50f95fd2f4674de5151283708bf2c47bbfc0d3affc39c65d4e62ec21bb16c`;
- `transverse_encoding_check.py`, SHA-256
  `1e8b32074597fbdf73573eb3874eb02fabab9b141a4ad1786af478b54377420a`.

Primary-source comparison: Bradač, arXiv:2605.28793v3, `main.tex`,
SHA-256
`90acf52f3766e780bc22114e08aa46b115cfe86e33d340e7f7eace01bb7fe39f`,
especially source lines 553 and 585--619.

## Verdict

**PASS AS A MECHANISM OBSTRUCTION.**  I found no fatal gap in the claimed
rank-zero path family, its path count, the fixed-first-coordinate lemma, or
the resulting contradiction to the scale-free record-map proposal retained
in `NEXT_LOWER_BOUND.md`.

This verdict does **not** certify a new Ramsey-number lower bound.  The result
only rules out the stated uniform record-map target, with
`exp(O_t(q log q))` records and at most `(C_t q^t)^u` preimages, when that
target is required for all lengths and signatures.  It does not rule out a
thresholded long-tail statement, a weighted tuple count, or a different
construction.

## Source-definition audit

The draft uses the same objects and threshold directions as Bradač's Claim
2.13:

1. A tuple is consistent precisely when each $a_i\perp b_i$ and, for
   $i<j$, $a_i\perp b_j$ implies $a_j\perp b_i$.
2. $W^\sigma(y)$ is the vector-space span of the earlier $b_i$ for which
   $a_i\perp y$, and $r^\sigma(y)=\dim W^\sigma(y)$.
3. For $b\in Z_r$, the source chooses
   $\ell=\ell_r^\sigma\in\{0,\ldots,r\}$ maximizing $|Z_\ell|$.
4. Popular means incidence with at least $|Z_\ell|/(16q)$ of the spaces
   $W(y)$, whereas poor means at most $|Z_\ell|/(8q)$ orthogonal points in
   $Z_\ell$.  Thus an unmarked pair must be strictly above the poor
   threshold and strictly below the popular threshold.
5. Forward-independent tuples are ordered tuples and may repeat vertices.
   The reviewed construction is stronger than needed here: along each path
   it produces distinct first coordinates and distinct second coordinates.

The polarity graph in the source permits loops at self-orthogonal points, so
the source equivalence `(a,b) in V(D*) iff a perpendicular to b` is literal;
there is no missing distinctness condition on $a$ and $b$.

## Detailed checks

### 1. Projective-incidence variance

There are $N=[t+1]_q$ projective hyperplanes, indexed bijectively by their
normal projective points.  A fixed point is in a uniformly random hyperplane
with probability

$$
p=\frac{[t]_q}{[t+1]_q},
$$

and two distinct points are jointly present with probability

$$
p_2=\frac{[t-1]_q}{[t+1]_q}.
$$

The covariance sign in the draft is correct, because

$$
(q^t-1)^2-(q^{t-1}-1)(q^{t+1}-1)
=q^{t-1}(q-1)^2\ge 0.
$$

Consequently $\operatorname{Var}|H\cap S|\le p|S|$.  If
$\mu=p|S|\ge8$, Chebyshev gives at most half the hyperplanes outside the
inclusive interval $[\mu/2,3\mu/2]$.  Hence the claimed lower bound of
$N/2$ balanced hyperplanes is valid for every eligible current set $S$,
not merely on average over the recursion.

### 2. Every constructed child is a genuine child of the $D^*$ tree

At step $i$, the chosen point
$b_i\in H_{a_i}\cap S_{i-1}$ satisfies $a_i\perp b_i$.  For every earlier
$j<i$, membership $b_i\in S_{i-1}$ gives
$a_j\not\perp b_i$.  All old-to-new consistency implications therefore
have false antecedent.  This proves that every selected pair extends the
actual consistent tuple, rather than a relaxed auxiliary process.

### 3. The identity $Z_0=S$

For $y\in S_i$, no selected $a_j$ is orthogonal to $y$, so
$W^{\sigma_i}(y)=\{0\}$.  Conversely, for $y\notin S_i$, some selected
$a_j$ is orthogonal to $y$, and its nonzero projective point $b_j$ lies in
$W^{\sigma_i}(y)$; hence this span is nonzero.  Therefore

$$
Z_0^{\sigma_i}=S_i
$$

exactly at every step.  Rank monotonicity prevents a previously removed
point from returning.

### 4. Strict popular/poor inequalities

Because $b_i\in S_{i-1}=Z_0$, one has
$r^{\sigma_{i-1}}(b_i)=0$ and hence $\ell=0$.  Every $W(y)$ for
$y\in Z_0$ is the zero subspace, so the projective point $b_i$ belongs to
zero of them.  Since $|Z_0|/(16q)>0$, $b_i$ is strictly below the popular
threshold.

Balancedness gives

$$
|H_{a_i}\cap Z_0|\ge \frac{p|Z_0|}{2}
>\frac{|Z_0|}{8q},
$$

where the strict inequality follows already from
$p>3/(4q)$.  Thus $a_i$ is strictly above the source's inclusive poor
threshold.  The child is genuinely unmarked.

### 5. Persistence and path multiplication

The balanced upper bound and $p<1/q$ give, uniformly over all constructed
prefixes,

$$
|S_i|\ge \left(1-\frac{3}{2q}\right)|S_{i-1}|.
$$

For $q\ge4$,

$$
-\log\left(1-\frac{3}{2q}\right)
\le \frac{3}{2q-3}\le\frac{12}{5q}.
$$

Together with
$k_q\le (t-1)q\log q/12$, this yields the draft's uniform lower bound
$p|S_i|\ge(3/4)q^{4(t-1)/5}$ for every $i<k_q$.  It exceeds $8$ for fixed
$t\ge2$ and all sufficiently large $q$, so the balanced-hyperplane lemma
continues to apply for all $k_q$ rounds.

At depth $i$, every constructed prefix has at least $N/2$ balanced choices
of $a$ and, for each, at least $p\alpha^iN/2$ choices of $b$.  Different
pairs give different children.  Multiplying these per-prefix bounds gives

$$
L_q=\left(\frac{pN^2}{4}\right)^{k_q}
\alpha^{k_q(k_q-1)/2}.
$$

The exponent algebra leading to

$$
L_q^{1/k_q}\ge
\frac{3}{16}q^{\,t+9(t-1)/10}
$$

is correct, including the direction of the inequality involving
$\alpha^{(k_q-1)/2}$.

### 6. Fixed-first-coordinate lemma

The source's literal removal block at an unmarked occurrence is nonempty:
its integer cardinality is at least the positive real number
$|Z_\ell|/(16q)$.  For a removal witness $y$ at the $j$-th unmarked
occurrence of a fixed $a$, every earlier second coordinate paired with that
same $a$ lies in $W^\sigma(y)$, because $y\perp a$.  The new $b_j$ does not
lie in that span by the definition of the removal block.  Hence the second
coordinates at these occurrences are linearly independent.  They all lie
in the $t$-dimensional vector hyperplane $a^\perp$, so there are at most
$t$ of them.

### 7. Quantifiers in the record-map contradiction

For the all-unmarked signature, $u=k_q$ and there are no marked-child
indices.  If the proposed uniform map had at most
$\exp(B_tq\log q)$ records and at most $(C_tq^t)^{k_q}$ paths in each
fiber, its total capacity would be their product.  But

$$
\log\frac{L_q}{(C_tq^t)^{k_q}}
=\Omega_t(q\log^2 q),
$$

whereas the allowed record term has logarithm only $O_t(q\log q)$.
This is a valid contradiction for every fixed $B_t,C_t$ and sufficiently
large prime powers $q$.

The contradiction depends essentially on the proposal being uniform over
all lengths and signatures.  It does not contradict a theorem assumed only
for $k\ge A_tq\log q$ when $A_t$ is larger than the constant reached by this
construction, nor Bradač's published $k\gtrsim_t q(\log q)^2$ bound.

## Executable audit

The supplied script compiled and its default grid passed.  Additional cases
`(t,q)=(2,257),(5,67),(8,31)` also passed.  I separately enumerated sampled
projective paths for the prime-field cases `(2,31)` and `(3,11)` and checked
the exact consistency implications, $Z_0=S$, the balanced-hyperplane count,
and the strict marking inequalities at every constructed step.

The script intentionally checks only arithmetic consequences; it does not
construct finite fields or certify that an arbitrary integer input is a
prime power.  The proof supplies the projective-geometric part, and the
document says this explicitly, so this is not a correctness defect.

## Resolved presentation note

After the initial review, the draft added the derivation
$-\log(1-x)\le x/(1-x)$ with $x=3/(2q)$ immediately after equation (14).
I checked this patch and the resulting reviewed hash recorded above.  It
resolves the only non-fatal presentation note and changes no statement or
constant.

## Earliest imported boundary

The first imported mathematical dependency is the exact definition and
marking rule in Bradač Claim 2.13.  From those definitions onward, the
obstruction is self-contained.  Its valid conclusion is:

> the scale-free uniform record-map proposal in `NEXT_LOWER_BOUND.md` is
> false, even on an all-unmarked type-zero signature.

It must not be promoted to a new Ramsey bound or to a claim that every
possible $q\log q$-threshold encoding is impossible.
