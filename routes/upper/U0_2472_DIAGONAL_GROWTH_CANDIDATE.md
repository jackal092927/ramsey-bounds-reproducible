# The `u0=309/125` diagonal-growth sharpening

Date: 2026-08-12

## Claim

Let

$$
 u_0=\frac{309}{125}=2.472,\qquad L=u_0^3,\qquad a=e^{-u_0},
$$

$$
 E(z)=\sum_{n\ge0}\frac{z^n}{(3n)!},\qquad
 H(z)=1+aE(z)^2,\qquad G(z)=\frac{H(z)-H(-z)}2,
$$

and

$$F(x,y)=G(x)H(y)+G(y)H(x).$$

The following two pointwise estimates hold:

$$
 F(LA_1,LA_2)<-\frac{5001}{10000}
 \quad\text{if some }A_i<-1,                                      \tag{1}
$$

and, if $A_1,A_2\ge-1$ and $M=\max(A_1,A_2)$,

$$
 F(LA_1,LA_2)<\frac{89}{10^6}
 \exp\!\left(4u_0(M+1)^{1/3}\right).                            \tag{2}
$$

Together with the pinned Yang--Mao positive-moment and tail interface,
these imply

$$
 \mathcal G_2^{(3)}\!\left(
 \frac{833}{1250},\frac{3092197917}{312500000}
 \right).                                                        \tag{3}
$$

The complete retained-spine/P6 transfer then gives the conditional local
computer-assisted bound

$$
 R(k,k)\le(3.780685300)^{k+o(k)}.                                \tag{4}
$$

## Status and frozen gates

**AUTHOR AND GENUINELY NON-IMPORTING 512-BIT ARB CHECKERS PASS; independent
proof review is still required.**  This document and its checkers are not
canonical until the proof review also passes.

The pre-registered promotion gates are:

1. the exact ratio target must be $10001/5000$ and have positive endpoint
   and full-half-line margin;
2. the diagonal-growth prefactor must be exactly $89/10^6$;
3. every critical outer margin, including decimal rounding, must exceed
   $10^{-9}$;
4. the safe decimal must improve $3.780685320$ by at least $10^{-8}$;
5. the inner and outer programs must reconstruct the same exact $C$.

## 1. Exact constants: ratio target versus separator

Put

$$
 \sigma_0=\frac1{10000},\qquad
 T=2+2\sigma_0=\frac{10001}{5000}.                               \tag{5}
$$

The ratio target is $2+2\sigma_0$, not $1+2\sigma_0$.  The latter
quantity enters only after the direct separator identity, where

$$
 \sigma_* = \frac{1+2\sigma_0}{2}=\frac{5001}{10000}.             \tag{6}
$$

This distinction is asserted with exact rational arithmetic in both
checkers.

## 2. Ratio certificate on the full half-line

For $u\ge0$, the cubic root filters are

$$
 P(u)=E(u^3)=\frac{e^u+2e^{-u/2}\cos(\sqrt3u/2)}3,
$$

$$
 N(u)=E(-u^3)=\frac{e^{-u}+2e^{u/2}\cos(\sqrt3u/2)}3.             \tag{7}
$$

Their derivatives are

$$
 P'(u)=\frac{e^u-e^{-u/2}\cos(\sqrt3u/2)
 -\sqrt3e^{-u/2}\sin(\sqrt3u/2)}3,
$$

$$
 N'(u)=\frac{-e^{-u}+e^{u/2}\cos(\sqrt3u/2)
 -\sqrt3e^{u/2}\sin(\sqrt3u/2)}3.                                \tag{8}
$$

Define

$$
 R(u)=\frac{1+aP(u)^2}{1+aN(u)^2}.
$$

The sign of $R'(u)$ is the sign of

$$
 W(u)=P P'(1+aN^2)-NN'(1+aP^2).                                  \tag{9}
$$

At 512-bit precision, the author checker proves

$$
 R(u_0)-T>1.5259\cdot10^{-5},                                    \tag{10}
$$

and partitions $[u_0,2.9]$ into 32,768 exact rational cells.  Direct
outward-rounded evaluation of (7)--(9) gives $W>0$ on every cell; the
smallest lower endpoint is greater than $10.361$.

For the remaining half-line use

$$
 P(u)\ge\frac{e^u-2e^{-u/2}}3,
 \qquad |N(u)|\le\frac{2e^{u/2}+e^{-u}}3.                         \tag{11}
$$

With $T$ as in (5), expanding the desired envelope inequality gives

$$
 K(u)=aB_T(u)-9(T-1)>0,
$$

$$
 B_T(u)=e^{2u}-4Te^u-4e^{u/2}-4Te^{-u/2}
        +4e^{-u}-Te^{-2u}.                                       \tag{12}
$$

The checker proves $K(2.9)>0$.  It also proves at $u=2.9$ that

$$
 D(u)=2e^u(e^u-2T)-2e^{u/2}-4e^{-u}>0
$$

and

$$
 D'(u)=4e^{2u}-4Te^u-e^{u/2}+4e^{-u}>0.                           \tag{13}
$$

For $u\ge2.9$, the right side of (13) remains positive: its first two
terms have exponentially increasing dominance over $e^{u/2}$, while the
last term is positive.  Hence $D$ remains positive.  Direct
differentiation of (12), discarding only positive terms, gives
$B_T'(u)\ge D(u)>0$.  Thus $K$ remains positive on the complete tail.
The envelope ratio itself has certified slack greater than $0.3303$ at the
switch.  Consequently

$$R(u)>T\qquad(u\ge u_0).                                        \tag{14}$$

## 3. The direct bad-event separator

Suppose $x=-t$ with $t\ge L$, and abbreviate
$A=H(-t)$ and $R=H(t)/H(-t)$.  For every real $y$, direct substitution
gives the exact identity

$$
 F(-t,y)=\frac A2\big((2-R)H(y)-H(-y)\big).                       \tag{15}
$$

Since $A,H(y),H(-y)\ge1$ and (14) gives $R>2+2\sigma_0$,

$$
 F(-t,y)<-\frac{1+2\sigma_0}{2}=-\frac{5001}{10000}.             \tag{16}
$$

Swapping coordinates when necessary proves (1).

## 4. Reduction of good-event growth to one dimension

The power series for $H$ has nonnegative coefficients.  Thus $H$ is
nondecreasing on $[0,\infty)$, and the odd part $G$ is nonnegative and
nondecreasing there.  For $x=-v^3\in[-L,0]$, the root filter gives

$$
 |E(-v^3)|\le e^{v/2},\qquad
 H(x)\le1+e^{-u_0}e^v\le2.                                      \tag{17}
$$

For all $x,y\ge-L$, let $m=\max\{x,y,0\}$.  Then

$$F(x,y)\le F(m,m).                                               \tag{18}$$

Indeed, if both variables are negative then $F<0$.  If
$x<0\le y$, the negative summand may be discarded and (17) gives

$$F(x,y)\le G(y)H(x)\le2G(y)\le2G(y)H(y)=F(y,y).$$

If $0\le x\le y$, monotonicity of $G$ and $H$ bounds both summands by
$G(y)H(y)$.  These cases prove (18).

For $z\ge0$,

$$
 F(z,z)=H(z)^2-H(z)H(-z)
 \le H(z)^2-H(-z)^2.                                             \tag{19}
$$

The second inequality uses $H(z)\ge H(-z)>0$.  Consequently it is enough
to prove, for every $u\ge0$,

$$
 \frac{H(u^3)^2-H(-u^3)^2}
 {\exp\!\left(4(u^3+u_0^3)^{1/3}\right)}
 <\frac{89}{10^6}.                                               \tag{20}
$$

The checker covers $[0,20]$ using 65,536 exact rational cells and
outward-rounded root filters.  The smallest certified slack is greater
than $5.23\cdot10^{-6}$.

For $u\ge20$, put $w=(u^3+u_0^3)^{1/3}\ge u$.  The elementary root-filter
bound

$$
 |P(u)|\le\frac{e^u}{3}(1+2e^{-3u/2}),\qquad H(-u^3)^2\ge1
$$

gives

$$
 \frac{H(u^3)^2-H(-u^3)^2}{e^{4w}}
 \le \frac{2a}{9}e^{-2u}(1+2e^{-3u/2})^2
 +\frac{a^2}{81}(1+2e^{-3u/2})^4.                                \tag{21}
$$

Both terms decrease with $u$.  At $u=20$ the right side is less than
$8.797576716\cdot10^{-5}$, leaving more than $1.0242\cdot10^{-6}$
below $89/10^6$.  The limiting constant $a^2/81$ has essentially the
same certified slack.  Equations (18)--(21) prove (2).

## 5. Exact tail budget and correlation constant

Choose

$$
 D=\frac{89}{10^6},\quad \sigma_*=\frac{5001}{10000},\quad
 \beta=\frac{833}{1250},\quad
 \varepsilon=\frac{7113}{10^7}.                                 \tag{22}
$$

The pinned moment/tail contradiction requires

$$D\beta(1+2/\varepsilon)<\sigma_*(1-\beta).$$

Exact rational arithmetic gives margin

$$
 \sigma_*(1-\beta)-D\beta(1+2/\varepsilon)
 =\frac{89775619}{8891250000000}>10^{-5}.                         \tag{23}
$$

The resulting exact correlation constant is

$$
 C=4u_0(1+\varepsilon)
 =\frac{3092197917}{312500000}=9.8950333344.                       \tag{24}
$$

This proves (3), conditional only on the already pinned source-level
moment-positivity and tail interface.

## 6. Retained-spine/P6 certificate

The outer checker uses the exact tuple

$$
 \eta=0.02868925,\quad p=0.47130784,\quad
 \delta=0.000053934,
$$

$$
 \lambda_0=13235,\quad \tau=0.00069374,
 \quad\Delta=0.0000034727.                                      \tag{25}
$$

It reconstructs (24) rather than accepting a decimal approximation.  The
complete degree-14 rate-function concavity and ordered-wedge checks give:

| gate | certified lower margin |
|---|---:|
| degree slack $\tau(1/2-\eta-p)$ | $2.0187\cdot10^{-9}$ |
| red page | $8.1307\cdot10^{-9}$ |
| blue page | $3.4828\cdot10^{-6}$ |
| diagonal reservoir | $2.4849\cdot10^{-5}$ |

Outward-rounded evaluation yields

$$
 e^{U(1)-\Delta}<3.780685298588<3.780685300,                      \tag{26}
$$

with rounding margin greater than $1.4125\cdot10^{-9}$.  The safe decimal
improves $3.780685320$ by exactly $2\cdot10^{-8}$.  Hence the two numerical
promotion gates both pass, proving (4) conditional on the pinned theorem
chain once independent replay and proof review also pass.

## Reproduction

```text
.venv/bin/python routes/upper/check_u0_2472_diagonal_growth.py
.venv/bin/python routes/upper/check_retained_spine_u0_2472.py
.venv/bin/python routes/upper/independent_check_u0_2472_diagonal_growth.py
```

## Claim boundary

This is an asymptotic, local, computer-assisted sharpening conditional on
the pinned Yang--Mao theorem interface and the already audited
retained-spine/P6 transfer.  It gives no finite-$k$ threshold, no finite
Ramsey-number value, no global optimum, and no priority claim.  Until the
independent proof referee passes, (4) remains a candidate and must not
replace the canonical bound.
