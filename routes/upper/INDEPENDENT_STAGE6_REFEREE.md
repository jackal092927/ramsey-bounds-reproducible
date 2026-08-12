# Independent adversarial referee report: sixth tetradecic descent stage

Date: 2026-08-12

## Verdict

**PASS.**  I found no gap in the exact $P_5\to P_6$ handoff, the continuous
sixth-stage certificate, the complete six-certificate induction, or the
predeclared acceptance gates.  The local computer-assisted claim

$$
R(k,k)\leq
\left(3.7806984277961236987518816497522162752\ldots\right)^{k+o(k)}
$$

is therefore

```text
PROVABLE AS STATED
```

under the same local proof boundary as the accepted fifth-stage theorem.  This
verdict is not external human peer review, public archival, or proof-assistant
formalization.  The earliest numerical dependency not independently
reimplemented here is Arb ball containment as exposed by `python-flint`.

## Frozen materials and environment

The exact prose claim and new proof input reviewed here are

```text
2881e8b1df310b449d0bffff5715b9176d9c191ba2a5d05bb376ab2843c58ccd  STAGE6_SEARCH.md
8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8  certificate-higher-order-tetradecic-chain-v6.json
```

The five exact-link predecessors are

```text
2664bc421cd0cb7489289caa283a3a3f22830580f7c21bf0e6cbe092910bc277  certificate-higher-order-quintic-v1.json
b5b595b4dcc9d1bdc2b5714f68fef99ec1c566bbd612d35ca19100d173d41c4d  certificate-higher-order-quintic-chain-v2.json
2052952c3af98074d5442fb736c7a2952146e92051a43fab84e75f099d9e00d7  certificate-higher-order-sextic-chain-v3.json
09253d757516dc258396f82c09a442aaaf9d499640c1cc99b5767e6d51d35942  certificate-higher-order-octic-chain-v4.json
4ec4dbbe190a08134efe68c3a76ce4b4fb3aabdad230af703c19a28a03ecf9a9  certificate-higher-order-decic-chain-v5.json
```

The unchanged checker hashes used in the replay are

```text
879ce15f4518f1d6737fdbba09d04f7433c96c4c3d81efcd3c666a35fdaae981  verify_arb.py
f4e2c8663022a82ed22c41677e71d4b609b0a9eace1770c56deb12351faf3494  verify_chain_arb.py
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
b0d4f0cb94bb816ca3342e6076dd8223d1003e661757481442fe166eb2330bfe  audit_tests.py
```

The locally closed combinatorial dependency and its independent referee are
pinned at

```text
b402469d8b08009833b15489ea14ed2fa0417c333d7900d5de1d82b4e36b9c30  LEMMA11_STANDALONE_PROOF.md
9d3963344c675045961f9dc82437ee3e2df3d31bdcb28b9d42954386be49c22e  INDEPENDENT_LEMMA11_REFEREE.md
```

I used Python 3.11.15 and the pinned `python-flint==0.9.0`; both interval
implementations set Arb precision to 256 bits.

## Independent checks

### 1. Exact handoff, degree support, and coverage

The ten source strings in the P5 target and P6 prior are identical.  Parsing
both lists independently as arbitrary-precision `Decimal` tuples also gives
equality entry by entry.  Repeating this test on every earlier adjacent pair
passes all five handoffs.  No binary-float tolerance enters the chain.

The P6 target has exactly fourteen coefficients.  I separately evaluated the
degree-14 polynomial and its first and second derivatives by explicit
full-length sums at a non-special point; both the primary and direct verifier
implementations enclosed all three independently computed values.  Thus no
coefficient above an older hard-coded degree is dropped.

The certificate has exactly 131,072 cells.  Every cell has positive width,
the first left endpoint is `0.0050000000000000001`, the final right endpoint
is exactly `1`, and all 131,071 adjacent endpoint strings match exactly.
Every coefficient and every stored endpoint/witness is a JSON string, and all
stored $M,Y$ lie strictly between zero and one.  The analytic small-regime
checker uses the same exact split, so there is neither a splice gap nor an
overlap-dependent argument.

### 2. Prior concavity and exact base

Before accepting the sixth link, I reran both 256-bit concavity implementations
on the exact P5 prior:

```text
verify_arb.prove_prior_concavity:          F5'' <= -0.35642515827888227
verify_region_direct_arb.prove_concavity:  F5'' <= -0.3574394324533535
```

Both bounds are strict on all of $(0,1]$, including their separately handled
interval adjacent to zero.  As an archive-only continuation diagnostic, both
implementations also prove strict concavity of the exact P6 target:

```text
primary continuation upper:  F6'' <= -0.34158474968063746
direct continuation upper:   F6'' <= -0.3515456913371641.
```

Independent 90-digit decimal arithmetic gives

```text
P6(1) = -0.153271949958248
F6(1) = 1.3299087618219930723187812632036105226006705914731...
exp(F6(1)) = 3.7806984277961236987518816497522162752862452544333...
```

and, using the exact P5 decimals,

```text
exp(F5(1)) - exp(F6(1))
= 0.0000581826134356775653529064802047549415605747327... .
```

This exceeds the predeclared base-improvement floor $10^{-6}$ by more than a
factor of 58.

### 3. Construction-gate replay and bounded search record

The floating search is not part of the mathematical proof, but it was a
predeclared acceptance gate.  I independently reconstructed the 20,001-point
broad scan as the union of 4,001 geometrically spaced points on
`[0.005,0.1]` and 16,001 linearly spaced points on `[0.1,1]`.  I enumerated
all four sampled interior local minima and applied bounded scalar refinement
to each, retaining both endpoints.  This reproduces

```text
minimum unbuffered floating slack:
0.00015473769852614172 near lambda = 0.339437036
```

and the next three refined minima in the frozen report.  It also reproduces
the sampled minima of $F_6$ and $F_6'$ as `0.030260793830868504` at the split
and `0.7658393690544814` at one.  Thus the frozen candidate clears the
predeclared unbuffered-slack floor $0.00015$.

I also challenged the apparently better degree-13 frontier row.  Replaying
that exact candidate on the constructor's original 20,001-point grid
(4,001 geometric plus 16,001 linear points) and refining every sampled local
minimum gives

```text
minimum slack = 0.00014808101253183104
at lambda = 0.3389505192262032,
```

which is below the declared floor.  Its lower diagnostic base therefore does
not make it admissible.  The raw degree-14 candidate was likewise rejected in
the frozen record after a dense leak.  The accepted target remains within the
predeclared degree range 10--14.  I found no stage-7 artifact, and the frozen
report explicitly stops after this one descent.

The floating discovery command and every rejected optimizer iterate are not
frozen as a machine-readable trace.  That is a provenance limitation of the
search narrative, not a validity gap in the fully checkable exact theorem
artifact.

### 4. Complete six-stage Arb replay

I independently ran the complete six-file command in `STAGE6_SEARCH.md`.  It
returned

```text
PASS: verified 6-stage Ramsey-rate certificate chain
```

and reproduced every certificate hash and all five exact handoffs.  The new
stage's proof-critical quantities were

```text
analytic small-regime slack/lambda:
  0.0037785734384423962376319094335140413159011347494... > 0

standard Ramsey-region margin:
  7.464714995786726e-05 at cell 8

swapped Ramsey-region margin:
  5.766703065384951e-05 at cell 131071

large-regime main slack:
  4.818471567626107e-05 at cell 131071

growth base:
  3.7806984277961236987518816497522162752862452544333... .
```

The checker also proves $F_6>0$, $F_6'>0$, $0<M,Y,X<1$, both region
orientations, and the strict main inequality on every complete cell.  All five
predecessor stages again returned positive analytic, region, and main margins.

### 5. Separately written direct region replay

`verify_region_direct_arb.py` does not import the primary verifier or use its
$A(\mu)=F_5(\mu)-\mu F_5'(\mu)$ envelope reduction.  Its independent direct
minimization over the continuous prior-ratio interval returned

```text
PASS: independent direct two-sided Ramsey-region replay
prior F5'' worst certified upper:       -0.35743943245335352
segments:                                131072
worst standard direct exponent slack:    1.0628096485437162e-06 at cell 0
worst swapped direct exponent slack:     5.766703065384951e-05 at cell 131071.
```

Both exact direct margins exceed the predeclared $5\times10^{-7}$ floor.  The
smaller one is strict but close enough that any coefficient rounding or
certificate regeneration must rerun both interval verifiers.

### 6. Regression replay and gate ledger

The unchanged `audit_tests.py` returned all intended passes:

```text
PASS: derivative sign regression; X base is positive iff F'>0
PASS: arbitrary-degree polynomial derivative regression
PASS: Horizon union-gap test
```

Consequently the predeclared gates close as follows:

| gate | independent result |
|---|---:|
| base improvement at least $10^{-6}$ | $5.8182613435\times10^{-5}$, PASS |
| dense/scalar unbuffered slack at least $1.5\times10^{-4}$ | $1.5473769853\times10^{-4}$, PASS |
| no more than 131,072 exact cells | 131,072, PASS |
| complete six-stage Arb replay | PASS |
| both direct margins at least $5\times10^{-7}$ | $1.0628096485\times10^{-6}$ and $5.7667030654\times10^{-5}$, PASS |
| exact P5-target/P6-prior `Decimal` link | PASS |
| unchanged regressions | PASS |
| bounded degree 10--14 and no stage 7 | PASS |

## Claim boundary and earliest open dependency

I approve the frozen report's wording as one local, asymptotic,
computer-assisted theorem.  I do **not** approve any stronger claim that it is
a published bound, gives an explicit finite-$k$ threshold, improves a named
finite Ramsey number, has a proof of infinite descent, or has received
external human peer review or proof-assistant verification.

The local combinatorial induction and balanced-book corollary are pinned to a
standalone proof and an earlier independent adversarial referee report, so
they are not the first unclosed local boundary.  The earliest remaining
non-symbolic dependency is Arb's documented ball-containment semantics and
its implementation in `python-flint==0.9.0`.  Beyond that lie evidence-strength
limitations rather than a detected sixth-stage mathematical gap: no replay
with a different interval library, no external human review, no public
archival, and no formal proof-assistant development.
