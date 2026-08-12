# Retracted delta: flawed-verifier regression certificate

## Claim status

**Status:** **INVALID AS A RAMSEY UPPER-BOUND CANDIDATE.**  The artifact passes
the pinned public validator, but an independent theorem audit found that the
validator accepts the union of two orientation regions where the GNNW Ramsey
region requires their intersection.

The missing standard-orientation inequality fails near `lambda=0.001` by about
`0.248`, so this is not a rounding-edge case.  This file is retained as a
negative regression example for corrected verifiers.

The certificate is inherited from `sections/solution_code3.tex` in the source
archive of HorizonMath, arXiv:2603.15617v1.  Its piecewise `M` and `Y` witnesses,
breakpoints, split point, shrink factor, and all other polynomial coefficients
are unchanged.

## Exact change

```text
source coefficients:    [-0.25, 0.033, 0.08, 0.0, -0.0778]
candidate coefficients: [-0.25, 0.033, 0.08, 0.0, -0.07795]
```

For

```text
F(lambda) = (1+lambda) log(1+lambda) - lambda log(lambda)
            + exp(-lambda) sum_{i=1}^5 a_i lambda^i,
```

the public validator reports `c = exp(F(1))`.

## Pinned provenance

- HorizonMath paper source: `https://arxiv.org/e-print/2603.15617v1`
- Source archive SHA-256: `47de19e5a03948e65416666e85de8d60d784e0ac8c382a2e8490644b75e78c12`
- Certificate member: `sections/solution_code3.tex`
- HorizonMath repository commit: `d509c90a75202a45585b01f75762188db4fa2d2d`
- Validator file: `validators/ramsey_asymptotic.py`
- Validator SHA-256: `0c8e144e4c7419774be17608413487448969d58a5636423b2fe4bd46e7a14cc2`

## Full validator result

```text
valid: true
c = 3.695879961267919
F(1) = 1.3072186752400892
polynomial degree = 5
analytic tail endpoint = 0.00010845982383068956978
worst small-lambda slack = 0.0002723049533145563055
worst large R_0 slack = 0.00098888192554324787084
worst large main slack = 0.00021556940670870104315
```

The original coefficient `-0.0778` was separately reproduced with
`c = 3.6960839126332994` and positive reported slacks.  Thus the delta improves
the implemented objective by approximately `0.00020395136538` while retaining
positive interval margins in that verifier.

## Decisive failed obligation

If `a=-log(x)`, `b=-log(y)`, and `U(mu)` is a known rate bound for ratios
`0<mu<=1`, membership in the symmetric Ramsey region requires both

```text
a + mu*b >= U(mu),
b + mu*a >= U(mu),
```

for every `mu` in `(0,1]`.  The public function `B_of_a` computes the minimum
of the two boundary thresholds (`min(bu,bs)`), which proves only that one
orientation holds.  The correct intersection test uses their maximum.  The
certificate fails that corrected test.

## Historical proof obligations (now superseded by the failure)

1. Reimplement the interval checks independently rather than reusing the public
   validator.
2. Audit the apparent `F'(lambda)<0` sign typo in the displayed GNNW theorem
   against its proof, which uses the positive-derivative form.
3. Prove that the large-regime `R_0` test is exactly a valid inner Ramsey-region
   test with the orientation and monotonicity used by the validator.
4. Prove the small-regime Lemma 14 splice, including overlap at
   `lambda = 10^-3`.
5. Confirm that piecewise-constant auxiliary witnesses meet all quantifiers and
   regularity requirements of the source theorem.
