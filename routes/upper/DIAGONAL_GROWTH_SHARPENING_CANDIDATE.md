# Diagonal-envelope sharpening of good-event growth

Date: 2026-08-12

## Claim

For the cubic root-filter functions already fixed in
`STRONG_SEPARATOR_GROWTH_SHARPENING.md`, let

$$
 u_0=\frac{619}{250},\qquad L=u_0^3,\qquad a=e^{-u_0},
$$

$$
 E(z)=\sum_{n\ge0}\frac{z^n}{(3n)!},\qquad
 H(z)=1+aE(z)^2,\qquad
 G(z)=\frac{H(z)-H(-z)}2,
$$

and

$$F(x,y)=G(x)H(y)+G(y)H(x).$$

If $A_1,A_2\ge-1$, $M=\max(A_1,A_2)$, and
$w(M)=u_0(M+1)^{1/3}$, then

$$
 F(LA_1,LA_2)<10^{-4}e^{4w(M)}. \tag{1}
$$

Together with the already certified pointwise bad-event separator
$F< -501/1000$, this proves the parameterized correlation property

$$
 \mathcal G_2^{(3)}\!\left(
 \frac{3253}{5000},
 4\frac{619}{250}\left(1+\frac{93}{125000}\right)
 \right). \tag{2}
$$

## Status

**AUTHOR AND NON-IMPORTING 512-BIT ARB CHECKERS PASS; pending an independent
proof referee.**  This is a candidate proof package, not a canonical result.

## Proof of the two-variable reduction

The power series for $H$ has nonnegative coefficients.  Therefore $H$ is
nondecreasing on $[0,\infty)$, while $G$ is odd, nonnegative, and
nondecreasing on $[0,\infty)$.  These facts follow term by term from the
power series (the odd coefficients of $G$ are nonnegative).

We also need a negative-axis bound.  If $x=-v^3\in[-L,0]$, the root filter
gives

$$
 |E(-v^3)|\le\frac{e^{-v}+2e^{v/2}}3\le e^{v/2}.
$$

Since $0\le v\le u_0$ and $a=e^{-u_0}$, this proves
$H(x)\le1+ae^v\le2$.

We prove

$$F(x,y)\le F(m,m),\qquad m=\max\{x,y,0\}, \tag{3}$$

for $x,y\ge-L$.  By symmetry suppose $x\le y$.

1. If $y<0$, then $G(x),G(y)<0$ and $H(x),H(y)>0$.  Hence
   $F(x,y)<0=F(0,0)$.
2. If $x<0\le y$, then the first summand is nonpositive and
   
   $$F(x,y)\le G(y)H(x)\le2G(y)\le2G(y)H(y)=F(y,y).$$
   
   The middle inequalities use the negative-axis bound $H(x)\le2$ and the
   universal lower bound $H(y)\ge1$.
3. If $0\le x\le y$, then both $G$ and $H$ are nondecreasing on the
   positive axis.  Bounding both summands by $G(y)H(y)$ yields
   $F(x,y)\le2G(y)H(y)=F(y,y)$.

This proves (3).  The boundary cases $x=0$ or $x=y$ are included by the same
weak inequalities.

If $M<0$, equation (3) already gives $F(LA_1,LA_2)\le0$, which proves (1).
If $M\ge0$, put $u=u_0M^{1/3}$; then $LM=u^3$ and
$(u^3+u_0^3)^{1/3}=u_0(M+1)^{1/3}=w(M)$.  It remains only to bound the
nonnegative diagonal at $z=u^3$.

For $z\ge0$, direct substitution gives the exact identity

$$
 F(z,z)=2G(z)H(z)=H(z)^2-H(z)H(-z). \tag{4}
$$

It is important that (4) is **not** $H(z)^2-H(-z)^2$.  However,
$H(z)\ge H(-z)>0$, so

$$
 F(z,z)\le H(z)^2-H(-z)^2. \tag{5}
$$

Thus it suffices to certify the stronger one-dimensional envelope

$$
 H(u^3)^2-H(-u^3)^2
 <10^{-4}\exp\!\left(4(u^3+u_0^3)^{1/3}\right),
 \qquad u\ge0. \tag{6}
$$

The 512-bit checker verifies (6) on 65,536 exact rational cells covering
$0\le u\le20$.  The least certified slack after normalization by the
exponential is greater than $1.69\cdot10^{-5}$.

For completeness, the half-line certificate is analytic.  The root filters
give, for $u\ge20$,

$$
 |E(u^3)|\le\frac{e^u}{3}(1+2e^{-3u/2}),
 \qquad H(-u^3)^2\ge1,
$$

and $w=(u^3+u_0^3)^{1/3}\ge u$.  Hence

$$
 \frac{H(u^3)^2-H(-u^3)^2}{e^{4w}}
 \le \frac{2a}{9}e^{-2u}(1+2e^{-3u/2})^2
 +\frac{a^2}{81}(1+2e^{-3u/2})^4. \tag{7}
$$

Both terms on the right decrease with $u$, and their value at $u=20$ is
less than $8.728\cdot10^{-5}$.  The certified tail slack exceeds
$1.27\cdot10^{-5}$.  Equations (3), (5), and (6) prove (1).

## Exact expectation-tail budget

Use

$$
 \sigma=\frac{501}{1000},\quad D=\frac1{10000},\quad
 \beta=\frac{3253}{5000},\quad
 \varepsilon=\frac{93}{125000}.
$$

The same master expectation and union-bound integration from the pinned
Yang--Mao interface needs

$$D\beta(1+2/\varepsilon)<\sigma(1-\beta).$$

Here the two sides are exact rationals, and their difference is

$$
 \sigma(1-\beta)-D\beta(1+2/\varepsilon)
 =\frac{427181}{4650000000}>10^{-5}. \tag{8}
$$

This proves (2), conditional on the same source-level moment-positivity and
tail interface already pinned and reviewed by the strong-separator package.

## Downstream retained-spine candidate

The exact tuple

$$
 \eta=0.0286892,\quad p=0.4713079,\quad
 \delta=0.00005393,
$$

$$
 \lambda_0=13236,\quad \tau=0.00069255,\quad
 \Delta=0.000003469
$$

passes the complete retained-spine/P6 wedge checker.  Its smallest critical
outer margins are

$$
 \tau(1/2-\eta-p)>2.008\cdot10^{-9},\qquad
 U(1)-\Delta-P_R>3.727\cdot10^{-9}.
$$

The blue-page and reservoir margins are respectively greater than
$3.47\cdot10^{-6}$ and $3.21\cdot10^{-5}$.  Outward-rounded evaluation gives

$$
 \exp(U(1)-\Delta)<3.780685312577<3.780685320. \tag{9}
$$

Thus, conditional on all pinned upstream theorems,

$$
 R(k,k)\le (3.780685320)^{k+o(k)}. \tag{10}
$$

The safe decimal improves the preceding strong-growth candidate
$3.780685405$ by $8.5\cdot10^{-8}$, meeting the pre-registered
$5\cdot10^{-8}$ improvement gate.  No canonical document should be updated
until independent replay and proof review both pass.

## Reproduction

```text
.venv/bin/python routes/upper/check_diagonal_growth.py
.venv/bin/python routes/upper/check_retained_spine_diagonal_growth.py
.venv/bin/python routes/upper/independent_check_diagonal_growth.py
```

## Claim boundary

The result is asymptotic and conditional on the pinned source theorem chain.
It supplies no finite-$k$ threshold, global optimality theorem, unconditional
Ramsey-number improvement, or priority claim.
