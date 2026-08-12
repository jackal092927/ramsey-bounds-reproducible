# Paired pathwise companion attempt

Date: 2026-08-12  
Target: the paired companion gap isolated in
[EXACT_COMPANION_AUDIT.md](./EXACT_COMPANION_AUDIT.md)

Primary sources:

- Hunter--Milojević--Sudakov (HMS),
  [arXiv:2512.17718v2](https://arxiv.org/abs/2512.17718v2), source file
  `arXiv_version.tex`, SHA-256
  `b72958ac35554eccb94dedab5800349d2c021af7d60f767125cb46998e0fd54a`.
- Lin--Niu,
  [arXiv:2605.25843v2](https://arxiv.org/abs/2605.25843v2), source file
  `off-diagonal-Ramsey-R.tex`, SHA-256
  `dbf1bfa2c7603c81b2e56a97028b138ccf9a9299a3d1f20c0b08cf489136f429`.

Line numbers below refer to those hashed source files.

## Claim

There are two distinct questions.

1. **Paired-ledger question.** Can the HMS $P=2$ exponential-moment proof and
   the refined $P_D\to1$ truncated-CGF proof be propagated through the same
   Bartlett histories, with all non-CGF terms charged to one common error
   ledger?
2. **Published-comparator question.** Is the resulting frozen HMS ledger the
   same object as the final $\rho_{\rm HMS}(D)$ and
   $\varepsilon_{\rm HMS}$ used in Lin--Niu's theorem comparison?

## Status

- **Paired ledger lemma: PROVABLE AS STATED for fixed $p,C$.** A complete
  proof is given below. Relative to a frozen, source-faithful HMS main-body
  ledger, the refined red induction saves

  $$
  \left(\frac{1+\gamma_R}{8}+O_{p,C}(D^{-1})\right)
  \frac{a^4}{p^4}\frac{r^4}{d}
  +O_{p,C}(r^3/d).
  \tag{1}
  $$

  The fixed-$C$ blue analogue has $p,\gamma_R$ replaced by
  $1-p,\gamma_B$.

- **Identification with a published final $\rho_{\rm HMS}(D)$: NOT
  CURRENTLY JUSTIFIED.** HMS v2 does not define a canonical exact
  $\rho_{\rm HMS}(D)$ in its main-body proof; it records a generic
  $O(r^4/d)$ error. Its explicit large-$C$ theorem uses a different appendix
  induction and different red/blue perfectness ledgers. Lin--Niu introduce
  their own $\rho_{\rm HMS}$ from an unspecified $K$ and later identify it
  with “the constant obtained in HMS.” The paired proof below makes one
  common $K$ legitimate, but it does not prove that comparator
  identification.

Thus this note closes the pathwise propagation gap, but it does **not** yet
establish a new Ramsey lower bound or validate Lin--Niu's final theorem.

## Evidence labels

- **[SOURCE]** literal statement or operation in one of the two hashed TeX
  files.
- **[DERIVED]** proved in this note from the displayed source ingredients.
- **[COMPUTED]** finite arithmetic check only.
- **[OPEN]** an implication not supplied by either source or this proof.

## Assumptions and notation

Fix $p\in(0,1/2)$ and $C>1$. Let

$$
d=D^2\ell^2,\qquad 1\le r\le C\ell,
$$

where first $D=D(p,C)$ is sufficiently large and then
$\ell=\ell_0(p,C,D)$ is sufficiently large. Put

$$
q=1-p,\qquad \Phi(-c_p)=p,\qquad a=\phi(c_p).
$$

For the red calculation define

$$
m_R=\frac ap,\qquad \lambda_R=-m_R\sqrt d,
$$

and let

$$
V_R=\operatorname{Var}(Z\mid Z\le-c_p)=1-\gamma_R,
\qquad
\gamma_R=\frac ap\left(\frac ap-c_p\right)>0.
$$

As in HMS lines 492--493, first condition on fixed diagonal entries satisfying
the perfect-event bounds. At reverse-exposure step $s$, set $k=r-s$.
Conditional on a fixed perfect history $M[s-1]$, the edge events leave

$$
X_i=y_i(s),\qquad s<i\le r,
$$

independent upper-truncated $N(0,1/d)$ variables. Write

$$
\mu_i=\mathbb E X_i,\qquad
\xi_i=X_i-\mu_i,\qquad
A_i=\sum_{\substack{s<j\le r\\j\ne i}}\mu_j,
\qquad
S_s=\sum_{s<i<j\le r}X_iX_j.
\tag{2}
$$

For every history compatible with the perfect event, the HMS cutoff estimate
(source lines 606--630) gives, uniformly in $i,s,r$,

$$
\mu_i=-\frac{m_R}{\sqrt d}
+O_{p,C}\left(\frac1{D\sqrt d}\right),
\qquad
V_i:=d\operatorname{Var}(X_i)
=1-\gamma_R+O_{p,C}(D^{-1}).
\tag{3}
$$

Put $\delta_{\rm perf}:=\alpha d^{-1/4}$, with the source's fixed
$\alpha=\alpha(p,C)$. The $\ell_0(D)$ ordering absorbs this diagonal error
into the $D^{-1}$ cutoff window.

## Source-line map

| Source lines | Role in the paired proof | Verdict |
|---|---|---|
| HMS 895--904 | exact decomposition $S=\mathbb ES+L+Q$ and $P=Q=2$ split | **[SOURCE]** |
| HMS 906--913 | before the final Cauchy inequality, the linear exponent is $(\lambda^2/d)\sum_iA_i^2$ | **[SOURCE]** |
| HMS 915--935 | centered quadratic contribution becomes $4|\lambda|k/d$ | **[SOURCE]** |
| HMS 531--573 | law of total probability, geometric-potential merge, reverse induction | **[SOURCE]** |
| HMS 606--630 | exact conditional truncations and uniform mean expansion | **[SOURCE]** |
| Lin--Niu 577--633 | same decomposition, $P_D,Q_D$ Hölder split, and exact $A_i$ before Cauchy | **[SOURCE]** |
| Lin--Niu 636--670 | replaces $\sum A_i^2$ by a coarser bound too early | **[SOURCE; avoid in pairing]** |
| Lin--Niu 673--724 | centered quadratic contribution is again $4|\lambda|k/d$ | **[SOURCE]** |
| Lin--Niu 767--961 | reverse induction; all common terms already merge in the HMS manner | **[SOURCE]** |
| Lin--Niu 1127--1173 | introduces an HMS exponent using an unspecified constant $K$ | **[SOURCE; not canonical]** |
| Lin--Niu 1200--1208 | states that HMS has coefficient $1/2$ | **[FAILED; HMS has coefficient $1$]** |
| Lin--Niu 1352--1359 | identifies its ledger exponent with “the constant obtained in HMS” | **[OPEN comparator identification]** |
| HMS 940--1362 | explicit large-$C$ result uses a different optimized appendix induction | **[SOURCE; earliest route divergence]** |

## Dependency map

The proof has four nontrivial components.

1. **Local exact pairing:** retain the same $\mu_i,A_i,V_i$ and history in
   both exponential-moment estimates.
2. **Uniform forced deficit:** lower-bound their difference before any
   history-dependent term is coarsened.
3. **Ledger-preserving reverse induction:** subtract that deterministic
   deficit while applying every other source inequality only once, into a
   common HMS ledger.
4. **Extraction:** use the existing exponentially costly non-perfect-event
   deletion to absorb the loss from replacing $(r-u)^4$ by $r^4$.

Only the later identification of this ledger with a published final HMS
constant remains open.

## Paired companion lemma

> **Lemma (fixed-$C$ paired main-body companion) [DERIVED].** Under the
> assumptions above, there are constants $K_0,K_1$ depending only on $p,C$
> such that the deterministic quantities $\mathsf d_k,\mathsf u_k$ in
> (12) and (14) are valid simultaneously for every compatible perfect
> Bartlett history. With $\mathfrak H_{s,r}$ and $\mathfrak R_{s,r}$ defined
> by (15)--(16), for every $0\le s\le r-1$,
> 
> $$
> \mathbb P(I_s\wedge B_r\mid M[s])\le \mathfrak R_{s,r}.
> $$
> 
> Consequently (21) holds for the red perfect-event probability. The
> lower-truncated Taylor-CGF estimate gives the fixed-$C$ blue analogue
> (22), and the source's extraction argument preserves the deficit as in
> (24). This lemma compares against the explicitly frozen main-body ledger;
> it makes no identification with a final published $\rho_{\rm HMS}$.

## Proof

### Step 1: exact local HMS and refined envelopes

Expanding (2) gives the identity

$$
S_s=\mathbb ES_s+\sum_iA_i\xi_i+\sum_{i<j}\xi_i\xi_j.
\tag{4}
$$

Stop the HMS proof at source line 909, before replacing $A_i^2$ by a
Cauchy bound. Its $P=Q=2$ argument gives

$$
H_s
:=
\lambda_R\mathbb ES_s
+\frac{\lambda_R^2}{d}\sum_iA_i^2
+\frac{4|\lambda_R|k}{d}
\tag{5}
$$

as an upper bound for
$\log\mathbb E\exp(\lambda_RS_s)$. Here and below all expectations are
under the same edge-conditioned history.

Choose real Hölder exponents

$$
Q_D=\frac{D}{8C m_R},\qquad
P_D=\frac{Q_D}{Q_D-1}.
\tag{6}
$$

For sufficiently large $D$, $Q_D>1$,
$P_D=1+O_{p,C}(D^{-1})$, and

$$
d\ge4Q_D|\lambda_R|k
$$

for every $k\le C\ell$. The upper-truncated CGF inequality of Lin--Niu
applies because $\lambda_R<0$ and, for sufficiently large $D$, $A_i<0$ when
$k\ge2$ (while $A_i=0$ when $k=1$). Thus
$P_D\lambda_RA_i/\sqrt d\ge0$. Retaining $A_i$ exactly gives

$$
R_s
:=
\lambda_R\mathbb ES_s
+\frac{P_D\lambda_R^2}{2d}\sum_iV_iA_i^2
+\frac{4|\lambda_R|k}{d}
\tag{7}
$$

as another valid upper bound for the same log moment.

The deterministic mean term and the centered-quadratic remainder in
(5)--(7) are literally identical. Hence, pathwise,

$$
H_s-R_s
=\frac{\lambda_R^2}{d}
\sum_i\left(1-\frac{P_DV_i}{2}\right)A_i^2.
\tag{8}
$$

This identity is the common-history cancellation which is lost if one first
replaces $\sum_iA_i^2$ by unrelated big-$O$ estimates.

### Step 2: a uniform history-independent deficit

By (3), there is a constant $K_0=K_0(p,C)$ such that

$$
1-\frac{P_DV_i}{2}
\ge \frac{1+\gamma_R}{2}-\frac{K_0}{D}
\tag{9}
$$

for every relevant history. Also, after increasing $D$ if necessary,
all $\mu_i$ are negative and

$$
|A_i|
\ge(k-1)\left(\frac{m_R}{\sqrt d}
-\frac{K_0}{D\sqrt d}\right).
\tag{10}
$$

Equations (8)--(10) imply

$$
H_s-R_s\ge \mathsf d_k,
\tag{11}
$$

where

$$
\mathsf d_k
:=
\left(\frac{1+\gamma_R}{2}-\frac{K_0}{D}\right)
m_R^2\left(m_R-\frac{K_0}{D}\right)^2
\frac{k(k-1)^2}{d}.
\tag{12}
$$

Equivalently,

$$
\mathsf d_k
=\left(\frac{1+\gamma_R}{2}+O_{p,C}(D^{-1})\right)
\frac{a^4}{p^4d}k(k-1)^2.
\tag{13}
$$

For sufficiently large $D$, $\mathsf d_k\ge0$. It is zero for $k=1$,
as it must be because $S_s$ then has no pair.

### Step 3: freeze one common HMS error ledger

The source proof next approximates $\lambda_R\mathbb ES_s$, merges the
geometric terms, and bounds the connection probability. Perform those
operations **once**, on the HMS envelope (5), and freeze one constant
$K_1=K_1(p,C)$ valid uniformly over all perfect histories. A valid one-step
ledger is

$$
\mathsf u_k
=\frac{a^4}{p^4d}k(k-1)^2
+K_1\left(
\frac{k^2}{D\sqrt d}
+\frac{k^3}{Dd}
+\frac{k}{\sqrt d}
+k\delta_{\rm perf}
\right).
\tag{14}
$$

Indeed:

- the first term is the leading part of (5)'s exact linear-MGF term under
  (3), with its uniform discrepancy charged to $k^3/(Dd)$;
- $k^2/(D\sqrt d)$ is the error in the common
  $\lambda_R\mathbb ES_s$ term;
- $k^3/(Dd)$ is the error in the common expansion of $\sum A_i^2$;
- $k/\sqrt d$ is the common centered-quadratic remainder;
- $k\delta_{\rm perf}$ is the common connection-probability error.

This is a refinement of the generic $O(k^4/d+k)$ ledger in HMS lines
500--506, not a new probabilistic assumption.

Let

$$
\Sigma_s=\sum_{s<i<j\le r}
\langle\pi_s(y_i),\pi_s(y_j)\rangle,
\qquad k=r-s.
$$

Define the frozen HMS source envelope

$$
\mathfrak H_{s,r}
=p^{\binom k2}
\exp\left(
-\frac{a\sqrt d}{p}\Sigma_s
-\frac{a^3}{p^3\sqrt d}\binom k3
+\sum_{t=1}^{k-1}\mathsf u_t
\right)
\tag{15}
$$

and its paired refined envelope

$$
\mathfrak R_{s,r}
=\mathfrak H_{s,r}
\exp\left(-\sum_{t=1}^{k-1}\mathsf d_t\right).
\tag{16}
$$

Again the juxtaposition in (16) is multiplication.

### Step 4: ledger-preserving reverse induction

We prove

$$
\mathbb P(I_s\wedge B_r\mid M[s])\le\mathfrak R_{s,r}
\tag{17}
$$

for every history, by reverse induction on $s$.

For $s=r-1$, $k=1$, both sums in (15)--(16) are empty, $\Sigma_s=0$,
and the right-hand side is one. Thus (17) holds.

Assume (17) at $s$ and expose column $M_s$ from a fixed history
$M[s-1]$. The law-of-total-probability identity is exactly HMS source
lines 531--535 and Lin--Niu lines 786--802. In the induction hypothesis,

$$
\Sigma_s
=\sum_{s<i<j\le r}
\langle\pi_{s-1}(y_i),\pi_{s-1}(y_j)\rangle+S_s.
\tag{18}
$$

All factors in (16) except $\exp(\lambda_RS_s)$ are independent of the
new Gaussian coordinates, including the accumulated deficit
$\sum_{t=1}^{k-1}\mathsf d_t$. This is why a uniform deficit was taken
*after* the exact pathwise subtraction.

Apply the refined moment envelope (7). By (11),

$$
R_s\le H_s-\mathsf d_k.
\tag{19}
$$

Now apply to $H_s$ the already frozen HMS ledger operation (14). No common
term is estimated a second time. The connection-potential term combines
with the first term in (18) to form $\Sigma_{s-1}$, and

$$
\binom k2+k=\binom{k+1}{2},\qquad
\binom k3+\binom k2=\binom{k+1}{3}.
$$

The old and new deficits combine as

$$
\sum_{t=1}^{k-1}\mathsf d_t+\mathsf d_k
=\sum_{t=1}^{k}\mathsf d_t.
$$

The resulting expression is exactly $\mathfrak R_{s-1,r}$. This proves
(17) and completes the reverse induction. ∎

This argument also explains why retaining *all* exact future deficit terms
inside the induction state would be awkward: those terms depend on the
newly exposed column and would create new cross-moments. The correct state is
the common HMS history potential plus the **uniform group deficit** (12).

### Step 5: exact accumulation

The finite sum is

$$
\sum_{k=1}^{r-1}k(k-1)^2
=\frac{r(r-1)(r-2)(3r-5)}{12}
=\frac{r^4}{4}+O(r^3).
\tag{20}
$$

Putting $s=0$ in (17) and using (13)--(20) gives

$$
\log\mathfrak R_{0,r}-\log\mathfrak H_{0,r}
\le
-\frac{(1+\gamma_R)a^4}{8p^4}\frac{r^4}{d}
+O_{p,C}\left(\frac{r^4}{Dd}+\frac{r^3}{d}\right).
\tag{21}
$$

This proves (1). The old audit's proposed coefficient
$(1+\gamma_R)a^4/(8p^4)$ is therefore not merely a local heuristic: it
propagates through the fixed-$C$ perfect-history induction relative to the
frozen HMS source ledger.

### Step 6: fixed-$C$ blue analogue

For blue cliques put

$$
m_B=\frac a{1-p},\qquad
\lambda_B=m_B\sqrt d,
$$

and

$$
V_B=\operatorname{Var}(Z\mid Z\ge-c_p)=1-\gamma_B,
\qquad
\gamma_B=\frac a{1-p}\left(c_p+\frac a{1-p}\right)>0.
$$

The conditional means are
$\mu_i=m_B/\sqrt d+O_{p,C}(1/(D\sqrt d))$, so $A_i>0$ for $k\ge2$
and $A_i=0$ for $k=1$; the linear tilt is nonnegative. The lower-truncated CGF is
not globally bounded by $V_Bu^2/2$ in this direction, but Lin--Niu source
lines 1537--1554 give, uniformly for the present tilts
$u=O_{p,C}(D^{-1})$,

$$
K_i(u)\le\frac{u^2}{2}
\left(V_i+O_{p,C}(D^{-1})\right).
$$

Repeating Steps 1--5 therefore gives

$$
\log\mathfrak R^{B}_{0,r}-\log\mathfrak H^{B}_{0,r}
\le
-\frac{(1+\gamma_B)a^4}{8(1-p)^4}\frac{r^4}{d}
+O_{p,C}\left(\frac{r^4}{Dd}+\frac{r^3}{d}\right).
\tag{22}
$$

This is **[DERIVED]** only in the fixed-$C$ order of limits. In the optimized
large-$C$ HMS appendix, the blue constraint
$d\ge4Q_D|\lambda_B|C\ell$ may prevent taking $Q_D\to\infty$ at the
appendix's minimal $D$; no large-$C$ uniform blue claim is made here.

### Step 7: removing the perfect-event star

For the Ramsey applications $r=\Theta_C(\ell)$. If greedy extraction drops
$u$ vertices, the loss in the new deficit is

$$
\mathsf D_r-\mathsf D_{r-u}
=O_{p,C}\left(\frac{r^3u}{d}\right)
=O_{p,C}\left(\frac{\ell u}{D^2}\right).
\tag{23}
$$

HMS source lines 385--440 charge every discarded vertex
$\Omega_{p,C}(\ell)$ in the log probability. For sufficiently large fixed
$D$, this dominates (23). The same union bound therefore gives

$$
\log\mathfrak R_{r}-\log\mathfrak H_{r}
\le-\mathsf D_r+o_\ell(r^4/d)
\tag{24}
$$

for the corresponding unconditional source ledgers. Thus extraction does
not reopen the paired gap.

## What exactly has and has not been compared

### Proven comparator

$\mathfrak H$ in (15) is a **source-faithful frozen HMS main-body ledger**:
it follows the same reverse induction, uses the exact pre-Cauchy $A_i$, and
then fixes one uniform constant for the source's generic errors. Equation
(21) compares two bounds on the same probability using this same ledger.

This is enough to repair the missing paired pathwise lemma in
EXACT_COMPANION_AUDIT.md. It also shows that, against this comparator, the
correct saving is $1+\gamma$, not merely $\gamma$.

### Earliest remaining mismatch with the claimed final comparator

It is **not** enough to identify (15) with the final quantity called
$\rho_{\rm HMS}(D)$ in Lin--Niu.

1. HMS main-body Proposition 4.4 records only an unspecified
   $O(r^4/d+r)$; it does not select a unique constant $K$, a unique
   second-order exponent, or a best $\varepsilon_{\rm HMS}$.
2. Lin--Niu lines 1127--1173 choose an unspecified $K$ and define a bound
   exponent from its right-hand side. Their lines 1200--1208 then give the
   wrong HMS local coefficient, so their assertion that the same $K$ has
   already been coupled is unsupported. The present proof supplies such a
   coupling, but for the explicitly frozen ledger (15).
3. The earliest *definitional* mismatch is Lin--Niu lines 1127--1173: their
   symbol $\rho_{\rm HMS}$ is built from an unspecified $K$, so it does not
   name a unique source quantity to which (15) could be equal. The first
   *proof-route* divergence occurs at HMS line 940: its
   explicit large-$C$ theorem switches to an optimized appendix proof with
   different red/blue perfectness events and different induction functions.
   Lin--Niu lines 1422--1433 import those appendix parameters into their
   main-body fixed-$C$ expansion without an appendix-compatible paired
   ledger or uniform error proof.

Accordingly, the exact minimal bridge for a theorem-level comparison is:

> **Comparator bridge [OPEN].** Define the published HMS reference exponent
> $\rho_{\rm HMS}^{\rm pub}(D)$ unambiguously. Prove, for the same $p,D$ and
> the same red/blue appendix ledgers, that
>
> $$
> \rho_{\rm HMS}^{\rm ledger}(D)
> \ge
> \rho_{\rm HMS}^{\rm pub}(D)-o(D^{-2})
> \tag{25}
> $$
>
> in the fixed-$C$ comparison (with the corresponding $C$-dependent scale
> in the large-$C$ appendix regime).

Once (25) is fixed, (21), the already proved transverse-crossing lemma, and
the common blue ledger would yield a strict improvement over that specified
reference. Without (25), the phrase “larger than the HMS constant” has no
unique mathematical comparator.

## Compound-deficit interpretation

The transferable mechanism is a group charge, not independent error
subtraction. At exposure step $s$, all future conditional means share the
single forced deficit

$$
\Delta_s(M[s-1])
=\frac{\lambda^2}{d}
\sum_i\left(1-\frac{P_DV_i}{2}\right)A_i^2.
$$

It is first evaluated on the same history and only then replaced by its
uniform lower bound $\mathsf d_k$. This is analogous to a forced hitting
group in a finite construction: shared witnesses must be charged together
before residual budget is distributed among local repairs.

## Reproducibility

[paired_companion_check.py](./paired_companion_check.py) verifies the exact
finite sum (20) and numerically checks the local identity (8) and its uniform
deficit lower bound on deterministic perturbed histories. It is a sanity
check, not part of the proof.

Run:

```bash
python3 routes/lower/paired_companion_check.py
```

## Final verdict

1. **[DERIVED]** The paired pathwise companion induction does close for
   fixed $p,C$ when the exact $A_i$ are retained until the two local moment
   envelopes are subtracted.
2. **[DERIVED]** The propagated saving against the frozen HMS source ledger
   has coefficient $(1+\gamma_R)a^4/(8p^4)$, with the fixed-$C$ blue analogue
   $(1+\gamma_B)a^4/[8(1-p)^4]$.
3. **[DERIVED]** Same-order history errors are harmless only because they
   enter one common ledger; estimating them separately would not prove a
   coefficient gain.
4. **[OPEN]** The frozen main-body ledger has not been identified with a
   unique final published $\rho_{\rm HMS}(D)$ or with the optimized HMS
   appendix constant. No new Ramsey-number lower bound is claimed.
