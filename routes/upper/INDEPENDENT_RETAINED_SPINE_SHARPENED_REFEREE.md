# Independent referee: specialized correlation and sharpened retained spine

Date: 2026-08-12  
Referee implementation: independent 512-bit Arb replay

## Claim reviewed

The author package claims

$$
\mathcal G_2^{(3)}\!\left(10^{-6},11.62088\right)
\tag{R1}
$$

and, conditional on the already declared frozen $P_6$, BookCor, and
Yang--Mao trust boundary,

$$
R(k,k)\le
\exp\!\left((U(1)-2.87\cdot10^{-6})k+o(k)\right)
\le(3.780687577208)^{k+o(k)}.
\tag{R2}
$$

The exact correlation parameters are

$$
\beta=\frac1{10^6},\qquad
C=\frac{145261}{12500},
$$

and the exact retained-spine tuple is

$$
(\eta,p,\delta,\lambda_0,\tau)
=(0.028681,0.471309,0.0000528,13520,0.000572).
$$

## Final verdict

**PASS — RESOLVED.**  No fatal mathematical or numerical gap was found.  The
initial review requested two local proof details before promotion:

1. Before squaring the lower root-filter envelope in Step 2, state that
   $e^u-2e^{-u/2}>0$ for $u\ge u_0=2.9$.
2. In the bad-event separator, replace the cited fact $H>0$ by the needed
   stronger fact $H\ge1$.  When the ratio sum is negative, this is what
   justifies multiplying it by $H(x_1)H(x_2)$ without weakening the
   $-\sigma$ bound.

Both facts follow immediately from displayed definitions and are
independently checked below.  The author inserted exactly these two details,
without changing a formula, parameter, claimed constant, or numerical
margin.  The revised author checker and revised independent 512-bit replay
both pass.  The claim is therefore `PROVABLE AS STATED` within its declared
conditional trust boundary.

## Frozen inputs reviewed

The initial author artifacts were reviewed at these SHA-256 values:

```text
076a7f2993d610e77cca68b970e7e91193701b7c535acf9af9792be1f078313c  SPECIALIZED_CORRELATION_SHARPENING.md
be17cc0848a54e606b4ad4bc3393b8ac317f030306c239d41bd0f90f38c5724a  check_specialized_correlation.py
83e79f2a2950c73d0a3697193b3fd826130d69f197f57febd4a8f9f1c25acdbf  RETAINED_SPINE_SHARPENED_CERTIFICATE.md
1eb81c9132985137e3135ac83d542ecf0be9354f21e919f724a69ebe857d834e  check_retained_spine_sharpened.py
```

The resolved, promoted artifacts are:

```text
c28026ed8d30e0c4096ccc46e3cc04d7026fa2c2975eab4a2537a9021a866ebe  SPECIALIZED_CORRELATION_SHARPENING.md
be17cc0848a54e606b4ad4bc3393b8ac317f030306c239d41bd0f90f38c5724a  check_specialized_correlation.py
83e79f2a2950c73d0a3697193b3fd826130d69f197f57febd4a8f9f1c25acdbf  RETAINED_SPINE_SHARPENED_CERTIFICATE.md
1a74a21d81002805657c74373c44b760c57edd36ad942d768e7d7afd6abfac40  check_retained_spine_sharpened.py
cf84ae77fa703ef93f7364ea9b33546fe3241efc03758ef8e1a6082bdbf00cd4  independent_check_retained_spine_sharpened.py
```

I separately downloaded Yang--Mao v1 from
`https://export.arxiv.org/e-print/2608.01962v1`.  Its `main.tex` has
SHA-256

```text
155b7104ec5b6935a576ae9f2b161976a966b0b46bd2b69153c0934ca688da2a
```

matching the author package.  The primary-source interfaces checked were:

- the cubic root filter and negative-axis estimate, source lines 438--581;
- the separator factorization and growth proof, source lines 687--791;
- the moment/tail proof, source lines 795--971;
- the definition of $\mathcal G_r^{(d)}(\beta,C)$, source lines 989--1009;
- the parameterized density-increment lemma, source lines 1017--1142;
- the parameterized book theorem and its exact $\rho,\Pi,\Xi$ constants,
  source lines 1146--1190.

The independent checker is
`independent_check_retained_spine_sharpened.py`.  Its initial SHA-256 was

```text
9f64be120026f824dda6db798fe9326867c92e880063e5cb38a3c2dc3ec587ca
```

After changing only its two author-file hash pins, its resolved SHA-256 is

```text
cf84ae77fa703ef93f7364ea9b33546fe3241efc03758ef8e1a6082bdbf00cd4
```

It does not import either author checker.

## 1. Specialized root-filter replay

Set

$$
u_0=\frac{29}{10},\qquad a=e^{-u_0},\qquad L=u_0^3,
\qquad \sigma=\frac1{200},
$$

and let $T=2+2\sigma=201/100$.  The exact cubic identities are

$$
E(u^3)=\frac{e^u+2e^{-u/2}\cos(\sqrt3u/2)}3,
$$

$$
E(-u^3)=\frac{e^{-u}+2e^{u/2}\cos(\sqrt3u/2)}3.
$$

Thus

$$
E(u^3)\ge P(u):=\frac{e^u-2e^{-u/2}}3,
\qquad
|E(-u^3)|\le N(u):=\frac{2e^{u/2}+e^{-u}}3.
\tag{1.1}
$$

The first local correction matters here: a lower bound may be squared only
after its right side is known nonnegative.  For $u\ge2.9$,

$$
e^u-2e^{-u/2}>18-2>0,
$$

so (1.1) rigorously yields $E(u^3)^2\ge P(u)^2$.

### Expanded algebra

The target inequality

$$
1+aP(u)^2>T\bigl(1+aN(u)^2\bigr)
\tag{1.2}
$$

is equivalent to

$$
e^{-u_0}B(u)>9(T-1)=\frac{909}{100},
$$

where direct expansion gives

$$
B(u)=e^{2u}-4Te^u-4e^{u/2}-4Te^{-u/2}
     +4e^{-u}-Te^{-2u}.
\tag{1.3}
$$

Substituting $T=201/100$ reproduces every coefficient in the author note;
there is no missing factor of $2$, $4$, or $9$.

### Complete half-line, not endpoint sampling

Differentiating (1.3) and discarding only positive terms gives

$$
B'(u)\ge
K(u):=2e^u(e^u-2T)-2e^{u/2}-4e^{-u}.
\tag{1.4}
$$

Moreover

$$
K'(u)=4e^{2u}-4Te^u-e^{u/2}+4e^{-u}.
\tag{1.5}
$$

For $u\ge u_0$, $e^u>18$, and therefore

$$
4e^{2u}-4Te^u=e^u(4e^u-8.04)>18(72-8.04)>e^{u/2}.
$$

Hence $K'(u)>0$ on the whole half-line.  The independent 512-bit evaluator
obtains

$$
K(u_0)>505.7326691384,
\qquad K'(u_0)>1171.0350892333.
$$

It also evaluates (1.2) directly, without the author's expanded $B/J$
control flow, and obtains the positive cross-multiplied slack

$$
1+aP(u_0)^2-T(1+aN(u_0)^2)
>0.00154098060247.
$$

Thus (1.2) holds for every $u\ge u_0$, and

$$
\frac{H(y)}{H(-y)}>2+2\sigma
\quad(y\ge L).
\tag{1.6}
$$

Consequently

$$
\frac{G(-y)}{H(-y)}< -\frac12-\sigma.
\tag{1.7}
$$

## 2. Generalized $-\sigma$ separator

For every real $x$, the sign argument gives

$$
\frac{G(x)}{H(x)}\le\frac12.
\tag{2.1}
$$

If one normalized coordinate $A_i<-1$, then $-LA_i>L$, so (1.7) applies
to that coordinate.  Combining it with (2.1) for the other coordinate gives

$$
\frac{G(LA_1)}{H(LA_1)}
+\frac{G(LA_2)}{H(LA_2)}< -\sigma.
\tag{2.2}
$$

Here is the second local correction.  The definition
$H(x)=1+aE(x)^2$ gives $H(x)\ge1$, not merely $H(x)>0$.  Since the sum in
(2.2) is negative,

$$
F(LA_1,LA_2)
=H(LA_1)H(LA_2)\left(\frac{G(LA_1)}{H(LA_1)}
+\frac{G(LA_2)}{H(LA_2)}\right)<-\sigma.
\tag{2.3}
$$

Thus the generalized separator is valid.  It does not invoke the stronger
printed conclusion $G(-y)/H(-y)\le-r$ from Yang--Mao Lemma 3.2.

## 3. Good-event envelope and expectation inequality

For $A\in[-1,0]$, the negative-axis filter gives

$$
a|E(LA)|^2\le e^{-u_0}e^v\le1,
\qquad 0\le v\le u_0.
$$

For $A\ge0$, coefficient positivity gives
$E(LA)\le e^{u_0A^{1/3}}$.  Therefore, for all $A\ge-1$,

$$
H(LA)\le2e^{2u_0(A+1)^{1/3}}.
$$

Since each ratio $G/H\le1/2$, the two-coordinate factorization gives

$$
F(LA_1,LA_2)le4e^{4u_0(M+1)^{1/3}}
=D_2e^{c(M+1)^{1/3}},
$$

with $D_2=4$ and $c=4u_0=58/5$.

Let

$$
\mathcal E=\{Z_1,Z_2\ge-1\},
\qquad Y=((\max(Z_1,Z_2)+1)_+)^{1/3}.
$$

Positive Taylor coefficients, the Yang--Mao tensor-moment identity, the good
envelope, and (2.3) imply

$$
0\le\mathbb EF(LZ_1,LZ_2)
\le D_2\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
-\sigma\mathbb P(\mathcal E^c).
$$

Hence the generalized master inequality is exactly

$$
D_2\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
\ge\sigma(1-\mathbb P(\mathcal E)).
\tag{3.1}
$$

The factor $\sigma$ and its inequality direction are correct.

## 4. Tail contradiction and exact budget

Under failure of $\mathcal G_2^{(3)}(\beta,C)$, the threshold $-1$ first
forces $\mathbb P(\mathcal E)<\beta$.  For $u\ge0$, the same union identity
as in Yang--Mao gives

$$
\mathbb P(\mathcal E\cap\{Y\ge u\})
<2\beta e^{-Cu}.
$$

Tonelli's formula therefore yields, because $C=(1+\varepsilon)c>c$,

$$
\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
<\beta\left(1+\frac{2c}{C-c}\right)
=\beta\left(1+\frac2\varepsilon\right).
\tag{4.1}
$$

The exact cost and credit are

$$
D_2\beta\left(1+\frac2\varepsilon\right)
=\frac{10009}{2250000},
$$

$$
\sigma(1-\beta)=\frac{999999}{200000000}.
$$

Their exact difference is

$$
\frac{999999}{200000000}-\frac{10009}{2250000}
=\frac{992791}{1800000000}>0.
\tag{4.2}
$$

Equations (3.1), (4.1), (4.2), and
$\mathbb P(\mathcal E)<\beta$ give the claimed strict contradiction.  This
proves (R1).

## 5. Parameterized book interface

Yang--Mao v1 does not restrict the book theorem to the constants printed in
their general correlation theorem.  Source lines 989--1009 define
$\mathcal G_r^{(d)}(\beta,C)$ for arbitrary $0<\beta\le1$, $C>0$; source
lines 1146--1190 assume that property and use exactly

$$
\rho=\log(r/\beta),
$$

$$
\Xi=2\rho+4C\lambda_0^{1/d}
+\frac{12C\log(1/\delta)}{\lambda_0^{(d-1)/d}}.
$$

For $r=2,d=3$, these are exactly the expressions in the author and referee
checkers.  The small value $\beta=10^{-6}$ is fully accounted for through
$\rho=\log(2/\beta)$; no printed $\beta_2=1/48$ or $8\log432$ remains hidden
in the book invocation.

## 6. Independent complete-square replay

The 512-bit checker rebuilds $P_6$ from the JSON coefficients using a
different Horner representation.  It proves $U''<0$ first on an analytic
near-zero interval and then on 65,536 closed cells.  It obtains

$$
A=0.00016919884368908026035\ldots,
$$

$$
E=0.10096958756532935427\ldots,
$$

and

$$
r_a=2.8424400546779021\cdot10^{-5},qquad
r_d=0.01696229086100559\ldots.
$$

All source gates are strict; in particular the regularization degree slack
is $5.72\cdot10^{-9}>0$.

The full square is covered as follows.

1. By symmetry take $0\le x\le y\le1$.
2. Concavity gives
   $$
   U(1)-D(x,y)\ge xA+(y-x)E.
   $$
   Thus the direct branch wins outside the complete weighted wedge
   $xA+(y-x)E\le\Delta$.
3. Inside the wedge, $x\le r_d$ and $y-x\le r_a<\tau$, fixing the two page
   formulas without a positive-part boundary crossing.
4. For the red page, endpoint monotonicity checks $\partial_xP_R<0$ and
   $\partial_yP_R>0$; 4,096 separate ratio cells prove that its derivative
   along the complete slanted boundary is negative.  Its maximum is therefore
   the axis endpoint $(0,r_a)$.
5. For the blue page, concavity first proves its $y$ derivative negative.
   Then 8,192 separate $x$ cells prove its diagonal derivative negative, so
   its maximum is the origin.
6. On the wedge edge, $x+y$ has derivative $2-A/E>0$; hence the reservoir
   maximum is exactly the diagonal endpoint $(r_d,r_d)$.

The independent lower margins are

| proof item | independent lower margin |
|---|---:|
| red page | $2.3362059296\cdot10^{-8}$ |
| blue page | $2.8942855952\cdot10^{-6}$ |
| reservoir | $4.5592338859\cdot10^{-3}$ |
| decimal rounding | $7.9347357905\cdot10^{-13}$ |

The cellwise derivative upper bounds are

$$
\frac d{dx}P_R(x,h(x))<-3.3844771408\cdot10^{-4},
$$

$$
\frac d{dx}P_B(x,x)<-1.6925575949\cdot10^{-4}.
$$

The first differs from the author's looser one-box enclosure, but both are
valid upper bounds for the same negative derivative.  Finally,

$$
e^{U(1)-2.87\cdot10^{-6}}
=3.78068757720720652642\ldots
<3.780687577208.
$$

This proves the complete variational inequality required for (R2).

## 7. Reproduction

From the project root:

```text
routes/upper/.venv/bin/python routes/upper/check_specialized_correlation.py
routes/upper/.venv/bin/python routes/upper/check_retained_spine_sharpened.py
routes/upper/.venv/bin/python routes/upper/independent_check_retained_spine_sharpened.py
```

All three executions returned `PASS`.  The independent script also compiles
under the pinned environment and checks `python-flint==0.9.0`.

## Claim boundary

The review supports (R2) only within the stated chain: the frozen local $P_6$
off-diagonal theorem, repaired BookCor interface, Yang--Mao v1
regularization and parameterized book construction, Arb containment, and the
specialized lemma proved here.  It does not establish a finite-$k$ threshold,
formal verification, external publication priority, global optimality of the
correlation or retained-spine parameters, or an unconditional globally
best-known bound.

## Resolution

The two explicit local insertions were made in the source-lemma note.  The
author wedge checker changed only the pinned source-note hash; the referee
checker changed only the two pinned author hashes.  Fresh executions of the
384-bit source arithmetic, 384-bit full-square checker, and 512-bit
independent replay all returned `PASS` with the same numerical values and
margins reported above.  No requested correction remains open.
