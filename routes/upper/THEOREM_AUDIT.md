# Theorem-to-code audit: diagonal Ramsey upper bound

Snapshot: 2026-08-12. Sources are pinned to GNNW arXiv:2407.19026v1 and
HorizonMath commit `d509c90a75202a45585b01f75762188db4fa2d2d`.

## Bottom line

The earlier `3.792918524...` object is **withdrawn as a theorem-linked
candidate**. Its numerical certificate used the beta `0.03` rate as a prior,
but that rate came from GNNW's Lemma 14 iteration, whose displayed branch choice
does not supply the claimed Ramsey-region point.

The currently recommended, independently checked computer-assisted theorem is

```text
R(k,k) <= (3.799062977328662...)^(k+o(k)).
```

It strictly improves the numerical base reported in the GNNW preprint without
using Lemma 14: the
elementary beta `0.08` rate is first certified from `Y=1-X`, then used as the
prior for target beta `0.0299` under a strict two-sided region. An independent
proof replay and an adversarial follow-up both return `YES`; external human
review and publication remain outside this workspace.

## 1. Exact sufficient theorem and the derivative sign

GNNW source lines 258--268 define `R` as the closure of all `(x,y)` for which,
eventually for **all positive** `k,l`,

```text
R(k,l) <= x^(-k) y^(-l).
```

Observation 7(4) converts an asymptotic bound of this form into membership in
`R`. Theorem 13 is at source lines 404--411. Its displayed line 406 says
`F'(lambda)<0`, but this is a typographical sign error:

1. The same line defines
   `X=(1-exp(-F'))^(1/(1-M)) (1-M)`. A real positive `X` requires `F'>0`.
2. Lines 402 and 418--436 use `exp(-F')` as a blue-density fraction and
   `1-exp(-F')` as a red-density fraction, again requiring `F'>0`.
3. GNNW's explicit functions have `F'>0`; Horizon's statement and checker use
   the positive sign.

`audit_tests.py` contains a ball-arithmetic regression for this sign.

### A second source-level bridge issue: `R` versus `R_*`

There is a separate interior-point omission in the printed Theorem 13 proof.
The theorem hypothesis at source line 406 requires only
`(X(lambda),Y(lambda)) in R`, whereas BookCor at lines 390--394 requires its
input `(x,y)` to lie in the interior `R_*`.  In the finite-net argument at
lines 425--428, the proof replaces `X(lambda)` by a strictly smaller
`x_lambda`, but leaves `y_lambda=Y(lambda)`.  For a general downward-closed
set, decreasing only one coordinate of a boundary point does not imply that
the result is an interior point.  Thus Theorem 13, in its literal stated
generality, needs either an `R_*` hypothesis or an explicit two-coordinate
interior argument.

The present candidate has such an argument, separately in its two regimes:

* On `[5*10^-3,1]`, both prior-rate inequalities have strict positive margin.
  For a fixed target lambda, continuity in the prior ratio `mu`, together with
  the positive limits `a=-log X` and `b=-log Y` at `mu=0`, allows `a,b` to be
  decreased slightly while preserving both inequalities.  Equivalently,
  `X,Y` can both be enlarged slightly while remaining in `R`.  Observation
  7(3) then gives `(X,Y) in R_*`, and the smaller `x_lambda` used by BookCor
  remains in `R_*`.
* On `(0,5*10^-3]`, `Y=1-X`.  The finite-net BookCor parameter satisfies
  `x_lambda<X`, so `x_lambda+Y<1`.  Choose `z` strictly between `x_lambda` and
  `X`; then `(z,1-z) in R` by Observation 7(1), while
  `x_lambda<z` and `Y=1-X<1-z`.  Observation 7(3) gives
  `(x_lambda,Y) in R_*`.

This is a candidate-specific repair, not a proof of printed Theorem 13 for
arbitrary discontinuous witnesses.  The proof replay must retain it as an
explicit lemma.

The same finite-net paragraph also chooses one `delta>0` through an expression
containing the exponent `1/(1-M(lambda))`, although the printed theorem assumes
no continuity of `M` and no uniform bound below one.  In that generality,
`M(lambda)` could approach one on a compact lambda interval and the asserted
uniform choice need not follow.  The certificate again has the missing
candidate-specific hypothesis: on the large cells
`0.0076223 <= M <= 0.3925490`, while on the elementary small regime
`M=lambda exp(-lambda)`.  Thus `sup M<0.393` globally and the uniform `delta`
exists after `F'` is bounded away from zero on each compact
`[epsilon',1]`.

## 2. A one-sided rate requires two inequalities

Let `a=-log x`, `b=-log y`. Suppose the prior theorem provides only

```text
log R(k,l) <= k U(l/k) + o(k),    l<=k.
```

To invoke Observation 7(4), one must cover both orders of `k,l`.

### Case 1: l<=k

With `mu=l/k`, the desired exponent is

```text
k a + l b = k(a+mu b).
```

Thus the prior rate proves this half only if

```text
(I)  a+mu b >= U(mu)  for every 0<mu<=1.
```

### Case 2: k<=l

Ramsey symmetry gives `R(k,l)=R(l,k)`. Apply the prior rate to `(l,k)` and put
`mu=k/l`. The desired exponent is now

```text
k a + l b = l(mu a+b).
```

Thus the other half requires

```text
(II) b+mu a >= U(mu)  for every 0<mu<=1.
```

Both (I) and (II) are required. Merely proving (II) for the swapped pair does
not prove that the swapped pair is in `R`: it proves only its `l<=k` half; its
other half is exactly (I). Claiming full membership first and then using the
symmetry of `R` would be circular.

## 3. Horizon's `min` is a theorem-to-code gap

For fixed `a`, condition (I) is equivalent to

```text
b >= bu(a) := sup_mu (U(mu)-a)/mu,
```

while condition (II) is equivalent to

```text
b >= bs(a) := sup_mu (U(mu)-mu a).
```

Therefore the all-`k,l` inner region requires

```text
b >= max(0, bu(a), bs(a)).
```

Horizon's pinned validator lines 276--299 instead return

```python
max(0, min(bu, bs))
```

and its prompt says symmetry permits either orientation. That union is not
implied by the cited one-sided rate theorem. `audit_tests.py` supplies a strict
union-pass/intersection-fail point at `lambda=.001`: condition (I) already has
margin below `-0.220` at `mu=1/2`, while the scalar test for (II) is positive.
This proves a false positive in the stated rate-envelope certificate. It does
not claim that the point is outside the unknown true region `R` by every
possible argument; no independent argument establishing it was supplied.

The new certificate is unaffected by this gap: `verify_arb.py` requires both
families separately. Strict positive margins also let one enlarge `X,Y`
slightly while retaining (I),(II), so the certified point lies inside `R_*`,
providing the room needed by GNNW BookCor rather than merely on the closure.

### Scalar-envelope reduction

For the reported prior rate `U`, the checker first proves `U''<0` on `(0,1]`.
On `(0,10^-3]` this is not left as a comment: Arb bounds the smooth correction
contribution by `0.660481<1`, while
`-1/(mu(1+mu)) <= -1/0.001001`; their sum is strictly negative. The remaining
interval is subdivided into 4,096 Arb cells.
Then

```text
A(mu)=U(mu)-mu U'(mu),   A'(mu)=-mu U''(mu)>0.
```

Consequently the interior maximizer for `bu` solves `A(mu)=a`; the maximizer
for `bs` solves `U'(mu)=a`. Endpoint cases are retained. The Arb checker derives
and checks these brackets independently rather than importing Horizon code.

## 4. Small lambda: elementary region, no Lemma 14 dependency

The original Horizon splice used GNNW Lemma 14. That lemma's source proof has
an apparent reversed comparison at line 460 and would require an additional
repair. The new checker avoids it completely.

For every `0<lambda<=5*10^-3`, choose

```text
M=lambda exp(-lambda),   Y=1-X.
```

GNNW Observation 7(1) directly gives `(X,1-X) in R`. Moreover, the subsequent
BookCor parameter shrinks `X`; because `X+Y=1`, the shrunk point is strictly
inside the elementary region `x+y<1`, hence in `R_*` by Observation 7(3).

The analytic Arb proof covers the whole open interval, not just a finite tail.
Writing `q=exp(-F')`, it proves coefficient bounds

```text
q_lo lambda <= q <= q_hi lambda,
-log X <= A lambda,
Y=1-X >= M+q-Mq >= D lambda.
```

It also proves `F>0` and `F'>0`. Substitution of
`log M=log lambda-lambda` and `log Y>=log lambda+log D` cancels both singular
`lambda log lambda` terms and yields

```text
main_slack(lambda)/lambda >= 0.00369567987777... > 0
```

uniformly on `(0,5*10^-3]`. This replaces both the questionable Lemma 14 splice
and the earlier overly coarse tail argument.

At `lambda=5*10^-3`, either witness may be chosen. The large certificate starts
there and also passes strictly. Theorem 13 requires `F` to be smooth but imposes
no continuity on `M,X,Y`.

## 5. Piecewise witnesses and finite-net uniformity

On `[5*10^-3,1]`, `M,Y` are piecewise constant on 32,768 cells. Theorem 13 states
no regularity requirement for these auxiliary functions. In its proof at
source lines 416--429, only finitely many parameter values are sampled; nearby
ratios are handled using continuity of `F,F'`. The finite value set here stays
strictly within `(0,1)`, so the BookCor lower threshold `L` can be chosen
uniformly over those sampled parameters.

## 6. Independent verifier and positive control

`verify_arb.py` was written from the formulas and does not import the Horizon
validator. Independent features include:

* python-flint/Arb balls at 256 bits instead of `mpmath.iv`;
* a proof of prior-rate strict concavity;
* separately derived `bu` and `bs` envelope reductions;
* recursive interval subdivision for dependency loss;
* explicit coverage checks and strict verification of both orientations;
* the elementary analytic small-lambda proof above.

`verify_region_direct_arb.py` is a second implementation. It does not import
`verify_arb.py` and does not use the `A(mu)` envelope reduction; it directly
minimizes both convex exponent slacks. For the recommended certificate it
proves lower bounds `8.3465e-7` and `6.0747e-5` in the two orientations.

A generated 32,768-cell certificate for the preprint's target beta `0.03`
against the safe beta `0.08` rate passes the same corrected checker and
returns `3.799202739615937...`; this is the positive control. Target beta
`0.0299` then passes with large-regime main margin `4.9425e-6` and returns the
smaller base above. Beta `0.0298` also passes but has only `4.23e-9` main margin
and is not recommended.

## 7. Remaining status boundary

Supported now:

* the checker first certifies the elementary beta `0.08` prior on all of
  `(0,1]`, recovers beta `0.03` as a positive control, and certifies beta
  `0.0299` under two-sided envelopes;
* the alternative proof chain improves the preprint objective without the
  Lemma 14 iteration, and two independent internal proof reviews accept the
  repaired implication;
* the old `3.7929` numerical objective is not theorem-supported by this audit.

Still desirable before external publication:

* human combinatorics review of the repaired GNNW BookCor/descent chain;
* formalization beyond the two independent Arb implementations;
* archival publication of the certificate and immutable verification log.
