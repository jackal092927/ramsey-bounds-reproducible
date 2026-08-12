# Higher-order target search and chained certificate

## Claim

Let

$$
F_j(\lambda)=H(\lambda)+P_j(\lambda)e^{-\lambda},
\qquad
H(\lambda)=(1+\lambda)\log(1+\lambda)-\lambda\log\lambda,
$$

with the following **exact decimal** coefficient vectors, listed in increasing
power of $\lambda$:

$$
\begin{aligned}
P_0 &: (-0.25,\ 0.08,\ 0.08),\\
P_1 &: (-0.25,\ 0.062797738895,\ -0.032456368039,\
         0.102292138999,\ -0.028160790049),\\
P_2 &: (-0.25,\ -0.008578629273557,\ 0.127585140806616,\
        -0.029829210000000,\ 0.010085181421050),\\
P_3 &: (-0.250000000000000,\ -0.003330465213687,\
         0.091728978292451,\ 0.040555948334794,\
        -0.053458127305523,\ 0.021783259992867).
\end{aligned}
$$

The three frozen certificates prove the exact chain
$F_0\to F_1\to F_2\to F_3$ and,
conditional only on the audited GNNW Lemma 11 / repaired BookCor descent used
by the preceding proof package, establish

$$
R(k,k)\leq
\left(3.7814656158401685107275297311637231\ldots\right)^{k+o(k)}.
$$

## Status

**PROVABLE AS STATED within the existing audited computer-assisted proof
framework.** The original external dependency and publication caveats are
unchanged: this is not yet a published or externally human-reviewed theorem.

## Assumptions and exact-link invariant

1. `INDEPENDENT_PROOF_REPLAY.md` and `BOOKCOR_AUDIT.md` correctly repair the
   source theorem and BookCor around GNNW Lemma 11.
2. Arb ball arithmetic in python-flint 0.9.0 has its documented containment
   semantics; the runs use 256-bit precision.
3. The first safe rate $F_0$ is proved with the elementary witness
   $M=\lambda e^{-\lambda}$, $Y=1-X$, not assumed.
4. At every later stage, the JSON `prior_coefficients` must equal the preceding
   JSON `target_coefficients` as exact `Decimal` tuples. This is checked before
   any arithmetic. In particular no rounded or silently substituted rate
   enters the chain.

## Why polynomial degree is irrelevant to the descent proof

The repaired finite-net descent lemma does not assume that the correction is
cubic. For a target $F$ it uses only:

1. $F>0$ and $F'>0$ on $(0,1]$;
2. $F$ is smooth and $\sup_I|F''|<\infty$ on every compact
   $I\subset(0,1]$;
3. the displayed $X$ formula and strict main inequality;
4. the BookCor point belongs to $\mathcal R_*$;
5. $\sup_I M<1$.

Every finite polynomial times $e^{-\lambda}$ is analytic, so item 2 holds for
both quintics and the sextic. The interval certificates prove items 1, 3, and
4; their finite
piecewise witness lists give

```text
stage 1: 0.0076114324934313093 <= M <= 0.39271931785717823
stage 2: 0.0076113188907315516 <= M <= 0.39204809435680854
stage 3: 0.0076143579747633220 <= M <= 0.39142102191105950
```

on $[0.005,1]$, while the elementary small-regime witness has $M<1$. Thus item
5 holds. Nothing in this dependency list changes when the correction degree
increases from three to five or six.

The prior-envelope reduction additionally uses strict concavity of the prior.
The generalized Arb implementation evaluates

$$
F''(\lambda)
=-\frac1{\lambda(1+\lambda)}
 +e^{-\lambda}\bigl(P''(\lambda)-2P'(\lambda)+P(\lambda)\bigr)
$$

for an arbitrary finite coefficient list. It proves each stage prior is
strictly concave on $(0,1]$; the independent direct verifier separately proves
the same facts with a different subdivision and implementation.

## Search/proof separation

`search_chained_target.py` and `generate_higher_order_certificate.py` are
floating-point constructors. They
uses a dense interpolated envelope only to choose piecewise constants $M,Y$.
No interpolation output is trusted as a proof.

The proof stage reads only exact decimals from the resulting JSON:

* `verify_chain_arb.py` checks exact links, proves prior concavity, proves the
  analytic small-$\lambda$ regime, and replays both region orientations and
  the main inequality over every continuous cell;
* `verify_region_direct_arb.py` is separately written, does not import
  `verify_arb.py`, and directly minimizes the two exponent slacks rather than
  using the $A(\mu)=U(\mu)-\mu U'(\mu)$ envelope reduction;
* `audit_tests.py` includes arbitrary-degree derivative and known union-gap
  regressions.

The search and proof code therefore do not share the numerical envelope
implementation or optimization result.

## Frozen certificates

### Stage 1: safe cubic prior to first quintic

```text
certificate: certificate-higher-order-quintic-v1.json
SHA-256: 2664bc421cd0cb7489289caa283a3a3f22830580f7c21bf0e6cbe092910bc277
cells: 65536 on [0.005,1]
region buffer: 0.00012
target coefficients:
  -0.25, 0.062797738895, -0.032456368039,
   0.102292138999, -0.028160790049
```

Certified output:

```text
target small slack/lambda: 0.0034410087628560810...
standard region margin:    1.087940012958612e-4
swapped region margin:     1.0994822689528693e-4
large main slack:          9.667544669720171e-5
independent direct standard exponent slack: 1.54983120140414e-6
independent direct swapped exponent slack:  1.0994822689528693e-4
exp(F1(1)): 3.7914853930774899343626155087867436...
```

### Stage 2: exact first-quintic prior to second quintic

```text
certificate: certificate-higher-order-quintic-chain-v2.json
SHA-256: b5b595b4dcc9d1bdc2b5714f68fef99ec1c566bbd612d35ca19100d173d41c4d
cells: 65536 on [0.005,1]
region buffer: 0.00012
prior coefficients: exactly the stage-1 target tuple
target coefficients:
  -0.25, -0.008578629273557, 0.127585140806616,
  -0.029829210000000, 0.010085181421050
```

Certified output:

```text
prior U'' worst certified upper bound (chain checker): -0.368386088401026
target small slack/lambda: 0.0038270889416388282...
standard region margin:    1.0960144273955114e-4
swapped region margin:     1.1009250090651343e-4
large main slack:          1.0520468957159067e-4

independent prior U'' upper bound:              -0.36862975299624107
independent direct standard exponent slack:     1.5614231112089097e-6
independent direct swapped exponent slack:      1.1009250090651343e-4

F2(1): 1.3308411275854774765336408519073957...
exp(F2(1)): 3.7842250653748521911439944463870320...
```

### Stage 3: exact second-quintic prior to sextic

```text
certificate: certificate-higher-order-sextic-chain-v3.json
SHA-256: 2052952c3af98074d5442fb736c7a2952146e92051a43fab84e75f099d9e00d7
cells: 65536 on [0.005,1]
region buffer: 0.00008
prior coefficients: exactly the stage-2 target tuple
target coefficients:
  -0.250000000000000, -0.003330465213687,
   0.091728978292451,  0.040555948334794,
  -0.053458127305523,  0.021783259992867
```

Certified output:

```text
target small slack/lambda: 0.0038903585040936769...
standard region margin:    6.960077165064378e-5
swapped region margin:     7.016617229398231e-5
large main slack:          1.6510787819556342e-4

independent prior U'' upper bound:              -0.37184261548417713
independent direct standard exponent slack:     9.911774569389889e-7
independent direct swapped exponent slack:      7.016617229398231e-5

F3(1): 1.3301116635422546032478941580882757...
exp(F3(1)): 3.7814656158401685107275297311637231...
```

The smallest direct-region margin in the final stage is therefore
$9.91\times10^{-7}$, while every main/descent margin across the chain is at
least $9.6\times10^{-5}$.

## Proof conclusion

The safe elementary rate proves $F_0$. The first certificate uses strict
two-sided $F_0$ envelopes to put its BookCor parameters in $\mathcal R_*$ and
the repaired descent lemma proves $F_1$. The second certificate names the
exact $F_1$ coefficient tuple as its prior; the chain checker rejects the file
unless that link is exact. Strict two-sided $F_1$ envelopes and the same
degree-agnostic repaired descent lemma then prove $F_2$. The third certificate
likewise names the exact $F_2$ tuple as prior, and its strict two-sided
envelopes prove $F_3$.

At $\lambda=1$,

$$
F_3(1)=2\log2+
\frac{-0.250000000000000-0.003330465213687+0.091728978292451
+0.040555948334794-0.053458127305523+0.021783259992867}{e},
$$

and Arb gives the constant displayed in the claim. $\square$

## Reproduction

From `routes/upper`:

```text
.venv/bin/python verify_chain_arb.py \
  certificate-higher-order-quintic-v1.json \
  certificate-higher-order-quintic-chain-v2.json \
  certificate-higher-order-sextic-chain-v3.json

.venv/bin/python verify_region_direct_arb.py \
  certificate-higher-order-quintic-v1.json

.venv/bin/python verify_region_direct_arb.py \
  certificate-higher-order-quintic-chain-v2.json

.venv/bin/python verify_region_direct_arb.py \
  certificate-higher-order-sextic-chain-v3.json

.venv/bin/python audit_tests.py
```

## Scope and remaining risk

* This proves an asymptotic diagonal upper bound, not a finite threshold.
* The certificates are local artifacts and still need public archival and
  external human combinatorics review.
* The theorem depends on the audited GNNW Lemma 11 / repaired BookCor core;
  neither numerical checker re-proves that combinatorial lemma.
* More descent stages may lower the constant further. They must preserve the
  same exact-link invariant and two independent replays; the current claim
  does not extrapolate beyond the three frozen stages.
