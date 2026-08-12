# Independent referee report: third sextic descent stage

Date: 2026-08-12

## Verdict

**YES.**  The third exact-linked certificate passes the stated local
computer-assisted proof framework.  I found no new gap in the handoff from
the already certified second quintic, the continuous numerical inequalities,
or the candidate-specific descent hypotheses.

In the proof-writer classification, the precise conditional claim below is

```text
PROVABLE AS STATED
```

The word “conditional” is essential: the earliest unclosed dependency is the
imported GNNW Lemma 11 together with the locally repaired BookCor replay, and
the numerical proof also trusts Arb's documented enclosure semantics.  This
report does not promote that imported dependency to a proof from first
principles.

## Exact claim reviewed

For

$$
F_3(\lambda)=H(\lambda)+P_3(\lambda)e^{-\lambda},
\qquad
H(\lambda)=(1+\lambda)\log(1+\lambda)-\lambda\log\lambda,
$$

where

$$
\begin{aligned}
P_3(\lambda)={}&-0.250000000000000\lambda
-0.003330465213687\lambda^2
+0.091728978292451\lambda^3\\
&+0.040555948334794\lambda^4
-0.053458127305523\lambda^5
+0.021783259992867\lambda^6,
\end{aligned}
$$

the three-stage exact-linked descent proves, within the inherited framework,

$$
\log R(k,\ell)\le kF_3(\ell/k)+o(k)
$$

uniformly for positive integers $1\leq\ell\leq k$.  In particular,

$$
R(k,k)\leq
\left(3.7814656158401685107275297311637231\ldots\right)^{k+o(k)}.
$$

This is a local conditional asymptotic theorem.  It is not an explicit
finite-$k$ bound, an externally peer-reviewed theorem, a formal-assistant
proof, or evidence for any fourth descent stage.

## Inputs and frozen hashes

The reviewed third-stage proof input is
`certificate-higher-order-sextic-chain-v3.json`:

```text
2052952c3af98074d5442fb736c7a2952146e92051a43fab84e75f099d9e00d7
```

Its inherited exact-link predecessors are:

```text
2664bc421cd0cb7489289caa283a3a3f22830580f7c21bf0e6cbe092910bc277  certificate-higher-order-quintic-v1.json
b5b595b4dcc9d1bdc2b5714f68fef99ec1c566bbd612d35ca19100d173d41c4d  certificate-higher-order-quintic-chain-v2.json
```

The reviewed constructor and verifier hashes are:

```text
281a3f41d8e5347fdf54aa89e3e1b96f5e6c7e1ba51a715f7107b123206ef8d6  search_chained_target.py
6c4ca964a8fc98eff5bb19a74caa00f7f7628fbd8bc6fe4d8fabb67456124b1b  generate_higher_order_certificate.py
879ce15f4518f1d6737fdbba09d04f7433c96c4c3d81efcd3c666a35fdaae981  verify_arb.py
f4e2c8663022a82ed22c41677e71d4b609b0a9eace1770c56deb12351faf3494  verify_chain_arb.py
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
b0d4f0cb94bb816ca3342e6076dd8223d1003e661757481442fe166eb2330bfe  audit_tests.py
```

These values agree with the current frozen verification log.

## Dependency map

1. The elementary witness proves the initial cubic rate $F_0$.
2. The first two already reviewed exact-linked certificates prove $F_1$ and
   $F_2$ as uniform one-sided Ramsey rates.
3. The third JSON prior must be the exact $F_2$ coefficient tuple.
4. Strict concavity of $F_2$ reduces both continuous Ramsey-region
   inequalities to certified one-dimensional extrema.
5. The third target must satisfy $F_3>0$, $F_3'>0$, the strict main
   inequality, valid witness ranges, and both strict region orientations on
   the whole large regime.
6. The elementary witness must prove the same target conditions on the whole
   open small-$\lambda$ regime, not merely at sampled points.
7. The repaired finite-net descent invokes BookCor at finitely many points.
   Its combinatorial validity inherits the audited GNNW Lemma 11 / BookCor
   dependency.
8. Substitution of $\lambda=1$ gives the stated diagonal base.

## Independent checks

### 1. Exact handoff and continuous coverage

The third certificate's `prior_coefficients` strings are literally the second
certificate's `target_coefficients` strings:

```text
-0.25, -0.008578629273557, 0.127585140806616,
-0.029829210000000, 0.010085181421050
```

`verify_chain_arb.py` additionally parses both lists as Python `Decimal`
tuples and rejects numerical inequality.  Thus the handoff is exact rational
decimal equality, not a binary-floating tolerance check.  The different but
equal spelling `-0.250000000000000` occurs only as the new target's linear
coefficient and creates no handoff ambiguity.

I separately parsed all endpoints as `Decimal`.  The third file has 65,536
positive-width cells; every left endpoint equals the preceding right endpoint,
the first begins at the certificate's exact split
`0.0050000000000000001`, and the final endpoint is exactly `1`.  The analytic
small-regime proof uses that same exact split, so there is neither a gap nor an
overlap.  The shorthand `[0.005,1]` in prose is not the literal stored
decimal, but this is only an archival wording issue.

The stored large-regime witness ranges are

```text
0.0076143579747633217 <= M <= 0.39142102191105949
0.017896261500108514  <= Y <= 0.82101363757449441.
```

They give $0<M,Y<1$ and, in particular, a compact-uniform separation of $M$
from $1$.

### 2. Search/proof separation

`search_chained_target.py` is correctly labelled as a floating-point
constructor.  Its coefficient basis for $F$ and $F'$ is algebraically
correct, its first coefficient is frozen, and minimizing the sum of the
remaining coefficient changes minimizes $F(1)$ at fixed linear coefficient.
Its finite-difference linear program and dense interpolated prior envelopes
have no proof status.

`generate_higher_order_certificate.py` likewise uses interpolation and scalar
optimization only to propose exact-decimal piecewise witnesses.  Neither Arb
verifier imports its envelope table or trusts its predicted slack.  Therefore
an optimizer or interpolation error could make certificate construction fail,
but could not cause an invalid certificate to pass the reviewed proof checks.

### 3. Prior concavity

The primary verifier proves the third-stage prior $F_2$ is strictly concave
on all of $(0,1]$.  Its worst certified upper bound for $F_2''$ is

```text
-0.37169086755178266.
```

The separately implemented direct-region checker uses a different small
cutoff and 8,192-cell subdivision and obtains

```text
-0.37184261548417713.
```

Both are strictly negative.  This validates monotonicity of
$A(\mu)=F_2(\mu)-\mu F_2'(\mu)$ and of $F_2'$, including every endpoint case
used by the two envelope reductions.  Concavity of the new target $F_3$ is not
needed unless a later stage attempts to use it as a prior.

### 4. Small-$\lambda$ applicability

The analytic splice applies because $P_3$ is a finite polynomial with no
constant term.  Hence its exact coefficients give finite constants in

$$
|P_3(\lambda)|\le C_0\lambda,
\qquad
|P_3'(\lambda)-P_3(\lambda)|\le C_1.
$$

With $M=\lambda e^{-\lambda}$ and $Y=1-X$, the checker bounds
$e^{-F_3'}$ above and below by positive multiples of $\lambda$, proves
$F_3,F_3'>0$, and cancels the two $\lambda\log\lambda$ terms in the main
inequality.  The certified lower bound on the normalized slack throughout

$$
0<\lambda\leq0.0050000000000000001
$$

is

```text
0.00389035850409367693619901533171038...
```

and is strictly positive.  I checked the inequality directions in the
coefficient argument; in particular the lower bound
$Y\ge M+q-Mq$ is used in the correct direction.

### 5. Large-regime $F$, $F'$, main inequality, and region

The full three-stage chain replay returned `PASS`.  Its third-stage output is:

```text
standard region margin:  (6.960077165064378e-05, cell 6)
swapped region margin:   (7.016617229398231e-05, cell 22533)
large main slack:        (0.00016510787819556342, cell 65535)
```

I also ran a standalone Arb replay of $F_3$, $F_3'$, $X$, and the main
inequality which does not import `verify_arb.py`.  It obtained:

```text
minimum F3 lower bound:       0.03024126810688174
minimum F3' lower bound:      0.7655549970958766
outer X range:                [0.21769798616878688, 0.986013482324779]
worst main slack:             0.00016510787819556342 at cell 65535
```

The agreement of the worst main slack is an additional diagnostic replay;
the standalone command was not saved as a frozen verifier artifact.

The separately written direct-region verifier, which neither imports the
main verifier nor uses its $A(\mu)$ envelope reduction, returned:

```text
PASS: independent direct two-sided Ramsey-region replay
worst standard exponent slack: 9.911774569389889e-07 at cell 0
worst swapped exponent slack:  7.016617229398231e-05 at cell 22533
```

The standard direct margin is small but rigorously positive at 256-bit
precision.  Its location at the first large cell is consistent with the
analytic splice meeting the large certificate at the exact split.

### 6. BookCor conditions

For the large regime, positivity of $F_3'$ gives
$p=1-e^{-F_3'}\in(0,1)$, the stored witness gives
$\mu=M\in(0,1)$ and $Y\in(0,1)$, and both strict exponent inequalities put
$(X,Y)$ in $\mathcal R_*$.  The perturbed BookCor coordinate satisfies

$$
x_{\lambda,\delta}<
(1-M)p^{1/(1-M)}=X,
$$

so it remains in the downward interior.  The strict main inequality gives the
required vertex-count comparison.  Smoothness of $F_3$, the positive compact
lower bound for $F_3'$, and the displayed upper bound for $M$ discharge the
finite-net uniformity hypotheses.

For the small regime, $(X,1-X)$ is in the elementary Ramsey region and the
same strict perturbation $x_{\lambda,\delta}<X$ moves the BookCor point into
the interior.  Thus the third stage introduces no hidden condition such as
$p>M$ and does not invoke the withdrawn Lemma 14 route.

### 7. Base computation

Using independent 80-digit `Decimal` arithmetic and the exact coefficient
sum

```text
-0.152720405899098
```

gives

$$
F_3(1)=2\log2-0.152720405899098/e
$$

and

```text
F3(1)       = 1.3301116635422546032478941580882756863783955342370...
exp(F3(1))  = 3.7814656158401685107275297311637230932250088793904...
```

This agrees with the Arb ball.  Relative to the second-stage base, the third
stage lowers the constant by

```text
0.00275944953468368041646471522330893...
```

## Reproduction results

The exact command using all three certificate files returned:

```text
PASS: verified 3-stage Ramsey-rate certificate chain
```

with the third-stage values recorded above.  The direct third-stage region
command returned:

```text
PASS: independent direct two-sided Ramsey-region replay
```

and all regressions returned:

```text
PASS: derivative sign regression; X base is positive iff F'>0
PASS: arbitrary-degree polynomial derivative regression
PASS: Horizon union-gap test
```

## Earliest gap and claim boundary

I found no gap beginning at the $F_2\to F_3$ handoff.  The earliest place the
overall Ramsey theorem is not closed internally from first principles is
upstream of every numerical stage: GNNW Lemma 11 and the combinatorial input
to the locally repaired BookCor.  Consequently the approved wording is:

> Conditional on the audited GNNW Lemma 11 / repaired BookCor core and Arb's
> enclosure semantics, the three frozen exact-Decimal-linked certificates
> prove
> $R(k,k)\le(3.7814656158401685107\ldots)^{k+o(k)}$.

The following stronger claims are **not** approved:

1. that the result is unconditional with respect to the imported GNNW core;
2. that it has passed external human peer review or formal verification;
3. that it supplies an explicit finite threshold or improves a named finite
   Ramsey number;
4. that arbitrary sextic coefficients are valid merely because the descent
   mechanism is degree independent;
5. that the search output, without the frozen certificate and strict Arb
   replays, has theorem status;
6. that a fourth stage follows without another exact-link certificate.

## Open risks and archive-only issues

- Both persistent numerical checkers ultimately trust the same
  `python-flint`/Arb library.  Their region logic is independent, but a formal
  assistant or a different interval library would reduce common arithmetic
  trust further.
- The direct-region checker persistently verifies only the two region
  inequalities.  I independently replayed the main inequality as a referee
  diagnostic, but that extra script is not a frozen repository artifact.
- The smallest direct standard-region margin is approximately
  $9.91\times10^{-7}$.  It is strictly certified, but future regeneration or
  coefficient rounding must rerun both verifiers rather than relying on the
  printed decimal.
- The exact split is `0.0050000000000000001`; prose that calls it exactly
  `0.005` is shorthand.  The common stored endpoint and analytic coverage
  show this is not a coverage gap.
- The verification log freezes the constructor, certificate, and verifier
  hashes, but it does not freeze the floating search command or optimization
  trace.  That affects provenance/reproducibility of discovery, not validity
  of the checkable theorem artifact.
- Public archival and external combinatorics review remain outstanding.
