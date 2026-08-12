# Fifth chained upper-bound descent

## Claim

Let

$$
H(\lambda)=(1+\lambda)\log(1+\lambda)-\lambda\log\lambda
$$

and, with the displayed terminating decimals interpreted exactly,

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
&-0.001354112596489\lambda^{10}.
\end{aligned}
$$

Set $F_5(\lambda)=H(\lambda)+P_5(\lambda)e^{-\lambda}$.  Using the locally
closed combinatorial descent in `LEMMA11_STANDALONE_PROOF.md`, independently
accepted in `INDEPENDENT_LEMMA11_REFEREE.md`, and Arb's documented enclosure
semantics, the exact five-stage chain proves

$$
\boxed{
R(k,k)\leq
\left(3.7807566104095593763172345562324210\ldots\right)^{k+o(k)}.
}
$$

This is a local computer-assisted theorem.  It is not a published result, an
explicit finite-$k$ inequality, or a formal-assistant proof.

## Status

```text
PROVABLE AS STATED
```

The status applies to the local theorem above.  Arb containment semantics and
the absence of external human review remain at the evidence boundary; the
formerly imported GNNW/BookCor combinatorial boundary is locally closed.

## Assumptions

1. The locally proved book induction and balanced-book corollary in
   `LEMMA11_STANDALONE_PROOF.md` are used in the form independently audited in
   `INDEPENDENT_LEMMA11_REFEREE.md`.
2. The first four exact-decimal targets are Ramsey rates by their already
   frozen certificates.
3. `python-flint` Arb at 256-bit precision has its documented ball-containment
   semantics.
4. Every JSON coefficient is an exact terminating decimal; no binary-float
   tolerance is allowed at a chain handoff.

The frozen local combinatorial proof has SHA-256
`b402469d8b08009833b15489ea14ed2fa0417c333d7900d5de1d82b4e36b9c30`;
its independent referee report has SHA-256
`9d3963344c675045961f9dc82437ee3e2df3d31bdcb28b9d42954386be49c22e`.

## Notation

- $P_4$ is the exact octic target in
  `certificate-higher-order-octic-chain-v4.json`.
- $F_j(\lambda)=H(\lambda)+P_j(\lambda)e^{-\lambda}$.
- The *main slack* is the strict target inequality replayed by
  `verify_chain_arb.py`.
- The *standard* and *swapped* margins are the two separate prior-rate Ramsey
  region orientations.  Both, not their union, are required.

## Proof strategy

Use a floating-point trust-region search only to construct a prospective
degree-ten target.  Freeze its decimal coefficients and piecewise-constant
book witnesses, then discard all floating interpolation as evidence.  Prove
the exact $F_4\to F_5$ link on the entire continuum with Arb, replay both
Ramsey-region orientations in a separately written direct verifier, and
finally replay the complete five-stage chain from the elementary cubic prior.

## Dependency map

1. The elementary cubic prior and stages 1--4 supply the already certified
   exact rate $F_4$.
2. Strict concavity of $F_4$ supplies the monotonicity needed by both continuous
   prior-envelope reductions.
3. An analytic elementary witness covers $0<\lambda\leq0.0050000000000000001$.
4. The 131,072 frozen cells cover the complementary interval through
   $\lambda=1$ and prove positivity, both Ramsey-region orientations, and the
   main inequality.
5. The independent direct verifier replays the two continuous exponent
   inequalities without importing the main verifier's envelope formula.
6. Exact Decimal equality links the fifth prior to the fourth target.
7. The locally proved book induction and balanced-book corollary convert these
   strict inequalities into the next Ramsey rate; evaluating at $\lambda=1$
   gives the displayed base.

## Proof

### 1. Frozen prior and concavity gate

The only prior used in this search was the exact target tuple from the frozen
fourth-stage certificate of SHA-256

```text
09253d757516dc258396f82c09a442aaaf9d499640c1cc99b5767e6d51d35942
```

namely

```text
-0.250000000000000, 0.006788512088209,
 0.038835297966515, 0.110380487198675,
-0.045883160603885,-0.048420977583689,
 0.038460877061037,-0.003292994769736
```

Before any fifth-stage optimization, the two 256-bit Arb implementations
proved $F_4''<0$ on all of $(0,1]$:

```text
verify_arb.prove_prior_concavity:          F4'' <= -0.3551324549829281
verify_region_direct_arb.prove_concavity:  F4'' <= -0.35590474586519238
```

They separately handle the singular interval next to zero and subdivide the
remaining interval.  Thus $F_4'$ is strictly decreasing and
$F_4(\mu)-\mu F_4'(\mu)$ is strictly increasing, which justifies all endpoint
and interior cases used by the two envelope computations.

As a continuation diagnostic, both implementations also prove strict
concavity of the final exact $F_5$ target:

```text
primary continuation bound:  F5'' <= -0.35642515827888227
direct continuation bound:   F5'' <= -0.3574394324533535
```

This last fact is not needed for the $F_4\to F_5$ link; it only makes $F_5$
eligible to be tested as a later prior.

### 2. Floating construction and rejected frontier point

`search_chained_target.py` was used only as a constructor.  Representative
endpoints at requested unbuffered mesh margin $1.5\times10^{-4}$ were:

| highest power | candidate base |
|---:|---:|
| 8 | 3.78076067533627 |
| 9 | 3.78075832165121 |
| 10, raw frontier | 3.78075592435119 |

The raw degree-ten point was **not** frozen.  A denser scan followed by nested
scalar refinement found a shallow second minimum

```text
slack = 0.00014992307193584242 at lambda ~= 0.3383369832,
```

below the requested construction target even though the optimization mesh's
active minimum was near $\lambda=0.935$.  To retain a modest construction
guard, the raw point was mixed with 0.5% of the exact $P_4$ tuple (padded by
two zero coefficients).  For the final displayed decimals, a broad dense
scan and local refinement gave

```text
minimum unbuffered floating slack:
0.00015000321056057864 at lambda ~= 0.9346903199

minimum sampled F5':
0.7658924675917616 at lambda = 1

floating base:
3.7807566104095596
```

These numbers selected the candidate but do not occur in either proof
checker.

### 3. Frozen fifth-stage certificate

Only the conservative final target was certified:

```text
file: certificate-higher-order-decic-chain-v5.json
SHA-256: 4ec4dbbe190a08134efe68c3a76ce4b4fb3aabdad230af703c19a28a03ecf9a9
cells: 131072
stored left endpoint: 0.0050000000000000001
stored right endpoint: 1
region buffer: 0.000080000000000000007
constructor predicted worst buffered slack: 0.00011256629107658789
```

The certificate is a proof input only after exact Arb replay.  Its interpolated
envelope table and scalar optimizer remain untrusted construction aids.

### 4. Complete five-stage Arb replay

`verify_chain_arb.py` first compared each prior and preceding target as tuples
of arbitrary-precision `Decimal` values.  It then replayed all five stages
from the elementary cubic prior and returned

```text
PASS: verified 5-stage Ramsey-rate certificate chain
```

For the new fifth stage, the rigorous values are

```text
target small slack/lambda:
0.0038635364902009499769566864189767439...

standard Ramsey-region margin:
7.472217372172618e-05 at cell 33

swapped Ramsey-region margin:
7.413705007828921e-05 at cell 131071

large-regime main slack:
8.565396565931536e-05 at cell 122989

F5(1):
1.3299241510858696270759805470122072168...

exp(F5(1)):
3.7807566104095593763172345562324210302...
```

Every value needed to establish strictness is positive.  The analytic splice
and the exact cells together cover all $0<\lambda\leq1$.

The complete frozen chain hashes are

```text
2664bc421cd0cb7489289caa283a3a3f22830580f7c21bf0e6cbe092910bc277  stage 1
b5b595b4dcc9d1bdc2b5714f68fef99ec1c566bbd612d35ca19100d173d41c4d  stage 2
2052952c3af98074d5442fb736c7a2952146e92051a43fab84e75f099d9e00d7  stage 3
09253d757516dc258396f82c09a442aaaf9d499640c1cc99b5767e6d51d35942  stage 4
4ec4dbbe190a08134efe68c3a76ce4b4fb3aabdad230af703c19a28a03ecf9a9  stage 5
```

### 5. Independent direct Ramsey-region replay

`verify_region_direct_arb.py` does not import `verify_arb.py` and does not use
its scalar $A(\mu)$ envelope reduction.  It directly minimizes both convex
exponent slacks over the complete prior-ratio interval.  On the fifth-stage
certificate it returned

```text
PASS: independent direct two-sided Ramsey-region replay
prior F4'' worst certified upper:       -0.35590474586519238
worst standard direct exponent slack:    1.0634883501982575e-06 at cell 0
worst swapped direct exponent slack:     7.413705007828921e-05 at cell 131071
```

The smaller direct margin is still more than twice the predeclared
$5\times10^{-7}$ diagnostic target.

### 6. Regression replay and conclusion

`audit_tests.py` passed the derivative-sign regression, arbitrary-degree
polynomial-derivative regression, and the known Horizon union-gap regression.
Therefore no search-script output is needed for the proof, the exact fifth
link is strict on the entire continuum, and the full exact chain proves the
local claim.  Evaluating the resulting rate at $\lambda=1$ gives the boxed
diagonal bound. $\square$

## Reproduction commands

Run from `routes/upper`:

```text
.venv/bin/python verify_chain_arb.py \
  certificate-higher-order-quintic-v1.json \
  certificate-higher-order-quintic-chain-v2.json \
  certificate-higher-order-sextic-chain-v3.json \
  certificate-higher-order-octic-chain-v4.json \
  certificate-higher-order-decic-chain-v5.json

.venv/bin/python verify_region_direct_arb.py \
  certificate-higher-order-decic-chain-v5.json

.venv/bin/python audit_tests.py
```

## Corrections or missing assumptions

- The wording “a new published Ramsey bound” is not supported.  The proved
  statement is the local computer-assisted theorem in the Claim section.
- The certificate does not supply an effective threshold in $k$ because the
  inherited asymptotic descent retains non-explicit $o(k)$ terms.
- A later stage may not treat a rounded or refitted version of $P_5$ as its
  prior.  It must use the exact ten displayed decimals and pass a new exact
  chain link.

## Open risks

1. The numerical proof imports Arb containment semantics through
   `python-flint` at 256-bit precision.
2. The fifth stage has not yet received independent external human review or
   public archival.
3. The local combinatorial proof and interval proof have not been formalized
   in a proof assistant.
4. The success of five finite descents does not establish convergence or an
   unrestricted infinite descent.
