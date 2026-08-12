# Independent adversarial referee: optimized retained-spine certificate

Date: 2026-08-12  
Role: independent review of the optimized parameter transfer and numerical
enclosure

## Verdict

```text
new exact Yang--Mao parameter tuple:              PASS
parameter-generic retained-spine transfer:        PASS
weighted-wedge cover of the complete square:      PASS
384-bit author checker, run unchanged:            PASS
448-bit replay checker, run unchanged:             PASS
512-bit different-evaluator referee replay:        PASS
C_* two-sided numerical bracket:                  PROVABLE AS STATED
terminating-decimal Ramsey base 3.780695781309:    PROVABLE AS STATED
minor documentation corrections:                  RESOLVED
finite-k threshold / global parameter optimum:    NOT CLAIMED
```

I found no uncovered region, reversed max/min, missing page branch, failed
source gate, interval-containment error, or downward-rounded published
decimal.  Conditional on the same two earliest inputs as the already
refereed transfer theorem--the Yang--Mao v1 combinatorial theorems and the
frozen uniform local $P_6$ off-diagonal rate--I approve

$$
 U(1)-0.000000714\le C_*\le U(1)-0.0000007
$$

and consequently

$$
 \boxed{R(k,k)\le(3.780695781309)^{k+o(k)}.}
$$

The first inequality is only a lower bracket on the variational constant
$C_*$ for this fixed parameter tuple.  It is not a lower bound on a Ramsey
number.

The reviewed primary certificate now resolves the three minor documentation
points identified in the first review, without changing a formula, constant,
or checker:

1. the $P_B$ derivative argument now explicitly invokes concavity to move
   from its own page ratio to the checked upper ratio endpoint;
2. the 448-bit script is now described as a high-precision replay, not as an
   implementation-independent program;
3. the two missing-backslash TeX typos are fixed.

## Reviewed snapshot

```text
c20c3988954e152baae4794462cf15752d6fea8c3555bb9b92140dff6e7aa353  RETAINED_SPINE_OPTIMIZED_CERTIFICATE.md
4c38c953f2aa541def665467b59dd8e05d8ea6a32f4e5f5b19f7ddf556e373c8  check_retained_spine_optimized.py
c3f868f781bed699ff8b1b09e688cdb7efaafc5276f66527526195998653914a  independent_check_retained_spine_optimized.py
5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa  RETAINED_SPINE_TRANSFER_ATTEMPT.md
6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db  INDEPENDENT_RETAINED_SPINE_REFEREE.md
b10815b10cb3ab922aa079ee74289c52239ec90939ed41b93907bf06a60ee274  check_retained_spine_transfer.py
8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8  certificate-higher-order-tetradecic-chain-v6.json
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
2f142a9371d29f07ffd68253c7dbb0981fe440f7f0b8284b4a81430f38395dbc  INDEPENDENT_PROOF_REPLAY.md
2881e8b1df310b449d0bffff5715b9176d9c191ba2a5d05bb376ab2843c58ccd  STAGE6_SEARCH.md
2bb40e6dc4f83203998adad57a0e922565bc8f6f07e1bdc810dd3ebfea481f5d  INDEPENDENT_STAGE6_REFEREE.md
```

The two supplied optimized scripts were run from the repository root with
`python-flint==0.9.0`; each checked the displayed upstream hashes before doing
numerics.

## Earliest dependency boundary

This review begins from two pinned, previously reviewed roots.

1. **External combinatorics.**  Yang--Mao
   [arXiv:2608.01962v1](https://arxiv.org/abs/2608.01962v1) supplies the
   regularization, correlation, parameterized book, and spine-compatibility
   theorems.  The prior independent transfer referee checked those statements
   against a `main.tex` snapshot of SHA-256
   `155b7104ec5b6935a576ae9f2b161976a966b0b46bd2b69153c0934ca688da2`.
   I rechecked the specialization and every parameter use in the transfer,
   but I do not re-prove those source theorems.
2. **Local off-diagonal input.**  The frozen $P_6$ package supplies, uniformly
   for the coloring-dependent pair of residual clique parameters,

   $$
   \log R(k,\ell)\le kU(\ell/k)+o(k).
   $$

   I checked the exact coefficient payload, its homogeneous use, and the new
   calculations below.  I do not re-prove the full six-stage combinatorial
   descent in this report.

Thus the earliest unproved assumptions here are not the optimized wedge
calculation.  They are the two imported roots above, together with Arb's
containment semantics.  No external peer review or proof-assistant
formalization is claimed.

## Re-instantiating the transfer with the new tuple

The transfer note displays one older fixed tuple, so I specifically checked
that its proof is parameter-generic rather than silently assuming those old
numbers.  Interpret the new decimals exactly:

$$
 \eta=0.02863,\quad p=0.47136,\quad \delta=0.000074,
 \quad\lambda_0=12000,\quad\tau=0.0001473.
$$

The source gates reconstructed in the pinned transfer referee are

$$
0<p<\frac12-\eta,\qquad
0<\delta\le\min\{p/4,1/4\},
$$

$$
\lambda_0\ge\max\{2,6\log(1/\delta)\},\qquad \tau>0.
$$

The exact Arb margins include

```text
(1/2-eta)-p:                     0.00001
p/4-delta:                       0.117766
1/4-delta:                       0.249926
lambda_0-6 log(1/delta):         11942.9313272114393...
```

For $r=2,d=3$, the constants $\beta=1/48$, $C=8\log432$, and
$\rho=\log96$ do not depend on the five optimized parameters.  Reconstructing
$\Pi,q,\Xi$ from the source formulas gives

```text
Pi:                              0.0040479142955607872...
q=log(1/p)+Pi:                   0.7561810600034323901...
Xi:                              4465.5327180751052174...
U'(1)-q:                         0.0096583090510489601... > 0
U(1)-2 tau Xi:                   0.0143628230770670752... > 0
```

The transfer proof uses no old decimal after these substitutions.  The
strict degree gap $1/2-\eta-p=10^{-5}$ absorbs the regularization theorem's
additive `-1`, because the book-reservoir condition makes $|W|$
exponential.  Since $\tau>0$ is fixed,
$t=\lfloor\tau k\rfloor$ eventually satisfies
$t\ge\lambda_0\delta^{-1/2}$.  The definitions of $\Pi$, $q$, and $\Xi$
then give exactly the two size hypotheses used by the parameterized book
theorem.  Hence the already reviewed branch proof transfers to this new
fixed tuple without a hidden use of the older parameter values.

## Complete weighted-wedge cover

Write $x=\sigma_R$, $y=\sigma_B$, and use symmetry to assume
$0\le x\le y\le1$.  Let

$$
c=\log\frac2{1+\eta},\qquad
A=U(1)-2c,\qquad E=U'(1)-c.
$$

The exact values are

```text
A: 0.0000700402818373292189949073451782... > 0
E: 0.1009200082844034787504667257145563... > A
```

Put $a=1-x\ge b=1-y$.  For $a>0$, concavity and the tangent at one give

$$
aU(b/a)\le aU(1)-(a-b)U'(1).
$$

Substitution into the homogeneous direct branch yields

$$
 U(1)-D(x,y)\ge xA+(y-x)E=:G(x,y).
\tag{1}
$$

At the only excluded ordered endpoint, $(x,y)=(1,1)$, equation (1) holds by
direct evaluation, with both sides equal to $A$.  Axial residual endpoints
follow directly or by continuity.  Therefore (1) covers the complete closed
ordered triangle.

Set $\Delta=7\cdot10^{-7}$.  If $G\ge\Delta$, the direct branch is already
at most $U(1)-\Delta$.  On the complementary closed wedge $G\le\Delta$,

$$
r_d=\frac\Delta A
 =0.00999424876138808595\ldots,
\qquad
r_a=\frac\Delta E
 =0.000006936186509491006\ldots,
$$

and

$$
0\le x\le r_d,\qquad
0\le y-x\le r_a,\qquad
y\le h(x)=r_a+x\left(1-\frac AE\right)\le r_d.
\tag{2}
$$

The certified inequalities

$$
r_a<\tau,\qquad r_d+\tau<1,\qquad
0<1-A/E<1
$$

ensure that neither positive-part operation is active and fix the larger
homogeneous coordinate on each page.  Equations (1)--(2), their common
boundary $G=\Delta$, and the symmetric ordered triangle cover all of
$[0,1]^2$.

## First page branch $P_R$

On the wedge,

$$
P_R(x,y)=c(x+y)+\tau q+(1-y)U(z),
\qquad z=\frac{1-\tau-x}{1-y}.
$$

The exact ratio range is contained in

$$
1-\frac\tau{1-r_d}\le z\le
\frac{1-\tau}{1-r_a}<1.
$$

Differentiating gives

$$
P_{R,x}=c-U'(z),\qquad
P_{R,y}=c-U(z)+zU'(z).
$$

Both supplied checkers prove $P_{R,x}<0<P_{R,y}$ on this full interval.
For fixed $x$, the maximum is consequently at $y=h(x)$.  Along that edge,

$$
\frac d{dx}P_R(x,h(x))
=P_{R,x}+\left(1-\frac AE\right)P_{R,y}<0.
$$

Thus $P_R$ is maximized at $(0,r_a)$.  The author enclosure is

$$
U(1)-\Delta-P_R(0,r_a)
=2.6716427596396848\ldots\times10^{-8}>0.
\tag{3}
$$

For an evaluator-independent check, I used the frozen power-sum polynomial
implementation in `verify_region_direct_arb.py`, rather than the optimized
scripts' Horner evaluator, at 512-bit precision.  Subdividing the sloping
edge into 8,192 closed $x$-intervals gave the rigorous worst upper endpoint

```text
d/dx P_R(x,h(x)) <= -8.9093325956901163...e-5 < 0.
```

This replay also reproduced (3).

## Second page branch $P_B$

The other page is

$$
P_B(x,y)=c(x+y)+\tau q+(1-x)U(w),
\qquad w=\frac{1-y-\tau}{1-x}.
$$

Here

$$
\partial_yP_B=c-U'(w).
$$

The corrected primary note now records the required monotonic bridge: $w$ is
not literally the same ratio as the preceding $z$, but on $x\le y$,

$$
0<w\le1-\tau<\frac{1-\tau}{1-r_a}=:z_+.
$$

Global strict concavity makes $U'$ decreasing, so

$$
c-U'(w)\le c-U'(z_+)<0.
\tag{4}
$$

The independent 512-bit power-sum evaluation gives the right side of (4)
at most

```text
-0.1009707595657702177... < 0.
```

Consequently $P_B(x,y)\le P_B(x,x)$.  On the diagonal,

$$
\frac d{dx}P_B(x,x)
=2c-U\left(1-\frac\tau{1-x}\right)
-\frac\tau{1-x}U'\left(1-\frac\tau{1-x}\right).
$$

The supplied broad-interval proof gives an upper endpoint below
$-6.7216175\cdot10^{-5}$.  My different evaluator, with 8,192 closed
$x$-cells, gives the independent upper endpoint

```text
-7.0043725439307204...e-5 < 0.
```

Therefore the branch maximum is $P_B(0,0)$, and

$$
U(1)-\Delta-P_B(0,0)
=7.2659130694402019\ldots\times10^{-7}>0.
\tag{5}
$$

## Reservoir branch and the max/min logic

The reservoir rate

$$
Q(x,y)=c(x+y)+2\tau\Xi
$$

is coordinatewise increasing.  The wedge lies inside
$[0,r_d]^2$, so the intentionally loose square-corner estimate gives

$$
U(1)-\Delta-Q(r_d,r_d)
=0.0010713840814684579\ldots>0.
\tag{6}
$$

The book theorem may choose either color and requires both its page-size and
reservoir-size hypotheses.  Therefore the correct operation is

$$
B=\max\{P_R,P_B,Q\}.
$$

Equations (3), (5), and (6) bound this maximum throughout the weighted
wedge.  Equation (1) bounds $D$ on its complement.  Hence every point has

$$
\min\{D,B\}\le U(1)-\Delta,
$$

and maximizing over the square proves
$C_*\le U(1)-7\cdot10^{-7}$.

## Axis witness and the lower bracket on $C_*$

At the exact rational-decimal point

$$
(x,y)=(0,0.000007069),
$$

the direct branch and the first page branch satisfy

```text
D-(U(1)-0.000000714):      5.8742850169842469...e-10 > 0
P_R-(U(1)-0.000000714):    6.8454546509923354...e-10 > 0
```

Since $B\ge P_R$, both entries of $\min\{D,B\}$ exceed the target at this
one point.  Thus

$$
C_*\ge U(1)-0.000000714.
$$

This argument neither constructs a graph nor supplies any Ramsey lower
bound; it only shows that the proved upper enclosure is within
$1.4\cdot10^{-8}$ in exponent of the variational maximum for this tuple.

## Arb containment and decimal rounding

The author checker passed unchanged at 384 bits.  The supplied replay passed
unchanged at 448 bits, with a different near-zero concavity split and twice
as many concavity cells.  A source diff shows that the latter otherwise uses
the same formulas and control flow.  It is therefore fair evidence against
precision and partition accidents, but should not be described as a fully
independent implementation.

To address that limitation, the 512-bit referee replay used the older pinned
power-sum evaluator, whose polynomial, first-derivative, and second-derivative
implementations differ from the optimized Horner code.  It independently
proved global concavity, every scalar gate, both page reductions, the
reservoir bound, and both witness margins.  All comparisons were Arb interval
comparisons; printed midpoints were not used as proof.

Finally, the exact exponent endpoint is

$$
U(1)-7\cdot10^{-7}
=1.3299080618219930723187812632\ldots,
$$

and the 512-bit enclosure gives

$$
\exp(U(1)-7\cdot10^{-7})
=3.7806957813081505123639726847\ldots.
$$

The exact terminating decimal `3.780695781309` exceeds this Arb ball by

$$
8.4948763602731522\ldots\times10^{-13}>0.
$$

Thus the reported base is rounded upward, not truncated downward.

## Approved claim boundary

I approve the conditional computer-assisted asymptotic claim

$$
R(k,k)\le(3.780695781309)^{k+o(k)}
$$

for the exact displayed tuple and the pinned $P_6$/Yang--Mao v1 dependency
boundary.  I do not approve an explicit finite-$k$ threshold, a statement
that the five-dimensional parameter choice is globally optimal, a novelty or
priority claim, unconditional reliance on a later Yang--Mao version, or a
claim of formal verification.
