# Independent adversarial review: cross-type transfer attempt

Date: **2026-08-12**

Reviewed artifacts:

- `CROSS_TYPE_TRANSFER_ATTEMPT.md`, SHA-256
  `76ea57a686af2ccd99e61111a47306fa10ba5e54b4f9f42c8f416ada9665a4fb`;
- `cross_type_transfer_check.py`, SHA-256
  `309625aab3630678445b91d5f0f378820b13e856e47b92313bebf1e12f426c52`.

Primary-source comparison: Bradač,
[arXiv:2605.28793v3](https://arxiv.org/abs/2605.28793v3), `main.tex`
SHA-256
`90acf52f3766e780bc22114e08aa46b115cfe86e33d340e7f7eace01bb7fe39f`,
especially source lines 553 and 581--623.

## Verdict

```text
PASS AFTER CORRECTION (RESOLVED)
DIVERSIFICATION QUANTIFIERS NOW MATCH THE PROOF
NO NEW RAMSEY BOUND
```

The exact rank-layer flow, root counterexample, unmarked contraction
certificate, marked/unsaturated counterexample, full-state legality formula,
legal-child fanout formula, and full-state transfer operator are all
**PROVABLE AS STATED**.

The initially reviewed snapshot stated the source-type-diversification
conclusion too broadly.  The current document now correctly records that the
imported rank-zero construction proves an all-$\psi=0$ prefix only through

$$
k_q=\left\lfloor\frac{(t-1)q\log q}{12}\right\rfloor.
$$

It disproves diversification before this explicit threshold and disproves
record maps required uniformly over every prefix length.  It does **not**
disprove an eventual-diversification theorem with threshold $A_tq\log q$
when $A_t$ is larger than $(t-1)/12$.  The current status section explicitly
labels that eventual-diversification question open.

The correction affected the prose/status boundary, not the exact transition
lemmas or either concrete counterexample.  The actual $D^*(t,q)$ tuple bound
at $k\ge A_tq\log q$, and the hoped-for Ramsey lower bound with one fewer
logarithm, remain open.

## Resolved correction audit

The following material overclaims in the initial snapshot were all narrowed
in the current reviewed hash:

| initial location | initial issue | current resolution |
|---:|---|---|
| 50--58 | “No forced diversification of source types” could be read beyond the constructed prefix | Current lines 50--60 explicitly limit the obstruction to $k_q$ and state that a larger $A_tq\log q$ threshold is not ruled out. |
| 82--83 | “Diversify within $O_t(q\log q)$: FALSE” suppressed the decisive constant | Current lines 84--87 say diversification before $k_q$ is false and eventual diversification for larger $A_t$ is open. |
| 344 | Heading said diversification was impossible | Current line 348 limits the heading to the explicit rank-zero threshold. |
| 380--381 | Used a generic $\Theta_t(q\log q)$ prefix | Current lines 384--387 refer to the displayed $k_q$ prefix and leave larger multiples open. |
| 472--473 | The summary omitted the length restriction | Current lines 478--481 add “through length $k_q$” and state both remaining open routes. |

A precise replacement requested in the initial review was:

> **Unmarked source types must diversify before
> $k_q=\lfloor(t-1)q\log q/12\rfloor$: FALSE.  Eventual diversification by
> $A_tq\log q$ for some larger constant $A_t$: OPEN / NOT CURRENTLY
> JUSTIFIED.**

The current status lines 84--87 implement this replacement.  This distinction
is material because the target tuple theorem itself is allowed to choose an
unspecified constant $A_t$.  The older source document records the same
boundary: `TRANSVERSE_ENCODING_ATTEMPT.md` lines 441--445 and its independent
review lines 195--198 explicitly state that the construction does not refute
a threshold with sufficiently large $A_t$.

## 1. Source-definition alignment

The reviewed proof uses the same objects and polarity conventions as Claim
2.13:

1. A history is consistent when $a_i\perp b_i$ and, for $i<j$,
   $a_i\perp b_j$ implies $a_j\perp b_i$.
2. The source state is

   $$
   W^\sigma(y)=\operatorname{span}\{b_i:a_i\perp y\},
   \qquad r^\sigma(y)=\dim W^\sigma(y).
   $$

3. $U_r=\{y:r(y)\le r\}$ and $Z_r=U_r\setminus U_{r-1}$, including the
   source's auxiliary layer $Z_{t+1}$.
4. For $b\in Z_r$ with $r\le t$, the source chooses
   $\ell_r\in\{0,\ldots,r\}$ maximizing $|Z_\ell|$.
5. Popular is inclusive at $\ge |Z_\ell|/(16q)$ and poor is inclusive at
   $\le |Z_\ell|/(8q)$.  Hence an unmarked child is strictly below the first
   threshold and strictly above the second.
6. The polarity graph permits loops at self-orthogonal projective points.
   Thus $V(D^*)=\{(a,b):a\perp b\}$ is literal, with no omitted
   $a\ne b$ condition.

The cited source-line table agrees with v3 `main.tex`.  The first imported
dependency is Claim 2.13's exact state and marking definitions; all
transition identities after that are direct linear algebra.

## 2. Exact rank-layer flow

Appending $(a,b)$ adds the one-space $\langle b\rangle$ to $W^\sigma(y)$
exactly when $y\perp a$.  Hence

$$
r^{\sigma(a,b)}(y)=r^\sigma(y)+
\mathbf1_{\{y\perp a,\ b\not\subseteq W^\sigma(y)\}}.
$$

The rank can increase by at most one.  If

$$
R_j=\{y\in Z_j^\sigma:y\perp a,
                 \ b\not\subseteq W^\sigma(y)\},
$$

then a point of old rank below $j$ cannot leave $U_j$, a point of rank $j$
leaves exactly when it belongs to $R_j$, and a point of rank above $j$
cannot enter.  Therefore

$$
U_j^{\sigma(a,b)}=U_j^\sigma\setminus R_j
$$

for every $0\le j\le t$.  The adjacent-layer identities, including the
$Z_{t+1}$ sink, follow by partitioning the same pointwise alternatives.

This also verifies the linear potential identity

$$
\Phi_{\mathbf c}(\sigma(a,b))-
\Phi_{\mathbf c}(\sigma)=-\sum_{j=0}^t c_j|R_j|.
$$

One promoted point leaves exactly one cutoff, not all larger nested cutoffs.
Different cutoffs can shrink in the same step only through different old
rank layers.

**Rank-flow verdict: PASS.**

## 3. What unmarkedness actually certifies

For an unmarked child, let $r=r^\sigma(b)$ and
$\ell=\ell_r^\sigma$.  Non-poorness gives strictly more than
$|Z_\ell|/(8q)$ points in $H_a\cap Z_\ell$, while non-popularity gives
strictly fewer than $|Z_\ell|/(16q)$ points $y\in Z_\ell$ whose $W(y)$
contains $b$.  Their set difference is contained in $R_\ell$, so

$$
|R_\ell|\ge \frac{|Z_\ell|}{16q}.
$$

The weak inequality is safe despite the strict threshold directions.  The
source contains no corresponding lower bound for $R_j$ when $j\ne\ell$.
It also does not assert that those other blocks vanish.  Thus the reviewed
document correctly separates “not source-certified” from “zero.”

At the empty history all points have rank zero.  For every legal $(a,b)$,

$$
R_0=H_a,\qquad R_j=\varnothing\quad(j>0).
$$

Furthermore $b$ is not popular and
$|H_a|=[t]_q>[t+1]_q/(8q)$, so $a$ is not poor.  Every root child is
unmarked of type zero, while only $U_0$ shrinks.  This is a valid universal
counterexample to the claim that every unmarked step must contract at least
two cutoff coordinates.

**Unmarked-certificate and root-counterexample verdict: PASS.**

## 4. Marked children at an unsaturated state

After one root extension $(a_0,b_0)$, the exact state is

$$
W(y)=\begin{cases}
\langle b_0\rangle,&y\in H_{a_0},\\
0,&y\notin H_{a_0}.
\end{cases}
$$

Consequently

$$
Z_0=PG(t,q)\setminus H_{a_0},\quad |Z_0|=q^t,
\qquad
Z_1=H_{a_0},\quad |Z_1|=[t]_q.
$$

For every $b\in H_{a_0}$, the pair $(a_0,b)$ is a legal child: it satisfies
$a_0\perp b$ and $a_0\perp W(b)$.  Its old rank is one and
$|Z_0|>|Z_1|$, so $\ell_1=0$.  Since
$H_{a_0}\cap Z_0=\varnothing$, $a_0$ is poor under the inclusive source
definition.  This yields at least $[t]_q$ distinct marked children while
$|U_0|=q^t$.

Choosing $b=b_0$ changes no $W(y)$ and gives a marked state-neutral loop.
Repeated tuple vertices are legal in the source's ordered forward-tuple
tree: the consistency implications become
$a_0\perp b_0\Rightarrow a_0\perp b_0$, and $D^*$ has no directed loop at
$(a_0,b_0)$.  Hence the loop may be repeated arbitrarily.

The example disproves only a **categorical** marked/unsaturated exclusion.
It has $\Theta_t(q^{t-1})$ marked children, whereas Claim 2.13's general
marked cap is $O_t(q^t)$.  It therefore neither proves nor disproves the
quantitative inverse fanout relation that would be needed to save a
logarithm.  The reviewed document states this boundary correctly.

**Marked/unsaturated verdict: PASS.**

## 5. Rank-zero prefix and the quantifier failure

The imported rank-zero construction was independently reviewed at hashes

```text
abc50f95fd2f4674de5151283708bf2c47bbfc0d3affc39c65d4e62ec21bb16c  TRANSVERSE_ENCODING_ATTEMPT.md
1626cd6539df6280b6e0e5b88543ed6a530594a66734241ea6909d2fa1f01c0f  INDEPENDENT_TRANSVERSE_REFEREE.md
```

It proves that the actual tuple tree has at least $L_q$ paths of the exact
length $k_q$ for which every step is unmarked and $\psi=0$, with

$$
L_q^{1/k_q}\ge\frac3{16}q^{t+9(t-1)/10}.
$$

The transfer document imports this literal result correctly in Proposition
5.  Its current heading, consequence paragraph, status line and final summary
all retain the explicit constant.  If a proposed theorem says diversification
occurs by $A_tq\log q$, the construction is a counterexample only when its
guaranteed all-zero prefix reaches that chosen threshold.  No such reach is
proved for $A_t>(t-1)/12$, and the current document says so.

The prefix entropy still validly refutes the earlier **scale-free uniform
record map**, because that proposal had to handle every length and signature.
It does not refute a thresholded long-tail theorem.

**Rank-zero claim verdict: PASS AFTER CORRECTION; GLOBAL
DIVERSIFICATION BOUNDARY IS NOW ACCURATE.**

## 6. Exact full-state fanout and transfer operator

For a proposed new label $(a,b)$, consistency with every old pair requires

$$
a_i\perp b\Longrightarrow a\perp b_i.
$$

The $b_i$ selected by true antecedents span $W^\sigma(b)$.  Together with
the vertex condition $a\perp b$, legality is therefore equivalent to

$$
a\perp\bigl(W^\sigma(b)+\langle b\rangle\bigr).
$$

If the latter subspace has vector dimension $d$, nondegeneracy gives an
orthogonal complement of dimension $t+1-d$, containing exactly
$[t+1-d]_q$ projective points.  Summing over projective $b$ proves

$$
\Delta(\sigma)=
\sum_b[t+1-\dim(W^\sigma(b)+\langle b\rangle)]_q.
$$

This is an **equality**, strengthening the source's convenient upper bound
$2q^{t-r(b)}$.  It also handles the rank-$t+1$ case: then the summand is
$[0]_q=0$.

The full state $\mathcal W=(W(y))_y$ determines the legal pair labels and,
by the rank-flow formula, the successor full state for each label.  Hence
the stated pair-labelled transfer operator is exact, including multiplicity
when distinct labels yield the same successor state.  The number of
length-$k$ continuations is consequently $T^k\mathbf1$.

The cutoff vector does not record the subspace incidences needed in either
legality or transition.  The finite diagnostic supplies an explicit
corroborating witness: in $(t,q)=(2,2)$, reachable states 26 and 27 have the
same rank profile $(2,4,1,0)$ and cutoff profile $(2,6,7)$, but different
multiplicity distributions over successor rank profiles.  This shows that
the literal rank/cutoff partition is not lumpable.  It does not rule out a
different quotient or a one-sided domination theorem.

**Full-state operator verdict: PASS.**

## 7. Executable audit

The checker compiled and the documented default exploration completed:

```text
PG points:                     7
D* vertices:                  21
reachable full states:    23,962
distinct state edges:     96,054
pair-labelled transitions:134,883
state-neutral transitions:58,401
rank-profile lumpability failures: 19,887
```

I independently checked, across all 23,962 reachable states and all 134,883
pair-labelled transitions, the exact $R_j$ cutoff-flow identities and the
full-state fanout formula.  I also checked the root and one-step
marked/state-neutral construction directly in this finite instance.

These computations are diagnostics only.  The script supports prime $q$
through ordinary modular arithmetic, not general prime powers, and its
finite output proves no asymptotic claim.  None of the accepted analytic
lemmas depends on it.

## Final claim boundary

After the listed correction, the defensible result is:

1. Claim 2.13's exact pointwise transition is adjacent-rank flow; nesting
   supplies no automatic multi-cutoff gain.
2. Unmarkedness directly certifies a removal block only in its selected
   source layer; other layers require new incidence information.
3. Multi-cutoff contraction at every unmarked step is false already at the
   root.
4. Marked children and a neutral marked loop can coexist with
   $|U_0|=q^t$, but a quantitative fanout/saturation tradeoff remains open.
5. Source type need not diversify before the explicit threshold $k_q$;
   eventual diversification by a larger $A_tq\log q$ remains open.
6. The exact Markov state is the full family $(W(y))_y$; the cutoff profile
   is not an exact lumping in the smallest finite case.

No new tuple bound and no new Ramsey-number lower bound follows.  The next
viable route must prove a new averaged correlation, domination, or
full-state compression theorem rather than use cutoff nesting alone.
