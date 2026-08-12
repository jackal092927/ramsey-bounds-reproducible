# Independent adversarial referee: exact-diagonal next round

Date: 2026-08-12  
Reviewed runtime: `python-flint==0.9.0`, 512-bit Arb

## Verdict

**PASS (MINOR PROVENANCE CORRECTION RESOLVED).**  The mathematical claim
survives unchanged.  Under the explicitly pinned Yang--Mao v1 and
retained-spine/P6 dependencies, the reviewed package proves

$$
 \mathcal G_2^{(3)}\!\left(
 \frac{330867}{500000},
 \frac{12366348252219}{1250000000000}
 \right)
 \tag{R1}
$$

and the conditional local computer-assisted asymptotic bound

$$
 R(k,k)\le(3.780685290)^{k+o(k)}.
 \tag{R2}
$$

I found no gap in the ratio/separator argument, the full two-dimensional
sign reduction, the exact-diagonal compact enclosure, the analytic
half-line, the exact expectation-tail budget, the inner/outer parameter
handoff, the retained-spine/P6 wedge, or the final exponential.  Every
numerical acceptance gate written in the protocol passes without being
weakened.

The initial review required one correction only to the provenance sentence
in the candidate which says that the $10^{-10}$ analytic-tail gate was fixed
before the sole freeze.  The available chronology proves only that this
threshold appears in the author checker before the final candidate document,
not that it was part
of the already-frozen public protocol or fixed before rationalization.  The
public protocol requires a **strict proved** analytic tail and reserves
its $10^{-9}$ threshold explicitly for the listed outer margins; it does not
state a numerical inner-tail gate.  The author inner checker, created before
the final candidate document, separately imposes $10^{-10}$, and the earlier
search program uses a $2\cdot10^{-10}$ asymptotic allowance.  Therefore the
accurate wording is:

> The protocol required a strict analytic tail proof.  The author checker
> independently imposed a $10^{-10}$ inner proof margin before the final
> candidate document, while the exploratory search used a
> $2\cdot10^{-10}$ asymptotic allowance.

This was not a mathematical failure: the certified tail slack is
$8.3673017611\ldots\cdot10^{-10}>0$, so it meets the protocol as written and
also exceeds the checker's additional $10^{-10}$ threshold.  The author made
exactly this wording correction without changing the protocol, formulas, or
constants.  I reviewed the corrected paragraph, updated the independent hash
pins, and freshly replayed all four 512-bit checks.  Every check returned
`PASS` with unchanged mathematical margins.  The correction is therefore
resolved and this report imposes no remaining hold on promotion.

The claim remains conditional and asymptotic.  It supplies no finite-$k$
threshold, unconditional theorem, finite Ramsey-number value, global
optimum, publication priority, or world-best assertion.

## Frozen review snapshot

The pre-correction snapshot reviewed here is

```text
7fa44c0ae2755f0e1dbb436a9cf3a6b0f50867d3fcb8df0e74bb13c394636827  EXACT_DIAGONAL_NEXT_PROTOCOL.md
9c0ad6e0957a15975c545784e1826206f5ae8268f5aae8ed050b617e33120e9a  search_exact_diagonal_next.py
17db00d9374ce3ba3e68a3a4626ec2c51a70ec45a307972dacc245b153382c3e  check_exact_diagonal_next.py
e2035cbffefcb147141fcee4831cac2af085f26d9183091ee20d90acc89ac87b  check_retained_spine_exact_diagonal_next.py
69fb89a9134be649f0290437cfce02c787cd24c3b3fd434a19370bcfa2d6e6aa  EXACT_DIAGONAL_NEXT_CANDIDATE.md
022b5d8d4b95c9c9ce57085e1797af6e7657da3b971134c6c2fd98e24bcfa25c  independent_check_exact_diagonal_next.py
353921e2333a29ce5b0cfc88a70c8696219bb605aae2f0a174cd386c88f4a770  referee_check_exact_diagonal_next.py
```

The resolved post-correction snapshot is

```text
7fa44c0ae2755f0e1dbb436a9cf3a6b0f50867d3fcb8df0e74bb13c394636827  EXACT_DIAGONAL_NEXT_PROTOCOL.md
9c0ad6e0957a15975c545784e1826206f5ae8268f5aae8ed050b617e33120e9a  search_exact_diagonal_next.py
17db00d9374ce3ba3e68a3a4626ec2c51a70ec45a307972dacc245b153382c3e  check_exact_diagonal_next.py
e2035cbffefcb147141fcee4831cac2af085f26d9183091ee20d90acc89ac87b  check_retained_spine_exact_diagonal_next.py
e4ea58def640593690a7545e111c3b38f1bfcf8a5735fe7985600481e0bf36d4  EXACT_DIAGONAL_NEXT_CANDIDATE.md
fc379e3b861b69054aadaa80ebc3c791cb8358f22c9b0aa01070c56aa131c26c  independent_check_exact_diagonal_next.py
3c30f72ddc24848f2b72c278f35b5d8bd6296ae8a40b045d30c5b7e087bd7150  referee_check_exact_diagonal_next.py
```

The immediate outer dependencies are pinned by

```text
8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8  certificate-higher-order-tetradecic-chain-v6.json
5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa  RETAINED_SPINE_TRANSFER_ATTEMPT.md
6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db  INDEPENDENT_RETAINED_SPINE_REFEREE.md
b10815b10cb3ab922aa079ee74289c52239ec90939ed41b93907bf06a60ee274  check_retained_spine_transfer.py
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
4b29c692dd1fc96859491b25d61c9b0e1124a33cf57a45ef01abb5a2e49ed30d  HYBRID_CORRELATION_SHARPENING.md
80b5ae4d663194623b4b6222181792d1bf71f5f73684133d84f936ed1807fefb  STRONG_SEPARATOR_GROWTH_SHARPENING.md
```

I freshly downloaded the Yang--Mao v1 TeX source from
<https://arxiv.org/abs/2608.01962v1>.  Its identity is

```text
155b7104ec5b6935a576ae9f2b161976a966b0b46bd2b69153c0934ca688da2a  main.tex
```

The source defines $\mathcal G_r^{(d)}(\beta,C)$ for every
$0<\beta\le1$ and $C>0$, and its parameterized book theorem accepts exactly
that domain.  Thus the large value $\beta=330867/500000<1$ is allowed.

## Protocol chronology and freeze audit

The workspace has no Git history, so filesystem birth/modification times are
provenance evidence rather than a tamper-evident log.  Within that limitation,
the ordering is unambiguous:

| artifact | birth time | final modification time |
|---|---:|---:|
| protocol | 09:36:22 | 09:36:31 |
| exploratory search | 09:37:22 | 09:37:22 |
| author inner checker | 09:39:16 | 09:39:34 |
| author outer checker | 09:40:32 | 09:40:53 |
| candidate document | 09:42:44 | 09:44:13 |
| non-importing replay | 09:43:59 | 09:44:36 |

Thus the protocol predates the exploratory search and all exact candidate
artifacts.  The protocol hash is also pinned by the non-importing replay.
The workspace contains one rationalized exact candidate in this round.  A
fresh deterministic run of the exploratory program returned the single
floating frontier

```text
u0       = 2.4715654916099403
D        = 0.00008805245279949252
beta     = 0.66173758931383
epsilon  = 0.0006893016965982804
C        = 9.893076583586243
gap      = 0.000003477335359765774
base     = 3.7806852810626537
```

The exact package rationalizes this frontier once, to

$$
u_0=\frac{1235783}{500000},\quad
D=\frac{88053}{10^9},\quad
\beta=\frac{330867}{500000},\quad
\varepsilon=\frac{6893}{10^7}.
$$

I found no second high-precision candidate or reopened freeze in the reviewed
workspace.

The numerical protocol gates replay as follows.

| frozen gate | certified value | verdict |
|---|---:|---:|
| actual-base improvement | $>1.02078502924\cdot10^{-8}$ | PASS |
| safe decimal | $3.780685290$ | PASS |
| degree margin | $>1.5056762\cdot10^{-9}$ | PASS |
| red-page margin | $>5.10067078\cdot10^{-9}$ | PASS |
| blue-page margin | $>3.48256584\cdot10^{-6}$ | PASS |
| reservoir margin | $>6.04687796\cdot10^{-6}$ | PASS |
| rounding margin | $>1.620359886\cdot10^{-9}$ | PASS |
| exact expectation-tail budget | $1.14428071085\ldots\cdot10^{-5}$ | PASS |
| exact inner/outer $C$ identity | $12366348252219/1250000000000$ | PASS |
| author and non-importing 512-bit checks | all commands return `PASS` | PASS |

The narrowest protocol-listed outer margin is the degree margin, not the
analytic-tail slack.

## Exact claim and dependency map

Put

$$
u_0=\frac{1235783}{500000},\qquad L=u_0^3,\qquad a=e^{-u_0},
$$

$$
E(z)=\sum_{n\ge0}\frac{z^n}{(3n)!},\qquad
H(z)=1+aE(z)^2,
$$

$$
G(z)=\frac{H(z)-H(-z)}2,qquad
F(x,y)=G(x)H(y)+G(y)H(x).
\tag{1}
$$

The new conclusion depends on five nontrivial components.

1. The nonnegative Taylor coefficients of $F$ give the Yang--Mao positive
   tensor-moment inequality.
2. A full-half-line ratio estimate yields the strict bad-event separator.
3. Every point in the good two-dimensional region reduces to the
   nonnegative diagonal, where the exact identity is enclosed on a compact
   interval and then on an analytic tail.
4. The exact rational expectation-tail budget proves (R1) under the pinned
   Yang--Mao parameterized interface.
5. The already reviewed retained-spine transfer, with the frozen degree-14
   rate, converts (R1) into the complete outer wedge and (R2).

No stronger Yang--Mao theorem or rate-function property is silently assumed.

## 1. Critical ratio, exact target, and separator

Define

$$
\sigma_0=\frac1{10^8},\qquad
T=2+2\sigma_0=\frac{100000001}{50000000},
$$

$$
\sigma_*=\frac{1+2\sigma_0}{2}
=\frac{50000001}{100000000}.
\tag{2}
$$

The ratio target and separator are distinct.  For $u\ge0$, the cubic root
filters are

$$
P(u)=\frac{e^u+2e^{-u/2}\cos(\sqrt3u/2)}3,
$$

$$
N(u)=\frac{e^{-u}+2e^{u/2}\cos(\sqrt3u/2)}3,
\tag{3}
$$

with the derivatives displayed in the candidate.  If

$$
R(u)=\frac{1+aP(u)^2}{1+aN(u)^2},
$$

then $R'(u)$ has the sign of

$$
W(u)=PP'(1+aN^2)-NN'(1+aP^2).
\tag{4}
$$

At the deliberately near-critical endpoint, independent 512-bit evaluation
gives

$$
R(u_0)-T
>2.6595378524051951\cdot10^{-7}>0.
\tag{5}
$$

The author and frozen replay respectively use 65,536 and 131,072 rational
cells on $[u_0,2.9]$.  My non-importing adaptive replay instead resolves the
whole interval with three dyadic leaves, maximum depth two, and obtains the
coarse but strictly positive lower bound

$$
W(u)>1.0124509175\ldots.
\tag{6}
$$

For $u\ge2.9$, the elementary envelopes in the candidate reduce the ratio
claim to

$$
K(u)=aB_T(u)-9(T-1)>0,
$$

$$
B_T(u)=e^{2u}-4Te^u-4e^{u/2}-4Te^{-u/2}
       +4e^{-u}-Te^{-2u}.
\tag{7}
$$

The separate reconstruction gives $K(2.9)>5.03528$.  Let

$$
D_0(u)=2e^u(e^u-2T)-2e^{u/2}-4e^{-u}.
$$

Direct differentiation gives $B_T'(u)\ge D_0(u)$.  Moreover,
$D_0(2.9)>0$, and for every $u\ge2.9$ one has $e^u>T+1$, so

$$
D_0'(u)=4e^u(e^u-T)-e^{u/2}+4e^{-u}
       >4e^u-e^{u/2}>0.
\tag{8}
$$

Thus $D_0$, $B_T$, and $K$ remain strictly increasing on the full tail.
Equations (5)--(8) prove $R(u)>T$ for every $u\ge u_0$; no sampled tail is
being substituted for a half-line argument.

If $t\ge L$, put $A=H(-t)$ and $R_t=H(t)/H(-t)$.  For arbitrary real $y$,
exact substitution gives

$$
F(-t,y)=\frac A2\bigl((2-R_t)H(y)-H(-y)\bigr).
\tag{9}
$$

Since $A,H(y),H(-y)\ge1$ and $R_t>2+2\sigma_0$,

$$
F(-t,y)<-\frac{1+2\sigma_0}{2}=-\sigma_*.
\tag{10}
$$

Equation (9) is valid for every $y$, including a second bad coordinate;
symmetry handles which coordinate is below $-L$.  The separator is therefore
strict on the entire bad event.

## 2. Full two-dimensional sign reduction

The coefficients of $H$ are nonnegative.  On $[0,\infty)$, $H$ is
nondecreasing and the odd part $G$ is nonnegative and nondecreasing.  If
$x=-v^3\in[-L,0]$, the root filter gives

$$
|E(-v^3)|\le e^{v/2},\qquad
H(x)\le1+e^{v-u_0}\le2.
\tag{11}
$$

For $x,y\ge-L$, put $m=\max\{x,y,0\}$ and assume by symmetry that
$x\le y$.  The sign partition is exhaustive.

1. If $x\le y<0$, both $G$ factors are negative and both $H$ factors are
   positive, so $F(x,y)<0=F(0,0)$.
2. If $x<0\le y$, discard $G(x)H(y)\le0$ and use (11):
   $$
   F(x,y)\le G(y)H(x)\le2G(y)\le2G(y)H(y)=F(y,y).
   $$
3. If $0\le x\le y$, monotonicity bounds each summand by $G(y)H(y)$,
   again giving $F(x,y)\le F(y,y)$.

The weak inequalities include $x=-L$, $x=0$, $y=0$, and $x=y$.  Hence

$$
F(x,y)\le F(m,m)qquad(x,y\ge-L).
\tag{12}
$$

No quadrant, axis, or double-negative case is missing.

## 3. Exact diagonal, compact interval, and analytic tail

For $z\ge0$, the package uses the exact identity

$$
F(z,z)=2G(z)H(z)=H(z)^2-H(z)H(-z),
\tag{13}
$$

not the older square-difference surrogate.  Put $z=u^3$ and

$$
w=(u^3+u_0^3)^{1/3}.
$$

The exact target is

$$
D=\frac{88053}{10^9}.
\tag{14}
$$

The author checker encloses (13) over $[0,20]$ using 131,072 exact rational
cells, and the frozen non-importing replay uses 262,144 cells.  My separate
program reconstructs the filters and (13) without importing either checker
and adaptively covers the interval with 778 leaves, maximum depth 11.  Even
with this deliberately coarser dependency enclosure, every cell proves

$$
D-\frac{F(u^3,u^3)}{e^{4w}}
>6.9885\cdot10^{-9}>0.
\tag{15}
$$

The fine fixed-grid replay gives the much stronger compact slack
$4.2943\cdot10^{-6}$.

For $u\ge20$, $H(-u^3)\ge1$ implies

$$
H(u^3)^2-H(u^3)H(-u^3)
\le H(u^3)^2-H(u^3).
\tag{16}
$$

Writing $H(u^3)=1+aP(u)^2$, the right side is exactly

$$
aP(u)^2+a^2P(u)^4.
\tag{17}
$$

Using

$$
|P(u)|\le\frac{e^u}{3}(1+2e^{-3u/2}),\qquad w\ge u,
$$

gives the analytic half-line envelope

$$
\frac{F(u^3,u^3)}{e^{4w}}
\le
\frac a9e^{-2u}(1+2e^{-3u/2})^2
+\frac{a^2}{81}(1+2e^{-3u/2})^4.
\tag{18}
$$

Both terms are decreasing: logarithmic differentiation gives a strictly
negative derivative for the first term, while the second decreases with
$e^{-3u/2}$.  Therefore evaluation at $u=20$ proves the entire tail.  The
independent 512-bit bounds are

$$
D-\text{RHS}_{(18)}(20)
>8.3673017611043569\cdot10^{-10},
\tag{19}
$$

$$
D-\frac{a^2}{81}
>8.3673024206701623\cdot10^{-10}.
\tag{20}
$$

The actual asymptotic constant is $a^2/81$: the $a^2P^4$ term has this
limit after division by $e^{4w}$, while all lower-order terms vanish.
Equations (12)--(20) prove the complete good-region estimate strictly.

The exact diagonal is genuinely used in (13)--(17), but the new decimal
should not be causally attributed to that substitution alone.  The binding
tail remains close to the common asymptotic floor, and the numerical gain
comes from the jointly tightened $D$, near-critical $u_0$, and retuned outer
tuple.  This is consistent with the protocol's method diagnostic.

## 4. Exact tail budget and inner/outer handoff

The exact parameters entering the contradiction are

$$
D=\frac{88053}{10^9},\quad
\sigma_*=\frac{50000001}{100000000},
$$

$$
\beta=\frac{330867}{500000},\quad
\varepsilon=\frac{6893}{10^7}.
\tag{21}
$$

Under failure of $\mathcal G_2^{(3)}(\beta,C)$, the two-coordinate union
bound and tail integral give the upper cost

$$
D\beta\left(1+\frac2\varepsilon\right),
$$

whereas positive tensor moments and the strict separator give the lower
credit $\sigma_*(1-\beta)$.  Their exact difference is

$$
\sigma_*(1-\beta)
-D\beta\left(1+\frac2\varepsilon\right)
=\frac{39437634699447}{3446500000000000000}
$$

$$
=1.14428071085005\ldots\cdot10^{-5}>10^{-5}.
\tag{22}
$$

Thus threshold equality cannot consume the protocol margin.  The exact
correlation constant is

$$
C=4u_0(1+\varepsilon)
=\frac{12366348252219}{1250000000000}
=9.8930786017752.
\tag{23}
$$

The inner checker, author outer checker, frozen non-importing replay, and my
separate replay all reconstruct (23) from $(u_0,\varepsilon)$; none accepts
the decimal as input.  This proves (R1) under the pinned source interface.

## 5. Independent retained-spine/P6 reconstruction

The outer tuple is

$$
\eta=0.02868896,\quad p=0.47130887,\quad
\delta=0.000053863,
$$

$$
\lambda_0=13233,\quad \tau=0.00069386,\quad
\Delta=0.0000034754.
\tag{24}
$$

All are treated as exact terminating rationals.  I reconstructed the frozen
degree-14 rate

$$
U(z)=(1+z)\log(1+z)-z\log z+P_6(z)e^{-z}
\tag{25}
$$

from all fourteen certificate coefficients.  Near zero, the pole term in
$U''$ is handled analytically.  The remainder of $(0,1]$ is covered by 42
adaptive leaves, maximum depth eight, and every enclosure gives $U''<0$.
The deliberately coarse worst upper endpoint is below $-0.0109$; the frozen
fine replay gives $-0.3602795\ldots$.  Both prove global strict concavity.

Define

$$
c_\eta=\log\frac2{1+\eta},\qquad
A=U(1)-2c_\eta,qquad E=U'(1)-c_\eta.
$$

On the ordered half-square $0\le x\le y$, concavity gives the direct gain

$$
U(1)-D_{\rm direct}(x,y)\ge xA+(y-x)E.
\tag{26}
$$

The only exceptional wedge is therefore

$$
\mathcal W=\{0\le x\le y:xA+(y-x)E\le\Delta\}.
\tag{27}
$$

With

$$
r_{\rm axis}=\frac\Delta E,\qquad
r_{\rm diag}=\frac\Delta A,\qquad
s=1-\frac AE,
$$

the exact order

$$
0<r_{\rm axis}<\tau<r_{\rm diag}<1,
\qquad0<s<1
\tag{28}
$$

makes $\mathcal W$ the triangle with vertices
$(0,0)$, $(0,r_{\rm axis})$, and
$(r_{\rm diag},r_{\rm diag})$.  Symmetry covers the opposite ordering.

For the red page, its two coordinate derivatives have signs
$\partial_x<0$ and $\partial_y>0$, so a maximum lies on the sloping
boundary.  If $z$ is its rate-function argument, the boundary derivative is

$$
B(z)=c_\eta-U'(z)
+s\bigl(c_\eta-U(z)+zU'(z)\bigr).
$$

Since

$$
B'(z)=(sz-1)U''(z)>0,
$$

its largest value occurs at the axis endpoint, where the independent
enclosure is still negative.  Hence the red maximum is the axis vertex and
its margin is

$$
>5.10067078229\cdot10^{-9}.
\tag{29}
$$

For the blue page, $\partial_y<0$ reduces the maximum to $y=x$.  Writing
$q=\tau/(1-x)$, the derivative along this diagonal has derivative
$qU''(1-q)<0$ with respect to $q$; its maximum is therefore at the origin,
where it is strictly negative.  The blue-page margin is

$$
>3.48256584382\cdot10^{-6}.
\tag{30}
$$

The reservoir rate is coordinatewise increasing, so the diagonal vertex
maximizes it.  Its margin is

$$
>6.04687796010\cdot10^{-6}.
\tag{31}
$$

Finally,

$$
\tau(1/2-\eta-p)
=1.5056762\cdot10^{-9}>10^{-9},
\tag{32}
$$

and 512-bit outward rounding gives

$$
e^{U(1)-\Delta}
<3.7806852883796401133524\ldots
<3.780685290.
\tag{33}
$$

The rounding margin exceeds $1.620359886\cdot10^{-9}$.  Relative to the
previous actual candidate,

$$
3.7806852985874904057580\ldots-e^{U(1)-\Delta}
>1.02078502924\cdot10^{-8},
\tag{34}
$$

while the exact safe-decimal improvement is
$3.780685300-3.780685290=10^{-8}$.  Equations (26)--(34) cover the complete
ordered wedge, its symmetric copy, both book colors, the simultaneous
reservoir requirement, and every outer gate.  They establish (R2).

## Replay record and independence

All frozen commands returned `PASS` unchanged:

```text
.venv/bin/python routes/upper/check_exact_diagonal_next.py
.venv/bin/python routes/upper/check_retained_spine_exact_diagonal_next.py
.venv/bin/python routes/upper/independent_check_exact_diagonal_next.py
```

The third program imports no author checker and reconstructs the special
functions, exact rationals, rate and derivatives, compact and tail estimates,
global concavity, wedge, and final exponential at 512-bit precision.

I additionally wrote and ran

```text
.venv/bin/python routes/upper/referee_check_exact_diagonal_next.py
```

This referee replay also imports no author code.  It uses adaptive dyadic
subdivision instead of any author's fixed grid, proves the ratio finite
interval with 3 leaves, the exact-diagonal compact interval with 778 leaves,
and global rate concavity with 42 leaves.  It then uses analytic endpoint
reductions rather than the author's sampled red/blue boundary derivatives.
The agreement is therefore not a duplicated control flow masquerading as an
independent check.

## Remaining boundaries

- The minor provenance correction is resolved; the post-correction
  hash-pinned author, non-importing, and adaptive referee replays all pass.
- The theorem depends on the pinned Yang--Mao v1 moment/tail and book
  interfaces and the frozen local P6/BookCor/retained-spine chain.
- Arb interval arithmetic is trusted at the pinned runtime; this is not a
  proof-assistant formalization.
- The result is asymptotic and has no extracted finite-$k$ threshold.
- The inner analytic-tail margin is only about $8.37\cdot10^{-10}$ and the
  degree margin only about $1.51\cdot10^{-9}$, so hashes and outward rounding
  are material.
- No optimality, novelty, priority, finite Ramsey-number, or world-best claim
  follows.

Within these explicit boundaries, the corrected and replayed package supports
the safe base **3.780685290**.
