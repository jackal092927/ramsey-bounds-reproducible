# Strong bad-event separator and direct good-event growth

Date: 2026-08-12

## Claim

For the functions in `HYBRID_CORRELATION_SHARPENING.md`, retain the exact
constants

$$
 u_0=619/250,quad L=u_0^3,quad a=e^{-u_0},quad
 c=4u_0,quad \sigma_0=1/1000,
$$

and put

$$
 \sigma_*=\frac{501}{1000},\qquad D_*=\frac{11}{1000}.
$$

Then

$$
 F(LA_1,LA_2)<-\sigma_*
 \quad\hbox{if some }A_i<-1,
 \tag{1}
$$

while, for $A_1,A_2\ge-1$ and $M=\max(A_1,A_2)$,

$$
 F(LA_1,LA_2)
 \le D_*\exp\!\left(c(M+1)^{1/3}\right).
 \tag{2}
$$

Consequently the same positive-moment/tail argument proves

$$
 \mathcal G_2^{(3)}\!\left(\frac{11}{250},
 \frac{62025657}{6250000}\right).
 \tag{3}
$$

## Status and pre-registered gates

**AUTHOR 384-BIT ARB CHECKER PASS; pending a non-importing replay and proof
referee.**  Promotion requires all interval cells to resolve strictly, at
least $10^{-5}$ slack in the exact tail budget, and downstream critical
margins at least $10^{-9}$.

This is a source-level strengthening: it changes the pointwise separator
and growth lemmas, rather than merely tuning floating-point parameters.

## Proof

Write $H=1+aE^2$, $G=(H-H\circ(-\mathrm{id}))/2$, and

$$F(x,y)=G(x)H(y)+G(y)H(x).$$

### 1. Exact bad-event identity

Suppose first that $x=-u$ with $u\ge L$, and set
$A=H(-u)$ and $R=H(u)/H(-u)$.  Direct substitution gives, for every real
$y$,

$$
 F(-u,y)=\frac A2\bigl((2-R)H(y)-H(-y)\bigr).
 \tag{4}
$$

The already certified hybrid ratio lemma gives
$R>2+2\sigma_0$.  Since $A,H(y),H(-y)\ge1$, (4) implies

$$
 F(-u,y)<-\frac{1+2\sigma_0}{2}=-\sigma_*.
$$

This applies after swapping the two coordinates if necessary, proving (1),
including the case when both coordinates are bad.  Notice that the old
factorized proof discarded the additional $-H(-y)/2$ in (4); retaining it
raises the usable negative credit from $0.001$ to $0.501$.

### 2. A sharper one-variable envelope

For $A\ge-1$ put

$$w(A)=u_0(A+1)^{1/3}.$$

We claim

$$H(LA)\le\frac{113}{100}e^{2w(A)}.\tag{5}$$

If $A\ge0$, write $LA=u^3$ and
$w=(u^3+u_0^3)^{1/3}\ge u$.  The standard positive-axis bound gives

$$H(LA)\le1+ae^{2u}\le(1+a)e^{2w}<\frac{113}{100}e^{2w}.$$

If $-1\le A\le0$, write $LA=-v^3$, $0\le v\le u_0$.  The companion
checker partitions this exact interval into 16,384 rational cells and,
with outward-rounded 384-bit Arb arithmetic, proves directly that

$$1+aE(-v^3)^2<\frac{113}{100}
 \exp\!\left(2(u_0^3-v^3)^{1/3}\right).$$

The worst point is the $v=u_0$ endpoint, where the certified slack remains
larger than $0.0049$.  This proves (5).

### 3. Direct control of the positive part of $F$

For $x\ge0$, coefficient positivity implies

$$0\le G(x)=\frac a2(E(x)^2-E(-x)^2)\le\frac a2E(x)^2.\tag{6}$$

If $x=u^3\ge0$ and $w=(u^3+u_0^3)^{1/3}$, then

$$E(u^3)\le\frac{e^w}{3}.\tag{7}$$

Indeed, the root filter reduces (7) to

$$e^u+2e^{-u/2}\cos(\sqrt3u/2)\le e^w.$$

On $0\le u\le20$, the checker proves this directly on 65,536 rational
Arb cells.  For $u\ge20$, it uses the stronger elementary inequality

$$e^u+2e^{-u/2}\le e^w.$$

Writing $q=u_0^3/u^3\le u_0^3/20^3<1$, concavity of
$(1+q)^{1/3}$ gives

$$w-u=u\bigl((1+q)^{1/3}-1\bigr)
 \ge \frac{u_0^3}{3u^2(1+q)^{2/3}},$$

and the checker verifies at $u=20$ the stronger fact that this lower bound
exceeds $2e^{-3u/2}$.  The left lower bound decreases only polynomially,
whereas $\log(1+2e^{-3u/2})\le2e^{-3u/2}$ and this majorant decreases
exponentially; differentiating their logarithms proves the inequality for
the whole half-line.  Thus (7) holds.

Terms of $F$ whose $G$-coordinate is negative are nonpositive and may be
discarded.  Applying (5)--(7) to every remaining term, and writing
$w_i=w(A_i)\le w(M)$, gives

$$
 F(LA_1,LA_2)
 \le2\cdot\frac a{18}e^{2w(M)}
 \cdot\frac{113}{100}e^{2w(M)}
 =\frac{113a}{900}e^{4w(M)}.
$$

The checker proves $113a/900<11/1000$, establishing (2).

### 4. Exact tail budget

Repeat the master expectation argument, replacing its old constants by
$\sigma_*,D_*$.  Under failure of (3), the same union-bound tail integration
with $\varepsilon=203/100000$ gives

$$D_*\,\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
 <D_*\beta(1+2/\varepsilon),$$

whereas (1) and moment positivity give the strict lower bound
$\sigma_*(1-\beta)$.  For $\beta=11/250$ the exact rational inequality

$$
 \frac{11}{1000}\frac{11}{250}
 \left(1+\frac{2}{203/100000}\right)
 <\frac{501}{1000}\left(1-\frac{11}{250}\right)
$$

holds with margin greater than $10^{-5}$.  The contradiction proves (3).

## Claim boundary

This note changes only the parameterized correlation property.  It imports
the exact ratio proof, Yang--Mao's tensor-moment positivity, and their
parameterized tail interface.  It makes no finite-$k$, unconditional,
optimality, or priority claim.

## Reproduction

```text
.venv/bin/python routes/upper/check_strong_separator_growth.py
```
