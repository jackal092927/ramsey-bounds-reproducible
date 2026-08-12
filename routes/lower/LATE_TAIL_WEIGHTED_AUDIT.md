# Proof package: late tails and weighted counting after Claim 2.13

Date: 2026-08-12  
Primary source: Bradač, [arXiv:2605.28793v3](https://arxiv.org/abs/2605.28793v3),
source `main.tex`, SHA-256
`90acf52f3766e780bc22114e08aa46b115cfe86e33d340e7f7eace01bb7fe39f`.

## Claim

Fix $t\geq2$ and let $q$ be a sufficiently large prime power.  Use exactly
the marking rule in Bradač Claim 2.13 for the forward-independent-tuple tree
of $D^*(t,q)$.  Put

$$
\rho=1-\frac1{32tq},\qquad d_q=-\log\rho.
\tag{1}
$$

This document proves four statements and isolates what remains open.

1. **Type-resolved weighted fanout.**  If $N_\ell(\sigma)$ is the number of
   unmarked children $\sigma'$ of a history $\sigma$ with
   $\psi(\sigma')=\ell$, then

   $$
   N_\ell(\sigma)
   \leq 4q^{t-\ell}|U_\ell^\sigma|.
   \tag{2}
   $$

   Consequently, if a fixed marked/type word of length $k$ has $m_\ell$
   unmarked positions of type $\ell$ and $m_M$ marked positions, the number
   of paths realizing that word is at most

   $$
   h^{m_M}\prod_{\ell=0}^t
   \left(8q^tq^{t-\ell}\right)^{m_\ell}
   \rho^{\binom{m_\ell}{2}},
   \qquad h=A(t)q^t.
   \tag{3}
   $$

2. **State-conditioned late tail.**  Call a history *saturated* if

   $$
   |U_\ell^\sigma|\leq2q^\ell
   \quad\text{for every }0\leq\ell\leq t.
   \tag{4}
   $$

   Every descendant of a saturated history has at most

   $$
   \bigl(A(t)+8(t+1)\bigr)q^t
   \tag{5}
   $$

   children.  Thus the number of length-$s$ suffixes from that history is at
   most the $s$-th power of (5).  Moreover, (4) is guaranteed once the path
   has accumulated at least

   $$
   J_\ell=
   \left\lceil\frac{(t-\ell)\log q}{d_q}\right\rceil
   \tag{6}
   $$

   earlier unmarked steps of each type $\ell$.

3. **Depth-conditioned late tail is false.**  For every integer $M\geq0$,
   the actual tree of $D^*(t,q)$ contains a path whose vertex at depth
   $M+2$ is unmarked under the source rule.  In fact, after one unmarked
   pair one may repeat the same pair $M$ times; all repetitions are marked,
   leave every $W(y)$ unchanged, and may then be followed by another
   unmarked type-zero step.  Hence no bound of the form "all vertices after
   depth $B_tq\log q$ are marked" follows, for any $B_t$.

4. **Two rigorous no-go statements.**

   - The black-box conclusion of Claim 2.13 (at most $Aq^t$ marked children
     and at most $Aq\log q$ unmarked vertices per path) cannot, by itself,
     imply a $(C_tq^t)^k$ path bound at any threshold
     $k\geq B_tq\log q$.  The witness here is an abstract tree, not a
     subtree asserted to occur in $D^*(t,q)$.
   - Any positive-potential proof that contracts the total weight of the
     rank-zero saturation family by a factor at most $B_tq^t$ per level must
     assign some terminal path weight

     $$
     \exp\bigl(-\Omega_t(q(\log q)^2)\bigr)
     \tag{7}
     $$

     relative to the root.  Therefore a terminal recovery loss of only
     $\exp(O_t(q\log q))$ is impossible for that proof template.

## Status

- **Type-resolved fanout (2)--(3):** **PROVABLE AS STATED**.
- **State-conditioned late tail (4)--(6):** **PROVABLE AS STATED**.
- **A late tail determined only by the absolute depth:** **FALSE AS
  STATED**, inside the actual $D^*(t,q)$ tree.
- **Deriving the $q\log q$ threshold from only the two numerical outputs of
  Claim 2.13:** **FALSE AS STATED**, by an explicit abstract tree.
  This is not a counterexample to any Ramsey bound or to the corresponding
  counting statement for the actual $D^*(t,q)$.
- **A scalar weighted-contraction proof with only
  $\exp(O_t(q\log q))$ terminal distortion:** **FALSE AS STATED** for the
  rank-zero saturation family.
- **The actual bound
  $\overrightarrow i_k(D^*(t,q))\leq(C_tq^t)^k$ for every
  $k\geq A_tq\log q$:** **OPEN / NOT CURRENTLY JUSTIFIED**.  The results
  here neither prove nor disprove it.
- **A new Ramsey lower bound with one fewer logarithm:** **NOT CURRENTLY
  JUSTIFIED**.

## Source alignment

The proof below uses the v3 source in the following exact order.

| v3 `main.tex` lines | source item | use below |
|---:|---|---|
| 553 | definition of $D^*(t,q)$ | delayed-step construction |
| 581--585 | Claim 2.13 and consistency | all path statements |
| 587--595 | $W^\sigma(y)$, $r^\sigma(y)$, and the bound $2q^{t-r(b)}$ | (2) |
| 597--603 | $U_r$, $Z_r$, $\ell_r^\sigma$, popular children | type partition |
| 605--615 | poor children and their marked count | delayed repetitions |
| 617 | definition of $\psi$ and $U_\ell$ contraction by $\rho$ | (3), (6) |
| 619--620 | at most $Aq\log q$ unmarked vertices | comparison only |
| 621--623 | the generic $\Delta^w$ loss | black-box obstruction |

No stronger monotonicity is imported: only the elementary fact, immediate
from the definition of $W^\sigma(y)$, that every $U_\ell$ is nonincreasing
when a history is extended.

## Assumptions and notation

- Projective points are the $1$-spaces of
  $V=\mathbb F_q^{t+1}$, with the source's standard nondegenerate bilinear
  form.
- $N=[t+1]_q$ is the number of projective points.  For $q\geq2$,
  $N<2q^t$.
- $Z_r^\sigma=U_r^\sigma\setminus U_{r-1}^\sigma$ and
  $\ell_r^\sigma\in\{0,\ldots,r\}$ maximizes
  $|Z_0^\sigma|,\ldots,|Z_r^\sigma|$.
- An unmarked child $\sigma'$ has source type
  $\psi(\sigma')=\ell_r^\sigma$, where
  $r=r^\sigma(b)$ for its second coordinate $b$.
- $A(t)$ denotes the source constant for the number $h=A(t)q^t$ of marked
  children.  Its numerical value is irrelevant.

## Proof strategy

First count the children of one source type using the extension bound for a
fixed $b$.  Then telescope the exact $U_\ell$ contraction along positions
of the same type.  This gives both a Gaussian penalty in the type count and
a genuine suffix bound once all normalized layer sizes are small.

Next, distinguish this state condition from absolute depth.  A state-neutral
marked repetition delays the next unmarked step by an arbitrary amount.
Finally, use an extremal abstract tree and the already proved rank-zero
saturation family to show why neither Claim 2.13 as a black box nor a
recoverable scalar weight can remove the initial
$\exp(\Theta_t(q(\log q)^2))$ entropy.

## Dependency map

1. Lemma 1 uses v3 equation (7), $|Z_r|\leq|Z_{\ell_r}|$, and a geometric
   series.
2. Lemma 2 uses Lemma 1, v3 line 617, and $N<2q^t$.
3. Corollary 3 uses Lemma 1 and monotonicity of every $U_\ell$.
4. Proposition 4 uses the exact source definitions plus the balanced
   hyperplane lemma proved in
   [TRANSVERSE_ENCODING_ATTEMPT.md](./TRANSVERSE_ENCODING_ATTEMPT.md).
5. Proposition 5 is a self-contained abstract-tree counterexample.
6. Proposition 6 uses the rank-zero path lower bound in that same document.

## Proof

### Lemma 1: type-resolved child count

For every consistent history $\sigma$ and $0\leq\ell\leq t$, equation (2)
holds.

**Proof.**  Fix $r\in\{\ell,\ldots,t\}$ for which
$\ell_r^\sigma=\ell$.  Every child with $r^\sigma(b)=r$ has
$b\in Z_r^\sigma$.  V3 equation (7) gives at most $2q^{t-r}$ possible first
coordinates $a$ for each fixed $b$.  Since $\ell_r^\sigma$ maximizes the
layer size through rank $r$,

$$
|Z_r^\sigma|\leq|Z_\ell^\sigma|\leq|U_\ell^\sigma|.
$$

The number of all extensions, and therefore of unmarked extensions, with
this $r$ is at most $2q^{t-r}|U_\ell^\sigma|$.  Summing over the possible
$r$ gives

$$
N_\ell(\sigma)
\leq2|U_\ell^\sigma|\sum_{r=\ell}^tq^{t-r}
\leq4q^{t-\ell}|U_\ell^\sigma|,
$$

because $1+q^{-1}+q^{-2}+\cdots\leq2$ for $q\geq2$.  This proves (2).
$\square$

### Lemma 2: the exact type-count penalty

Fix a marked/type word
$\omega\in\{M,0,1,\ldots,t\}^k$.  Let $m_M$ be its number of $M$ symbols
and $m_\ell$ its number of $\ell$ symbols.  The number of paths whose
marked/unmarked status and $\psi$ types equal $\omega$ satisfies (3).

**Proof.**  Consider the $j$-th type-$\ell$ position along any prefix
realizing the word.  Before this position there have been $j-1$ earlier
unmarked contractions of $U_\ell$.  All intervening extensions can only
decrease $U_\ell$.  V3 line 617 and $|U_\ell^{\varnothing}|=N<2q^t$ give

$$
|U_\ell^\sigma|\leq2q^t\rho^{j-1}.
\tag{8}
$$

Lemma 1 therefore bounds the number of choices at this position by

$$
8q^{2t-\ell}\rho^{j-1}
=8q^tq^{t-\ell}\rho^{j-1}.
\tag{9}
$$

At every marked position the source gives at most $h=A(t)q^t$ choices.
Multiplying (9) over $j=1,\ldots,m_\ell$ and then over all $\ell$ gives
(3), since $\sum_{j=1}^{m_\ell}(j-1)=\binom{m_\ell}{2}$. $\square$

The logarithm of the factor in (3) beyond a constant multiple of $q^t$ per
step is

$$
F(\mathbf m)=\sum_{\ell=0}^t
\left((t-\ell)m_\ell\log q
-d_q\binom{m_\ell}{2}\right).
\tag{10}
$$

For one type, putting $a=(t-\ell)\log q$ and completing the square gives

$$
\max_{m\geq0}\left(am-d_q\binom m2\right)
\leq\frac{(a+d_q/2)^2}{2d_q}.
\tag{11}
$$

Since $d_q\geq1/(32tq)$, summing (11) yields only

$$
\max_{\mathbf m}F(\mathbf m)=O_t(q(\log q)^2).
\tag{12}
$$

Thus the normalized $U_\ell$ potential rigorously reproduces the known
$q(\log q)^2$ overhead.  Equation (12) is an upper bound, not a claim that
every type vector realizes that much entropy.

### Corollary 3: a genuine state-conditioned tail

If $\sigma$ satisfies (4), then every descendant $\tau$ also satisfies
(4), and every such $\tau$ has at most (5) children.  Hence the number of
length-$s$ continuations of $\sigma$ is at most

$$
\left(\bigl(A(t)+8(t+1)\bigr)q^t\right)^s.
\tag{13}
$$

Condition (4) follows if the prefix has at least $J_\ell$ earlier unmarked
steps of every type $\ell$.

**Proof.**  Monotonicity preserves (4).  Lemma 1 bounds the number of
unmarked children of each type by

$$
4q^{t-\ell}|U_\ell^\tau|\leq8q^t.
$$

Summing over $t+1$ types and adding the at most $A(t)q^t$ marked children
proves (5), and induction proves (13).

If a prefix has had $m_\ell$ type-$\ell$ unmarked steps, (8) gives
$|U_\ell|\leq2q^t\rho^{m_\ell}$.  For $m_\ell\geq J_\ell$, definition (6)
implies $\rho^{m_\ell}\leq q^{-(t-\ell)}$, proving (4). $\square$

Notice that
$J_\ell=O_t((t-\ell)q\log q)$ and
$\sum_\ell J_\ell=O_t(q\log q)$.  This does **not** say that a path of that
absolute length is saturated: it requires the stated typewise counters.

### Proposition 4: unmarked steps can be delayed arbitrarily

For every $M\geq0$ and all sufficiently large $q$, an actual path in the
$D^*(t,q)$ tuple tree has a marked, state-neutral block of length $M$
followed by an unmarked child.

**Proof.**  Choose any projective pair $(a,b)$ with $a\perp b$.  At the
root, every $W(y)$ is zero, so $r(b)=\ell=0$ and $b$ is not popular.  The
hyperplane $H_a=\{y:a\perp y\}$ has $[t]_q$ points, which is strictly more
than $N/(8q)$ for large $q$.  Thus $a$ is not poor, and the first child
$(a,b)$ is unmarked.

After this step,

$$
W(y)=
\begin{cases}
\langle b\rangle,&y\in H_a,\\
0,&y\notin H_a.
\end{cases}
\tag{14}
$$

Append $(a,b)$ again.  It is consistent with every previous copy.  Here
$r(b)=1$, while

$$
Z_0=PG(t,q)\setminus H_a,
\qquad |Z_0|=q^t>[t]_q=|Z_1|.
$$

Hence the source chooses $\ell_1=0$.  The point $a$ has no neighbour in
$Z_0$, so it is poor and the repeated child is marked.  Equation (14) is
unchanged, because the same vector is added to the same spans.  The same
argument applies to every further repetition, giving $M$ marked,
state-neutral steps.

Let $S=Z_0=PG(t,q)\setminus H_a$.  The balanced-hyperplane lemma in
`TRANSVERSE_ENCODING_ATTEMPT.md` supplies, for large $q$, a projective
hyperplane $H_c$ satisfying

$$
\frac{p|S|}{2}\leq|H_c\cap S|\leq\frac{3p|S|}{2},
\qquad p=\frac{[t]_q}{[t+1]_q}.
$$

Choose $d\in H_c\cap S$ and append $(c,d)$.  Every previous first
coordinate is $a$, and $a\not\perp d$ because $d\in S$, so consistency has
no old-to-new constraint.  Also $c\perp d$.  We have $W(d)=0$, hence
$r(d)=\ell=0$.  The new $d$ is contained in no zero-dimensional $W(y)$
for $y\in S$, so it is not popular.  Finally,
$|H_c\cap S|> |S|/(8q)$, so $c$ is not poor.  The child is unmarked and
occurs at depth $M+2$. $\square$

This is a literal counterexample to an absolute-depth tail.  It does not
create $Aq^t$ independent state-neutral choices at each delayed step, so it
does not by itself disprove the desired global tuple-count bound.

### Proposition 5: Claim 2.13 is insufficient as a black box

Fix any constants $B>0$ and $C>0$.  There are rooted trees satisfying

- at most $q^t$ marked children at every vertex, and
- at most $\lfloor q\log q\rfloor$ unmarked vertices on every root path,

but having more than $(Cq^t)^k$ paths at
$k=\lceil Bq\log q\rceil$ for all sufficiently large $q$.

**Proof.**  Put $w=\lfloor q\log q\rfloor$ and
$\Delta=q^{2t-1}$.  Through level $w$, give every vertex exactly $\Delta$
unmarked children.  At all later levels, give every vertex exactly $q^t$
marked children.

If $k\leq w$, the number of length-$k$ paths is $\Delta^k$, and

$$
\log\frac{\Delta^k}{(Cq^t)^k}
=k\bigl((t-1)\log q-\log C\bigr)>0
$$

for large $q$.  If $k>w$, the path count is
$\Delta^w(q^t)^{k-w}$, and

$$
\log\frac{\Delta^w(q^t)^{k-w}}{(Cq^t)^k}
=w(t-1)\log q-k\log C
=\Theta_{t,B}(q(\log q)^2)>0.
$$

The two required tree properties hold by construction. $\square$

Therefore no replacement for v3 Lemma 2.7 that uses only the numerical
outputs $(h,w)$ of Claim 2.13 can establish a $q\log q$ threshold.  A valid
proof must exploit additional correlations among the actual children.  The
tree in Proposition 5 is **not** claimed to embed in $D^*(t,q)$ and provides
**no** Ramsey counterexample.

### Proposition 6: a terminal-range obstruction for positive potentials

Let $\mathcal F_q$ be the rank-zero saturation subtree constructed in
`TRANSVERSE_ENCODING_ATTEMPT.md`, truncated at

$$
k_q=\left\lfloor\frac{(t-1)q\log q}{12}\right\rfloor.
$$

It has at least $L_q$ leaves, with

$$
L_q^{1/k_q}\geq\frac3{16}q^{t+9(t-1)/10}.
\tag{15}
$$

Suppose $\Phi$ is positive on its vertices, $\Phi(\varnothing)=1$, and for
every nonterminal $\sigma\in\mathcal F_q$,

$$
\sum_{\tau\text{ a child of }\sigma\text{ in }\mathcal F_q}
\Phi(\tau)\leq B_tq^t\Phi(\sigma),
\tag{16}
$$

where $B_t$ is independent of $q$.  Then some leaf $\tau$ satisfies

$$
\Phi(\tau)
\leq\left(\frac{16B_t}{3}
q^{-9(t-1)/10}\right)^{k_q}
\leq
\exp\left(-\frac{(t-1)^2}{20}q(\log q)^2\right)
\tag{17}
$$

for all sufficiently large $q$.

**Proof.**  Iterating (16) shows that the sum of the weights of all leaves
is at most $(B_tq^t)^{k_q}$.  Since there are at least $L_q$ leaves, one
has weight at most their average.  Equation (15) gives the first inequality
in (17).  For large $q$,
$\log(16B_t/3)\leq(t-1)\log q/10$ and
$k_q\geq(t-1)q\log q/13$.  Substitution gives an exponent at most
$-(4/5)(t-1)k_q\log q$, which is smaller than the final exponent in (17).
$\square$

In particular, (16) cannot be combined with a uniform terminal lower bound
$\Phi(\tau)\geq\exp(-D_tq\log q)$.  This obstruction applies even if
$\Phi$ depends on the entire history rather than only on the $U_\ell$.
It does not rule out signed weights, a vector-valued transfer operator, or
an argument that recovers the very small terminal weights through an
additional structural cancellation.  It is a statement at the truncation
depth $k_q$; a long-horizon potential is not excluded from becoming this
small there and recovering on a later, structurally controlled tail.

## What is proved, and what would still be needed

The provable late tail is **state based**: after every normalized layer
$|U_\ell|/q^\ell$ is $O_t(1)$, direct fanout is $O_t(q^t)$.  The source
contraction reaches that region after $O_t(q\log q)$ unmarked events of the
appropriate types.  Neither elapsed depth nor total unmarked count forces
all those typewise conditions.

To prove the open $k\geq A_tq\log q$ tuple bound, one must therefore control
the *prefix entropy* before saturation.  At least one of the following genuinely
new inputs is required:

1. an aggregate correlation showing that histories with large
   $|U_\ell|/q^\ell$ have substantially fewer continuations of the other
   types or fewer marked continuations;
2. a many-history compression whose terminal recovery explicitly cancels
   the $\exp(\Omega_t(q(\log q)^2))$ rank-zero family;
3. a different algebraic construction or a conversion to Ramsey graphs
   that downweights precisely those prefixes.

Equations (2)--(6) alone do not provide any of these inputs.

## Executable arithmetic check

Run

```bash
python3 routes/lower/late_tail_weighted_check.py
```

The script checks the finite arithmetic in (6), (10)--(12), the two cases
of the abstract-tree ratio, and the explicit exponent in (17) over a grid of
parameters.  It does not replace the projective or tree arguments above.

## Open risks

- The positive suffix lemma is conditional on the simultaneous state bounds
  (4); calling it a depth tail would reverse the quantifiers.
- Proposition 5 is an obstruction to using Claim 2.13 *as a black box*, not
  an abstract model of every geometric dependency in $D^*$.
- Proposition 6 rules out a specified positive-potential template with a
  recoverable terminal range.  It does not prove that every possible
  weighted or operator argument fails.
- No bound for a Ramsey number is improved in this document.
