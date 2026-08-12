# Proof Package: two-sided truncated-Gaussian correction

## Claim

Fix $C>1$, and let $p_C\in(0,1/2)$ be the unique solution of

$$
p_C=(1-p_C)^C.
$$

Suppose a Gaussian-random-graph Ramsey construction has normalized red and
blue clique exponents $R_D(p)$ and $B_D(p)$, where $D\to\infty$, with a
transverse optimizing crossing at $p=p_C+O_C(D^{-1})$. Suppose further that
refined upper- and lower-truncated Gaussian estimates change these exponents by

$$
R_D^+(p)=R_D(p)+\frac{\beta_R(p)}{D^2}+O_C(D^{-3}),
\qquad
B_D^+(p)=B_D(p)+\frac{C^3\beta_B(p)}{D^2}+O_C(D^{-3}),
$$

with the same expansions after one differentiation in $p$, uniformly in a
fixed neighborhood of $p_C$. Then

$$
\max_p\min\{R_D^+(p),B_D^+(p)\}
=
\max_p\min\{R_D(p),B_D(p)\}
+\frac{K_2(C)}{D^2}+O_C(D^{-3}),
$$

where

$$
K_2(C)=\lambda_C\beta_R(p_C)
+(1-\lambda_C)C^3\beta_B(p_C),
\qquad
\lambda_C=\frac{Cp_C}{Cp_C+1-p_C}.
$$

Writing $c_C>0$ for the number satisfying $\Phi(-c_C)=p_C$, and
$a_C=\phi(c_C)$, the coefficients proposed by the truncated-normal
calculation are

$$
\begin{aligned}
\gamma_R&=\frac{a_C}{p_C}\left(\frac{a_C}{p_C}-c_C\right),
&\beta_R&=\frac{\gamma_Ra_C^4}{8p_C^4},\\
\gamma_B&=\frac{a_C}{1-p_C}\left(\frac{a_C}{1-p_C}+c_C\right),
&\beta_B&=\frac{\gamma_Ba_C^4}{8(1-p_C)^4}.
\end{aligned}
$$

In particular, $K_2(C)>\lambda_C\beta_R(p_C)>0$. Relative to a
red-only refinement, the conditional new contribution is

$$
\frac{(1-\lambda_C)C^3\beta_B(p_C)}{D^2}+O_C(D^{-3}).
$$

## Status

**PROVABLE AS AN OPTIMIZATION LEMMA; THE RAMSEY APPLICATION STILL NEEDS A
PAIRED COMPANION INDUCTION.**

The optimization claim above is proved below. The omitted blue perfect-event
induction and extraction are now written in
[BLUE_INDUCTION_DRAFT.md](./BLUE_INDUCTION_DRAFT.md), relative to a matched
$P_D\to1$ unit-proxy Hölder companion. However,
[EXACT_COMPANION_AUDIT.md](./EXACT_COMPANION_AUDIT.md) shows that this
companion is not the literal HMS expansion: HMS uses a $P=2$ split and has
twice the leading linear-MGF coefficient. Consequently, the unconditional
Ramsey improvement is **not currently justified here** until a pathwise
quartic-resolved comparison is proved.

## Assumptions

1. $C>1$ is fixed before $D\to\infty$ and then $\ell\to\infty$. No uniform
   claim as $C\to\infty$ is made.
2. Near $p_C$, the unperturbed exponents and their first derivatives obey

   $$
   R_D(p)=-\tfrac12\log p+O_C(D^{-1}),\qquad
   B_D(p)=-\tfrac C2\log(1-p)+O_C(D^{-1}).
   $$

3. The maximum of the minimum is attained at the unique local transverse
   crossing of the decreasing red and increasing blue curves.
4. The two $D^{-2}$ clique-probability corrections, including their $C^1$
   error estimates, hold as stated in the Claim.

## Notation

- $\phi,\Phi$: standard normal density and distribution function.
- $R_D,B_D$: clique exponents normalized so that both can be compared to
  $\rho=\ell^{-1}\log n$. In particular, the blue log-probability is divided
  by $C\ell^2$.
- $D$: dimension scale in $d=D^2\ell^2$.
- $\lambda_C$: sensitivity of the crossing to a vertical red shift.

## Proof Strategy

First derive both variance deficits exactly from truncated-normal moments.
Then perturb the transverse intersection of the red and blue exponent curves.
The $C^3$ factor is checked before the perturbation by normalizing the blue
clique probability at $r=C\ell$.

## Dependency Map

1. The coefficient formulas depend only on elementary truncated-normal
   moment identities.
2. The $C^3$ factor depends on $r=C\ell$, $d=D^2\ell^2$, and blue
   normalization by $C\ell^2$.
3. The weighted sum depends on a first-order Taylor expansion at a transverse
   crossing.
4. A Ramsey theorem additionally depends on the currently missing paired
   HMS-versus-refined companion induction. Blue propagation and extraction
   relative to the unit-Hölder baseline are no longer the gap.

## Proof

### Step 1: truncated-normal variance deficits

Let $c=c_C$, $a=a_C$, and $p=p_C$. For $Z\sim N(0,1)$, integration by parts
gives

$$
\mathbb E[Z\mid Z\le -c]=-\frac ap,
\qquad
\mathbb E[Z^2\mid Z\le -c]=1+c\frac ap.
$$

Therefore

$$
1-\operatorname{Var}(Z\mid Z\le-c)
=\left(\frac ap\right)^2-c\frac ap
=\gamma_R.
$$

The inverse Mills inequality $a/p>c$ for $c>0$ shows $\gamma_R>0$. Similarly,

$$
\mathbb E[Z\mid Z\ge -c]=\frac a{1-p},
\qquad
\mathbb E[Z^2\mid Z\ge -c]=1-c\frac a{1-p},
$$

and hence

$$
1-\operatorname{Var}(Z\mid Z\ge-c)
=c\frac a{1-p}+\left(\frac a{1-p}\right)^2
=\gamma_B>0.
$$

Substitution in the quadratic correction stated by Lin--Niu gives the
displayed $\beta_R,\beta_B$. Both are strictly positive.

### Step 2: the blue normalization is $C^3\beta_B/D^2$

Assume the lower-truncated induction gives a multiplicative clique-probability
correction

$$
\exp\left(-\beta_B\frac{r^4}{d}
+O_C(D^{-1})\frac{r^4}{d}
+o_\ell\!\left(\frac{r^4}{d}\right)\right).
$$

For a blue clique, $r=C\ell$ and $d=D^2\ell^2$. Its normalized exponent is
minus the log probability divided by $C\ell^2$. Thus the leading shift is

$$
\frac{\beta_B C^4\ell^4}{D^2\ell^2}\cdot
\frac1{C\ell^2}
=\frac{C^3\beta_B}{D^2}.
$$

The displayed error becomes $O_C(D^{-3})+o_\ell(D^{-2})$. This verifies both
the power and sign of $C$.

### Step 3: perturb the transverse crossing

Let $p_D$ be the unperturbed optimizing crossing. By Assumptions 2--3,
$p_D=p_C+O_C(D^{-1})$. Write

$$
r'=R_D'(p_D)=-\frac1{2p_C}+O_C(D^{-1}),
\qquad
b'=B_D'(p_D)=\frac C{2(1-p_C)}+O_C(D^{-1}).
$$

In particular, $r'<0<b'$. Let the perturbed crossing be $p_D+h$.
Subtracting the two perturbed curve equations and applying Taylor's theorem
gives

$$
(r'-b')h
+\frac{\beta_R(p_C)-C^3\beta_B(p_C)}{D^2}
=O_C(D^{-3})+O_C(h^2).
$$

Transversality first implies $h=O_C(D^{-2})$, so $h^2=O_C(D^{-4})$, and

$$
h=\frac{\beta_R(p_C)-C^3\beta_B(p_C)}{b'-r'}D^{-2}
+O_C(D^{-3}).
$$

Evaluating the perturbed common height using the blue curve yields

$$
\begin{aligned}
\Delta\rho
&=b'h+\frac{C^3\beta_B(p_C)}{D^2}+O_C(D^{-3})\\
&=\left(
\frac{b'}{b'-r'}\beta_R(p_C)
+\frac{-r'}{b'-r'}C^3\beta_B(p_C)
\right)D^{-2}+O_C(D^{-3}).
\end{aligned}
$$

At leading order,

$$
\frac{b'}{b'-r'}
=\frac{Cp_C}{Cp_C+1-p_C}+O_C(D^{-1})
=\lambda_C+O_C(D^{-1}).
$$

Multiplication by $D^{-2}$ absorbs the last error into $O_C(D^{-3})$.
This proves the formula for $K_2(C)$. Since both beta coefficients and both
weights are positive, the strict positivity and the red-only comparison
follow. $\square$

## Corrections or Missing Assumptions

- Lin--Niu's lower-truncated cumulant lemma is local: its remainder is
  $O_{b,M}(D^{-1})$. For fixed $C$, the cutoff $b=-c_C$ is fixed and this is
  compatible with an $O_C(D^{-3})$ normalized error. This does not establish
  uniformity when $C\to\infty$.
- The centered blue tilts and extraction have been checked in
  **BLUE_INDUCTION_DRAFT.md** for fixed $C$. The unresolved point is earlier
  in the comparison: the Lin--Niu $1/2$ unit-Hölder coefficient is not the
  coefficient $1$ in the HMS $P=2$ source expansion.

## Open Risks

1. A generic HMS $O(r^4/d)$ error cannot certify a named $r^4/d$
   improvement. All common history-dependent terms must be coupled before
   their difference is taken.
2. Constants in the local lower-truncated remainder may grow rapidly with
   $C$; the numerical large-$C$ table is not a uniform asymptotic proof.
3. The Lin--Niu preprint itself has not been treated here as peer-reviewed.
