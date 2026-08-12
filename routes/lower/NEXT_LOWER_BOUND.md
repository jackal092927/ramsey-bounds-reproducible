# Next lower-bound cut: a rigorous multi-witness obstruction

Date: 2026-08-12  
Primary source: Bradač, arXiv:2605.28793v3, source `main.tex`, SHA-256
`90acf52f3766e780bc22114e08aa46b115cfe86e33d340e7f7eace01bb7fe39f`.

## Claim

We compare two possible next steps.

1. Make the large-$C$ threshold in
   [HMS_APPENDIX_BRIDGE.md](./HMS_APPENDIX_BRIDGE.md) numerical.
2. Replace Bradač's one-coordinate decay record by a compound record of the
   projective points removed at each unmarked step.

The first option is not currently justified from the printed HMS theorem:
its red proposition and its final bookkeeping retain absolute but unspecified
$O/o$ constants.  A numerical scan of the already defined quantities cannot
turn those symbols into a certified $C_0$.

For the second option, an exact piece of the proposed mechanism can be
proved, but the hoped-for consequence does **not** follow.  In the notation
of Bradač Claim 2.13, an unmarked child $\sigma'=\sigma(a,b)$ of type
$\ell$ removes the set

$$
R=\{y\in Z_\ell^\sigma:y\perp a, b\not\subseteq W^\sigma(y)\},
\qquad |R|\geq \frac{|Z_\ell^\sigma|}{16q}.
\tag{1}
$$

Every point of $R$ is permanently absent from $U_\ell$ after this step.
Nevertheless, the size lower bound (1), even together with projective
geometry, need not force more than one independent witness.  We give below,
for every prime power $q$ and every $t\geq2$, an actual consistent history
followed by $q$ consecutive unmarked children, each with $R$ of rank exactly
one, while the union of all $q$ blocks has rank only two.  More generally,
if $d_R=\dim\operatorname{span}R$, then the exact implication is only

$$
|R|\leq [d_R]_q:=\frac{q^{d_R}-1}{q-1},
\qquad
d_R\geq
\left\lceil\log_q((q-1)|R|+1)\right\rceil.
\tag{2}
$$

Consequently the current source invariant
$|Z_\ell|\geq1$ permits $|R|=1$ and $d_R=1$.  Even when
$|Z_\ell|=\Theta(q^j)$, (2) forces only $d_R\geq j+O(1)$, not a new rank
proportional to the number of unmarked steps.  Thus the removal blocks alone
do not prove an $\exp(O_t(q\log q))$ encoding.

## Status

- **Explicit HMS $C_0$ from the frozen source theorem:**
  **NOT CURRENTLY JUSTIFIED**.  The obstacle is an unspecified source
  constant, not numerical precision.
- **Permanent-removal statement (1):** **PROVABLE AS STATED**.
- **Projective rank bound (2):** **PROVABLE AS STATED**, and sharp.
- **Relative-to-$W(b)$ rank bound:** **PROVABLE AS STATED**, but it does not
  control rank transverse to certificates charged on earlier steps.
- **Actual nontransverse $q$-block family in $D^*(t,q)$:**
  **PROVABLE AS STATED** for every prime power $q$ and every $t\geq2$.
- **Compound-removal blocks imply the desired $q\log q$ tree threshold:**
  **NOT CURRENTLY JUSTIFIED**.  The missing ingredient is a transverse-rank
  or bounded-multiplicity lemma that is absent from Claim 2.13.
- **Free "small $Z_r$ can all be marked" refinement:**
  **PROVABLE AS STATED**, but by itself it does not repair the rank gap.

This is an obstruction to the presently proposed proof device, not a proof
that Bradač's final logarithmic loss is unavoidable.

## Assumptions and notation

- $q$ is a prime power and $t\geq2$ is fixed.
- Projective points are $1$-spaces of $V=\mathbb F_q^{t+1}$.
- $\sigma=(a_1,b_1,\ldots,a_m,b_m)$ is a consistent history in
  $D^*(t,q)$, as in Bradač source lines 585--597.
- For a projective point $y$,

  $$
  W^\sigma(y)=\operatorname{span}\{b_i:a_i\perp y\},
  \quad r^\sigma(y)=\dim W^\sigma(y),
  $$

  and $U_j^\sigma=\{y:r^\sigma(y)\leq j\}$,
  $Z_j^\sigma=U_j^\sigma\setminus U_{j-1}^\sigma$.
- An unmarked extension $(a,b)$ has source type
  $\ell=\ell_{r^\sigma(b)}^\sigma$.

## Proof strategy

We first extract the literal set removed in Bradač's proof.  We then count
projective points in a fixed vector subspace.  This gives the strongest rank
conclusion available from cardinality alone and supplies matching low-rank
examples.  Finally, we isolate the extra lemma that a successful compound
encoding would have to prove.

## Dependency map

1. Lemma 1 uses only the definitions of consistency and $W^\sigma(y)$ and
   Bradač's non-poor/non-popular inequalities.
2. Lemma 2 uses the exact count of $1$-spaces in $\mathbb F_q^d$.
3. Lemma 3 refines the rank count relative to the current source span
   $W^\sigma(b)$ and uses consistency to place both spaces in $a^\perp$.
4. The obstruction is witnessed inside the actual $D^*(t,q)$ tree by the
   explicit history in Proposition 4.
5. The small-$Z_r$ marking lemma uses the source extension bound
   $2q^{t-r}$ for each fixed $b\in Z_r$.

## Proof

### Lemma 1: literal, disjoint removal blocks

Let $\sigma' = \sigma(a,b)$ be unmarked, put
$r=r^\sigma(b)$, and let $\ell=\ell_r^\sigma$.  Define $R$ by (1).
Then

$$
|R|\geq |Z_\ell^\sigma|/(16q),
\qquad
R\subseteq U_\ell^\sigma\setminus U_\ell^{\sigma'}.
\tag{3}
$$

Moreover $U_\ell$ is nonincreasing under every later extension, so removal
sets of the same type $\ell$ arising at different steps along one path are
pairwise disjoint.

**Proof.** Since $a$ is not poor, at least
$|Z_\ell^\sigma|/(8q)$ points $y\in Z_\ell^\sigma$ satisfy $y\perp a$.
Since $b$ is not popular, at most $|Z_\ell^\sigma|/(16q)$ of those points
satisfy $b\subseteq W^\sigma(y)$.  Subtraction gives the first assertion in
(3).  For $y\in R$, the old span has dimension $\ell$, while $b$ is not in
that span.  Because $y\perp a$, the new term $b$ is added to the definition
of $W(y)$, and therefore

$$
W^{\sigma'}(y)=W^\sigma(y)+\langle b\rangle,
\qquad
r^{\sigma'}(y)=\ell+1.
$$

Thus $y$ leaves $U_\ell$, proving (3).  Every later history only adds vectors
to each $W(y)$, so $r(y)$ never decreases.  A removed point cannot occur in
a later type-$\ell$ block.  This proves disjointness. $\square$

### Lemma 2: the sharp cardinality-to-rank conversion

For every set $R$ of projective points, (2) holds.  For each
$1\leq d\leq t+1$ it is sharp: taking all projective points of a fixed
$d$-dimensional vector subspace gives
$|R|=[d]_q$ and $\dim\operatorname{span}R=d$.

**Proof.** If $\dim\operatorname{span}R=d_R$, then all points of $R$ lie in
the projectivization of a $d_R$-dimensional vector space.  Its number of
$1$-spaces is exactly

$$
[d_R]_q=1+q+\cdots+q^{d_R-1}
=\frac{q^{d_R}-1}{q-1}.
$$

This proves the first inequality in (2); solving it for $d_R$ proves the
second.  The displayed subspace construction gives equality. $\square$

### Lemma 3: exact rank transverse to the current $W(b)$

For an unmarked extension $(a,b)$, put
$W=W^\sigma(b)$, $r=\dim W$, and

$$
d_{\rm rel}=\dim\big((W+\operatorname{span}R)/W\big).
$$

Then

$$
|R|\leq[r+d_{\rm rel}]_q,
\qquad
d_{\rm rel}\geq
\max\left\{0,
\left\lceil\log_q((q-1)|R|+1)\right\rceil-r
\right\},
\tag{4}
$$

and $W+\operatorname{span}R\subseteq a^\perp$.

**Proof.** Every generator $b_i$ of $W^\sigma(b)$ has $a_i\perp b$.
Consistency of the extension then gives $a\perp b_i$, so
$W\subseteq a^\perp$.  Definition (1) gives $R\subseteq a^\perp$ as well.
This proves the subspace inclusion.  The vector space
$W+\operatorname{span}R$ has dimension $r+d_{\rm rel}$ and contains every
projective point of $R$.  Counting its $1$-spaces gives the first inequality
in (4); inversion gives the second. $\square$

This is the precise transverse rank supplied by one block relative to its
current source span.  It does not measure rank transverse to the union of
spans already charged on earlier steps, which is the quantity a compound
encoding would need.

### Proposition 4: an actual rank-one unmarked family

For every prime power $q$ and every $t\geq2$, the forward-independent-tuple
tree of $D^*(t,q)$ contains a consistent history $\sigma$ of length
$1+(t-1)(q-1)=O_t(q)$ followed by $q$ consecutive unmarked children.  Their
literal removal blocks are distinct singletons $R_z$, but

$$
\dim\operatorname{span}R_z=1
\quad\hbox{for every }z\in\mathbb F_q,
\qquad
\dim\operatorname{span}\bigcup_{z\in\mathbb F_q}R_z=2.
\tag{5}
$$

In particular, neither a rank-two bound for each block nor additive
transverse rank across these $q$ disjoint blocks holds for all actual
unmarked paths.

**Proof.** Work in $V=\mathbb F_q^{t+1}$ with standard basis
$e_1,\ldots,e_{t+1}$, and define

$$
\mathcal A=\{\langle e_2\rangle\}
\cup\{\langle e_2+ce_j\rangle:
3\leq j\leq t+1,\ c\in\mathbb F_q^*\}.
\tag{6}
$$

The points in (6) are distinct, so $|\mathcal A|=1+(t-1)(q-1)$.  Let
$\sigma$ consist, in any order, of the pairs $(a,e_1)$ with
$a\in\mathcal A$.  Every pair is a vertex of $D^*$ because $a\perp e_1$.
For an earlier $a_i$ and a later $a_j$, the consistency implication has
antecedent $a_i\perp e_1$ and consequent $a_j\perp e_1$; both hold.  Hence
$\sigma$ is a vertex of the forward-independent-tuple tree.

All second coordinates in $\sigma$ equal $e_1$.  Consequently
$r^\sigma(y)=0$ precisely when $a\cdot y\ne0$ for every $a\in\mathcal A$.
The choice $a=e_2$ first forces $y_2\ne0$, so normalize $y_2=1$.  For each
$j\geq3$, the remaining conditions are

$$
1+cy_j\ne0\quad\hbox{for every }c\in\mathbb F_q^*.
\tag{7}
$$

If $y_j\ne0$, choosing $c=-y_j^{-1}$ contradicts (7).  Conversely, if every
$y_j=0$ for $j\geq3$, all conditions in (7) hold.  Therefore

$$
Z_0^\sigma
=\{\langle xe_1+e_2\rangle:x\in\mathbb F_q\},
\qquad |Z_0^\sigma|=q.
\tag{8}
$$

Write $y_z=\langle ze_1+e_2\rangle$ and
$a_z=\langle e_1-ze_2\rangle$.  Starting from $\sigma$, append the vertices
$(a_z,y_z)$ in any order.  We prove inductively that, if
$S\subseteq\mathbb F_q$ is the set of already processed labels, then

$$
Z_0=\{y_x:x\in\mathbb F_q\setminus S\}.
\tag{9}
$$

This is (8) when $S=\varnothing$.  Suppose $z\notin S$.  The candidate is a
vertex of $D^*$ because

$$
(e_1-ze_2)\cdot(ze_1+e_2)=z-z=0.
$$

For every original $a\in\mathcal A$, $a\cdot y_z=1$.  For every previously
processed $x\in S$,

$$
a_x\cdot y_z=z-x\ne0.
$$

Thus every old-to-new consistency antecedent is false, so the candidate
extends the current history.  For each unprocessed $x$, no previously added
$a$ is orthogonal to $y_x$, and hence $W(y_x)=\{0\}$.  On the new step,

$$
a_z\cdot y_x=x-z,
$$

so precisely $y_z$ leaves $U_0$.  Points outside the initial $Z_0$ cannot
enter it because every $r(y)$ is nondecreasing.  This proves (9) with
$S$ replaced by $S\cup\{z\}$.

It remains to verify that every step is literally unmarked.  Before
processing $z$, one has $r(y_z)=0$, so $r=\ell=0$.  Every current
$W(y_x)$ is zero, so $y_z$ is contained in zero such spans and is not
popular.  Exactly one current point, $y_z$, is orthogonal to $a_z$.  Since

$$
1>\frac{|Z_0|}{8q}\qquad (1\leq |Z_0|\leq q),
$$

$a_z$ is not poor.  Hence the child is unmarked and its literal block is
$R_z=\{y_z\}$.  After all $q$ steps the blocks are these $q$ points on a
projective line (equation (8) omits $\langle e_1\rangle$).  Each has rank one and their union spans
$\langle e_1,e_2\rangle$, of dimension two.  This proves (5). $\square$

This example, including all $q$ unmarked blocks, occurs within $O_t(q)$
steps.  It therefore remains inside the proposed $k=\Theta_t(q\log q)$
regime.  Under the extra marking rule of Lemma 5 below, a child of this family
is additionally marked precisely when its current $|Z_0|$ is at most $M_0$.
Thus, for fixed $M_0$ and $q>M_0$, the first
$q-\lfloor M_0\rfloor=\Theta(q)$ singleton blocks still remain unmarked.

The same obstruction persists at larger scales.  A hyperplane of $V$ has

$$
[t]_q=\Theta_t(q^{t-1})
$$

projective points but span dimension only $t$.  Hence a block can be very
large without supplying a comparably large number of independent witnesses.
Orthogonality to $a$ itself places every $R$ inside the hyperplane $a^\perp$,
so the projective-space example is a sharp cardinality-to-rank model
compatible with the orthogonality constraint in Lemma 1.

### Lemma 5: the free small-layer marking refinement

Fix constants $M_0,\ldots,M_t\geq0$.  In addition to Bradač's marked
children, mark every extension whose $b$ belongs to some $Z_r^\sigma$ with
$|Z_r^\sigma|\leq M_rq^r$.  This adds at most

$$
2\left(\sum_{r=0}^t M_r\right)q^t
\tag{10}
$$

marked children at every history.  Therefore every remaining unmarked child
of rank type $r$ satisfies $|Z_r^\sigma|>M_rq^r$.

**Proof.** For fixed $b\in Z_r^\sigma$, source equation (7) gives at most
$2q^{t-r}$ choices of $a$.  Thus the extensions from a small layer are at
most

$$
|Z_r^\sigma|\,2q^{t-r}\leq2M_rq^t.
$$

Sum over $0\leq r\leq t$. $\square$

This strengthening is real but insufficient.  Since the source chooses
$\ell$ so that $|Z_\ell|$ is largest among
$|Z_0|,\ldots,|Z_r|$, one actually has

$$
|Z_\ell|\geq |Z_r|>M_rq^r,
\qquad
|R|>\frac{M_r}{16}q^{r-1}.
$$

Combining this with Lemma 2 gives an exact within-block rank lower bound.  In
particular, for fixed $M_r>0$, $r\geq2$, and sufficiently large $q$, it forces
$\dim\operatorname{span}R\geq r$.  What it still does not provide is rank
transverse to spans already charged on other steps.  Large blocks from
different steps can repeatedly lie in the same low-dimensional projective
subspace, as Proposition 4 demonstrates for $\Theta(q)$ surviving singleton
blocks when $r=0$.

## What lemma would actually close the logarithmic improvement?

> **Superseding notice (2026-08-12).**  The uniform, all-length record-map
> target stated below is false.  The rank-zero saturation construction in
> [TRANSVERSE_ENCODING_ATTEMPT.md](./TRANSVERSE_ENCODING_ATTEMPT.md) gives
> $k_q=\lfloor(t-1)q\log q/12\rfloor$ consecutive unmarked type-zero steps
> and at least $L_q$ realizing paths, where
> $L_q/(C_tq^t)^{k_q}=\exp(\Omega_t(q\log^2q))$ for every fixed $C_t$.
> Thus $\exp(O_t(q\log q))$ records with at most $(C_tq^t)^u$ preimages
> cannot cover even the all-unmarked signature at this length.  The target is
> retained below to record the failed mechanism, not as a live conjecture.
> This counterexample does **not** rule out a statement restricted to
> $k\geq A_tq\log q$ for a sufficiently large $A_t$; such a statement would
> require a new quantitative tail-entropy argument, which is not currently
> proved.

A sufficient new statement would have to control multiplicity or transverse
rank, not merely the union size.  The following was the original candidate;
the superseding notice explains why it is now retained only as a failed
target:

> **Transverse block-encoding lemma (false in this uniform form).**  Fix an
> ordering of the marked children at every tree vertex.  For every length-$k$ marked/unmarked
> signature with $u$ unmarked positions and every fixed sequence of the local
> marked-child indices, the paths realizing those data admit a record map with
> at most $\exp(O_t(q\log q))$ possible record values, each having at most
> $(C_tq^t)^u$ preimages.  The record may contain certificates
> $E_i\subseteq R_i$ from the literal blocks of Lemma 1, but both the number of
> possible records and the multiplicity of each record must obey these bounds.

One possible way to prove this would be a bounded-multiplicity statement for
the maps

$$
(a,b,\sigma)\longmapsto
(\ell,\operatorname{span}E,\text{transition of the }U_j),
$$

together with a lower bound on new rank after quotienting by spans already
charged at earlier steps.  Neither property is contained in Bradač
Claim 2.13.  Proving only that the literal $R_i$ are disjoint does not suffice:
many disjoint subsets may lie in one projective hyperplane and share the same
orthogonality constraint on $a$.

This formulation explicitly counts the certificate records; merely bounding
the paths compatible with one chosen certificate family would not suffice.
Had this uniform lemma held, summing over signatures and the at most $h$
marked choices at each marked step would have given

$$
2^k h^{k-u}(C_tq^t)^u\exp(O_t(q\log q)).
$$

For $k\gtrsim_t q\log q$ this is $(C'_tq^t)^k$, so the existing sampling
argument would give

$$
r(s,k)\geq
\Omega_s\!\left(\frac{k^{s-1}}{(\log k)^{s-2}}\right).
$$

The implication itself remains a valid counterfactual calculation, but its
premise is false in this uniform form.  No Ramsey lower-bound improvement is
claimed here.

## Explicit HMS-threshold audit

The alternative route cannot presently produce a source-level numeric
$C_0$.  HMS Appendix-B line 973 declares the relevant $O$ constants
absolute, but Proposition B.2 uses an unspecified coefficient in

$$
1+O\!\left(\frac{\sqrt{\log(1/p)}}D\right),
$$

and lines 1308--1336 introduce further sequential $o(1)$ terms.  The proof
of [HMS_APPENDIX_BRIDGE.md](./HMS_APPENDIX_BRIDGE.md) deliberately freezes
the first coefficient as a symbolic $K$; its theorem is therefore valid for
sufficiently large fixed $C$, but the frozen source statement contains no
number from which a certified $C_0$ can be computed.

It may be possible to replace the source's red $O$ by the exact compact-window
envelope already developed in the bridge and then redo every blue and
extraction inequality with explicit constants.  That would be a new proof,
not a numerical evaluation of the frozen theorem, and it remains open here.

## Executable check

Run

```bash
python3 routes/lower/bradac_multiwitness_obstruction.py
```

The script verifies the exact projective point counts, their rank thresholds,
and the hyperplane counterexamples.  Over the prime fields tested, it also
enumerates all projective points and directly replays every condition in
Proposition 4.  These are finite checks, not a proof of the open encoding
lemma; the written field-theoretic proof covers all prime powers.

## Open risks

- Proposition 4 rules out both a uniform per-block rank-two claim and naive
  additive rank across $q$ consecutive blocks.  An $O(q)$ exceptional pattern
  can still be absorbed by an $\exp(O_t(q\log q))$ budget, so it does not rule
  out a subtler global encoding.
- A sharper analysis of consistency may force additional transverse
  structure not visible in the current proof.  That is the correct place for
  the next attack.
- The source's asymptotic $q\log^2q$ threshold remains the established one;
  this document does not improve a published Ramsey lower bound.
