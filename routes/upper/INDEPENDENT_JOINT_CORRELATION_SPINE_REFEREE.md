# Independent adversarial referee: hybrid correlation and joint retained spine

Date: 2026-08-12  
Referee replay: independently audited 512-bit Arb implementation

## Verdict

**PASS.** I found no mathematical or numerical gap in the frozen package.
The two claims survive unchanged, with the dependency boundary stated by the
authors:

$$
\mathcal G_2^{(3)}\!\left(\frac1{4000000},
\frac{6202999}{625000}\right),
\tag{R1}
$$

and, conditional on the pinned local $P_6$/BookCor chain, the already
refereed retained-spine transfer, and the Yang--Mao v1 regularization and
parameterized book theorem,

$$
R(k,k)\le
\exp\!\left((U(1)-3.355\cdot10^{-6})k+o(k)\right)
\le (3.780685745)^{k+o(k)}.
\tag{R2}
$$

The proof status is therefore **PROVABLE AS STATED UNDER THE EXPLICIT PINNED
ASSUMPTIONS**. The phrase “pending independent replay” in the two frozen
author notes records their pre-referee status; it is not a remaining proof
gap.

This verdict does not support a world-record, publication-priority,
finite-$k$, explicit-threshold, or optimality claim.

## Frozen artifacts and source identity

The exact author snapshot reviewed here is

```text
4b29c692dd1fc96859491b25d61c9b0e1124a33cf57a45ef01abb5a2e49ed30d  HYBRID_CORRELATION_SHARPENING.md
a620937acd6770f622fc799fe28e5dcd6f0ebf072e395bc16d81220e1c02fc30  check_hybrid_correlation.py
34118932b873f5f08fcd81b640882344a564e2d39efd8451ec18c390b0e69fe0  RETAINED_SPINE_JOINT_OPTIMIZED_CERTIFICATE.md
f9fc324c7199cce760f7b59e011e4a2364473b6e9168870eab5f7ff91397e3cb  check_retained_spine_joint_optimized.py
```

The pinned upstream files used by the outer certificate also match:

```text
5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa  RETAINED_SPINE_TRANSFER_ATTEMPT.md
6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db  INDEPENDENT_RETAINED_SPINE_REFEREE.md
8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8  certificate-higher-order-tetradecic-chain-v6.json
4c38c953f2aa541def665467b59dd8e05d8ea6a32f4e5f5b19f7ddf556e373c8  check_retained_spine_optimized.py
```

I independently downloaded the official Yang--Mao v1 TeX source from
`https://export.arxiv.org/e-print/2608.01962v1`. Its `main.tex` has SHA-256

```text
155b7104ec5b6935a576ae9f2b161976a966b0b46bd2b69153c0934ca688da2a  main.tex
```

which agrees with the author pin. The interfaces used here occur at source
lines 370--417 (positive tensor moments), 428--568 (root filters), 687--791
(separator factorization and growth), 795--971 (moment/tail contradiction),
989--1009 (the arbitrary-parameter definition of
$\mathcal G_r^{(d)}(\beta,C)$), and 1146--1190 (the parameterized book
theorem).

The independent replay file is
`independent_check_retained_spine_joint_optimized.py`, SHA-256

```text
830f9133b16abecf01fb879109c50bf4acfd8b93c7a87313626e08b197dc32d4
```

It imports neither author checker. It reconstructs $U,U',U''$ using a
different Horner representation, uses 512-bit rather than 384-bit Arb,
quadruples the finite correlation partition, refines the concavity
partition, and checks the fragile page derivatives cellwise. I read the
implementation before running it; thus the verdict does not treat a printed
`PASS` as self-authenticating evidence.

## Dependency map

1. (R1) uses the exact cubic root-filter identities, one finite Arb
   monotonicity proof, one analytic half-line proof, the Yang--Mao positive
   tensor-moment lemma, and the tail-integration argument defining
   $\mathcal G_2^{(3)}$.
2. The direct branch of (R2) uses strict concavity of the frozen rate $U$.
3. The exceptional wedge uses endpoint reductions for both page branches and
   monotonicity of the reservoir branch.
4. The numerical base uses an outward-rounded enclosure of
   $\exp(U(1)-\Delta)$ with $\Delta=3.355\cdot10^{-6}$.
5. Turning the variational inequality into a Ramsey theorem uses the already
   refereed retained-spine transfer and its declared Yang--Mao and local
   $P_6$/BookCor dependencies.

## Review of the hybrid correlation proof

### 1. Exact cubic ratio and its derivative

Let

$$
u_0=\frac{619}{250},\qquad a=e^{-u_0},\qquad
T=\frac{1001}{500}.
$$

For

$$
P(u)=E(u^3),\qquad N(u)=E(-u^3),
$$

the displayed cubic root filters and both displayed derivatives in the
author note are correct. If

$$
R(u)=\frac{1+aP(u)^2}{1+aN(u)^2},
$$

then direct differentiation gives

$$
R'(u)=\frac{2a}{(1+aN(u)^2)^2}
\left[P P'(1+aN^2)-N N'(1+aP^2)\right].
$$

Thus the checker quantity

$$
W=P P'(1+aN^2)-N N'(1+aP^2)
$$

has exactly the sign of $R'$. There is no missing denominator, factor, or
sign.

The independent replay used $16{,}384$ rational cells on
$[619/250,29/10]$, versus $4{,}096$ in the author checker. Every outward
interval for $W$ was positive. It also independently obtained

$$
R(u_0)-T
=0.0002005988217396235052348499865\ldots>0.
$$

Consequently $R(u)>T$ on the complete finite interval, not merely at sampled
points.

### 2. Analytic tail

The elementary envelopes

$$
P(u)\ge \frac{e^u-2e^{-u/2}}3,
\qquad
|N(u)|\le \frac{2e^{u/2}+e^{-u}}3
$$

are valid. The first right-hand side is positive for $u\ge2.9$, so squaring
its lower bound is legitimate.

Expanding the desired cross-multiplied inequality produces exactly

$$
B_T(u)=e^{2u}-4Te^u-4e^{u/2}-4Te^{-u/2}
       +4e^{-u}-Te^{-2u}.
$$

Writing

$$
D(u)=2e^u(e^u-2T)-2e^{u/2}-4e^{-u},
$$

direct differentiation gives

$$
B_T'(u)-D(u)=2Te^{-u/2}+2Te^{-2u}>0
$$

and

$$
D'(u)=4e^{2u}-4Te^u-e^{u/2}+4e^{-u}>0
\qquad (u\ge2.9).
$$

The last sign follows from $e^u>18$: the term
$e^u(4e^u-4T)$ already dominates $e^{u/2}$. The independent 512-bit replay
gave

$$
D(2.9)>506.3142417902340,
\qquad D'(2.9)>1171.6166618851513,
$$

and a positive cross-multiplied endpoint slack greater than $0.5492$.
Therefore the analytic proof covers the entire half-line $[2.9,\infty)$.

### 3. Separator and growth constant

The ratio bound gives, for $y\ge u_0^3$,

$$
\frac{G(-y)}{H(-y)}< -\frac12-\sigma,
\qquad \sigma=\frac1{1000}.
$$

Every other coordinate satisfies $G/H\le1/2$. Hence if either normalized
coordinate is below $-1$, the two ratios sum to less than $-\sigma$.
Because $H(x)=1+aE(x)^2\ge1$, multiplying by $H(x_1)H(x_2)$ preserves the
needed strict upper bound

$$
F(x_1,x_2)<-\sigma.
$$

This uses the stronger fact $H\ge1$, not only positivity.

On the good event, the one-variable estimate

$$
H(LA)\le2\exp\!\left(2u_0(A+1)^{1/3}\right)
\qquad(A\ge-1)
$$

is valid separately on $[-1,0]$ and $[0,\infty)$. The factorization of $F$
then yields the correct constants

$$
D_2=4,\qquad c=4u_0=\frac{1238}{125}.
$$

### 4. Moment inequality and tail integration

The Taylor coefficients of $F$ are nonnegative, so the positive tensor-
moment lemma gives $\mathbb EF(LZ_1,LZ_2)\ge0$. With

$$
\mathcal E=\{Z_1,Z_2\ge-1\},
$$

the separator and growth bounds give exactly

$$
4\,\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
\ge \sigma(1-\mathbb P(\mathcal E)).
\tag{1}
$$

Failure of $\mathcal G_2^{(3)}(\beta,C)$ at threshold $-1$ implies
$\mathbb P(\mathcal E)<\beta$. For $u\ge0$, failure at
$\lambda=u^3-1$ and the union bound give

$$
\mathbb P(\mathcal E\cap\{Y\ge u\})<2\beta e^{-Cu}.
$$

Tonelli's identity therefore yields, for $C=(1+\varepsilon)c$,

$$
\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
<\beta\left(1+\frac{2c}{C-c}\right)
=\beta\left(1+\frac2\varepsilon\right).
\tag{2}
$$

No factor of $c$, $2$, or $4$ is missing. For the exact constants

$$
\beta=\frac1{4000000},\qquad
\varepsilon=\frac{21}{10000},\qquad
C=\frac{6202999}{625000},
$$

the cost-credit difference is

$$
\sigma(1-\beta)-4\beta\left(1+\frac2\varepsilon\right)
=\frac{3915979}{84000000000}>0.
$$

Equations (1) and (2) contradict one another under failure, proving (R1).
Yang--Mao v1 defines $\mathcal G_r^{(d)}(\beta,C)$ for arbitrary
$0<\beta\le1$ and $C>0$, and its book theorem assumes precisely that
parameterized property. Thus the new pair is admissible; the printed
Yang--Mao constants are not silently reintroduced.

## Review of the joint retained-spine enclosure

### 1. Gates and complete wedge

For the exact tuple

$$
(\eta,p,\delta,\lambda_0,\tau,\Delta)
=(0.028688,0.471310,0.0000525,13580,0.000665,
0.000003355),
$$

all book gates are strict. In particular,

$$
\frac12-\eta-p=2\cdot10^{-6},
\qquad
\tau\left(\frac12-\eta-p\right)=1.33\cdot10^{-9}.
$$

The independent checker reconstructs the fourteen exact decimal $P_6$
coefficients and proves $U''<0$ on all of $(0,1]$: it uses an analytic
near-zero pole bound and $65{,}536$ closed Arb cells for the remainder.

Put

$$
A=U(1)-2c_\eta,\qquad E=U'(1)-c_\eta.
$$

The independent enclosures give

$$
A=0.0001828084586877061976\ldots,
\qquad
E=0.1009763923728286672\ldots,
\qquad 0<A<E.
$$

For $0\le x\le y$, concavity gives the direct-branch gain

$$
G(x,y)=xA+(y-x)E.
$$

Outside $G\le\Delta$, the direct branch is already at most
$U(1)-\Delta$. The complement is exactly the triangle

$$
0\le x\le y,\qquad y\le h(x)
=\frac\Delta E+\left(1-\frac AE\right)x,
$$

with vertices

$$
(0,0),\quad(0,r_{\rm axis}),\quad
(r_{\rm diag},r_{\rm diag}),
$$

where

$$
r_{\rm axis}=\frac\Delta E
=0.0000332255878939757359\ldots,
$$

$$
r_{\rm diag}=\frac\Delta A
=0.0183525424593803138\ldots.
$$

The ordering $r_{\rm axis}<\tau<r_{\rm diag}$ is strict. It both proves
complete wedge coverage and fixes which homogeneous-rate coordinate is
larger in each page formula.

### 2. Red page

On the triangle the red page is

$$
P_R(x,y)=c_\eta(x+y)+\tau q
+(1-y)U\!\left(\frac{1-\tau-x}{1-y}\right).
$$

Its derivatives are exactly

$$
\partial_xP_R=c_\eta-U'(z),
\qquad
\partial_yP_R=c_\eta-U(z)+zU'(z).
$$

The ratio $z$ lies between its diagonal and axis endpoint values. Concavity
makes the first derivative negative and the second positive at the needed
extrema. The independent checker then covers the mixed derivative

$$
\partial_xP_R+h'(x)\partial_yP_R
$$

with $8{,}192$ Arb cells and proves it negative everywhere. Thus $P_R$ is
maximized at $(0,r_{\rm axis})$, with certified target margin

$$
U(1)-\Delta-P_R(0,r_{\rm axis})
=1.2044882603435507\cdot10^{-8}\ldots>10^{-9}.
$$

### 3. Blue page

The blue page is

$$
P_B(x,y)=c_\eta(x+y)+\tau q
+(1-x)U\!\left(\frac{1-y-\tau}{1-x}\right).
$$

Its $y$ derivative is negative, so the maximum first reduces to $y=x$.
The resulting diagonal derivative is

$$
2c_\eta-U(w)-\frac\tau{1-x}U'(w),
\qquad
w=1-\frac\tau{1-x}.
$$

The independent replay covers $0\le x\le r_{\rm diag}$ with $16{,}384$
Arb cells and proves this derivative negative. Therefore the blue page is
maximized at $(0,0)$, with margin

$$
U(1)-\Delta-P_B(0,0)
=3.3687609019302810\cdot10^{-6}\ldots>10^{-9}.
$$

### 4. Reservoir and symmetry

The reservoir branch is coordinatewise increasing. On $y=h(x)$, the
derivative of $x+y$ is $2-A/E>0$, so the diagonal endpoint is its exact
maximum over the wedge. The certified margin is

$$
U(1)-\Delta-2c_\eta r_{\rm diag}-2\tau\Xi
=0.0007801641511624468\ldots>10^{-9}.
$$

Swapping $x$ and $y$ exchanges the two page branches and leaves their
maximum invariant. Hence the ordered-wedge proof covers the full square
$[0,1]^2$.

### 5. Safe decimal

The independent 512-bit enclosure gives

$$
\exp(U(1)-\Delta)
=3.7806857435741762369715660858\ldots
<3.780685745.
$$

The outward-rounded decimal margin is

$$
3.780685745-\exp(U(1)-\Delta)
=1.4258237630284339\cdot10^{-9}\ldots>10^{-9}.
$$

Thus the safe decimal is rounded in the correct direction. The full wedge,
not a floating sample, is covered.

## Independent replay result

Using Python 3.11.15, `python-flint==0.9.0`, and 512-bit precision, the
independent checker returned `PASS`. Proof-critical lower margins included

```text
hybrid endpoint ratio slack:        2.005988217396235e-4
hybrid tail cost-credit slack:      3915979/84000000000
degree slack after tau:              1.330000000000000e-9
red page target margin:              1.204488260343551e-8
blue page target margin:             3.368760901930281e-6
reservoir target margin:             7.801641511624468e-4
safe-decimal rounding margin:        1.425823763028434e-9
```

A separate floating global diagnostic located the apparent branch crossing
near the red axis and gave a slightly larger empirical exponent gain of
about $3.3611\cdot10^{-6}$. This diagnostic is not used in the proof; it is
only a consistency check on the certified value $3.355\cdot10^{-6}$.

## Result-to-claim gate

- `claim_supported`: **yes**, for the exact conditional claims (R1) and
  (R2).
- `what_results_support`: the new parameterized correlation property and the
  complete-square asymptotic upper bound with safe base $3.780685745$.
- `what_results_dont_support`: an unconditional removal of the pinned
  $P_6$/BookCor/Yang--Mao boundary, any explicit finite-$k$ inequality, a
  best-known/world-record statement, priority, or parameter optimality.
- `missing_evidence`: none for promoting the exact conditional asymptotic
  claim; a full independent audit or formalization of every upstream theorem
  would be required to remove the dependency qualifier.
- `suggested_claim_revision`: no mathematical revision. Preserve the words
  “conditional on the pinned dependencies” and “asymptotic.”
- `next_experiments_needed`: none for this promotion gate. Further parameter
  search is optional and would require a fresh frozen certificate and
  referee replay.
- `confidence`: **high** within the declared trust boundary.

## Approved wording

> Conditional on the Yang--Mao v1 regularization and parameterized book
> theorem, and on the pinned local $P_6$/BookCor retained-spine chain, a
> computer-assisted Arb proof establishes
> $R(k,k)\le(3.780685745)^{k+o(k)}$.

No stronger scope statement is approved by this report.
