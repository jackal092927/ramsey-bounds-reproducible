# Independent proof replay: the beta 0.0299 upper bound

## Claim

Let

$$
H(\lambda)=(1+\lambda)\log(1+\lambda)-\lambda\log\lambda
$$

and

$$
F(\lambda)=H(\lambda)+
\left(-\frac14\lambda+0.0299\lambda^2+0.08\lambda^3\right)e^{-\lambda}
\qquad (0<\lambda\leq 1).
$$

Then

$$
R(k,\ell)\leq \exp\!\left(F(\ell/k)k+o(k)\right)
\qquad (1\leq \ell\leq k),
$$

where the $o(k)$ is uniform over $1\leq\ell\leq k$. In particular,

$$
R(k,k)\leq
\left(3.799062977328661874100936344594\ldots\right)^{k+o(k)}.
$$

The numerical witness is the exact-decimal JSON object
`certificate-recommended-beta00299-split005.json`, whose SHA-256 is

```text
f7344d74bb2e5f033e14dbe9e943af7b90e52937d86610eb9f2dc548605aa11e
```

## Status

**PROVABLE AS STATED**, subject to the explicitly declared imported GNNW
combinatorial result below. The claimed bound survives unchanged.

The proof does **not** invoke GNNW Theorem 13 as literally printed. Its
displayed derivative sign is impossible, and its proof omits an
$\mathcal R_*$ justification. Section 5 below gives and proves the
candidate-specific repaired descent statement actually used.

## Assumptions and imported result

1. We use the standard symmetry $R(k,\ell)=R(\ell,k)$.
2. We use Gupta--Ndiaye--Norin--Wei (GNNW),
   [arXiv:2407.19026v1](https://arxiv.org/abs/2407.19026v1), Theorem 12
   (called `t:bookCor` in the TeX source), including its dependency on their
   Lemma 11. The source proof of Theorem 12 contains several local direction,
   strictness, and quantifier typos; `BOOKCOR_AUDIT.md` supplies a complete
   repaired replay. We do not re-prove the earlier combinatorial Lemma 11.
3. We do not treat the application of Theorem 12 as a black box: its strict
   $x$ inequality, its $\mathcal R_*$ hypothesis, the finite-net
   uniformity, and every substitution into it are checked in Section 5.
4. We trust the documented enclosure semantics of Arb as exposed by
   `python-flint==0.9.0`. Every accepted inequality is strict between Arb
   balls at 256-bit precision.

The imported GNNW theorem is:

> If $0<\mu,x,y,p<1$, $x<p^{1/(1-\mu)}(1-\mu)$, and
> $(x,y)\in\mathcal R_*$, then there is $L_0$ such that, for all positive
> $k,\ell$ with $\ell\geq L_0$, every red-blue coloring of $K_N$ with red
> density at least $p$ and
> $N\geq x^{-k/2}(\mu y)^{-\ell/2}$ contains a red $K_k$ or a blue
> $K_\ell$.

## Notation and exact quantifiers

GNNW define $\mathcal R$ as the closure in $\mathbb R^2$ of the set of
pairs $(x,y)\in(0,1)^2$ for which there is $N_0=N_0(x,y)$ such that

$$
R(k,\ell)\leq x^{-k}y^{-\ell}
$$

for **all positive integers** $k,\ell$ satisfying $k+\ell\geq N_0$.
They define $\mathcal R_*$ to be the interior of $\mathcal R$.

Write

$$
a=-\log x,\qquad b=-\log y.
$$

The elementary Erdős--Szekeres region gives
$(x,1-x)\in\mathcal R$ for $0<x<1$. The valid monotonicity direction is:
if $(x,y)\in\mathcal R$ and $0<x'\leq x$, $0<y'\leq y$, then
$(x',y')\in\mathcal R$. The inequality printed in the proof of GNNW
Observation 9(2) has its comparison sign reversed, but the observation itself
and its immediate proof by exponentiation have the stated direction.

For an asymptotic rate in this replay, the precise meaning is the following
uniform epsilon statement: for every $\varepsilon>0$, there is $K_0$ such
that the displayed upper bound with $o(k)$ replaced by $\varepsilon k$
holds for all $k\geq K_0$ and all $1\leq\ell\leq k$. This is the strength
proved by the repaired finite-net argument in Section 5.

## Proof Strategy

The proof is a two-stage descent: first certify an elementary prior rate, then
use its strict two-sided rate region to certify the target rate.

## Dependency Map

1. Certify an elementary prior rate $U$ using only the
   Erdős--Szekeres boundary $Y=1-X$ and the repaired descent lemma.
2. Convert that one-sided prior rate into a two-orientation inner description
   of $\mathcal R$; strict inequalities imply membership in
   $\mathcal R_*$.
3. Use the JSON witness to certify the target $F$ on
   $[5\cdot10^{-3},1]$ against both prior-rate orientations.
4. On $(0,5\cdot10^{-3}]$, use the elementary witness directly and prove its
   main inequality analytically.
5. Apply the repaired finite-net descent lemma to obtain the target rate.
6. Substitute $\lambda=1$.

The only unreproved combinatorial core is GNNW Lemma 11.  Theorem 12 is
replayed with source repairs in `BOOKCOR_AUDIT.md`; the rate, region, interior,
finite-net, and numerical-continuum bridges are all supplied here.

## Proof

### 1. Source-level audit of GNNW Theorem 13

The literal statement at TeX source line 406 assumes $F'(\lambda)<0$ and sets

$$
X(\lambda)=
(1-e^{-F'(\lambda)})^{1/(1-M(\lambda))}(1-M(\lambda)).
$$

This sign cannot be correct. If $F'<0$, then $1-e^{-F'}<0$, so the displayed
real-valued $X$ is generally undefined. The proof sets the red-density
parameter to $1-e^{-F'+2\delta}$, which must lie in $(0,1)$, and the explicit
GNNW functions have $F'>0$. The required hypothesis is therefore

$$
F'(\lambda)>0.
$$

There is a second, logically independent defect. Theorem 13 assumes only
$(X,Y)\in\mathcal R$, while Theorem 12 requires the parameter passed to it to
belong to $\mathcal R_*$. The proof shrinks $X$ to $x_\lambda<X$ but leaves
$Y$ unchanged. For a general downward-closed set, shrinking only one
coordinate of a boundary point need not produce an interior point.

There is also a uniformity omission in the theorem's printed generality. The
choice of a single $\delta$ in its finite-net proof contains the factor
$1/(1-M(\lambda))$. With arbitrary, possibly discontinuous $M$ taking values
arbitrarily close to $1$, the asserted uniform $\delta$ need not exist.
The candidate witnesses satisfy the needed compact-uniform bound, and the
repaired lemma below states it.

Finally, two local source expressions need their evident corrections:

* the `p` and `mu` in the definition of $x_\lambda$ at source line 426 mean
  $p_\lambda$ and $M(\lambda)$;
* $F((\ell-1)k)$ at source line 435 means
  $F((\ell-1)/k)$, as the following mean-value calculation confirms;
* the last derivative estimate is valid with
  $\sup|F''|/k$, not the printed $\max F''/k$.

Thus the literal general Theorem 13 is not used. These corrections are all
incorporated below.

### 2. From a one-sided rate to the two required envelopes

Let $U:(0,1]\to\mathbb R$ be a rate satisfying, uniformly for
$1\leq\ell\leq k$,

$$
\log R(k,\ell)\leq kU(\ell/k)+o(k).
\tag{2.1}
$$

Fix $(x,y)\in(0,1)^2$ and put $a=-\log x$, $b=-\log y$.
For $\ell\leq k$, set $\mu=\ell/k$. To dominate (2.1), one needs

$$
a+\mu b\geq U(\mu).
\tag{2.2}
$$

For $k\leq\ell$, symmetry gives
$\log R(k,\ell)=\log R(\ell,k)\leq\ell U(k/\ell)+o(\ell)$.
With $\mu=k/\ell$, one independently needs

$$
b+\mu a\geq U(\mu).
\tag{2.3}
$$

It is therefore not enough to accept either orientation. Both are required.

#### Lemma 2.1 (strict two-sided rate implies interior)

Assume that $U$ extends continuously to $U(0)=0$, that (2.1) holds in the
uniform epsilon sense, and that both (2.2) and (2.3) are strict for every
$0<\mu\leq1$. Then $(x,y)\in\mathcal R_*$.

##### Proof

Define on $[0,1]$

$$
D_1(\mu)=a+\mu b-U(\mu),\qquad
D_2(\mu)=b+\mu a-U(\mu).
$$

They are continuous; $D_1(0)=a>0$, $D_2(0)=b>0$, and they are positive by
hypothesis elsewhere. Compactness gives

$$
d=\min_{\mu\in[0,1]}\min(D_1(\mu),D_2(\mu))>0.
$$

Choose $0<\eta<\min(a,b,d/4)$ and put
$a^+=a-\eta$, $b^+=b-\eta$,
$x^+=e^{-a^+}>x$, $y^+=e^{-b^+}>y$. For every $\mu\in[0,1]$,

$$
a^++\mu b^+-U(\mu)
=D_1(\mu)-\eta(1+\mu)\geq d-2\eta>0,
$$

and the same estimate holds in the swapped orientation. Taking the rate error
smaller than $d-2\eta$ proves, for all sufficiently large $k+\ell$ and both
orders of $k,\ell$,

$$
R(k,\ell)\leq (x^+)^{-k}(y^+)^{-\ell}.
$$

Thus $(x^+,y^+)\in\mathcal R$. Since both coordinates of $(x,y)$ are
strictly smaller, GNNW Observation 9(3) gives
$(x,y)\in\mathcal R_*$. $\square$

This argument resolves the quantifier issue directly and does not rely on an
ambiguous, non-uniform reading of the $o(k),o(\ell)$ in Observation 9(4).

### 3. Scalar reduction of both envelopes

The certified prior is

$$
U(\mu)=H(\mu)+
\left(-0.25\mu+0.08\mu^2+0.08\mu^3\right)e^{-\mu}.
\tag{3.1}
$$

All displayed coefficients, including `0.08`, are the exact decimals stored
in the frozen certificate and checked by Arb.

For fixed $a>0$, conditions (2.2)--(2.3) are equivalent to

$$
b> B_{\rm std}(a):=sup_{0<\mu\leq1}\frac{U(\mu)-a}{\mu}
\tag{3.2}
$$

and

$$
b>B_{\rm swap}(a):=sup_{0<\mu\leq1}\left(U(\mu)-\mu a\right).
\tag{3.3}
$$

The checker first proves $U''(\mu)<0$ on all of $(0,1]$. On
$(0,10^{-3}]$, the entropy contribution satisfies

$$
-\frac1{\mu(1+\mu)}\leq-\frac1{0.001001},
$$

while Arb bounds the polynomial-exponential correction by less than $1$.
It checks $[10^{-3},1]$ using 4,096 interval cells. The replayed worst upper
bound for $U''$ is $-0.40787039816230575$.

Set

$$
A(\mu)=U(\mu)-\mu U'(\mu).
$$

Then $A'(\mu)=-\mu U''(\mu)>0$. Differentiating (3.2)'s objective gives

$$
\frac{d}{d\mu}\frac{U(\mu)-a}{\mu}
=\frac{a-A(\mu)}{\mu^2}.
$$

Hence its sole possible interior maximum solves $A(\mu)=a$, and at that
point the value is $U'(\mu)$. Endpoint $\mu=1$ is retained. Similarly, the
derivative of (3.3)'s objective is $U'(\mu)-a$; strict concavity makes
$U'$ decreasing, so its sole possible interior maximum solves $U'(\mu)=a$,
again with endpoints retained. This proves the envelope reduction implemented
in `envelope_upper_candidates`; it is not a heuristic optimizer.

For an interval of target $\lambda$ values, the checker obtains a rigorous
lower endpoint $a_{\min}$ of $a(\lambda)$. Both envelope suprema decrease as
$a$ increases. Evaluating them at $a_{\min}$ is therefore a valid worst-case
upper bound for the entire target interval.

### 4. Certifying the elementary prior rate

For (3.1), define for every $0<\lambda\leq1$

$$
M(\lambda)=\lambda e^{-\lambda},
$$

$$
X(\lambda)=
(1-e^{-U'(\lambda)})^{1/(1-M(\lambda))}(1-M(\lambda)),
\qquad Y(\lambda)=1-X(\lambda).
$$

The elementary Ramsey region gives $(X,Y)\in\mathcal R$. Although this point
can lie on the boundary, the perturbed parameter used in Section 5 satisfies
$x_\lambda<X$. Hence $x_\lambda+Y<1$. Choose $z$ with
$x_\lambda<z<X$. Then $Y=1-X<1-z$ and
$(z,1-z)\in\mathcal R$, so downward closure gives a northeast point of
$(x_\lambda,Y)$ in $\mathcal R$. Observation 9(3) yields

$$
(x_\lambda,Y)\in\mathcal R_*.
\tag{4.1}
$$

The checker proves $U>0$, $U'>0$, and

$$
U(\lambda)+\frac12\bigl(
\log X(\lambda)+\lambda\log M(\lambda)+\lambda\log Y(\lambda)
\bigr)>0
\tag{4.2}
$$

on all of $(0,1]$. The interval $[5\cdot10^{-3},1]$ is covered by 4,096 Arb
cells. The worst certified slack there is
$3.1150059697914928\times10^{-8}$.

For completeness, the open interval down to zero is not inferred from a
finite sample. If $P(\lambda)$ is the polynomial correction and
$q=e^{-U'}$, the analytic routine bounds

$$
q_-\lambda\leq q\leq q_+\lambda,
\qquad -\log X\leq C\lambda,
\qquad Y\geq M+q-Mq\geq D\lambda
$$

for positive constants $q_-,q_+,C,D$ on $(0,5\cdot10^{-3}]$. It also bounds
$|P(\lambda)|\leq C_0\lambda$ and
$|P'(\lambda)-P(\lambda)|\leq C_1$. Substituting
$\log M=\log\lambda-\lambda$ and
$\log Y\geq\log\lambda+\log D$ into (4.2) cancels both
$\lambda\log\lambda$ singularities. Arb proves

$$
\frac{\text{left side of (4.2)}}{\lambda}
\geq 0.00330349733874634\ldots>0.
$$

The repaired descent lemma in Section 5, together with (4.1)--(4.2), now
proves the uniform one-sided rate (2.1) for $U$. No use is made of GNNW
Lemma 14.

### 5. Candidate-specific repaired finite-net descent

#### Lemma 5.1 (finite-net descent sufficient for these witnesses)

Let $G:(0,1]\to\mathbb R_+$ be smooth with $G'>0$. Suppose functions
$M,X,Y:(0,1]\to(0,1)$ satisfy

$$
X(\lambda)=
(1-e^{-G'(\lambda)})^{1/(1-M(\lambda))}(1-M(\lambda))
\tag{5.1}
$$

and

$$
G(\lambda)>-\frac12\left(
\log X(\lambda)+\lambda\log M(\lambda)+\lambda\log Y(\lambda)
\right)
\tag{5.2}
$$

for all $\lambda$. Assume in addition that, for every compact
$I\subset(0,1]$,

$$
\inf_{I}G'>0,\qquad \sup_I M<1,
\tag{5.3}
$$

and that the BookCor parameter $(x_{\lambda,\delta},Y(\lambda))$ defined
below lies in $\mathcal R_*$ for all sufficiently small $\delta>0$. Then

$$
R(k,\ell)\leq\exp(G(\ell/k)k+o(k))
$$

uniformly for $1\leq\ell\leq k$.

##### Proof

Fix $\varepsilon>0$. The classical Erdős--Szekeres estimate gives
$\log R(k,\ell)\leq kH(\ell/k)+o(k)$ uniformly as $\ell/k\to0$.
For both functions used here, $H(\lambda)-G(\lambda)=O(\lambda)$ at zero.
Choose $\rho>0$ so that this difference is at most $\varepsilon/2$ on
$(0,\rho]$; after increasing the threshold, the desired bound with error
$\varepsilon k$ already holds for $\ell\leq\rho k$.
It remains to work on $I=[\rho,1]$.

For $\lambda\in I$ and $\delta>0$, set

$$
p_{\lambda,\delta}=1-e^{-G'(\lambda)+2\delta},
$$

$$
x_{\lambda,\delta}
=e^{-\delta}\,
p_{\lambda,\delta}^{1/(1-M(\lambda))}(1-M(\lambda)).
\tag{5.4}
$$

For sufficiently small $\delta$, (5.3) gives $p_{\lambda,\delta}\in(0,1)$
uniformly. Also

$$
\log\frac{x_{\lambda,\delta}}{X(\lambda)}
=-\delta+\frac{1}{1-M(\lambda)}
\log\frac{1-e^{-G'(\lambda)+2\delta}}
{1-e^{-G'(\lambda)}}.
$$

The right side converges uniformly to $0$ on $I$ by (5.3). Choose
$\delta>0$ so small that

$$
e^{-\varepsilon}X(\lambda)\leq x_{\lambda,\delta}<X(\lambda)
\tag{5.5}
$$

for every $\lambda\in I$. The strict upper inequality follows separately
because $p_{\lambda,\delta}<1-e^{-G'(\lambda)}$ and $e^{-\delta}<1$.

Uniform continuity of $G,G'$ on $I$ gives a mesh width $h>0$ such that,
whenever $\lambda\leq\lambda_j\leq\lambda+h$,

$$
|G(\lambda_j)-G(\lambda)|\leq\varepsilon/2,\qquad
|G'(\lambda_j)-G'(\lambda)|\leq\delta.
\tag{5.6}
$$

Take a finite descending grid $\{\lambda_j\}$ covering $I$. At each grid
point, apply GNNW Theorem 12 with

$$
p=p_{\lambda_j,\delta},\quad
\mu=M(\lambda_j),\quad
x=x_{\lambda_j,\delta},\quad
y=Y(\lambda_j).
$$

Its strict $x$ hypothesis follows from the factor $e^{-\delta}$ in (5.4),
and its $\mathcal R_*$ hypothesis is assumed in the lemma and verified
separately for both witness regimes below. There are only finitely many grid
points, so the maximum of their thresholds $L_0$ is finite. No continuity of
$M$ or $Y$ is used here.

Let $k\geq\ell\geq\max(L_0,\rho k)$, put $r=\ell/k$, and select
$\lambda_j\in[r,r+h]$. A coloring with red density at least

$$
1-e^{-G'(r)+\delta}
$$

has red density at least $p_{\lambda_j,\delta}$ by (5.6). Moreover, using
(5.2), (5.5), $\lambda_jk\geq\ell$, and
$\log M+\log Y<0$,

$$
\begin{aligned}
N&\geq e^{(G(r)+\varepsilon)k}
\geq e^{(G(\lambda_j)+\varepsilon/2)k}\\
&\geq
\exp\!\left[-\frac12\left(k\log X(\lambda_j)
+\lambda_jk\log M(\lambda_j)
+\lambda_jk\log Y(\lambda_j)\right)+\frac{\varepsilon k}{2}\right]\\
&\geq (e^{-\varepsilon}X(\lambda_j))^{-k/2}
(M(\lambda_j)Y(\lambda_j))^{-\ell/2}\\
&\geq x_{\lambda_j,\delta}^{-k/2}
(M(\lambda_j)Y(\lambda_j))^{-\ell/2}.
\end{aligned}
$$

GNNW Theorem 12 therefore handles the high-red-density case.

For the complementary case, some vertex has blue degree at least
$e^{-G'(r)+\delta}N-1$. For large $k$ this is at least

$$
\exp\left(G(r)k+\varepsilon k-G'(r)+\delta/2\right).
$$

Induct on $\ell$. The induction hypothesis at $\ell-1$ is applicable because

$$
k\left(G(r)-G(r-1/k)\right)=G'(\xi)
$$

for some $\xi\in[r-1/k,r]$, and hence

$$
G'(r)-G'(\xi)\leq
\frac1k\sup_{t\in[\rho/2,1]}|G''(t)|\leq\delta/2
$$

for sufficiently large $k$. This is exactly the needed comparison. The
small-$\ell$ range is the induction base. The resulting epsilon statement is
uniform over $1\leq\ell\leq k$. $\square$

#### Verification of Lemma 5.1's interior condition

For the elementary prior and for the target on $(0,5\cdot10^{-3})$, we have
$Y=1-X$. Equation (5.5) gives $x_{\lambda,\delta}<X$, and the argument
leading to (4.1) proves
$(x_{\lambda,\delta},Y)\in\mathcal R_*$.

For the target on $[5\cdot10^{-3},1]$, the certificate proves both strict
envelopes (3.2)--(3.3). Lemma 2.1 gives
$(X,Y)\in\mathcal R_*$. Since $x_{\lambda,\delta}<X$, downward closure of
the interior (or a direct northeast-point argument) gives
$(x_{\lambda,\delta},Y)\in\mathcal R_*$. Thus GNNW Theorem 12 is applied
with its exact interior hypothesis in every regime.

### 6. Target witness and the small-lambda proof

On each of the 32,768 exact-decimal cells covering $[5\cdot10^{-3},1]$, the JSON
specifies constants $M,Y\in(0,1)$ and defines $X$ by (5.1) with $G=F$.
At a shared cell endpoint, either adjacent witness can be selected; the
checker proves both on their closed cells. Make the functions right-continuous
for definiteness.

On $(0,5\cdot10^{-3})$, set

$$
M(\lambda)=\lambda e^{-\lambda},\qquad Y(\lambda)=1-X(\lambda).
$$

The same analytic argument as in Section 4 proves $F>0$, $F'>0$, and (5.2)
throughout this whole open interval. The target normalized slack satisfies

$$
\frac{F+\frac12(\log X+\lambda\log M+\lambda\log Y)}{\lambda}
\geq0.00369567987777145\ldots>0.
$$

No limiting point is omitted. At $\lambda=5\cdot10^{-3}$, use the first JSON cell,
which is independently strict.

The piecewise $M,Y$ are discontinuous, but Lemma 5.1 does not require their
continuity. On every compact interval away from zero, the elementary part is
continuous and the large part has only finitely many values. The exact
certificate ranges are

```text
0.0076223064688733461 <= M <= 0.39254897298540486
0.017881628195265304 <= Y <= 0.81960502417040293
```

on $[5\cdot10^{-3},1]$, so $M$ is uniformly separated from $1$. The checker proves
$F'\geq0.7629833785113415$ there. On every compact subset of the elementary
regime, $F'$ has a positive minimum. Thus (5.3), and hence the uniform
$\delta$ needed by the finite-net proof, holds.

### 7. Why the Arb run proves continuous intervals

The checker does not test only cell midpoints.

1. The JSON endpoints form an exact-decimal partition: the first left
   endpoint is `0.005`, every right endpoint is textually/numerically equal to
   the next left endpoint, and the last right endpoint is `1`.
2. For each cell, `ball_interval(lo,hi)` constructs an Arb ball containing
   every real $\lambda\in[lo,hi]$.
3. `main_slack_over_lambda` evaluates the natural interval extension of every
   elementary operation. If dependency inflation prevents a strict sign, it
   bisects recursively. The completed run returned only after every resulting
   subinterval had strict positive slack.
4. `region_margins_over_lambda` does the same, while replacing the interval
   $a(\lambda)$ by its rigorous lower endpoint, the worst case for both
   envelopes. Its root brackets are justified by strict concavity as proved
   in Section 3.
5. The open interval $(0,5\cdot10^{-3}]$ is covered by the analytic coefficient
   proof in `prove_small_regime`, not by extrapolation from a positive cutoff.

The replayed strict outputs are:

```text
prior U'' worst certified upper bound: -0.40787039816230575
prior elementary small-regime slack/lambda: 0.00330349733874634...
prior elementary worst [0.005,1] slack: 3.1150059697914928e-08
target small-regime slack/lambda: 0.00369567987777145...
segments: 32768
min_F: 0.03022313226845907
min_F_prime: 0.7629834735848138
worst_standard_region_margin: 5.8529290109470086e-05
worst_swapped_region_margin: 6.074652597491317e-05
worst_large_main_slack: 4.942496275865115e-06
```

Every sign needed by Lemmas 2.1 and 5.1 is therefore strict.

### 8. Completion of the proof

Section 4 and Lemma 5.1 establish the prior rate (3.1). Sections 2--3 turn
that rate, together with the two certified envelopes, into the required
$\mathcal R_*$ points for the target large-regime witness. Section 6 supplies
the target small-regime witness. All hypotheses of Lemma 5.1 now hold with
$G=F$, proving

$$
R(k,\ell)\leq\exp(F(\ell/k)k+o(k))
$$

uniformly for $1\leq\ell\leq k$.

At $\lambda=1$,

$$
F(1)=2\log2+(-0.25+0.0299+0.08)e^{-1}
=\log4-0.1401e^{-1}.
$$

Therefore

$$
e^{F(1)}=4e^{-0.1401/e}
=3.7990629773286618741009363445941409697\ldots,
$$

and

$$
R(k,k)\leq
\left(3.799062977328661874100936344594\ldots\right)^{k+o(k)}.
\qquad\square
$$

## Corrections or missing assumptions

The Ramsey claim itself needs no weakening. The route requires these explicit
repairs to the printed source theorem:

1. replace $F'<0$ by $F'>0$;
2. actually prove the perturbed BookCor point lies in $\mathcal R_*$;
3. add compact-uniform separation of $M$ from $1$ (or an equivalent uniform
   perturbation hypothesis);
4. read the unsubscripted `p,mu` as $p_\lambda,M(\lambda)$;
5. read $F((\ell-1)k)$ as $F((\ell-1)/k)$ and use $\sup|F''|$.

These are candidate-specifically discharged above. They should not be used to
claim that the literal, arbitrary-witness version of GNNW Theorem 13 has been
proved.

## Open risks

* GNNW Lemma 11 is an explicitly imported published combinatorial dependency;
  the repaired Theorem 12 replay does not independently re-prove that earlier
  book lemma.
* Arb and `python-flint` are trusted numerical-proof infrastructure. A second
  independently structured checker now passes, but it uses the same Arb
  library; another ball library or formal proof assistant would further reduce
  software trust.
* This is an asymptotic result. It supplies no explicit finite threshold in
  $k$ and no improved bound for any specified finite Ramsey number.

## Exact reproduction

From `/Users/Jackal/iWorld/ireserch/Ramsey`:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r routes/upper/requirements-verify.txt
.venv/bin/python routes/upper/verify_arb.py \
  routes/upper/certificate-recommended-beta00299-split005.json
.venv/bin/python routes/upper/audit_tests.py
shasum -a 256 routes/upper/certificate-recommended-beta00299-split005.json \
  routes/upper/verify_arb.py routes/upper/audit_tests.py
```

The expected certificate hash is the value at the start of this document.
The expected verifier hash in this replay is
`5bcb2443d9ba02aed34455e1a1a511bc0ec32360d0c7a0f98e2832628b81f367`.
