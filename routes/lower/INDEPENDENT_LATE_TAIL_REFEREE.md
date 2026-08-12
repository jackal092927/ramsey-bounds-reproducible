# Independent adversarial review: late-tail and weighted obstruction

Date: **2026-08-12**

Reviewed artifacts:

- `LATE_TAIL_WEIGHTED_AUDIT.md`, SHA-256
  `b7f2315037b1c4734e0c59a7b737f992edbb268c5d612064e94c3b932b8efe71`;
- `late_tail_weighted_check.py`, SHA-256
  `ae29d6c17502375b79b358fde7d85b17536778890831fbca7b1af8125f72ec06`;
- imported rank-zero lemma in `TRANSVERSE_ENCODING_ATTEMPT.md`, SHA-256
  `abc50f95fd2f4674de5151283708bf2c47bbfc0d3affc39c65d4e62ec21bb16c`.

Primary-source comparison: Bradač,
[arXiv:2605.28793v3](https://arxiv.org/abs/2605.28793v3).  I independently
downloaded the v3 source and obtained SHA-256
`90acf52f3766e780bc22114e08aa46b115cfe86e33d340e7f7eace01bb7fe39f`
for `main.tex`, matching the reviewed document.  The relevant source lines
are 412 (definition of a forward-independent tuple), 553 (definition of
$D^*$), and 581--623 (Claim 2.13 and its use).

## Verdict

**PASS AS STATED, WITH THE CLAIM BOUNDARIES ALREADY WRITTEN IN THE DRAFT.**

I found no fatal gap in the type-resolved fanout, the typewise contraction,
the state-conditioned suffix bound, the arbitrarily delayed unmarked child,
the abstract-tree black-box obstruction, or the positive-potential terminal
range obstruction.

There is therefore no “earliest gap” to report.  The first plausible failure
point is Lemma 1's summation over rank $r$: if children of one type were
summed without conditioning on $ell_r=\ell$, the bound would be invalid.
The draft conditions correctly, uses the source maximizer separately at each
$r$, and obtains the claimed geometric sum.  The next plausible failure
point is Proposition 4's repeated tuple: repetition is legal under the
source's literal $V(D^*)^k$ definition, remains consistent, is poor, and
leaves the state unchanged.

This verdict certifies a mechanism analysis, not a new Ramsey bound.  In
particular, Proposition 5 concerns only what follows from the two numerical
outputs of Claim 2.13, and Proposition 6 excludes only the explicitly stated
positive scalar potential plus a uniform terminal lower bound.  The actual
$D^*$ tuple bound at the proposed $q\log q$ threshold remains open.

## 1. Source-definition alignment

The source defines a forward-independent $k$-tuple as an element of
$V(D)^k$, not as a tuple of distinct vertices.  It prohibits an arc only
between positions $i<j$.  Thus repeated vertices are allowed whenever the
repeated vertex has no loop in $D$.  For

$$
v=(a,b)\in V(D^*),\qquad a\perp b,
$$

the definition of $D^*$ would require both $a\perp b$ and
$a\not\perp b$ for an arc $(v,v)$, so $D^*$ has no such loop.  Repeating
$(a,b)$ is consequently legal in the actual tuple tree.

The reviewed document also has the correct orientation of consistency:
for an old pair $(a_i,b_i)$ and a new pair $(a,b)$, the condition is

$$
a_i\perp b\quad\Longrightarrow\quad a\perp b_i.
$$

Its definitions of

$$
W^\sigma(y)=\operatorname{span}\{b_i:a_i\perp y\},
\qquad r^\sigma(y)=\dim W^\sigma(y),
$$

$U_r$, $Z_r$, the maximizing layer $\ell_r^\sigma$, popular, poor, and
$\psi$ agree with source lines 585--617.  The threshold directions also
agree: poor is inclusive at $\le |Z_\ell|/(8q)$ and popular is inclusive at
$\ge |Z_\ell|/(16q)$, so an unmarked child is strictly above the former and
strictly below the latter.

## 2. Type-resolved fanout

Fix a source type $\ell$.  A child of that type has a unique rank
$r=r^\sigma(b)$ with $\ell\le r\le t$ and $\ell_r^\sigma=\ell$; rank
$t+1$ has no extension by source equation (7).  For each eligible $r$:

1. $b\in Z_r^\sigma$;
2. the maximizing definition of $\ell_r^\sigma$ gives
   $|Z_r^\sigma|\le |Z_\ell^\sigma|\le |U_\ell^\sigma|$; and
3. source equation (7) gives at most $2q^{t-r}$ choices of $a$ for each
   fixed $b$.

The $Z_r$ partition by rank, so no $b$ is counted twice.  Summing only over
the eligible ranks gives

$$
N_\ell(\sigma)
\le 2|U_\ell^\sigma|\sum_{r=\ell}^tq^{t-r}
\le4q^{t-\ell}|U_\ell^\sigma|.
$$

This verifies equation (2), including the factor $q^{t-\ell}$ that is easy
to lose if the $r$-sum is collapsed too early.

For the $j$-th earlier unmarked occurrence of the same type, source line 617
contracts $U_\ell$ by $\rho$.  Every intervening extension can only enlarge
each span $W(y)$, so every rank is nondecreasing and $U_\ell$ is
nonincreasing.  Starting from $|U_\ell^\varnothing|=N<2q^t$ therefore gives

$$
|U_\ell^\sigma|\le2q^t\rho^{j-1}.
$$

Multiplication over the positions of a fixed marked/type word yields exactly
equation (3).  Marked children need not be assigned a type, and their total
fanout is independently bounded by $h=A(t)q^t$, as used in the product.

The completion-of-the-square calculation in (10)--(12) is also correct.
Strictly, the one-sentence derivation of (12) uses both
$d_q\ge1/(32tq)$ and the immediate companion estimate
$d_q=O_t(1/q)$ from its explicit definition; the latter controls the
harmless $d_q/8$ term.  This is an omitted elementary phrase, not a proof
gap.

## 3. State saturation and suffix counting

If every $|U_\ell|\le2q^\ell$, Lemma 1 gives at most $8q^t$ unmarked
children of each type.  The unmarked children partition over the $t+1$
types, and adding the marked-child cap gives

$$
\bigl(A(t)+8(t+1)\bigr)q^t
$$

total children.  Monotonicity of all $U_\ell$ preserves the state condition
under every descendant, so iterating this one-step bound proves the suffix
bound.

After $m_\ell$ type-$\ell$ unmarked events, one has
$|U_\ell|\le2q^t\rho^{m_\ell}$.  The definition

$$
J_\ell=\left\lceil\frac{(t-\ell)\log q}{-\log\rho}\right\rceil
$$

therefore gives $\rho^{J_\ell}\le q^{-(t-\ell)}$ and hence
$|U_\ell|\le2q^\ell$.  This is a simultaneous, type-counter condition.
The draft never converts the sum of the $J_\ell$ into an absolute-depth
condition, so its quantifiers are correct.

## 4. Repeated tuple and delayed unmarked step

Take $a\perp b$.  At the root, all $W(y)$ are zero, so $(a,b)$ has
$r=\ell=0$, is not popular, and is not poor because
$|H_a|=[t]_q>N/(8q)$ for sufficiently large $q$.  It is unmarked.

After this child,

$$
W(y)=\langle b\rangle\quad(y\in H_a),
\qquad W(y)=0\quad(y\notin H_a).
$$

For another copy of $(a,b)$, all old-to-new consistency implications read
$a\perp b\Rightarrow a\perp b$ and therefore hold.  Moreover,

$$
r(b)=1,qquad Z_0=PG(t,q)\setminus H_a,qquad Z_1=H_a,
$$

with exact sizes $|Z_0|=q^t>[t]_q=|Z_1|$.  Thus $\ell_1=0$.  Since
$H_a\cap Z_0=\varnothing$, the repeated first coordinate $a$ is poor.
The repetition is marked.  Adding the same one-space $\langle b\rangle$
to a span already containing it changes no $W(y)$, so this argument repeats
for an arbitrary number $M$ of copies.

For $S=Z_0$, the balanced-hyperplane lemma supplies $H_c$ with
$|H_c\cap S|\ge p|S|/2>|S|/(8q)$.  Choosing
$d\in H_c\cap S$ gives $c\perp d$, while every old antecedent
$a\perp d$ is false because $d\in S$.  Thus the extension is consistent.
It has $r(d)=\ell=0$, is not popular because every $W(y)$ on $S$ is zero,
and is not poor by the strict displayed inequality.  It is unmarked at
depth $M+2$.

Hence the actual source-marked tree has unmarked vertices at arbitrarily
large absolute depths.  The draft correctly notes that this one delayed
path does not itself violate a global path-count bound.

## 5. Abstract-tree claim boundary

Proposition 5 fixes arbitrary constants $B,C>0$, takes

$$
w=\lfloor q\log q\rfloor,
\qquad \Delta=q^{2t-1},
\qquad k=\lceil Bq\log q\rceil,
$$

uses $\Delta$ unmarked children for the first $w$ levels, and $q^t$ marked
children thereafter.  This tree satisfies stronger caps than Claim 2.13
for any source constant $A(t)\ge1$, and its maximum degree is on the same
$q^{2t-1}$ scale as $|V(D^*)|$.

For $k\le w$, the base ratio is $q^{t-1}/C>1$.  For $k>w$, its logarithm is

$$
w(t-1)\log q-k\log C
= (t-1)q(\log q)^2-O_{B,C}(q\log q)>0.
$$

Thus the counterexample is valid for every fixed $B,C$ and sufficiently
large $q$.  It disproves an inference from only $(h,w)$; it is not claimed
to be a subtree of $D^*$ or a counterexample to a Ramsey theorem.  The draft
states this boundary repeatedly and correctly.

## 6. Positive-potential quantifiers

On the rank-zero family $\mathcal F_q$, suppose $\Phi>0$, the root has
weight one, $B_t$ is independent of $q$, and the local child sums satisfy

$$
\sum_{\tau\text{ child of }\sigma}\Phi(\tau)
\le B_tq^t\Phi(\sigma).
$$

Summing this inequality level by level gives total leaf weight at most
$(B_tq^t)^{k_q}$.  The independently audited leaf lower bound

$$
L_q^{1/k_q}\ge\frac3{16}q^{t+9(t-1)/10}
$$

then forces at least one leaf below the average, exactly as in the first
inequality of (17).  For fixed $B_t$ and sufficiently large $q$,

$$
\log(16B_t/3)\le\frac{t-1}{10}\log q,
\qquad
k_q\ge\frac{t-1}{13}q\log q,
$$

and the resulting coefficient is stronger than the claimed $1/20$.

The conclusion excludes combining this local contraction with a **uniform
per-leaf** lower bound
$\Phi(\tau)\ge\exp(-D_tq\log q)$, for fixed $D_t$.  It does not exclude
average-only recovery, signed or vector weights, cancellation outside the
positive scalar framework, or recovery on a later controlled tail.  These
are precisely the limitations recorded in the draft, so no quantifier is
being silently strengthened.

## 7. Executable audit

The supplied script compiled and its default grid returned

```text
late-tail weighted arithmetic checks: PASS
```

I also ran its four checks over an expanded grid
$2\le t\le12$ and prime-power values including
$3,4,5,8,9,16,25,27,49,81,125,257,1024,65536$, plus the large asymptotic
sentinel used by the script.  The expanded grid passed.  Separate exact
rational checks verified, for these dimensions and fields,

$$
[t+1]_q-[t]_q=q^t,qquad q^t>[t]_q,qquad
\frac{[t]_q}{[t+1]_q}>\frac3{4q}.
$$

As the draft explicitly says, the script checks arithmetic only.  The
projective-incidence and tree arguments remain mathematical dependencies
and were audited above rather than delegated to the finite grid.

## Final claim boundary

- Equations (2)--(6) and Propositions 4--6 pass review.
- Absolute depth does not force saturation under the source marking.
- Claim 2.13's two numerical outputs alone cannot yield the proposed
  $q\log q$ path threshold.
- The specified positive scalar potential cannot have both
  $O_t(q^t)$ weighted fanout and uniformly recoverable
  $\exp(O_t(q\log q))$ terminal weights on the rank-zero family.
- None of these statements proves or disproves the actual long-tail tuple
  estimate for $D^*$, and none improves a Ramsey-number bound.
