# Independent adversarial referee report: standalone GNNW book lemma

Date: 2026-08-12  
Audited file: `routes/upper/LEMMA11_STANDALONE_PROOF.md`  
Audited SHA-256:
`b402469d8b08009833b15489ea14ed2fa0417c333d7900d5de1d82b4e36b9c30`  
Primary comparison source: Gupta--Ndiaye--Norin--Wei,
[arXiv:2407.19026v1](https://arxiv.org/abs/2407.19026v1), Lemmas 7--11 and
Theorem 12.

## Verdict

**PASS, AFTER TWO LOCAL REPAIRS THAT ARE PRESENT IN THE AUDITED HASH.**

The audited version gives a self-contained proof of its Theorem A and
Corollary B.  These are the combinatorial statements needed in place of GNNW
Lemma 11 and Theorem 12.  I found no remaining fatal gap in the quantifiers,
regularization, book extraction, induction branches, strict contradiction, or
balanced-partition argument.

The two repairs required during review were:

1. the original draft's one-line real-binomial estimate in Lemma 3 was not a
   justified constant chain; it has been replaced by integer-valued discrete
   Jensen, `q=floor(D)`, and a valid product estimate;
2. the blue induction condition (5.17) now explicitly requires
   `alpha_B >= 0`, just as the red condition does.  Without that condition an
   even moment order could turn a negative density excess into a spurious
   positive branch certificate.

Both repairs are local.  They leave the statements and all asymptotic or
numerical parameters unchanged.

## Exact claim and dependency boundary

The audited claim has the following quantifier order.  For fixed real
parameters satisfying (A.1), there is one `L_0`, depending only on those
parameters, such that the conclusion holds simultaneously for every positive
integer triple `(k, ell, t)` with `ell >= L_0`.  In particular, `L_0` does not
depend on `k`, `t`, or `n=k+t`.

The proof uses only:

1. the definition of the two-colour Ramsey number;
2. the elementary Erdos--Szekeres recursion, in the standard consequence
   `R(k,m) <= binom(k+m-2,m-1)`;
3. Cauchy--Schwarz, discrete convexity, averaging, elementary calculus, and
   induction;
4. the stated topological definition of the rate region `R` and its interior.

The rate-region consequence actually used later is proved locally as Lemma 1;
GNNW Lemma 11 or Theorem 12 is not invoked in that proof.  Arb interval
semantics and the numerical descent certificates are outside this lemma's
scope.  Thus this report closes the formerly imported GNNW combinatorial
boundary, but it does not audit those later numerical dependencies.

## 1. Interior-point lemma and choice of parameters

### Lemma 1

The topology argument is valid.  If `(u,v)` is interior to the closed rate
region, one may move a sufficiently small positive distance northeast and
remain in the region.  Approximating that northeast point by a point in the
eventual-bound set gives `(u',v')` with both `u'>u` and `v'>v`.  Since
`(u')^{-a}(v')^{-b} <= u^{-a}v^{-b}`, its eventual bound implies (1.1).

### Lemma 4 and the moment order

The normalization

```text
(p^(1/r)-mu)^r (1-mu)^(1-r)
= (1-mu) [1+(p^(1/r)-1)/(1-mu)]^r
```

gives the limit in (4.1).  This remains valid for arbitrary `p,mu` in `(0,1)`:
`p^(1/r)>mu` for all sufficiently large `r`.  No assumption `p>mu` is needed.

The strict hypothesis implies `x_0+mu_0<1`, because
`p^(1/(1-mu_0))<1`.  The proof first chooses a sufficiently large integer
`r>1` with positive base and then chooses `epsilon`.  At `epsilon=0`, every
condition in (5.2) that needs room is strict.  Continuity and openness
therefore permit one common positive `epsilon`.  In particular:

- the special inequality tends at zero to
  `mu_0 < mu_0/(mu_0+x_0)`, equivalent to `x_0+mu_0<1`;
- `(p-epsilon)^(1/r)>mu_0+3epsilon` has positive room;
- the final inequality in (5.2) follows continuously from the strict choice
  of `r` in (5.1).

No circular choice of `r` and `epsilon` remains.

## 2. One uniform `L_0`

All appearances of "increase `L_0`" can be satisfied simultaneously, uniformly
over `n=k+t`.  Put `A=1+epsilon>1`.  It is enough to dominate the following
finite suprema (with harmless changes to fixed constants):

```text
sup_{n>=2} n^r A^(-n),
sup_{n>=2} m(n)^2 A^(-n),
sup_{n>=2} n^3 R(k,m(n)) A^(-n),
sup_{n>=2} n^2 A^(-n).
```

For the third expression, `k<=n`, `m(n)=O(log^2 n)`, and

```text
R(k,m(n)) <= (k+m(n))^m(n) = exp(O(log^3 n)) = exp(o(n)).
```

Every displayed supremum is finite because `A^n` is genuinely exponential.
The eventual rate-region threshold is also uniform once `ell>=L_0`, since
`k+ell>=ell`.  Taking the maximum of these finitely many thresholds proves
that (5.6), (5.10), (5.20), and the use of Lemma 1 all share one `L_0`.

## 3. Regularization and preservation of (5.5)

Let `theta=p-delta_n`,

```text
E=e_R(X,Y)-theta|X||Y|,
F=E/(|X||Y|)=d(X,Y)-theta.
```

Condition (5.4) gives `F>=0`, and the positive right side of (5.5) actually
gives `F>0`.  Deleting a vertex with red degree below `theta|Y|` strictly
increases `E`; it also decreases the denominator, so `F` increases.  The
moment on the left of (5.5) is

```text
F^r |X||Y| = F^(r-1) E.
```

It therefore cannot decrease.  The process cannot delete the last vertex,
because that would contradict the maintained positive excess.  At termination
every remaining vertex has the required red degree, and averaging over any
nonempty subset proves (5.7).

The later size estimate (5.8) is also in the correct direction.  The moment
base is positive and at most one, while failure of the Ramsey alternative in
`Y` gives the required strict upper bound on `|Y|`.  Moreover,

```text
(x+epsilon)/x >= 1+epsilon,
(y+epsilon)/y >= 1+epsilon,
mu^(-1) >= 1+epsilon,
```

where the last inequality is exactly a consequence of
`(1+epsilon)mu<=1`.  Hence the final exponent is `k+ell+t=n+ell`.

## 4. Blue-book extraction, including the repaired constants

This was the earliest gap in the first draft and is correct in the audited
version.

Let `U` be the blue `K_m` and let `D` be the average over `z in X\\U` of
`d_z=|N_B(z) intersect U|`.  Counting from `U`, and harmlessly subtracting
`m` rather than `m-1`, gives

```text
D >= m(nu|X|-m)/(|X|-m)
  = nu m - (1-nu)m^2/(|X|-m)
  > nu m - 1/4.
```

The last inequality holds even at `m=1`: `|X|>=5m^2` makes the quotient at
most `1/4`, and `1-nu<1` makes it strict.

For integer `j>=0`, with `binom(j,b)=0` below `b`, the first differences of
`binom(j,b)` are nondecreasing.  Thus the sequence is discretely convex.  If
`q=floor(D)`, smoothing integer degrees at fixed mean, or equivalently the
piecewise-linear Jensen inequality, gives

```text
average_z binom(d_z,b) >= binom(q,b).
```

There is no unjustified use of a real generalized binomial coefficient.

Since `q>D-1>nu m-5/4`, for every `0<=i<b`,

```text
(q-i)/(m-i)
> nu - ((1-nu)i+5/4)/(m-i)
>= nu(1-(b+1/4)/(5b^2)).
```

The subtracted fraction increases with `i`, so it suffices to take `i=b-1`
and the smallest allowed `m=5b^2/nu`.  After cross-multiplication the remaining
nonnegative margin is

```text
nu(b-1)(1-(b+1/4)/(5b^2)).
```

If `q<b`, taking `i=q` in the preceding positive lower bound would give
`0>0`; hence `q>=b` and the product ratio is legitimate.  It follows that

```text
binom(q,b)/binom(m,b)
>= nu^b(1-(b+1/4)/(5b^2))^b
>= (3/4)nu^b.
```

For `b=1` the factor is exactly `3/4`.  For `b>=2`, Bernoulli gives a lower
bound strictly larger than `3/4`.  Finally `|X\\U|>=4|X|/5`, so the expected
page size is at least `3nu^b|X|/5`, which is stronger than (3.1).

## 5. The big-blue induction branch and (5.11)

All parameters of Lemma 3 are met.  In its application
`nu=mu+epsilon`, while `m>=5mu^(-1)b^2` is stronger than
`m>=5nu^(-1)b^2`.  The conditions in (5.2) also ensure `nu<1`.

If `b>=t`, the blue base itself contains the target blue clique.  Otherwise
`t-b>=1`, so induction at `n-b<n` is allowed.  Regularization gives the density
condition for `(T,Y)`, and

```text
delta_(n-b)-delta_n >= delta_(n-1)-delta_n >= epsilon/n^2.
```

The factor direction in (5.11) is correct.  From (5.5) and the fact that its
moment base is at most one,

```text
|X||Y| >= x^(-k)y^(-ell)mu^(-t).
```

Also `(mu+epsilon)/mu>=1+epsilon`, and the definition of `b` gives

```text
(1/2)(epsilon/n^2)^r ((mu+epsilon)/mu)^b >= 1.
```

Thus the target moment has exactly `mu^(-t+b)`.  A blue `K_(t-b)` in the page
joins the blue base, while either of the other goodness outcomes lifts
directly.

## 6. Red-step averaging and both one-vertex branches

The contribution of `W` is at most `w|Y|`.  Since
`e_R(X,Y)>=(p-epsilon)|X||Y|`, (5.10) gives the displayed bound by
`epsilon e_R(X,Y)/n^3`.  Lemma 2 then gives a weighted average over
`X\\W`; the total remaining weight is at most `e_R(X,Y)`.  Because the target
density is positive, this proves the existence of the vertex in (5.13).

For this vertex, `Y'` is nonempty and

```text
alpha >= delta_(n-1)-delta_n-epsilon/n^3 >= epsilon/n^2 > 0.
```

Equation (5.15) follows by splitting `X` into `X_R`, `X_B`, and `{v}`.
The `+1` is valid because every edge from `v` to `Y'` is red; the resulting
expression exceeds the desired excess by `p'|Y'|>=0`.

For (5.16), multiplication by `|Y'|` and
`|Y'|>=(p-epsilon)|Y|` supplies the factor `x`.  Inequality (5.13) plus
the exact delta calculation gives

```text
d(X,Y')-p' >= d(X,Y)+delta_n-p,
```

so the target moment is `x^(-k+1)y^(-ell)mu^(-t)`.  The vertex `v` is red
to both `X_R` and `Y'`, so all three goodness outcomes lift correctly.

The blue branch is identical with factor `mu` and target
`x^(-k)y^(-ell)mu^(-t+1)`.  The audited (5.17) includes the essential
condition `alpha_B>=0`, so its density hypothesis is valid.  A blue
`K_(t-1)` in `X_B` joins `v`; the red and `Y'`-blue alternatives already lie
in the original candidate.

If `X_R` or `X_B` is empty, its weighted term is interpreted as zero and its
branch is skipped, exactly as the text states.  The corresponding
`a^q` or `c^q` term is also zero.  Equation (5.8) gives `|X|>1`, so at least
one of the two sets is nonempty and at least one failed-branch estimate is
strict.  Consequently (5.18), not merely a weak version of it, follows.

## 7. The terminal contradiction

Here `q=1-1/r` lies in `(0,1)`, `a+c=1-|X|^(-1)<1`, and
`c<=mu+epsilon`.  Hence

```text
x^(1/r)a^q + mu^(1/r)c^q <= f(c),
f(z)=x^(1/r)(1-z)^q+mu^(1/r)z^q.
```

Direct differentiation shows that `f` is increasing precisely through
`z=mu/(mu+x)`.  The special condition in (5.2) puts the entire required
interval below this point.  At the endpoint,

```text
x^(1/r)(1-mu-epsilon)^q <= x^(1/r)(1-mu)^q,
mu^(1/r)(mu+epsilon)^q <= mu+epsilon,
```

which proves (5.19) in the stated direction.

The bound in (5.20) is uniform by Section 2.  Substitution into the strict
(5.18) preserves strictness and gives

```text
x^(1/r)(1-mu)^(1-1/r)+mu+2epsilon
> (p-epsilon)^(1/r).
```

The right-side difference is positive by (5.2), so raising to the `r`th
power is order-preserving and yields the strict (5.21).  With
`x=x_0+epsilon` and `mu=mu_0+epsilon`, the final line of (5.2) says exactly
the opposite weak inequality.  This is a genuine contradiction.

## 8. Corollary B and rounding

Because `(x,y)` is interior, a small increase in only the second coordinate
gives `y_0>y` with `(x,y_0)` still interior.  In a uniformly random equitable
bipartition every edge has the same crossing probability and the number of
cross pairs is fixed.  Therefore the average cross-red density equals the
global red density, and one equitable partition has cross-red density at
least `p`.

Let

```text
A=x^(-k/2)(mu y_0)^(-ell/2).
```

Here `A>1`.  Once `(y_0/y)^(ell/2)>=3`, (B.2) gives
`N>=3A>=2A+1`.  Thus the smaller equitable part satisfies
`floor(N/2)>=(N-1)/2>=A`; this explicitly resolves the integer rounding.
Both parts have size at least `A`, their product meets Theorem A with
`t=ell`, and every possible goodness outcome is the desired Ramsey outcome.

## Residual risks

No mathematical gap remains in the audited statements.  The following are
scope notes, not blockers:

- this is a human line-by-line replay, not a proof-assistant formalization;
- if the standalone proof is edited after the audited SHA-256, this report
  must be rechecked against the new hash;
- the certified numerical descent still separately depends on faithful Arb
  interval semantics and on the corresponding certificate audits.

