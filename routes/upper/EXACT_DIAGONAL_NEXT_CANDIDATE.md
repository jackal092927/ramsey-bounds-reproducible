# Exact-diagonal next-round sharpening

Date: 2026-08-12

## Claim

Let

$$
 u_0=\frac{1235783}{500000}=2.471566,
 \qquad L=u_0^3,\qquad a=e^{-u_0},
$$

$$
 E(z)=\sum_{n\ge0}\frac{z^n}{(3n)!},\qquad
 H(z)=1+aE(z)^2,\qquad G(z)=\frac{H(z)-H(-z)}2,
$$

and

$$
F(x,y)=G(x)H(y)+G(y)H(x).
$$

Then

$$
 F(LA_1,LA_2)<-\frac{50000001}{100000000}
 \quad\text{if some }A_i<-1,                                    \tag{1}
$$

while, if $A_1,A_2\ge-1$ and $M=\max(A_1,A_2)$,

$$
 F(LA_1,LA_2)<\frac{88053}{10^9}
 \exp\!\left(4u_0(M+1)^{1/3}\right).                           \tag{2}
$$

Under the pinned Yang--Mao positive-moment and tail interface, these
estimates prove

$$
 \mathcal G_2^{(3)}\!\left(
 \frac{330867}{500000},
 \frac{12366348252219}{1250000000000}
 \right).                                                       \tag{3}
$$

The retained-spine/P6 transfer then gives the conditional local
computer-assisted candidate

$$
 R(k,k)\le(3.780685290)^{k+o(k)}.                               \tag{4}
$$

## Status

**AUTHOR 512-BIT ARB INNER AND OUTER CHECKERS AND A GENUINELY NON-IMPORTING
512-BIT REPLAY PASS; independent proof review is still required.**  This
package is not canonical.

The candidate is the sole high-precision freeze allowed by
`EXACT_DIAGONAL_NEXT_PROTOCOL.md`; the search will not be reopened in this
round.

## 1. Ratio target and direct separator

Fix

$$
 \sigma_0=\frac1{10^8},\qquad
 T=2+2\sigma_0=\frac{100000001}{50000000},                       \tag{5}
$$

and therefore

$$
 \sigma_* = \frac{1+2\sigma_0}{2}
 =\frac{50000001}{100000000}.                                   \tag{6}
$$

For $u\ge0$, the cubic filters and their derivatives are

$$
 P(u)=\frac{e^u+2e^{-u/2}\cos(\sqrt3u/2)}3,
 \qquad
 N(u)=\frac{e^{-u}+2e^{u/2}\cos(\sqrt3u/2)}3,                   \tag{7}
$$

$$
 P'(u)=\frac{e^u-e^{-u/2}\cos(\sqrt3u/2)
 -\sqrt3e^{-u/2}\sin(\sqrt3u/2)}3,
$$

$$
 N'(u)=\frac{-e^{-u}+e^{u/2}\cos(\sqrt3u/2)
 -\sqrt3e^{u/2}\sin(\sqrt3u/2)}3.                              \tag{8}
$$

With

$$
 R(u)=\frac{1+aP(u)^2}{1+aN(u)^2},
$$

the sign of $R'$ is the sign of

$$
 W(u)=PP'(1+aN^2)-NN'(1+aP^2).                                 \tag{9}
$$

The author checker proves

$$
R(u_0)-T>2.6595\cdot10^{-7}.                                   \tag{10}
$$

and proves $W>0$ on 65,536 exact rational cells covering
$[u_0,2.9]$.  On $[2.9,\infty)$ it uses the analytic filter envelopes

$$
 P(u)\ge\frac{e^u-2e^{-u/2}}3,
 \qquad |N(u)|\le\frac{2e^{u/2}+e^{-u}}3,                       \tag{11}
$$

and the same expanded monotone tail polynomial

$$
 B_T(u)=e^{2u}-4Te^u-4e^{u/2}-4Te^{-u/2}
        +4e^{-u}-Te^{-2u}.                                      \tag{12}
$$

At $2.9$, the checker proves $aB_T-9(T-1)>0$, as well as positivity
of

$$
 D(u)=2e^u(e^u-2T)-2e^{u/2}-4e^{-u}
$$

and its lower derivative gate

$$
D'(u)=4e^{2u}-4Te^u-e^{u/2}+4e^{-u}.                            \tag{13}
$$

The exponential dominance in (13) persists for $u\ge2.9$, while direct
differentiation gives $B_T'(u)\ge D(u)$.  Thus $R(u)>T$ on the complete
half-line $u\ge u_0$.

If $x=-t$ with $t\ge L$, put $A=H(-t)$ and
$R=H(t)/H(-t)$.  The exact identity

$$
 F(-t,y)=\frac A2\big((2-R)H(y)-H(-y)\big)                       \tag{14}
$$

and $A,H(y),H(-y)\ge1$ give

$$
 F(-t,y)<-\frac{1+2\sigma_0}{2}=-\sigma_*.
$$

Swapping coordinates proves (1).

## 2. Full two-dimensional reduction

The series of $H$ has nonnegative coefficients.  Hence $H$ is
nondecreasing on $[0,\infty)$, and its odd part $G$ is nonnegative and
nondecreasing there.  For $x=-v^3\in[-L,0]$,

$$
 |E(-v^3)|\le e^{v/2},\qquad H(x)\le1+e^{-u_0}e^v\le2.           \tag{15}
$$

For $x,y\ge-L$, set $m=\max\{x,y,0\}$.  Then

$$
F(x,y)\le F(m,m).                                               \tag{16}
$$

To verify every sign region, suppose by symmetry that $x\le y$.

1. If $y<0$, both $G(x)$ and $G(y)$ are negative while both $H$ factors
   are positive, so $F(x,y)<0=F(0,0)$.
2. If $x<0\le y$, discard the nonpositive term $G(x)H(y)$ and use (15):

   $$
   F(x,y)\le G(y)H(x)\le2G(y)\le2G(y)H(y)=F(y,y).
   $$

3. If $0\le x\le y$, monotonicity bounds each summand by $G(y)H(y)$,
   again giving $F(x,y)\le F(y,y)$.

This proves (16), including all boundary cases.

## 3. Exact diagonal, compact interval, and asymptotic tail

Unlike the preceding candidate, this proof retains the exact identity

$$
 F(z,z)=2G(z)H(z)=H(z)^2-H(z)H(-z),\qquad z\ge0.                 \tag{17}
$$

Put $z=u^3$ and $w=(u^3+u_0^3)^{1/3}$.  By (16), it is enough to prove

$$
 \frac{H(u^3)^2-H(u^3)H(-u^3)}{e^{4w}}
 <\frac{88053}{10^9},\qquad u\ge0.                              \tag{18}
$$

The author checker verifies (18) directly on 131,072 exact rational
cells covering $[0,20]$.  It evaluates (17), not the larger
$H(u^3)^2-H(-u^3)^2$.  The smallest compact slack is greater than
$4.2687\cdot10^{-6}$.

For $u\ge20$, use $H(-u^3)\ge1$ to obtain

$$
 H(u^3)^2-H(u^3)H(-u^3)
 \le H(u^3)^2-H(u^3).                                           \tag{19}
$$

Writing $H(u^3)=1+aP(u)^2$, the right side of (19) is exactly

$$
aP(u)^2+a^2P(u)^4.                                              \tag{20}
$$

The filter estimate

$$
|P(u)|\le\frac{e^u}{3}(1+2e^{-3u/2}).
$$

and $w\ge u$ give

$$
 \frac{F(u^3,u^3)}{e^{4w}}
 \le \frac a9e^{-2u}(1+2e^{-3u/2})^2
 +\frac{a^2}{81}(1+2e^{-3u/2})^4.                               \tag{21}
$$

Both terms decrease.  At $u=20$, the right side of (21) is less than
$8.805216326983\cdot10^{-5}$, leaving a certified slack greater than
$8.3673\cdot10^{-10}$.  Its asymptotic constant is

$$
 D_\infty=\frac{a^2}{81},                                       \tag{22}
$$

with essentially the same strict slack.  This validates the method
diagnostic in the protocol: the exact diagonal substantially improves the
compact expression but does not remove the asymptotic floor.

The protocol's $10^{-9}$ critical-margin gate applies to the **outer**
degree/page/reservoir/rounding inequalities, while the inner analytic tail
was required there to be proved strictly positive.  The author checker,
written before this final candidate document, independently imposes a
$10^{-10}$ inner proof margin; the exploratory search used a
$2\cdot10^{-10}$ asymptotic allowance.  Both tail and asymptotic slacks
exceed the checker threshold.  The separate exact expectation-tail budget
has its own, stronger $10^{-5}$ protocol gate below.

Equations (16)--(21) prove (2).

## 4. Exact expectation-tail budget and handoff

Choose

$$
 D=\frac{88053}{10^9},\quad
 \beta=\frac{330867}{500000},\quad
 \varepsilon=\frac{6893}{10^7}.                                \tag{23}
$$

Exact rational arithmetic gives

$$
 \sigma_*(1-\beta)-D\beta(1+2/\varepsilon)
 =\frac{39437634699447}{3446500000000000000}
 >10^{-5}.                                                       \tag{24}
$$

Therefore the pinned moment/tail contradiction proves (3), with exact
correlation constant

$$
 C=4u_0(1+\varepsilon)
 =\frac{12366348252219}{1250000000000}
 =9.8930786017752.                                               \tag{25}
$$

Both the inner and outer checkers construct the rational number in (25)
from $(u_0,\varepsilon)$ and assert exact equality.

## 5. Retained-spine/P6 certificate

The sole frozen outer tuple is

$$
 \eta=0.02868896,\quad p=0.47130887,\quad
 \delta=0.000053863,
$$

$$
 \lambda_0=13233,\quad \tau=0.00069386,
 \quad\Delta=0.0000034754.                                     \tag{26}
$$

The full degree-14 rate concavity and ordered-wedge checker certifies:

| gate | certified lower margin |
|---|---:|
| degree slack | $1.5056\cdot10^{-9}$ |
| red page | $5.1006\cdot10^{-9}$ |
| blue page | $3.4825\cdot10^{-6}$ |
| diagonal reservoir | $6.0468\cdot10^{-6}$ |

It also gives

$$
 e^{U(1)-\Delta}<3.780685288380<3.780685290,                     \tag{27}
$$

with rounding margin greater than $1.6203\cdot10^{-9}$.  Relative to the
previous actual candidate base $3.7806852985874904\ldots$, the certified
improvement is greater than $1.020785\cdot10^{-8}$.  The safe decimal
improves $3.780685300$ by exactly $10^{-8}$.  Thus every frozen protocol
gate passes at the author-checker stage.

## Reproduction

```text
.venv/bin/python routes/upper/check_exact_diagonal_next.py
.venv/bin/python routes/upper/check_retained_spine_exact_diagonal_next.py
.venv/bin/python routes/upper/independent_check_exact_diagonal_next.py
```

## Claim boundary

This is an asymptotic, local, computer-assisted candidate conditional on
the pinned Yang--Mao theorem interface and the already audited
retained-spine/P6 transfer.  It supplies no finite-$k$ threshold, finite
Ramsey-number value, global optimum, or priority claim.  Until the
independent proof referee passes, (4) must not replace the canonical result.
