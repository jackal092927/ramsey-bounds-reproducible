# Optimizing the HMS red same-history companion

Date: 2026-08-12  
Target: optimize the new term in
[HMS_APPENDIX_BRIDGE.md](./HMS_APPENDIX_BRIDGE.md) without changing its
frozen HMS red ledger

Primary source snapshots:

- Hunter--Milojević--Sudakov (HMS),
  [arXiv:2512.17718v2](https://arxiv.org/abs/2512.17718v2), source
  `arXiv_version.tex`, SHA-256
  `b72958ac35554eccb94dedab5800349d2c021af7d60f767125cb46998e0fd54a`.
- Lin--Niu, [arXiv:2605.25843v2](https://arxiv.org/abs/2605.25843v2),
  source `off-diagonal-Ramsey-R.tex`, SHA-256
  `dbf1bfa2c7603c81b2e56a97028b138ccf9a9299a3d1f20c0b08cf489136f429`.

Line references below are to those exact source files.

## Claim

There are two conclusions, and their scopes are deliberately different.

### A. A strict fixed-$C$ improvement

There is $C_0$ such that, for every fixed real $C\ge C_0$, the exact
same-history red companion term in `HMS_APPENDIX_BRIDGE.md` can be replaced
by an explicitly larger term $G_*(C)>0$.  With the definitions below,

$$
\liminf_{\ell\to\infty}\frac1\ell
\log R\!\left(\ell,\lfloor C\ell\rfloor\right)
\ge
-\frac12\log p_C+\frac{B_R(C)}2+G_*(C).
\tag{T*}
$$

The public-constant consequence is

$$
\liminf_{\ell\to\infty}\frac1\ell
\log R\!\left(\ell,\lfloor C\ell\rfloor\right)
\ge
-\frac12\log p_C+\frac1{20}+G_*(C).
\tag{A*}
$$

If $c_R(C)/(4D^2)$ denotes the previous companion term, with the literal
definitions in `HMS_APPENDIX_BRIDGE.md`, then

$$
G_*(C)>\frac{c_R(C)}{4D^2}
\tag{S}
$$

for every sufficiently large $C$.

### B. A method-internal sharp leading coefficient

Consider a **uniform additive centered-moment companion** with the following
quantifiers.  For each fixed $C$ and every group size $k$, it chooses a
deterministic number $\delta_{C,k,d}$ which is valid as a same-step saving
relative to (20) for every red-perfect history at that $k$; the reverse
induction then accumulates $\sum_{k<\ell}\delta_{C,k,d}$ without averaging or
coupling the residual history dependence.  If such a companion keeps the
same HMS tilt and deterministic mean/connection ledger and changes only the
centered exponential-moment estimate, then

$$
\limsup_{\ell\to\infty}\frac1{\ell^2}
\sum_{k=1}^{\ell-1}\delta_{C,k,d}
\le\frac{m_0^4}{4D^2}
=\frac{1+o(1)}{32\log C}\quad(C\to\infty).
\tag{M}
$$

The first limit in (M) fixes $C$ before sending $\ell\to\infty$; only the
final displayed equivalence then sends $C\to\infty$.  The new $G_*(C)$
saturates this cap asymptotically:

$$
G_*(C)=\frac{1+o(1)}{32\log C}.
\tag{O}
$$

Consequently $1/32$ cannot be raised to $1/16$ by rechoosing the
Hölder exponents, using the exact one-sided CGF, or shrinking the cutoff
window within this uniform additive class.  A history-dependent saving
which is later averaged or coupled through a richer induction state is not
bounded here.  This is not a universal obstruction to improving the Ramsey
lower bound.

## Status

**PROVABLE AS STATED, source-relative and pending independent referee
replay.**

- The strict finite-$C$ improvement (T*)--(S) is proved below.
- The method-internal upper bound (M) is proved below and matches (O).
- No blue-side improvement is used.  The unchanged HMS blue rate remains
  strictly above the red rate for sufficiently large $C$.
- No effective numerical value of $C_0$ is claimed.  HMS leaves absolute
  constants in its appendix $O/o$ terms unspecified.
- This document does not claim global optimality, publication priority, or
  external peer review.

## Assumptions

1. $C$ is sufficiently large and fixed before $\ell\to\infty$.
2. $p_C\in(0,1/2)$ is the solution of

   $$
   \log p_C=C\log(1-p_C),
   $$

   and

   $$
   p=p_C+\frac1C,\qquad
   \Phi(-c_p)=p,\qquad
   a=\phi(c_p),\qquad
   D=\frac{4aC}{1-p},\qquad
   d=\lceil D^2\ell^2\rceil.
   \tag{1}
   $$

3. We use HMS red-perfectness exactly as defined in source lines 963--971,
   with

   $$
   \alpha_R=10\sqrt{\log(10/p)}.
   \tag{2}
   $$

4. We use the exact pre-Cauchy exponential-moment decomposition in HMS
   lines 895--935, the upper-truncated CGF identity proved in Lin--Niu
   lines 499--537, and the red Appendix-B induction in HMS lines 1192--1289.
5. $B_R(C)$ is the same frozen source-ledger quantity as in
   `HMS_APPENDIX_BRIDGE.md`: for one existential absolute source constant
   $K$,

   $$
   \theta_C=1-K\frac{\sqrt{\log p^{-1}}}{D},\qquad
   B_R(C)=-\log\frac p{p_C}
   +\theta_C\frac{a^3}{3p^3D}.
   \tag{3}
   $$

6. The unchanged HMS blue appendix bound is accepted with the same
   parameters.  No blue CGF deficit, blue Hölder interval, or blue
   same-history refinement is invoked anywhere below.

## Notation

For conditioning on $Z\le-b$, put

$$
m(b):=\frac{\phi(b)}{\Phi(-b)},\qquad
v(b):=1+b\,m(b)-m(b)^2.
\tag{4}
$$

Thus the conditional mean and variance are $-m(b)$ and $v(b)$.  Write

$$
m_0:=m(c_p)=\frac ap,\qquad
\omega_0:=\frac{\alpha_R^2}{D}.
\tag{5}
$$

For the centered variable

$$
Y_b:=Z+m(b)\quad\text{conditioned on }Z\le-b,
$$

define its exact positive-direction CGF

$$
K_b(u):=\log\mathbb E e^{uY_b}
=\frac{u^2}{2}+u\,m(b)
+\log\Phi(-b-u)-\log\Phi(-b),\qquad u\ge0,
\tag{6}
$$

and its normalized version

$$
\psi_b(u):=
\begin{cases}
K_b(u)/u^2,&u>0,\\[2mm]
v(b)/2,&u=0.
\end{cases}
\tag{7}
$$

At the optimized limiting window set

$$
b_*:=c_p-\omega_0,\qquad m_*:=m(b_*),\qquad v_*:=v(b_*).
\tag{8}
$$

For $0\le x\le1$, define

$$
P_*(x):=\frac{D}{D-4m_0x},\qquad
u_*(x):=\frac{P_*(x)m_0m_*x}{D}.
\tag{9}
$$

For sufficiently large $C$, $D>8m_0$ and
$P_*(1)v_*<2$.  Finally define

$$
\boxed{
G_*(C):=
\frac{m_0^2m_*^2}{D^2}
\int_0^1x^3
\left[1-P_*(x)\psi_{b_*}(u_*(x))\right],dx.}
\tag{10}
$$

The integrand at $x=0$ is interpreted by continuity.  The factor $x^3$
makes its chosen endpoint value immaterial.

## Proof Strategy

1. Write the exact centered CGF as an integral of the truncated variance;
   this proves all monotonicity needed for a uniform history bound.
2. Keep an arbitrary cutoff window and arbitrary step-dependent Hölder
   exponent, and derive their exact admissible region and gain.
3. Optimize the exponent separately at every group size and take the
   smallest limiting cutoff window allowed by red-perfectness.
4. Insert the resulting deterministic group deficit into the already
   verified HMS reverse induction and extraction.
5. Compare the new gain strictly with the frozen old term.
6. Use Jensen's inequality on the full centered quadratic expression to
   bound every same-mean companion, proving the sharp $1/32$ obstruction.

## Dependency Map

1. Lemma 1 below depends only on the exact truncated-normal CGF identity and
   monotonicity of truncated variance.
2. The admissible Hölder region depends on HMS's centered-quadratic estimate
   and its literal feasibility inequality $d\ge4Q|\lambda|k$.
3. The pathwise deficit depends on retaining the same $b_i,\mu_i,A_i$ in
   the HMS and refined envelopes before any source $O$ term is coarsened.
4. The rate gain depends on the same reverse induction and deletion charge
   already checked in `HMS_APPENDIX_BRIDGE.md` and its two referee reports.
5. The method cap depends on the central admissible history and Jensen; it
   does not use the blue construction.
6. The final Ramsey statement uses the unchanged HMS blue probability and
   the same first-moment extraction as the frozen theorem.

## Proof

### Step 1: exact CGF representation and monotonicity

The source calculation behind (6) gives

$$
K_b(0)=K_b'(0)=0,\qquad K_b''(u)=v(b+u).
\tag{11}
$$

Integrating twice and rescaling the integration variable yields

$$
K_b(u)=\int_0^u(u-s)v(b+s)\,ds,
\qquad
\psi_b(u)=\int_0^1(1-t)v(b+ut)\,dt.
\tag{12}
$$

The Mills ratio $m(b)$ is strictly increasing in $b$, while $v(b)$ is
strictly decreasing.  The latter is the cutoff orientation of Lin--Niu's
variance-monotonicity lemma: their variance is increasing in the upper
cutoff $-b$, hence decreasing in $b$.

It follows directly from (12) that

$$
0<\psi_b(u)\le\frac{v(b)}2,
\tag{13}
$$

and $\psi_b(u)$ is nonincreasing in each of $b$ and $u$, strictly decreasing
in either variable away from a degenerate endpoint.  Formula (12) also
proves continuity at $u=0$.  Finally $K_b(u)\ge0$ by Jensen because $Y_b$
is centered.

These facts use the exact CGF.  No Taylor remainder and no blue-oriented
CGF inequality is needed.

### Step 2: the actual limiting cutoff window

Fix a red-perfect exposure history.  HMS line 1208 and its diagonal bound
give

$$
|b_i-c_p|
\le
\sqrt d\,
|\langle\pi_{s-1}(y_i),\pi_{s-1}(y_s)\rangle|
+d^{-1/5}.
\tag{14}
$$

Red-perfectness and Cauchy--Schwarz give

$$
\sqrt d\,
|\langle\pi_{s-1}(y_i),\pi_{s-1}(y_s)\rangle|
\le\frac{\alpha_R^2\ell}{\sqrt d}
\le\frac{\alpha_R^2}{D}=\omega_0.
\tag{15}
$$

The frozen proof replaced the right side of (14) by $2\omega_0$ after
requiring $d^{-1/5}\le\omega_0$.  For the limiting theorem one can retain
more information.  For every fixed $w>\omega_0$, after choosing
$\ell\ge\ell_0(C,w)$, equations (14)--(15) imply

$$
b_i\in I_w:=[c_p-w,c_p+w].
\tag{16}
$$

We first prove a theorem for every $w>\omega_0$ and then take
$w\downarrow\omega_0$.  We never assert that the boundary window
$w=\omega_0$ contains every finite-$\ell$ cutoff.

This does not alter HMS red-perfectness or condition on a smaller event.
For each fixed $w>\omega_0$, (16) is a deterministic consequence of the
original red-perfect event once $\ell\ge\ell_0(C,w)$.  Therefore the same
law-of-total-probability induction and the same perfect-sequence extraction
continue to cover every history covered by HMS; no history is discarded by
the window refinement.

Put

$$
b_w=c_p-w,\qquad m_w=m(b_w),\qquad v_w=v(b_w).
\tag{17}
$$

By monotonicity, throughout (16),

$$
m(b_i)\ge m_w,\qquad v(b_i)\le v_w.
\tag{18}
$$

### Step 3: the general admissible Hölder/CGF region

At a reverse-exposure step let $k=r-s$, let

$$
X_i=y_i(s),\qquad
\mu_i=-\frac{m(b_i)}{\sqrt d},\qquad
A_i=\sum_{j\ne i}\mu_j,\qquad
\lambda=-m_0\sqrt d.
\tag{19}
$$

Stopping HMS lines 895--935 before the final Cauchy coarsening gives the
same exact envelope used in the frozen bridge:

$$
H_s=\lambda\mathbb ES
+\frac{\lambda^2}{d}\sum_iA_i^2
+\frac{4|\lambda|k}{d}.
\tag{20}
$$

Choose conjugate Hölder exponents $P_k,Q_k>1$.  The centered-quadratic
factor is legal whenever

$$
1<Q_k\le\frac{\sqrt d}{4m_0k},
\qquad
P_k=\frac{Q_k}{Q_k-1}.
\tag{21}
$$

Indeed (21) is exactly $d\ge4Q_k|\lambda|k$.  The positive-direction
linear CGF is exact, so Hölder and the same HMS quadratic estimate give

$$
R_s=\lambda\mathbb ES
+\frac1{P_k}\sum_iK_{b_i}(u_i)
+\frac{4|\lambda|k}{d},
\qquad
u_i:=\frac{P_k\lambda A_i}{\sqrt d}>0.
\tag{22}
$$

Write $M_i=\sum_{j\ne i}m(b_j)$.  Then

$$
A_i=-\frac{M_i}{\sqrt d},\qquad
u_i=\frac{P_km_0M_i}{\sqrt d},\qquad
\frac{\lambda^2}{d}A_i^2=\frac{m_0^2M_i^2}{d}.
\tag{23}
$$

Subtracting (22) from (20) on this same history gives the identity

$$
H_s-R_s
=\frac{m_0^2}{d}\sum_iM_i^2
\left[1-P_k\psi_{b_i}(u_i)\right].
\tag{24}
$$

By (18), $M_i\ge(k-1)m_w$ and

$$
u_i\ge u_{k,w,d}:=
\frac{P_km_0m_w(k-1)}{\sqrt d}.
\tag{25}
$$

Using both monotonicities in (12), (24) yields the deterministic,
history-uniform group deficit

$$
R_s\le H_s-\mathsf d_{k,w,d}(P_k),
\tag{26}
$$

where

$$
\mathsf d_{k,w,d}(P_k):=
\frac{m_0^2m_w^2}{d}k(k-1)^2
\left[1-P_k\psi_{b_w}
\left(\frac{P_km_0m_w(k-1)}{\sqrt d}\right)\right].
\tag{27}
$$

A sufficient positivity condition for this uniform formula is

$$
P_kv_w<2.
\tag{28}
$$

At the limiting boundary $w=\omega_0$, for sufficiently large $C$ one has
$P_*(1)v_*<2$.  Since
$P_{k,d}^*\le P_*(1)$ for $k\le\ell$, continuity in $w$ implies that, for
each such fixed $C$, (28) holds simultaneously for the optimized choices
whenever $w$ lies in a sufficiently small right-neighborhood of $\omega_0$.
This is the only range used in the limit $w\downarrow\omega_0$.

Equations (16), (21), and (28) are the requested admissible region.  They
display all cutoff, Hölder, CGF-direction, and quadratic-feasibility
conditions; none is imported from the blue ledger.

### Step 4: optimize the admissible parameters

For fixed history and fixed $z=m_0M_i/\sqrt d>0$, the refined fraction of
the HMS linear budget is

$$
P\psi_b(Pz)=\frac{K_b(Pz)}{Pz^2}
=\frac1z\frac{K_b(Pz)}{Pz}.
\tag{29}
$$

Convexity of $K_b$, together with $K_b(0)=0$, implies that
$K_b(t)/t$ is nondecreasing for $t>0$.  Thus (29) is nondecreasing in $P$.
Since $P=Q/(Q-1)$ decreases with $Q$, the largest legal $Q_k$ gives the
largest deficit:

$$
Q_{k,d}^*=\frac{\sqrt d}{4m_0k},
\qquad
P_{k,d}^*=\frac{\sqrt d}{\sqrt d-4m_0k}.
\tag{30}
$$

Equality in the feasibility condition is allowed by the source moment
lemma.  Also, the monotonicities in Step 1 and $m_w\uparrow$ as $w\downarrow$
show that the deterministic bound (27) improves as the cutoff interval is
narrowed.  Therefore the optimal limiting window is $w\downarrow\omega_0$.

Let $k/\ell\to x$.  Since $\sqrt d/\ell\to D$, (30) gives

$$
P_{k,d}^*\longrightarrow P_*(x),
\qquad
\frac{P_{k,d}^*m_0m_w(k-1)}{\sqrt d}
\longrightarrow\frac{P_*(x)m_0m_wx}{D}.
\tag{31}
$$

The Riemann-sum limit of (27) is therefore

$$
\lim_{\ell\to\infty}
\frac1{\ell^2}\sum_{k=1}^{\ell-1}
\mathsf d_{k,w,d}(P_{k,d}^*)
=G(C,w),
\tag{32}
$$

where

$$
G(C,w):=
\frac{m_0^2m_w^2}{D^2}
\int_0^1x^3
\left[
1-P_*(x)\psi_{b_w}
\left(\frac{P_*(x)m_0m_wx}{D}\right)
\right]dx.
\tag{33}
$$

All functions in (33) are continuous on the relevant compact set.  Hence

$$
\lim_{w\downarrow\omega_0}G(C,w)=G_*(C),
\tag{34}
$$

with $G_*(C)$ as in (10).

This optimization has three distinct sources of strict finite-$C$ gain:

1. $\omega_0$ replaces the old $2\omega_0$ limiting relaxation;
2. $Q_{k,d}$ is taken at its legal boundary separately for every $k$, rather
   than using the old constant $D/(8m_0)$;
3. $K_b(u)$ is retained exactly, rather than replaced by $v(b)u^2/2$.

### Step 5: reverse induction, extraction, and the Ramsey rate

For any fixed $w>\omega_0$, the quantities in (27) depend only on $k,d$ and
the frozen parameters, not on the exposed history.  Replace the accumulated
deficit in the strengthened HMS induction by

$$
\mathcal D_{C,w,d}(r):=
\sum_{k=1}^{r-1}\mathsf d_{k,w,d}(P_{k,d}^*).
\tag{35}
$$

The reverse-induction step is identical to Step 3 of
`HMS_APPENDIX_BRIDGE.md`: the old accumulated sum is independent of the new
column, and (26) appends exactly the next group deficit.  Thus

$$
P^*_{R,r}\le\mathcal H_C(r)
\exp[-\mathcal D_{C,w,d}(r)],
\tag{36}
$$

where $\mathcal H_C$ is the same frozen HMS target; no source error is
estimated twice.

The extraction also survives.  By (13), the bracket in (27) lies in
$[0,1]$.  Because $b_w<c_p$, one has $m_w<m_0$, and for $0\le u\le\ell$,

$$
0\le
\mathcal D_{C,w,d}(\ell)
-\mathcal D_{C,w,d}(\ell-u)
\le
\frac{m_0^4\ell^3u}{d}
\le
\frac{m_0^4}{D^2}\,\ell u.
\tag{37}
$$

Now $m_0^4/D^2=(1+o(1))/(8\log C)<1$ for sufficiently large $C$.
Therefore the single $\ell u$ charge already reserved for loss of the old
group deficit in equations (23)--(23f) of `HMS_APPENDIX_BRIDGE.md` also pays
for (37).  The projection-failure factor remains
$(p/10)^{10\ell u}$, so the same subset sum is $o(1)$.  This proves the
unconditional analogue of (36).

Equations (32) and the frozen red first-moment calculation give, for every
$w>\omega_0$,

$$
\liminf_{\ell\to\infty}\frac1\ell
\log R(\ell,\lfloor C\ell\rfloor)
\ge
-\frac12\log p_C+\frac{B_R(C)}2+G(C,w).
\tag{38}
$$

The unchanged blue constraint is larger for sufficiently large $C$, since
its bonus is $1/2+o(1)$, while the red source bonus is $1/12+o(1)$ and
$G(C,w)=o(1)$.  Taking the supremum of (38) over all $w>\omega_0$ and using
(34) proves (T*).  Replacing the exact frozen red source bonus by HMS's
public $1/20$ bookkeeping proves (A*).

### Step 6: strict comparison with the previous companion term

The strict comparison can be made before changing either the old cutoff
window or the old Hölder exponents.  This avoids using the limiting-window
optimization as evidence for strictness.  The previous theorem used

$$
b_{\rm old}=c_p-2\omega_0,\quad
m_{\rm old}=m(b_{\rm old}),\quad
v_{\rm old}=v(b_{\rm old}),\quad
P_{\rm old}=\frac{D}{D-8m_0},
\tag{39}
$$

and

$$
\frac{c_R(C)}{4D^2}
=\frac{m_0^2m_{\rm old}^2}{4D^2}
\left(1-\frac{P_{\rm old}v_{\rm old}}2\right).
\tag{40}
$$

Keep these literal old choices and define the same-window exact-CGF gain

$$
G_{\rm same}(C):=
\frac{m_0^2m_{\rm old}^2}{D^2}
\int_0^1x^3
\left[
1-P_{\rm old}\psi_{b_{\rm old}}
\left(\frac{P_{\rm old}m_0m_{\rm old}x}{D}\right)
\right]dx.
\tag{40a}
$$

This is the Riemann-sum limit of (27) with exactly the old window and the
old constant pair $(P_{\rm old},Q_{\rm old})$.  On every same history, the
only changed step is the inequality

$$
K_{b_i}(u)\le\frac{v(b_i)u^2}{2}.
$$

Equation (12) gives, for every $u>0$,

$$
\psi_b(u)=\int_0^1(1-t)v(b+ut)\,dt
<\frac{v(b)}2.
\tag{40b}
$$

Thus the exact CGF has the required upper-bound direction on every
admissible positive tilt, and it is strictly smaller than the old quadratic
CGF envelope whenever $k\ge2$.  Applying (40b) pointwise for every $x>0$
in (40a), without changing any history or window, proves

$$
G_{\rm same}(C)>
\frac{m_0^2m_{\rm old}^2}{D^2}
\int_0^1x^3\left(1-\frac{P_{\rm old}v_{\rm old}}2\right)dx
=\frac{c_R(C)}{4D^2}.
\tag{40c}
$$

For every $x\in[0,1]$,

$$
P_*(x)\le\frac{D}{D-4m_0}<P_{\rm old},\qquad
m_*>m_{\rm old},\qquad
v_*<v_{\rm old}.
\tag{41}
$$

Increasing the lower cutoff $b_{\rm old}$ to $b_*$ increases $m$, decreases
$\psi_b$, and increases its positive argument; all three changes decrease
the refined fraction $P\psi_b(Pz)$.  Decreasing $P$ from $P_{\rm old}$ to
$P_*(x)$ decreases that fraction as well by (29).  Hence the comparison is
pointwise in $x$:

$$
G_*(C)>G_{\rm same}(C)>\frac{c_R(C)}{4D^2}.
\tag{41a}
$$

For completeness, the weaker variance-only comparison also follows from
(13) and (41):

$$
\begin{aligned}
G_*(C)
&\ge
\frac{m_0^2m_*^2}{D^2}
\int_0^1x^3\left(1-\frac{P_*(x)v_*}{2}\right)dx\\
&>
\frac{m_0^2m_{\rm old}^2}{4D^2}
\left(1-\frac{P_{\rm old}v_{\rm old}}2\right).
\end{aligned}
\tag{42}
$$

The right side is (40), again proving (S).  The first proof (40a)--(40c) is
the promised same-window, same-history strict comparison.  The passage to
the smaller limiting window was independently justified in Steps 2 and 5.

### Step 7: asymptotics and the method-internal upper bound

Put $L=\log(1/p)$.  The source asymptotics give

$$
m_0\sim\sqrt{2L},\qquad
D\sim4\sqrt2\,L^{3/2},\qquad
\omega_0=O(L^{-1/2}).
\tag{43}
$$

Consequently

$$
\frac{m_*}{m_0}\to1,\qquad
\sup_{0\le x\le1}P_*(x)\to1,\qquad
v_*\to0,\qquad
\sup_{0\le x\le1}u_*(x)\to0.
\tag{44}
$$

By (13), the bracket in (10) converges uniformly to one.  Hence

$$
G_*(C)
=(1+o(1))\frac{m_0^4}{D^2}\int_0^1x^3dx
=(1+o(1))\frac{m_0^4}{4D^2}
=\frac{1+o(1)}{32\log C},
\tag{45}
$$

which proves (O).

It remains to show that the coefficient cannot be doubled inside the stated
method class.  On the central admissible history $b_i=c_p$ for all $i$,

$$
\mu_i=-\frac{m_0}{\sqrt d},\qquad
A_i=-\frac{(k-1)m_0}{\sqrt d}.
\tag{46}
$$

Write the exact centered part of the quadratic form as

$$
W_s=\sum_iA_i\xi_i+\sum_{i<j}\xi_i\xi_j.
\tag{47}
$$

Independence and centering give $\mathbb EW_s=0$.  Jensen's inequality
therefore gives

$$
\log\mathbb E e^{\lambda W_s}\ge0.
\tag{48}
$$

The frozen HMS envelope allocates to this centered factor

$$
\frac{\lambda^2}{d}\sum_iA_i^2
+\frac{4|\lambda|k}{d}
=\frac{m_0^4}{d}k(k-1)^2
+\frac{4m_0k}{\sqrt d}.
\tag{49}
$$

Let $\delta_{C,k,d}$ be any uniform same-step saving in the class stated in
Claim B.  It must in particular be valid on the central history (or on a
sequence of admissible histories converging to it).  Equations (48)--(49)
therefore give

$$
\delta_{C,k,d}\le
\frac{m_0^4}{d}k(k-1)^2+\frac{4m_0k}{\sqrt d}.
\tag{49a}
$$

The second term is rate-negligible because

$$
\frac1{\ell^2}\sum_{k<\ell}\frac{4m_0k}{\sqrt d}
=O_C(\ell^{-1})\to0.
\tag{50}
$$

The first term sums exactly to

$$
\frac{m_0^4}{d}
\sum_{k=1}^{\ell-1}k(k-1)^2,
$$

whose $\ell^{-2}$ limit is $m_0^4/(4D^2)$.  This proves (M).  The central
history may be taken as a limit of red-perfect histories with diagonal
entries tending to one and projection inner products tending to zero; all
moment expressions are continuous there.  Therefore a uniform deficit
cannot evade (48) by excluding a probability-zero exact representative.

Combining (45) with (M) proves that the coefficient $1/32$ is sharp for
uniform, deterministic-per-group, additive centered-moment companions of
the frozen HMS ledger, not merely for the constant Hölder split used
previously.  The proof does not bound a history-dependent saving which is
retained in a richer state and only averaged after later exposures.
$\square$

## Corrections or Missing Assumptions

1. The old $2\omega_0$ window is a convenient finite-$\ell$ relaxation, not
   the optimal limiting window.  The proof above reaches $\omega_0$ only by
   proving every $w>\omega_0$ case and taking a supremum afterward.
2. One constant Hölder pair is not optimal.  The feasibility budget depends
   on $k$, so the optimal legal $Q_{k,d}$ is step-dependent.
3. The exact CGF improves the finite-$C$ term but not its leading large-$C$
   coefficient.  Claiming $1/16$ in the uniform additive class would exceed
   the complete centered-moment budget in (49a).
4. The upper bound (M) is method-internal.  It does not constrain a proof
   which changes the deterministic mean/connection potential, retains and
   later averages a history-dependent deficit, changes the dimension choice
   $D$, changes the blue construction, or changes the underlying random
   graph model.
5. The theorem retains the source-relative, existential quantifier order

   $$
   \exists C_0\ \forall C\ge C_0\ \exists\ell_0(C)\
   \forall\ell\ge\ell_0(C).
   $$

   No joint $C,\ell$ limit and no numerical $C_0$ is asserted.

## Next viable lemmas

There are two honest ways past the $1/32$ wall.

1. **Red mean-ledger lemma.**  Couple the exact connection probabilities,
   cutoff-dependent conditional means, and the cubic induction potential
   before the HMS tangent/coarsening, and prove a new negative group term of
   order $m_0^4k^3/d$ which is not part of the centered budget (49).  A
   history-uniform statement at this order would change the leading
   coefficient; another centered-CGF inequality cannot.
2. **Blue feasibility replacement.**  The source fixes
   $D\ge4aC/(1-p)$ through its blue quadratic moment.  Since the cap scales
   as $D^{-2}$, doubling it would require, at leading order, a construction
   valid near

   $$
   D\le\frac{4}{\sqrt2}\frac{aC}{1-p}
   =2\sqrt2\frac{aC}{1-p},
   $$

   followed by a fresh red/blue crossing calculation.  Such a result needs
   a genuinely sharper blue joint-moment or induction lemma; the blocked
   blue Hölder split in the frozen bridge does not supply it.

Either target changes a source term outside the obstruction proved here.

## Reproducibility

[hms_parameter_optimization_check.py](./hms_parameter_optimization_check.py)
recomputes, at 180 decimal digits:

1. the exact finite sum $\sum_{k<r}k(k-1)^2$;
2. $p_C,p,c_p,D,\omega_0$ and the exact centered CGF;
3. monotonicity orientations for $\psi_b(u)$ on diagnostic grids;
4. the old gain, its exact-CGF improvement with the identical old
   window/Hölder pair, the optimized constant-$Q$ gain, and $G_*(C)$;
5. the strict inequalities

   $$
   \frac{c_R(C)}{4D^2}
   <G_{\rm same}(C)<G_{\rm constant\ Q}(C)<G_*(C)
   <\frac{m_0^4}{4D^2};
   $$

6. numerical approach of $32\log C\,G_*(C)$ to one.

Run

```bash
.venv/bin/python routes/lower/hms_parameter_optimization_check.py
```

The script is an arithmetic replay, not evidence for the probabilistic
induction or the method upper bound.

## Open Risks

1. An independent referee should replay the exact-CGF scaling in (22)--(27),
   especially the factor $1/P_k$ and the standardized argument $u_i$.
2. The source preprints and this local extension have not received external
   peer review.
3. $G_*(C)$ is explicit, but the full exact-ledger theorem (T*) remains
   non-effective in $C$ because the frozen HMS constant $K$ is symbolic.
4. The proof optimizes a source-faithful rectangular cutoff lower envelope.
   It does not claim the best possible finite-$C$ deterministic deficit over
   all correlated cutoff vectors; only the large-$C$ leading coefficient in
   the uniform additive class of Claim B is proved optimal.

## Final Verdict

- **Strict improvement:** yes, $G_*(C)>c_R(C)/(4D^2)$ for every sufficiently
  large fixed $C$.
- **Raise $1/32$ to $1/16$ by Hölder/CGF/window tuning:** no.
- **Reason:** the optimized exact-CGF construction already asymptotically
  consumes the entire leading uniform additive centered-moment budget of
  the frozen HMS envelope.
- **Best next move:** change the red deterministic mean ledger or replace
  the blue lemma that forces the minimal dimension scale $D$.
