# Independent referee report on `HISTORY_WEIGHT_OPTIMIZATION_NEXT.md`

Date: 2026-08-12  
Review posture: independent, adversarial, source-level, and proof-first

## Verdict

### Main source-relative Ramsey theorem

**PROVABLE AS STATED. PASS.**

Relative to the pinned HMS appendix bridge and optimized exact-CGF deficit,
the controlled deterministic residual closes the same red reverse induction
and gives, for every sufficiently large fixed $C$,

$$
\liminf_{\ell\to\infty}\frac1\ell
\log R\!\left(\ell,\lfloor C\ell\rfloor\right)
\ge
-\frac12\log p_C+\frac{B_R(C)}2+G_*(C)+\widehat H_*(C),
$$

where

$$
\widehat H_*(C)>H_*(C)>0
$$

eventually and

$$
\widehat H_*(C)=\frac{1+o(1)}{64\log C}.
$$

The quantifier order remains source-relative and non-effective:

$$
\exists C_0\ \forall C\ge C_0\ \exists \ell_0(C)\
\forall \ell\ge\ell_0(C).
$$

The old term $G_*(C)$ and the new term $\widehat H_*(C)$ occur in
different summands of one same-history decomposition.  They are not double
counted.

### Exact-merge uniqueness

**PROVABLE AS STATED. PASS.**  Exact gradient merge determines the effective
triangular coefficient array uniquely.  A uniform potential scale only
renames those effective coefficients, so it cannot alter the leading
$1/(96\log C)$ term inside that exact-merge invariant.

### Narrow method cap

**PROVABLE AS STATED. PASS; THE QUALIFIER CORRECTION IS RESOLVED.**  The
revised Section 9 now explicitly restricts the advertised
$1/(64\log C)$ leading cap to deterministic residual arrays that

1. use the same weighted-pair recursion;
2. keep the increments nonnegative so that the weighted quadratic reduction
   used in the proof applies;
3. obey the same full-box scalar strong-concavity and three-factor
   H\"older/CGF feasibility bounds; and
4. have deterministic, history-independent coefficients fixed before each
   column is sampled.

These are exactly the four admissibility conditions required by the initial
referee report.  The revised text also expressly excludes outcome-adaptive
weights, matrix-valued square completion, higher-order potentials, a sharper
source quadratic MGF, and different extraction invariants.  The cap's
quantified domain now matches the proof in Section 9 of this report.

There is therefore no fatal or unresolved local gap in any claim as now
stated.  Reading the cap beyond this explicitly admissible scalar class would
still be unsupported, but the corrected author package does not do so.

## Result-to-claim judgment

- `claim_supported`: **yes** for the source-relative Ramsey theorem, the
  exact-merge statement, and the narrow cap on the now explicitly admissible
  scalar residual class.
- `what_results_support`: a source-relative added exponent
  $\widehat H_*(C)\sim1/(64\log C)$ in the frozen HMS construction, for all
  sufficiently large fixed $C$.
- `what_results_dont_support`: an effective $C_0$, a finite Ramsey-number
  improvement, a new blue bound, an unconditional theorem outside the frozen
  HMS bridge, or novelty/priority/world-best status.
- `missing_evidence`: for publication, an external human proof review and an
  archival immutable copy of the two source snapshots.
- `confidence`: **high** on all claims within their stated scope.

## Frozen materials and source integrity

The reviewed author artifacts reproduce their declared hashes:

- `HISTORY_WEIGHT_OPTIMIZATION_NEXT.md`, SHA-256
  `2234a769d7798a79174cbfb362ada64f5d760aefbe7e6d4fb8763cd5633a0312`;
- `history_weight_optimization_next_check.py`, SHA-256
  `616040b91aad4becf92dcfbe13b7e6d49a3c9c73f0f222ba56114104f1c7d554`.

The initially reviewed author snapshot had SHA-256
`6c22c7729546421f6578b1374f1216fcda5e300d9250541a5732e0cf3f4e2e4d`.
The current snapshot supersedes it by resolving only the method-cap
admissibility qualifier identified in the initial verdict; no theorem,
formula, or numerical constant is changed.

The pinned predecessor artifacts also reproduce their hashes:

- `HISTORY_DEPENDENT_LEDGER_ATTEMPT.md`, SHA-256
  `29c55690fbf37b884640ec2be3fc3d746ce810add6793ce7c014e06d08f23329`;
- `INDEPENDENT_HISTORY_DEPENDENT_LEDGER_REFEREE.md`, SHA-256
  `a858849824862ca1ab07dc1a9682275a19a0af811c45a7e60f28a4579a474dd4`;
- `LOWER_HMS_PARAMETER_OPTIMIZATION.md`, SHA-256
  `32f22f107352b38549053794fef10fe3db853b5eee952a212c6ea058bc18bab1`;
- `HMS_APPENDIX_BRIDGE.md`, SHA-256
  `8d38003528d53d62589eb6ab0e960e29a494788bfe74bf23f871ee81d6732944`.

I independently downloaded the cited arXiv v2 source archives.  Their main
TeX files reproduce the source hashes used by the predecessor referee:

- Hunter--Milojevi\'c--Sudakov, arXiv:2512.17718v2,
  `arXiv_version.tex`, SHA-256
  `b72958ac35554eccb94dedab5800349d2c021af7d60f767125cb46998e0fd54a`;
- Lin--Niu, arXiv:2605.25843v2,
  `off-diagonal-Ramsey-R.tex`, SHA-256
  `dbf1bfa2c7603c81b2e56a97028b138ccf9a9299a3d1f20c0b08cf489136f429`.

The relevant source dependencies remain:

1. HMS lines 895--935: the pre-Cauchy centered-moment decomposition and
   centered quadratic square-MGF estimate;
2. HMS lines 963--971 and 1202--1208: red-perfectness and the cutoff
   approximation;
3. HMS lines 1192--1289: the reverse-induction skeleton and conditional
   independence after exposing one column;
4. HMS lines 1294--1361: the unchanged red/blue first-moment extraction;
5. Lin--Niu lines 359--493: monotonicity of truncated variance; and
6. Lin--Niu lines 499--537: the exact positive-direction centered CGF.

## Dependency map for the new proof

1. The deterministic recursion gives the residual gradient identity.
2. The full-box Hessian bound supplies one scalar strong-concavity constant
   $\mu_w>0$.
3. Strong concavity and square completion turn the residual gradient into a
   deterministic $e_{ij}^2/(2\mu_wd)$ charge.
4. Three-factor H\"older pays the uniform quadratic factor, the increment
   quadratic factor, and the changed linear CGF exactly once.
5. The deterministic mass identities sum the central increment and residual
   penalty over all exposure steps.
6. The weighted projection identity merges all future and boundary edges in
   the reverse induction.
7. The HMS greedy extraction absorbs the loss caused by deleted vertices.
8. The first-moment conversion turns the accumulated fourth-order mass into
   the displayed Ramsey-rate term.

## 1. Controlled recursion, gradient, and Hessian

Write

$$
t_0=m_0\sqrt d,\qquad
\gamma_d=\frac{m_0m'_0}{\sqrt d},\qquad
e_{ij}=\theta(i-1),\qquad \theta=m_0^2,
$$

and define

$$
T_{ij}=t_0+\gamma_d
\sum_{\substack{q>i\\q\ne j}}T_{jq}+e_{ij}.
\tag{R1}
$$

Every edge on the right of (R1) has smaller endpoint greater than $i$, so
the array is well defined by decreasing first endpoint and is deterministic
before the relevant column is sampled.

For

$$
F_i(b)=\sum_{j>i}\log\Phi(-b_j)
-\frac1d\sum_{i<j<q}T_{jq}m(b_j)m(b_q),
$$

direct differentiation gives

$$
\partial_jF_i(c\mathbf1)
=-m_0-\frac{m_0m'_0}{d}
\sum_{\substack{q>i\\q\ne j}}T_{jq}
=-\frac{T_{ij}-e_{ij}}{\sqrt d}.
\tag{R2}
$$

This is an exact identity; the control is not hidden in a source error.

The maximum-weight estimate is also directionally correct:

$$
T_{\max}\le
\frac{t_0+\theta r}{1-\rho},
\qquad
\rho=\frac{m_0m'_0}{D}.
$$

It implies

$$
\frac1d\max_j\sum_{q\ne j}T_{jq}
\le
\frac{m_0+\theta/D}{D(1-\rho)}.
$$

Lin--Niu's variance monotonicity has the correct orientation here:
$m''(b)\ge0$.  Hence the extra diagonal part of $-\nabla^2F_i$ is
nonnegative, while the off-diagonal absolute row sum is at most

$$
j_+(w)^2\frac{m_0+\theta/D}{D(1-\rho)}.
$$

Gershgorin therefore proves

$$
-\nabla^2F_i(b)\succeq\mu_wI
$$

on the entire cutoff box, not just on the sampled checker points.

## 2. Residual square completion and discretization

This is the first genuinely new step, and its signs are correct.
Let

$$
\delta_j=b_j-c=\sqrt d\,h_{ij}+\varepsilon_{ij},
\qquad |\varepsilon_{ij}|\le d^{-1/5}.
$$

Strong concavity and (R2) give

$$
F_i(b)\le F_i(c\mathbf1)
-\sum_{j>i}\frac{T_{ij}-e_{ij}}{\sqrt d}\delta_j
-\frac{\mu_w}{2}\sum_{j>i}\delta_j^2.
\tag{R3}
$$

For each coordinate,

$$
-\frac{T-e}{\sqrt d}\delta
=-Th-\frac{T}{\sqrt d}\varepsilon
+\frac e{\sqrt d}\delta.
\tag{R4}
$$

The last term in (R4) is paid using

$$
\frac{e\delta}{\sqrt d}-\frac{\mu_w\delta^2}{2}
\le\frac{e^2}{2\mu_wd},
\tag{R5}
$$

and the middle term is at most $Td^{-1/5}/\sqrt d$.  Thus

$$
F_i(b)\le F_i(c\mathbf1)-\sum_{j>i}T_{ij}h_{ij}
+\sum_{j>i}\frac{e_{ij}^2}{2\mu_wd}
+\frac{d^{-1/5}}{\sqrt d}\sum_{j>i}T_{ij}.
\tag{R6}
$$

No $e\varepsilon$ term is missing: it is already part of
$e\delta/\sqrt d$ in (R5).  Equation (R6) supplies the full coefficient
$T_{ij}$ needed by the projection invariant and pays every residual
deterministically.

The resulting discretization sum is bounded by

$$
0\le J_{r,d}\le
\frac{m_0+\theta/D}{1-\rho}\,d^{-1/5}\binom r2
=o_C(r^2).
$$

For extraction it is safest to interpret $J_{r,d}$ as this deterministic
upper envelope.  Under that convention $J_{q,d}\le J_{\ell,d}$ is literal.
If $J_{r,d}$ instead denotes the uncoarsened signed sum, only its displayed
upper envelope is needed; the conclusion is unchanged.

## 3. Deterministic weights and exact multiplicities

For $j<q$, recurrence (R1) contains exactly $r-j-1$ future incident
weights.  Therefore

$$
A_0(r-j-1)+\theta(j-1)
\le\Delta_{jq}
\le
\frac{A_0+\rho\theta}{1-\rho}(r-j-1)+\theta(j-1),
$$

where $A_0=m_0^2m'_0$.  Since the two counts sum to $r-2$, the bounds using
$a_-$ and $a_+$ follow.

The two critical accumulated identities are also correct.  The direct
feedback part satisfies

$$
\sum_{j=1}^{r-1}(j-1)(r-j)(r-j-1)=2\binom r4,
\tag{R7}
$$

and the residual multiplicity is

$$
K_r:=\sum_{i=1}^{r-1}(r-i)(i-1)^2
=\binom r3+2\binom r4.
\tag{R8}
$$

An edge residual $e_{jq}=\theta(j-1)$ appears in every $S_i$ with $i<j$,
so it receives exactly the second factor $j-1$.  Thus

$$
\sum_iS_i\ge2A_0\binom r4+\theta K_r.
$$

At exposure step $i$ there are exactly $r-i$ boundary residuals equal to
$\theta(i-1)$, giving independently

$$
\sum_{i<j}e_{ij}^2=\theta^2K_r.
$$

The same $K_r$ in these two places is therefore structural, not a fitted
coincidence.

## 4. Three-factor H\"older and centered costs

Conditioned on the red boundary edges, write $X_j=\mu_j+\xi_j$.  The exact
weighted exponent separates into

1. its deterministic mean;
2. the centered linear factor;
3. the uniform centered quadratic factor with coefficient $t_0$; and
4. the increment centered quadratic factor with coefficients $\Delta$.

Choose

$$
Q_0=\frac d{4t_0k},\qquad
Q_1=\frac d{4R_i},\qquad
P^{-1}=1-Q_0^{-1}-Q_1^{-1}.
$$

The condition

$$
\frac{4m_0}{D}+\frac{4a_+}{D^2}<\frac12
$$

makes all three exponents legal and gives $1<P\le2$.

The uniform quadratic factor costs $4t_0k/d$, exactly as in HMS.  For the
increment factor,

$$
-\sum_{j<q}\Delta_{jq}\xi_j\xi_q
\le\frac12\sum_jR_j\xi_j^2.
$$

Since $Q_1R_j/(2d)\le1/8$, the HMS square-MGF lemma gives, after taking the
$Q_1$-th root,

$$
\frac{16}{3}\frac{S_i}{d},
$$

using $\sum_jR_j=2S_i$.  The factor $16/3$ is correct.

For the linear factor, $K_b''(u)=v(b+u)\in[0,1]$ in the needed positive
direction.  Consequently

$$
\frac{K_b(P(u+\delta))-K_b(Pu)}P\le2u\delta+\delta^2
$$

and

$$
0\le\frac{\partial}{\partial P}\frac{K_b(Pu)}P\le u^2.
$$

The three deterministic comparison terms are, in order,

$$
\frac{4m_0M_w^2}{D}\frac{S_i}{d},\qquad
\frac{2M_w^2a_+}{D^2}\frac{S_i}{d},\qquad
\frac{32m_0^2M_w^2a_+}{a_-D^2}\frac{S_i}{d}.
$$

Their sum is $\widehat L_w(C)S_i/d$.  Thus the central deterministic
increment $-m_0^2S_i/d$ leaves exactly

$$
-\widehat B_w(C)\frac{S_i}{d},
\qquad
\widehat B_w=m_0^2-\frac{16}{3}-\widehat L_w.
\tag{R9}
$$

## 5. Why $G_*(C)$ is not counted twice

Let $\mathcal U_i$ be the old HMS pre-Cauchy centered allocation and let
$\mathcal C_i^{\rm old}$ be the already optimized exact-CGF centered
envelope.  On the same cutoff history,

$$
\mathsf d_i=\mathcal U_i-\mathcal C_i^{\rm old}.
\tag{R10}
$$

The new H\"older comparison starts from
$\mathcal C_i^{\rm old}$ and pays only

- the change from the old linear exponent $P_0$ to $P$;
- the added linear coefficients $\delta u$; and
- the added increment quadratic factor.

Combining (R6), (R9), and (R10) gives the one-step ledger

$$
\begin{aligned}
E_i^{\rm new}\le{}&
\bigl[k\log p-A_0^{\rm HMS}+\mathcal U_i\bigr]
-\sum_{j>i}T_{ij}h_{ij}
-\mathsf d_i
-\widehat B_w\frac{S_i}{d}\\
&+\sum_{j>i}\frac{e_{ij}^2}{2\mu_wd}
+\frac{d^{-1/5}}{\sqrt d}\sum_{j>i}T_{ij},
\end{aligned}
\tag{R11}
$$

where $A_0^{\rm HMS}=m_0^3\binom{k}{2}/\sqrt d$ is the unchanged central
HMS mean term.  In (R11):

- $-\mathsf d_i$ is exactly the old source-relative $G_*$ saving;
- $-\widehat B_wS_i/d$ is the new deterministic-increment saving; and
- $e_{ij}^2/(2\mu_wd)$ pays the residual gradient.

These are disjoint summands.  The source's one-sided constant $K$ is still
sufficient because the bracket in (R11) is the same frozen HMS bracket:
the joint concavity argument replaces the history-perturbed deterministic
mean by the exact central mean and introduces no new source $O$ term.

## 6. Reverse induction

For fixed target size $r$, construct the full triangular array before any
column exposure.  At state $s$, retain the nonexchangeable weighted
projection potential on future edges.  In the step from $s=i$ to $s=i-1$:

1. the new-coordinate part of the future projection potential produces the
   weighted quadratic form $-Q_T$;
2. (R6) supplies every boundary edge $(i,j)$ with its full coefficient
   $T_{ij}$;
3. the previous-coordinate projection retains every future edge; and
4. (R11) appends exactly one old deficit, one new central charge, one
   residual penalty, and one discretization charge.

The weights need not be exchangeable; determinism and measurability before
sampling the column are sufficient.  At the empty state, (R7)--(R8) give

$$
P^*_{R,r}\le\mathcal H_C(r)
\exp\left[
-\mathcal D_{C,w,d}(r)
-\frac1d\left{
2\widehat B_wA_0\binom r4+E_wK_r
\right}+J_{r,d}\right],
$$

where

$$
E_w=\widehat B_w\theta-\frac{\theta^2}{2\mu_w}.
$$

The sign is correct even though an individual residual charge can be
positive: reverse induction multiplies by its deterministic exponential,
and only the accumulated coefficient $E_w>0$ is used at the end.

## 7. Perfect-sequence extraction

For a retained set of size $q\le\ell$, rebuilding the deterministic array
in retained order is legitimate because the weights are proof coefficients,
not part of the random graph.  Since $q/\sqrt d\le1/D$, all feasibility
bounds only improve.

If $u=\ell-q$ vertices are deleted, then

$$
\binom\ell4-\binom{\ell-u}4\le u\binom\ell3,
\qquad
\binom\ell3-\binom{\ell-u}3\le u\binom\ell2.
$$

Using $K_r=\binom r3+2\binom r4$, the new restoration charge is at most

$$
\left[
\frac{\widehat B_wA_0+E_w}{3D^2}+o_C(1)
\right]\ell u.
$$

This coefficient is $O(1/\log C)<1$ eventually.  The frozen extraction
already pays the old optimized-deficit loss, and the unchanged projection
failure factor

$$
\left(\frac p{10}\right)^{10\ell u}
$$

strictly dominates the missing-edge, cubic, old-deficit, new-deficit, and
discretization charges.  Hence the same binomial subset sum is $o(1)$.

## 8. Rate coefficient and asymptotics

Because $K_\ell/\ell^4\to1/12$, the new clique-probability exponent
contributes

$$
\widehat H(C,w)
=\frac{\widehat B_wA_0+E_w}{12D^2}
$$

to the Ramsey rate.  As $C\to\infty$ and then
$w\downarrow\omega_0$,

$$
m_0^2=(2+o(1))\log C,\qquad
D^2=(32+o(1))(\log C)^3,
$$

$$
\mu_w\to1,\qquad
\widehat B_w=m_0^2[1+o(1)],\qquad
A_0=m_0^2[1+o(1)].
$$

Therefore

$$
\widehat B_wA_0=(4+o(1))(\log C)^2
$$

and

$$
E_w
=\widehat B_wm_0^2-\frac{m_0^4}{2\mu_w}
=(2+o(1))(\log C)^2.
$$

It follows that

$$
\widehat H_*(C)
=\frac{(6+o(1))(\log C)^2}
{12(32+o(1))(\log C)^3}
=\frac{1+o(1)}{64\log C}.
$$

The predecessor term is $H_*(C)=(1+o(1))/(96\log C)$, so the strict
eventual comparison follows.  Also
$G_*(C)+\widehat H_*(C)=o(1)$, leaving the unchanged blue constraint above
the strengthened red constraint.

## 9. Quantified version of the narrow cap

The cap can be made rigorous under the admissibility qualifier in the
verdict.  A residual $e_{ij}$ occurs directly in the central increment at
each of the $i-1$ earlier exposure steps, while its square-completion penalty
occurs once at step $i$.  Ignoring feedback, its contribution is bounded by

$$
\widehat B_w(i-1)e_{ij}-\frac{e_{ij}^2}{2\mu_w}
\le
\frac{\mu_w\widehat B_w^2}{2}(i-1)^2.
\tag{R12}
$$

Equality in (R12) is attained at
$e_{ij}=\mu_w\widehat B_w(i-1)$.  Since

$$
\mu_w\widehat B_w=m_0^2[1+o(1)],
$$

the author's choice $e_{ij}=m_0^2(i-1)$ is asymptotically optimal.

For any admissible array in the same comparison, centered costs are
nonnegative, so its usable central coefficient is at most
$m_0^2[1+o(1)]$.  The same H\"older feasibility bound gives
$d^{-1}\max_j\sum_qT_{jq}=O(1)$, while the uniform Mills asymptotics on the
shrinking cutoff box give $m'(b)\le1$ and $m(b)m''(b)=o(1)$.  Hence every
diagonal entry of $-\nabla^2F_i$ is at most $1+o(1)$; since the least
eigenvalue is no larger than the least diagonal entry, any usable uniform
scalar strong-concavity constant is at most $1+o(1)$.  The residual-free
feedback therefore contributes at most the old leading numerator $m_0^4$,
and (R12) contributes at most an additional $m_0^4/2$.  The feedback
operator has norm
$\rho=o(1)$, so propagating a residual changes these quantities only by a
$1+o(1)$ factor.  Hence the total leading numerator is at most
$3m_0^4/2$, which gives

$$
\frac{3m_0^4/2}{12D^2}
=\frac{1+o(1)}{64\log C}.
$$

This proves the cap for the explicitly admissible scalar method class.  It
does not quantify over richer induction states.

## 10. Arithmetic replay and evidentiary boundary

The frozen checker was rerun afresh against the corrected author snapshot and
runs successfully.  It reports strict positive margins
at $C=10^{12},10^{20},10^{40},10^{80}$, verifies the controlled recursion,
the residual identity, the $K_r$ combinatorics, a nonconstant Hessian sample,
the exact CGF increment, and numerical convergence of
$64\log(C)\widehat H$ toward one.

I also independently checked the integer identities (R7)--(R8) for
$2\le r\le19$.

These computations are corroboration only.  They do not prove full-box
concavity, the source ledger, reverse induction, extraction, or theorem
quantifiers.  The PASS verdict rests on the analytic reconstruction above.

## Final scope warning

This report validates a theorem relative to the pinned source bridge.  It
does not turn the local package into a published theorem, establish priority,
or certify a finite value of $C_0$.  Any later canonical promotion should
retain the source-relative and non-effective labels and preserve the four
admissibility conditions now present in Section 9 verbatim in substance.
