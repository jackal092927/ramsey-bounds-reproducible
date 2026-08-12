# Retained-spine round-2 bounded-frontier report

Date: 2026-08-12  
Protocol SHA-256:
`367d067753c0db0c8356449dd6d260d62b1b6b9ac2eee473478d17c142c9e6be`

## Claim attempted

With the Yang--Mao constants and the frozen $P_6$ rate unchanged, find one
exact five-parameter tuple

$$
(\eta,p,\delta,\lambda_0,\tau)
$$

for which the already refereed weighted-wedge transfer certifies

$$
C_*\le U(1)-\Delta_2,
\qquad \Delta_2\ge10^{-6},
$$

with every proof-critical strict Arb margin at least $10^{-9}$.

## Status

`NOT CURRENTLY JUSTIFIED`.

The pre-registered target was not reached.  No round-2 theorem, decimal
Ramsey base, or Arb proof certificate is promoted from this search.  The
previously refereed gain $7\cdot10^{-7}$ and its base remain the authoritative
result for the frozen Yang--Mao constants.

## Assumptions and notation

Let

$$
c=\log\frac2{1+\eta},\qquad
A=U(1)-2c,\qquad E=U'(1)-c,
$$

$$
q=\log(1/p)+\frac{3\delta}{p}
 +\frac{6\log(1/\delta)\log(1/p)}{\lambda_0},
$$

and let $\Xi$ be the frozen Yang--Mao reservoir cost used in the existing
certificate.  For a proposed exponent gain $\Delta$, the weighted wedge has
diagonal and axis radii

$$
r_d=\frac\Delta A,\qquad r_a=\frac\Delta E.
$$

The diagnostic search uses ordinary IEEE floating-point arithmetic and
SciPy.  It is not an interval calculation.

## Strategy and dependency map

1. Use necessary scalar gates to bound $\eta$.
2. Relax the strict degree gate to its favourable closure
   $p=1/2-\eta$.
3. For each $(\eta,\delta,\lambda_0,\Delta)$, choose the largest reservoir-
   legal $\tau$, since this is the value most favourable to the red axis
   page.
4. Solve the red-axis page equality for the largest diagnostic $\Delta$.
5. Maximize the resulting three-dimensional frontier with four deterministic
   differential-evolution seeds.

This reduction gives a favourable bounded numerical frontier.  It does not
give a rigorous global upper bound on all source-legal parameters.

## Analytic reductions

### Step 1: the degree parameter is monotone

For fixed $(\eta,\delta,\lambda_0)$,

$$
\frac{\partial q}{\partial p}
=-\frac1p-\frac{3\delta}{p^2}
-\frac{6\log(1/\delta)}{\lambda_0p}<0.
$$

The other proof-critical costs do not depend on $p$.  Consequently the
relaxed boundary $p=1/2-\eta$ is at least as favourable as every legal
$p<1/2-\eta$.  The numerical search is therefore run on that boundary; its
reported $p$ is not itself a legal exact candidate.

The gates $A>0$ and $q<U'(1)$ imply the necessary interval

$$
2e^{-U(1)/2}-1<\eta<\frac12-e^{-U'(1)}.
$$

Numerically this is

$$
0.0285939778632\ldots<\eta<0.0350564920499\ldots.
$$

The search stays $10^{-10}$ inside these endpoints.

### Step 2: the reservoir and page constraints are jointly active

At the diagonal endpoint $(r_d,r_d)$ the reservoir condition is

$$
2cr_d+2\tau\Xi\le U(1)-\Delta.
$$

Since $1+2c/A=U(1)/A$, this gives

$$
\tau\le \tau_{\max}(\Delta)
=\frac{U(1)(1-\Delta/A)}{2\Xi}.
\tag{1}
$$

At the red axis endpoint, the page is

$$
P_R(0,r_a)=cr_a+\tau q
 +(1-r_a)U\!\left(\frac{1-\tau}{1-r_a}\right).
\tag{2}
$$

Its derivative with respect to $\tau$ is

$$
q-U'\!\left(\frac{1-\tau}{1-r_a}\right)<q-U'(1)<0,
$$

where strict concavity and $(1-\tau)/(1-r_a)<1$ are used.  Thus increasing
$\tau$ helps (2), while it hurts the reservoir.  The favourable relaxed
frontier may set (1) to equality and then solve
$P_R(0,r_a)=U(1)-\Delta$.

## Bounded numerical evidence

The deterministic script
`search_retained_spine_round2.py` searched

$$
\begin{aligned}
0.0285939779632&\le\eta\le0.0350564919499,\\
10^{-12}&\le\delta\le0.125,\\
10&\le\lambda_0\le10^9,
\end{aligned}
$$

while enforcing all associated source gates.  The four seeds returned

| seed | relaxed frontier $\Delta$ |
|---:|---:|
| 260801962 | $7.178719323007764\cdot10^{-7}$ |
| 260801963 | $7.178719322866366\cdot10^{-7}$ |
| 260801964 | $7.178719323073725\cdot10^{-7}$ |
| 260801965 | $7.178719323198720\cdot10^{-7}$ |

The best floating-point point was

$$
\begin{aligned}
\eta&=0.028636946766686565,\\
p_{\rm closure}&=0.47136305323331346,\\
\delta&=0.000053616723679132295,\\
\lambda_0&=13312.527771289087,\\
\tau&=0.00014264106040090874,
\end{aligned}
$$

with

$$
\Delta_{\rm float}=7.1787193231987202\cdot10^{-7}.
$$

The red-axis page and diagonal reservoir constraints were simultaneously
active to displayed floating precision.  The optimum was far from the
$\delta$ and $\lambda_0$ box boundaries.  The four frontier values differ by
less than $3.4\cdot10^{-17}$, but this agreement is evidence of numerical
stability, not a proof of global optimality.

The shortfall from the pre-registered threshold is

$$
10^{-6}-\Delta_{\rm float}
=2.8212806768012794\cdot10^{-7}.
$$

At this point $r_a\approx7.11\cdot10^{-6}$.  Replacing the axis tangent by
the exact direct deficit changes that deficit by only about
$9.15\cdot10^{-12}$ at the sampled frontier.  This diagnostic explains why
a more exact treatment of the same tiny wedge is not expected to bridge the
$2.82\cdot10^{-7}$ target shortfall.  It is not an impossibility theorem for
other transfer mechanisms.

## Acceptance decision

The protocol requires $\Delta_2\ge10^{-6}$ before an exact tuple and Arb
proof are generated.  The favourable relaxed finite-box frontier is below
that threshold.  Therefore:

```text
round-2 accepted:                         NO
new fixed-tuple theorem:                  NO
new decimal Ramsey upper base:            NO
old optimized certificate modified:       NO
bounded floating frontier recorded:       YES
```

## Reproduction and integrity

From the project root:

```text
python3 routes/upper/search_retained_spine_round2.py
python3 -m py_compile routes/upper/search_retained_spine_round2.py
```

Artifact hashes at the decision point:

```text
ceeec30f6068303ffc8b21d8d918383d0518db05369c3caa88aadb3ca6c69b8d  search_retained_spine_round2.py
c20c3988954e152baae4794462cf15752d6fea8c3555bb9b92140dff6e7aa353  RETAINED_SPINE_OPTIMIZED_CERTIFICATE.md
4c38c953f2aa541def665467b59dd8e05d8ea6a32f4e5f5b19f7ddf556e373c8  check_retained_spine_optimized.py
c3f868f781bed699ff8b1b09e688cdb7efaafc5276f66527526195998653914a  independent_check_retained_spine_optimized.py
```

## Corrections or missing assumptions

- A global impossibility theorem would require rigorous control outside the
  finite $\delta,\lambda_0$ box and interval verification of the reduced
  optimization.  This report does not claim either.
- A source-level improvement of the Yang--Mao correlation constants would be
  a different theorem input and must not be folded into this frozen-constant
  round after pre-registration.

## Open risks and next mathematical cut

- The diagnostic optimizer and all displayed frontier decimals use binary
  floating point.
- The active diagonal reservoir constraint is exact within the current
  weighted-wedge geometry; improving that bottleneck requires reducing
  $\Xi$, changing the book/correlation input, or replacing the fixed global
  book parameters by a genuinely stronger transfer.
- The red-axis page constraint is the co-active obstruction.  Merely sampling
  more densely in the same five-parameter frozen model is unlikely to be a
  productive next step.
