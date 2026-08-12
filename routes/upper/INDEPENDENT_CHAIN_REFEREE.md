# Independent referee report: exact-linked higher-order upper chain

Date: 2026-08-12

## Verdict and claim classification

**Concrete two-stage claim: PASS, conditional on the imported GNNW
combinatorial core.**  I found no gap in the exact-linked numerical chain, the
candidate-specific repaired descent, the strict Ramsey-region interior bridge,
or the small-\(\lambda\) splice.  With the coefficient convention

\[
P(\lambda)=\sum_{i=1}^d c_i\lambda^i
\]

(so the displayed vectors begin with the coefficient of \(\lambda\), not a
constant term), the reviewed package supports

\[
R(k,k)\leq
\left(3.7842250653748521911439944463870320\ldots\right)^{k+o(k)}.
\]

This is a **local conditional computer-assisted theorem**, not an
unconditional, formally verified, published, or externally peer-reviewed
theorem.  The earliest unclosed mathematical dependency is GNNW Lemma 11 and
the preceding combinatorial material used by the repaired `t:bookmain` /
`t:bookCor`.  The local package audits and repairs their use but does not
independently re-prove Lemma 11.

The broader phrase "arbitrary finite-degree polynomial" needs qualification.
The descent mechanism is degree-blind, and the derivative code accepts any
finite coefficient list, but arbitrary coefficients are not automatically
valid.  Every stage must still certify all sign, main-inequality, region, and
uniformity hypotheses.  The analytic splice as written also uses
\(P(0)=0\).  Thus this report approves the two frozen quintic stages, not all
finite polynomials merely by virtue of finite degree.

## What was independently replayed

I reviewed `HIGHER_ORDER_SEARCH.md`,
`HIGHER_ORDER_RESULT_TO_CLAIM.md`, `INDEPENDENT_PROOF_REPLAY.md`,
`BOOKCOR_AUDIT.md`, both frozen JSON certificates, and the chain and direct
Arb verifiers.  I then ran the chain verifier, both direct-region replays, and
the regression tests from the repository root.

The exact chain is

\[
\begin{aligned}
P_0={}&-0.25\lambda+0.08\lambda^2+0.08\lambda^3,\\
P_1={}&-0.25\lambda+0.062797738895\lambda^2
-0.032456368039\lambda^3\\
&+0.102292138999\lambda^4-0.028160790049\lambda^5,\\
P_2={}&-0.25\lambda-0.008578629273557\lambda^2
+0.127585140806616\lambda^3\\
&-0.029829210000000\lambda^4+0.010085181421050\lambda^5.
\end{aligned}
\]

`verify_chain_arb.py` compares each JSON handoff as tuples of exact Python
`Decimal` values before doing Arb arithmetic.  The second certificate's prior
tuple equals the first certificate's target tuple exactly.  I also checked the
JSON endpoints as exact decimals: each file has 65,536 positive-width cells,
no gap or overlap, starts at its stated split, and ends at exactly 1.

The independent run returned:

```text
PASS: verified 2-stage Ramsey-rate certificate chain

stage 0
  target small slack/lambda: 0.0034410087628560810...
  standard region margin:    0.0001087940012958612
  swapped region margin:     0.00010994822689528693
  large main slack:          0.00009667544669720171
  exp(F_1(1)):               3.7914853930774899343626155087867436...

stage 1
  target small slack/lambda: 0.0038270889416388282...
  standard region margin:    0.00010960144273955114
  swapped region margin:     0.00011009250090651343
  large main slack:          0.00010520468957159067
  exp(F_2(1)):               3.7842250653748521911439944463870320...
```

The separately written direct-region verifier, which neither imports
`verify_arb.py` nor uses its \(A(\mu)=U(\mu)-\mu U'(\mu)\) envelope reduction,
returned:

```text
stage 0
  prior U'' upper bound:                 -0.40795020415189553
  worst direct standard exponent slack:  1.54983120140414e-06
  worst direct swapped exponent slack:   0.00010994822689528693

stage 1
  prior U'' upper bound:                 -0.36862975299624107
  worst direct standard exponent slack:  1.5614231112089097e-06
  worst direct swapped exponent slack:   0.00011009250090651343
```

The derivative-sign, arbitrary-degree derivative, and known one-orientation
union-gap regressions also passed.

## Mathematical audit

### 1. Degree dependence and concavity

The repaired descent lemma itself uses the target only through smoothness,
\(F>0\), \(F'>0\), local boundedness of \(|F''|\), the strict main
inequality, valid BookCor points in \(\mathcal R_*\), and
\(\sup_I M<1\) on every compact \(I\subset(0,1]\).  It does **not** use
target concavity and does not inspect the polynomial degree.  A finite
polynomial times \(e^{-\lambda}\) supplies the required local smoothness.

Prior concavity plays a different, computational role: it justifies the
one-dimensional envelope reductions used to prove both rate-region
orientations.  The stage-0 cubic prior and the stage-1 quintic prior are each
certified strictly concave.  No concavity of the final target \(F_2\) is
needed for the stated two-stage theorem; it would have to be proved if
\(F_2\) were used as a prior in a later stage.

Consequently the correct generic statement is: the **descent lemma is degree
independent**, while this certificate method additionally requires either a
proved concave prior or some other rigorous proof of the two region
inequalities.

### 2. What a prior must supply

At a large-regime stage the prior is used only to establish the proposed
BookCor point in \(\mathcal R_*\).  For the method in this package, that is
obtained from:

1. a prior bound uniform in the epsilon sense over all integer ratios
   \(1\leq \ell\leq k\);
2. continuity at zero with \(U(0)=0\); and
3. strict standard and swapped exponent inequalities.

The two orientations are both necessary.  Compactness upgrades their
pointwise strictness to a common positive exponent margin, permits both
coordinates to be enlarged, and hence gives a genuine interior point rather
than merely a point of \(\mathcal R\).  Stage 0 proves its cubic prior by the
elementary witness.  The first repaired descent supplies the required uniform
rate for \(F_1\), and exact coefficient equality then permits \(F_1\) to be
the stage-1 prior.  There is no circular use of the second certificate.

Strict concavity is a verifier convenience for minimizing the two exponent
slacks, not an additional premise of the abstract interior lemma.

### 3. \(F\), \(F'\), and the witness range

On every large-regime cell the chain verifier proves \(F>0\), \(F'>0\),
\(0<M,Y,X<1\), the main inequality, and both region inequalities using Arb
balls over the full closed cell.  In the small regime the analytic routine
proves \(F>0\) and \(F'>0\), rather than extrapolating from a sampled point.

The exact finite-cell witness ranges include

```text
stage 0: 0.0076114324934313093 <= M <= 0.39271931785717823
stage 1: 0.0076113188907315516 <= M <= 0.39204809435680854
```

and the small witness is \(M=\lambda e^{-\lambda}<1\).  Hence every compact
interval away from zero has a single bound \(\sup_I M<1\).  Continuity and
the certified positivity of \(F'\) similarly give \(\inf_I F'>0\), and the
finite-degree target gives \(\sup_I|F''|<\infty\).

### 4. Small-\(\lambda\) splice

For \(P(\lambda)=\sum_{i=1}^d c_i\lambda^i\), the analytic verifier uses

\[
|P(\lambda)|\leq C_0\lambda,
\qquad |P'(\lambda)-P(\lambda)|\leq C_1,
\]

with finite sums of the exact coefficient magnitudes.  Writing
\(q=e^{-F'}\), it rigorously obtains
\(q_-\lambda\leq q\leq q_+\lambda\),
\(-\log X\leq A\lambda\), and \(Y\geq D\lambda\) for \(D>0\).
Substitution of
\(\log M=\log\lambda-\lambda\) and
\(\log Y\geq\log\lambda+\log D\) cancels both
\(\lambda\log\lambda\) singular terms.  The two reported positive
normalized slacks therefore cover the whole open interval down to zero.

This argument is rigorous for arbitrary finite coefficient magnitude **when
the resulting interval inequalities pass**; it does not assert that they
will pass for every coefficient choice.  It also does not cover a nonzero
constant term in \(P\) without a new zero-endpoint analysis.

### 5. Finite-net uniformity

The repaired proof first handles sufficiently small ratios with the uniform
Erdos--Szekeres estimate and \(H(\lambda)-F(\lambda)=O(\lambda)\).  On a
fixed compact \([\rho,1]\), positive \(\inf F'\) and
\(\sup M<1\) allow one common perturbation \(\delta>0\).  Uniform continuity
of \(F,F'\) supplies a finite ratio net.  Each net point has a BookCor
threshold, and the maximum of finitely many thresholds is finite.  Local
boundedness of \(|F''|\) closes the induction comparison between
\(\ell/k\) and \((\ell-1)/k\).

The certificate witnesses \(M,Y\) are piecewise constant and discontinuous,
but the proof never takes their derivatives or needs their continuity.  It
uses only their point values, their common range bounds, and finitely many
BookCor calls.  Either adjacent witness may be chosen at a shared endpoint,
and both are certified on their closed cells.  I find the quantifier order
and the uniform epsilon conclusion closed.

### 6. BookCor repair

The local replay correctly does not invoke GNNW Theorem 13 literally.  The
printed derivative sign would make \(1-e^{-F'}\) negative; the usable sign is
\(F'>0\).  The replay also supplies the missing \(\mathcal R_*\) argument.

For `t:bookmain` / `t:bookCor`, the reviewed repairs are coherent: choose the
integer \(r\) before \(\varepsilon\); remove the unnecessary printed
restriction \(p>\mu\); impose the additional small-\(\varepsilon\),
interior, and monotonicity conditions; preserve the strict inequality in the
last optimization; and handle the induction edge cases.  In particular the
limit formula is valid for every fixed \(p,\mu\in(0,1)\), since
\(p^{1/r}\to1>\mu\).  Thus the certificate is not missing a hidden
\(p>M\) condition.

This replay is still conditional on the earlier GNNW combinatorial lemma(s),
most importantly Lemma 11.  That is an imported dependency, not a numerical
certificate obligation.

## Earliest potential gap and residual risks

1. **Imported mathematical dependency:** the first place this local package
   does not close the proof from first principles is GNNW Lemma 11 and the
   preceding combinatorial input to BookCor.  If that imported result or the
   repaired source replay fails, the Ramsey claim fails.  I found no later
   independent gap in the two-stage descent.
2. **Degree overstatement risk:** "arbitrary degree" must not be read as
   "arbitrary polynomial is automatically a valid rate."  The current small
   splice assumes no constant term, and every numerical/analytic hypothesis
   must pass separately.
3. **Shared arithmetic trust:** the chain and direct-region implementations
   are structurally independent for the region calculation, but both use
   python-flint/Arb at 256-bit precision.  This is two-code, one-arithmetic-
   library evidence, not a fully independent formalization.
4. **Frozen-log provenance mismatch:** the current
   `VERIFICATION_LOG_HIGHER_ORDER.md` records SHA-256
   `36ef42c9...` for `verify_arb.py`, whereas the file actually reviewed and
   run here has SHA-256 `879ce15f...`.  The certificate hashes and the two
   top-level verifier hashes agree with the log.  This stale verifier hash is
   not a mathematical counterexample because the current code was inspected
   and rerun successfully, but the archival log should be regenerated or the
   exact verifier version pinned before public release.
5. The result is asymptotic and gives no explicit finite threshold.  Public
   archival and external combinatorics review remain outstanding.

## Frozen inputs and reviewed-code hashes

```text
2664bc421cd0cb7489289caa283a3a3f22830580f7c21bf0e6cbe092910bc277  certificate-higher-order-quintic-v1.json
b5b595b4dcc9d1bdc2b5714f68fef99ec1c566bbd612d35ca19100d173d41c4d  certificate-higher-order-quintic-chain-v2.json
879ce15f4518f1d6737fdbba09d04f7433c96c4c3d81efcd3c666a35fdaae981  verify_arb.py
f4e2c8663022a82ed22c41677e71d4b609b0a9eace1770c56deb12351faf3494  verify_chain_arb.py
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
b0d4f0cb94bb816ca3342e6076dd8223d1003e661757481442fe166eb2330bfe  audit_tests.py
```

## Reproduction

From `/Users/Jackal/iWorld/ireserch/Ramsey`:

```bash
.venv/bin/python routes/upper/verify_chain_arb.py \
  routes/upper/certificate-higher-order-quintic-v1.json \
  routes/upper/certificate-higher-order-quintic-chain-v2.json

.venv/bin/python routes/upper/verify_region_direct_arb.py \
  routes/upper/certificate-higher-order-quintic-v1.json

.venv/bin/python routes/upper/verify_region_direct_arb.py \
  routes/upper/certificate-higher-order-quintic-chain-v2.json

.venv/bin/python routes/upper/audit_tests.py

shasum -a 256 \
  routes/upper/certificate-higher-order-quintic-v1.json \
  routes/upper/certificate-higher-order-quintic-chain-v2.json \
  routes/upper/verify_arb.py \
  routes/upper/verify_chain_arb.py \
  routes/upper/verify_region_direct_arb.py \
  routes/upper/audit_tests.py
```

## Approved claim wording

> Conditional on the audited GNNW Lemma 11 / repaired BookCor combinatorial
> core and Arb's enclosure semantics, the two frozen, exact-Decimal-linked
> quintic certificates prove
> \(R(k,k)\leq(3.7842250653748521911\ldots)^{k+o(k)}\).
> The claim is degree-independent only at the level of the descent mechanism;
> each concrete prior and target must independently pass all analytic,
> two-sided-region, and exact-link checks.

