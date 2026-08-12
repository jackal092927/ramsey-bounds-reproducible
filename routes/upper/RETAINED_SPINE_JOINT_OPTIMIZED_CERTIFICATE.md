# Jointly optimized retained-spine proof package

Date: 2026-08-12

## Claim

Conditional on the pinned six-stage local off-diagonal rate $U=F_6$, the
repaired BookCor interface, the Yang--Mao regularization and parameterized
book construction, and the hybrid correlation lemma proved in
`HYBRID_CORRELATION_SHARPENING.md`,

$$
R(k,k)
\le \exp\!\left((U(1)-3.355\cdot10^{-6})k+o(k)\right)
\le (3.780685745)^{k+o(k)}.
\tag{1}
$$

The non-rounded base enclosed by the author checker is

$$
3.7806857435741762369\ldots.
\tag{2}
$$

## Status

**PROVABLE AS STATED under the explicit pinned dependencies; AUTHOR
384-BIT ARB CHECKER PASS; pending independent replay.**

The claim survives unchanged under the author checker.  It must remain a
theorem-linked candidate until an implementation-independent checker and a
proof referee replay both pass.

## Assumptions

1. The frozen degree-14 rate $U=F_6$ and its locally proved off-diagonal
   theorem are valid exactly as pinned by SHA-256 in the checker.
2. The repaired BookCor/finite-net descent and the already refereed
   retained-spine max/min transfer are valid at their pinned interfaces.
3. The Yang--Mao regularization and parameterized book construction apply to
   every pair $(\beta,C)$ satisfying their property
   $\mathcal G_2^{(3)}(\beta,C)$.
4. The companion proof and checker establish

   $$
   \mathcal G_2^{(3)}\!\left(\frac1{4000000},
   \frac{6202999}{625000}\right).
   \tag{3}
   $$

5. `python-flint==0.9.0` implements the outward-rounded Arb containment
   semantics used in the numerical proof.

## Notation and exact parameters

The retained-spine tuple consists entirely of exact terminating decimals:

$$
\eta=0.028688,\qquad p=0.471310,\qquad
\delta=0.0000525,
\tag{4}
$$

$$
\lambda_0=13580,\qquad \tau=0.000665,
\qquad \Delta=0.000003355.
\tag{5}
$$

The exact correlation pair is

$$
\beta=\frac1{4000000},\qquad
C=\frac{6202999}{625000}=9.9247984.
\tag{6}
$$

Define

$$
c_\eta=\log\frac2{1+\eta},
\qquad
\Pi=\frac{3\delta}{p}
+\frac{6\log(1/\delta)\log(1/p)}{\lambda_0},
\qquad q=\log(1/p)+\Pi,
\tag{7}
$$

and

$$
\rho=\log(2/\beta),\qquad
\Xi=2\rho+4C\lambda_0^{1/3}
+\frac{12C\log(1/\delta)}{\lambda_0^{2/3}}.
\tag{8}
$$

The author checker encloses

$$
q=0.7558486998027463\ldots,
\qquad
\Xi=980.9935268063087\ldots.
\tag{9}
$$

Finally put

$$
A=U(1)-2c_\eta,
\qquad E=U'(1)-c_\eta.
\tag{10}
$$

Their rigorous enclosures are centered at

$$
A=0.0001828084586877061\ldots,
\qquad E=0.1009763923728286\ldots,
\quad 0<A<E.
\tag{11}
$$

## Proof strategy

Use strict concavity of $U$ to let the direct branch control every point
outside a weighted wedge.  On that entire wedge, use analytic derivative
signs to reduce the two page branches to endpoints and maximize the
reservoir branch at the diagonal endpoint.  Every transcendental inequality
is then enclosed with outward-rounded Arb arithmetic.

## Dependency map

1. Equation (3) depends on the separate hybrid exact/envelope correlation
   proof and its 384-bit finite-interval replay.
2. The direct-branch wedge depends on global strict concavity of $U$, which
   the checker re-proves on all of $(0,1]$.
3. The red page depends on two coordinate derivative signs and one sloping
   boundary derivative sign.
4. The blue page depends on a negative $y$ derivative and a negative
   diagonal derivative.
5. The reservoir branch depends on coordinatewise monotonicity from the
   already reviewed transfer and an exact linear maximization over the
   wedge.
6. The reported decimal depends on the Arb enclosure of
   $\exp(U(1)-\Delta)$ and a strict rounding margin.

## Proof

### Step 1: parameter gates

The exact tuple (4)--(6) satisfies

$$
0<\eta,\qquad
0<p<\frac12-\eta,\qquad
0<\delta\le\min\!\left(\frac p4,\frac14\right),
\tag{12}
$$

$$
\lambda_0\ge2,\qquad
\lambda_0\ge6\log(1/\delta),
\qquad 0<\tau<1.
\tag{13}
$$

The minimum-degree parameter slack is exactly

$$
\frac12-\eta-p=2\cdot10^{-6},
\tag{14}
$$

and its retained form is

$$
\tau\left(\frac12-\eta-p\right)
=1.33\cdot10^{-9}>10^{-9}.
\tag{15}
$$

The checker also proves $q<U'(1)$ and $2\tau\Xi<U(1)$.

### Step 2: complete direct-branch complement

The checker re-proves $U''(z)<0$ on all $0<z\le1$.  Therefore the tangent
gain of the direct branch is

$$
G(x,y)=\min(x,y)A+|x-y|E.
\tag{16}
$$

Where $G(x,y)\ge\Delta$, the direct branch is at most
$U(1)-\Delta$.  By symmetry it remains to control

$$
0\le x\le y,\qquad xA+(y-x)E\le\Delta.
\tag{17}
$$

The intercepts and boundary slope are

$$
r_{\rm axis}=\frac\Delta E
=0.0000332255878939757\ldots,
\tag{18}
$$

$$
r_{\rm diag}=\frac\Delta A
=0.0183525424593803\ldots,
\qquad
s=1-\frac AE\in(0,1).
\tag{19}
$$

The strict ordering

$$
0<r_{\rm axis}<\tau<r_{\rm diag}<1
\tag{20}
$$

holds.  Thus (17) is the complete exceptional wedge, rather than a sampled
rectangle or an incomplete boundary subset.

### Step 3: red-page endpoint reduction

On (17), the red page is

$$
P_R(x,y)=c_\eta(x+y)+\tau q
+(1-y)U\!\left(\frac{1-\tau-x}{1-y}\right).
\tag{21}
$$

The argument of $U$ ranges through the rigorously enclosed interval

$$
1-\frac{\tau}{1-r_{\rm diag}}
\le z\le
\frac{1-\tau}{1-r_{\rm axis}}.
\tag{22}
$$

On this entire interval the author checker proves

$$
\partial_xP_R<0,\qquad \partial_yP_R>0,
\tag{23}
$$

and, on the sloping boundary of (17),

$$
\frac d{dx}P_R(x,h(x))<0.
\tag{24}
$$

The upper endpoints of the two negative derivatives are respectively below
$-0.10113$ and $-0.000126$, while the positive derivative is above
$0.10086$.  Hence the maximum is the axis endpoint
$(0,r_{\rm axis})$.  Direct evaluation there gives

$$
U(1)-\Delta-P_R(0,r_{\rm axis})
>1.2044\cdot10^{-8}>10^{-9}.
\tag{25}
$$

### Step 4: blue-page endpoint reduction

In the same ordered wedge,

$$
P_B(x,y)=c_\eta(x+y)+\tau q
+(1-x)U\!\left(\frac{1-y-\tau}{1-x}\right).
\tag{26}
$$

The checker proves $\partial_yP_B<0$, which first sends the maximum to
$y=x$.  It then proves that the derivative of $P_B(x,x)$ is negative on
$0\le x\le r_{\rm diag}$.  Thus the maximum is at $(0,0)$, where

$$
U(1)-\Delta-P_B(0,0)
>3.3687\cdot10^{-6}>10^{-9}.
\tag{27}
$$

### Step 5: reservoir endpoint reduction

The reservoir cost is coordinatewise increasing.  On the sloping boundary
of (17), the derivative of $x+y$ is $2-A/E>0$, so its maximum is at the
diagonal endpoint.  The resulting cost is

$$
2c_\eta r_{\rm diag}+2\tau\Xi.
\tag{28}
$$

The author checker obtains the strict margin

$$
U(1)-\Delta-2c_\eta r_{\rm diag}-2\tau\Xi
>7.8016\cdot10^{-4}>10^{-9}.
\tag{29}
$$

Together, Steps 2--5 prove that the max/min retained-spine variational
constant is at most $U(1)-\Delta$ on the entire square $[0,1]^2$.

### Step 6: safe decimal

At 384-bit precision with outward rounding, the checker proves

$$
\exp(U(1)-\Delta)
<3.780685743574176237.
\tag{30}
$$

It also proves the exact decimal margin

$$
3.780685745-\exp(U(1)-\Delta)
>1.4258\cdot10^{-9}>10^{-9}.
\tag{31}
$$

Since $3.780685745<3.7806870$, the pre-registered promotion threshold and
all pre-registered critical-margin gates are satisfied.  Equations
(16)--(31), inserted into the already reviewed retained-spine transfer,
prove (1). $\square$

## Corrections or missing assumptions

- No correction to the stated conditional claim is needed.
- Removing any pinned theorem dependency would require re-proving that
  upstream theorem; this package does not silently claim such independence.

## Open risks and claim boundary

- The claim is asymptotic and gives no explicit finite-$k$ threshold.
- It is conditional on the pinned local theorem chain and the external
  Yang--Mao regularization/book construction.
- Arb replay is rigorous interval computation, not proof-assistant
  formalization.
- No global optimality of (4)--(6), publication priority, or globally
  best-known status is claimed.
- Until independent replay, this remains an author-certified candidate and
  should not replace the canonical bound.

## Reproduction

```text
.venv/bin/python routes/upper/check_hybrid_correlation.py
.venv/bin/python routes/upper/check_retained_spine_joint_optimized.py
```
