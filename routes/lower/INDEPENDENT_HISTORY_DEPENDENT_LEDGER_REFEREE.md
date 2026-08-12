# Independent referee report on `HISTORY_DEPENDENT_LEDGER_ATTEMPT.md`

Date: 2026-08-12  
Review posture: source-level, adversarial, and independent of the author
checker

## Verdict

**PROVABLE AS STATED, relative to the two pinned source snapshots and the
already frozen HMS bridge.  PASS.**

I found no fatal mathematical gap in the weighted recursion, the full-box
concavity argument, the three-factor moment comparison, the
non-exchangeable reverse induction, the perfect-sequence extraction, or the
rate conversion.  In particular, the two savings in the claimed exponent
are not double counted:

1. the old term $G_*(C)$ is the deficit between the old HMS centered
   pre-Cauchy allocation and the exact centered linear CGF, with the
   deterministic mean held fixed;
2. the new term $H_*(C)$ comes from the central deterministic mean of the
   increment weights $\Delta_{ij}$, after paying every new centered linear
   and quadratic cost.

They occur in different summands of one exact same-history decomposition.
The decisive source-ledger identity is reconstructed in Section 6 below.

Thus the report supports, for every sufficiently large fixed $C$,

$$
\liminf_{\ell\to\infty}\frac1\ell
\log R\!\left(\ell,\lfloor C\ell\rfloor\right)
\ge
-\frac12\log p_C+\frac{B_R(C)}2+G_*(C)+H_*(C),
$$

as well as the public coarsening with $B_R(C)/2$ replaced by $1/20$ and

$$
H_*(C)=\frac{1+o(1)}{96\log C}>0.
$$

The quantifier is source-relative, existential, and non-effective:

$$
\exists C_0\ \forall C\ge C_0\ \exists\ell_0(C)\
\forall\ell\ge\ell_0(C).
$$

No numerical $C_0$, publication priority, or optimality beyond this
particular weighted ledger follows.

The earliest fatal gap is therefore **none in the stated theorem**.  The
first boundary at which the result would cease to be justified is replacing
the deterministic triangular array by outcome-dependent weights: the
measurability argument used in the reverse induction would then fail.  The
proof does not make that stronger claim.

## Materials and source integrity

I reviewed the frozen artifacts

- `HISTORY_DEPENDENT_LEDGER_ATTEMPT.md`, SHA-256
  `29c55690fbf37b884640ec2be3fc3d746ce810add6793ce7c014e06d08f23329`;
- `history_dependent_ledger_check.py`, SHA-256
  `e243d33c1cdc5bae94e7c4d06b80f7f60da5159f3a1485233e4ad91b06d29241`;
- `LOWER_HMS_PARAMETER_OPTIMIZATION.md`, SHA-256
  `32f22f107352b38549053794fef10fe3db853b5eee952a212c6ea058bc18bab1`;
- `HMS_APPENDIX_BRIDGE.md`, SHA-256
  `8d38003528d53d62589eb6ab0e960e29a494788bfe74bf23f871ee81d6732944`.

I independently downloaded the two cited arXiv v2 source archives.  Their
principal TeX files reproduce the hashes stated by the author:

- Hunter--Milojević--Sudakov, arXiv:2512.17718v2,
  `arXiv_version.tex`, SHA-256
  `b72958ac35554eccb94dedab5800349d2c021af7d60f767125cb46998e0fd54a`;
- Lin--Niu, arXiv:2605.25843v2,
  `off-diagonal-Ramsey-R.tex`, SHA-256
  `dbf1bfa2c7603c81b2e56a97028b138ccf9a9299a3d1f20c0b08cf489136f429`.

All source-line references in this report refer to those exact snapshots.

## Dependency map

1. HMS lines 895--935 give the pre-Cauchy centered-moment allocation and
   the centered quadratic square-MGF estimate.
2. Lin--Niu lines 360--493 prove monotonicity of truncated variance in the
   upper cutoff; lines 499--537 give the exact positive-direction CGF.
3. HMS lines 963--971 and 1202--1208 give red-perfectness and the cutoff
   relation.
4. The weighted gradient identity supplies the boundary edges missing from
   the projection potential.
5. Three-factor Hölder compares the new centered moment to the already
   optimized old centered moment on the same history.
6. The source ledger is reopened before its $O(\cdot)$ coarsening; this is
   what permits both the old exact-CGF deficit and the new deterministic-mean
   deficit to be charged once.
7. HMS lines 1192--1289 provide the reverse-induction skeleton, and the
   perfect-sequence extraction supplies the unconditional probability bound.
8. The unchanged blue ledger remains above the strengthened red constraint,
   so the original first-moment crossing applies.

## 1. Source reconstruction: pre-Cauchy exponent and reverse induction

At a red exposure step with $k$ future variables, set

$$
X_j=\mu_j+\xi_j,
\qquad
\mu_j=-\frac{m_j}{\sqrt d},
\qquad
M_j=\sum_{q\ne j}m_q,
\qquad
\lambda=-m_0\sqrt d.
$$

For the uniform quadratic sum $S=\sum_{j<q}X_jX_q$, HMS lines 895--903
split

$$
S=\mathbb ES+\sum_j A_j\xi_j+\sum_{j<q}\xi_j\xi_q,
\qquad
A_j=-\frac{M_j}{\sqrt d}.
$$

Stopping HMS lines 906--935 before the final Cauchy bound gives the exact
pre-Cauchy envelope

$$
H_i
=\lambda\mathbb ES
+\frac{\lambda^2}{d}\sum_jA_j^2
+\frac{4|\lambda|k}{d}.
\tag{R1}
$$

The coefficient of $\sum A_j^2$ is one: the doubled linear tilt initially
produces coefficient two and the square root in HMS line 903 halves it.
With $t_0=m_0\sqrt d$, the centered part of (R1) is

$$
\mathcal U_i
=\frac{m_0^2}{d}\sum_jM_j^2+\frac{4t_0k}{d}.
\tag{R2}
$$

The optimized old centered envelope is

$$
\mathcal C_i^{\rm old}
=\mathcal L(P_0,u^0)+\frac{4t_0k}{d},
\tag{R3}
$$

and therefore the old exact-CGF deficit is exactly

$$
\mathsf d_i
=\mathcal U_i-\mathcal C_i^{\rm old}.
\tag{R4}
$$

This recovers equations (20)--(27) of the frozen optimization package from
the pinned HMS source.  It is important that (R4) contains no deterministic
mean term: that term cancels before the deficit is taken.

HMS lines 1192--1289 use reverse induction on the number of exposed columns.
Conditioned on $M[s-1]$, the entries below the diagonal in column $s$ are
independent; conditioning on all red edges from $s$ leaves independent
upper-truncated Gaussians (HMS lines 1211--1248).  The source projection
identity then merges the old potential after the conditional moment is
bounded.  These are precisely the structural facts used by the enlarged
state; no exchangeability of the scalar coefficient is part of the source
induction.

## 2. Weighted recursion, gradient, and projection indices: PASS

For $i<j$, the proposed recursion is

$$
T_{ij}=t_0+\gamma_d
\sum_{\substack{q>i\\q\ne j}}T_{jq},
\qquad
\gamma_d=\frac{m_0m'_0}{\sqrt d}.
\tag{R5}
$$

Every edge in the sum has both endpoints greater than $i$, so it has already
been defined when first endpoints are processed in decreasing order.  The
array is deterministic once $(r,d,C)$ are fixed and hence is measurable
before the relevant column is sampled.

For

$$
F_i(b)=\sum_{j>i}\log\Phi(-b_j)
-\frac1d\sum_{i<j<q}T_{jq}m(b_j)m(b_q),
$$

direct differentiation at $c\mathbf1$ gives

$$
\partial_jF_i(c\mathbf1)
=-m_0-\frac{m_0m'_0}{d}
  \sum_{\substack{q>i\\q\ne j}}T_{jq}
=-\frac{T_{ij}}{\sqrt d}.
\tag{R6}
$$

Thus, after substituting

$$
b_j-c=\sqrt d\,
\langle\pi_{i-1}(y_i),\pi_{i-1}(y_j)\rangle+e_{ij},
\qquad |e_{ij}|\le d^{-1/5},
$$

the tangent contributes the missing boundary edge

$$
-T_{ij}\langle\pi_{i-1}(y_i),\pi_{i-1}(y_j)\rangle
$$

with the stated diagonal error.  At the same time

$$
\langle\pi_i(y_j),\pi_i(y_q)\rangle
=\langle\pi_{i-1}(y_j),\pi_{i-1}(y_q)\rangle
+y_j(i)y_q(i).
$$

Consequently the old future edges and the new boundary edges form exactly
the potential at state $i-1$.  There is no missing edge, duplicate edge, or
one-step index shift.

### The requested audit of the second line of Lemma 4

For a fixed edge $j<q$, apply (R5) with first endpoint $j$ and second
endpoint $q$.  The index in its weighted degree ranges over

$$
\{j+1,\ldots,r\}\setminus\{q\},
$$

which has exactly $r-j-1$ elements.  Every corresponding weight lies in
$[t_0,t_0/(1-\rho_C)]$.  Hence

$$
\gamma_dt_0(r-j-1)
\le\Delta_{jq}
\le\frac{\gamma_dt_0(r-j-1)}{1-\rho_C}.
\tag{R7}
$$

The count is independent of the location of $q$ because terms with
$j<k<q$ use the already defined symmetric edge $T_{kq}$.  The second line
of Lemma 4 is therefore correct.

Summing (R7) over future edges gives

$$
S_i\ge\gamma_dt_0\frac{k(k-1)(k-2)}3,
$$

and summing over exposure steps gives

$$
\sum_iS_i\ge2\gamma_dt_0\binom r4
=2m_0^2m'_0\binom r4.
\tag{R8}
$$

The factor two and the binomial index in (R8) are both correct.

## 3. Full cutoff-box Hessian and the sign of $m''$: PASS

For the proof document's cutoff parameter,

$$
m'(b)=m(b)(m(b)-b)=1-v(b).
$$

Lin--Niu parameterize by the upper cutoff $t=-b$ and prove that the
conditional variance $V(t)$ is nondecreasing in $t$.  Therefore

$$
v(b)=V(-b)\quad\text{is nonincreasing},
\qquad
m''(b)=-v'(b)\ge0.
\tag{R9}
$$

This cutoff-orientation translation is the main possible sign trap; the
proof document has it in the correct direction.

The Hessian is

$$
\begin{aligned}
(\nabla^2F_i)_{jj}
&=-m'(b_j)-\frac{m''(b_j)}d
  \sum_{q\ne j}T_{jq}m(b_q),\\
(\nabla^2F_i)_{jq}
&=-\frac{T_{jq}}d m'(b_j)m'(b_q).
\end{aligned}
$$

All extra diagonal contributions to $-\nabla^2F_i$ are nonnegative by
(R9).  Since

$$
\frac1d\sum_{q\ne j}T_{jq}
\le\frac{m_0}{D(1-\rho_C)},
$$

the off-diagonal absolute row sum is at most

$$
j_+(w)^2\frac{m_0}{D(1-\rho_C)}.
$$

Condition (19) makes the symmetric matrix $-\nabla^2F_i$ strictly
diagonally dominant with positive diagonal on the *entire* box
$[c-w,c+w]^{V_i}$.  Gershgorin therefore proves positive definiteness
uniformly; the proof is not relying on the checker's sampled grid.

## 4. Three-factor Hölder and all centered costs: PASS

The exponent splits exactly into a deterministic mean and three centered
factors:

$$
\sum_j(u_j^0+\delta u_j)\sqrt d\,\xi_j,
\quad
-t_0\sum_{j<q}\xi_j\xi_q,
\quad
-\sum_{j<q}\Delta_{jq}\xi_j\xi_q.
$$

With

$$
Q_0=\frac d{4t_0k},
\qquad
Q_1=\frac d{4R_i},
\qquad
\frac1P=1-\frac1{Q_0}-\frac1{Q_1},
$$

condition (35) gives $Q_0,Q_1>1$ and $1<P\le2$.

### Uniform quadratic factor

HMS lines 915--935 apply with tilt $-Q_0t_0$.  The source condition is

$$
d\ge4Q_0t_0k,
$$

which holds with equality.  After the $Q_0$-th root, the contribution is
exactly $4t_0k/d$.  Equality here is allowed; the square-MGF denominator in
the source proof still has strict room.

### Increment quadratic factor

Since $\Delta_{jq}\ge0$,

$$
-\sum_{j<q}\Delta_{jq}\xi_j\xi_q
\le\frac12\sum_jR_j\xi_j^2.
$$

The square-MGF argument is

$$
x_j=\frac{Q_1R_j}{2d}\le\frac18.
$$

HMS lines 878--893 give

$$
\log\mathbb E e^{(Q_1R_j/2)\xi_j^2}
\le\frac{16}{3}x_j.
$$

After independence, summation, and the $Q_1$-th root,

$$
\frac1{Q_1}\sum_j\frac{16}{3}
\frac{Q_1R_j}{2d}
=\frac{16}{3}\frac{S_i}{d},
$$

because $\sum_jR_j=2S_i$.  The constant $16/3$ is correct.

### Linear factor

For $Z\le-b$, the exact centered CGF is

$$
K_b(u)=\frac{u^2}{2}+um(b)
+\log\Phi(-b-u)-\log\Phi(-b),
$$

and

$$
K_b''(u)=v(b+u)\in[0,1]
\qquad(u\ge0).
$$

Thus all arguments are in the positive direction required by Lin--Niu.
Integrating $K_b''\le1$ proves

$$
\frac{K_b(P(u+\delta))-K_b(Pu)}P
\le2u\delta+\delta^2,
$$

and convexity together with the same second-derivative bound gives

$$
0\le\partial_P\frac{K_b(Pu)}P\le u^2.
$$

The deterministic estimates then yield, term by term,

$$
\left[
\frac{4m_0M_w^2}{D},
\frac{2M_w^2m_0^2m'_0}{(1-\rho_C)D^2},
\frac{96m_0^2M_w^2}{(1-\rho_C)D^2}
\right]\frac{S_i}{d}.
$$

I independently checked the powers of $d$, the factor two from
$\sum_jR_j=2S_i$, and the use of $R_i/S_i$.  Their sum is precisely
$L_w(C)S_i/d$.

## 5. Deterministic feasibility and asymptotic signs: PASS

The recursion gives

$$
T_{\max}\le t_0+\gamma_drT_{\max},
\qquad
\gamma_dr\le\rho_C,
$$

so $T_{\max}\le t_0/(1-\rho_C)$.  This proves every weight and Hölder
feasibility bound used above.

As $C\to\infty$, writing $L=\log C$ at leading order,

$$
m_0^2=(2+o(1))L,
\qquad
D^2=(32+o(1))L^3,
\qquad
m'_0\to1,
\qquad
\rho_C\to0.
$$

Also $M_w/m_0\to1$ in the limiting window.  Consequently

$$
L_w(C)=o(m_0^2),
\qquad
B_w(C)=m_0^2-\frac{16}{3}-L_w(C)>0
$$

eventually.  The full-box condition and condition (35) likewise hold for
all sufficiently large $C$.  These are existential large-$C$ statements,
as claimed.

## 6. Critical audit of equations (51)--(52): PASS, no double count

This is the central audit.

Let

$$
A_0:=\frac{m_0^3}{\sqrt d}\binom k2,
\qquad
\mathcal U_i:=\frac{m_0^2}{d}\sum_jM_j^2+\frac{4t_0k}{d},
$$

where $\mathcal U_i$ is the old HMS pre-Cauchy centered allocation from
(R2).  Let $\mathcal C_i^{\rm old}$ be (R3).  The already proved exact-CGF
deficit is the same-history identity

$$
\mathsf d_i=\mathcal U_i-\mathcal C_i^{\rm old}.
\tag{R10}
$$

The new joint tangent and Lemma 3 give, before source coarsening,

$$
\begin{aligned}
E_i^{\rm new}
\le{}&k\log p-A_0
-\frac{m_0^2S_i}{d}
-\sum_{j>i}T_{ij}h_{ij}
+\varepsilon_i\\
&+\mathcal C_i^{\rm old}
+\left(\frac{16}{3}+L_w(C)\right)\frac{S_i}{d},
\end{aligned}
\tag{R11}
$$

with

$$
0\le\varepsilon_i
\le\frac{d^{-1/5}}{\sqrt d}\sum_{j>i}T_{ij}.
$$

Substituting (R10) into (R11) produces the exact ledger

$$
\begin{aligned}
E_i^{\rm new}
\le{}&
\left[k\log p-A_0+\mathcal U_i\right]
-\sum_{j>i}T_{ij}h_{ij}+\varepsilon_i
-\mathsf d_i\\
&-\left[m_0^2-\frac{16}{3}-L_w(C)\right]
  \frac{S_i}{d}.
\end{aligned}
\tag{R12}
$$

Equation (R12) displays the separation:

- $-\mathsf d_i$ is the old centered exact-CGF saving;
- $-m_0^2S_i/d$ is the new deterministic central-mean saving;
- $(16/3+L_w(C))S_i/d$ pays every new centered factor.

Nothing in $-m_0^2S_i/d$ was used to establish (R10), and nothing in
$\mathsf d_i$ is used again to pay the new centered costs.  Therefore the
coefficient in equations (51)--(52) is genuinely

$$
B_w(C)=m_0^2-\frac{16}{3}-L_w(C).
$$

### Why the frozen source $K$ is unchanged

The bracket in (R12) is

$$
k\log p-A_0+\mathcal U_i.
\tag{R13}
$$

HMS lines 1252 and 1260--1264 already bound the two summands of
$\mathcal U_i$: the square-MGF remainder is paid by the source's `+1`, and
the centered linear allocation is paid inside the
$O(\sqrt{\log p^{-1}}/D)$ coefficient.  Replacing the history-perturbed
deterministic mean by $-A_0$ introduces no new error; it removes the source
mean-perturbation error.  Hence the very same one-sided absolute constant
$K$ frozen for those source occurrences gives

$$
-A_0+\mathcal U_i
\le
-\left(1-K\frac{\sqrt{\log p^{-1}}}{D}\right)A_0+1.
\tag{R14}
$$

No new $O(\cdot)$ term has appeared in (R14), and no enlargement of $K$ is
needed.  This is stronger than merely saying that another unspecified
constant could absorb the new calculation.  Combining (R12)--(R14) proves
the stated frozen one-step envelope with both deficits exactly once.

## 7. Non-exchangeable reverse induction: PASS

For a fixed target size $r$, construct the entire deterministic triangular
array $T_{ij}$ before exposure.  At state $s$, retain

$$
\mathcal P_s
=-\sum_{s<i<j\le r}T_{ij}
\langle\pi_s(y_i),\pi_s(y_j)\rangle
$$

together with the accumulated old deficits and the deterministic new
charges from already exposed steps.

The clean base is $s=r$ (empty future set), or equivalently $s=r-1$ after
the vacuous transition.  In the step from $s=i$ to $s=i-1$:

1. $-Q_T$ supplies the new-coordinate part of all future weighted edges;
2. (R6) supplies precisely the boundary edges $(i,j)$;
3. the previous-coordinate parts retain every future edge;
4. the old deficit and the new charge append exactly their $i$-th terms.

At $s=0$, $\pi_0=0$, so the projection potential vanishes.  This yields

$$
P^*_{R,r}\le\mathcal H_C(r)
\exp\left[
-\mathcal D_{C,w,d}(r)
-\frac{2m_0^2m'_0B_w(C)}d\binom r4
+J_{r,d}
\right].
$$

The array is non-exchangeable but deterministic.  Reverse induction needs
measurability, not exchangeability, and that requirement is satisfied.

## 8. Perfect-sequence extraction and $J_q\le J_\ell$: PASS

For every retained ordered set of size $q$, relabel it in its retained order
and construct the deterministic $q$-vertex weight array.  Red-perfectness is
preserved by the HMS greedy extraction, and $q/\sqrt d\le1/D$, so every
finite-size condition only improves.

If $u=\ell-q$ vertices are deleted, then

$$
\binom\ell4-\binom{\ell-u}4
\le u\binom\ell3\le\frac{\ell^3u}{6}.
$$

The new-deficit restoration cost is therefore at most

$$
\frac{m_0^2m'_0B_w(C)}{3D^2}\,\ell u
=\left(\frac{1+o(1)}{24\log C}\right)\ell u
<\ell u
$$

for sufficiently large $C$.  The old optimized deficit costs at most one
further $\ell u$, as proved in the frozen package.

The diagonal error satisfies

$$
0\le J_{q,d}
\le\frac{m_0}{1-\rho_C}d^{-1/5}\binom q2
\le J_{\ell,d}.
$$

This inequality is sufficient because $J$ occurs with a **positive** sign
in the probability upper bound.  When comparing the retained-$q$ bound to
the target at $\ell$, replacing $J_{q,d}$ by the larger $J_{\ell,d}$ makes
the target weaker; no restoration charge is required.  The fact that
$J_{\ell,d}=o_C(\ell^2)$ also removes it from the rate.

Together, the missing-edge factor, cubic term, old deficit, and new deficit
cost at most

$$
\bigl(\log(1/p)+3\bigr)\ell u
$$

for sufficiently large $C$.  The projection-failure factor contributes

$$
-10\log(10/p)\,\ell u,
$$

which strictly dominates.  Thus the residual subset sum is $o(1)$ over all
$0\le u\le\ell$.  Small retained sizes cause no problem because every pair
and four-set charge vanishes at the appropriate endpoint, as in the frozen
bridge.

## 9. Rate coefficient, asymptotics, and red--blue crossing: PASS

At $r=\ell$,

$$
\lim_{\ell\to\infty}
\frac{2m_0^2m'_0B_w(C)}{d\ell^2}\binom\ell4
=\frac{m_0^2m'_0B_w(C)}{12D^2}.
$$

The factor $1/12$ is correct: the accumulated mass contributes the factor
two in (R8), while $\binom\ell4/\ell^4\to1/24$.

Since $B_w(C)\sim m_0^2$, $m'_0\to1$,
$m_0^2\sim2\log C$, and $D^2\sim32(\log C)^3$,

$$
H_*(C)
=\frac{m_0^2m'_0B_*(C)}{12D^2}
=\frac{1+o(1)}{96\log C}.
$$

The frozen red and blue baselines agree through
$\log p_C=C\log(1-p_C)$.  Their source bonuses tend respectively to
$1/12$ and $1/2$, whereas

$$
G_*(C)+H_*(C)=O(1/\log C)=o(1).
$$

Thus the strengthened red constraint remains the bottleneck for all
sufficiently large $C$; the unchanged blue bound and the same first-moment
argument prove the displayed Ramsey inequality.  Replacing the exact frozen
red bonus by the already certified public $1/20$ leaves both positive
companion terms intact.

## 10. Checker replay and its evidentiary limit

The frozen checker runs successfully and reports:

- finite weighted recursion, gradient, and mass bounds: PASS;
- sampled Hessian and exact linear-CGF cost comparison: PASS;
- cutoff-box feasibility and positivity: PASS;
- convergence toward $1/(96\log C)$: PASS.

This output is useful arithmetic evidence only.  The checker samples one
nonconstant cutoff vector and several large finite values of $C$; it cannot
prove full-box concavity, source-ledger compatibility, reverse induction,
extraction, or the asymptotic quantifiers.  The PASS verdict above rests on
the analytic and source-level reconstruction, not on those printed labels.

## Minor presentation defects (non-fatal)

The frozen Markdown contains several dropped TeX backslashes or separators,
including the displayed cutoff approximation near (22), `\le` near (23),
`\qquad` near (28), `\left[` near (52), and `\to` near (62).  Reading the
intended formulas from their surrounding definitions leaves the mathematical
argument unambiguous.  These should be repaired before publication, but they
do not change this verdict.

## Scope warning

This report validates only the pinned, source-relative theorem and its
stated large-$C$ asymptotic.  It does not validate an effective threshold,
an outcome-adaptive weight array, a blue-side improvement, a finite Ramsey
number, a diagonal upper bound, or a claim that the coefficient $1/96$ is
optimal among all enlarged induction states.
