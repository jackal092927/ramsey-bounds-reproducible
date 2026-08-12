# A specialized two-colour correlation constant

Date: 2026-08-12

Primary source: Yang--Mao, *New upper bound for multicolor Ramsey
numbers*, [arXiv:2608.01962v1](https://arxiv.org/abs/2608.01962v1).
The source snapshot used by the retained-spine audit is `main.tex`, SHA-256
`155b7104ec5b6935a576ae9f2b161976a966b0b46bd2b69153c0934ca688da2a`.

## Claim

In the notation of Yang--Mao's parameterized correlation property,

$$
\mathcal G_2^{(3)}\!\left(\frac{1}{1000000},
\frac{145261}{12500}\right)
\tag{1}
$$

holds.  Numerically, the two constants in (1) are

$$
\beta=0.000001,
\qquad C=11.62088.
\tag{2}
$$

This is a tradeoff, not a componentwise improvement of Yang--Mao's printed
pair $(1/48,8\log432)$: the new $C$ is much smaller and the new $\beta$ is
also smaller.  Their book lemma is explicitly parameterized by any pair
$(\beta,C)$ for which $\mathcal G_2^{(3)}(\beta,C)$ holds, so this tradeoff
is admissible at that interface.

## Status

**PROVABLE AS STATED, pending independent referee replay.**

The proof below is a specialization and tightening of Yang--Mao source
lines 438--824.  It does not yet assert a new Ramsey base.  Such a claim
requires a separate retained-spine certificate using (1).

## Exact constants

Put

$$
u_0=\frac{29}{10}=2.9,
\qquad a=e^{-u_0},
\qquad L=u_0^3,
\tag{3}
$$

and define

$$
E(z)=\sum_{n\ge0}\frac{z^n}{(3n)!},
\quad H(z)=1+aE(z)^2,
\quad G(z)=\frac{H(z)-H(-z)}2.
\tag{4}
$$

For the two-coordinate function set

$$
F(x_1,x_2)=G(x_1)H(x_2)+G(x_2)H(x_1).
\tag{5}
$$

Finally let

$$
c=4u_0=\frac{58}{5},
\qquad \sigma=\frac1{200},
\qquad \varepsilon=\frac{9}{5000},
\qquad C=(1+\varepsilon)c=\frac{145261}{12500},
\qquad \beta=\frac{1}{1000000}.
\tag{6}
$$

## Dependency map

1. The positivity of all Taylor coefficients of $F$ and the moment
   positivity argument are exactly Yang--Mao Lemma 2.2 and source
   lines 699--716.
2. We do not import the full normalization in the last part of Yang--Mao
   Lemma 3.2.  We directly prove the weaker but sufficient $r=2,d=3$
   separator $F<-\sigma$ on the bad event.
3. The growth estimate for $F$ on $[-1,\infty)^2$ is the same proof as
   Yang--Mao Lemma 3.3(ii), with $u_{2,3}$ replaced by $u_0$.
4. The final tail integration is Yang--Mao Theorem 3.4 with its unnecessary
   choices $C=2c$ and $\beta=1/(4D_2(2+1))$ left as variables.

## Proof

### Step 1: signs and positive coefficients

The series $E$ has nonnegative coefficients, hence so does $H$.  The odd
part $G$ also has nonnegative coefficients.  Consequently every
multivariate Taylor coefficient of $F$ is nonnegative.

For $x\ge0$, coefficient positivity gives $|E(-x)|\le E(x)$ and therefore

$$
0\le \frac{G(x)}{H(x)}
=\frac12\left(1-\frac{H(-x)}{H(x)}\right)\le\frac12.
\tag{7}
$$

For $x<0$, oddness of $G$ gives $G(x)/H(x)\le0$.

### Step 2: the specialized negative-tail ratio

For $u\ge0$, the exact cubic root filters are

$$
E(u^3)=\frac{e^u+2e^{-u/2}\cos(\sqrt3u/2)}3,
\qquad
E(-u^3)=\frac{e^{-u}+2e^{u/2}\cos(\sqrt3u/2)}3.
\tag{8}
$$

Thus

$$
E(u^3)\ge\frac{e^u-2e^{-u/2}}3,
\qquad
|E(-u^3)|\le\frac{2e^{u/2}+e^{-u}}3.
\tag{9}
$$

For $u\ge u_0=2.9$, the lower-bound base
$e^u-2e^{-u/2}$ is positive (indeed it is already greater than $16$ at
$u=u_0$).  Hence squaring this lower bound in the argument below preserves
the direction of the inequality.

Define

$$
\begin{aligned}
B(u)={}&e^{2u}-\frac{201}{25}e^u-4e^{u/2}
       -\frac{201}{25}e^{-u/2}
       +4e^{-u}-\frac{201}{100}e^{-2u},\\
J(u)={}&e^{-u_0}B(u)-\frac{909}{100}.
\end{aligned}
\tag{10}
$$

The Arb checker accompanying this note proves, with outward rounding,

$$
J(u_0)>0,
\qquad
2e^{u_0}\left(e^{u_0}-\frac{201}{50}\right)
-2e^{u_0/2}-4e^{-u_0}>0.
\tag{11}
$$

The second expression in (11) remains positive for $u\ge u_0$.  Indeed its
derivative is

$$
4e^{2u}-\frac{201}{25}e^u-e^{u/2}+4e^{-u}>0
\tag{12}
$$

there: $u\ge u_0=2.9$ implies $e^u>18$, so the first two terms alone
dominate $e^{u/2}$, while the last term is positive.  Since

$$
B'(u)
\ge 2e^u\left(e^u-\frac{201}{50}\right)-2e^{u/2}-4e^{-u},
\tag{13}
$$

equations (11)--(13) show that $B$, hence $J$, is increasing on
$[u_0,\infty)$.  Therefore $J(u)>0$ for all $u\ge u_0$.

Using (9), the inequality $J(u)>0$ is exactly

$$
1+\frac a9(e^u-2e^{-u/2})^2
>\frac{201}{100}
\left[1+\frac a9(2e^{u/2}+e^{-u})^2\right].
\tag{14}
$$

It follows that, for every $y=u^3\ge L$,

$$
\frac{H(y)}{H(-y)}>\frac{201}{100}=2+2\sigma.
\tag{15}
$$

Consequently

$$
\frac{G(-y)}{H(-y)}
=-\frac12\left(\frac{H(y)}{H(-y)}-1\right)
<-\frac12-\sigma.
\tag{16}
$$

This is weaker than the printed normalization in Yang--Mao Lemma 3.2, but
it is exactly what is needed to reprove the two-coordinate bad-event
separator below.

### Step 3: the two-coordinate envelope

Let $A_1,A_2\ge-1$ and $M=\max(A_1,A_2)$.  The source proof of Lemma
3.3(ii) applies verbatim.  For $-1\le A\le0$, write
$LA=-v^3$, where $0\le v\le u_0$.  By the negative-axis root-filter bound,

$$
a|E(-v^3)|^2\le e^{-u_0}e^v\le1.
\tag{17}
$$

For $A\ge0$, coefficient positivity gives
$E(LA)\le e^{u_0A^{1/3}}$.  Hence, for all $A\ge-1$,

$$
H(LA)\le2\exp\!\left(2u_0(A+1)^{1/3}\right).
\tag{18}
$$

As $G/H\le1/2$ on the nonnegative side and is nonpositive on the negative
side, (18) gives

$$
F(LA_1,LA_2)
\le4\exp\!\left(4u_0(M+1)^{1/3}\right)
=D_2e^{c(M+1)^{1/3}},
\quad D_2=4.
\tag{19}
$$

On the other hand, if some $A_i<-1$, (16) and (7) show that the sum of the
two ratios $G/H$ is less than $-\sigma$.  Moreover, the definition gives
$H(x)=1+aE(x)^2\ge1$, so $H(LA_1)H(LA_2)\ge1$.  Multiplying the negative
ratio sum by this product therefore gives

$$
F(LA_1,LA_2)<-\sigma.
\tag{20}
$$

### Step 4: the sharpened tail integration

Let $Z_1,Z_2$ be the two inner products in the definition of
$\mathcal G_2^{(3)}$.  Positivity of the Taylor coefficients and
Yang--Mao's tensor-moment lemma give

$$
\mathbb E F(LZ_1,LZ_2)\ge0.
\tag{21}
$$

Put

$$
\mathcal E=\{Z_1,Z_2\ge-1\},
\qquad Y=((\max(Z_1,Z_2)+1)_+)^{1/3}.
$$

Equations (19)--(21) imply

$$
D_2\,\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
\ge\sigma\bigl(1-\mathbb P(\mathcal E)\bigr).
\tag{22}
$$

Suppose the conclusion of $\mathcal G_2^{(3)}(\beta,C)$ failed for both
coordinates and every threshold.  If $\mathbb P(\mathcal E)\ge\beta$, the
threshold $-1$ already contradicts failure.  Thus
$\mathbb P(\mathcal E)<\beta$.  The same union bound and tail integration as
in Yang--Mao source lines 795--824 then give

$$
\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
<\beta+2\beta\frac{c}{C-c}
=\beta\left(1+\frac2\varepsilon\right).
\tag{23}
$$

Our exact rationals satisfy

$$
\beta D_2\left(1+\frac2\varepsilon\right)
<\sigma(1-\beta).
\tag{24}
$$

Equations (22)--(24) and $\mathbb P(\mathcal E)<\beta$ now give the strict
opposite inequalities

$$
D_2\,\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
>\sigma(1-\beta)
\quad\text{and}\quad
D_2\,\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
<\sigma(1-\beta),
$$

a contradiction.  This proves (1).

## What this does and does not establish

- It supplies a stronger parameter pair for the exact parameterized book
  theorem used by the retained-spine transfer.
- It does not modify regularization, preliminary-spine compatibility, the
  page-set loss, or the frozen off-diagonal rate $P_6$.
- It does not by itself prove a new Ramsey base.  A full-square
  retained-spine enclosure with the new $(\beta,C)$ is still required.
- It makes no claim that (2) is optimal.  Both the root-filter parameter and
  the $\beta$--$C$ tradeoff can be optimized further.

## Reproduction

Run

```text
.venv/bin/python routes/upper/check_specialized_correlation.py
```

The checker verifies the two transcendental endpoint inequalities, all
exact rational identities and the strict tail-integration budget.
