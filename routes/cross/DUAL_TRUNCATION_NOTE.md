# Two-sided truncation sensitivity and its remaining comparator gap

Evidence level: **derived for fixed $C$ against a frozen source ledger**.  The
blue reverse induction and the paired common-history comparison are now proved;
identification with a unique final/published HMS comparator remains open.  It
is therefore not yet a Ramsey lower-bound theorem.

Lin--Niu v2 develop an upper-truncated Gaussian refinement on the red side and
state, without carrying through the induction, that the lower-truncated analogue
would add

```text
- beta_blue(p) r^4/d,
beta_blue(p) = gamma_blue(p) a^4 / (8(1-p)^4)
```

to the logarithm of the blue clique-probability bound.  The fixed-$C$ blue
induction and perfect-event extraction are proved in `lower/BLUE_INDUCTION_DRAFT.md`.
With `r=C*l` and `d=D^2*l^2`, it raises the normalized blue exponent relative
to the unit-Hölder companion by

```text
delta_blue = C^3 beta_blue(p_C) / D^2.
```

The analogous variance-only red shift relative to that companion is

```text
delta_red = beta_red(p_C) / D^2.
```

At the transverse crossing of

```text
r_0(p) = -log(p)/2,
b_0(p) = -C log(1-p)/2,
```

let

```text
lambda_C = C p_C / (C p_C + 1-p_C).
```

A first-order implicit-function calculation with *both* curves shifted gives

```text
rho_both(D) - rho_unit_Holder(D)
  = [lambda_C beta_red(p_C)
     + (1-lambda_C) C^3 beta_blue(p_C)] / D^2
    + O(D^-3).
```

The second term is absent from the explicit computation in Lin--Niu.  The
transverse-crossing formula and fixed-$C$ uniform errors are now proved.  A
stronger common-history lemma also compares the refined proof with a frozen HMS
main-body ledger and gives coefficients with `1+gamma` in place of `gamma`.
What has not been proved is that this frozen ledger equals a unique final HMS
reference exponent to order `D^-2`; HMS's optimized appendix uses a different
induction.  That comparator bridge, not the blue induction, is the current
theorem-level blocker.

## Numerical size of the unit-Hölder blue term

The standard-library script `dual_truncation_sensitivity.py` evaluates the
truncated-normal variances and the two sensitivity weights.

| `C` | red coefficient | blue addition | blue/red ratio |
|---:|---:|---:|---:|
| 1.1 | 0.0189110 | 0.0182435 | 0.9647 |
| 2 | 0.0478483 | 0.0366959 | 0.7669 |
| 5 | 0.159336 | 0.0826485 | 0.5187 |
| 10 | 0.339407 | 0.123814 | 0.3648 |
| 100 | 2.08343 | 0.144552 | 0.0694 |

Thus the blue term is material for fixed moderate `C`, nearly
doubling the second-order improvement close to the diagonal.  Its relative
effect decays for large `C`, consistent with the paper's statement that it does
not alter the leading large-`C` asymptotic.

## Remaining proof checklist

1. Define the published HMS reference exponent unambiguously.
2. Prove that the frozen main-body ledger agrees with it up to `o(D^-2)`, or
   reproduce the optimized appendix using the paired common-history deficit.
3. Only after that bridge, optimize finite `D`; an asymptotic positive
   coefficient alone does not give the best explicit numerical Ramsey base.

Primary sources: Lin--Niu arXiv:2605.25843v2 and
Hunter--Milojević--Sudakov arXiv:2512.17718v2.  See
`lower/PAIRED_COMPANION_ATTEMPT.md` for the exact source-line audit.
