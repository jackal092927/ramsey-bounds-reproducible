# History-dependent HMS mean-ledger proof package

Date: 2026-08-12  
Route: red Appendix-B ledger beyond the uniform-additive centered-moment cap

Primary source snapshots:

- Hunter--Milojević--Sudakov (HMS),
  [arXiv:2512.17718v2](https://arxiv.org/abs/2512.17718v2), source
  `arXiv_version.tex`, SHA-256
  `b72958ac35554eccb94dedab5800349d2c021af7d60f767125cb46998e0fd54a`.
- Lin--Niu, [arXiv:2605.25843v2](https://arxiv.org/abs/2605.25843v2),
  source `off-diagonal-Ramsey-R.tex`, SHA-256
  `dbf1bfa2c7603c81b2e56a97028b138ccf9a9299a3d1f20c0b08cf489136f429`.

This package starts from the already checked source bridge in
`HMS_APPENDIX_BRIDGE.md` and the exact-CGF optimization in
`LOWER_HMS_PARAMETER_OPTIMIZATION.md`.  It changes neither the Gaussian
graph nor the blue construction.

## Claim

Let all notation be as in `LOWER_HMS_PARAMETER_OPTIMIZATION.md`.  In
particular, for fixed sufficiently large $C$,

$$
p=p_C+\frac1C,\qquad
\Phi(-c)=p,\qquad
m_0=m(c)=\frac{\phi(c)}p,\qquad
D=\frac{4\phi(c)C}{1-p},
\tag{1}
$$

where $m(b)=\phi(b)/\Phi(-b)$, and
$d=\lceil D^2\ell^2\rceil$.  Put

$$
m'_0=m'(c),\qquad
\omega_0=\frac{\alpha_R^2}{D},\qquad
\rho_C=\frac{m_0m'_0}{D}.
\tag{2}
$$

For $w>\omega_0$, define

$$
M_w=m(c+w)
\tag{3}
$$

and

$$
\begin{aligned}
L_w(C):={}&\frac{4m_0M_w^2}{D}
+\frac{2M_w^2m_0^2m'_0}{(1-\rho_C)D^2}
+\frac{96m_0^2M_w^2}{(1-\rho_C)D^2},\\
B_w(C):={}&m_0^2-\frac{16}{3}-L_w(C),\\
H(C,w):={}&\frac{m_0^2m'_0B_w(C)}{12D^2}.
\end{aligned}
\tag{4}
$$

Let $H_*(C)=\lim_{w\downarrow\omega_0}H(C,w)$; the limit is obtained by
replacing $M_w$ by $m(c+\omega_0)$ in (4).  Then there is $C_0$ such that,
for every fixed $C\ge C_0$,

$$
\boxed{
\liminf_{\ell\to\infty}\frac1\ell
\log R\!\left(\ell,\lfloor C\ell\rfloor\right)
\ge
-\frac12\log p_C+\frac{B_R(C)}2+G_*(C)+H_*(C).}
\tag{T}
$$

Here $B_R(C)$ and $G_*(C)$ are exactly the frozen source-ledger and
history-uniform companion terms in `LOWER_HMS_PARAMETER_OPTIMIZATION.md`.
In particular, the public-constant consequence is

$$
\liminf_{\ell\to\infty}\frac1\ell
\log R\!\left(\ell,\lfloor C\ell\rfloor\right)
\ge
-\frac12\log p_C+\frac1{20}+G_*(C)+H_*(C).
\tag{A}
$$

Moreover,

$$
H_*(C)=\frac{1+o(1)}{96\log C}>0
\qquad(C\to\infty).
\tag{5}
$$

Thus this route formally adds one third of the leading
$G_*(C)\sim1/(32\log C)$ companion gain.  It lies outside the uniform
additive centered-moment class capped in the earlier package because it
changes the deterministic mean/connection potential itself.

## Status

**PROVABLE AS STATED relative to the two pinned source snapshots and the
already checked frozen bridge; pending independent referee replay.**

All four hard gates are closed below:

1. the full cutoff-box Hessian is uniformly negative definite;
2. the extra centered linear-CGF cost and weighted-quadratic cost have
   explicit constants, with $16/3$ for the latter;
3. the enlarged, non-exchangeable induction state merges exactly;
4. perfect-sequence extraction absorbs its deterministic loss.

Until an independent source-level replay is complete, (T), (A), and (5)
must be described as a **candidate proved in this local package**, not as a
canonical or externally verified Ramsey bound.  No effective numerical
$C_0$, publication priority, or global optimality is claimed.

## Assumptions

1. $C$ is fixed before $\ell\to\infty$, and is sufficiently large for all
   inequalities in (19), (28), and (43) below.
2. HMS red-perfectness, the cutoff relation in HMS line 1208, the
   pre-Cauchy exponential decomposition in HMS lines 895--935, and the
   Appendix-B reverse induction in HMS lines 1192--1289 are used unchanged.
3. Lin--Niu's exact upper-truncated CGF identity in lines 499--537 is used
   in the positive direction only.
4. The already verified history-uniform deficit
   $\mathsf d_{k,w,d}(P^*_{k,d})$ from equations (26)--(35) of
   `LOWER_HMS_PARAMETER_OPTIMIZATION.md` is retained unchanged.
5. The source's centered truncated Gaussians are $1/d$-subgaussian, as used
   in HMS lines 915--935.  Its square-MGF lemma is HMS lines 878--893.

## Notation

Fix a target red clique on the ordered vertices $[r]$, where $r\le\ell$.
At reverse-exposure step $s$, the future vertex set is

$$
V_s=\{s+1,\ldots,r\},\qquad k=|V_s|=r-s.
\tag{6}
$$

Put

$$
t_0=m_0\sqrt d,\qquad
\gamma_d=\frac{m_0m'_0}{\sqrt d}.
\tag{7}
$$

Every weight below is symmetric: $T_{ij}=T_{ji}$ and
$\Delta_{ij}=\Delta_{ji}$ when an unordered edge is written in either
orientation.

## Proof strategy

The invariant object is the weighted projection potential

$$
\mathcal P_s
=-\sum_{s<i<j\le r}T_{ij}
  \langle\pi_s(y_i),\pi_s(y_j)\rangle.
\tag{8}
$$

The weights are chosen backward so that the gradient of one joint
connection-plus-conditional-mean function is exactly the missing boundary
of (8).  Concavity turns that identity into a pathwise tangent bound.  The
new centered moment is then compared, on the same history, with the old
optimized uniform-weight centered moment.  This retains $G_*(C)$ and pays
only an explicit lower-order linear-CGF cost plus a $16/3$ weighted-square
cost.  Finally the deterministic new deficits are accumulated inside the
same reverse induction.

## Dependency map

1. Lemma 1 is finite backward algebra and proves adaptedness.
2. Lemma 2 uses variance monotonicity of an upper-truncated Gaussian and
   Gershgorin's theorem to prove the full-box tangent inequality.
3. Lemma 3 uses three-factor H\"older, the exact CGF, and HMS's square-MGF
   lemma to compare centered moments.
4. Lemma 4 gives deterministic weight and cost bounds and supplies the
   positive per-step deficit.
5. Proposition 5 inserts Lemmas 1--4 into the frozen reverse induction.
6. Proposition 6 repeats the frozen perfect-sequence extraction with one
   extra deterministic loss.

## Proof

### Step 1: the adapted weighted-degree recursion

Define the weights by decreasing first endpoint.  Once all weights whose
smaller endpoint is larger than $i$ are defined, set, for every $j>i$,

$$
\boxed{
T_{ij}=t_0+\gamma_d
\sum_{\substack{k>i\\k\ne j}}T_{jk}.}
\tag{9}
$$

The sum in (9) is the **weighted degree of $j$ in the already defined
future graph on $V_i$**.  It is not an ordinary neighbor count.  Set

$$
\Delta_{ij}=T_{ij}-t_0\ge0.
\tag{10}
$$

This recursion is adapted: when column $i$ is exposed, every weight on the
right of (9) belongs to an edge wholly inside $V_i$ and was fixed at an
earlier stage of the backward definition.  It is also deterministic once
$r,d,C$ are fixed; it does not depend on any Gaussian outcome.

For a cutoff vector $b=(b_j)_{j\in V_i}$ define the invariant joint function

$$
F_i(b)=
\sum_{j\in V_i}\log\Phi(-b_j)
-\frac1d\sum_{\{j,q\}\subset V_i}T_{jq}m(b_j)m(b_q).
\tag{11}
$$

The first term is the logarithm of the probability that vertex $i$ has all
required red edges.  The second is the deterministic conditional-mean part
of the weighted quadratic potential exposed in column $i$.

**Lemma 1 (exact gradient and adaptedness).**  For every $j\in V_i$,

$$
\partial_jF_i(c\mathbf1)
=-m_0-\frac{m_0m'_0}{d}
 \sum_{\substack{q>i\\q\ne j}}T_{jq}
=-\frac{T_{ij}}{\sqrt d}.
\tag{12}
$$

**Proof.**  Since
$(\log\Phi(-b))'=-m(b)$, differentiation of (11) at the central cutoff
gives the first equality.  Dividing (9) by $\sqrt d$ and using (7) gives
the second.  Every quantity in (12) is measurable before column $i$ is
sampled by the deterministic observation following (10). $\square$

The factor $d^{-1}$ in (11) and the word *weighted* in (9) are essential.
Replacing the weighted degree by a neighbor count would miss a factor
$m_0\sqrt d$ and make (12) false.

### Step 2: uniform negative definiteness on the full cutoff box

For $b>0$, write

$$
m'(b)=m(b)(m(b)-b)=1-v(b),
\tag{13}
$$

where $v(b)$ is the variance of $Z$ conditioned on $Z\le-b$.  Lin--Niu's
variance-monotonicity lemma says that the conditional variance increases
with the upper cutoff.  Hence $v(b)=V(-b)$ is nonincreasing in $b$, and

$$
m'(b)>0,\qquad m''(b)=-v'(b)\ge0.
\tag{14}
$$

Fix $w>\omega_0$ and put

$$
j_-(w)=m'(c-w),\qquad j_+(w)=m'(c+w).
\tag{15}
$$

By (14), these are respectively the minimum and maximum of $m'$ on
$I_w=[c-w,c+w]$.

Let $T_{\max}$ be the largest weight for the current $r$.  From (9),

$$
T_{\max}\le t_0+\gamma_d rT_{\max}.
\tag{16}
$$

Since $r\le\ell$ and $\sqrt d\ge D\ell$,

$$
\gamma_dr\le\rho_C.
\tag{17}
$$

Thus, whenever $\rho_C<1$,

$$
T_{\max}\le\frac{t_0}{1-\rho_C},\qquad
\max_j\frac1d\sum_{q\ne j}T_{jq}
\le\frac{m_0}{D(1-\rho_C)}.
\tag{18}
$$

We impose the explicit full-box condition

$$
\boxed{
j_-(w)>
j_+(w)^2\frac{m_0}{D(1-\rho_C)}.}
\tag{19}
$$

**Lemma 2 (full-box strict concavity).**  Under (19), every $F_i$ is
strictly concave on $I_w^{V_i}$, uniformly in $i,r,d$ and the red-perfect
history.

**Proof.**  Direct differentiation of (11) gives

$$
\begin{aligned}
(\nabla^2F_i)_{jj}
&=-m'(b_j)-\frac{m''(b_j)}d
  \sum_{q\ne j}T_{jq}m(b_q),\\
(\nabla^2F_i)_{jq}
&=-\frac{T_{jq}}d m'(b_j)m'(b_q)
\quad(j\ne q).
\end{aligned}
\tag{20}
$$

By (14), the second term on the diagonal is nonpositive.  Therefore every
diagonal entry of $-\nabla^2F_i$ is at least $j_-(w)$, while (15) and (18)
bound the absolute row sum of its off-diagonal entries by

$$
j_+(w)^2\frac{m_0}{D(1-\rho_C)}.
\tag{21}
$$

Condition (19) makes the symmetric matrix $-\nabla^2F_i$ strictly
diagonally dominant with positive diagonal.  Gershgorin's theorem therefore
places all its eigenvalues in $(0,\infty)$. $\square$

For a red-perfect history, HMS line 1208 and the projection bound give, for
every fixed $w>\omega_0$ and all sufficiently large $\ell$,

$$
b_j\in I_w,\qquad
|b_j-c-\sqrt d,h_{ij}|\le d^{-1/5},
\tag{22}
$$

where
$h_{ij}=\langle\pi_{i-1}(y_i),\pi_{i-1}(y_j)\rangle$.
Lemmas 1--2 and (22) yield the pathwise tangent inequality

$$
F_i(b)le F_i(c\mathbf1)
-\sum_{j>i}T_{ij}h_{ij}
+\frac{d^{-1/5}}{\sqrt d}\sum_{j>i}T_{ij}.
\tag{23}
$$

This is the exact potential-merging inequality needed later.

The conditions are nonempty for all sufficiently large $C$.  The source
asymptotics give

$$
m_0\sim\sqrt{2\log(1/p)},\quad
D\sim4\sqrt2\log(1/p)^{3/2},\quad
\omega_0=O(\log(1/p)^{-1/2}),
\tag{24}
$$

while (13)--(14) give $j_-(w),j_+(w)\to1$ as
$C\to\infty$ and then $w\downarrow\omega_0$.  The right side of (19) is
$O(1/\log C)$.

### Step 3: exact centered decomposition

At exposure step $i$, condition on the red edges from $i$ to $V_i$ and on
the prior history.  The variables

$$
X_j=y_j(i),\qquad
\mu_j=\mathbb EX_j=-\frac{m_j}{\sqrt d},\qquad
m_j=m(b_j),\qquad
\xi_j=X_j-\mu_j
\tag{25}
$$

are independent.  Put

$$
Q_T=\sum_{\{j,q\}\subset V_i}T_{jq}X_jX_q.
\tag{26}
$$

Writing $T=t_0+\Delta$ gives the exact exponent decomposition

$$
-Q_T
=-\frac1d\sum_{j<q}T_{jq}m_jm_q
+\sum_j(u_j^0+\delta u_j)(\sqrt d\,\xi_j)
-t_0\sum_{j<q}\xi_j\xi_q
-\sum_{j<q}\Delta_{jq}\xi_j\xi_q,
\tag{27}
$$

where

$$
u_j^0=\frac{t_0}{d}\sum_{q\ne j}m_q,qquad
\delta u_j=\frac1d\sum_{q\ne j}\Delta_{jq}m_q.
\tag{28}
$$

Let

$$
S_i=\sum_{\{j,q\}\subset V_i}\Delta_{jq},\qquad
R_j=\sum_{q\ne j}\Delta_{jq},\qquad
R_i=\max_{j\in V_i}R_j.
\tag{29}
$$

When $R_i>0$, choose three conjugate H\"older exponents by

$$
Q_0=\frac{d}{4t_0k},\qquad
Q_1=\frac{d}{4R_i},\qquad
\frac1P=1-\frac1{Q_0}-\frac1{Q_1}.
\tag{30}
$$

If $R_i=0$, set $Q_1=\infty$.  The old optimized two-factor split is

$$
P_0=\left(1-\frac{4t_0k}{d}\right)^{-1}.
\tag{31}
$$

For each cutoff, let

$$
K_b(u)=\log\mathbb E\exp(u\sqrt d\,\xi)
\tag{32}
$$

be the exact centered upper-truncated CGF.  Its source identity gives

$$
K_b(0)=K_b'(0)=0,qquad
0\le K_b''(u)=v(b+u)\le1
\quad(u\ge0).
\tag{33}
$$

Define

$$
\mathcal L(P,u)=\frac1P\sum_jK_{b_j}(Pu_j).
\tag{34}
$$

The old optimized centered-linear term is
$\mathcal L(P_0,u^0)$; the new one is
$\mathcal L(P,u^0+\delta u)$.

### Step 4: explicit centered costs

Assume

$$
\frac{4m_0}{D}
+\frac{4m_0^2m'_0}{(1-\rho_C)D^2}<\frac12.
\tag{35}
$$

Lemma 4 below proves that (35) implies
$Q_0,Q_1>1$, $1<P\le2$, and the square-MGF conditions used here.

**Lemma 3 (centered comparison with explicit costs).**  For every cutoff
vector in $I_w^{V_i}$,

$$
\begin{aligned}
\log\mathbb E\exp\Big(&\sum_j(u_j^0+\delta u_j)\sqrt d\,\xi_j
-t_0\sum_{j<q}\xi_j\xi_q
-\sum_{j<q}\Delta_{jq}\xi_j\xi_q\Big)\\
&\le
\mathcal L(P_0,u^0)+\frac{4t_0k}{d}
+C_i^{\rm lin}+\frac{16}{3}\frac{S_i}{d},
\end{aligned}
\tag{36}
$$

where

$$
C_i^{\rm lin}
\le L_w(C)\frac{S_i}{d}.
\tag{37}
$$

**Proof.**  Apply three-factor H\"older to the last three random terms in
(27), with exponents (30).

For the uniform quadratic factor, HMS lines 915--935 applied with
$Q_0t_0$ and then raised to $1/Q_0$ give $4t_0k/d$; equality is permitted
in $d\ge4Q_0t_0k$.

For the extra weighted factor, positivity of $\Delta$ gives

$$
-\sum_{j<q}\Delta_{jq}\xi_j\xi_q
\le\frac12\sum_jR_j\xi_j^2.
\tag{38}
$$

With $Q_1=d/(4R_i)$, each square-MGF argument
$x_j=Q_1R_j/(2d)$ is at most $1/8$.  HMS's square-MGF lemma and
$\log(1+x)\le x$ give

$$
\begin{aligned}
\frac1{Q_1}\log\mathbb E
 \exp\left(-Q_1\sum_{j<q}\Delta_{jq}\xi_j\xi_q\right)
&\le\frac1{Q_1}\sum_j\frac{16}{3}\frac{Q_1R_j}{2d}\\
&=\frac{16}{3}\frac{S_i}{d}.
\end{aligned}
\tag{39}
$$

It remains to compare the linear factors.  From (33), for $u,\delta\ge0$
and $1\le P\le2$,

$$
\frac{K_b(P(u+\delta))-K_b(Pu)}P
\le2u\delta+\delta^2.
\tag{40}
$$

Also, differentiating $K_b(Pu)/P$ and using (33) gives

$$
0\le\frac{\partial}{\partial P}\frac{K_b(Pu)}P\le u^2.
\tag{41}
$$

Put $a=4t_0k/d$ and $z=4R_i/d$.  By (35) and Lemma 4,
$a+z\le1/2$, and hence

$$
0\le P-P_0
=\frac{z}{(1-a-z)(1-a)}
\le\frac{16R_i}{d}.
\tag{42}
$$

Summing (40)--(41) yields

$$
C_i^{\rm lin}
\le2\sum_ju_j^0\delta u_j
+\sum_j(\delta u_j)^2
+\frac{16R_i}{d}\sum_j(u_j^0)^2.
\tag{43}
$$

The deterministic estimates in Lemma 4 turn the three terms in (43), in
order, into

$$
\left[
\frac{4m_0M_w^2}{D},\quad
\frac{2M_w^2m_0^2m'_0}{(1-\rho_C)D^2},\quad
\frac{96m_0^2M_w^2}{(1-\rho_C)D^2}
\right]\frac{S_i}{d}.
\tag{44}
$$

Their sum is (37). $\square$

### Step 5: deterministic weight arithmetic

**Lemma 4 (weight bounds and accumulated mass).**  For every exposure step
with $k=|V_i|$,

$$
\begin{aligned}
&t_0\le T_{jq}\le\frac{t_0}{1-\rho_C},\\
&\gamma_dt_0(r-j-1)
 \le\Delta_{jq}
 \le\frac{\gamma_dt_0(r-j-1)}{1-\rho_C}
 \quad(j<q),\\
&S_i\ge\gamma_dt_0\frac{k(k-1)(k-2)}3,\\
&R_i\le\frac{\gamma_dt_0(k-1)^2}{1-\rho_C},\\
&\frac{R_i}{S_i}\le\frac{6}{(1-\rho_C)k}
 \quad(k\ge3),\\
&\sum_{i=1}^{r-1}S_i
 \ge2\gamma_dt_0\binom r4
=2m_0^2m'_0\binom r4.
\end{aligned}
\tag{45}
$$

**Proof.**  The first line is (16)--(18).  In (9), the future weighted
degree contains exactly $r-j-1$ edges when the smaller endpoint is $j$;
bounding each by $t_0$ and $t_0/(1-\rho_C)$ gives the second line.

For $j\in V_i$, write $h=r-j$.  There are $h$ choices of $q>j$.  Therefore

$$
S_i\ge\gamma_dt_0\sum_{h=1}^{k-1}h(h-1)
=\gamma_dt_0\frac{k(k-1)(k-2)}3.
\tag{46}
$$

Every vertex has at most $k-1$ incident future edges and each increment is
at most $\gamma_dt_0(k-1)/(1-\rho_C)$, proving the fourth line.  Dividing
that bound by (46) and using
$3(k-1)/(k(k-2))\le6/k$ for $k\ge3$ proves the fifth.  Finally sum (46) over
$k=1,\ldots,r-1$ and use

$$
\sum_{k=1}^{r-1}k(k-1)(k-2)=6\binom r4.
\tag{47}
$$

This proves (45). $\square$

We now justify (44).  From (28)--(29), with $m_j\le M_w$,

$$
u_j^0\le\frac{m_0M_wk}{\sqrt d},\qquad
\sum_j\delta u_j\le\frac{2M_wS_i}{d},\qquad
\max_j\delta u_j\le\frac{M_wR_i}{d}.
\tag{48}
$$

The first two terms in (43) are consequently bounded by the first two
terms in (44), using $k/\sqrt d\le1/D$ and the fourth line of (45).  For
the last term, use the fifth line of (45):

$$
\frac{16R_i}{d}\sum_j(u_j^0)^2
\le
\frac{96m_0^2M_w^2}{(1-\rho_C)D^2}\frac{S_i}{d}.
\tag{49}
$$

The fourth line of (45) also gives

$$
\frac1{Q_0}+\frac1{Q_1}
\le\frac{4m_0}{D}
+\frac{4m_0^2m'_0}{(1-\rho_C)D^2},
\tag{50}
$$

so (35) proves every feasibility assertion used in Lemma 3.

### Step 6: the positive pathwise group deficit

Let $\mathsf d_{k,w,d}(P^*_{k,d})$ be the old optimized history-uniform
deficit in equation (27) of `LOWER_HMS_PARAMETER_OPTIMIZATION.md`.  Its
proof compares the old optimized linear term
$\mathcal L(P_0,u^0)$ with the exact pre-Cauchy HMS centered allocation on
the same history.

Combining (23), (27), and Lemma 3 with that old comparison yields the same
frozen HMS one-step envelope, now with

$$
-\mathsf d_{k,w,d}(P^*_{k,d})
-B_w(C)\frac{S_i}{d}
+\frac{d^{-1/5}}{\sqrt d}\sum_{j>i}T_{ij}
\tag{51}
$$

appended to its exponent.  To see the coefficient in (51) without any
ledger shorthand, at the central cutoff

$$
F_i(c\mathbf1)
=k\log p
-\frac{m_0^2}{d}left[t_0\binom k2+S_i\right].
\tag{52}
$$

The $t_0$ part is the unchanged HMS central mean.  The increment contributes
$-m_0^2S_i/d$; (36)--(37) pay
$(16/3+L_w(C))S_i/d$.  Their difference is precisely
$-B_w(C)S_i/d$.  All old centered, source-error, and exact-CGF terms occur
once, in the same history.  This is why the new gain can be added to
$G_*(C)$ rather than replacing it.

The source's one-sided $K$ in $B_R(C)$ is unchanged.  HMS lines 1260--1274
already pay the old central centered allocation.  Equation (52) replaces
the source's history-perturbed deterministic mean by its exact central
value, while (51) separately pays every new centered term; no larger
source $O$ term is invoked.

### Step 7: reverse-induction state

For fixed $r$, replace the projection term in the frozen HMS induction by
$\mathcal P_s$ from (8).  Also multiply its right side by the old accumulated
exact-CGF deficit and by

$$
\exp\left[
-\sum_{a=s+1}^{r-1}B_w(C)\frac{S_a}{d}
+\sum_{a=s+1}^{r-1}
 \frac{d^{-1/5}}{\sqrt d}\sum_{j>a}T_{aj}
\right].
\tag{53}
$$

The precise lower limit in an empty sum is immaterial; (53) contains
exactly the steps already exposed in the reverse induction.

At the base case the future graph has at most one vertex, so all pair sums
vanish.  Assume the state at $s=i$ and expose column $i$.  The projection
identity

$$
\langle\pi_i(y_j),\pi_i(y_q)\rangle
=\langle\pi_{i-1}(y_j),\pi_{i-1}(y_q)\rangle
+y_j(i)y_q(i)
\tag{54}
$$

turns the new-coordinate part of $\mathcal P_i$ into $-Q_T$.  Equation
(51) bounds its conditional moment together with the connection factor.
The tangent term $-\sum_{j>i}T_{ij}h_{ij}$ supplies exactly the missing
edges from $i$ to $V_i$, while the first term on the right of (54) retains
all future edges.  Their union is $\mathcal P_{i-1}$.  The old deficit and
the new deterministic charge append their next summands in (53).

Every weight in this argument was fixed before sampling column $i$.
Therefore there is no anticipative coefficient and no untracked
history-dependent cross-moment.  This proves the enlarged reverse induction.

At $s=0$ the projection potential is empty.  Lemma 4 gives the perfect-event
bound

$$
P^*_{R,r}
\le\mathcal H_C(r)
\exp\left[
-\mathcal D_{C,w,d}(r)
-\frac{2m_0^2m'_0B_w(C)}d\binom r4
+J_{r,d}
\right],
\tag{55}
$$

where $\mathcal H_C$ and $\mathcal D_{C,w,d}$ are the frozen source envelope
and old optimized deficit, and (18) gives the explicit diagonal-error bound

$$
0\le J_{r,d}
\le\frac{m_0}{1-\rho_C}d^{-1/5}\binom r2
=o_C(r^2)
\quad(r=\Theta(\ell)).
\tag{56}
$$

This closes the reverse-induction gate.

### Step 8: perfect-sequence extraction

Apply (55) to every retained ordered subset produced by the HMS greedy
perfect-sequence extraction.  The same proof is valid for a retained set of
size $q\le\ell$ in the original dimension $d$: then $q/\sqrt d\le1/D$, so
all feasibility and concavity bounds only improve.

If $u$ vertices are deleted, then

$$
\binom\ell4-\binom{\ell-u}4
\le u\binom\ell3\le\frac{\ell^3u}{6}.
\tag{57}
$$

Consequently the cost of restoring the new deficit at size $\ell$ is at
most

$$
\frac{m_0^2m'_0B_w(C)}{3D^2}\,\ell u.
\tag{58}
$$

For sufficiently large $C$, the coefficient in (58) is
$(1+o(1))/(24\log C)<1$.  Also $J_{q,d}\le J_{\ell,d}$, so the positive
error in (56) needs no restoration charge.  The old optimized deficit loss
is already at most $\ell u$ by equation (37) of the frozen package.  Thus
the new total restoration cost adds less than one further $\ell u$ to the
literal extraction accounting in equations (23a)--(23g) of
`HMS_APPENDIX_BRIDGE.md`.

The projection-failure factor remains

$$
\left(\frac p{10}\right)^{10\ell u},
\tag{59}
$$

whose logarithmic charge
$10\log(10/p)\ell u$ dominates the missing edge, cubic, old deficit, new
deficit, and diagonal terms.  The same binomial subset sum is $o(1)$.
Hence (55) holds for the unconditional red probability with a multiplicative
$1+o(1)$ factor.  This closes the extraction gate.

### Step 9: rate conversion and positivity

For fixed $w>\omega_0$, equations (55)--(56) and
$d/\ell^2\to D^2$ give the new rate term

$$
\lim_{\ell\to\infty}
\frac{2m_0^2m'_0B_w(C)}{d\ell^2}\binom\ell4
=\frac{m_0^2m'_0B_w(C)}{12D^2}
=H(C,w).
\tag{60}
$$

All blue quantities and the red/blue crossing are unchanged.  The frozen
red constraint is still below the blue one for sufficiently large $C$,
because $G_*(C)+H(C,w)=o(1)$ while the source bonuses tend respectively to
$1/12$ and $1/2$.  Thus the frozen first-moment extraction gives (T) with
$H(C,w)$ for every $w>\omega_0$.  Continuity of $m$ lets
$w\downarrow\omega_0$, proving (T).  The same public coarsening gives (A).

It remains to verify that all sign conditions hold.  From (24), (13), and
the cutoff-window limit,

$$
\rho_C=o(1),\qquad
\frac{M_w}{m_0}\to1,qquad
m'_0\to1.
\tag{61}
$$

Equations (19) and (35) therefore hold for sufficiently large $C$, and

$$
\frac{L_w(C)}{m_0^2}	o0,qquad
\frac{B_w(C)}{m_0^2}	o1.
\tag{62}
$$

In particular $B_w(C)>0$.  Finally, with
$m_0^2=(2+o(1))\log C$ and
$D^2=(32+o(1))(\log C)^3$, equations (4) and (62) give

$$
H_*(C)
=\frac{(1+o(1))m_0^4}{12D^2}
=\frac{1+o(1)}{96\log C}.
\tag{63}
$$

This proves (5), and completes the proof of (T)--(A). $\square$

## Corrections to the original sketch

1. The recursion must use a weighted future degree.  An unweighted degree
   gives the wrong normalization and does not match the gradient.
2. The relevant invariant is the joint function (11), not the connection
   probability or cutoff mean in isolation.
3. The weighted quadratic remainder cannot be passed through the rank-one
   HMS cancellation.  It must be split from the uniform complete-graph
   part; the pairwise square bound then costs $16S_i/(3d)$.
4. Adding a third H\"older factor increases the linear exponent from $P_0$
   to $P$.  Equations (40)--(49) explicitly pay this cost; omitting it would
   leave a same-order bookkeeping gap.
5. The new state is deterministic but not exchangeable.  Reverse induction
   needs the full triangular array $T_{ij}$, not a scalar group-size charge.

## Scope and non-claims

- The result is asymptotic in the order
  $C$ fixed, then $\ell\to\infty$, then $C\to\infty$ only for (5).
- No numerical value of $C_0$ is asserted.  The frozen HMS source constant
  in $B_R(C)$ remains existential.
- The coefficient $1/96$ is a proved lower contribution of this particular
  recursive ledger, not an optimum over history-dependent potentials.
- No improvement to the blue ledger, no diagonal Ramsey upper bound, and no
  finite Ramsey-number claim is made here.
- The package has not yet received independent referee replay and therefore
  is not yet the canonical project theorem.

## Reproducibility

`history_dependent_ledger_check.py` independently replays the finite weight
recursion, the gradient identity, structural sums, Hessian diagonal-dominance
margin, H\"older feasibility, and the constants in (4) at high precision.
It is an arithmetic/symbolic sanity check, not a proof of the probabilistic
induction or extraction.

Run:

```bash
.venv/bin/python routes/lower/history_dependent_ledger_check.py
```

## Open risks

1. An independent referee should replay the source-to-ledger comparison in
   (51), especially that the old exact-CGF deficit is used once and that the
   frozen source $K$ is unchanged.
2. The source preprints and this local extension have not received external
   peer review.
3. The diagnostic checker samples finite cutoff vectors; the analytic
   full-box certification is Lemma 2, not the grid.
