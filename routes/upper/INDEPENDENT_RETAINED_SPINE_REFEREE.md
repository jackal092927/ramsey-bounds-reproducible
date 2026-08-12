# Independent adversarial referee report: retained-spine transfer

Date: 2026-08-12

## Verdict

```text
PASS AFTER MINOR CORRECTIONS (RESOLVED)
STRICT QUALITATIVE IMPROVEMENT: PROVABLE AS STATED
NEW DECIMAL BASE: NOT CERTIFIED
```

I found no fatal gap in the retained-spine transfer.  Conditional on the
frozen uniform $P_6$ off-diagonal rate and the Yang--Mao v1 regularization,
correlation, and book theorems, the reviewed argument proves that the explicit
constant

$$
C_*=max_{\sigma\in[0,1]^2}\min\{D(\sigma),B(\sigma)\}
$$

satisfies

$$
R(k,k)\le \exp(C_*k+o(k)),
\qquad C_*<F_6(1).
$$

It is therefore legitimate to claim **existence of a strictly smaller
asymptotic base** $e^{C_*}<3.7806984277961236988\ldots$ without attaching a
decimal value to $e^{C_*}$.  A two-dimensional interval maximization is needed
for a certified decimal, but not for the strict qualitative conclusion.

The initially reviewed snapshot had one nonfatal boundary omission: the proof
of the direct-branch strictness divided by $a=1-\sigma_R$ at
$\sigma=(1,1)$, where $a=b=0$.  The current reviewed hash closes that point
separately by

$$
D(1,1)=2c_\eta<U(1).
$$

The current reviewed hash also names explicitly the imported correlation
property $\mathcal G_2^{(3)}(1/48,8\log432)$ and cites the source definition of
$D_r$.  Both requested corrections are therefore resolved, and the main
claim survives unchanged.

## Frozen materials

The reviewed workspace snapshot is pinned by

```text
5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa  RETAINED_SPINE_TRANSFER_ATTEMPT.md
b10815b10cb3ab922aa079ee74289c52239ec90939ed41b93907bf06a60ee274  check_retained_spine_transfer.py
8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8  certificate-higher-order-tetradecic-chain-v6.json
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
2f142a9371d29f07ffd68253c7dbb0981fe440f7f0b8284b4a81430f38395dbc  INDEPENDENT_PROOF_REPLAY.md
2881e8b1df310b449d0bffff5715b9176d9c191ba2a5d05bb376ab2843c58ccd  STAGE6_SEARCH.md
2bb40e6dc4f83203998adad57a0e922565bc8f6f07e1bdc810dd3ebfea481f5d  INDEPENDENT_STAGE6_REFEREE.md
```

I independently downloaded the TeX source of Yang--Mao,
[arXiv:2608.01962v1](https://arxiv.org/abs/2608.01962v1).  The exact source
used in this review has

```text
155b7104ec5b6935a576ae9f2b161976a966b0b46bd2b69153c0934ca688da2a  main.tex
```

The scalar replay used Python 3.11.15, `python-flint==0.9.0`, and 256-bit Arb
precision.

## Dependency map and exact source hypotheses

The transfer has four nontrivial imported inputs.

1. **Regularization.**  Yang--Mao source lines 318--332 give pairwise
   disjoint preliminary spines $S_1,S_2,W$, with

   $$
   |W|\ge\left(\frac{1+\eta}{2}\right)^{s_R+s_B}N,
   $$

   minimum color degrees at least $(1/2-\eta)|W|-1$, and all edges from
   $S_i$ into $W$ in color $i$.

2. **Correlation property and constants.**  Source lines 438--442,
   570--581, 699--716, and 795--824 define the exact constants.  For
   $r=2,d=3$,

   $$
   \theta_3=\frac\pi3,\quad
   \eta_3=\frac32,\quad
   \gamma_3=\frac12,
   $$

   and hence

   $$
   u_{2,3}
   =\max\left\{1,\frac{\log4}{3/2},\log432\right\}
   =\log432.
   $$

   Since $D_2=2\cdot2^{1}=4$, the theorem gives

   $$
   \beta_2=\frac1{4D_2(2+1)}=\frac1{48},
   \qquad C_{2,3}=4\cdot2\,u_{2,3}=8\log432.
   $$

   Thus the required property
   $\mathcal G_2^{(3)}(1/48,8\log432)$ really is available.  The primary
   note's source table should include lines 699--716, where $D_r$ is defined;
   the displayed specialization itself is correct.

3. **Parameterized book theorem.**  Source lines 1146--1190 require positive
   integers $t,m$, $0<p\le1$, $0<\delta\le\min\{p/4,1/4\}$,
   $\lambda_0\ge\max\{2,6\log(1/\delta)\}$, and

   $$
   t\ge\lambda_0\delta^{-1/(d-1)}.
   $$

   It also requires, for every color,

   $$
   |N_i(x)\cap Y_i|\ge p|Y_i|,
   \qquad
   |Y_i|\ge p^{-t}e^{\Pi t}m,
   $$

   together with

   $$
   |X|\ge 2rt\,e^{rt\Xi}.
   $$

   With $r=2$, this last condition is exactly
   $|X|\ge4t e^{2t\Xi}$.  The theorem returns a color-$i$ spine of exactly
   $t$ vertices and a page set of exactly $m$ vertices.  It does not require
   $X,Y_1,Y_2$ to be disjoint, and Yang--Mao themselves apply it with all
   three sets equal to $W$ at source lines 2258--2265.

4. **Off-diagonal interface.**  The frozen $P_6$ proof supplies, in the
   uniform epsilon sense,

   $$
   \log R(k,\ell)\le kU(\ell/k)+o(k)
   \qquad(1\le\ell\le k).
   $$

   Ramsey symmetry gives the homogeneous rate $\widehat U$ when both scaled
   parameters are linear.  If their maximum is sublinear, the classical
   Erd\H{o}s--Szekeres estimate is $o(k)$.  Splitting according as the larger
   Ramsey parameter is above or below the fixed threshold in the uniform
   epsilon statement proves

   $$
   \log R(\lfloor ak\rfloor,\lfloor bk\rfloor)
   \le k\widehat U(a,b)+o(k)
   $$

   uniformly on $[0,1]^2$ wherever the Ramsey parameters are positive.  The
   zero-coordinate appearances in the book formula represent the separately
   defined immediate-completion case $m_i=1$, not a use of an undefined
   Ramsey number $R(0,n)$.

## Adversarial replay of the branch structure

### 1. Why the minimum is the correct outer operation

After regularization, the same coloring and the same reservoir $W$ are
available to both proof strategies.  The direct argument and the book
argument are not uncontrollable outcomes of a random procedure.  The proof
may select whichever sufficient size threshold is smaller after observing
$(s_R,s_B)$.  Therefore

$$
\min\{D(\sigma),B(\sigma)\}
$$

is correct.  If the two thresholds tie, the proof takes the direct branch;
otherwise it takes the book branch.  These two cases are exhaustive.

The preliminary spine vector can depend adversarially on the coloring, so the
outer operation must be a maximum over $\sigma$.  Thus

$$
C_*=\max_\sigma\min\{D(\sigma),B(\sigma)\}
$$

has the correct max/min direction.

### 2. Why the maxima inside the book branch are necessary and sufficient

The book theorem may return either color.  For a red book, its page set must
have at least

$$
m_R=R(k-s_R-t,k-s_B)
$$

vertices unless $s_R+t\ge k$; the blue expression is symmetric.  Taking
$m=\max\{m_R,m_B\}$ therefore handles either color selected by the theorem.
This is exactly the maximum $M_\tau$ in the exponential rate.

The page-size and reservoir-size inequalities are simultaneous hypotheses of
the book theorem.  Their rate thresholds must consequently be combined as

$$
B(\sigma)=\max\{P(\sigma),Q(\sigma)\}.
$$

No max/min direction is reversed.

### 3. Exhaustion of the Ramsey coloring

In the direct branch, the uniform off-diagonal bound forces inside $W$ either
a red $K_{k-s_R}$ or a blue $K_{k-s_B}$, which extends with the corresponding
preliminary spine.

In the book branch, $B(\sigma)\le C_*$ implies both book size conditions.
The strict inequality

$$
p=0.46799<\frac12-\eta=0.468
$$

absorbs the regularization theorem's additive degree error once $|W|$ is
large.  The reservoir condition itself makes $|W|$ exponential, and
$t=\lfloor\tau k\rfloor$ eventually exceeds
$\lambda_0\delta^{-1/2}$.  Hence every source hypothesis is met with
$X=Y_R=Y_B=W$.

If the returned book color $i$ has $s_i+t\ge k$, its two spines already
contain a monochromatic $K_k$.  Otherwise, the page set has at least $m_i$
vertices.  Its induced coloring contains either the color-$i$ clique needed
to extend $S_i\cup T$, or the other-color clique needed to extend the other
preliminary spine.  Yang--Mao source lines 1571--1618 prove exactly these
compatibility statements.  Thus the direct/book case split exhausts every
red--blue coloring.

## Strictness and compactness

Let $c=c_\eta$, $a=1-\sigma_R$, and $b=1-\sigma_B$.  If $a\ge b$ and
$a>0$, concavity gives

$$
U(b/a)\le U(1)-U'(1)(1-b/a).
$$

Multiplication by $a$ and collection of terms yields

$$
U(1)-D(\sigma)
\ge
\sigma_R\bigl(U(1)-2c\bigr)
+(\sigma_B-\sigma_R)\bigl(U'(1)-c\bigr).
$$

The symmetric calculation handles $b\ge a$ with $b>0$.  The right side is
strictly positive away from the origin because both certified coefficients
are positive.  The only point excluded by the displayed ratio calculation is
$a=b=0$, namely $\sigma=(1,1)$; direct evaluation gives

$$
U(1)-D(1,1)=U(1)-2c>0.
$$

This is the minor boundary repair noted in the verdict.  If one of $a,b$ is
zero but not both, the same inequality follows by continuity from $U(0)=0$.

At the unique point where the direct threshold equals $U(1)$,
$\sigma=(0,0)$, the book threshold obeys

$$
P(0,0)=U(1-\tau)+\tau q
\le U(1)-\tau\bigl(U'(1)-q\bigr)<U(1)
$$

and

$$
Q(0,0)=2\tau\Xi<U(1).
$$

Thus $B(0,0)<U(1)$.  The homogeneous extension $\widehat U$ is continuous,
including at the axes and the origin, because $U(0)=0$; hence $D$, $B$, and
$\min(D,B)$ are continuous on the compact square.  Pointwise strictness plus
attainment of the maximum proves

$$
C_*<U(1).
$$

No numerical grid or sampled optimizer is required for this existence
argument.

## Uniformity, floors, and the asymptotic conclusion

The proof uses the uniform form of the off-diagonal $o(k)$ term.  This is
essential because $\sigma$ is selected by the coloring and may vary with
$k$.  The frozen $P_6$ replay supplies precisely this uniform epsilon
statement.

For the book branch, $t/k\to\tau$ and uniform continuity of $\widehat U$ on
the compact square convert both integer Ramsey parameters to $M_\tau$ with a
uniform $o(k)$ error.  Since
$q=\log(1/p)+\Pi>0$ and $\Xi>0$, replacing $\tau k$ by
$t=\lfloor\tau k\rfloor$ only makes the two required exponential factors
smaller up to the already absorbed subexponential prefactors.  The factor
$4t$ contributes only $o(k)$ to the logarithm.

For every fixed $\varepsilon>0$, the argument applies to
$N=\lceil e^{(C_*+\varepsilon)k}\rceil$ for all sufficiently large $k$.
Therefore

$$
\limsup_{k\to\infty}\frac1k\log R(k,k)\le C_*.
$$

This is equivalent to the asserted $\exp(C_*k+o(k))$ upper bound.  The ceiling
and all integer cutoffs change logarithms by $o(k)$ only.

## Scalar-checker replay

I reran `check_retained_spine_transfer.py` unchanged.  It returned

```text
PASS: retained-spine scalar transfer gates
P6 concavity upper:                         -0.3515456913371641
U(1)-2*c_eta:                                0.0066117348208444356...
U'(1)-c_eta:                                 0.10419085555390703...
U'(1)-(log(1/p)+Pi):                         0.0043688677990053810...
U(1)-2*tau*Xi:                               0.76039753828682979...
```

The script reads all fourteen $P_6$ coefficients as exact decimal strings.
Its formulas for $U$, $U'$, $\Pi$, $\Xi$, $\beta_2$, $C_{2,3}$, and $\rho$
match the source specializations above.  The imported concavity routine checks
the interval adjacent to zero using an analytic pole bound and covers
`[0.0001,1]` with 8,192 closed Arb cells.  Every proof-critical comparison is
an Arb interval comparison; the printed float is only a summary of an already
certified upper endpoint.

The script does **not** prove the Yang--Mao combinatorial theorems, the frozen
$P_6$ off-diagonal theorem, the branch transfer, compactness, or a numerical
upper bound for $C_*$.  The reviewed note does not ask it to do so.  Treating
the script as proof of any of those statements would be invalid; in the
current package it is used only for the scalar parameter gates and target
concavity.

## Resolved corrections and claim boundary

The current primary note resolves both requested changes:

1. lines 316--318 handle $\sigma=(1,1)$ directly before the ratio $U(b/a)$;
2. line 41 imports $\mathcal G_2^{(3)}(1/48,8\log432)$ and cites source lines
   699--716 defining $D_r$.

The note also retains the essential word **uniform** when importing the
off-diagonal $o(k)$ estimate.  Pointwise asymptotics would not suffice for
coloring-dependent spine sizes.

I approve only the following conclusion:

> There exists an explicitly defined constant $C_*<F_6(1)$ such that, under
> the pinned local $P_6$ proof boundary and the Yang--Mao v1 inputs,
> $R(k,k)\le\exp(C_*k+o(k))$.

I do not approve a decimal value for $e^{C_*}$, an explicit finite-$k$
threshold, a claim that this is published or externally peer reviewed, or a
claim of global novelty.  The remaining trust boundary includes the
Yang--Mao arXiv v1 theorems, the pinned local $P_6$ proof package, and Arb
containment through `python-flint==0.9.0`.
