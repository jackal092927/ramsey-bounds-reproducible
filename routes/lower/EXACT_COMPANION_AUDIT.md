# Exact companion audit: HMS versus the refined blue quartic term

> **Second-stage resolution (2026-08-12).** The paired common-history
> propagation requested below is now proved, for fixed $p,C$, relative to an
> explicitly frozen source-faithful HMS main-body ledger; see
> [PAIRED_COMPANION_ATTEMPT.md](./PAIRED_COMPANION_ATTEMPT.md). Thus the
> historical **[OPEN]** statements below should now be read as the outcome of
> the first source audit. The remaining gap is narrower: identify that frozen
> ledger with a uniquely defined published/final HMS comparator (or reproduce
> the optimized appendix with the same paired ledger). No new Ramsey lower
> bound is claimed.

## Outcome

The requested source-to-formula alignment does **not** validate the currently
quoted coefficient as an improvement over the HMS preprint's induction.

What can be proved is more precise:

1. **[DERIVED, proved below]** Relative to a newly introduced
   $P_D\to1$ Hölder induction that still uses the unit variance proxy, the
   lower-truncated variance refinement saves

   $$
   \beta_B(p)\frac{r^4}{d},
   \qquad
   \beta_B(p)=\frac{\gamma_B(p)a^4}{8(1-p)^4}.
   $$

2. **[DERIVED, local moment comparison proved below]** Relative to the actual
   Cauchy--Schwarz ($P=2$) expansion in HMS, the leading local saving is larger:

   $$
   \widetilde\beta_B(p)\frac{r^4}{d},
   \qquad
   \widetilde\beta_B(p)
   =\frac{(1+\gamma_B(p))a^4}{8(1-p)^4}.
   $$

   The extra ``$1$'' is the gain from changing the splitting exponent from
   $P=2$ to $P_D=1+O(D^{-1})$; the $\gamma_B$ is the directional
   truncated-variance gain.

3. **[OPEN]** Neither HMS nor Lin--Niu supplies the quartic-resolved, pathwise
   reverse-induction comparison needed to propagate the second statement
   through all histories while cancelling the other order-$r^4/d$ terms.
   Therefore neither coefficient is claimed here as a new Ramsey lower bound.

The first missing statement is not a subtle large-$C$ uniformity estimate. It
occurs earlier: Lin--Niu identify the HMS companion coefficient as $1/2$, while
the HMS source gives coefficient $1$ before the same quantity. The needed
repair is the **paired companion induction lemma** stated near the end of this
document.

## Evidence status

- **[SOURCE]** literal statement in the latest primary-source preprint.
- **[DERIVED]** proved below from the displayed source lemmas.
- **[CONDITIONAL]** follows if the named missing induction lemma is proved.
- **[OPEN]** not established by the inspected sources or this note.

## Source snapshots

The arXiv API was queried on 2026-08-12. It reports HMS v2, updated
2026-05-18, and Lin--Niu v2, updated 2026-07-02.

| Source | Version used | Local source file SHA-256 |
|---|---|---|
| Hunter--Milojević--Sudakov, *Gaussian random graphs and Ramsey numbers* | [arXiv:2512.17718v2](https://arxiv.org/abs/2512.17718v2) | `b72958ac35554eccb94dedab5800349d2c021af7d60f767125cb46998e0fd54a` |
| Lin--Niu, *Sharper Ramsey lower bounds from refined Gaussian estimates* | [arXiv:2605.25843v2](https://arxiv.org/abs/2605.25843v2) | `dbf1bfa2c7603c81b2e56a97028b138ccf9a9299a3d1f20c0b08cf489136f429` |
| Barreto--Marchal--Arbel, *Optimal sub-Gaussian variance proxy for truncated Gaussian and exponential random variables* | [arXiv:2403.08628v2](https://arxiv.org/abs/2403.08628v2) | arXiv HTML used for the theorem statement |

The line numbers below refer to the two hashed TeX source files.

## Source-line-to-formula map

| Source lines | Literal role | Formula obtained | Audit conclusion |
|---|---|---|---|
| HMS 349--354 | Stated quadratic exponential-moment lemma | $\log\mathbb E e^{\lambda S}\le \lambda\mathbb ES+\lambda^2k^2d^{-1}\sum_i\mu_i^2+4|\lambda|k/d$ | The displayed HMS coefficient has no $1/2$. |
| HMS 895--904 | Decompose $S=\mathbb ES+L+Q$ and apply Cauchy--Schwarz | The split is Hölder with $P=Q=2$. | This is the origin of the factor $1$, rather than $1/2$, on the linear factor. |
| HMS 906--913 | Bound the linear factor | Before the last Cauchy bound, its contribution after the square root is $\lambda^2d^{-1}\sum_iA_i^2$. | The exact pre-coarsening HMS companion is coefficient $1$. |
| HMS 915--935 | Bound the centered quadratic factor and combine | The remainder is $4|\lambda|k/d$. | This is the same remainder obtained after the $P_D,Q_D$ split. |
| HMS 609--636 | Invoke the lemma in the main blue induction | With $\lambda=a\sqrt d/(1-p)$ and $\mu_i=a/[(1-p)\sqrt d]+O(1/(D\sqrt d))$, the hidden one-step quartic is $a^4k^3/[(1-p)^4d]+O(k^3/(Dd))$. | Its leading coefficient is $1$, not $1/2$. |
| HMS 547--573 and 645--658 | Blue auxiliary claim and final perfect probability | The one-step term is hidden in $O(k^3/d)$ and the accumulated term in $O(r^4/d)$. | HMS does not state a quartic-resolved companion expansion. |
| HMS 1103--1134 | Appendix blue proof | It again invokes the same HMS lemma and again has the factor $1+2\lambda k/d$. | The appendix contains no alternative $1/2$ expansion. |
| Barreto--Marchal--Arbel, HTML 83--102 | Optimal variance proxy for a one-sided truncated Gaussian | The optimal **global** variance proxy equals the original Gaussian variance $1$. | The unit proxy used by HMS is globally exact; the smaller conditional variance is only usable directionally or locally. |
| Lin--Niu 241--248 | Import the HMS quadratic lemma | The imported formula again has $\lambda^2k^2d^{-1}\sum_i\mu_i^2$. | Their own citation agrees with HMS coefficient $1$. |
| Lin--Niu 591--670 | Replace Cauchy by Hölder with $P_D\to1$ and use the truncated CGF | The linear contribution is $(1-\gamma+O(D^{-1}))\lambda^2(k-1)^2(2d)^{-1}\sum_i\mu_i^2$. | The factor $1/2$ already includes a new Hölder improvement, before using $\gamma$. |
| Lin--Niu 673--724 | Centered quadratic factor | After taking the $1/Q_D$ power, the remainder is $4|\lambda|k/d$. | The centered remainder matches HMS and does not repay the factor-$1/2$ gain. |
| Lin--Niu 1004--1031 | Accumulate $\sum_t t(t-1)^2$ | The variance-only subtraction is $-\gamma a^4r^4/(8p^4d)+O(r^3/d)$. | Correct relative to the newly defined unit-Hölder baseline. |
| Lin--Niu 1048--1061 | Identify the positive unit term with the HMS factor | The text says it “reproduces” HMS up to a generic error. | A generic $O(r^4/d)$ cannot certify equality of its order-$r^4/d$ coefficient. |
| Lin--Niu 1200--1216 | Explicit HMS comparison | It asserts the HMS contribution is $a^4k(k-1)^2/(2p^4d)$. | This is the earliest unsupported source-level identification; HMS gives twice this coefficient before lower-order polynomial changes. |
| Lin--Niu 1535--1557 | Blue concluding remark | It states a local lower-truncated lemma and $\beta_B=\gamma_Ba^4/[8(1-p)^4]$, but omits the induction. | This is a source remark, not the missing companion proof. |

## Why the two coefficients differ

Fix a blue exposure step, put $q=1-p$, and write

$$
\lambda=\frac{a\sqrt d}{q}>0,
\qquad
S=\sum_{1\le i<j\le k}X_iX_j.
$$

Under the blue conditioning, the $X_i$ are independent lower-truncated
Gaussians. Set

$$
\mu_i=\mathbb EX_i,
\qquad
\xi_i=X_i-\mu_i,
\qquad
A_i=\sum_{j\ne i}\mu_j.
$$

Then

$$
S=\mathbb ES+\sum_iA_i\xi_i+\sum_{i<j}\xi_i\xi_j.
$$

The perfect-sequence cutoff estimates give, uniformly for fixed $p,C$,

$$
\mu_i=\frac{a}{q\sqrt d}+O_{p,C}\!\left(\frac1{D\sqrt d}\right),
\qquad
\sum_iA_i^2
=\frac{a^2}{q^2d}k(k-1)^2
+O_{p,C}\!\left(\frac{k^3}{Dd}\right).
$$

### The exact pre-coarsening HMS envelope

Stopping the HMS proof before its final Cauchy bound on $\sum_iA_i^2$ gives

$$
H_k
=\lambda\mathbb ES
+\frac{\lambda^2}{d}\sum_iA_i^2
+\frac{4\lambda k}{d}.
$$

The coefficient $1$ comes from applying Cauchy--Schwarz to the linear and
centered-quadratic exponential factors: the linear MGF is evaluated at
$2\lambda$, and the square root changes its coefficient from $2$ to $1$.

### A new unit-proxy Hölder envelope

Choose

$$
Q_D=\frac{D}{8C(a/q)},
\qquad
P_D=\frac{Q_D}{Q_D-1},
$$

for sufficiently large $D$ (rounding $Q_D$ down, if desired, changes only
constants). Since $k\le C\ell$ and $d=D^2\ell^2$,
$d\ge4Q_D\lambda k$, while
$P_D=1+O_{p,C}(D^{-1})$. Hölder's inequality, the unit subgaussian proxy on
the linear factor, and the centered HMS lemma on the quadratic factor give

$$
U_k
=\lambda\mathbb ES
+\left(\frac12+O_{p,C}(D^{-1})\right)
\frac{\lambda^2}{d}\sum_iA_i^2
+\frac{4\lambda k}{d}.
$$

Thus even without a variance deficit, the change $P=2$ to $P_D\to1$ saves
one half of the HMS linear contribution.

### The refined lower-truncated envelope

For a standardized cutoff $b_i=-c_p+O_{p,C}(D^{-1})$, define

$$
V_B=\operatorname{Var}(Z\mid Z\ge-c_p)=1-\gamma_B,
$$

where

$$
\gamma_B
=\frac{a}{q}\left(c_p+\frac{a}{q}\right)>0.
$$

The centered standardized tilt is

$$
u_i=\frac{P_D\lambda A_i}{\sqrt d}=O_{p,C}(D^{-1}).
$$

The exact centered lower-truncated CGF satisfies

$$
K_b''(u)=\operatorname{Var}(Z\mid Z\ge b-u).
$$

Smoothness on a fixed compact neighborhood of $-c_p$ therefore yields

$$
K_{b_i}(u_i)
\le \frac{u_i^2}{2}
\left(V_B+O_{p,C}(D^{-1})\right).
$$

Consequently the refined envelope is

$$
R_k
=\lambda\mathbb ES
+\left(\frac{1-\gamma_B}{2}+O_{p,C}(D^{-1})\right)
\frac{\lambda^2}{d}\sum_iA_i^2
+\frac{4\lambda k}{d}.
$$

Subtracting the three envelopes gives two different, valid comparisons:

$$
U_k-R_k
=\frac{\gamma_Ba^4}{2q^4d}k(k-1)^2
+O_{p,C}\!\left(\frac{k^3}{Dd}\right),
$$

but

$$
H_k-R_k
=\frac{(1+\gamma_B)a^4}{2q^4d}k(k-1)^2
+O_{p,C}\!\left(\frac{k^3}{Dd}\right).
$$

This proves the local source-alignment claim. The same calculation with
$\lambda<0$, upper truncation, and
$\gamma_R=(a/p)(a/p-c_p)$ applies on the red side.

## Exact finite sum and all relative scales

The exact accumulation polynomial is

$$
\sum_{k=1}^{r-1}k(k-1)^2
=\frac{r(r-1)(r-2)(3r-5)}{12}
=\frac{r^4}{4}+O(r^3).
$$

Therefore a quartic-resolved paired induction would give

$$
\log P_{\mathrm{blue},r}^{\mathrm{ref}}
\le
\log P_{\mathrm{blue},r}^{\mathrm{unit\text{-}H\ddot{o}lder}}
-\frac{\gamma_Ba^4}{8q^4}\frac{r^4}{d}
+O_{p,C}\!\left(\frac{r^3}{d}\right)
+O_{p,C}\!\left(\frac{r^4}{Dd}\right),
$$

or, relative to the exact pre-coarsening HMS $P=2$ companion,

$$
\log P_{\mathrm{blue},r}^{\mathrm{ref}}
\le
\log P_{\mathrm{blue},r}^{\mathrm{HMS\text{-}exact}}
-\frac{(1+\gamma_B)a^4}{8q^4}\frac{r^4}{d}
+O_{p,C}\!\left(\frac{r^3}{d}\right)
+O_{p,C}\!\left(\frac{r^4}{Dd}\right).
$$

These two displays are **[CONDITIONAL]** on the global paired companion lemma;
the local one-step comparison preceding them is **[DERIVED]**.

For $r=C\ell$ and $d=D^2\ell^2$, after dividing the negative log blue
probability by $C\ell^2$:

| Log-probability term | Normalized scale |
|---|---:|
| $r^4/d$ | $C^3D^{-2}$ |
| $r^4/(Dd)$ | $C^3D^{-3}$ |
| $r^3/d$ | $O_C(D^{-2}\ell^{-1})$ |
| accumulated $\sum_k4\lambda k/d$ | $O_{p,C}(D^{-1}\ell^{-1})$ |
| perfectness/extraction remainder | $o_\ell(D^{-2})$ for fixed $p,C,D$ |

The order of limits is important: first $C$ is fixed, then the
Ramsey-scale limit $\ell\to\infty$ is taken, and only then may $D$ be treated
as a large auxiliary constant. The local lower-truncated remainder is uniform
for $p$ in a fixed neighborhood of $p_C$, because the cutoffs and tilts remain
in a fixed compact set. No uniform claim as $C\to\infty$ follows.

## Why generic HMS errors cannot finish the comparison

Some terms which are harmless for a first-order HMS theorem are exactly as
large as the desired quartic correction. For example, expanding the
history-dependent means separately produces

$$
O_{p,C}\!\left(\frac{r^3}{D\sqrt d}\right)
=O_{p,C}\!\left(\frac{\ell^2}{D^2}\right)
$$

when $r=\Theta_C(\ell)$. This is the same log scale as $r^4/d$. It cancels
only if the HMS and refined recurrences retain the **same exact conditional
means, connection factors, cutoffs, and perfectness histories** before their
difference is taken. Absorbing it into an unspecified $K r^4/d$ and then
subtracting a named beta coefficient is not a valid coefficient comparison.

## Minimal supplemental lemma

The earliest missing result can be isolated as follows.

> **Paired quartic companion induction lemma [OPEN].** Fix $p\in(0,1)$ and
> $C>1$. For every perfect Bartlett history and every
> $k\le C\ell$, retain the exact conditional means $\mu_i$, coefficients
> $A_i$, connection probability, and deterministic term $\lambda\mathbb ES$.
> Let $\mathcal H_s$ be the reverse-induction envelope obtained from the
> pre-coarsening HMS $P=2$ moment bound, and let $\mathcal R_s$ use the
> $P_D\to1$ lower-truncated CGF bound. Then, uniformly over those histories,
>
> $$
> \log\mathcal R_0-\log\mathcal H_0
> \le
> -\frac{(1+\gamma_B)a^4}{8(1-p)^4}\frac{r^4}{d}
> +O_{p,C}\!\left(\frac{r^4}{Dd}+\frac{r^3}{d}\right),
> $$
>
> and the same estimate survives greedy removal of the perfect-event star up
> to $o_\ell(r^4/d)$.

A weaker version comparing $\mathcal R_s$ to the new unit-Hölder envelope
has $\gamma_B$ in place of $1+\gamma_B$. That weaker lemma would justify the
coefficient stated in the Lin--Niu concluding remark, but it would compare to
a newly sharpened companion, not to the HMS source expansion.

The lemma must be pathwise or recursively coupled. A standalone probability
bound with an unspecified $O(r^4/d)$ constant is insufficient.

## Conditional crossing constants

Let $p_C=(1-p_C)^C$, $q_C=1-p_C$, and

$$
\lambda_C=\frac{Cp_C}{Cp_C+q_C}.
$$

### If the comparator is the new unit-Hölder induction

The variance-only two-sided coefficient is

$$
K_{\mathrm{unit}}(C)
=\lambda_C\frac{\gamma_Ra_C^4}{8p_C^4}
+(1-\lambda_C)C^3
\frac{\gamma_Ba_C^4}{8q_C^4}.
$$

This is the coefficient already computed in the two-sided truncation note.

### If the comparator is the actual HMS $P=2$ expansion

If the paired companion lemma and its red analogue are proved, the candidate
coefficient becomes

$$
K_{\mathrm{HMS}}^{\mathrm{candidate}}(C)
=\lambda_C\frac{(1+\gamma_R)a_C^4}{8p_C^4}
+(1-\lambda_C)C^3
\frac{(1+\gamma_B)a_C^4}{8q_C^4}.
$$

If only the blue refinement is added to an otherwise fixed HMS comparison,
the candidate gain is instead

$$
(1-\lambda_C)C^3
\frac{(1+\gamma_B)a_C^4}{8q_C^4}\,D^{-2}
+O_C(D^{-3}).
$$

The transverse-crossing $O_C(D^{-3})$ is valid for fixed $C$: the optimizer
moves by $O_C(D^{-2})$, the unperturbed crossing is
$p_C+O_C(D^{-1})$, and the beta functions are $C^1$ in a fixed neighborhood.

For orientation only, the exact-companion script gives:

| $C$ | variance-only $K_{\mathrm{unit}}$ | candidate $K_{\mathrm{HMS}}$ |
|---:|---:|---:|
| 1 | 0.0322515 | 0.0829121 |
| 1.1 | 0.0371545 | 0.0955225 |
| 2 | 0.0845442 | 0.2180270 |
| 5 | 0.2419841 | 0.6307886 |
| 10 | 0.4632213 | 1.2162643 |
| 100 | 2.2279771 | 5.5920060 |

All entries multiply $D^{-2}$. They are **[COMPUTED] candidate
coefficients**, not proved Ramsey improvements.

## Final audit verdict

- The inverse Mills and variance formulas have the correct signs.
- The blue normalization is $C^3$, not $C^4$.
- Fixed-$C$ local CGF uniformity is adequate for an $O_C(D^{-3})$ normalized
  remainder; large-$C$ uniformity is not available.
- The first fatal alignment gap is the claimed HMS coefficient $1/2$.
  Source-level HMS uses $1$.
- A local comparison can be proved and predicts a larger $(1+\gamma_B)$
  coefficient against HMS.
- A new Ramsey lower bound must not be claimed until the paired quartic
  companion induction lemma is written and checked on both colors.
