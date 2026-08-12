# Upper-bound route progress

## Current result

The current recommended local computer-assisted theorem is now

$$
R(k,k)\le (3.780685290)^{k+o(k)}.
$$

It uses the exact six-stage rate below as a frozen input and combines it with
Yang--Mao's retained preliminary spines and parameterized book theorem.  The
exact-diagonal candidate with
$u_0=1235783/500000$ establishes

$$
\mathcal G_2^{(3)}
\left(\frac{330867}{500000},
\frac{12366348252219}{1250000000000}\right),
\qquad
\frac{12366348252219}{1250000000000}=9.8930786017752.
$$

Feeding this correlation input into the retained-spine transfer gives the
exact decimal tuple

```text
(eta,p,delta,lambda0,tau)
=(0.02868896,0.47130887,0.000053863,13233,0.00069386)
```

and a complete weighted-wedge proof of exponent gain `3.4754e-6`.  The exact
ratio target gives the uniform bad-event separator; the good-event proof
handles every two-dimensional sign pattern and then uses the exact identity
$F(z,z)=H(z)^2-H(z)H(-z)$ on both a compact interval and analytic half-line.
Both author checks pass at 512 bits.  A genuinely non-importing 512-bit Arb
implementation reconstructs the entire inner and outer chain.  A second
non-importing adaptive 512-bit referee checker uses different subdivisions
and analytic endpoint reductions.  The resolved adversarial referee found no
remaining gap.  The actual base before upward rounding is
`3.7806852883796401133524...`, hence strictly below
`3.780685288379640114`.

Claim boundary: this is a local asymptotic theorem conditional on Yang--Mao
v1 regularization, positive tensor-moment, tail, and parameterized-book
interfaces, the frozen P6/BookCor proof package and retained-spine transfer,
and Arb containment.  It gives no explicit finite-$k$ threshold, specific
finite Ramsey-number result, global parameter optimum, novelty, priority,
publication, external peer review, or world-best claim.  The current canonical
proof, author checks, non-importing replay, independent adaptive checker, and
resolved referee are:

```text
e4ea58def640593690a7545e111c3b38f1bfcf8a5735fe7985600481e0bf36d4  EXACT_DIAGONAL_NEXT_CANDIDATE.md
17db00d9374ce3ba3e68a3a4626ec2c51a70ec45a307972dacc245b153382c3e  check_exact_diagonal_next.py
e2035cbffefcb147141fcee4831cac2af085f26d9183091ee20d90acc89ac87b  check_retained_spine_exact_diagonal_next.py
fc379e3b861b69054aadaa80ebc3c791cb8358f22c9b0aa01070c56aa131c26c  independent_check_exact_diagonal_next.py
3c30f72ddc24848f2b72c278f35b5d8bd6296ae8a40b045d30c5b7e087bd7150  referee_check_exact_diagonal_next.py
a21402a5dad40490bd493201f0cf6579c5d94ee74aa8460d7117298a737d3ef3  INDEPENDENT_EXACT_DIAGONAL_NEXT_REFEREE.md
```

The independently reviewed $u_0=309/125$ package, safe base `3.780685300`
(actual `3.7806852985874904057...`), is the immediate canonical predecessor.
The reviewed safe-base `3.780685320` diagonal-envelope package and safe-base
`3.780685405` strong-separator package are earlier predecessors.  The reviewed
safe-base `3.780685745` hybrid-correlation package, the safe-base
`3.780687577208` specialized-correlation package, and the safe-base
`3.780695781309`/gain-`7e-7` package are earlier predecessors:
`STRONG_SEPARATOR_GROWTH_SHARPENING.md`,
`RETAINED_SPINE_STRONG_GROWTH_CANDIDATE.md`,
`INDEPENDENT_STRONG_SEPARATOR_GROWTH_REFEREE.md`,
`HYBRID_CORRELATION_SHARPENING.md`,
`RETAINED_SPINE_JOINT_OPTIMIZED_CERTIFICATE.md`,
`INDEPENDENT_JOINT_CORRELATION_SPINE_REFEREE.md`,
`RETAINED_SPINE_TRANSFER_ATTEMPT.md`,
`INDEPENDENT_RETAINED_SPINE_REFEREE.md`,
`RETAINED_SPINE_OPTIMIZED_CERTIFICATE.md`, and
`INDEPENDENT_RETAINED_SPINE_OPTIMIZED_REFEREE.md`.  The earlier
`RETAINED_SPINE_NUMERIC_CERTIFICATE.md` remains as a frozen predecessor.

## Frozen P6 input

The retained-spine theorem's frozen rate input is the exact-linked
six-stage quintic/quintic/sextic/octic/decic/tetradecic descent

```text
P1 = (-0.25, 0.062797738895, -0.032456368039,
       0.102292138999, -0.028160790049)
P2 = (-0.25, -0.008578629273557, 0.127585140806616,
      -0.029829210000000, 0.010085181421050)
P3 = (-0.250000000000000, -0.003330465213687,
       0.091728978292451,  0.040555948334794,
      -0.053458127305523,  0.021783259992867)
P4 = (-0.250000000000000,  0.006788512088209,
       0.038835297966515,  0.110380487198675,
      -0.045883160603885, -0.048420977583689,
       0.038460877061037, -0.003292994769736)
P5 = (-0.250000000000000,  0.008940782406867,
       0.025638668310206,  0.132358619338106,
      -0.049722086579346, -0.069400050582772,
       0.053089364457318, -0.002238059505066,
      -0.000543242850723, -0.001354112596489)
P6 = (-0.250000000000000,  0.019891840059418,
      -0.012275954247190,  0.144110816398083,
       0.006277913420654, -0.066101623491668,
      -0.002287675993602, -0.058238059505066,
       0.030675864198693,  0.052472201910597,
       0.043300454861853, -0.042529975074653,
      -0.055263639426635,  0.036695886931268)
c = exp(F6(1)) = 3.7806984277961236988...
```

The proof chain first certifies the elementary beta `0.08` rate using
`Y=1-X`, proves the two quintics in sequence, and then uses the exact second
quintic tuple as the strict two-sided prior for the sextic.  The exact sextic
tuple is then the prior for the octic stage, whose exact target is the prior
for the decic stage, whose target is the exact prior for the tetradecic stage.
The five-stage `3.7807566104095593763...` result is the independently reviewed
local predecessor.  The four-stage `3.7808931385024181222...` result is
another independently reviewed predecessor.  The older three-stage
`3.7814656158401685107...` result remains an earlier milestone, and the robust
beta `0.0299` cubic bound
`3.7990629773286618741...` remains an independently frozen baseline.

Claim status: **independently replayed local computer-assisted theorem**.  The
generic proof bridge and complete chain through stage three have independent
reviews; a separate adversarial referee also reran the full four-stage chain
and direct-region checker and found no stage-four gap.  A new independent
referee reran the fifth-stage chain and direct checker and found no gap.  A
sixth-stage adversarial referee independently reran the full chain, direct
checker, exact link, dense gate, and coverage audit and found no gap.  The
formerly
imported GNNW Lemma 11/Theorem 12 combinatorial core now has a standalone proof
and an independent adversarial referee PASS.  Arb semantics, external human
review, and public archival remain as trust boundaries.
The former `3.792918524...` headline is withdrawn because
its beta `0.03` prior depended on the unproved Lemma 14 iteration.

## Frozen evidence

* Recommended certificates: `certificate-higher-order-quintic-v1.json`,
  `certificate-higher-order-quintic-chain-v2.json`,
  `certificate-higher-order-sextic-chain-v3.json`,
  `certificate-higher-order-octic-chain-v4.json`,
  `certificate-higher-order-decic-chain-v5.json`,
  `certificate-higher-order-tetradecic-chain-v6.json`
* SHA-256: `2664bc421cd0cb7489289caa283a3a3f22830580f7c21bf0e6cbe092910bc277`,
  `b5b595b4dcc9d1bdc2b5714f68fef99ec1c566bbd612d35ca19100d173d41c4d`,
  `2052952c3af98074d5442fb736c7a2952146e92051a43fab84e75f099d9e00d7`,
  `09253d757516dc258396f82c09a442aaaf9d499640c1cc99b5767e6d51d35942`,
  `4ec4dbbe190a08134efe68c3a76ce4b4fb3aabdad230af703c19a28a03ecf9a9`,
  `8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8`
* Certificate cells: 65,536 for stages 1--3 and 131,072 for stages 4--6 on
  `[0.005,1]`
* Verifier: `verify_arb.py`
* Exact-link verifier: `verify_chain_arb.py`
* Independent direct-region verifier: `verify_region_direct_arb.py`
* Arithmetic: python-flint 0.9.0, Arb precision 256 bits
* Search generator: `generate_higher_order_certificate.py`
* Chained-target search only: `search_chained_target.py`
* Audit regressions: `audit_tests.py`
* Mathematical bridge: `THEOREM_AUDIT.md`
* Complete proof replay: `INDEPENDENT_PROOF_REPLAY.md`
* BookCor source repair: `BOOKCOR_AUDIT.md`
* Standalone combinatorial core: `LEMMA11_STANDALONE_PROOF.md`
* Independent combinatorial referee: `INDEPENDENT_LEMMA11_REFEREE.md`
* Higher-order theorem package: `HIGHER_ORDER_SEARCH.md`
* Fourth-stage construction and replay: `STAGE4_SEARCH.md`
* Fifth-stage construction and replay: `STAGE5_SEARCH.md`
* Fifth-stage independent adversarial referee: `INDEPENDENT_STAGE5_REFEREE.md`
* Sixth-stage construction and replay: `STAGE6_SEARCH.md`
* Sixth-stage independent adversarial referee: `INDEPENDENT_STAGE6_REFEREE.md`
* Fourth-stage independent adversarial referee: `INDEPENDENT_STAGE4_REFEREE.md`
* Third-stage independent referee: `INDEPENDENT_STAGE3_REFEREE.md`
* Full-chain adversarial review: `ADVERSARIAL_FULL_CHAIN_REVIEW.md`
* Result-to-claim finding: `HIGHER_ORDER_RESULT_TO_CLAIM.md`, `findings.md`
* Frozen stage-one-through-three stdout and hashes:
  `VERIFICATION_LOG_HIGHER_ORDER.md`; later stdout/hashes: `STAGE4_SEARCH.md`,
  `STAGE5_SEARCH.md`, `STAGE6_SEARCH.md`

## Current six-stage Arb summary

```text
PASS: verified 6-stage Ramsey-rate certificate chain
stage 1 small slack/lambda: 0.0034410087628560810...
stage 1 standard / swapped region: 1.087940012958612e-4 / 1.0994822689528693e-4
stage 1 large main: 9.667544669720171e-5
stage 1 independent direct standard / swapped: 1.54983120140414e-6 / 1.0994822689528693e-4
stage 2 small slack/lambda: 0.0038270889416388282...
stage 2 standard / swapped region: 1.0960144273955114e-4 / 1.1009250090651343e-4
stage 2 large main: 1.0520468957159067e-4
stage 2 independent direct standard / swapped: 1.5614231112089097e-6 / 1.1009250090651343e-4
F2(1): 1.330841127585477476533640851907...
stage 3 small slack/lambda: 0.0038903585040936769...
stage 3 standard / swapped region: 6.960077165064378e-5 / 7.016617229398231e-5
stage 3 large main: 1.6510787819556342e-4
stage 3 independent direct standard / swapped: 9.911774569389889e-7 / 7.016617229398231e-5
F3(1): 1.330111663542254603247894158088...
stage 4 small slack/lambda: 0.0038794631355425788...
stage 4 standard / swapped region: 7.473125335382186e-5 / 7.502455280615754e-5
stage 4 large main: 1.1266755240590772e-4
stage 4 independent direct standard / swapped: 1.063861730808328e-6 / 7.502455280615754e-5
F4(1): 1.329960261748861714580826192902...
stage 5 small slack/lambda: 0.0038635364902009499769...
stage 5 standard / swapped region: 7.472217372172618e-5 / 7.413705007828921e-5
stage 5 large main: 8.565396565931536e-5
stage 5 independent direct standard / swapped: 1.0634883501982575e-6 / 7.413705007828921e-5
F5(1): 1.329924151085869627075980547012...
stage 6 small slack/lambda: 0.0037785734384423962376...
stage 6 standard / swapped region: 7.464714995786726e-5 / 5.766703065384951e-5
stage 6 large main: 4.818471567626107e-5
stage 6 independent direct standard / swapped: 1.0628096485437162e-6 / 5.766703065384951e-5
F6(1): 1.329908761821993072318781263204...
growth base: 3.780698427796123698751881649752...
```

The separately written direct-region replay does not import `verify_arb.py` or
its `A(mu)` envelope reduction. Stage-one-through-three stdout is frozen in
`VERIFICATION_LOG_HIGHER_ORDER.md`; the later-stage replays are frozen in
`STAGE4_SEARCH.md`, `STAGE5_SEARCH.md`, and `STAGE6_SEARCH.md`.

## Positive control

A separate 32,768-cell beta `0.03` certificate using the safe beta `0.08` prior
also passes the same checker with comparable margins. It is the theorem-safe
repair/positive control.

```text
growth base: 3.799202739615937195778455775939...
prior beta: 0.08, certified independently with Y=1-X
```

The frontier beta `0.0298` certificate also passes at
`c=3.798923220182859...`, but its worst main margin is only `4.23e-9`; it is
retained as a non-recommended numerical frontier rather than the headline.

## Audit corrections during this route

1. `F'<0` in the displayed GNNW theorem is a sign typo; the formula and proof
   require `F'>0`.
2. Horizon's `min(bu,bs)` accepts the union of two one-sided rate conditions,
   but GNNW Observation 7(4) requires all positive `k,l`; the correct sufficient
   inner region uses `max`, i.e. both conditions. The new certificate satisfies
   both, so the correction does not invalidate it.
3. An intermediate small-lambda implementation used the wrong exponential
   constant and relied on a questionable Lemma 14 splice. It was removed rather
   than patched: the final checker uses the elementary witness `Y=1-X` and an
   analytic proof on the entire `(0,0.005]` interval.
4. The final small-regime proof uses the valid termwise bound
   `|i-lambda|<=i` and certifies normalized main slack uniformly.
5. The printed theorem assumes only `(X,Y) in R`, but its proof invokes
   BookCor with an `R_*` input after shrinking only `X`.  The candidate repairs
   this explicitly: strict two-sided rate margins give `R_*` on the large
   regime, and `x+Y<1` gives `R_*` on the elementary small regime.
6. The printed theorem also lacks the `sup M<1` hypothesis needed for its
   uniform finite-net perturbation.  The candidate certifies the stronger
   global bound `M<0.393`, so this omission is repairable for this object.

## Reproduction

```text
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-verify.txt
.venv/bin/python verify_chain_arb.py certificate-higher-order-quintic-v1.json certificate-higher-order-quintic-chain-v2.json certificate-higher-order-sextic-chain-v3.json certificate-higher-order-octic-chain-v4.json certificate-higher-order-decic-chain-v5.json certificate-higher-order-tetradecic-chain-v6.json
.venv/bin/python verify_region_direct_arb.py certificate-higher-order-quintic-v1.json
.venv/bin/python verify_region_direct_arb.py certificate-higher-order-quintic-chain-v2.json
.venv/bin/python verify_region_direct_arb.py certificate-higher-order-sextic-chain-v3.json
.venv/bin/python verify_region_direct_arb.py certificate-higher-order-octic-chain-v4.json
.venv/bin/python verify_region_direct_arb.py certificate-higher-order-decic-chain-v5.json
.venv/bin/python verify_region_direct_arb.py certificate-higher-order-tetradecic-chain-v6.json
.venv/bin/python check_retained_spine_transfer.py
.venv/bin/python check_retained_spine_numeric.py
.venv/bin/python independent_check_retained_spine_numeric.py
.venv/bin/python check_retained_spine_optimized.py
.venv/bin/python independent_check_retained_spine_optimized.py
.venv/bin/python check_specialized_correlation.py
.venv/bin/python check_retained_spine_sharpened.py
.venv/bin/python independent_check_retained_spine_sharpened.py
.venv/bin/python check_hybrid_correlation.py
.venv/bin/python check_retained_spine_joint_optimized.py
.venv/bin/python independent_check_retained_spine_joint_optimized.py
.venv/bin/python check_u0_2472_diagonal_growth.py
.venv/bin/python check_retained_spine_u0_2472.py
.venv/bin/python independent_check_u0_2472_diagonal_growth.py
.venv/bin/python check_exact_diagonal_next.py
.venv/bin/python check_retained_spine_exact_diagonal_next.py
.venv/bin/python independent_check_exact_diagonal_next.py
.venv/bin/python referee_check_exact_diagonal_next.py
.venv/bin/python audit_tests.py
```

Search dependencies are separate in `requirements-search.txt`.

## Next proof and optimization step

The next proof priority is external specialist review, immutable archival,
and optional formalization of the exact-diagonal retained-spine/P6 package.
The locally proved exponent gain is now `3.4754e-6`, with actual upper base
`3.7806852883796401133524...`.  No global correlation/retained-spine
parameter optimum, seventh polynomial stage, finite-$k$ threshold, specific
finite Ramsey-number result, novelty, publication priority, publication, or
world-best claim is made.
