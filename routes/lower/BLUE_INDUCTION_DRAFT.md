# Proof draft: lower-truncated blue Bartlett induction

## Claim

Fix $C>1$ and $p\in(0,1)$, and let

$$
\Phi(-c_p)=p,\qquad a=\phi(c_p),\qquad d=D^2\ell^2.
$$

Assume $D$ is sufficiently large as a function of $p,C$, and
$1\le r\le C\ell$. Use the Gaussian random graph notation of
Hunter--Milojević--Sudakov and Lin--Niu: $C_s$ is the event that vertices
$s+1,\ldots,r$ form a blue clique, $B_r$ is the perfect-sequence event, and
$M[s]$ denotes the first $s$ exposed Bartlett columns.

For $0\le s\le r-1$, put

$$
\Sigma_s=
\sum_{s<i<j\le r}
\left\langle\pi_s(\mathbf y_i),\pi_s(\mathbf y_j)\right\rangle,
$$

and define

$$
\gamma_B(p)
=1-\operatorname{Var}(Z\mid Z\ge-c_p)
=\frac{a}{1-p}\left(c_p+\frac{a}{1-p}\right)>0.
$$

Let

$$
\mathcal E_t=
\frac{t^2}{D\sqrt d}
+\frac{t^3}{Dd}
+\frac{t}{\sqrt d}
+t\delta
$$

be the one-step error scale, with $\delta$ the perfectness parameter. Define

$$
\mathcal R^B_{s,r}
=
\sum_{m=s+1}^{r-1}
\left[
(1-\gamma_B(p))
\frac{a^4}{2(1-p)^4d}
(r-m)(r-m-1)^2
+O_{p,C}(\mathcal E_{r-m})
\right].
$$

Then, conditional on the source lemmas listed below,

$$
\mathbb P[C_s\wedge B_r\mid M[s]]
\le
(1-p)^{\binom{r-s}{2}}
\exp\left(
\frac{a\sqrt d}{1-p}\Sigma_s
+\frac{a^3}{(1-p)^3\sqrt d}\binom{r-s}{3}
+\mathcal R^B_{s,r}
\right).
$$

At $s=0$, this replaces the quartic contribution in the **new
$P_D\to1$ unit-proxy Hölder induction** by $1-\gamma_B(p)$. Relative to that
otherwise identical unit-proxy induction,
the logarithmic blue clique bound improves by

$$
-\beta_B(p)\frac{r^4}{d}
+O_{p,C}\left(\frac{r^3}{d}\right)
+O_{p,C}(D^{-1})\frac{r^4}{d},
\qquad
\beta_B(p)=\frac{\gamma_B(p)a^4}{8(1-p)^4}.
$$

For $r=\Theta_C(\ell)$, the same comparison holds for the unconditional blue
clique probability $P_{\mathrm{blue},r}$, up to an additive $o(1)$ in its log
upper bound. In particular, the greedy perfect-subsequence extraction does
not consume an order-$r^4/d$ improvement.

## Status

**PROVABLE AS STATED, conditional on the explicitly named source lemmas and
relative to the new unit-Hölder companion.**

This document fills the term-by-term perfect-sequence induction omitted from
the concluding remark of Lin--Niu and verifies that the standard extraction
preserves the gain for Ramsey-scale cliques. It does **not** identify that
unit-Hölder companion with the HMS source expansion. The source audit in
[EXACT_COMPANION_AUDIT.md](./EXACT_COMPANION_AUDIT.md) shows that HMS uses a
$P=2$ split with twice the leading linear-MGF coefficient. A new Ramsey
theorem therefore still requires the paired companion induction stated there.

## Assumptions imported from the source papers

1. **Blue connection estimate.** Given $M[s-1]$,

   $$
   \mathbb P\left[\bigwedge_{i=s+1}^r E_{s,i}\mid M[s-1]\right]
   \le
   (1-p)^{r-s}
   \exp\left(
   \frac{a\sqrt d}{1-p}
   \sum_{i=s+1}^r
   \langle\pi_{s-1}(\mathbf y_s),\pi_{s-1}(\mathbf y_i)\rangle
   +O_{p,C}((r-s)\delta)
   \right).
   $$

2. **Lower-truncated local CGF.** If
   $Y=Z-\mathbb E[Z\mid Z\ge b]$, then, uniformly for
   $|u|\le M/D$,

   $$
   \log\mathbb E[e^{uY}\mid Z\ge b]
   \le
   \frac{u^2}{2}
   \left(\operatorname{Var}(Z\mid Z\ge b)+O_{b,M}(D^{-1})\right).
   $$

3. **Centered quadratic lemma.** The exponential moment of
   $\sum_{i<j}\xi_i\xi_j$ for independent centered truncated Gaussians is
   bounded using variance proxy $1/d$, as in HMS.
4. **Perfect-sequence cutoff control.** Every conditional cutoff equals
   $-c_p+O_{p,C}(D^{-1})$ after standardization, and every conditional mean
   equals

   $$
   \mu_i=\frac{a}{(1-p)\sqrt d}
   +O_{p,C}\left(\frac1{D\sqrt d}\right)>0.
   $$

5. **Perfectness concentration.** In the greedy extraction, a discarded
   vector has conditional probability at most
   $\eta^{\ell}$ with $\eta=(p/10)^{10C}$. This is the norm/projection
   concentration estimate used in HMS.

## Dependency Map

1. The refined exponential-moment lemma uses Assumptions 2--4 and Hölder's
   inequality.
2. The reverse induction uses the refined moment lemma and Assumption 1.
3. The quartic coefficient follows from the exact finite sum
   $\sum_{t=1}^{r-1}t(t-1)^2$.
4. Removing $B_r$ at Ramsey scale uses Assumption 5 and a union bound over the
   kept subsequence.

## Proof

### Step 1: refined blue exponential moment

Fix an induction step $s$ and write $k=r-s$. Under the conditioning that
vertex $s$ is blue-adjacent to all later vertices, let

$$
X_i=y_i(s),\qquad
\mu_i=\mathbb E[X_i],\qquad
\xi_i=X_i-\mu_i,
\qquad s<i\le r.
$$

The $X_i$ are independent lower-truncated Gaussians. Set

$$
S=\sum_{s<i<j\le r}X_iX_j,\qquad
\lambda=\frac{a\sqrt d}{1-p}>0.
$$

Expanding around the means gives

$$
S=
\sum_{s<i<j\le r}\mu_i\mu_j
+\sum_{i=s+1}^r A_i\xi_i
+\sum_{s<i<j\le r}\xi_i\xi_j,
\qquad
A_i=\sum_{\substack{s<j\le r\\j\ne i}}\mu_j>0.
$$

Choose Hölder exponents $P_D=1+O_{p,C}(D^{-1})$ and
$Q_D=O_{p,C}(D)$ with $P_D^{-1}+Q_D^{-1}=1$ and
$d\ge4Q_D|\lambda|k$. Such a choice exists because

$$
\frac{d}{|\lambda|k}
=
\frac{D^2\ell^2}
{[aD\ell/(1-p)]\,k}
\ge
\frac{1-p}{aC}D.
$$

Hölder's inequality yields

$$
\begin{aligned}
\mathbb E[e^{\lambda S}]
&\le
\exp\left(\lambda\sum_{i<j}\mu_i\mu_j\right)
\left[
\mathbb E\exp\left(P_D\lambda\sum_i A_i\xi_i\right)
\right]^{1/P_D}\\
&\quad\cdot
\left[
\mathbb E\exp\left(Q_D\lambda\sum_{i<j}\xi_i\xi_j\right)
\right]^{1/Q_D}.
\end{aligned}
$$

For the linear factor, the standardized tilt is

$$
u_i=\frac{P_D\lambda A_i}{\sqrt d}.
$$

Using $k\le C\ell$ and
$\mu_i=a/[(1-p)\sqrt d]+O_{p,C}(1/(D\sqrt d))$ gives

$$
0<u_i
\le
\frac{P_Da}{1-p}A_i
=O_{p,C}(D^{-1}).
$$

Thus Assumption 2 applies. The standardized lower-truncated variance is

$$
V_B(-c_p)+O_{p,C}(D^{-1})
=1-\gamma_B(p)+O_{p,C}(D^{-1}).
$$

Independence and the CGF bound therefore give

$$
\frac1{P_D}
\log\mathbb E\exp\left(P_D\lambda\sum_iA_i\xi_i\right)
\le
\left(1-\gamma_B(p)+O_{p,C}(D^{-1})\right)
\frac{\lambda^2}{2d}\sum_iA_i^2.
$$

Cauchy's inequality gives

$$
\sum_iA_i^2\le(k-1)^2\sum_i\mu_i^2.
$$

The centered quadratic lemma, applied with $Q_D\lambda$, gives

$$
\frac1{Q_D}
\log\mathbb E\exp\left(
Q_D\lambda\sum_{i<j}\xi_i\xi_j
\right)
\le\frac{4|\lambda|k}{d},
$$

because every $\xi_i$ is centered. Combining the deterministic, linear, and
quadratic factors proves

$$
\log\mathbb E[e^{\lambda S}]
\le
\lambda\mathbb E[S]
+\left(1-\gamma_B(p)+O_{p,C}(D^{-1})\right)
\frac{\lambda^2(k-1)^2}{2d}\sum_i\mu_i^2
+\frac{4|\lambda|k}{d}.
$$

Substitution of $\lambda$ and $\mu_i$ gives

$$
\lambda\mathbb E[S]
=
\frac{a^3}{(1-p)^3\sqrt d}\binom{k}{2}
+O_{p,C}\left(\frac{k^2}{D\sqrt d}\right)
$$

and

$$
\begin{aligned}
&\left(1-\gamma_B(p)+O_{p,C}(D^{-1})\right)
\frac{\lambda^2(k-1)^2}{2d}\sum_i\mu_i^2\\
&\qquad=
(1-\gamma_B(p))
\frac{a^4}{2(1-p)^4d}k(k-1)^2
+O_{p,C}\left(\frac{k^3}{Dd}\right).
\end{aligned}
$$

Hence

$$
\begin{aligned}
\mathbb E[e^{\lambda S}]
\le\exp\bigg(
&\frac{a^3}{(1-p)^3\sqrt d}\binom{k}{2}
+(1-\gamma_B(p))
\frac{a^4}{2(1-p)^4d}k(k-1)^2\\
&+O_{p,C}\left(
\frac{k^2}{D\sqrt d}
+\frac{k^3}{Dd}
+\frac{k}{\sqrt d}
\right)
\bigg).
\end{aligned}
$$

### Step 2: reverse induction

For the base case $s=r-1$, there is one remaining vertex. The claimed bound is
$1$ because $\Sigma_{r-1}=0$ and $\mathcal R^B_{r-1,r}=0$.

Assume the bound holds at $s$. Condition on the $s$-th column and on
$\bigwedge_{i=s+1}^rE_{s,i}$. Orthogonal projection gives

$$
\Sigma_s
=
\sum_{s<i<j\le r}
\langle\pi_{s-1}(\mathbf y_i),\pi_{s-1}(\mathbf y_j)\rangle
+S.
$$

The induction hypothesis isolates the random factor
$\mathbb E[e^{\lambda S}]$. Step 1 bounds this factor. Assumption 1 supplies
the probability that vertex $s$ is blue-adjacent to every later vertex.
Multiplying the two estimates uses the identities

$$
(1-p)^k(1-p)^{\binom{k}{2}}
=(1-p)^{\binom{k+1}{2}},
$$

$$
\binom{k}{3}+\binom{k}{2}=\binom{k+1}{3},
$$

and

$$
\begin{aligned}
&\sum_{s<i<j\le r}
\langle\pi_{s-1}(\mathbf y_i),\pi_{s-1}(\mathbf y_j)\rangle\\
&\quad+
\sum_{i=s+1}^r
\langle\pi_{s-1}(\mathbf y_s),\pi_{s-1}(\mathbf y_i)\rangle
=\Sigma_{s-1}.
\end{aligned}
$$

The new variance contribution is

$$
(1-\gamma_B(p))
\frac{a^4}{2(1-p)^4d}
(r-s)(r-s-1)^2,
$$

and all one-step remainders are $O_{p,C}(\mathcal E_{r-s})$. This is exactly
the new summand in $\mathcal R^B_{s-1,r}$. The induction closes.

### Step 3: extract the quartic coefficient inside the perfect event

At $s=0$, the projection sum $\Sigma_0$ vanishes. The accumulated variance
term contains

$$
\sum_{t=1}^{r-1}t(t-1)^2
=\frac{(r-1)r(r-2)(3r-5)}{12}
=\frac{r^4}{4}+O(r^3).
$$

Replacing $1-\gamma_B(p)$ by the unit proxy $1$ changes the log upper bound by

$$
\gamma_B(p)\frac{a^4}{2(1-p)^4d}
\left(\frac{r^4}{4}+O(r^3)\right)
=
\beta_B(p)\frac{r^4}{d}
+O_{p,C}\left(\frac{r^3}{d}\right).
$$

Therefore retaining the true lower-truncated variance improves the
unit-proxy log upper bound by the negative of this quantity. The
$O_{p,C}(D^{-1})$ variance approximation contributes
$O_{p,C}(D^{-1})r^4/d$. This proves the stated perfect-sequence comparison.

### Step 4: the greedy extraction preserves the quartic gain

Assume $r=\Theta_C(\ell)$. Greedily scan
$\mathbf x_1,\ldots,\mathbf x_r$, retaining a vector precisely when it
satisfies the norm and projection conditions relative to the previously kept
vectors. If the kept index set is $I$ and $u=r-|I|$, the retained subsequence
is perfect. Assumption 5 and sequential conditioning give

$$
\mathbb P[\text{blue clique and kept set }I]
\le
P^*_{\mathrm{blue},r-u}\,\eta^{\ell u}.
$$

Compare the starred bound at $r-u$ with the target bound at $r$. The loss in
the binomial base is at most

$$
-(\binom r2-\binom{r-u}{2})\log(1-p)
=O_{p,C}(\ell u).
$$

The positive cubic term is smaller at $r-u$, so it creates no loss. The
negative quartic improvement costs at most

$$
\beta_B(p)\frac{r^4-(r-u)^4}{d}
\le
\frac{4\beta_B(p)r^3u}{d}
=O_{p,C}\left(\frac{\ell u}{D^2}\right).
$$

The difference between all displayed error scales at $r-u$ and $r$ is also
$O_{p,C}(\ell u)$; in fact, every $D$-dependent contribution is smaller.
The concentration parameter in HMS is chosen so that
$\eta^{\ell u}$ dominates these losses with a residual factor
$e^{-c_{p,C}\ell u}$ for some $c_{p,C}>0$.

Summing over kept sets gives

$$
\sum_{u=0}^r\binom ru e^{-c_{p,C}\ell u}
=\left(1+e^{-c_{p,C}\ell}\right)^r
=1+o(1).
$$

Thus the unconditional blue probability is at most $1+o(1)$ times the
Ramsey-scale starred target bound. Its logarithm changes by $o(1)$, which is
negligible compared with $r^4/d=\Theta_C(\ell^2/D^2)$. The extraction
therefore preserves the quartic gain. $\square$

## Remaining gap to an unconditional Ramsey bound

1. Prove the pathwise paired companion lemma in
   **EXACT_COMPANION_AUDIT.md**. The literal HMS expansion has coefficient
   $1$, whereas the unit-Hölder companion used here has coefficient $1/2$.
   They cannot be identified inside a generic $O(r^4/d)$ term.
2. Take limits in the order: fixed $C$, choose sufficiently large $D$, then
   let $\ell\to\infty$.
3. Do not infer the $C\to\infty$ asymptotic without uniform bounds on the
   lower-truncated CGF remainder.
