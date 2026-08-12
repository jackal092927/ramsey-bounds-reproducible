# Hybrid exact/envelope two-colour correlation lemma

Date: 2026-08-12

Primary source: Yang--Mao, *New upper bound for multicolor Ramsey
numbers*, [arXiv:2608.01962v1](https://arxiv.org/abs/2608.01962v1).
The pinned source snapshot used by the upstream audit is `main.tex`, SHA-256
`155b7104ec5b6935a576ae9f2b161976a966b0b46bd2b69153c0934ca688da2a`.

## Claim

In Yang--Mao's notation,

$$
\mathcal G_2^{(3)}\!\left(\frac1{4000000},
\frac{6202999}{625000}\right)
\tag{1}
$$

holds.  Thus the exact parameters are

$$
\beta=\frac1{4000000},\qquad
C=\frac{6202999}{625000}=9.9247984.
\tag{2}
$$

## Status

**PROVABLE AS STATED; AUTHOR ARB CHECKER PASS; pending independent replay.**

This is a source-level tightening of the specialized correlation argument,
not merely a floating-point parameter search.  The new ingredient is a
hybrid separator proof: the exact cubic root-filter ratio is certified on a
finite interval, while a monotone analytic envelope covers the remaining
half-line.

## Assumptions and dependency boundary

The proof imports only the following mathematical steps from the pinned
Yang--Mao source.

1. The coefficient-positivity tensor-moment lemma used in their Lemma 2.2.
2. The definition of $\mathcal G_2^{(3)}(\beta,C)$ and the union-bound tail
   integration in their Theorem 3.4.
3. No printed choice of $\beta$ or $C$, and no printed negative-tail
   normalization, is imported.

The exact root-filter interval lemma below is checked with `python-flint`
`0.9.0` at 384-bit precision using outward-rounded Arb intervals.

## Notation and exact constants

Put

$$
u_0=\frac{619}{250}=2.476,\qquad
a=e^{-u_0},\qquad L=u_0^3,
\tag{3}
$$

and define

$$
E(z)=\sum_{n\ge0}\frac{z^n}{(3n)!},\qquad
H(z)=1+aE(z)^2,\qquad
G(z)=\frac{H(z)-H(-z)}2.
\tag{4}
$$

For two coordinates let

$$
F(x_1,x_2)=G(x_1)H(x_2)+G(x_2)H(x_1).
\tag{5}
$$

The remaining constants are

$$
\sigma=\frac1{1000},\qquad
T=2+2\sigma=\frac{1001}{500},\qquad
c=4u_0=\frac{1238}{125},
\tag{6}
$$

and

$$
\varepsilon=\frac{21}{10000},\qquad
C=(1+\varepsilon)c=\frac{6202999}{625000}.
\tag{7}
$$

## Proof strategy and dependency map

1. Prove $H(u^3)/H(-u^3)>T$ for every $u\ge u_0$.
2. On $[u_0,2.9]$, use the exact root filters and a cellwise Arb proof that
   the ratio is strictly increasing.
3. On $[2.9,\infty)$, use elementary upper/lower root-filter envelopes and
   an analytic monotonicity argument.
4. Convert the ratio into the separator $F<-\sigma$ whenever one coordinate
   is below $-1$.
5. Re-run Yang--Mao's positive-moment and tail-integration contradiction
   with the exact generalized separator budget.

## Proof

### Step 1: signs and coefficient positivity

The Taylor coefficients of $E$, hence of $H$, are nonnegative.  The odd
part $G$ has nonnegative coefficients, so every multivariate Taylor
coefficient of $F$ is nonnegative.  For $x\ge0$,

$$
0\le \frac{G(x)}{H(x)}
=\frac12\left(1-\frac{H(-x)}{H(x)}\right)\le\frac12,
\tag{8}
$$

where coefficient positivity gives $|E(-x)|\le E(x)$.  For $x<0$ the same
ratio is nonpositive because $G$ is odd and $H>0$.

### Step 2: exact finite-interval ratio

Write $s=\sqrt3$ and, for $u\ge0$,

$$
P(u)=E(u^3)
=\frac{e^u+2e^{-u/2}\cos(su/2)}3,
\qquad
N(u)=E(-u^3)
=\frac{e^{-u}+2e^{u/2}\cos(su/2)}3.
\tag{9}
$$

Their exact derivatives are

$$
P'(u)=\frac{e^u-e^{-u/2}\cos(su/2)
-s e^{-u/2}\sin(su/2)}3,
\tag{10}
$$

$$
N'(u)=\frac{-e^{-u}+e^{u/2}\cos(su/2)
-s e^{u/2}\sin(su/2)}3.
\tag{11}
$$

Set

$$
R(u)=\frac{1+aP(u)^2}{1+aN(u)^2}.
\tag{12}
$$

The denominator is at least one, and the sign of $R'(u)$ is the sign of

$$
W(u)=P(u)P'(u)(1+aN(u)^2)
-N(u)N'(u)(1+aP(u)^2).
\tag{13}
$$

The companion checker partitions the exact rational interval
$[619/250,29/10]$ into $4096$ equal rational cells.  On every cell it
evaluates (9)--(13) directly with 384-bit outward-rounded Arb arithmetic and
proves that the lower endpoint of the enclosure of $W$ is positive.  It
also directly proves

$$
R(u_0)-T>0.
\tag{14}
$$

This is an exhaustive interval proof, not a sampling assertion.  Therefore
$R$ is strictly increasing on the full interval and

$$
\frac{H(u^3)}{H(-u^3)}=R(u)>T
\qquad (u_0\le u\le2.9).
\tag{15}
$$

### Step 3: analytic half-line envelope

For $u\ge0$, (9) gives

$$
P(u)\ge\frac{e^u-2e^{-u/2}}3,
\qquad
|N(u)|\le\frac{2e^{u/2}+e^{-u}}3.
\tag{16}
$$

For $u\ge2.9$ the first lower-bound base is positive.  Define

$$
\begin{aligned}
B_T(u)={}&e^{2u}-4T e^u-4e^{u/2}-4T e^{-u/2}
 +4e^{-u}-T e^{-2u},\\
K(u)={}&aB_T(u)-9(T-1).
\end{aligned}
\tag{17}
$$

The checker proves $K(2.9)>0$ and

$$
D(2.9)>0,
\qquad
D(u)=2e^u(e^u-2T)-2e^{u/2}-4e^{-u}.
\tag{18}
$$

For $u\ge2.9$, we have $e^u>18$ and

$$
D'(u)=4e^{2u}-4Te^u-e^{u/2}+4e^{-u}>0,
\tag{19}
$$

because $4e^u-4T>72-8.008>63$ and hence the first two
terms in (19) already dominate $e^{u/2}$.  Thus $D(u)>0$ throughout the
half-line.  Direct differentiation of (17), followed only by deleting
positive terms, gives $B_T'(u)\ge D(u)>0$.  Hence $K$ is increasing and
$K(u)>0$ for every $u\ge2.9$.

After expanding squares, $K(u)>0$ is exactly

$$
1+\frac a9(e^u-2e^{-u/2})^2
>T\left[1+\frac a9(2e^{u/2}+e^{-u})^2\right].
\tag{20}
$$

Equations (16) and (20) imply

$$
\frac{H(u^3)}{H(-u^3)}>T
\qquad (u\ge2.9).
\tag{21}
$$

Combining (15) and (21) covers every $u\ge u_0$.

### Step 4: separator and growth envelope

For $y=u^3\ge L$, the ratio just proved yields

$$
\frac{G(-y)}{H(-y)}
=-\frac12\left(\frac{H(y)}{H(-y)}-1\right)
<-\frac12-\sigma.
\tag{22}
$$

For $-1\le A\le0$, write $LA=-v^3$ with $0\le v\le u_0$.
The root-filter formula gives $|E(-v^3)|\le e^{v/2}$, and hence

$$
a|E(-v^3)|^2\le e^{-u_0}e^v\le1.
\tag{23}
$$

For $A\ge0$, coefficient positivity gives
$E(LA)\le e^{u_0A^{1/3}}$.  Consequently, for every $A\ge-1$,

$$
H(LA)\le2\exp\!\left(2u_0(A+1)^{1/3}\right).
\tag{24}
$$

Let $A_1,A_2\ge-1$ and $M=\max(A_1,A_2)$.  Using (8) and (24),

$$
F(LA_1,LA_2)
\le4\exp\!\left(4u_0(M+1)^{1/3}\right)
=D_2e^{c(M+1)^{1/3}},
\quad D_2=4.
\tag{25}
$$

If instead some $A_i<-1$, then (8) and (22) make the sum of the two
ratios $G/H$ strictly smaller than $-\sigma$.  Since $H\ge1$,

$$
F(LA_1,LA_2)<-\sigma.
\tag{26}
$$

### Step 5: moment and tail contradiction

Let $Z_1,Z_2$ be the two inner products in the definition of
$\mathcal G_2^{(3)}$, and put

$$
\mathcal E=\{Z_1,Z_2\ge-1\},
\qquad
Y=((\max(Z_1,Z_2)+1)_+)^{1/3}.
\tag{27}
$$

Coefficient positivity and Yang--Mao's tensor-moment lemma give
$\mathbb EF(LZ_1,LZ_2)\ge0$.  Suppose the conclusion of
$\mathcal G_2^{(3)}(\beta,C)$ failed for both coordinates and every
threshold.  Failure at threshold $-1$ implies
$\mathbb P(\mathcal E)<\beta<1$.  Equations (25)--(26) then imply the
strict lower bound

$$
D_2\,\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
>\sigma(1-\mathbb P(\mathcal E))
>\sigma(1-\beta).
\tag{28}
$$

The union-bound tail integration in Yang--Mao's Theorem 3.4 gives, under
the same failure assumption,

$$
\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
<\beta\left(1+\frac2\varepsilon\right).
\tag{29}
$$

The exact rational constants satisfy

$$
D_2\beta\left(1+\frac2\varepsilon\right)
=\frac{20021}{21000000}
<\frac{3999999}{4000000000}
=\sigma(1-\beta).
\tag{30}
$$

Equations (28)--(30) contradict one another.  This proves (1). $\square$

## Claim boundary and open risks

- This file proves only the parameterized correlation property (1).  A new
  Ramsey base requires a separate complete-square retained-spine enclosure.
- It does not alter the Yang--Mao regularization/book construction or the
  frozen local off-diagonal rate.
- The finite-interval step relies on Arb containment semantics and the
  pinned `python-flint` version; it is not a formal proof-assistant theorem.
- No optimality, publication-priority, or finite-$k$ claim is made.

## Reproduction

```text
.venv/bin/python routes/upper/check_hybrid_correlation.py
```

