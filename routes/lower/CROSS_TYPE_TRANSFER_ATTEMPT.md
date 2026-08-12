# Proof package: exact cross-type transfer after Claim 2.13

Date: 2026-08-12  
Primary source: Bradač,
[arXiv:2605.28793v3](https://arxiv.org/abs/2605.28793v3), source
`main.tex`, SHA-256
`90acf52f3766e780bc22114e08aa46b115cfe86e33d340e7f7eace01bb7fe39f`.

## Claim

Fix $t\geq2$ and a prime power $q$.  Use exactly the consistent-tuple tree,
state $W^\sigma(y)$, ranks $r^\sigma(y)$, layers $Z_j^\sigma$, cutoffs
$U_j^\sigma$, and marking rule in Bradač Claim 2.13.  This document resolves
the first proposed cross-type cut and leaves the genuinely nonlocal version
open.

1. **Exact rank-layer transfer.**  If $(a,b)$ legally extends $\sigma$, put

   $$
   R_j^\sigma(a,b)=
   \{y\in Z_j^\sigma:y\perp a,\ b\not\subseteq W^\sigma(y)\},
   \qquad 0\leq j\leq t.
   \tag{1}
   $$

   Then

   $$
   U_j^{\sigma(a,b)}=U_j^\sigma\setminus R_j^\sigma(a,b)
   \qquad(0\leq j\leq t).
   \tag{2}
   $$

   Thus a point promoted from rank $j$ to rank $j+1$ leaves exactly the
   cutoff $U_j$; nesting of the $U_j$ does not make that point leave any
   other cutoff.

2. **What unmarkedness certifies.**  If the child is unmarked and its source
   type is $\ell=\psi(\sigma(a,b))$, Claim 2.13 certifies

   $$
   |R_\ell^\sigma(a,b)|\geq \frac{|Z_\ell^\sigma|}{16q}.
   \tag{3}
   $$

   It gives no positive lower bound for any $R_j$ with $j\ne\ell$.  In
   particular, the proposed universal statement that every unmarked step
   contracts two or more of the $U_j$ is false.

3. **No forced diversification before the explicit rank-zero threshold.**  The rank-zero family
   already proved in
   [TRANSVERSE_ENCODING_ATTEMPT.md](./TRANSVERSE_ENCODING_ATTEMPT.md)
   contains $\Theta_t(q\log q)$ consecutive unmarked steps all having
   $\psi=0$, with prefix entropy
   $\exp(\Omega_t(q(\log q)^2))$ beyond a $C_tq^t$ base.  Hence no argument
   can force the unmarked steps to spread among the $t+1$ source types before
   the explicit length $k_q=\lfloor(t-1)q\log q/12\rfloor$.  This does
   **not** rule out eventual diversification by $A_tq\log q$ for a larger
   constant $A_t$, nor assert that the same steps have $R_j=\varnothing$ for
   every $j>0$.

4. **Strong marked/unsaturated mutual exclusion is false.**  There are
   states with $|U_0|=q^t$ and at least $[t]_q=\Theta_t(q^{t-1})$ marked
   children.  One of those children is state-neutral and can be repeated
   arbitrarily.  A stronger quantitative tradeoff capable of saving the
   remaining logarithm is not proved or disproved here.

5. **The exact transfer operator lives on the full $W$-state.**  The map
   $y\mapsto W^\sigma(y)$ determines all legal children and their successor
   states.  The vector $(|U_0|,\ldots,|U_t|)$ does not contain the incidence
   data appearing in (1), so (2) is not a closed transfer rule on that
   vector.  Any successful reduction to a smaller vector state must prove a
   new lumping or domination inequality; it cannot follow from nesting
   alone.

## Status

- **Exact transfer identities (1)--(2):** **PROVABLE AS STATED**.
- **Unmarked certificate (3):** **PROVABLE AS STATED**.
- **Every unmarked step contracts multiple cutoff layers:** **FALSE AS
  STATED**, already at the root.
- **The $U_j$ nesting itself supplies additive cross-type contraction:**
  **FALSE AS STATED**.
- **Unmarked source types must diversify before
  $k_q=\lfloor(t-1)q\log q/12\rfloor$:** **FALSE**, by the audited rank-zero
  family.  **Eventual diversification by $A_tq\log q$ for some larger
  constant $A_t$:** **OPEN / NOT CURRENTLY JUSTIFIED**.
- **An unsaturated state has no marked or no state-neutral child:** **FALSE
  AS STATED**.
- **A quantitative inverse relation between marked fanout and unsaturated
  layer sizes:** **OPEN / NOT CURRENTLY JUSTIFIED**.
- **A closed, constant-dimensional transfer inequality strong enough to
  replace the $O_t(q(\log q)^2)$ prefix loss by $O_t(q\log q)$:** **OPEN /
  NOT CURRENTLY JUSTIFIED**.
- **The tuple bound at $k\geq A_tq\log q$ and the corresponding Ramsey
  lower bound with one fewer logarithm:** **NOT CURRENTLY JUSTIFIED**.

## Assumptions

- Projective points are the $1$-spaces of
  $V=\mathbb F_q^{t+1}$ with the source's nondegenerate bilinear form.
- A history
  $\sigma=(a_1,b_1,\ldots,a_m,b_m)$ is *consistent* when
  $a_i\perp b_i$ and, for $i<j$,
  $a_i\perp b_j$ implies $a_j\perp b_i$.
- The source state and rank are

  $$
  W^\sigma(y)=\operatorname{span}\{b_i:a_i\perp y\},
  \qquad r^\sigma(y)=\dim W^\sigma(y).
  \tag{4}
  $$

- $U_j^\sigma=\{y:r^\sigma(y)\leq j\}$,
  $Z_j^\sigma=U_j^\sigma\setminus U_{j-1}^\sigma$, and
  $U_{-1}=\varnothing$.
- $[d]_q=(q^d-1)/(q-1)$ denotes the number of projective points in a
  $d$-dimensional vector space; $[0]_q=0$.

## Source alignment

| v3 `main.tex` lines | source item | use below |
|---:|---|---|
| 553 | definition of $D^*(t,q)$ | legal vertices |
| 581--585 | consistent tuples | Lemma 1 |
| 587--595 | $W^\sigma$, rank, fixed-$b$ extensions | Lemmas 1 and 5 |
| 597--603 | $U_j$, $Z_j$, $\ell_r$, popular | unmarked type |
| 605--615 | poor children | Proposition 4 |
| 617 | certified contraction and $\psi$ | Corollary 2 |
| 619--623 | path count using the unmarked cap | claim boundary |

No transition or monotonicity stronger than these literal definitions is
imported.

## Notation

- Write $\sigma'=\sigma(a,b)$ for a legal extension.
- Put $H_a=\{y:y\perp a\}$.
- The *full state* is

  $$
  \mathcal W(\sigma)=(W^\sigma(y))_{y\in PG(t,q)}.
  \tag{5}
  $$

- For coefficients $c_0,\ldots,c_t$, define the linear cutoff statistic

  $$
  \Phi_{\mathbf c}(\sigma)=\sum_{j=0}^t c_j|U_j^\sigma|.
  \tag{6}
  $$

## Proof strategy

Compute the transition point by point rather than bounding one selected
coordinate.  This exposes the exact diagonal flow between adjacent rank
layers.  Then test the desired multi-layer conclusion at the root, where all
points have rank zero.  Next import the audited rank-zero family only for its
literal source-type and entropy conclusions.  Finally, use one unmarked
root extension followed by poor extensions to test the proposed
marked/unsaturated exclusion and identify the full Markov state.

## Dependency map

1. Lemma 1 uses only definition (4).
2. Corollaries 2 and 3 use Lemma 1; Corollary 2 additionally uses the
   non-poor/non-popular inequalities on source line 617.
3. Proposition 4 uses the root state and the exact poor definition.
4. Proposition 5 imports the independently audited rank-zero construction
   and makes no stronger statement about its higher-rank removal sets.
5. Lemma 6 uses consistency and Lemma 1 to define the exact transfer
   operator.

## Proof

### Lemma 1: exact adjacent-rank flow

For every legal extension $\sigma'=\sigma(a,b)$ and every projective point
$y$,

$$
W^{\sigma'}(y)=
\begin{cases}
W^\sigma(y)+\langle b\rangle,&y\perp a,\\
W^\sigma(y),&y\not\perp a.
\end{cases}
\tag{7}
$$

Consequently

$$
r^{\sigma'}(y)=r^\sigma(y)+
\mathbf 1_{\{y\perp a,\ b\not\subseteq W^\sigma(y)\}}.
\tag{8}
$$

The sets in (1) satisfy (2), and the rank layers obey

$$
\begin{aligned}
Z_0^{\sigma'}&=Z_0^\sigma\setminus R_0,\\
Z_j^{\sigma'}&=(Z_j^\sigma\setminus R_j)\mathbin{\dot\cup}R_{j-1}
&& (1\leq j\leq t),\\
Z_{t+1}^{\sigma'}&=Z_{t+1}^\sigma\mathbin{\dot\cup}R_t.
\end{aligned}
\tag{9}
$$

**Proof.**  Definition (4) says that the new second coordinate $b$ is added
to $W(y)$ precisely when the new first coordinate satisfies $a\perp y$.
This proves (7).  Adding one vector either preserves the span or raises its
dimension by exactly one, proving (8).

Fix $j\in\{0,\ldots,t\}$.  A point of old rank below $j$ has new rank at
most $j$ and remains in $U_j$.  A point of old rank exactly $j$ leaves
$U_j$ precisely when the indicator in (8) equals one, which is precisely
membership in $R_j$.  A point of old rank above $j$ cannot enter $U_j$.
This proves (2).  Sorting the same pointwise alternatives by their new rank
gives the disjoint unions in (9). $\square$

The key consequence is that nesting does not create a cascade through the
cutoffs.  If a point of rank $j$ is promoted, it leaves $U_j$ but remains in
$U_{j+1},\ldots,U_t$.  One step can shrink several $U_j$ only by promoting
different points in different old rank layers.

### Corollary 2: exact linear vector-potential change

For arbitrary real coefficients $c_0,\ldots,c_t$,

$$
\Phi_{\mathbf c}(\sigma')
=\Phi_{\mathbf c}(\sigma)-\sum_{j=0}^t c_j|R_j^\sigma(a,b)|.
\tag{10}
$$

If $\sigma'$ is unmarked with source type $\ell$, then (3) holds, so for
nonnegative coefficients (10) implies only the source-guaranteed estimate

$$
\Phi_{\mathbf c}(\sigma')
\leq\Phi_{\mathbf c}(\sigma)
-\frac{c_\ell|Z_\ell^\sigma|}{16q}.
\tag{11}
$$

**Proof.**  Sum (2) with coefficients $c_j$.  For an unmarked child, source
line 617 says that $a$ is not poor and $b$ is not popular on the selected
layer $Z_\ell$.  Subtracting the two incidence counts gives exactly (3),
as in the source.  Dropping the other nonnegative terms in (10) gives
(11). $\square$

Equation (10) is a useful exact identity, but (11) contains no new
cross-type gain.  A stronger result would need lower bounds on several
$R_j$ or an averaged correlation among them.

### Corollary 3: root counterexample to common cutoff contraction

At the empty history, every legal child $(a,b)$ is unmarked and has source
type zero.  Its exact transfer is

$$
R_0=H_a,
\qquad R_j=\varnothing\quad(1\leq j\leq t),
\tag{12}
$$

and therefore

$$
U_0'=PG(t,q)\setminus H_a,
\qquad U_j'=PG(t,q)\quad(1\leq j\leq t).
\tag{13}
$$

**Proof.**  At the root every $W(y)$ is zero and every point has rank zero.
For a vertex $(a,b)$ of $D^*$ one has $a\perp b$.  Formula (1) gives
$R_0=H_a$ and $R_j=\varnothing$ for $j>0$ because the old $Z_j$ are empty.

The child is unmarked under the literal source rule.  Its rank is
$r(b)=0$, so $\ell=0$.  The point $b$ is contained in none of the zero
spaces $W(y)$ and is not popular.  Moreover,

$$
|H_a|=[t]_q>\frac{[t+1]_q}{8q}=\frac{|Z_0|}{8q},
$$

so $a$ is not poor.  Equations (12)--(13) now follow from Lemma 1.
$\square$

This disproves every universal claim requiring two distinct cutoff
coordinates to contract at every unmarked step.  It also shows why the
nesting relation by itself cannot supply such a claim.

### Proposition 4: marked children coexist with a highly unsaturated layer

There is a reachable state $\sigma$ satisfying

$$
|U_0^\sigma|=q^t
\tag{14}
$$

that has at least $[t]_q$ marked children.  One of them is state-neutral and
may be repeated an arbitrary number of times.

**Proof.**  Start with any pair $(a_0,b_0)$ with $a_0\perp b_0$.  By
Corollary 3 this is an unmarked root extension.  Its state is

$$
W^\sigma(y)=
\begin{cases}
\langle b_0\rangle,&y\in H_{a_0},\\
0,&y\notin H_{a_0}.
\end{cases}
\tag{15}
$$

Thus

$$
Z_0=PG(t,q)\setminus H_{a_0},\quad |Z_0|=q^t,
\qquad
Z_1=H_{a_0},\quad |Z_1|=[t]_q.
\tag{16}
$$

For every projective point $b\in H_{a_0}$, the pair $(a_0,b)$ legally
extends $\sigma$: one has $a_0\perp b$ and
$W^\sigma(b)=\langle b_0\rangle\subseteq a_0^\perp$.  Its old rank is one.
Since $q^t>[t]_q$, the maximizing source layer for $r=1$ is $\ell_1=0$.
But $H_{a_0}\cap Z_0=\varnothing$, so $a_0$ is poor and the child is
marked.  The $[t]_q$ choices of $b$ are distinct children.

For $b=b_0$, (15) is unchanged: wherever $a_0\perp y$, the old space
already contains $b_0$.  Hence this marked child is state-neutral.  The
same argument applies after every repetition. $\square$

In particular, the simultaneous saturation threshold
$|U_0|\leq2q^0$ from `LATE_TAIL_WEIGHTED_AUDIT.md` fails by a factor
$q^t/2$, yet marked children and a marked neutral loop exist.  This refutes
a categorical marked/unsaturated mutual exclusion.  It does not refute a
quantitative theorem saying that *most* or *sufficiently many* marked
children force a saving elsewhere; the example supplies
$\Theta_t(q^{t-1})$, one power of $q$ below the source cap
$O_t(q^t)$.

### Proposition 5: source-type diversification need not occur before the explicit rank-zero threshold

Let

$$
k_q=\left\lfloor\frac{(t-1)q\log q}{12}\right\rfloor.
\tag{17}
$$

For sufficiently large $q$, the actual tuple tree contains at least $L_q$
length-$k_q$ paths such that every step is unmarked and has source type
zero, where

$$
L_q^{1/k_q}\geq
\frac3{16}q^{t+9(t-1)/10}.
\tag{18}
$$

Consequently, for every fixed $C_t$,

$$
\log\frac{L_q}{(C_tq^t)^{k_q}}
=\Omega_t(q(\log q)^2).
\tag{19}
$$

**Proof.**  This is the rank-zero saturation lemma and its elementary
comparison proved in `TRANSVERSE_ENCODING_ATTEMPT.md`, equations (2)--(5).
That proof recursively chooses a hyperplane balanced on the current
rank-zero set $S$ and then chooses $b$ inside its intersection with $S$.
It proves directly that $r(b)=\ell=0$, that the child is unmarked, and that
the construction lasts for (17) rounds.  Its independent adversarial review
is recorded in `INDEPENDENT_TRANSVERSE_REFEREE.md`.  Taking logarithms in
(18) gives (19). $\square$

This proposition rules out any proof step asserting that the displayed
$k_q$-length prefix of unmarked events must use several values of $\psi$.
It does not rule out diversification after a larger constant multiple of
$q\log q$.
Under Lemma 1, its guaranteed transitions are all in coordinate $U_0$.
Other rank layers can also contain promoted points during these steps; the
proposition gives no bound on those additional $R_j$.  Exploiting precisely
those extra, history-dependent promotions remains a logically viable route.

### Lemma 6: the exact full-state transfer operator

Two histories with the same full state $\mathcal W(\sigma)$ have the same
legal pair-labelled children and the same successor full state for every
legal label $(a,b)$.  More explicitly, $(a,b)$ is legal exactly when

$$
a\perp b
\quad\text{and}\quad
a\perp W^\sigma(b),
\tag{20}
$$

and its successor is given by (7).  The total number of legal children is

$$
\Delta(\sigma)=
\sum_{b\in PG(t,q)}
[t+1-\dim(W^\sigma(b)+\langle b\rangle)]_q.
\tag{21}
$$

Therefore, on functions of full states, the exact forward-tuple transfer
operator is

$$
(Tf)(\mathcal W)=
\sum_{(a,b)\text{ satisfying }(20)}
f(\mathcal W^{(a,b)}),
\tag{22}
$$

and the number of length-$k$ continuations is $(T^k\mathbf1)(\mathcal W)$.

**Proof.**  For every old pair $(a_i,b_i)$, consistency of the extension
requires

$$
a_i\perp b\Longrightarrow a\perp b_i.
$$

The second coordinates in the antecedent cases span $W^\sigma(b)$, so all
these implications are equivalent to $a\perp W^\sigma(b)$.  The new pair
must additionally be a vertex of $D^*$, which is $a\perp b$.  This proves
(20).  Nondegeneracy says that the orthogonal complement of
$W^\sigma(b)+\langle b\rangle$ has the displayed dimension, so it contains
the number of projective points in (21).  Lemma 1 determines the successor,
proving the Markov and operator assertions. $\square$

The cutoff vector records only the dimensions $r(y)$ aggregated over $y$.
It forgets at least the predicates $b\subseteq W(b)$, the intersections
$H_a\cap Z_j$, and the incidences $b\subseteq W(y)$ that occur in
(1), (20), and (21).  Thus the exact formulas do not close on
$(|U_0|,\ldots,|U_t|)$.  A useful smaller operator could still exist, but it
would require a new domination theorem rather than an algebraic consequence
of Claim 2.13.

## Finite exploratory check

Run

```bash
python3 routes/lower/cross_type_transfer_check.py --t 2 --q 2
```

The script implements (7), (20), and the exact finite state graph for the
prime field $q=2$.  In the default case it finds:

- $7$ projective points and $21$ vertices of $D^*(2,2)$;
- $23{,}962$ reachable full $W$-states;
- reachable states with identical rank/cutoff profiles but different
  multiplicity distributions over successor profiles.

This is a finite diagnostic showing that the most literal rank-profile
lumping already fails in the smallest case.  It is **not** used to prove an
asymptotic statement, and no experimental output is a premise of Lemmas
1--6 or Propositions 4--5.

## Corrections or missing assumptions

- A useful cross-type lemma cannot count the nesting of the $U_j$ as
  repeated progress: equations (2) and (9) show that one promoted point pays
  for exactly one cutoff.
- Source type $\psi=\ell$ records only the coordinate for which Claim 2.13
  proves a contraction.  It does not record all nonempty $R_j$.
- The rank-zero family forbids forced diversification of $\psi$ through
  length $k_q$, but leaves open eventual diversification at a larger
  $A_tq\log q$ threshold and a theorem exploiting unrecorded higher-rank
  transitions.
- The marked neutral loop forbids an absolute-depth or categorical
  marked/unsaturated dichotomy, but does not settle a quantitative
  marked-fanout inequality.

## Open risks

- The remaining plausible transfer must retain the incidence geometry of
  the blocks $R_j$ or enough of the full family $W(y)$ to dominate (22).
  A vector consisting only of layer cardinalities is not justified.
- A block-level, many-history compression could conceivably cancel the
  rank-zero prefix entropy after a longer tail.  Nothing here disproves it.
- Signed operators, quotient representations of the full $W$-state, and
  average terminal recovery remain open; the positive scalar obstruction in
  `LATE_TAIL_WEIGHTED_AUDIT.md` does not cover them.
- No new bound for a Ramsey number follows from this document.
