# Independent adversarial referee report: fourth octic descent stage

Date: 2026-08-12

## Verdict

**PASS WITH IMPORTED DEPENDENCY.**  I found no new gap at the exact
$P_3\to P_4$ handoff, in the continuous fourth-stage certificate, or in the
four-certificate induction.

In the proof-writer classification, the precise *conditional* claim reviewed
below is

```text
PROVABLE AS STATED
```

The qualifier is substantive.  The earliest dependency not re-proved from
first principles in this review remains the imported GNNW Lemma 11 together
with the locally repaired BookCor combinatorial descent.  The numerical proof
also imports Arb's documented enclosure semantics through `python-flint`.

## Exact claim reviewed

Let

$$
H(\lambda)=(1+\lambda)\log(1+\lambda)-\lambda\log\lambda
$$

and

$$
\begin{aligned}
P_4(\lambda)={}&-0.250000000000000\lambda
+0.006788512088209\lambda^2
+0.038835297966515\lambda^3\\
&+0.110380487198675\lambda^4
-0.045883160603885\lambda^5
-0.048420977583689\lambda^6\\
&+0.038460877061037\lambda^7
-0.003292994769736\lambda^8,
\end{aligned}
$$

with $F_4(\lambda)=H(\lambda)+P_4(\lambda)e^{-\lambda}$.  Conditional on the
audited GNNW/BookCor descent used in the preceding three stages, the frozen
four-stage chain proves the corresponding uniform one-sided Ramsey rate and,
at $\lambda=1$,

$$
R(k,k)\leq
\left(3.7808931385024181222517908784987532\ldots\right)^{k+o(k)}.
$$

This is a local conditional asymptotic computer-assisted theorem.  It is not
an explicit finite-$k$ inequality, an externally peer-reviewed theorem, or a
formal-assistant proof.

## Frozen inputs and hashes

The reviewed stage-four proof input is:

```text
09253d757516dc258396f82c09a442aaaf9d499640c1cc99b5767e6d51d35942  certificate-higher-order-octic-chain-v4.json
```

Its exact-link predecessors are:

```text
2664bc421cd0cb7489289caa283a3a3f22830580f7c21bf0e6cbe092910bc277  certificate-higher-order-quintic-v1.json
b5b595b4dcc9d1bdc2b5714f68fef99ec1c566bbd612d35ca19100d173d41c4d  certificate-higher-order-quintic-chain-v2.json
2052952c3af98074d5442fb736c7a2952146e92051a43fab84e75f099d9e00d7  certificate-higher-order-sextic-chain-v3.json
```

The reviewed constructor and checker hashes are:

```text
58a69340dea1378317475aba4c79c6ba529059a87da1df72774c7d48b4961cc4  search_chained_target.py
6c4ca964a8fc98eff5bb19a74caa00f7f7628fbd8bc6fe4d8fabb67456124b1b  generate_higher_order_certificate.py
879ce15f4518f1d6737fdbba09d04f7433c96c4c3d81efcd3c666a35fdaae981  verify_arb.py
f4e2c8663022a82ed22c41677e71d4b609b0a9eace1770c56deb12351faf3494  verify_chain_arb.py
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
b0d4f0cb94bb816ca3342e6076dd8223d1003e661757481442fe166eb2330bfe  audit_tests.py
```

## Dependency map

1. The elementary witness closes the initial cubic prior without using a
   prior numerical certificate.
2. The first three exact-linked certificates prove $F_1,F_2,F_3$ within the
   inherited descent framework.
3. The fourth JSON prior must equal the exact third JSON target, with no
   floating-point tolerance.
4. Strict concavity of $F_3$ must justify both continuous prior-envelope
   reductions.
5. On the large regime, the fourth target must have $F_4,F_4'>0$, valid
   $M,X,Y$ ranges, both strict Ramsey-region orientations, and positive main
   slack on every point, not just on a mesh.
6. A separate analytic argument must cover the whole open interval down to
   $\lambda=0$.
7. The repaired finite-net/BookCor descent converts those strict inequalities
   into the next uniform Ramsey rate; this is where the imported GNNW
   combinatorial dependency enters.
8. Substitution of $\lambda=1$ gives the displayed diagonal base.

## Independent checks

### 1. Exact $P_3\to P_4$ link

The stage-three target and stage-four prior are the same six exact decimal
coefficients, including spelling:

```text
-0.250000000000000, -0.003330465213687,
 0.091728978292451,  0.040555948334794,
-0.053458127305523,  0.021783259992867
```

I compared the JSON lists directly and as arbitrary-precision `Decimal`
tuples.  Both comparisons agree.  The chain checker independently performs
the `Decimal` comparison before running any interval inequalities.  Thus no
rounded binary-floating handoff can enter the proof chain.

### 2. Exact continuous coverage and witness ranges

The fourth certificate contains exactly 131,072 positive-width cells.  I
checked every adjacent pair: each stored right-endpoint string equals the next
stored left-endpoint string.  The exact stored endpoints are

```text
0.0050000000000000001  and  1.
```

The analytic small-regime checker parses the same stored split, so the union
of the analytic and interval parts covers all $0<\lambda\leq1$.  The prose
abbreviation `[0.005,1]` is not the literal left decimal but creates no proof
gap.

Across the frozen cells the piecewise-constant witnesses satisfy

```text
0.0076086413128496032 <= M <= 0.39144557681412723
0.017886995941749265  <= Y <= 0.82095075547335117.
```

The Arb replays additionally prove $0<X<1$ on every whole cell.  In
particular, the large-regime witness is compactly separated from $M=1$.

### 3. Warm-start change and search/proof separation

The new `--initial-coefficients` path requires exactly `--degree` entries and
checks that its first coefficient agrees with the prior's first coefficient.
The coefficient basis used by the LP is the derivative of
$c_i\lambda^i e^{-\lambda}$, the first LP direction is fixed to zero, and a
zero-iteration replay returned the supplied eight coefficients unchanged.

The guard compares parsed binary floats rather than source decimal strings.
That is harmless here because this program is explicitly only a constructor:
the final JSON has the exact desired `-0.250000000000000` coefficient, and the
proof checkers parse and test the emitted exact decimals from scratch.  The
dense envelope interpolation, finite-difference Jacobian, predicted slack,
and warm start are not imported by either verifier.  Consequently an error in
the floating search can at worst propose a certificate that fails; it cannot
make an invalid certificate pass.

### 4. Prior concavity

I reran both 256-bit implementations on the exact $P_3$ prior:

```text
verify_arb.prove_prior_concavity:           F3'' <= -0.3618584052687671
verify_region_direct_arb.prove_concavity:   F3'' <= -0.36219400575974847
```

Both bounds are strict on all of $(0,1]$, including their separately handled
small intervals.  This proves that $F_3'$ decreases and
$A(\mu)=F_3(\mu)-\mu F_3'(\mu)$ increases, validating all endpoint and
interior cases in the two prior-envelope computations.

The document's optional continuation assertion also reproduces:

```text
primary P4 concavity upper:   -0.3551324549829281
direct P4 concavity upper:    -0.3559047458651924.
```

Concavity of $F_4$ is not needed to prove this fourth stage; it only makes
$F_4$ eligible as a prospective later prior.

### 5. Analytic small-$\lambda$ regime

For the exact finite polynomial $P_4$, the analytic checker obtains

```text
slack(lambda)/lambda >=
0.0038794631355425788456986812430578459... > 0
```

uniformly on
$0<\lambda\leq0.0050000000000000001$.  I rechecked the inequality directions:
the coefficient sums give $|P_4(\lambda)|\leq C_0\lambda$ and
$|P_4'(\lambda)-P_4(\lambda)|\leq C_1$; with
$M=\lambda e^{-\lambda}$ and $Y=1-X$, the lower bound
$Y\geq M+q-Mq$ is in the required direction; and the two
$\lambda\log\lambda$ terms cancel after division by $\lambda$.  This is an
open-tail proof, not extrapolation from the first large cell.

### 6. Large-regime target and main inequality

The complete chain checker returned for stage four:

```text
standard envelope margin:  7.473125335382186e-05 at cell 5
swapped envelope margin:   7.502455280615754e-05 at cell 131058
large main slack:          1.1266755240590772e-04 at cell 122401.
```

As an additional adversarial diagnostic, I replayed all 131,072 cells using
the polynomial, derivative, and interval primitives from the separately
written direct-region implementation rather than `verify_arb.py`.  It proved

```text
min F4 lower bound:     0.03025099347807219
min F4' lower bound:    0.7658536847459241
outer X range:          [0.2177730572875589, 0.986019741743803]
worst main slack:       0.00011266755240590772 at cell 122401.
```

Thus the main check is not relying only on the constructor's reported
`0.00013770259745871094` predicted slack.

### 7. Independent two-orientation Ramsey-region replay

`verify_region_direct_arb.py` does not import `verify_arb.py` and does not use
its $A(\mu)$ envelope formula.  It directly minimizes the two convex exponent
slacks over the complete prior-ratio interval.  My rerun returned

```text
PASS: independent direct two-sided Ramsey-region replay
prior F3'' worst certified upper:       -0.36219400575974847
worst standard direct exponent slack:    1.063861730808328e-06 at cell 0
worst swapped direct exponent slack:     7.502455280615754e-05 at cell 131058.
```

Both orientations are strictly positive.  The smaller standard exponent
slack occurs where the analytic splice meets the first large cell, as expected;
it still exceeds the predeclared $5\times10^{-7}$ diagnostic target.

### 8. Full four-stage replay and regressions

The exact command named in `STAGE4_SEARCH.md` completed with

```text
PASS: verified 4-stage Ramsey-rate certificate chain
```

and reproduced all four certificate hashes and links.  The fourth-stage
values are those displayed above.  The inherited first three stages also
reproduced their previously frozen positive small, region, and main margins.

`audit_tests.py` returned all three expected passes:

```text
PASS: derivative sign regression; X base is positive iff F'>0
PASS: arbitrary-degree polynomial derivative regression
PASS: Horizon union-gap test
```

### 9. Independent base calculation

The exact coefficient sum is

```text
P4(1) = -0.153131958642874.
```

Independent 80-digit decimal arithmetic gives

$$
F_4(1)=2\log2-0.153131958642874/e
$$

and

```text
F4(1)      = 1.3299602617488617145808261929025859091598657576290...
exp(F4(1)) = 3.7808931385024181222517908784987532623973039405998....
```

This agrees with the Arb enclosure.  Relative to the stage-three base, the
decrease is

```text
0.0005724773377503884757388526649698308277049387906....
```

## BookCor applicability at stage four

On the large compact regime, the verified $F_4'>0$ gives
$p=1-e^{-F_4'}\in(0,1)$; the stored witnesses give $M,Y\in(0,1)$; and the two
strict region inequalities put $(X,Y)$ in the required interior Ramsey-rate
region.  The strict main inequality and the uniform bounds
$\inf F_4'>0$, $\sup M<1$ supply the same finite-net uniformity used in the
already reviewed stages.  The small regime instead uses the elementary
$(X,1-X)$ Ramsey-region witness.  No extra condition such as $p>M$ and no
withdrawn Lemma 14 route is introduced by stage four.

This paragraph verifies candidate-specific applicability of the repaired
descent statement; it does not constitute a new proof of its imported
combinatorial core.

## Earliest gap and approved claim boundary

I found no gap beginning at the fourth-stage handoff.  The earliest unclosed
boundary of the overall argument is upstream of all four numerical
certificates: **GNNW Lemma 11 plus the locally repaired BookCor combinatorial
proof**.  A separate external dependency is the correctness of Arb enclosure
arithmetic as exposed by `python-flint`.

The approved wording is therefore:

> Conditional on the audited GNNW Lemma 11 / repaired BookCor core and Arb's
> enclosure semantics, the four frozen exact-Decimal-linked certificates
> prove
> $R(k,k)\leq(3.7808931385024181222\ldots)^{k+o(k)}$.

The evidence does **not** approve claims that the bound is published,
externally peer reviewed, unconditional with respect to that imported core,
formalized in a proof assistant, effective at a stated finite threshold, or
automatically iterable to a fifth stage.

## Residual and archive-only risks

- Both persistent numerical implementations ultimately rely on the same Arb
  library, despite independent region logic.  A different interval library or
  formal arithmetic replay would reduce that common dependency.
- The independently rerun main-inequality diagnostic is recorded here but is
  not a separately frozen repository checker.
- The current `.venv` is a verification environment and does not contain the
  NumPy/SciPy constructor dependencies; replaying the optional floating search
  requires the separately listed search dependencies.  This does not affect
  certificate verification.
- The smallest direct margin is about $1.06\times10^{-6}$.  It is rigorously
  positive for the frozen decimals, but any regeneration or coefficient
  rounding must rerun both checkers.
- No fifth-stage or infinite-descent conclusion was reviewed.
