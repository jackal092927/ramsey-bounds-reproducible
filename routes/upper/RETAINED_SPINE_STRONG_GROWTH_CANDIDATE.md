# Retained-spine candidate with strong correlation growth

Date: 2026-08-12

## Claim

Conditional on the frozen $P_6$/BookCor/retained-spine theorem chain and on
`STRONG_SEPARATOR_GROWTH_SHARPENING.md`,

$$
 R(k,k)\le
 \exp\!\left((U(1)-3.445\cdot10^{-6})k+o(k)\right)
 \le(3.780685405)^{k+o(k)}.\tag{1}
$$

## Status and pre-registered gates

**AUTHOR 384-BIT ARB CHECKER PASS; pending non-importing replay and
independent proof referee.**  The candidate was frozen before final replay.
Required gates are: every analytic derivative sign resolves on the complete
wedge, every critical scalar margin is greater than $10^{-9}$, and the safe
decimal improves the current certified $3.780685745$ by at least $10^{-7}$.

## Exact tuple

$$
 \eta=0.0286887,\quad p=0.4713083,\quad
 \delta=0.00005355,
$$

$$
 \lambda_0=13340,\quad \tau=0.000686,
 \quad\Delta=0.000003445,
$$

and the new correlation pair is

$$
 \beta=\frac{11}{250},\qquad
 C=4\frac{619}{250}\left(1+\frac{203}{100000}\right)
 =9.92410512.
$$

The proof is the same complete-square wedge reduction as in
`RETAINED_SPINE_JOINT_OPTIMIZED_CERTIFICATE.md`; no new variational step is
introduced.  For completeness, define

$$
 c_\eta=\log\frac2{1+\eta},\quad
 \Pi=\frac{3\delta}{p}
 +\frac{6\log(1/\delta)\log(1/p)}{\lambda_0},
 \quad q=\log(1/p)+\Pi,
$$

$$
 \rho=\log(2/\beta),\quad
 \Xi=2\rho+4C\lambda_0^{1/3}
 +\frac{12C\log(1/\delta)}{\lambda_0^{2/3}}.
$$

Set $A=U(1)-2c_\eta$ and $E=U'(1)-c_\eta$.  Global strict concavity of
$U$ leaves only the complete ordered wedge

$$0\le x\le y,\qquad xA+(y-x)E\le\Delta.$$

The checker re-proves global concavity and reduces the red, blue, and
reservoir branches to their certified endpoints.  In particular, it checks
the fragile red sloping-boundary and blue diagonal derivatives cellwise on
4,096 exact rational cells rather than enclosing either full interval in a
single dependency-inflated box.

The author replay gives the following strict lower margins:

$$
 \tau(1/2-\eta-p)>2.05\cdot10^{-9},
$$

$$
 U(1)-\Delta-P_R>3.82\cdot10^{-9},
$$

$$
 U(1)-\Delta-P_B>3.45\cdot10^{-6},
$$

$$
 U(1)-\Delta-P_{\rm reservoir}>1.47\cdot10^{-5}.
$$

Finally, outward-rounded evaluation proves

$$
 \exp(U(1)-\Delta)<3.780685403313<3.780685405,
$$

with more than $10^{-9}$ rounding margin.  This proves (1) under the pinned
dependencies.

## Claim boundary

The claim remains asymptotic and theorem-linked.  It does not supply a
finite-$k$ threshold and makes no unconditional, global-optimality, or
priority claim.  It must not replace canonical documents until an
implementation-independent replay and proof review pass.

## Reproduction

```text
.venv/bin/python routes/upper/check_strong_separator_growth.py
.venv/bin/python routes/upper/check_retained_spine_strong_growth.py
```
