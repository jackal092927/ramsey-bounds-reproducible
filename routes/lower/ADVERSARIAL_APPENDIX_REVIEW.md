# Adversarial review of the HMS optimized-appendix bridge

Date: 2026-08-12  
Object reviewed: [HMS_APPENDIX_BRIDGE.md](./HMS_APPENDIX_BRIDGE.md)  
Review posture: search for the earliest fatal gap, not optimization

## Sources independently replayed

I downloaded the two cited v2 source archives from the official arXiv
e-print endpoints and checked the relevant proofs against fresh copies.

- Hunter--Milojević--Sudakov (HMS),
  [arXiv:2512.17718v2](https://arxiv.org/abs/2512.17718),
  `arXiv_version.tex`, SHA-256
  `b72958ac35554eccb94dedab5800349d2c021af7d60f767125cb46998e0fd54a`.
- Lin--Niu,
  [arXiv:2605.25843v2](https://arxiv.org/abs/2605.25843),
  `off-diagonal-Ramsey-R.tex`, SHA-256
  `dbf1bfa2c7603c81b2e56a97028b138ccf9a9299a3d1f20c0b08cf489136f429`.

The hashes agree with the snapshots identified in the bridge document.
Line references below are to those exact source files.

## Claim under review

For every sufficiently large fixed real $C$, with the notation of the
bridge, the red same-history Hölder refinement contributes the strictly
positive rate term

$$
\frac{c_R(C)}{4D^2}
$$

to the same frozen HMS red ledger. In particular, the bridge claims

$$
\liminf_{\ell\to\infty}\frac1\ell
\log R\!\left(\ell,\lfloor C\ell\rfloor\right)
\ge
-\frac12\log p_C+\frac1{20}+\frac{c_R(C)}{4D^2},
\tag{A}
$$

as well as its exact frozen-ledger formulation (T). The blue side is left
unchanged.

## Status

**Proof-writer status: PROVABLE AS STATED.**  
**Adversarial verdict: PASS WITH DEPENDENCIES.**

I did not find a fatal gap in the red bridge, its extraction, or the passage
to the Ramsey rate. The conclusion survives unchanged, provided that the
source lemmas listed under **Dependencies and residual risks** are accepted.
The exact theorem (T) is non-effective because its source constant $K$ is
not numerically specified; this is a limitation of presentation and
computability, not a false inference. The public theorem (A) does not expose
$K$ in its stated rate.

## Dependency map

1. The local deficit depends on the exact pre-Cauchy expression inside the
   proof of HMS's quadratic-moment lemma (HMS lines 895--935), not merely on
   the coarsened statement of that lemma.
2. Its improved linear factor depends on the one-sided upper-truncated CGF
   inequality in Lin--Niu lines 499--537 and on the HMS centered-quadratic
   estimate after Hölder inflation.
3. Propagation to $P^*_{R,r}$ depends on reopening the HMS reverse induction
   at lines 1192--1289 with one fixed one-sided representative of every
   source $O(\sqrt{\log p^{-1}}/D)$ term.
4. Propagation to $P_{R,\ell}$ depends on the perfect-sequence deletion
   argument at HMS lines 385--440, with the appendix's red value of
   $\alpha$ from lines 955--971.
5. The Ramsey conclusion depends on the unchanged HMS blue bound and a
   first-moment union bound.

## Adversarial checks

### 1. Freezing the unspecified source constant $K$

This is legal only with the following quantifier order:

$$
\exists K<\infty\ \exists C_0\ \forall C\ge C_0\
\exists \ell_0(C)\ \forall \ell\ge\ell_0(C).
\tag{1}
$$

HMS explicitly declares the appendix's implied $O(\cdot)$ constants to be
absolute at line 973. There are finitely many red occurrences in lines
1180--1289. Thus one may choose a single $K$ dominating their one-sided
errors and replace every negative factor

$$
-\bigl(1+O(x_C)\bigr)A,
\qquad x_C=\frac{\sqrt{\log p^{-1}}}{D},\quad A\ge0,
$$

by the weaker but literal upper bound $-(1-Kx_C)A$. Since
$D/\sqrt{\log p^{-1}}\to\infty$, the resulting
$\theta_C=1-Kx_C$ is positive after increasing $C_0$.

What is *not* justified is treating $K$ as known numerically or advertising
(T) as an effective finite-$C$ numerical bound. The bridge does neither in
its proof, although the theorem would be clearer if it said explicitly
"there exists an absolute $K$" before defining $B_R(C)$. This does not
affect (A), which uses HMS's public $e^{-1/10}$ ledger.

**Verdict:** no fatal quantifier gap; non-effective dependency only.

### 2. Does the same-history Hölder deficit really subtract?

Let $L_s=\log\mathbb E e^{\lambda S}$ for a fixed admissible history. The
two relevant explicit expressions satisfy

$$
L_s\le R_s,
$$

where $R_s$ is the refined Hölder envelope, and the formulas themselves give

$$
H_s-R_s=
\frac{\lambda^2}{d}\sum_i
\left(1-\frac{P_Cv_R(b_i)}2\right)A_i^2
\ge \mathsf d_k.
$$

Consequently the logical chain is

$$
L_s\le R_s\le H_s-\mathsf d_k.
\tag{2}
$$

This is not the invalid operation of subtracting two unrelated upper bounds.
The exact expression $H_s$ is obtained by stopping the proof of HMS's lemma
after its product linear-MGF bound (HMS lines 906--913) and before the final
Cauchy bound on $A_i$. The refined expression $R_s$ follows from Hölder,
Lin--Niu's CGF lemma, and the same HMS quadratic estimate. For the actual
upper cutoff $Z\le-b_i$, Lin--Niu's variance is exactly

$$
v_R(b_i)=1+b_i m_R(b_i)-m_R(b_i)^2.
$$

The CGF argument is positive because $\lambda<0$ and $A_i<0$. For $k=1$
the argument is zero and the claim follows by continuity/equality; the
deficit is then also zero.

The Hölder quadratic factor is admissible because

$$
4Q_C|\lambda|k
\le \frac{D\ell\sqrt d}{2}
\le \frac d2.
$$

The cutoff window gives $v_R(b_i)\le v_+$ and
$|A_i|\ge(k-1)m_-/\sqrt d$, hence

$$
\mathsf d_k=\frac{c_R(C)}d k(k-1)^2.
$$

Finally, the HMS coarsening has the direction $H_s\le U_s$, where $U_s$
is the source one-step envelope with coefficient $\theta_C$. Combining this
with (2) gives $L_s\le U_s-\mathsf d_k$, so the deficit is subtracted before
the source errors are coarsened.

**Verdict:** the subtraction is sound and history-uniform.

### 3. Positivity of $c_R(C)$ and its quantifiers

For $p=p_C+1/C$ and $C\to\infty$, standard uniform Mills expansions on
$|b-c_p|\le\omega_C$ give

$$
m_-=(1+o(1))m_0,\qquad v_+=o(1),\qquad
Q_C\to\infty,\qquad P_C=1+o(1).
$$

Thus $\kappa_C=1-P_Cv_+/2>0$ and
$c_R(C)=\kappa_Cm_0^2m_-^2>0$ for all $C$ beyond one fixed threshold.
The cutoff window is valid only after subsequently choosing
$\ell\ge\ell_0(C)$ so that the $d^{-1/5}$ error is small. This matches the
quantifier order (1).

The bridge's appeal to continuity alone is terse: continuity on a moving
interval would not suffice by itself. Uniform Mills asymptotics as
$c_p-\omega_C\to\infty$ supply the missing one-line justification. This is
a routine expansion, not an additional conjecture.

**Verdict:** positive for sufficiently large fixed $C$; no joint
$C,\ell\to\infty$ claim is proved or needed.

### 4. Reverse-induction direction and deficit index

At induction level $s$, let $k=r-s$ be the size of the already treated
suffix. Use the strengthened state

$$
\Psi(k):=\sum_{t=1}^{k-1}\mathsf d_t.
$$

The HMS step from $s$ to $s-1$ changes $k$ to $k+1$ and introduces the
one-step moment with deficit $\mathsf d_k$. Therefore

$$
\Psi(k)+\mathsf d_k=\Psi(k+1).
$$

The base $k=0$ or $1$ has zero deficit. At $s=0$, $k=r$, so the accumulated
quantity is exactly

$$
\Psi(r)=\sum_{t=1}^{r-1}\frac{c_R(C)}d\,t(t-1)^2
=\mathcal D_C(r).
$$

The sign is favorable throughout: every step multiplies the upper bound by
$e^{-\mathsf d_k}$.

**Verdict:** the reverse direction and the endpoint $r-1$ are correct.

### 5. Perfect-sequence extraction and the sum over bad vectors

For a retained set of size $\ell-u$, the appendix red projection failure
cost can be bounded by

$$
\left(\frac p{10}\right)^{10\ell u}.
$$

This follows from the conditional projection tail used in HMS lines
400--410 after replacing the main-body $\alpha$ by
$\alpha_R=10\sqrt{\log(10/p)}$. The discarded-vector events need not be
independent: the bound is uniform conditional on all earlier vectors, so a
tower-property product gives the displayed factor. Edges involving
discarded vectors are dropped, which only enlarges the event.

Writing

$$
\Delta_j=\binom\ell j-\binom{\ell-u}j,
$$

the exact logarithm of the ratio between the retained bound and the desired
$r=\ell$ bound contains the costs

$$
\Delta_2\log(1/p)
+\theta_C\frac{a^3}{p^3\sqrt d}\Delta_3
+\bigl(\mathcal D_C(\ell)-\mathcal D_C(\ell-u)\bigr),
\tag{3}
$$

and also two favorable terms, which the bridge legitimately discards:

$$
-\frac apd^{-1/5}\Delta_2-u.
$$

For $0\le u\le\ell$,

$$
\Delta_2\le\ell u,\qquad
\Delta_3\le\frac12\ell^2u,\qquad
\mathcal D_C(\ell)-\mathcal D_C(\ell-u)
\le\frac{4c_R(C)}{D^2}\ell u.
$$

For sufficiently large $C$, (3) is at most
$(\log(1/p)+2)\ell u$, whereas the failure factor contributes
$-10\log(10/p)\ell u$. Hence each nonempty deletion class has a residual
$-\eta_C\ell u$ with $\eta_C>0$, and

$$
\sum_{u=1}^{\ell}\binom\ell u e^{-\eta_C\ell u}=o(1).
$$

The retained sizes $1$ and $2$ are covered by the underlying HMS induction,
whose statement is valid down to $r=1$; size $0$ uses the empty-event
convention. No bad-vector class is omitted.

**Verdict:** the deficit survives extraction; the union over retained sets
is summable with ample fixed-$C$ slack.

### 6. Red/blue bottleneck and min/max direction

The exact limiting first-moment constraints are

$$
\rho<\rho_R(C):=
-\frac12\log p_C+\frac{B_R(C)}2+\frac{c_R(C)}{4D^2}
$$

and

$$
\rho<\rho_B(C):=
-\frac12\log p_C+\frac{CB_B(C)}2.
$$

The admissible rate is their **minimum**, not their maximum. The bridge uses
this direction correctly. Its source asymptotics give

$$
\frac{B_R(C)}2=\frac1{12}+o(1),\qquad
\frac{CB_B(C)}2=\frac12+o(1),\qquad
\frac{c_R(C)}{4D^2}=o(1).
$$

Thus $\rho_R(C)<\rho_B(C)$ for all sufficiently large $C$. In the public
coarsening the corresponding bonuses are
$1/20+c_R(C)/(4D^2)$ and $1/6$, so red is again the bottleneck eventually.

**Verdict:** no min/max reversal and no need for a blue improvement.

### 7. Is the public $+1/20$ legal?

Yes. HMS's public red probability lemma supplies the per-edge factor
$e^{-1/10}$. With $n=\exp(\rho\ell)$, the leading red first moment tends to
zero for every

$$
\rho<-\frac12\log p_C+\frac1{20}
+\frac{c_R(C)}{4D^2}.
$$

The unchanged blue first moment permits the larger public rate
$-\frac12\log p_C+1/6$. Therefore (A) follows. The difference
$1/20-1/24=1/120$ is unused HMS slack, not a contribution of the new
Hölder deficit; the bridge labels this correctly.

**Verdict:** $+1/20$ is a valid public consequence, but only the
$c_R(C)/(4D^2)$ term is new.

### 8. From clique probabilities to the Ramsey rate

For every fixed $\rho<\min\{\rho_R(C),\rho_B(C)\}$, take an integer
$n=\lfloor e^{\rho\ell}\rfloor$. The expected number of red
$K_\ell$'s and blue $K_{q_\ell}$'s, where
$q_\ell=\lfloor C\ell\rfloor$, both tend to zero. Hence for all sufficiently
large $\ell$ there is a coloring on $n$ vertices containing neither, so

$$
R(\ell,q_\ell)>n.
$$

Letting $\rho$ increase to the minimum gives the claimed liminf inequality.
This is the correct direction from probability to Ramsey number.

**Verdict:** sound.

### 9. The floor $\lfloor C\ell\rfloor$

The HMS blue-perfect proposition applies to every integer
$r\le C\ell$ (and $r\ge10$, automatic eventually), not only to $r=C\ell$.
With $q_\ell=C\ell+O(1)$,

$$
\frac{q_\ell}{\ell}=C+O(\ell^{-1}),\qquad
\binom{q_\ell}{j}=\binom{C\ell}{j}+O_C(\ell^{j-1})
$$

for $j=2,3$. After the $\ell^2$ normalization all changes are $o(1)$.
The identity $C\log(1-p_C)=\log p_C$ remains the limiting baseline.

**Verdict:** the floor introduces no rate loss.

## Earliest fragile point

The earliest point that would become a genuine gap if cited only from a
black-box source statement is the passage from bridge equation (19) to (20).
HMS's *stated* moment lemma has already applied Cauchy and hides the error in
$O(\sqrt{\log p^{-1}}/D)$. The new deficit is recoverable only by reopening
the proof at HMS lines 895--935, retaining $\sum_iA_i^2$, and choosing a
single one-sided $K$ before running the appendix induction. The bridge does
exactly this, and the source proof supports the required inequality
directions. Therefore this is a fragile dependency, not a fatal gap.

## Dependencies and residual risks

- The review accepts HMS's Bartlett representation, projection/norm tails,
  log-concavity step, and the fact that a centered truncated Gaussian has
  subgaussian proxy at most the untruncated variance. The last fact is cited
  by HMS to external work and was not reproved here.
- The review checked the proof of Lin--Niu's one-sided CGF lemma and its
  cutoff orientation. It is used only for positive tilts of an
  upper-truncated Gaussian.
- Standard uniform Mills-ratio expansions are required to turn the bridge's
  asymptotic positivity discussion into a literal $C_0$ statement.
- Neither source preprint nor this local proof package has external peer
  review. This verdict is a source-relative mathematical replay, not a
  publication-level certification.
- The exact ledger theorem (T) remains non-effective until an explicit HMS
  one-sided constant $K$ is derived. The public theorem (A) remains a valid
  asymptotic theorem without such a numerical extraction.

## Final adversarial verdict

No fatal gap was found in any of the requested checkpoints:

1. freezing the source $K$ is legitimate with existential, ordered
   quantifiers;
2. the same-history deficit is a bound on the refined MGF itself and is
   subtracted before HMS coarsening;
3. reverse induction accumulates exactly $\mathcal D_C(r)$ with the correct
   sign;
4. the bad-vector extraction pays for every lost red, cubic, and deficit
   term and its subset sum is negligible;
5. red is the minimum of the red/blue rate constraints for sufficiently
   large $C$;
6. the probability bounds imply the stated Ramsey liminf;
7. the public $+1/20$ is legal but pre-existing HMS slack;
8. $c_R(C)>0$ has the correct "first $C$, then $\ell$" quantifiers; and
9. replacing $C\ell$ by $\lfloor C\ell\rfloor$ changes only $o(1)$ terms.

Accordingly, the red lower-bound improvement should remain classified as a
**local proof-package theorem, PASS WITH DEPENDENCIES, pending external
human review**.
