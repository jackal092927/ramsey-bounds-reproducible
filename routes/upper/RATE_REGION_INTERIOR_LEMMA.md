# Proof Package: strict two-sided rates give a Ramsey-region interior point

## Claim

Let $U:(0,1]\to\mathbb R$ extend continuously to $[0,1]$ with $U(0)=0$.
Assume the uniform one-sided rate bound

$$
\log R(k,\ell)\le kU(\ell/k)+o(k)
$$

for all positive integers $\ell\le k$, where the $o(k)$ term is uniform over
$1\le\ell\le k$.

Let $a,b>0$ satisfy

$$
b>\sup_{0<\mu\le1}\frac{U(\mu)-a}{\mu}
\tag{S}
$$

and

$$
b>\sup_{0<\mu\le1}\bigl(U(\mu)-\mu a\bigr).
\tag{W}
$$

Then

$$
(e^{-a},e^{-b})\in\mathcal R_*.
$$

Here $\mathcal R$ and $\mathcal R_*$ are the Ramsey rate region and its
interior as defined at GNNW arXiv:2407.19026v1, source lines 258--268.

## Status

PROVABLE AS STATED.

## Assumptions

- Ramsey symmetry: $R(k,\ell)=R(\ell,k)$.
- The one-sided rate is uniform over all integer ratios $1\le\ell\le k$.
- GNNW Observation 7(3)--(4): a global asymptotic monomial bound gives a point
  in $\mathcal R$, and strict coordinatewise decrease from a point of
  $\mathcal R$ gives a point of $\mathcal R_*$.

## Notation

- $X=e^{-a}$ and $Y=e^{-b}$.
- For $0\le\mu\le1$ define

  $$
  h_S(\mu)=a+\mu b-U(\mu),
  \qquad
  h_W(\mu)=b+\mu a-U(\mu).
  $$

## Proof Strategy

Conditions (S) and (W) certify the two possible orders of the Ramsey
parameters.  Their strictness, continuity, and the positive endpoint values at
$\mu=0$ give a uniform exponent margin.  That margin permits both $X$ and $Y$
to be enlarged while retaining the global rate bound.  The original point is
then strictly below a point of $\mathcal R$, hence is in the interior.

## Dependency Map

1. Conditions (S) and (W) imply $h_S,h_W>0$ on $(0,1]$.
2. Continuity at zero gives a positive uniform minimum on $[0,1]$.
3. A small simultaneous decrease of $a,b$ preserves both rate inequalities.
4. The first inequality handles $\ell\le k$; the second handles $k\le\ell$
   after Ramsey symmetry.
5. GNNW Observation 7(4), followed by Observation 7(3), gives interior
   membership.

## Proof

### Step 1: convert the envelope conditions into exponent slack

For every $0<\mu\le1$, condition (S) gives

$$
b>\frac{U(\mu)-a}{\mu}.
$$

Multiplication by $\mu>0$ yields

$$
h_S(\mu)=a+\mu b-U(\mu)>0.
$$

Condition (W) gives directly

$$
h_W(\mu)=b+\mu a-U(\mu)>0.
$$

Because $U(0)=0$, the continuous extensions satisfy

$$
h_S(0)=a>0,
\qquad
h_W(0)=b>0.
$$

Both functions are therefore positive and continuous on the compact interval
$[0,1]$.  Consequently

$$
\Delta=min_{0\le\mu\le1}\min\{h_S(\mu),h_W(\mu)\}>0.
\tag{1}
$$

This compactness step is important: strict pointwise inequalities without the
positive limits at $\mu=0$ would not by themselves provide a common
coordinate perturbation.

### Step 2: enlarge both Ramsey coordinates

Choose

$$
0<\eta<\min\left\{a,b,\frac{\Delta}{4}\right\}
$$

and put

$$
a'=a-\eta,
\qquad
b'=b-\eta,
\qquad
X'=e^{-a'},
\qquad
Y'=e^{-b'}.
$$

Then $X'>X$ and $Y'>Y$.  For every $0\le\mu\le1$,

$$
a'+\mu b'-U(\mu)
=h_S(\mu)-\eta(1+\mu)
\ge\Delta-2\eta
>\frac{\Delta}{2},
\tag{2}
$$

and similarly

$$
b'+\mu a'-U(\mu)>\frac{\Delta}{2}.
\tag{3}
$$

Thus both ordered-pair rate inequalities remain strict after both coordinates
are enlarged.

### Step 3: cover the order $\ell\le k$

Let $\ell\le k$ and set $\mu=\ell/k$.  By the assumed prior rate and (2),

$$
\begin{aligned}
\log R(k,\ell)
&\le kU(\mu)+o(k)\\
&\le k(a'+\mu b')-\frac{\Delta}{2}k+o(k)\\
&=ka'+\ell b'-\frac{\Delta}{2}k+o(k).
\end{aligned}
$$

The displayed linear margin absorbs the uniform sublinear error.  Hence, for
all sufficiently large $k$ (uniformly over $1\le\ell\le k$),

$$
R(k,\ell)\le (X')^{-k}(Y')^{-\ell}.
\tag{4}
$$

### Step 4: cover the order $k\le\ell$

Now let $k\le\ell$ and put $\mu=k/\ell$.  Ramsey symmetry and the prior rate
applied to $(\ell,k)$ give

$$
\begin{aligned}
\log R(k,\ell)
&=\log R(\ell,k)\\
&\le \ell U(\mu)+o(\ell)\\
&\le \ell(b'+\mu a')-\frac{\Delta}{2}\ell+o(\ell)\\
&=ka'+\ell b'-\frac{\Delta}{2}\ell+o(\ell).
\end{aligned}
$$

The linear margin again absorbs the uniform $o(\ell)$ term.  Thus (4) holds
for all sufficiently large $\ell$, uniformly over $1\le k\le\ell$.

### Step 5: pass from the global rate to the interior

Steps 3--4 give a common threshold in $k+\ell$ after taking the larger of the
two uniform thresholds.  By the definition of $\mathcal R$ (equivalently,
by the strengthened form of GNNW Observation 7(4)),

$$
(X',Y')\in\mathcal R.
$$

Since $0<X<X'$ and $0<Y<Y'$, Observation 7(3) gives

$$
(X,Y)=(e^{-a},e^{-b})\in\mathcal R_*.
$$

This proves the claim. $\square$

## Application to the current certificate

For the elementary prior used by
`certificate-recommended-beta00299-split005.json`, the function $U$ is analytic on
$(0,1]$ and has $U(\mu)\to0$ as $\mu\downarrow0$.  The Arb verifier proves
strict upper bounds for both suprema (S) and (W) on every target-lambda cell.
Its reported minimum margins are respectively

$$
5.8529290109470086\times10^{-5}
$$

and

$$
6.074652597491317\times10^{-5}.
$$

Therefore every large-regime witness point certified by the file lies in
$\mathcal R_*$, not merely in the closure $\mathcal R$.

## Corrections or Missing Assumptions

- If the prior $o(k)$ term were only pointwise for each fixed ratio rather than
  uniform over integer pairs, GNNW Observation 7(4) would require an additional
  uniformization argument.  The corrected descent proof supplies an
  epsilon-uniform rate, which is the interpretation used here.
- This lemma repairs the large-regime interior step for the current candidate.
  It does not make the printed GNNW Theorem 13 valid for arbitrary witness
  functions satisfying only non-strict membership in $\mathcal R$.

## Open Risks

- A second Arb implementation now directly verifies both exponent slacks
  without the scalar-envelope reduction; formal proof-assistant replay remains
  optional trust reduction.
- The separate small-regime interior argument uses the elementary
  $X+Y=1$ boundary and is documented in `THEOREM_AUDIT.md`; it is not an
  application of this strict-rate lemma.
