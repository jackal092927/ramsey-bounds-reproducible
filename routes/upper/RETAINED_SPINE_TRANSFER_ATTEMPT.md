# Retained-spine transfer into the repaired two-colour rate descent

Date: 2026-08-12  
Scope: Yang--Mao arXiv:2608.01962v1 plus the frozen six-stage rate in this
workspace.

## Verdict

```text
exact retained-spine transfer lemma:       PROVABLE AS STATED
strict improvement C_* < F_6(1):           PROVABLE AS STATED
new decimal growth base:                   OPEN (no 2D Arb enclosure yet)
subtract -t^2/(64k) inside the old cells:  FALSE AS A PROOF STEP
```

The useful outcome is not a seventh polynomial stage.  There is a separately
closed outer transfer which combines the current off-diagonal rate with the
Yang--Mao preliminary spines and book theorem.  It defines an explicit
two-dimensional maximum $C_*$ and proves

\[
 R(k,k)\leq \exp\bigl(C_*k+o(k)\bigr),
 \qquad C_*<F_6(1).
\]

Thus the mechanism gives a **strict qualitative improvement** over the frozen
base $e^{F_6(1)}=3.7806984277961236988\ldots$, under the same local trust
boundary and the Yang--Mao inputs.  This note does not attach a decimal to
$e^{C_*}$: doing that requires a new two-dimensional Arb enclosure, not a
sampled optimization.

## Primary-source audit

The line references below are to `main.tex` in the v1 TeX source downloaded
from <https://export.arxiv.org/e-print/2608.01962v1>.

| Source lines | Imported statement | Use here |
|---:|---|---|
| 318--332 | Erdős--Szekeres regularization: preliminary colour spines $S_i$, common reservoir $W$, $|W|\ge ((1+\eta)/r)^s n$, and minimum colour degrees | produces the two retained spines and the reservoir cost |
| 570--581, 795--824 | explicit root-filter and correlation constants | specializes to $r=2,d=3$, $\beta=1/48$, $C_{2,3}=8\log 432$ |
| 699--716, 795--824, 1001--1010 | $D_r=r2^{r-1}$ and the resulting correlation property | imports $\mathcal G_2^{(3)}(1/48,8\log432)$ used by the book theorem |
| 1146--1190 | parameterized monochromatic book theorem | forces a $t$-spine in one of the two colours with a page set of prescribed size |
| 1569--1618 | compatibility of preliminary spines with the final book | extends a clique found in the page set to a $K_k$ |
| 1620--1739 | one-coordinate relative-entropy estimate | explains the Yang--Mao gain, but its crude multinomial rate is replaced here by the exact $F_6$ rate |
| 2155--2343 | retained-spine transfer in the paper's $r^{rk}$ normalization | model for the outer case split; not quoted as a fixed-$r$ numerical bound |

The workspace input is the exact rate

\[
 U(\lambda)=F_6(\lambda)=H(\lambda)+P_6(\lambda)e^{-\lambda},
 \qquad 0\leq\lambda\leq1,
\]

with the exact $P_6$ coefficients in `STAGE6_SEARCH.md`, lines 5--32.  The
six-stage theorem and its base are at lines 32--46.  The uniform one-sided
normalization and the need to handle both parameter orders are spelled out in
`INDEPENDENT_PROOF_REPLAY.md`, lines 174--201.  In particular, the frozen
proof supplies, uniformly for $1\leq \ell\leq k$,

\[
 \log R(k,\ell)\leq kU(\ell/k)+o(k).
\tag{1}
\]

## Current normalization

Extend $U$ continuously by $U(0)=0$, and define its symmetric homogeneous
extension on $[0,1]^2$ by

\[
 \widehat U(a,b)=
 \begin{cases}
  \max\{a,b\}\,
  U\!\left(\dfrac{\min\{a,b\}}{\max\{a,b\}}\right),
       &\max\{a,b\}>0,\\[2mm]
  0,&a=b=0.
 \end{cases}
\tag{2}
\]

Equation (1), Ramsey symmetry, and the classical bound in the sublinear
parameter range give

\[
 \log R(\lfloor ak\rfloor,\lfloor bk\rfloor)
 \leq k\widehat U(a,b)+o(k)
\tag{3}
\]

uniformly over $a,b\in[0,1]$.  Formula (2), rather than the Yang--Mao
multinomial $2^{(a+b)k}$, is the exact rate interface.

## Fixed book parameters

Interpret the following terminating decimals exactly:

\[
 \eta=0.032,\qquad p=0.46799,\qquad
 \delta=0.00001,\qquad \lambda_0=25000,
 \qquad \tau=0.00005.
\tag{4}
\]

For $r=2,d=3$, the Yang--Mao constants reduce to

\[
 u_{2,3}=\log432,qquad
 \beta_2=\frac1{48},\qquad
 C_{2,3}=8\log432,qquad
 \rho=\log96.
\tag{5}
\]

Put

\[
 L=\log(1/\delta),\qquad L_p=\log(1/p),
\]

\[
 \Pi=\frac{3\delta}{p}+\frac{6LL_p}{\lambda_0},
\qquad
 \Xi=2\rho+4C_{2,3}\lambda_0^{1/3}
       +\frac{12C_{2,3}L}{\lambda_0^{2/3}},
\tag{6}
\]

and abbreviate

\[
 c_\eta=\log\frac{2}{1+\eta},
 \qquad q=\log(1/p)+\Pi.
\tag{7}
\]

The exact scalar checker
`check_retained_spine_transfer.py` proves the book-theorem parameter gates,
strict concavity of the **target** $F_6$, and

\[
 2c_\eta<U(1),\qquad c_\eta<U'(1),\qquad
 q<U'(1),\qquad 2\tau\Xi<U(1).
\tag{8}
\]

Its 256-bit Arb output is

```text
PASS: retained-spine scalar transfer gates
P6 concavity upper: -0.3515456913371641
U(1):                         1.3299087618219930723187812632036105...
U'(1):                        0.7658393690544813503003599036437724...
c_eta:                        0.6616485135005743183514223708683667...
U(1)-2*c_eta:                 0.0066117348208444356159365214668770...
U'(1)-c_eta:                  0.1041908555539070319489375327754057...
Pi:                           0.0021621504413293968514178757379833...
q=log(1/p)+Pi:                0.7614705012554759692723091291774390...
U'(1)-q:                      0.0043688677990053810280507744663334...
Xi:                           5695.1122353516327721007501909253779...
U(1)-2*tau*Xi:                0.7603975382868297951087062441110727...
```

The large value of $\Xi$ makes the eventual finite-$k$ threshold enormous, but
it does not prevent a strict asymptotic transfer.

## Candidate transfer lemma

Let $\sigma=(\sigma_R,\sigma_B)\in[0,1]^2$ encode the preliminary red and
blue spine sizes divided by $k$.  Define the direct-prior branch

\[
 D(\sigma)=c_\eta(\sigma_R+\sigma_B)
 +\widehat U(1-\sigma_R,1-\sigma_B).
\tag{9}
\]

For the book branch, define the largest remaining page exponent

\[
 \begin{aligned}
 M_\tau(\sigma)=\max\bigl\{&
 \widehat U((1-\sigma_R-\tau)_+,1-\sigma_B),\\
 &\widehat U(1-\sigma_R,(1-\sigma_B-\tau)_+)
 \bigr\},
 \end{aligned}
\tag{10}
\]

where $x_+=\max\{x,0\}$.  A zero first coordinate in (10) means that the
preliminary spine plus the final $t$-spine already has size at least $k$,
so no page clique is required in that colour.  Set

\[
 P(\sigma)=c_\eta(\sigma_R+\sigma_B)+\tau q+M_\tau(\sigma),
\tag{11}
\]

\[
 Q(\sigma)=c_\eta(\sigma_R+\sigma_B)+2\tau\Xi,
 \qquad B(\sigma)=\max\{P(\sigma),Q(\sigma)\},
\tag{12}
\]

and finally

\[
 \boxed{
 C_*=\max_{\sigma\in[0,1]^2}
       \min\{D(\sigma),B(\sigma)\}.}
\tag{13}
\]

### Lemma (retained-spine transfer)

If $U$ satisfies (1), the Yang--Mao regularization and book theorems hold
with the parameters (4)--(7), and $C_*$ is defined by (13), then

\[
 \boxed{R(k,k)\leq\exp(C_*k+o(k)).}
\tag{14}
\]

### Proof

Fix $\varepsilon>0$, take
$N=\lceil\exp((C_*+\varepsilon)k)\rceil$, and consider
an arbitrary red--blue colouring of $K_N$.  Apply Yang--Mao regularization
with parameter $\eta$.  If a preliminary spine already has at least $k$
vertices, we are done.  Otherwise write

\[
 s_R=\sigma_Rk,\qquad s_B=\sigma_Bk
\]

up to the harmless integer rounding.  The common reservoir satisfies

\[
 \log|W|\geq
 (C_*+\varepsilon)k-c_\eta(s_R+s_B)+o(k).
\tag{15}
\]

At this particular $\sigma$, choose the smaller of the two branches in (13).

**Direct branch.**  If $D(\sigma)\leq B(\sigma)$, then
$D(\sigma)\leq C_*$.  Equations (3), (9), and (15), with the fixed
$\varepsilon$-margin absorbing the uniform $o(k)$, imply

\[
 |W|\geq R(k-s_R,k-s_B)
\]

for all sufficiently large $k$.  A red $K_{k-s_R}$ in $W$ extends
with $S_R$, and a blue $K_{k-s_B}$ extends with $S_B$.  Either outcome
gives a monochromatic $K_k$.

**Book branch.**  Suppose $B(\sigma)<D(\sigma)$.  Put
$t=\lfloor\tau k\rfloor$ and define

\[
 m_R=\begin{cases}
  1,&s_R+t\geq k,\\
  R(k-s_R-t,k-s_B),&s_R+t<k,
 \end{cases}
 \qquad
 m_B=\begin{cases}
  1,&s_B+t\geq k,\\
  R(k-s_R,k-s_B-t),&s_B+t<k.
 \end{cases}
\]

Set $m=\max\{m_R,m_B\}$.  Uniformity of (3), continuity of
$\widehat U$, and $t/k\to\tau$ give

\[
 \log m\leq kM_\tau(\sigma)+o(k).
\tag{16}
\]

The inequalities $P(\sigma)\leq C_*$ and $Q(\sigma)\leq C_*$, together
with (15)--(16), imply for all sufficiently large $k$

\[
 |W|\geq p^{-t}e^{\Pi t}m,
 \qquad
 |W|\geq4t\,e^{2t\Xi}.
\tag{17}
\]

Because $p<1/2-\eta$ and the second bound in (17) is exponential, the
regularization degree estimate

\[
 |N_i(w)\cap W|\geq(1/2-\eta)|W|-1
\]

is at least $p|W|$ for every $w\in W$ and both colours.  Also
$t\geq\lambda_0\delta^{-1/2}$ eventually.  All hypotheses of the Yang--Mao
book theorem therefore hold with $X=Y_R=Y_B=W$.  It returns a colour-$i$
$t$-spine $T\subseteq W$ and a page set $P_0\subseteq W\setminus T$
of size $m$.

If $s_i+t\geq k$, then $S_i\cup T$ already contains a colour-$i$
$K_k$.  Otherwise, $|P_0|\geq m_i$, so $P_0$ contains either the
required colour-$i$ clique or the required clique in the other colour.
Yang--Mao spine compatibility extends it with the corresponding preliminary
spine (and with $T$ in colour $i$) to a $K_k$.

Both branches give a monochromatic $K_k$.  Since $\varepsilon$ was arbitrary, (14)
follows. \(\square\)

## Why the transfer is strictly improving

The strict inequality does not require a sampled optimizer.

First, $D(\sigma)<U(1)$ for every $\sigma\ne(0,0)$.  At the endpoint
$\sigma=(1,1)$ this follows directly from
$D(1,1)=2c_\eta<U(1)$.  At every other nonzero $\sigma$, put
$a=1-\sigma_R$, $b=1-\sigma_B$, and assume $a\geq b$.  Then
$\sigma_R\leq\sigma_B$.  Concavity of $U$ gives

\[
 U(b/a)\leq U(1)-U'(1)(1-b/a).
\]

Substitution into (9) yields the quantitative bound

\[
 \begin{aligned}
 U(1)-D(\sigma)
 \geq{}&\sigma_R\bigl(U(1)-2c_\eta\bigr)\\
 &+(\sigma_B-\sigma_R)\bigl(U'(1)-c_\eta\bigr)>0
 \end{aligned}
\tag{18}
\]

unless $\sigma=(0,0)$.  The opposite order is symmetric.  Both coefficients
in (18) are strictly positive by (8).

At the unique point where the direct branch is not strict,

\[
 P(0,0)=U(1-\tau)+\tau q.
\]

Concavity again gives

\[
 U(1)-U(1-\tau)\geq\tau U'(1),
\]

and hence

\[
 P(0,0)\leq U(1)-\tau\bigl(U'(1)-q\bigr)<U(1).
\tag{19}
\]

The other book requirement satisfies

\[
 Q(0,0)=2\tau\Xi<U(1)
\tag{20}
\]

by (8).  Therefore $B(0,0)<U(1)$.

The functions $\widehat U,D,B$ are continuous on the compact square
$[0,1]^2$.  At the origin, the book branch is strictly below $U(1)$ by
(19)--(20); everywhere else, the direct branch is strictly below $U(1)$ by
(18).  Thus

\[
 \min\{D(\sigma),B(\sigma)\}<U(1)
 \quad\text{for every }\sigma\in[0,1]^2.
\]

Compactness now gives the strict global inequality

\[
 \boxed{C_*<U(1)=F_6(1).}
\tag{21}
\]

Combining (14) and (21) proves the stated qualitative improvement.

## Exact interface for a future Arb enclosure

No new combinatorial idea is needed to obtain a decimal.  The numerical task
is exactly the following:

1. evaluate (2), (9)--(12) with the exact P6 coefficients and fixed parameters
   (4)--(7);
2. partition $[0,1]^2$ into exact rational rectangles;
3. on each rectangle, certify an upper bound for at least one of $D$ or
   $B$, and hence for their minimum;
4. take the largest certified rectangle bound $C_{\rm Arb}$;
5. require the single final sign $C_{\rm Arb}<F_6(1)$.

The branch minimum is helpful: near $\sigma=0$, certify $B$; away from the
origin, (18) is already an analytic upper bound for $D$.  Consequently a
full square grid is unnecessary.  A small book-controlled neighbourhood of
the origin plus the analytic direct bound should suffice.

A floating diagnostic with the parameters (4) placed the apparent worst
point on an axis about $10^{-6}$ from the origin and suggested an exponent
gain of order $10^{-7}$.  This is only a construction hint.  It is not used
in (14) or (21), and it is not a reported Ramsey base.

## Why the naive splice is invalid

Yang--Mao's displayed factor

\[
 \exp(-t^2/(64k))
\]

comes after three operations: preliminary-spine regularization, production
of a final $t$-book, and an off-diagonal bound inside its page set.  The
existing P6 JSON cells encode a different one-dimensional GNNW BookCor
witness.  They do not record preliminary spine sizes, a common two-colour
minimum-degree reservoir, or the Yang--Mao page/reservoir costs.  Therefore
subtracting $t^2/(64k)$ from $F_6$, or adding it to an existing cell slack,
does not follow from either proof.

The first valid interface is (13): an outer two-variable choice between a
direct off-diagonal use of $U$ and the retained-spine book use of $U$.

## Self-audit and claim boundary

1. **No numerical overclaim.**  The theorem is $C_*<F_6(1)$, with $C_*$
   explicitly defined by (13).  No decimal for $C_*$ is certified here.
2. **No seventh descent.**  The P6 rate is used as a frozen prior; its
   coefficients are not fitted or modified.
3. **Target concavity checked.**  Earlier stage-6 verification needed P5
   concavity as the prior.  The new scalar checker separately proves P6
   concavity, which is the property used in (18)--(19).
4. **The `-1` degree term is absorbed.**  We choose the strict
   $p<1/2-\eta$; the book branch forces $|W|$ exponential, so the additive
   `-1` is harmless for sufficiently large $k$.
5. **Floors are asymptotic only.**  Replacing $\tau k$ by
   $t=\lfloor\tau k\rfloor$ changes (10)--(12) by $o(1)$, using uniform
   continuity of $\widehat U$.
6. **Trust boundary.**  The result inherits the local P6 proof boundary,
   python-flint/Arb containment semantics, and the Yang--Mao v1
   regularization, correlation, and book theorems.  It has not received an
   independent referee replay or proof-assistant formalization.

## Reproduction

From `routes/upper`:

```text
../../.venv/bin/python check_retained_spine_transfer.py
```

The checker proves every scalar sign used in the strict compactness argument.
It intentionally does not print or certify a new growth base.
