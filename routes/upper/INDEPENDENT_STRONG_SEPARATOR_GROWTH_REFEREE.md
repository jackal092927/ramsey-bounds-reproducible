# Independent adversarial referee: strong separator and retained-spine growth

Date: 2026-08-12  
Replay: non-importing 512-bit Arb checker

## Verdict

**PASS.** I found no mathematical, quantifier, strictness, numerical, or
dependency-identity gap in the frozen package.  The following two statements
survive unchanged.

First,

$$
 \mathcal G_2^{(3)}\!\left(
 \frac{11}{250},\frac{62025657}{6250000}
 \right)
 \quad\left(\frac{62025657}{6250000}=9.92410512\right).
 \tag{R1}
$$

Second, conditional on the explicitly pinned local $P_6$/BookCor theorem
chain, the already refereed retained-spine transfer, and the Yang--Mao v1
regularization and parameterized book theorem,

$$
 R(k,k)\le
 \exp\!\left((U(1)-3.445\cdot10^{-6})k+o(k)\right)
 \le (3.780685405)^{k+o(k)}.
 \tag{R2}
$$

Thus the proof status is **PROVABLE AS STATED UNDER THE EXPLICIT PINNED
DEPENDENCIES**.  This verdict supports neither an unconditional theorem nor a
finite-$k$ threshold, global optimality, publication priority, or a
world-record claim.

## Frozen identities and replay environment

The author snapshot reviewed here has SHA-256 identities

```text
80b5ae4d663194623b4b6222181792d1bf71f5f73684133d84f936ed1807fefb  STRONG_SEPARATOR_GROWTH_SHARPENING.md
9ea998eeab45a839c0fd24428bf9ccc7e0123cfc1550aaacc45f9e64a1568ccd  check_strong_separator_growth.py
f185d5ffe07944e52aeee8c54272da948b9d9be2efe6cfad4f6ddfc8549c0d96  RETAINED_SPINE_STRONG_GROWTH_CANDIDATE.md
3c9d6dadbab9469c1971466791ea4218313c93ec1a16825460099631b0251faf  check_retained_spine_strong_growth.py
```

The independent replay is
`independent_check_retained_spine_strong_growth.py`.  It pins the four author
files above and every theorem-chain artifact on which it relies.  It imports
no author checker, reconstructs the cubic root filters and the degree-14 rate
with different evaluators, uses 512-bit rather than 384-bit Arb, doubles both
new envelope partitions, quadruples the global-concavity partition, and uses
analytic monotonicity instead of copying the author's two fragile outer
cellwise checks.  The reviewed runtime was `python-flint==0.9.0`.

```text
bd398f73c149ffa44a4a4516811d74b5a532fd7c9b57aad979e43184d3df5252  independent_check_retained_spine_strong_growth.py
```

The exact theorem-chain pins are

```text
4b29c692dd1fc96859491b25d61c9b0e1124a33cf57a45ef01abb5a2e49ed30d  HYBRID_CORRELATION_SHARPENING.md
47bde6908563ee3a855cea2e9f75fe5167ab46e52a5e8691e9be0f2e1f5d5afc  INDEPENDENT_JOINT_CORRELATION_SPINE_REFEREE.md
830f9133b16abecf01fb879109c50bf4acfd8b93c7a87313626e08b197dc32d4  independent_check_retained_spine_joint_optimized.py
5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa  RETAINED_SPINE_TRANSFER_ATTEMPT.md
6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db  INDEPENDENT_RETAINED_SPINE_REFEREE.md
8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8  certificate-higher-order-tetradecic-chain-v6.json
2f142a9371d29f07ffd68253c7dbb0981fe440f7f0b8284b4a81430f38395dbc  INDEPENDENT_PROOF_REPLAY.md
2881e8b1df310b449d0bffff5715b9176d9c191ba2a5d05bb376ab2843c58ccd  STAGE6_SEARCH.md
2bb40e6dc4f83203998adad57a0e922565bc8f6f07e1bdc810dd3ebfea481f5d  INDEPENDENT_STAGE6_REFEREE.md
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
b10815b10cb3ab922aa079ee74289c52239ec90939ed41b93907bf06a60ee274  check_retained_spine_transfer.py
86fc83d1735644a063616ba1ba5aea2d1519f4088bbca591d871b784d21f2d18  BOOKCOR_AUDIT.md
```

The Yang--Mao v1 source identity and the exact source interfaces were already
independently checked in `INDEPENDENT_JOINT_CORRELATION_SPINE_REFEREE.md`:
its downloaded `main.tex` has SHA-256
`155b7104ec5b6935a576ae9f2b161976a966b0b46bd2b69153c0934ca688da2a`.
The new argument changes only the pointwise separator/growth estimates and
the numerical parameters passed through those already reviewed interfaces.

## 1. Exact bad-event identity and all quantifiers

Put

$$
 H(z)=1+aE(z)^2,\qquad
 G(z)=\frac{H(z)-H(-z)}2,
$$

$$
 F(x,y)=G(x)H(y)+G(y)H(x),
$$

and let $x=-u$, $u\ge L$.  Write

$$
 A=H(-u),\qquad R=\frac{H(u)}{H(-u)}.
$$

Then $H(u)=AR$ and

$$
 G(-u)=\frac{A-AR}{2},\qquad
 G(y)=\frac{H(y)-H(-y)}2.
$$

Substitution, without an inequality, gives

$$
 \begin{aligned}
 F(-u,y)
 &=\frac A2(1-R)H(y)
   +\frac A2\bigl(H(y)-H(-y)\bigr)\\
 &=\frac A2\bigl((2-R)H(y)-H(-y)\bigr).
 \end{aligned}
 \tag{1}
$$

The previously independently replayed ratio lemma is strict:

$$
 R>2+\frac{2}{1000}.
$$

Because $A,H(y),H(-y)\ge1$, equation (1) implies, for **every real $y$**,

$$
 F(-u,y)
 <\frac A2\left(-\frac{2}{1000}H(y)-H(-y)\right)
 \le-\frac{1002}{2000}
 =-\frac{501}{1000}.
 \tag{2}
$$

This verifies both strictness steps: the first inequality remains strict after
multiplication by positive quantities, and the second need not be strict.
It also closes the potentially fragile two-bad-coordinate case.  Formula (1)
places no condition on $y$, so if both coordinates are below $-L$, choose
either one as $x$; no union, ordering, or assumption that the other coordinate
is good is used.  Symmetry handles which coordinate is first.

The independent checker also replays the imported ratio lemma instead of
trusting its printed status.  It uses 16,384 cells on
$[619/250,29/10]$ and directly checks the analytic half-line endpoint.  It
obtains

```text
endpoint ratio slack:                         0.0002005988217396235...
finite ratio derivative numerator lower:     10.446932232867577...
half-line cross-multiplied slack at 2.9:       0.5492003812612323...
```

## 2. Independent growth-envelope replay

### Negative segment

For $-1\le A\le0$, write $LA=-v^3$, $0\le v\le u_0$.  The replay checks

$$
 1+e^{-u_0}E(-v^3)^2
 <\frac{113}{100}
   \exp\!\left(2(u_0^3-v^3)^{1/3}\right)
 \tag{3}
$$

on 32,768 exact rational cells.  It constructs the cube-root interval from
its two monotone endpoint values, avoiding the repeated-variable dependency
at $v=u_0$.  The minimum certified lower endpoint of the slack is

$$
 0.00498077975103464545\ldots>0.
$$

On $A\ge0$, coefficient positivity gives $E(u^3)\le e^u$ and
$w=(u^3+u_0^3)^{1/3}\ge u$.  Hence

$$
 H(u^3)\le1+ae^{2u}\le(1+a)e^{2w}
 <\frac{113}{100}e^{2w},
$$

where the last scalar inequality is independently enclosed.

### Positive root-filter segment and half-line direction

The replay checks, on 131,072 exact rational cells over $0\le u\le20$,

$$
 E(u^3)\le\frac13
 \exp\!\left((u^3+u_0^3)^{1/3}\right).
 \tag{4}
$$

Its minimum certified cell slack is $2.9644800792\ldots$; the apparently
large value is consistent with the $u=0$ endpoint, where the right side is
$e^{u_0}/3$.

For completeness, the analytic half-line direction in the author note is
correct.  Let

$$
 q=\frac{u_0^3}{u^3},\qquad
 \ell(u)=\frac{u_0^3}{3u^2(1+q)^{2/3}}.
$$

Concavity of $t^{1/3}$ in its secant form gives

$$
 (u^3+u_0^3)^{1/3}-u\ge\ell(u).
$$

Direct differentiation gives the exact log derivative

$$
 \frac{d}{du}\log\ell(u)
 =-\frac{2}{u(1+q)}\ge-\frac2u\ge-\frac1{10}
 \qquad(u\ge20).
 \tag{5}
$$

By comparison,

$$
 \frac{d}{du}\log\bigl(2e^{-3u/2}\bigr)=-\frac32.
$$

Thus the ratio $\ell(u)/(2e^{-3u/2})$ is strictly increasing, not
decreasing.  At $u=20$ the replay obtains

$$
 \ell(20)>0.0126334462836,
 \qquad
 \log(1+2e^{-30})<2e^{-30}<1.871524593769\cdot10^{-13}.
$$

The endpoint ordering therefore persists on the complete half-line.  This is
the required direction for

$$
 e^u+2e^{-u/2}\le e^{(u^3+u_0^3)^{1/3}}.
$$

Finally,

$$
 \frac{113e^{-u_0}}{900}
 =0.01055656914977919\ldots<\frac{11}{1000}.
$$

Discarding only terms whose $G$ coordinate is negative is safe because each
is multiplied by positive $H$.  If a remaining $G$ coordinate is positive,
then its argument is nonnegative and (4) applies; the other $H$ coordinate
is covered by (3) or the positive estimate.  Hence the stated common maximum
$M$ and coefficient $11/1000$ are valid.

## 3. Tail budget and exact parameter handoff

The earlier independently reviewed moment/tail argument applies to any
separator magnitude $\sigma$, good-event prefactor $D$, failure probability
$\beta$, and $C=(1+\varepsilon)c$ satisfying the same pointwise hypotheses.
Here the exact values are

$$
 \sigma=\frac{501}{1000},\quad
 D=\frac{11}{1000},\quad
 \beta=\frac{11}{250},\quad
 \varepsilon=\frac{203}{100000},\quad
 c=4\frac{619}{250}.
$$

The independent replay uses rational arithmetic and obtains

$$
 C=c(1+\varepsilon)
 =4\frac{619}{250}\left(1+\frac{203}{100000}\right)
 =\frac{62025657}{6250000}
 =9.92410512.
 \tag{6}
$$

The good-event tail cost and bad-event credit are exactly

$$
 D\beta\left(1+\frac2\varepsilon\right)
 =\frac{24224563}{50750000},
$$

$$
 \sigma(1-\beta)=\frac{119739}{250000}.
$$

Their difference is

$$
 \frac{41227}{25375000}
 =0.0016247\ldots>10^{-5}.
 \tag{7}
$$

All inequalities inherited from failure of the correlation property are
strict, so equality at a threshold cannot erase the contradiction.  The
outer replay reconstructs $C$ from the same exact $\varepsilon$ and $u_0$;
there is no rounded or stale correlation constant between (R1) and (R2).

## 4. Complete retained-spine wedge

The replay reconstructs

$$
 U(z)=(1+z)\log(1+z)-z\log z+P_6(z)e^{-z}
$$

from all fourteen frozen decimal coefficients, interpreted as exact
rationals.  A 65,536-cell 512-bit proof plus the analytic pole bound near
zero gives

$$
 U''(z)<0\quad(0<z\le1),
$$

with worst certified upper endpoint below $-0.36027$.  It independently
reconstructs every source gate, including

$$
 \tau(1/2-\eta-p)=2.058\cdot10^{-9}>10^{-9}.
$$

Set

$$
 A=U(1)-2c_\eta,qquad E=U'(1)-c_\eta.
$$

The direct-branch tangent inequality from concavity gives, in the ordered
triangle $0\le x\le y$,

$$
 U(1)-D(x,y)\ge xA+(y-x)E.
$$

Therefore every point outside

$$
 \mathcal W=\{0\le x\le y:\ xA+(y-x)E\le\Delta\}
 \tag{8}
$$

is already controlled.  The replay verifies $0<A<E$ and

$$
 0<r_{\rm axis}=\Delta/E<\tau
 <r_{\rm diag}=\Delta/A<1,
$$

so (8), together with its symmetric copy, is the complete complement and no
axis or corner is omitted.

For the red page, put

$$
 z=\frac{1-\tau-x}{1-y},\qquad
 h(x)=r_{\rm axis}+\left(1-\frac AE\right)x.
$$

Strict concavity makes $U'$ decreasing and $U-zU'$ increasing.  This proves
the coordinate signs $\partial_xP_R<0$ and $\partial_yP_R>0$ throughout the
wedge from endpoint evaluations.  More independently than the author
checker, the replay observes that along $y=h(x)$,

$$
 B(z)=c_\eta-U'(z)+s(c_\eta-U(z)+zU'(z)),
 \qquad s=1-A/E,
$$

and

$$
 B'(z)=(sz-1)U''(z)>0
$$

because $0<s,z<1$ and $U''<0$.  Thus only the $z$ upper endpoint is needed;
the replay obtains

$$
 B(z)<-0.0003685097333\ldots.
$$

It follows that the red maximum is $(0,r_{\rm axis})$.

For the blue page, $\partial_yP_B<0$ sends the maximum to $y=x$.  Let
$t=\tau/(1-x)$ and $w=1-t$.  The diagonal derivative is

$$
 C(x)=2c_\eta-U(w)-tU'(w),
$$

and direct differentiation yields

$$
 C'(x)=\frac{t^2}{1-x}U''(w)<0.
$$

Therefore the maximum derivative occurs at $x=0$, where the replay gives

$$
 C(0)<-0.0001842545423\ldots.
$$

The blue maximum is consequently the origin.  Finally, the reservoir cost is
coordinatewise increasing, and $x+h(x)$ has derivative $1+s>0$, so its
wedge maximum is the diagonal endpoint.  These reductions cover the entire
ordered wedge and symmetry covers the other order.

The resulting independent strict margins are

```text
raw minimum-degree slack:     3.0000000000000000e-6
degree gate:                 2.0580000000000000e-9
delta <= p/4 gate:           1.1777352500000000e-1
lambda >= 6 log(1/delta):    1.3280990631433577e+4
U'(1)-q:                     9.9281356926404941e-3
U(1)-2 tau Xi:               2.4891482068564254e-2
red page:                    3.8288495571039199e-9
blue page:                   3.4507980807351386e-6
reservoir:                   1.4736480060059178e-5
```

Each exceeds the preregistered $10^{-9}$ threshold.

## 5. Decimal and claim boundary

The independent 512-bit enclosure is

$$
 \exp(U(1)-\Delta)
 <3.7806854033124746271\ldots<3.780685405.
$$

The terminating safe decimal has certified rounding margin

$$
 1.6875253729274931\cdot10^{-9}>10^{-9}.
$$

Relative to the preceding certified safe decimal $3.780685745$, the
improvement is exactly $3.40\cdot10^{-7}>10^{-7}$.  This is an asymptotic,
conditional theorem-linked bound; the package supplies no explicit finite
$k$ threshold.

## Earliest unsupported step

There is no new unsupported step inside the reviewed strong-separator or
retained-spine arithmetic.  The earliest non-self-contained premise remains
the same declared theorem boundary as in the previous accepted package: the
frozen six-stage local off-diagonal $P_6$/BookCor rate and the Yang--Mao v1
regularization, positive tensor-moment, and parameterized book theorems.  The
workspace pins and independently reviews those interfaces, but this report
does not re-prove their full combinatorial arguments from first principles.

## Reproduction

```text
.venv/bin/python routes/upper/independent_check_retained_spine_strong_growth.py
```

Expected first line:

```text
PASS: independent 512-bit strong-growth retained-spine replay
```
