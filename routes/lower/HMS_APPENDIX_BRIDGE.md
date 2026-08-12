# HMS optimized-appendix comparator bridge

Date: 2026-08-12  
Target: the comparator bridge left open in
[PAIRED_COMPANION_ATTEMPT.md](./PAIRED_COMPANION_ATTEMPT.md)

Primary source snapshots:

- Hunter--Milojević--Sudakov (HMS), arXiv:2512.17718v2,
  `arXiv_version.tex`, SHA-256
  `b72958ac35554eccb94dedab5800349d2c021af7d60f767125cb46998e0fd54a`.
- Lin--Niu, arXiv:2605.25843v2,
  `off-diagonal-Ramsey-R.tex`, SHA-256
  `dbf1bfa2c7603c81b2e56a97028b138ccf9a9299a3d1f20c0b08cf489136f429`.

Line numbers below refer to these exact files.
The replay copies used for this audit were downloaded from the arXiv
`e-print` endpoints into
`/tmp/ramsey-hms-appendix.fr9Aam/hms/arXiv_version.tex` and
`/tmp/ramsey-hms-appendix.fr9Aam/linniu/off-diagonal-Ramsey-R.tex`.
Those temporary paths are reproducibility pointers, not repository inputs;
the hashes above are the authoritative identifiers.

## Claim

There are three logically separate claims.

1. **Red appendix bridge.** At HMS's Appendix-B choice

   $$
   p=p_C+\frac1C,\qquad
   D=\frac{4aC}{1-p},\qquad
   d_\ell=\left\lceil D^2\ell^2\right\rceil,
   \tag{1}
   $$

   the exact common-history deficit from the paired main-body proof can be
   inserted into the *same* red-perfect appendix induction, before any HMS
   error is coarsened.

2. **Blue appendix bridge by the same Hölder split.** At the same minimal
   value of $D$, an analogous positive blue deficit can be inserted using the
   $P,Q$ split of the paired proof.

3. **Ramsey consequence.** The red bridge alone gives a strict improvement
   of the printed HMS Appendix-B exponent because the printed final
   bookkeeping is red-limited.

The primary theorem is an exact frozen-ledger comparison. Freeze the
one-sided source constant $K$ as in (8a), and define $B_R(C)$ by (8c). There
is $C_0$ such that for every fixed real $C\ge C_0$, defining
$p_C,p,D,c_R(C)$ by (1), (4)--(7), one has

$$
\liminf_{\substack{\ell\to\infty\\\ell\in\mathbb N}}
\frac1\ell\log R\!\left(\ell,\lfloor C\ell\rfloor\right)
\ge-\frac12\log p_C+\frac{B_R(C)}2+\frac{c_R(C)}{4D^2}.
\tag{T}
$$

Relative to the **same** frozen HMS red ledger, whose rate is
$-\frac12\log p_C+B_R(C)/2$, the final term in (T) is a genuine strict
improvement.

Two useful consequences are kept separate:

1. the fully public-constant theorem

   $$
   \liminf_{\ell\to\infty}\frac1\ell
   \log R(\ell,\lfloor C\ell\rfloor)
   \ge-\frac12\log p_C+\frac1{20}+\frac{c_R(C)}{4D^2};
   \tag{A}
   $$

2. for every $\eta<1/12$, after increasing $C_0=C_0(\eta)$,

   $$
   \liminf_{\ell\to\infty}\frac1\ell
   \log R(\ell,\lfloor C\ell\rfloor)
   \ge-\frac12\log p_C+\eta+\frac{c_R(C)}{4D^2}.
   \tag{C}
   $$

For example, (C) permits $\eta=1/13$. Most of the $\eta$ term is latent HMS
source slack; only $c_R(C)/(4D^2)$ is companion-attributable.

## Status

- **Overall theorem (T), and consequences (A)--(C): PROVABLE**, subject to
  independent referee replay
  of this proof package before any external claim.
- **Red appendix bridge: PROVABLE.** It is proved below with an exact,
  history-uniform group deficit.
- **Blue appendix bridge by the same method: NOT JUSTIFIED.** At the
  worst blue step, the quadratic-moment feasibility condition and positivity
  of the proposed deficit require incompatible Hölder exponents. This is an
  obstruction to this proof device, not a proof that no sharper blue moment
  estimate exists.
- **Ramsey consequence: PROVABLE.** For every sufficiently large fixed $C$,
  the strengthened red ledger together with the unchanged HMS blue ledger
  proves (T), hence also (A)--(C). No blue refinement is required.

Thus the two-sided companion claim does not survive unchanged, but the part
needed for a new lower-bound theorem does.

## Assumptions

- $C$ is a sufficiently large fixed constant; after fixing $C$, let
  $\ell\to\infty$.
- $p_C\in(0,1/2)$ is the solution of

  $$
  C=\frac{\log p_C}{\log(1-p_C)}.
  $$

- The parameters $p,D,d_\ell$ are those in (1),
  $\Phi(-c_p)=p$, and $a=\phi(c_p)$.
- In the proof write $d=d_\ell$ and
  $D_\ell=\sqrt d/\ell$. Then $D_\ell\ge D$ and
  $D_\ell=D+O_C(\ell^{-2})$. This integer rounding preserves every source
  feasibility inequality and has no effect on the limiting coefficients.
- We use the HMS red- and blue-perfect events exactly as defined in HMS
  lines 955--971. In particular,

  $$
  \alpha_R=10\sqrt{\log(10/p)}.
  $$

- We use the upper-truncated cumulant-generating-function inequality proved
  in Lin--Niu lines 499--537. Its proof is self-contained and states that for
  $Z$ conditioned on $Z\le t$, its centered version $Y$, and $u>0$,

  $$
  \log\mathbb E e^{uY}\le
  \frac{u^2}{2}\operatorname{Var}(Z\mid Z\le t).
  \tag{2}
  $$

  The quantifiers are important: the lemma holds for **every**
  $t\in\mathbb R$ and **every** $u>0$, not merely near $-c_p$. For
  $X_i=Z_i/\sqrt d$ conditioned on $Z_i\le-b_i$, its application to
  $\exp(\tau(X_i-\mathbb EX_i))$ uses
  $t=-b_i$ and the standardized positive argument $u=\tau/\sqrt d$.
  The compact cutoff window is needed only to bound the variances and means
  uniformly, not for the validity of (2).

No assertion about a large-$C$-uniform blue refinement is assumed.

## Notation

For a standardized upper cutoff $-b$, define

$$
m_R(b):=\frac{\phi(b)}{\Phi(-b)},\qquad
v_R(b):=1+b\,m_R(b)-m_R(b)^2.
\tag{3}
$$

Thus, if $Z\sim N(0,1)$ is conditioned on $Z\le-b$, its mean and variance
are $-m_R(b)$ and $v_R(b)$, respectively. Put

$$
m_0:=m_R(c_p)=\frac ap,\qquad
\omega_C:=\frac{2\alpha_R^2}{D},
\tag{4}
$$

and define the compact-interval extrema

$$
m_-:=\min_{|b-c_p|\le\omega_C}m_R(b),\qquad
v_+:=\max_{|b-c_p|\le\omega_C}v_R(b).
\tag{5}
$$

The extrema in (5) are not numerical optimizations. Differentiation gives
$m_R'(b)=m_R(b)(m_R(b)-b)>0$, while the monotonicity of the variance of an
upper-truncated normal in its upper cutoff implies that $v_R(b)$ decreases
with $b$. Hence

$$
m_-=m_R(c_p-\omega_C),\qquad
v_+=v_R(c_p-\omega_C).
\tag{5a}
$$

Finally set

$$
Q_C:=\frac{D}{8m_0},\qquad
P_C:=\frac{Q_C}{Q_C-1},\qquad
\kappa_C:=1-\frac{P_Cv_+}{2},
\tag{6}
$$

and

$$
c_R(C):=\kappa_Cm_0^2m_-^2.
\tag{7}
$$

For sufficiently large $C$, all quantities in (5)--(7) are well defined and
$c_R(C)>0$. This sign is proved in Step 1 rather than assumed.

For an integer $r\ge1$, write

$$
\mathcal D_C(r)
:=\frac{c_R(C)}{d}\sum_{k=1}^{r-1}k(k-1)^2
=\frac{c_R(C)}{d}
  \frac{r(r-1)(r-2)(3r-5)}{12}.
\tag{8}
$$

Freeze a one-sided absolute constant $K$ large enough for every occurrence
of the red $O(\sqrt{\log p^{-1}}/D)$ term in HMS lines 1180--1289, and set

$$
\theta_C:=1-K\frac{\sqrt{\log p^{-1}}}{D}>0.
\tag{8a}
$$

For the extraction audit, the literal frozen HMS red appendix target is

$$
\mathcal H_C(r):=
p^{\binom r2}
\exp\left[
-\theta_C\frac{a^3}{p^3\sqrt d}\binom r3
+\frac apd^{-1/5}\binom r2+r
\right].
\tag{8b}
$$

All comparisons below use this same $\theta_C$ and this same
$\mathcal H_C$, so no hidden $O$-constant is compared across two ledgers.

Define the two source-ledger per-edge improvements relative to $p_C$ by

$$
B_R(C):=
-\log\frac p{p_C}
+\theta_C\frac{a^3}{3p^3D},
\tag{8c}
$$

and

$$
B_B(C):=
\log\frac{1-p_C}{1-p}
-\frac{4a^3C}{3(1-p)^3D}.
\tag{8d}
$$

The corresponding first-moment rate bonuses are $B_R(C)/2$ and
$CB_B(C)/2$. Lower-order terms from $\binom r3/\binom r2$ and integer
rounding vanish as $\ell\to\infty$.

## Source-line map

| Source lines | Function in this proof | Verdict |
|---|---|---|
| HMS 895--935 | Stops before the last Cauchy coarsening and gives the exact linear contribution $(\lambda^2/d)\sum_iA_i^2$ | usable unchanged |
| Lin--Niu 499--537 | Directional upper-truncated CGF (2) | usable unchanged |
| Lin--Niu 591--724 | $P,Q$ split; the centered-quadratic remainder stays $4|\lambda|k/d$ | usable unchanged |
| HMS 1192--1289 | Red appendix reverse induction | exact target ledger |
| HMS 1238--1275 | Red one-step moment claim; all later coarsening is applied to the HMS envelope | permits pathwise subtraction first |
| HMS 1296--1342 | Public red/blue bookkeeping bounds $e^{-1/10}$ and $e^{-1/(3C)}$ | final comparator |
| HMS 1344--1362 | Printed exponent $-\tfrac12\log p_C+\tfrac1{24}$ | strictly improved by (29) |
| HMS 1036--1176 | Blue appendix induction with tilt $\mu=f_r'(c_p)$ | same split is blocked |
| HMS 1105--1116 | Blue quadratic-moment feasibility $D\ge4\mu C$ | becomes $D\ge4Q\mu C$ after Hölder |

## Proof Strategy

The proof has five parts.

1. Prove that the red appendix histories keep every cutoff in one fixed
   compact interval and that (7) is strictly positive.
2. Subtract the refined and HMS moment envelopes *on the same history* before
   applying the source's coarse red estimate.
3. Add the resulting deterministic group deficit to the HMS appendix
   induction state and perform the same reverse induction.
4. Preserve the deficit through HMS's perfect-sequence extraction and final
   red/blue bookkeeping.
5. Separately show why the analogous blue $P,Q$ split cannot work at the
   source's minimal $D$.

## Dependency Map

1. The red local deficit uses (2), the exact HMS pre-Cauchy expression, and
   the cutoff window (10).
2. The red induction uses only the source law-of-total-probability identity,
   its connection-probability bound, and a deterministic deficit depending
   on the remaining group size.
3. The unconditional probability bound uses the same deletion charge as HMS;
   the loss $\mathcal D_C(r)-\mathcal D_C(r-u)$ is only $O_C(\ell u)$.
4. The Ramsey-rate theorem uses the strengthened red probability and HMS's
   unchanged blue probability.
5. The blue obstruction depends only on the central history $b_i=c_p$, so
   cutoff nonuniformity cannot remove it.

## Proof

### Step 1: the red appendix constants are positive

HMS line 1208 and red-perfectness give, at every red exposure step,

$$
\left|b_i-c_p-\sqrt d\,
\langle\pi_{s-1}(y_i),\pi_{s-1}(y_s)\rangle\right|
\le d^{-1/5}.
\tag{9}
$$

The red projection cutoff gives

$$
\left|\sqrt d\,
\langle\pi_{s-1}(y_i),\pi_{s-1}(y_s)\rangle\right|
\le \frac{\alpha_R^2}{D}.
$$

After increasing $\ell_0(C)$ so that
$d^{-1/5}\le\alpha_R^2/D$, (9) implies

$$
|b_i-c_p|\le\omega_C.
\tag{10}
$$

As $C\to\infty$, the standard Mills-ratio asymptotics and the definition of
$p_C$ give

$$
\begin{aligned}
p&=(1+o(1))p_C,\\
c_p&\sim\sqrt{2\log(1/p)},\\
m_0&\sim c_p,\\
D&\sim4\sqrt2\,\log(1/p)^{3/2},\\
\omega_C&=O(\log(1/p)^{-1/2})=o(1).
\end{aligned}
\tag{11}
$$

The functions in (3) are continuous. Moreover,
$v_R(c_p)=1-m_0(m_0-c_p)=o(1)$, and the same holds uniformly on the shrinking
interval in (5). Hence

$$
m_-=(1+o(1))m_0,\qquad v_+=o(1).
\tag{12}
$$

Also

$$
Q_C=\frac{D}{8m_0}\sim\frac12\log(1/p)\longrightarrow\infty,
$$

so $P_C=1+o(1)$. Equations (6) and (12) imply
$\kappa_C=1-o(1)>0$ and therefore

$$
c_R(C)>0
\tag{13}
$$

for every sufficiently large $C$. This establishes all sign and compactness
conditions used below.

### Step 2: exact red local subtraction inside the appendix history

Fix an HMS red-perfect history at exposure step $s$, and put $k=r-s$.
Under the conditioning in HMS line 1247, let

$$
X_i=y_i(s),\quad
\mu_i=\mathbb EX_i=-\frac{m_R(b_i)}{\sqrt d},\quad
\xi_i=X_i-\mu_i,
$$

and

$$
A_i:=\sum_{\substack{s<j\le r\\j\ne i}}\mu_j,\qquad
S:=\sum_{s<i<j\le r}X_iX_j,\qquad
\lambda:=-m_0\sqrt d.
\tag{14}
$$

Stopping the HMS proof at lines 906--913, before its last Cauchy inequality,
gives the valid envelope

$$
H_s=
\lambda\mathbb ES+
\frac{\lambda^2}{d}\sum_iA_i^2+
\frac{4|\lambda|k}{d}.
\tag{15}
$$

Apply Hölder with exponents $P_C,Q_C$. The quadratic factor is legal because

$$
4Q_C|\lambda|k
\le4\frac{D}{8m_0}m_0\sqrt d\,\ell
=\frac{D\ell\sqrt d}{2}
\le\frac d2<d.
\tag{16}
$$

All $\mu_i$ and $A_i$ are negative, while $\lambda<0$; hence the linear
CGF argument is positive and (2) applies. The same centered-quadratic HMS
bound, now with $Q_C\lambda$ and then raised to the power $1/Q_C$, gives

$$
R_s=
\lambda\mathbb ES+
\frac{P_C\lambda^2}{2d}\sum_i v_R(b_i)A_i^2+
\frac{4|\lambda|k}{d}
\tag{17}
$$

as a second valid upper envelope for $\log\mathbb Ee^{\lambda S}$.

Subtracting (17) from (15) is an exact same-history operation:

$$
H_s-R_s=
\frac{\lambda^2}{d}
\sum_i\left(1-\frac{P_Cv_R(b_i)}2\right)A_i^2.
\tag{18}
$$

By (5), (10), and (13),

$$
1-\frac{P_Cv_R(b_i)}2\ge\kappa_C,
\qquad
|A_i|\ge\frac{(k-1)m_-}{\sqrt d}.
$$

Since $\lambda^2/d=m_0^2$, (18) yields the deterministic pathwise bound

$$
R_s\le H_s-\mathsf d_k,\qquad
\mathsf d_k:=\frac{c_R(C)}d\,k(k-1)^2.
\tag{19}
$$

No HMS error term has been estimated twice in (19).

### Step 3: the strengthened red appendix induction

HMS lines 1248--1275 start from an upper bound at least as large as $H_s$:
they replace $\sum_iA_i^2$ by the final Cauchy bound and then coarsen the
mean and remainder. Therefore (19) implies the *same* HMS one-step claim,
with $-\mathsf d_k$ appended to its exponent. In a sign-explicit form, there
is the same absolute source constant $K$ such that the right side of HMS
line 1242 can be replaced by

$$
\exp\left(
-\left(1-K\frac{\sqrt{\log p^{-1}}}{D}\right)
 \frac{a^3}{p^3\sqrt d}\binom{k}{2}
+1-\mathsf d_k
\right).
\tag{20}
$$

Define the strengthened induction state by multiplying the right side of HMS
lines 1195--1198, for $k=r-s$, by

$$
\exp\left(-\sum_{t=1}^{k-1}\mathsf d_t\right).
\tag{21}
$$

The base case $k=0$ (or $k=1$) is unchanged. In the step from $s$ to $s-1$,
all old deficit terms in (21) are independent of the newly exposed column.
Use (20) for the only new moment. The HMS connection factor, geometric
potential, cubic term, $d^{-1/5}$ term, and linear error then merge exactly as
in lines 1277--1289, while

$$
\sum_{t=1}^{k-1}\mathsf d_t+\mathsf d_k
=\sum_{t=1}^{k}\mathsf d_t.
$$

This proves the strengthened appendix induction. At $s=0$ it gives

$$
P^*_{R,r}\le
\mathcal H_C(r)
\exp[-\mathcal D_C(r)].
\tag{22}
$$

Equation (22) is the requested appendix-ledger bridge.

### Step 4: extraction and the strengthened published bookkeeping

We audit the extraction at the only red size needed below, $r=\ell$.
If the HMS greedy extraction deletes $u$ vertices, then (8) gives

$$
0\le\mathcal D_C(\ell)-\mathcal D_C(\ell-u)
\le \frac{4c_R(C)\ell^3u}{d}
\le \frac{4c_R(C)}{D^2}\,\ell u.
\tag{23}
$$

Here is the complete exponent charge. With
$\alpha_R=10\sqrt{\log(10/p)}$, the projection-tail calculation in HMS
lines 400--410, with $C$ removed from the red projection cutoff as prescribed
at lines 959--966, gives

$$
p_I\le P^*_{R,\ell-u}\left(\frac p{10}\right)^{10\ell u}.
\tag{23a}
$$

The norm-failure probability is smaller because the appendix uses the
blue value of $\delta$. We also make the small retained-set endpoints
explicit. Although HMS states its red perfect-probability proposition for
$r\ge3$, its underlying reverse-induction proposition at lines 1192--1200 is
stated for every $r\ge1$; the strengthened induction above therefore proves
(22) unchanged for retained sizes $r=1,2$. For retained size $r=0$, use the
empty-event conventions

$$
P^*_{R,0}=1,\qquad \mathcal H_C(0)=1,\qquad \mathcal D_C(0)=0.
\tag{23a$'$}
$$

Thus (22), with this convention at $r=0$, is available for
$r=\ell-u$ for every $0\le u\le\ell$. To compare the right side of (23a)
with the $r=\ell$ target, put

$$
\Delta_2=\binom\ell2-\binom{\ell-u}{2},\qquad
\Delta_3=\binom\ell3-\binom{\ell-u}{3}.
$$

The exact combinatorial bounds are

$$
\Delta_2\le\ell u,\qquad
\Delta_3\le\frac{\ell^2u}{2}.
\tag{23b}
$$

Let $\theta_C$ be the fixed positive coefficient represented by
$1+O(\sqrt{\log p^{-1}}/D)$ in the source red ledger. For sufficiently large
$C$, $\theta_C\le2$, and

$$
\theta_C\frac{a^3}{p^3\sqrt d}\Delta_3
\le\frac{a^3}{p^3D}\,\ell u
\le \ell u,
\tag{23c}
$$

where the last inequality follows from
$a^3/(p^3D)\to1/2$. Equations (11)--(13) also give
$4c_R(C)/D^2\le1$ for sufficiently large $C$. Hence the total cost of
restoring the missing edge factor, cubic factor, and deficit is at most

$$
\bigl(\log(1/p)+2\bigr)\ell u.
\tag{23d}
$$

The positive $d^{-1/5}\binom r2$ and $r$ terms only make the $r=\ell$
target larger, so they require no charge. The logarithm of the failure factor
in (23a) has magnitude
$10\log(10/p)\ell u$, which strictly exceeds (23d). More explicitly,
combining (22) at $\ell-u$ with (23a)--(23d) gives, for every
$1\le u\le\ell$ and every set $I$ of $\ell-u$ retained indices,

$$
\begin{aligned}
p_I
&\le P^*_{R,\ell-u}
      \left(\frac p{10}\right)^{10\ell u}\\
&\le
\mathcal H_C(\ell)\,
\exp[-\mathcal D_C(\ell)]\,
\exp[-\eta_C\ell u],
\end{aligned}
\tag{23e}
$$

where one may take the concrete fixed-$C$ residual

$$
\eta_C
:=10\log(10/p)-\log(1/p)-2>0.
\tag{23f}
$$

The inequality (23e) uses the following literal exponent accounting:
$\log(1/p)\ell u$ restores the missing $p^{\Delta_2}$,
$\ell u$ restores the cubic term by (23c), and another $\ell u$ restores
the group deficit by (23). Since

$$
\sum_{u=1}^{\ell}\binom\ell u e^{-\eta_C\ell u}
=(1+e^{-\eta_C\ell})^\ell-1=o(1),
\tag{23g}
$$

while $u=0$ is the perfect term, summing (23e) over all retained sets proves

$$
P_{R,\ell}\le
\mathcal H_C(\ell)
\exp[-\mathcal D_C(\ell)](1+o(1)).
\tag{24}
$$

In particular, applying the unchanged HMS large-$C$ bookkeeping at lines
1314--1321 gives

$$
P_{R,\ell}\le
\left(p_Ce^{-1/10}\right)^{\binom\ell2}
\exp[-\mathcal D_C(\ell)](1+o(1)).
\tag{25}
$$

For integer $C\ell$, the blue estimate at HMS lines 1333--1339 remains

$$
P_{B,C\ell}\le
\left((1-p_C)e^{-1/(3C)}\right)^{\binom{C\ell}{2}}.
\tag{26}
$$

For the theorem statement put $q_\ell=\lfloor C\ell\rfloor$. The source's
blue-perfect Proposition at lines 977--985 is valid for every integer
$r\le C\ell$, so it applies directly to $q_\ell$. Repeating lines
1323--1339 with $q_\ell/\ell=C+O(\ell^{-1})$ gives

$$
\liminf_{\ell\to\infty}\rho_B(q_\ell)
\ge-\frac C2\log(1-p_C)+\frac16.
\tag{26a}
$$

Every parameter $p,D,d$ is unchanged; only occurrences of $C\ell$ in
polynomials are replaced by $q_\ell=C\ell+O(1)$, which changes their
$\ell^{-2}$ normalization by $o(1)$. Thus taking a floor neither changes nor
weakens the limiting blue constraint used below.

The exact sum in (8) gives

$$
\frac{\mathcal D_C(\ell)}{\ell^2}
\longrightarrow\frac{c_R(C)}{4D^2}.
\tag{27}
$$

We first retain the coarsened public constants as a checkpoint. Let
$n=\exp(\rho\ell)$. Equations (25)--(26a) show that the first moments of red
$K_\ell$ and blue $K_{q_\ell}$ tend to zero whenever

$$
\rho<-\frac12\log p_C+\frac1{20}+\frac{c_R(C)}{4D^2}
$$

and

$$
\rho<-\frac C2\log(1-p_C)+\frac16
=-\frac12\log p_C+\frac16,
\tag{28}
$$

respectively. Since $c_R(C)/D^2=o(1)$, the red constraint is the smaller one
for all sufficiently large $C$. Consequently,

$$
\boxed{
\liminf_{\ell\to\infty}
\frac1\ell\log R(\ell,\lfloor C\ell\rfloor)
\ge
-\frac12\log p_C+\frac1{20}+\frac{c_R(C)}{4D^2}.}
\tag{29}
$$

Equivalently, every fixed exponent strictly below the right side of (29) is
attained for all sufficiently large $\ell$.

We now recover the stronger claim (T) without the public coarsening.
From (24), (8b), and (27), the exact limiting red constraint is

$$
\rho<
-\frac12\log p_C
+\frac{B_R(C)}2
+\frac{c_R(C)}{4D^2},
\tag{29a}
$$

where $B_R(C)$ is (8c). From HMS lines 1307--1312 before their final
coarsening, applied to $q_\ell$, the exact limiting blue constraint is

$$
\rho<
-\frac12\log p_C+\frac{CB_B(C)}2,
\tag{29b}
$$

where (8d) uses
$-\frac C2\log(1-p_C)=-\frac12\log p_C$.

It remains to compare these two constraints, rather than assume which one is
active. Put $L=\log(1/p)$. The source asymptotics in HMS lines 1296--1336
give

$$
\frac p{p_C}=1+O(L^{-1}),\qquad
\frac{a^3}{p^3D}=\frac12+o(1),\qquad
\theta_C=1-o(1).
\tag{29c}
$$

Therefore

$$
B_R(C)=\frac16+o(1).
\tag{29d}
$$

On the blue side,

$$
\begin{aligned}
C\log\frac{1-p_C}{1-p}
&=C\log\left(1+\frac{1}{C(1-p)}\right)=1+o(1),\\
C\frac{4a^3C}{3(1-p)^3D}
&=\frac{Ca^2}{3(1-p)^2}=o(1),
\end{aligned}
\tag{29e}
$$

where the second equality uses $D=4aC/(1-p)$ and the last estimate is HMS
line 1336. Thus

$$
CB_B(C)=1+o(1).
\tag{29f}
$$

Finally, (31) below gives $c_R(C)/(4D^2)=o(1)$. Hence for every fixed
$C$ sufficiently large, (29d), (29f), and (31) imply

$$
\frac{B_R(C)}2+\frac{c_R(C)}{4D^2}
<\frac{CB_B(C)}2.
\tag{29g}
$$

Equations (29a), (29b), and (29g) prove the primary theorem (T). They prove
line by line that red is the final bottleneck and that retaining the old blue
construction does not constrain the new rate.

For every fixed $\eta<1/12$, (29d) also gives
$B_R(C)/2>\eta$ after increasing $C_0(\eta)$. Combining this with (T) proves
corollary (C); choosing $\eta=1/13$ gives a simple numerical version.
Equation (29) is exactly corollary (A).

This is a strict strengthening of the printed HMS exponent
$-\frac12\log p_C+1/24$. The constant improvement $1/20-1/24=1/120$ was
already latent in HMS's published probability Lemma (their theorem used
extra slack); the part attributable to the exact companion bridge is the
additional positive term

$$
\frac{c_R(C)}{4D^2}.
\tag{30}
$$

Accordingly, (29) must be read as the sum of three separately justified
pieces:

$$
\underbrace{-\frac12\log p_C+\frac1{24}}_{\text{printed HMS theorem}}
+
\underbrace{\frac1{120}}_{\text{unused HMS source slack}}
+
\underbrace{\frac{c_R(C)}{4D^2}}_{\text{new exact-deficit contribution}}.
\tag{30a}
$$

The first two terms alone are obtainable from HMS lines 1298--1362. Only the
last term is attributable to the present bridge.

From (11)--(13), if $L=\log(1/p)$, then

$$
c_R(C)=(1+o(1))m_0^4=(4+o(1))L^2,
\qquad
D^2=(32+o(1))L^3.
$$

Thus the attributable improvement has the transparent asymptotic form

$$
\frac{c_R(C)}{4D^2}
=\frac{1+o(1)}{32\log C}.
\tag{31}
$$

The factor in (31) is twice the $1/(64\log C)$ claimed by Lin--Niu because
their comparison assigns coefficient $1/2$ to the HMS linear moment, whereas
HMS lines 895--935 give coefficient $1$.

### Step 5: exact obstruction to the same blue Hölder bridge

It remains to explain why no blue term was used in (29). The optimized HMS
blue induction has a different potential. Let

$$
m_B:=\frac a{1-p},\qquad
\gamma_B:=m_B(c_p+m_B),\qquad
v_B=1-\gamma_B.
\tag{32}
$$

At $r=C\ell$, HMS lines 1112--1114 give the blue tilt

$$
\mu=f_r'(c_p)
=m_B\left(1-2\frac{m_Br}{\sqrt d}\gamma_B\right)
=m_B\left(1-\frac{\gamma_B}{2}\right),
\tag{33}
$$

where the last equality uses $D=4m_BC$.

If the paired $P,Q$ split were applied to this blue step, the centered
quadratic estimate with $Q\mu\sqrt d$ would require

$$
D\ge4Q\mu C,
\quad\text{hence}\quad
Q\le\frac{m_B}{\mu}
=\frac1{1-\gamma_B/2}.
\tag{34}
$$

On the central history $b_i=c_p$, positivity of the proposed linear deficit
would require

$$
1-\frac{P v_B}{2}>0,
\qquad P=\frac Q{Q-1}.
$$

Algebraically this is equivalent to

$$
Q>\frac2{1+\gamma_B}.
\tag{35}
$$

For the large-$C$ appendix regime,
$\gamma_B\sim2p\log(1/p)\to0$, in particular $\gamma_B<1/2$. But for
$0<\gamma_B<1/2$,

$$
\frac2{1+\gamma_B}
\ge
\frac1{1-\gamma_B/2}.
\tag{36}
$$

Thus (34) and (35) are incompatible. This failure already occurs at the
central cutoff, before any blue-perfect history variation is considered.
The earliest non-removable source term is the quadratic-moment condition in
HMS lines 1105--1116: their choice $D=4m_BC$ has no room for the Hölder
inflation needed to make the variance deficit positive.

This does not affect (T): the unchanged blue source rate has bonus
$1/2+o(1)$ by (29f), whereas the red source rate has bonus
$1/12+o(1)$ plus an $o(1)$ companion term.

## Corrections or Missing Assumptions

1. A claim of simultaneous red and blue improvement at the source choice
   $D=4aC/(1-p)$ must be weakened to the red claim, unless a new quadratic
   moment estimate avoids (34).
2. For each $\eta<1/12$, the new theorem first chooses
   $C\ge C_0(\eta)$ and then holds for every such **fixed** $C$ as
   $\ell\to\infty$. Uniformity in a joint $C,\ell$ limit is not claimed.
3. Equation (29) compares to the literal public HMS Appendix-B probability
   bounds. It does not identify an unspecified best constant hidden in a
   generic main-body $O(r^4/d)$.
4. The source's printed $1/24$ is not the optimized consequence of its own
   $e^{-1/10}$ red probability bound. The proof records the pre-existing
   $1/120$ slack separately from the new $D^{-2}$ term.
5. Because the source deliberately coarsens its red asymptotics, (29) is not
   claimed to be the optimal numerical consequence of the HMS construction.
   It is a fully specified improvement of a fully specified public ledger.

## Reproducibility

[hms_appendix_bridge_check.py](./hms_appendix_bridge_check.py), SHA-256
`86c8feb83246b986ba41c41ec62091b6efdd3c392cc4f46037ac3ff2d208ecc8`,
checks:

1. the exact finite sum in (8);
2. the explicitly defined $p_C,p,c_p,D,c_R(C)$;
3. positivity of $\kappa_C$ and the red/blue public-ledger bottleneck;
4. convergence of the leading source bonuses to $1/12$ and $1/2$;
5. the empty blue-Hölder interval in (34)--(36).

Run `python3 routes/lower/hms_appendix_bridge_check.py`.

The script is a floating-point arithmetic check and is not used in any proof
step.

## Open Risks

1. An independent line-by-line referee should verify the extraction
   bookkeeping in (24). The scale separation is strict for each fixed $C$,
   but HMS states that appendix extraction in prose rather than as a separate
   quantified lemma.
2. A genuinely two-sided optimized theorem would need a blue moment argument
   not based on the current $P,Q$ split, or a re-optimization with
   $D>4aC/(1-p)$ and a new red/blue crossing calculation.
3. The theorem is a proof-package result based on two preprints and has not
   undergone external peer review.

## Final Verdict

- The earliest appendix route divergence at HMS line 940 is repairable on
  the red side: the common-history deficit survives the exact optimized
  induction and the public bookkeeping.
- The corrected red coefficient relative to literal HMS is $1+\gamma_R$ at
  leading order, not $\gamma_R$.
- The resulting attributable rate gain is
  $c_R(C)/(4D^2)=(1+o(1))/(32\log C)$.
- The same Hölder mechanism is blocked on the optimized blue side by the
  exact incompatibility (34)--(36).
- Red alone proves the exact frozen-ledger theorem (T), adding the genuine
  term $c_R(C)/(4D^2)$ to the same HMS ledger rate
  $-\tfrac12\log p_C+B_R(C)/2$.
- The public theorem (A) and the asymptotic slack corollary (C) follow, but
  only the $c_R(C)/(4D^2)$ term in either statement is attributable to the
  new companion argument.
