# History-weight optimization beyond exact gradient merge

## Status and scope

**Status:** author proof package, **provable as stated relative to the pinned
HMS/source bridge**, pending an independent source referee.  This file and its
checker are deliberately noncanonical.  Nothing in the canonical lower-bound
route is changed by this package.

The result is a fixed-large-`C` asymptotic theorem.  It does **not** claim a
finite value of the threshold in `C`, a finite Ramsey-number improvement, a
new blue argument, an unconditional improvement outside the frozen HMS
framework, or novelty/priority/world-best status.

This note answers two separate questions.

1. General deterministic triangular weights and a uniform potential scale
   give no freedom if the boundary gradient is required to merge exactly.
   This exact-merge class has the pinned leading constant
   `1/(96 log C)`.
2. Keeping the negative quadratic term supplied by full-box strong concavity
   permits a deterministic boundary residual.  A controlled residual closes
   every ledger gate and raises the source-relative term to
   `1/(64 log C)`.

## Pinned inputs

The proof below uses exactly these frozen inputs.

| role | file | SHA-256 |
|---|---|---|
| refereed predecessor proof | `HISTORY_DEPENDENT_LEDGER_ATTEMPT.md` | `29c55690fbf37b884640ec2be3fc3d746ce810add6793ce7c014e06d08f23329` |
| predecessor arithmetic replay | `history_dependent_ledger_check.py` | `e243d33c1cdc5bae94e7c4d06b80f7f60da5159f3a1485233e4ad91b06d29241` |
| independent predecessor referee | `INDEPENDENT_HISTORY_DEPENDENT_LEDGER_REFEREE.md` | `a858849824862ca1ab07dc1a9682275a19a0af811c45a7e60f28a4579a474dd4` |
| optimized HMS deficit | `LOWER_HMS_PARAMETER_OPTIMIZATION.md` | `32f22f107352b38549053794fef10fe3db853b5eee952a212c6ea058bc18bab1` |
| literal HMS appendix bridge | `HMS_APPENDIX_BRIDGE.md` | `8d38003528d53d62589eb6ab0e960e29a494788bfe74bf23f871ee81d6732944` |
| arithmetic replay for this note | `history_weight_optimization_next_check.py` | `616040b91aad4becf92dcfbe13b7e6d49a3c9c73f0f222ba56114104f1c7d554` |

The source-level assumptions, the definitions of `p_C,p,c,D,B_R(C),G_*(C)`,
the cutoff error, and the HMS first-moment extraction are exactly those in the
pinned files.  In particular, this note does not strengthen a source lemma.

## The source-relative theorem

Use the predecessor notation

\[
m_0=m(c),\qquad m'_0=m'(c),\qquad
\rho=\frac{m_0m'_0}{D},\qquad
\omega_0=\frac{100\log(10/p)}D.
\]

For fixed `w>omega_0`, put

\[
M_w=m(c+w),\qquad
j_-(w)=m'(c-w),\qquad j_+(w)=m'(c+w),
\]

and define

\[
\theta=m_0^2,\qquad A_0=m_0^2m'_0,
\]

\[
a_- =\min\{A_0,\theta\},\qquad
a_+=\max\left\{\theta,
 \frac{A_0+\rho\theta}{1-\rho}\right\},
\tag{1}
\]

\[
\mu_w=
j_-(w)-j_+(w)^2
\frac{m_0+\theta/D}{D(1-\rho)},
\tag{2}
\]

\[
\widehat L_w(C)=
\frac{4m_0M_w^2}{D}
+\frac{2M_w^2a_+}{D^2}
+\frac{32m_0^2M_w^2a_+}{a_-D^2},
\tag{3}
\]

\[
\widehat B_w(C)=m_0^2-\frac{16}{3}-\widehat L_w(C),
\qquad
E_w(C)=\widehat B_w(C)\theta-
\frac{\theta^2}{2\mu_w},
\tag{4}
\]

\[
\widehat H(C,w)=
\frac{\widehat B_w(C)A_0+E_w(C)}{12D^2},
\qquad
\widehat H_*(C)=\lim_{w\downarrow\omega_0}\widehat H(C,w).
\tag{5}
\]

**Theorem.**  For all sufficiently large fixed `C`, the frozen HMS construction
satisfies

\[
\boxed{
\liminf_{\ell\to\infty}\frac1\ell
\log R(\ell,\lfloor C\ell\rfloor)
\ge
-\frac12\log p_C+\frac{B_R(C)}2+G_*(C)+\widehat H_*(C).}
\tag{6}
\]

Moreover,

\[
\widehat H_*(C)>H_*(C)>0
\quad\hbox{for all sufficiently large }C,
\qquad
\boxed{\widehat H_*(C)=\frac{1+o(1)}{64\log C}.}
\tag{7}
\]

The public coarsening `B_R(C)/2 >= 1/20` therefore remains available with
`H_*` replaced by `widehat H_*`.

## 1. Exact merge has a unique triangular array

Let `W_ij` be any deterministic symmetric triangular weight array used in

\[
F_i(b)=\sum_{j>i}\log\Phi(-b_j)
-\frac1d\sum_{i<j<q}W_{jq}m(b_j)m(b_q).
\tag{8}
\]

At the central cutoff,

\[
\partial_jF_i(c\mathbf1)
=-m_0-\frac{m_0m'_0}{d}
  \sum_{\substack{q>i\\q\ne j}}W_{jq}.
\tag{9}
\]

Exact boundary merge requires this derivative to be `-W_ij/sqrt(d)`.
Consequently it forces

\[
W_{ij}=m_0\sqrt d+
\frac{m_0m'_0}{\sqrt d}
\sum_{\substack{q>i\\q\ne j}}W_{jq}.
\tag{10}
\]

Processing first endpoints downward makes (10) a triangular system with a
unique solution.  Thus arbitrary deterministic triangular weights do not
give an optimization parameter inside the exact-merge invariant.

The same conclusion survives a uniform potential scale `kappa>0`.  If the
quadratic potential uses `kappa T`, then the joint function contains
`-(kappa/d) sum T m m`, and exact merge forces

\[
\frac{\kappa T_{ij}}{\sqrt d}
=m_0+\frac{\kappa m_0m'_0}{d}
 \sum_{\substack{q>i\\q\ne j}}T_{jq}.
\]

The effective coefficient `W_ij=kappa T_ij` again obeys (10).  Edge-dependent
scales merely rename the effective coefficients and give the same equation.

Finally, the feedback operator in (10) has row norm at most
`rho=m_0m'_0/D=o(1)`.  The predecessor's lower and upper weight bounds show
that its accumulated increment is the first-order mass

\[
2A_0\binom r4\,[1+O(\rho)].
\tag{11}
\]

Since the centered net coefficient is `m_0^2[1+o(1)]`, neither exact
evaluation of the feedback nor potential rescaling can change the leading
`1/(96 log C)`.  They can change only lower-order terms.

## 2. Controlled recursion and the residual gradient

The extra freedom appears only if the quadratic part of the tangent estimate
is retained.  For a target ordered set `[r]`, set

\[
t_0=m_0\sqrt d,\qquad
\gamma_d=\frac{m_0m'_0}{\sqrt d},\qquad
e_{ij}=\theta(i-1),
\tag{12}
\]

and, in decreasing order of the first endpoint, define

\[
\boxed{
T_{ij}=t_0+\gamma_d
\sum_{\substack{q>i\\q\ne j}}T_{jq}+e_{ij}.}
\tag{13}
\]

This is deterministic and adapted for exactly the same reason as the
predecessor recursion.  Write `Delta_ij=T_ij-t_0`.  With `F_i` as in (8), now
using `T`, equation (9) becomes the exact residual identity

\[
\partial_jF_i(c\mathbf1)
=-\frac{T_{ij}-e_{ij}}{\sqrt d}.
\tag{14}
\]

Thus the control has not been hidden in a history-dependent error: it is a
fixed, explicitly paid failure of exact gradient merge.

## 3. Hessian and the second-order square completion

The predecessor Hessian formula is unchanged.  The controlled recursion gives

\[
T_{\max}\le\frac{t_0+\theta r}{1-\rho},
\qquad
\frac1d\max_j\sum_{q\ne j}T_{jq}
\le\frac{m_0+\theta/D}{D(1-\rho)}.
\tag{15}
\]

The diagonal of `-nabla^2 F_i` is at least `j_-(w)` and its off-diagonal
row sum is at most the second term in (2).  Hence, when `mu_w>0`,

\[
-\nabla^2F_i(b)\succeq\mu_w I
\quad\hbox{throughout }[c-w,c+w]^{V_i}.
\tag{16}
\]

Let

\[
\delta_j=b_j-c=\sqrt d\,h_{ij}+\varepsilon_{ij},
\qquad |\varepsilon_{ij}|\le d^{-1/5}.
\]

Strong concavity, (14), and

\[
\frac{e_{ij}\delta_j}{\sqrt d}
-\frac{\mu_w\delta_j^2}{2}
\le\frac{e_{ij}^2}{2\mu_wd}
\tag{17}
\]

give the pathwise merge inequality

\[
F_i(b)\le F_i(c\mathbf1)
-\sum_{j>i}T_{ij}h_{ij}
+\sum_{j>i}\frac{e_{ij}^2}{2\mu_wd}
+\frac{d^{-1/5}}{\sqrt d}\sum_{j>i}T_{ij}.
\tag{18}
\]

Equation (18) is the missing second-order step.  The full `T` boundary merges
into the projection potential, while every residual is paid deterministically.

## 4. Deterministic weights and accumulated mass

For a future edge `j<q`, (13) and (15) yield

\[
A_0(r-j-1)+\theta(j-1)
\le\Delta_{jq}
\le
\frac{A_0+\rho\theta}{1-\rho}(r-j-1)+\theta(j-1).
\tag{19}
\]

The two counts in (19) sum to `r-2`; hence

\[
a_-(r-2)\le\Delta_{jq}\le a_+(r-2).
\tag{20}
\]

For a future set of size `k`, let

\[
S_i=\sum_{\{j,q\}\subset V_i}\Delta_{jq},\qquad
R_i=\max_{j\in V_i}\sum_{q\ne j}\Delta_{jq}.
\]

For `k>=2`, (20) gives

\[
S_i\ge a_-(r-2)\binom k2,
\quad
R_i\le a_+(r-2)(k-1),
\quad
\frac{R_i}{S_i}\le\frac{2a_+}{a_-k},
\quad
\frac{R_i}{d}\le\frac{a_+}{D^2}.
\tag{21}
\]

The sharper first inequality in (19), summed with the correct exposure
multiplicity, gives

\[
\sum_{i=1}^{r-1}S_i
\ge2A_0\binom r4+\theta K_r,
\qquad
K_r:=\sum_{i=1}^{r-1}(r-i)(i-1)^2
=\binom r3+2\binom r4.
\tag{22}
\]

The square-completion penalty has the matching exact identity

\[
\sum_{1\le i<j\le r}e_{ij}^2=\theta^2K_r.
\tag{23}
\]

Both the factor two in the old feedback mass and the new `K_r` multiplicity
are therefore explicit rather than asymptotic guesses.

## 5. Three-factor Holder and the new centered cost

Keep the predecessor decomposition `T=t_0+Delta`, the same three conjugate
exponents

\[
Q_0=\frac d{4t_0k},\qquad
Q_1=\frac d{4R_i},\qquad
P^{-1}=1-Q_0^{-1}-Q_1^{-1},
\]

and the same exact one-sided CGF.  By (21), all factors are legal whenever

\[
\frac{4m_0}{D}+\frac{4a_+}{D^2}<\frac12.
\tag{24}
\]

The weighted quadratic factor still costs exactly at most

\[
\frac{16}{3}\frac{S_i}{d}.
\tag{25}
\]

For completeness, the three linear-CGF comparison terms are bounded by

\[
2\sum_j u_j^0\delta u_j
\le\frac{4m_0M_w^2}{D}\frac{S_i}{d},
\]

\[
\sum_j(\delta u_j)^2
\le\frac{2M_w^2a_+}{D^2}\frac{S_i}{d},
\]

\[
\frac{16R_i}{d}\sum_j(u_j^0)^2
\le\frac{32m_0^2M_w^2a_+}{a_-D^2}\frac{S_i}{d}.
\tag{26}
\]

Here the last line uses `R_i/S_i<=2a_+/(a_-k)` and `k^2/d<=D^{-2}`.
Their sum is exactly (3).  Thus the central deterministic increment
`-m_0^2 S_i/d`, the weighted-square cost (25), and every new linear cost
(26) leave

\[
-\widehat B_w(C)\frac{S_i}{d}.
\tag{27}
\]

### No double count with `G_*(C)`

The old history-uniform exact-CGF deficit
`mathsf d_{k,w,d}(P^*_{k,d})` is retained once, unchanged.  It compares the
uniform `t_0` centered-linear term with the exact pre-Cauchy HMS allocation.
Equations (25)--(27) pay only the new `Delta` factor and the change from the
old Holder exponent to the three-factor exponent.  Equation (18) separately
pays the gradient residual.  Therefore no part of the old `G_*`, the new
central mean, or the residual penalty is used twice.

## 6. Reverse induction

Use the same nonexchangeable weighted projection potential as the predecessor,
with the controlled array (13).  At exposure step `i`, append to the frozen
one-step exponent

\[
-\mathsf d_{k,w,d}(P^*_{k,d})
-\widehat B_w(C)\frac{S_i}{d}
+\sum_{j>i}\frac{e_{ij}^2}{2\mu_wd}
+\frac{d^{-1/5}}{\sqrt d}\sum_{j>i}T_{ij}.
\tag{28}
\]

The projection identity retains every future edge; (18) supplies every
missing boundary edge with its full coefficient `T_ij`.  All coefficients in
(28) are fixed before the column is sampled.  A one-step deterministic charge
need not have a favorable sign: reverse induction multiplies by its exact
deterministic exponential, and only the accumulated sign is used.

At the empty state, (22)--(23) give

\[
P^*_{R,r}\le\mathcal H_C(r)
\exp\left[-\mathcal D_{C,w,d}(r)
-\frac1d\left{
2\widehat B_wA_0\binom r4+E_wK_r\right}
+J_{r,d}\right],
\tag{29}
\]

where the predecessor source envelope and old optimized deficit are unchanged,
and

\[
0\le J_{r,d}\le
\frac{m_0+\theta/D}{1-\rho}\,d^{-1/5}\binom r2
=o_C(r^2).
\tag{30}
\]

This checks the complete reverse-induction ledger, including the residual.

## 7. Perfect-sequence extraction

For every retained ordered set of size `q`, relabel it in retained order and
rebuild (13) with `r=q`.  Then `q/sqrt(d)<=1/D`, so (15), (16), and (24) only
improve, and `J_{q,d}<=J_{ell,d}`.

If `u` vertices are deleted, the extra deficit restored at size `ell` is at
most

\[
\begin{aligned}
\frac1d\bigg[&2\widehat B_wA_0\,u\binom\ell3\\
&+E_w\left(u\binom\ell2+2u\binom\ell3\right)\bigg]\\
&\le\left[
\frac{\widehat B_wA_0+E_w}{3D^2}+o_C(1)
\right]\ell u.
\end{aligned}
\tag{31}
\]

The bracket is `O(1/log C)<1` for large `C`.  The old optimized-deficit
restoration is already paid in the frozen package, while the unchanged
projection-failure factor `(p/10)^(10 ell u)` dominates (31), the missing-edge
and cubic charges, and (30).  The same subset sum is `o(1)`.  This closes the
extraction gate without changing the source argument.

## 8. Positivity, rate conversion, and asymptotics

As `C` tends to infinity and then `w` decreases to `omega_0`, the pinned
source asymptotics give

\[
\rho=o(1),\quad m'_0\to1,\quad M_w/m_0\to1,
\quad j_\pm(w)\to1,
\]

\[
\mu_w\to1,\qquad
\widehat L_w=o(m_0^2),\qquad
\widehat B_w=m_0^2[1+o(1)].
\tag{32}
\]

Thus (16), (24), `widehat B_w>0`, and `E_w>0` all hold for sufficiently
large fixed `C`.  Since `K_ell/ell^4 -> 1/12`, (29) contributes exactly (5)
to the Ramsey rate.  Finally,

\[
m_0^2=(2+o(1))\log C,qquad
D^2=(32+o(1))(\log C)^3,
\]

so

\[
\widehat B_wA_0=(4+o(1))(\log C)^2,
\quad
E_w=(2+o(1))(\log C)^2,
\]

and therefore

\[
\widehat H_*(C)
=\frac{(6+o(1))(\log C)^2}
       {12(32+o(1))(\log C)^3}
=\frac{1+o(1)}{64\log C}.
\tag{33}
\]

The predecessor has `H_*(C)=(1+o(1))/(96 log C)`, proving the eventual
strict inequality in (7).  Also `G_*+widehat H_*=O(1/log C)=o(1)`, so the
frozen red/blue crossing remains unchanged.

## 9. A narrow method cap

The result also identifies the limit of the following explicitly admissible
completion class.  Its residual arrays are deterministic and fixed before
each column is sampled; they use the same weighted-pair recursion, have
nonnegative increments (as required by the weighted quadratic reduction),
and obey the same scalar full-box strong-concavity and three-factor
H\"older/CGF feasibility bounds used above.  For a residual `e_ij` in this
class, its direct leading contribution after all earlier exposures is

\[
\widehat B_w(i-1)e_{ij}-\frac{e_{ij}^2}{2\mu_w}.
\tag{34}
\]

Pointwise, (34) is maximized at
`e_ij=mu_w widehat B_w(i-1)`.  Since
`mu_w widehat B_w=m_0^2[1+o(1)]`, the choice (12) is asymptotically optimal.
Feedback through (13) has norm `rho=o(1)` and changes only lower-order terms.
Hence `1/64` is the leading cap for this admissible scalar class, namely:

- the same deterministic triangular weighted-pair invariant;
- a history-independent boundary residual;
- nonnegative deterministic increments fixed before the relevant column is
  sampled;
- uniform full-box strong-concavity square completion; and
- the same three-factor Holder/CGF comparison.

This is **not** a cap on all history-dependent potentials.  Outcome-adaptive
weights, matrix-valued square completion, higher-order potentials, a sharper
source quadratic MGF, or a different extraction invariant remain outside the
statement.

## Checker boundary

Run

```text
.venv/bin/python routes/lower/history_weight_optimization_next_check.py
```

The checker independently replays the controlled recursion, residual gradient,
square completion, exact `K_r` identity, deterministic bounds, a nonconstant
full-Hessian sample, the exact CGF increment, strict finite margins at four
large values of `C`, comparison with the predecessor term, and numerical
approach to `64 log(C) widehat H=1`.  It intentionally does not certify the
source reverse induction, extraction prose, or theorem quantifiers; those are
the required scope of the pending independent source referee.
