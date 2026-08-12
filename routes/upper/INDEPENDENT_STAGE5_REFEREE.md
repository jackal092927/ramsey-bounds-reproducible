# Independent adversarial referee report: fifth decic descent stage

Date: 2026-08-12

## Verdict

**PASS.**  I found no gap at the exact $P_4\to P_5$ handoff, in the
continuous fifth-stage certificate, or in the complete five-certificate
induction.  The locally proved book induction and balanced-book corollary are
correctly pinned to their independently audited hashes, so the older
``imported GNNW/BookCor'' qualifier is no longer the first open boundary for
this claim.

The exact local computer-assisted claim reviewed below is

```text
PROVABLE AS STATED
```

This verdict is not a claim of external human peer review, public archival,
or proof-assistant formalization.  The earliest dependency not independently
reimplemented here is Arb ball containment as exposed by `python-flint`.

## Exact claim reviewed

For

$$
H(\lambda)=(1+\lambda)\log(1+\lambda)-\lambda\log\lambda
$$

and the exact terminating-decimal polynomial

$$
\begin{aligned}
P_5(\lambda)={}&-0.250000000000000\lambda
+0.008940782406867\lambda^2
+0.025638668310206\lambda^3\\
&+0.132358619338106\lambda^4
-0.049722086579346\lambda^5
-0.069400050582772\lambda^6\\
&+0.053089364457318\lambda^7
-0.002238059505066\lambda^8
-0.000543242850723\lambda^9\\
&-0.001354112596489\lambda^{10},
\end{aligned}
$$

put $F_5(\lambda)=H(\lambda)+P_5(\lambda)e^{-\lambda}$.  The frozen exact
five-stage chain, together with the local combinatorial descent, proves

$$
R(k,k)\leq
\left(3.7807566104095593763172345562324210\ldots\right)^{k+o(k)}.
$$

It is an asymptotic statement and does not provide an explicit finite-$k$
threshold.

## Frozen materials and hashes

The prose claim and fifth proof input reviewed here are

```text
2e81b42338f67f262712f245c152b00151553a2e5bf7006cb54ad2f599e75b10  STAGE5_SEARCH.md
4ec4dbbe190a08134efe68c3a76ce4b4fb3aabdad230af703c19a28a03ecf9a9  certificate-higher-order-decic-chain-v5.json
```

The four exact-link predecessors are

```text
2664bc421cd0cb7489289caa283a3a3f22830580f7c21bf0e6cbe092910bc277  certificate-higher-order-quintic-v1.json
b5b595b4dcc9d1bdc2b5714f68fef99ec1c566bbd612d35ca19100d173d41c4d  certificate-higher-order-quintic-chain-v2.json
2052952c3af98074d5442fb736c7a2952146e92051a43fab84e75f099d9e00d7  certificate-higher-order-sextic-chain-v3.json
09253d757516dc258396f82c09a442aaaf9d499640c1cc99b5767e6d51d35942  certificate-higher-order-octic-chain-v4.json
```

The checker hashes used in this replay are

```text
879ce15f4518f1d6737fdbba09d04f7433c96c4c3d81efcd3c666a35fdaae981  verify_arb.py
f4e2c8663022a82ed22c41677e71d4b609b0a9eace1770c56deb12351faf3494  verify_chain_arb.py
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
b0d4f0cb94bb816ca3342e6076dd8223d1003e661757481442fe166eb2330bfe  audit_tests.py
```

The replay used Python 3.11.15 and the pinned `python-flint==0.9.0`; both
verifiers set Arb precision to 256 bits.

## Independent checks

### 1. Exact $P_4\to P_5$ link

I compared the target coefficient list in the fourth certificate with the
prior coefficient list in the fifth certificate.  The lists are identical
both as source strings and as arbitrary-precision decimal numbers:

```text
-0.250000000000000,  0.006788512088209,
 0.038835297966515,  0.110380487198675,
-0.045883160603885, -0.048420977583689,
 0.038460877061037, -0.003292994769736.
```

The complete chain checker repeats an exact `Decimal` tuple comparison before
using the fifth prior.  No binary-float tolerance occurs at this handoff.  I
also checked all four earlier links; every adjacent target/prior list is
exactly equal.

### 2. Exact coverage

The fifth certificate has exactly 131,072 positive-width cells.  Its first
stored left endpoint is

```text
0.0050000000000000001
```

and its last right endpoint is exactly `1`.  Every stored right-endpoint
string equals the next stored left-endpoint string: there are zero adjacency
mismatches.  The analytic small-regime checker uses the same exact split.
Consequently the analytic part and frozen cells cover all
$0<\lambda\leq1$ with neither an omitted interval nor a rounded splice.

Both Arb replays separately enforce positive cell width, endpoint continuity,
and completion at $\lambda=1$.

### 3. Concavity gate

I reran both independent 256-bit concavity implementations on the exact
$P_4$ prior:

```text
verify_arb.prove_prior_concavity:          F4'' <= -0.3551324549829281
verify_region_direct_arb.prove_concavity:  F4'' <= -0.35590474586519238
```

Both are strict on the whole open interval $(0,1]$, including the separately
handled interval adjacent to zero.  This justifies the monotonicity used by
both continuous prior-envelope reductions.  The optional continuation test
for the new target also reproduces

```text
primary F5'' upper:  -0.35642515827888227
direct F5'' upper:   -0.3574394324533535.
```

### 4. Complete five-stage Arb replay

I ran the exact five-file command printed in `STAGE5_SEARCH.md`.  It completed
with

```text
PASS: verified 5-stage Ramsey-rate certificate chain
```

and reproduced all five hashes and all four exact handoffs.  The fifth-stage
strict quantities were

```text
analytic small-regime slack/lambda:
  0.0038635364902009499769566864189767432089151065759... > 0

standard Ramsey-region margin:
  7.472217372172618e-05 at cell 33

swapped Ramsey-region margin:
  7.413705007828921e-05 at cell 131071

large-regime main slack:
  8.565396565931536e-05 at cell 122989.
```

The verifier also proves $F_5>0$, $F_5'>0$, all witness ranges, and $0<X<1$
on every whole cell.  All four earlier stages again returned positive small,
standard, swapped, and main margins; no inherited stage failed during this
replay.

### 5. Separately written direct Ramsey-region replay

`verify_region_direct_arb.py` neither imports `verify_arb.py` nor uses its
$A(\mu)=F_4(\mu)-\mu F_4'(\mu)$ envelope formula.  It instead minimizes both
convex exponent slacks directly over the full prior-ratio interval.  My rerun
returned

```text
PASS: independent direct two-sided Ramsey-region replay
prior F4'' worst certified upper:       -0.35590474586519238
segments:                                131072
worst standard direct exponent slack:    1.0634883501982575e-06 at cell 0
worst swapped direct exponent slack:     7.413705007828921e-05 at cell 131071.
```

Thus the much smaller standard margin at the analytic/finite splice is still
strictly positive, and both orientations pass independently of the primary
envelope reduction.

### 6. Regression replay

`audit_tests.py` returned all three intended passes:

```text
PASS: derivative sign regression; X base is positive iff F'>0
PASS: arbitrary-degree polynomial derivative regression
PASS: Horizon union-gap test
```

The last test guards against accepting a union of the two Ramsey-region
orientations when their intersection is required.

### 7. Independent base calculation

The exact decimal coefficient sum is

```text
P5(1) = -0.153230117601899.
```

Independent 80-digit decimal arithmetic gives

```text
F5(1)      = 1.3299241510858696270759805470122072168049440032978...
exp(F5(1)) = 3.7807566104095593763172345562324210302278058291661....
```

This agrees with the 256-bit Arb enclosure and the displayed claim.

### 8. Combinatorial dependency wording

`STAGE5_SEARCH.md` correctly cites the locally closed combinatorial proof and
its independent referee report at the exact hashes

```text
b402469d8b08009833b15489ea14ed2fa0417c333d7900d5de1d82b4e36b9c30  LEMMA11_STANDALONE_PROOF.md
9d3963344c675045961f9dc82437ee3e2df3d31bdcb28b9d42954386be49c22e  INDEPENDENT_LEMMA11_REFEREE.md
```

It says that the *formerly* imported GNNW/BookCor boundary is locally closed;
it does not silently continue to treat the original published lemma as an
unproved black box.  It also retains the correct limitations: local
computer-assisted theorem, non-explicit $o(k)$, no external human review, and
no claim that five successful finite descents imply an infinite descent.

## Earliest unclosed boundary

I found no fifth-stage-specific gap.  The former GNNW/BookCor boundary has
been replaced by the pinned local proof and its independent adversarial
review.  The earliest remaining non-symbolic dependency is therefore the
correctness of Arb's documented enclosure semantics and its implementation in
`python-flint==0.9.0`.  Beyond that are evidence-strength limitations rather
than a detected mathematical counterexample: no external human peer review
or public archival, and no formal proof-assistant replay of either the local
combinatorial proof or the interval checker.

No sixth-stage claim was searched or reviewed here.
