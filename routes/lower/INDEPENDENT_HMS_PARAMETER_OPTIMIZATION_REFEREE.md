# Independent referee report on `LOWER_HMS_PARAMETER_OPTIMIZATION.md`

Date: 2026-08-12  
Review posture: source-level, adversarial, and independent of the author
checker

## Verdicts

### Strict fixed-$C$ theorem

**PROVABLE AS STATED, source-relative.  PASS.**

For every sufficiently large fixed $C$, the proof supports

$$
\liminf_{\ell\to\infty}\frac1\ell
\log R\!\left(\ell,\lfloor C\ell\rfloor\right)
\ge -\frac12\log p_C+\frac{B_R(C)}2+G_*(C),
$$

and its public-constant consequence with $B_R(C)/2$ replaced by $1/20$.
It also supports the strict comparison

$$
G_*(C)>\frac{c_R(C)}{4D^2}.
$$

The quantifiers remain existential and non-effective:

$$
\exists C_0\ \forall C\ge C_0\ \exists\ell_0(C)\
\forall\ell\ge\ell_0(C).
$$

No numerical value of $C_0$ follows because the frozen HMS appendix ledger
contains unspecified absolute constants.

### Method-optimality theorem

**PROVABLE WITH THE STATED NARROW SCOPE.  PASS WITH SCOPE WARNING.**

The leading cap

$$
\limsup_{\ell\to\infty}\frac1{\ell^2}
\sum_{k<\ell}\delta_{C,k,d}
\le \frac{m_0^4}{4D^2}
=\frac{1+o(1)}{32\log C}
$$

is valid for a deterministic, history-uniform, additive per-group saving
relative to the frozen centered-moment envelope (20).  Since $G_*(C)$ is
asymptotic to this cap, $1/32$ cannot be doubled by changing only the
Hölder split, the one-sided centered CGF bound, or the rectangular cutoff
window inside that class.

This does **not** cap a history-dependent saving retained in an enlarged
induction state, an averaged/coupled saving, a change to the deterministic
mean or connection ledger, a different dimension choice, a new blue
estimate, or a different random graph model.  The proof document states
these exclusions, and the method-optimality verdict depends on preserving
them.

The earliest fatal gap is therefore **none in either stated claim**.  The
earliest point at which a stronger interpretation fails is Claim B's
uniform-additive hypothesis: Jensen on one central history cannot rule out a
history-dependent quantity that is averaged only after later exposures.

## Materials and source integrity

I checked the following local artifacts:

- `LOWER_HMS_PARAMETER_OPTIMIZATION.md`, SHA-256
  `32f22f107352b38549053794fef10fe3db853b5eee952a212c6ea058bc18bab1`;
- `hms_parameter_optimization_check.py`, SHA-256
  `36e1f7a7a5cf2a0386677a921c4472a028ba66e1b76a3263efc22eb37113606a`;
- the already frozen and independently reviewed
  `HMS_APPENDIX_BRIDGE.md`, SHA-256
  `8d38003528d53d62589eb6ab0e960e29a494788bfe74bf23f871ee81d6732944`.

The two cited source snapshots exist locally and reproduce the hashes in the
proof document:

- Hunter--Milojević--Sudakov, `arXiv_version.tex`, arXiv:2512.17718v2,
  SHA-256
  `b72958ac35554eccb94dedab5800349d2c021af7d60f767125cb46998e0fd54a`;
- Lin--Niu, `off-diagonal-Ramsey-R.tex`, arXiv:2605.25843v2, SHA-256
  `dbf1bfa2c7603c81b2e56a97028b138ccf9a9299a3d1f20c0b08cf489136f429`.

All source-line references below refer to these exact snapshots.

## Dependency map

1. The exact CGF identity uses Lin--Niu lines 499--537 after translating
   their cutoff $t$ to the proof document's parameter $t=-b$.
2. The same-history comparison uses the pre-Cauchy decomposition inside HMS
   lines 895--935, not only the coarsened statement of HMS Lemma 2.6.
3. Hölder feasibility uses HMS Lemma 2.6 with $Q_k\lambda$ and hence requires
   $d\ge4Q_k|\lambda|k$.
4. The pathwise group saving must be deterministic in $k,d,C,w$ before it is
   inserted into the reverse induction at HMS lines 1192--1289.
5. Passage from perfect to unconditional clique probabilities uses the same
   deletion accounting already audited in `HMS_APPENDIX_BRIDGE.md`.
6. The Ramsey rate uses the unchanged HMS blue probability and the frozen
   red/blue first-moment comparison at HMS lines 1294--1361.
7. The method cap uses only the central admissible history, Jensen's
   inequality, and the requirement that the saving be uniform over all
   admissible histories.

## Detailed checks

### 1. Exact upper-truncated CGF and its orientation: PASS

For $Z\le-b$, let

$$
m(b)=\frac{\phi(b)}{\Phi(-b)},\qquad
Y_b=Z+m(b).
$$

Direct integration gives

$$
K_b(u)=\log\mathbb E e^{uY_b}
=\frac{u^2}{2}+um(b)+\log\Phi(-b-u)-\log\Phi(-b).
$$

Differentiating in the proof document's $b$-parameter gives

$$
K_b'(u)=u+m(b)-m(b+u),
$$

and, since

$$
m'(q)=m(q)^2-qm(q),\qquad
v(q)=1+qm(q)-m(q)^2=1-m'(q),
$$

one obtains

$$
\boxed{K_b''(u)=v(b+u)}.
$$

This is the potentially confusing sign.  Lin--Niu parameterize an upper
cutoff by $t$, for which their formula is $K''(u)=V(t-u)$.  Substituting
$t=-b$ gives $V(-b-u)=v(b+u)$, exactly as used in the proof document.

The twice-integrated identity is consequently

$$
K_b(u)=\int_0^u(u-s)v(b+s)\,ds,
\qquad
\psi_b(u)=\int_0^1(1-t)v(b+ut)\,dt.
$$

Lin--Niu lines 360--493 show that variance increases with their upper cutoff
$t$; hence $v(b)=V(-b)$ decreases with $b$.  The normal CDF is strictly
log-concave on every finite interval, so this monotonicity is strict at
finite parameters.  Therefore $\psi_b(u)$ is decreasing in both $b$ and
$u$, and for $u>0$,

$$
0<\psi_b(u)<\frac{v(b)}2.
$$

The CGF direction and the strict inequality used later are correct.

### 2. Hölder scaling, the $1/P_k$ factor, and feasibility: PASS

For a fixed HMS history, write

$$
X_i=\mu_i+\xi_i,\qquad
A_i=\sum_{j\ne i}\mu_j,
$$

so that the random centered part is

$$
\sum_iA_i\xi_i+\sum_{i<j}\xi_i\xi_j.
$$

Hölder with conjugate exponents $P_k,Q_k$ gives

$$
\log\mathbb E e^{\lambda S}
\le \lambda\mathbb ES
+\frac1{P_k}\log\mathbb E
e^{P_k\lambda\sum_iA_i\xi_i}
+\frac1{Q_k}\log\mathbb E
e^{Q_k\lambda\sum_{i<j}\xi_i\xi_j}.
$$

Since $\sqrt d\,\xi_i$ has CGF $K_{b_i}$ and the centered variables remain
independent after the product truncation, the linear factor is exactly

$$
\frac1{P_k}\sum_i
K_{b_i}\!\left(\frac{P_k\lambda A_i}{\sqrt d}\right).
$$

There is neither a missing factor $P_k$ nor a missing $\sqrt d$.  Here
$\lambda=-m_0\sqrt d$ and $A_i<0$, so the argument is positive and the
one-sided Lin--Niu identity applies.

Applying HMS Lemma 2.6 to the centered quadratic factor with tilt
$Q_k\lambda$ is legal precisely when

$$
d\ge4Q_k|\lambda|k
\quad\Longleftrightarrow\quad
Q_k\le\frac{\sqrt d}{4m_0k}.
$$

After taking the $Q_k$-th root, its error is
$4|\lambda|k/d$, independent of $Q_k$.  Equality in the displayed
feasibility inequality is allowed by the source lemma.  Its proof still has
strict room in the square-moment denominator at this boundary.

### 3. Same-history subtraction and uniform deficit: PASS

Stopping HMS lines 895--935 before the last Cauchy coarsening gives

$$
H_s=\lambda\mathbb ES
+\frac{\lambda^2}{d}\sum_iA_i^2
+\frac{4|\lambda|k}{d}.
$$

The factor on $\sum_iA_i^2$ is one: HMS first obtains an exponent
$2\lambda^2\sum_iA_i^2/d$ for the doubled linear tilt, then the square root
from Cauchy--Schwarz halves it.

With $M_i=\sum_{j\ne i}m(b_j)$, the refined envelope and the HMS envelope
are explicit formulas for the same conditional history.  Their difference
is therefore the algebraic identity

$$
H_s-R_s
=\frac{m_0^2}{d}\sum_iM_i^2
\left[1-P_k\psi_{b_i}(u_i)\right].
$$

This is not subtraction of unrelated upper bounds: the actual log moment
satisfies

$$
\log\mathbb E e^{\lambda S}\le R_s
\le H_s-\mathsf d_{k,w,d}(P_k).
$$

On $b_i\in[c_p-w,c_p+w]$,

$$
M_i\ge(k-1)m_w,qquad
u_i\ge\frac{P_km_0m_w(k-1)}{\sqrt d},
$$

and both monotonicities of $\psi$ have the required direction.  Once
$P_kv_w<2$, the lower bracket is nonnegative, so replacing both $M_i^2$ and
the bracket by their lower bounds is legitimate.  This yields exactly the
$k(k-1)^2/d$ deficit in (27).

### 4. Optimizing $Q_k$ and the cutoff window: PASS

For fixed $b,z>0$,

$$
P\psi_b(Pz)=\frac1z\frac{K_b(Pz)}{Pz}.
$$

Convexity and $K_b(0)=0$ imply that $K_b(t)/t$ is nondecreasing, so the
display is nondecreasing in $P$.  Because $P=Q/(Q-1)$ decreases with $Q$,
the maximal legal

$$
Q_{k,d}^*=\frac{\sqrt d}{4m_0k}
$$

maximizes the certified deficit.  Its conjugate exponent is

$$
P_{k,d}^*=\frac{\sqrt d}{\sqrt d-4m_0k}.
$$

For sufficiently large $C$, $D>8m_0$ and hence these are genuine Hölder
exponents uniformly for $k\le\ell$.

Narrowing the lower cutoff from $b_w=c_p-w$ upward increases $m_w$, lowers
$\psi_{b_w}$, and raises its positive argument.  Each change improves the
deficit.  Thus the best limiting rectangular window is obtained as
$w\downarrow\omega_0$.

### 5. The $w>\omega_0$ quantifier and red-perfect induction: PASS

HMS line 1208 and red-perfectness give

$$
|b_i-c_p|\le\omega_0+d^{-1/5}.
$$

The proof document correctly does **not** replace the right side by
$\omega_0$ at finite $\ell$.  For each fixed $C$ and each fixed
$w>\omega_0$, one first chooses $\ell_0(C,w)$ so that
$d^{-1/5}<w-\omega_0$.  Then the window is a deterministic consequence of
the original red-perfect event.  No history is conditioned away and the
reverse induction is unchanged.

For each such $w$, the theorem gives one lower bound for the same number

$$
L_C:=\liminf_{\ell\to\infty}\ell^{-1}
\log R(\ell,\lfloor C\ell\rfloor).
$$

Thus $L_C\ge A_C+G(C,w)$ for every $w>\omega_0$, which implies

$$
L_C\ge A_C+\sup_{w>\omega_0}G(C,w)
=A_C+G_*(C).
$$

The dependence of $\ell_0$ on $w$ does not invalidate this argument.  There
is no interchange of one uniform finite-$\ell$ assertion with an infimum
over $w$.

### 6. Riemann-sum normalization: PASS

With $k/\ell\to x$ and $d/\ell^2\to D^2$,

$$
\mathsf d_{k,w,d}
=\ell\,\frac{m_0^2m_w^2}{D^2}x^3
\left[1-P_*(x)\psi_{b_w}
\left(\frac{P_*(x)m_0m_wx}{D}\right)\right]+o(\ell).
$$

There are $\ell+O(1)$ groups.  Dividing their sum by $\ell^2$ therefore
gives exactly the integral in (33), with no missing factors $1/2$, $1/4$,
or $D$.  Independently,

$$
\sum_{k=1}^{r-1}k(k-1)^2
=\frac{r(r-1)(r-2)(3r-5)}{12}
=\frac{r^4}{4}+O(r^3),
$$

which explains the $1/4$ in both the old companion term and the method cap.

### 7. Reverse induction and extraction: PASS

For fixed $w$, the group deficit depends only on $C,w,k,d$.  At induction
level $s$, the already accumulated terms are independent of the newly
exposed column; the one-step moment contributes the next term exactly as in
the frozen bridge.  The deficit index is therefore correct.

For deletion of $u$ vertices, positivity and the upper bound of one on the
bracket give

$$
0\le\mathcal D(\ell)-\mathcal D(\ell-u)
\le\frac{m_0^4\ell^3u}{d}
\le\frac{m_0^4}{D^2}\ell u.
$$

Since $m_0^4/D^2=(1+o(1))/(8\log C)<1$, the same single $\ell u$ charge
used in the frozen extraction pays for the new deficit.  It replaces, rather
than adds to, the old companion.  The edge and cubic restoration charges and
the factor $(p/10)^{10\ell u}$ are unchanged, so the retained-set sum remains
$o(1)$.

### 8. Strict same-window, same-history comparison: PASS

Keep the old cutoff window and the old constant Hölder pair.  For every
positive tilt, strict variance monotonicity gives

$$
\psi_b(u)<\frac{v(b)}2.
$$

After multiplying by the positive $x^3$ weight and integrating over
$x\in(0,1]$, this proves

$$
G_{\rm same}(C)>\frac{c_R(C)}{4D^2}
$$

without appealing to the smaller limiting window or a different history.
This is the cleanest proof of strictness.

Moving from the old window to $b_*$ raises $m$, lowers $\psi$, and raises
the positive CGF argument; moving from $P_{\rm old}$ to $P_*(x)$ also lowers
$P\psi_b(Pz)$.  The bracket is positive for sufficiently large $C$, and the
outer $m^2$ prefactor increases.  Hence

$$
G_*(C)>G_{\rm same}(C)>\frac{c_R(C)}{4D^2}.
$$

### 9. Public rate and the blue bottleneck: PASS

The new accumulated deficit contributes $-G(C,w)\ell^2+o(\ell^2)$ to the
red clique log-probability.  Since $n=e^{\rho\ell}$ contributes
$+\rho\ell^2+o(\ell^2)$ to the red first moment, the rate gain is $+G(C,w)$,
not $G(C,w)/2$.

HMS lines 1296--1339 give the public red probability factor
$p_Ce^{-1/10}$ and the public blue factor
$(1-p_C)e^{-1/(3C)}$.  Therefore their first-moment bonuses are $1/20$ and
$1/6$, respectively.  In the exact frozen ledger,

$$
\frac{B_R(C)}2=\frac1{12}+o(1),\qquad
\frac{CB_B(C)}2=\frac12+o(1).
$$

The optimized term is $G_*(C)=o(1)$, so red remains the bottleneck for every
sufficiently large fixed $C$.  The floor in $\lfloor C\ell\rfloor$ changes
only $o(\ell^2)$ terms, as already checked in the frozen bridge.

### 10. The method cap and central history: PASS WITH SCOPE WARNING

At the central prefix history $b_i=c_p$,

$$
\mu_i=-\frac{m_0}{\sqrt d},\qquad
A_i=-\frac{(k-1)m_0}{\sqrt d}.
$$

Let

$$
W_s=\sum_iA_i\xi_i+\sum_{i<j}\xi_i\xi_j.
$$

Independence and centering give $\mathbb EW_s=0$, so Jensen gives the lower
bound

$$
\log\mathbb E e^{\lambda W_s}\ge0.
$$

The frozen centered envelope on that history is

$$
\frac{m_0^4}{d}k(k-1)^2+\frac{4m_0k}{\sqrt d}.
$$

Any deterministic per-$k$ saving valid for **every** admissible history must
also be valid here, and hence cannot exceed this entire allocation.  The
central prefix is geometrically red-perfect when the diagonal entries equal
one and prior projection inner products vanish.  If one insists on
positive-probability representatives for regular conditional laws, take
red-perfect histories approaching this prefix; all moment expressions and
the HMS envelope are continuous, while the saving itself is deterministic.

Summing the quadratic allocation and dividing by $\ell^2$ gives
$m_0^4/(4D^2)$.  The remainder contributes only

$$
\frac1{\ell^2}\sum_{k<\ell}\frac{4m_0k}{\sqrt d}
=O_C(\ell^{-1})\to0.
$$

This proves (M).  Moreover, $m_*/m_0\to1$, $P_*(x)\to1$, and
$\psi_{b_*}(u_*(x))\to0$ uniformly, so

$$
G_*(C)=(1+o(1))\frac{m_0^4}{4D^2}
=\frac{1+o(1)}{32\log C}.
$$

The cap is therefore sharp at leading order in the declared method class.
It is not a universal impossibility theorem.

## Independent arithmetic replay

I first ran the author checker at 180 decimal digits.  It passed the exact
finite-sum identity, all strict old/same-window/constant-$Q$/optimized
orderings at $C=10^{12},10^{20},10^{40},10^{80}$, the method cap, and the
approach of $32\log C\,G_*(C)$ to one.

I then made an independent replay that did **not** evaluate $K_b$ using the
author's closed log-tail formula.  Instead it computed

$$
\psi_b(u)=\int_0^1(1-t)v(b+ut)\,dt
$$

directly and used a separately written bisection and quadrature path.  At
$C=10^{15}$ it returned

$$
\begin{array}{c|c}
\text{quantity}&\text{value}\\ \hline
c_R/(4D^2)&0.0000216324664155608857494879\\
G_{\rm same}&0.0000216378663870180779462787\\
G_*&0.000275622124706968923827464\\
m_0^4/(4D^2)&0.000882291047133853995215838
\end{array}
$$

and independently checked $K_b''(u)-v(b+u)$ at a nonsource grid point to
about $10^{-78}$.  These computations are diagnostics only; the theorem is
supported by the analytic inequalities above.

## Resolved review comments and residual limitations

1. The reviewed draft originally called $P_kv_w<2$ "asymptotically
   necessary" without formalizing necessity.  The final reviewed version
   now claims only the sufficient condition that the proof uses.
2. The final reviewed version also restricts the positivity argument to a
   sufficiently small right-neighborhood of $\omega_0$, using continuity
   from $P_*(1)v_*<2$.  This removes any suggestion of uniformity over
   arbitrarily large $w>\omega_0$.
3. I re-ran the literal documented command in the repository root after the
   final edit.  `.venv/bin/python` imports `mpmath` version 1.4.1 and the full
   checker passes.  There is no remaining environment warning.
4. The checker uses arbitrary-precision floating-point quadrature, not
   interval arithmetic.  It should remain labeled diagnostic, as the proof
   document already does.

## Final referee statement

- **Strict fixed-$C$ improvement:** PASS.
- **Exact same-window strictness:** PASS.
- **Hölder/CGF/window leading coefficient $1/32$:** sharp inside the stated
  uniform additive centered-moment class.
- **Claim that no Ramsey lower-bound method can beat $1/32$:** not made and
  not proved.
- **Most promising route beyond this package:** change the deterministic
  red mean/connection ledger or the blue feasibility lemma, or retain a
  history-dependent saving in a richer induction state.
