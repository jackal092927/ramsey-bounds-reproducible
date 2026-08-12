# Audit of GNNW `t:bookmain` and `t:bookCor`

## Verdict

**YES — provable as stated after local proof repairs.**  The hypothesis
`p > mu` in `l:limit` is unnecessary.  After repairing the quantifier order,
one missing small-epsilon condition, several typographical errors, and the
direction/strictness of the final optimization chain, `t:bookmain` and hence
`t:bookCor` hold for every

$$
0<p,\mu<1.
$$

This audit concerns the imported arXiv v1 source
`/tmp/ramsey-upper-replay.ZfHCv8/RamseyArXiv.tex`, with SHA-256

```
9475bdc42aac1cb2c995fdfba1803f0ec4dc53ac0c5a838623cb31b5e19eaa2e
```

No stronger relation between $p$ and $\mu$ is needed.

## 1. Repaired limit lemma (source lines 279--290)

The correct statement is the following.

**Lemma.** For every $p,\mu\in(0,1)$, as $r\to\infty$ through the positive
integers (and hence through integers for which $p^{1/r}>\mu$),

$$
\lim_{r\to\infty}
(p^{1/r}-\mu)^r(1-\mu)^{1-r}
=p^{1/(1-\mu)}(1-\mu).
$$

Indeed, $p^{1/r}\to1>\mu$, so the base is positive for every sufficiently
large $r$, and

$$
\begin{aligned}
\log\left((p^{1/r}-\mu)^r(1-\mu)^{-r}\right)
&=r\log\left(1+\frac{p^{1/r}-1}{1-\mu}\right)\\
&\longrightarrow \frac{\log p}{1-\mu}.
\end{aligned}
$$

Multiplication by $1-\mu$ proves the formula.  Thus the printed condition
$p>\mu$ is not used and is not needed.

## 2. Correct order of the $r,\varepsilon$ choices (lines 295--304)

Write

$$
B(p,\mu_0)=p^{1/(1-\mu_0)}(1-\mu_0).
$$

The strict hypothesis $x_0<B(p,\mu_0)$ first implies
$x_0+\mu_0<1$, because $p^{1/(1-\mu_0)}<1$.  Use the repaired limit lemma
to choose an **integer $r>1$** for which

$$
x_0<(p^{1/r}-\mu_0)^r(1-\mu_0)^{1-r}.
$$

Only after fixing this $r$ choose $\varepsilon>0$ sufficiently small.  In
addition to the printed conditions, require

$$
\begin{gathered}
p\ge 2\varepsilon,
\qquad (1+\varepsilon)(\mu_0+\varepsilon)\le1,
\qquad x_0+\mu_0+2\varepsilon\le1,\\
(x_0+2\varepsilon,y_0+2\varepsilon)\in\mathcal R_*,\\
\mu_0+2\varepsilon
\le
\frac{\mu_0+\varepsilon}
{(\mu_0+\varepsilon)+(x_0+\varepsilon)},\\
(p-\varepsilon)^{1/r}>\mu_0+3\varepsilon,\\
x_0\le
\left((p-\varepsilon)^{1/r}-\mu_0-3\varepsilon\right)^r
(1-\mu_0-\varepsilon)^{1-r}-\varepsilon.
\tag{2.1}
\end{gathered}
$$

All these conditions can be imposed simultaneously.  The last two follow by
continuity and the strict choice of $r$.  The new monotonicity condition holds
at $\varepsilon=0$ with strict slack because it reduces to
$x_0+\mu_0<1$.  The stronger $\mathcal R_*$ condition follows from openness
of $\mathcal R_*$.

Set, as in the source,

$$
x=x_0+\varepsilon,\qquad y=y_0+\varepsilon,\qquad
\mu=\mu_0+\varepsilon.
$$

The typo on line 304 must be corrected from
`y_0 <= x/(1+eps)` to

$$
y_0\le \frac{y}{1+\varepsilon}.
$$

The analogous inequalities for $x_0$ and $\mu_0$ are valid.  These corrected
relations justify the factor $(1+\varepsilon)^{k+\ell+t}$ on line 307.

The stronger interior choice also repairs line 322.  An interior point of
$\mathcal R$ supplies the required eventual Ramsey bound at its own
coordinates: move slightly northeast while remaining in $\mathcal R$, then
approximate that northeast point by a point in the defining eventual-bound
set.  Therefore, for all sufficiently large $k+\ell$,

$$
R(k,\ell)\le (x+\varepsilon)^{-k}(y+\varepsilon)^{-\ell}.
$$

## 3. Repaired optimization at lines 368--385

Let

$$
a=\frac{|X_R|}{|X|},\qquad b=\frac{|X_B|}{|X|},
\qquad q=1-\frac1r\in(0,1).
$$

The source's line 375 should read $a+b\le1$ (in fact
$a+b=1-|X|^{-1}<1$), not $a+b\le|X|$.  Failure of both induction branches
gives the strict inequality

$$
x^{1/r}a^q+\mu^{1/r}b^q
+\frac{(p-\varepsilon)^{1/r}}{\alpha|X|}
>(p-\varepsilon)^{1/r}.
\tag{3.1}
$$

Define

$$
f(b)=x^{1/r}(1-b)^q+\mu^{1/r}b^q.
$$

Its derivative has the sign of

$$
\frac{\mu}{b}-\frac{x}{1-b},
$$

so $f$ is increasing on
$[0,\mu/(\mu+x)]$.  Since $a\le1-b$ and the newly imposed condition gives

$$
b\le\mu+\varepsilon\le\frac{\mu}{\mu+x},
$$

the needed chain is an **upper** bound, not the printed “lower bound”:

$$
\begin{aligned}
x^{1/r}a^q+\mu^{1/r}b^q
&\le f(b)\\
&\le f(\mu+\varepsilon)\\
&\le x^{1/r}(1-\mu)^q+\mu+\varepsilon.
\end{aligned}
\tag{3.2}
$$

The last step uses
$1-\mu-\varepsilon\le1-\mu$ and
$\mu^{1/r}(\mu+\varepsilon)^q\le\mu+\varepsilon$.

The source correctly proves

$$
\alpha\ge\frac{\varepsilon}{(k+t)^2}
$$

at line 379 and, after increasing $L_0$, proves

$$
\frac{(p-\varepsilon)^{1/r}}{\alpha|X|}\le\varepsilon.
$$

Combining these estimates with the **strict** inequality (3.1) yields

$$
x^{1/r}(1-\mu)^{1-1/r}+\mu+2\varepsilon
>(p-\varepsilon)^{1/r}.
$$

The positivity condition chosen in Section 2 permits raising to the $r$th
power, giving

$$
x>
\left((p-\varepsilon)^{1/r}-\mu-2\varepsilon\right)^r
(1-\mu)^{1-r}.
\tag{3.3}
$$

Since $x=x_0+\varepsilon$ and $\mu=\mu_0+\varepsilon$, (2.1) gives the reverse
non-strict inequality.  This is the required contradiction.  Consequently,
the `>=` symbols printed at lines 377 and 383 must retain the strictness from
line 371: the valid conclusion is `>`.  With the printed non-strict symbols,
line 385 is not a contradiction.

## 4. Induction edge cases and minor line repairs

The following local conventions/branches complete the proof without adding
assumptions.

1. In the big-blue step (lines 333--340), if $b\ge t$, the blue base $S$
   already contains a blue $K_t$.  Otherwise choose exactly $b$ vertices of
   the base and invoke induction with the positive integer $t-b$.
2. If $X_R$ or $X_B$ is empty in lines 356--371, its density is not defined.
   Omit that induction branch and set its weighted contribution to zero.
   Formula (3.1) then follows by continuity, with $0^q=0$.  At least one of
   the two parts is nonempty because line 323 makes $|X|$ large.
3. Line 272 has the inequality sign reversed: decreasing $x$ or $y$ makes
   $x^{-k}y^{-\ell}$ larger.  The stated downward-closure conclusion is
   nevertheless correct.
4. Lines 348 and 350 use `x` where the summation variable is `v`.
5. The apparent occurrences of `|X|||Y'|` and the missing multiplication
   symbols near lines 358 and 384 are TeX typographical errors.

The remaining estimates are uniform once $\ell\ge L_0$: the exponential
factor from line 323 dominates the polynomial and
$\exp(O(\log^3(k+t)))$ terms, and $p-\varepsilon>0$ by construction.

## 5. Consequence for `t:bookCor` (lines 390--395)

Given $(x,y)\in\mathcal R_*$, openness permits choosing $y_0>y$ with
$(x,y_0)\in\mathcal R_*$.  A balanced bipartition maximizing cross-red
density has density at least the global red density $p$.  For large $\ell$,
the condition $(y_0/y)^{\ell/2}\ge3$ ensures that each side has size at least

$$
x^{-k/2}(\mu y_0)^{-\ell/2}.
$$

Applying the repaired `t:bookmain` with $t=\ell$, $x_0=x$,
$\mu_0=\mu$, and the enlarged $y_0$ proves `t:bookCor` exactly as stated.

## 6. Effect on the beta `0.0299` candidate

There is no adverse hidden parameter restriction.  Every finite-net call uses

$$
x_{\lambda,\delta}
< (1-M(\lambda))
p_{\lambda,\delta}^{1/(1-M(\lambda))}
<1-M(\lambda),
$$

so the strict inequality
$x_{\lambda,\delta}+M(\lambda)<1$ needed for the small-epsilon choice holds
algebraically.  On the recommended split-`0.005` certificate's large-lambda
cells,

$$
0.0076223064688733461
\le M(\lambda)\le
0.39254897298540486,
$$

so $M$ is also uniformly separated from $1$.  In the analytic small-lambda
regime, $M(\lambda)=\lambda e^{-\lambda}<1$; the descent argument only asks
for uniformity on compact intervals $[\rho,1]$, not uniformly as
$\lambda\downarrow0$.  Therefore the repaired BookCor applies throughout the
beta `0.0299` construction.

## Exact source-line map

| Source lines | Audit finding | Repair |
|---|---|---|
| 279--290 | Unneeded $p>\mu$ restriction | State the limit for all $p,\mu\in(0,1)$ and take sufficiently large integer $r$ |
| 300--301 | Quantifier order and monotonicity condition omitted | Choose $r>1$ first; then choose $\varepsilon$ with the conditions in Section 2 |
| 300, 322 | Printed $\mathcal R$ membership is too weak for the stated use | Choose $(x_0+2\varepsilon,y_0+2\varepsilon)\in\mathcal R_*$ |
| 304 | $y_0$ compared with $x$ | Replace $x$ by $y$ |
| 333--340 | $t-b\le0$ not separated | If $b\ge t$, stop with a blue $K_t$; otherwise induct |
| 348, 350 | Wrong dummy variable | Replace `x` by `v` |
| 356--371 | Empty-part densities undefined | Omit empty branches and use zero weighted contribution |
| 375 | Dimensionally false sum and wrong bound direction | Use $a+b\le1$ and the upper-bound chain (3.2) |
| 377, 383--385 | Strictness lost, so printed contradiction does not follow | Preserve `>` from line 371, yielding (3.3) against (2.1) |
| 390--395 | Corollary reduction | Valid after the repaired main lemma; no additional $p,\mu$ relation |
