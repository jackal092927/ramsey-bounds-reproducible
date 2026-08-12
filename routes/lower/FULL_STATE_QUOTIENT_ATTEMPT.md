# Full-state quotient attempt after the cross-type obstruction

Date: 2026-08-12  
Primary source and normalization: Bradač,
[arXiv:2605.28793v3](https://arxiv.org/abs/2605.28793v3), especially the
consistent-tuple tree and $W^\sigma(y)$ in Claim 2.13.  The exact legality
and transition formulas used here are Lemmas 1 and 6 of
[`CROSS_TYPE_TRANSFER_ATTEMPT.md`](./CROSS_TYPE_TRANSFER_ATTEMPT.md).

## Headline result

There is a rigorous quotient of the full Markov state, but it is a symmetry
quotient rather than the desired constant-dimensional statistic.

1. The orbits of the full state $y\mapsto W^\sigma(y)$ under the projective
   orthogonal group form an **exact strong lumping** of the pair-labelled
   transfer operator.
2. Every positive transfer supersolution can be averaged over this group.
   Consequently, restricting a Perron-weight or domination search to
   orbit-invariant weights loses nothing.
3. The small incidence refinement

   $$
   M_{r,e}=\#\{y:\dim W(y)=r,\ \mathbf 1_{\{y\subseteq W(y)\}}=e\}
   \tag{1}
   $$

   determines the *current* legal fanout exactly, but it is not Markov and
   is not strongly lumpable.  An explicit reachable counterexample occurs
   already for $t=2,q=2$.

Thus the symmetry route is **PROVABLE BUT NOT YET BOUND-IMPROVING**.  It
gives a lossless reduced operator on which a new positive or signed weight
could be sought.  It does not prove the $k\geq A_tq\log q$ tuple estimate,
does not force eventual source-type diversification, and does not improve a
Ramsey lower bound.

## Setup

Let $V=\mathbb F_q^{t+1}$ with the source's nondegenerate bilinear form, and
write $\mathcal P=PG(t,q)$.  For a reachable history $\sigma$, its full state
is

$$
\mathcal W_\sigma=(W^\sigma(y))_{y\in\mathcal P}.
\tag{2}
$$

For a projective pair $(a,b)$, the exact formulas from the preceding audit
are

$$
(a,b)\text{ legal at }\mathcal W
\iff a\perp b\text{ and }a\perp W(b),
\tag{3}
$$

and

$$
W^{(a,b)}(y)=
\begin{cases}
W(y)+\langle b\rangle,&a\perp y,\\
W(y),&a\not\perp y.
\end{cases}
\tag{4}
$$

On functions of full states, define

$$
(Tf)(\mathcal W)=
\sum_{(a,b)\text{ legal at }\mathcal W}
f(\mathcal W^{(a,b)}).
\tag{5}
$$

All multiplicities below count projective pair labels $(a,b)$, exactly as
in (5).  Collapsing distinct labels that happen to yield the same successor
would change the tuple count and is not done.

Let $G=PO(V)$ be the projective image of the orthogonal group.  Its action on
full states is

$$
(g\mathcal W)(gy)=gW(y).
\tag{6}
$$

This is well-defined on projective points and subspaces; scalar matrices
act trivially.

## Theorem 1: orthogonal orbits are an exact strong lumping

For every $g\in G$, every full state $\mathcal W$, and every projective pair
$(a,b)$:

$$
(a,b)\text{ is legal at }\mathcal W
\iff
(ga,gb)\text{ is legal at }g\mathcal W,
\tag{7}
$$

and, whenever they are legal,

$$
g(\mathcal W^{(a,b)})
=(g\mathcal W)^{(ga,gb)}.
\tag{8}
$$

Consequently, if $[\mathcal W]$ denotes a $G$-orbit, then

$$
\overline T_{[\mathcal W],[\mathcal X]}
=\#\{(a,b)\text{ legal at }\mathcal W:
       [\mathcal W^{(a,b)}]=[\mathcal X]\}
\tag{9}
$$

is independent of the representative $\mathcal W$.  The matrix
$\overline T$ is therefore an exact quotient of $T$.  Starting at the empty
state, quotient powers reproduce the full pair-labelled path counts
exactly.

**Proof.**  An orthogonal transformation is a bijection of projective
points and preserves orthogonality.  It also satisfies
$g(W+\langle b\rangle)=gW+\langle gb\rangle$.  Applying these facts to
(3) proves (7), and applying them pointwise to (4) proves (8).

If $\mathcal W_2=g\mathcal W_1$, the label map
$(a,b)\mapsto(ga,gb)$ is a multiplicity-preserving bijection between their
legal children.  By (8), it also preserves the successor orbit.  Therefore
the number in (9) is the same for $\mathcal W_1$ and $\mathcal W_2$, which
is strong lumpability.  The empty state is fixed by $G$, so induction on
the path length gives equality of full and quotient path counts. $\square$

### Corollary 2: orbit-invariant weights lose no positive domination power

Suppose $h>0$ on the finite reachable full-state space and

$$
Th\leq\Lambda h.
\tag{10}
$$

Then

$$
h_G(\mathcal W)=\frac1{|G|}\sum_{g\in G}h(g\mathcal W)
\tag{11}
$$

is positive, constant on $G$-orbits, and still satisfies
$Th_G\leq\Lambda h_G$.  Moreover,

$$
\rho(T)=\rho(\overline T)
\tag{12}
$$

on the finite reachable state graph.

**Proof.**  Equations (7)--(8) say exactly that $T$ commutes with the
permutation action of every $g\in G$.  Average (10) over $G$ to get the
first claim.  For (12), a nonnegative matrix has a nonzero nonnegative
eigenvector at its spectral radius.  Averaging such a vector over $G$
cannot give zero and produces an invariant eigenvector with the same
eigenvalue.  Hence the full spectral radius occurs on the invariant
subspace represented by $\overline T$.  Conversely, every quotient
eigenvector lifts to an invariant full-state eigenvector, proving equality.
$\square$

This corollary is the useful content of the quotient: a future transfer
weight may be searched on orbits without an unproved symmetry ansatz.

## Lemma 3: a constant-dimensional feature gives the exact present fanout

Let $M_{r,e}$ be (1), where $0\leq r\leq t+1$ and $e\in\{0,1\}$.  With

$$
[d]_q=\frac{q^d-1}{q-1},
\tag{13}
$$

the number of legal pair labels at $\mathcal W$ is exactly

$$
\Delta(\mathcal W)
=\sum_{\substack{0\leq r\leq t+1,\ e\in\{0,1\}\\
                  r+1-e\leq t+1}}
M_{r,e}\,[t-r+e]_q,
\tag{14}
$$

The omitted cell $M_{t+1,0}$ is formally impossible: a full-dimensional
space contains $b$.

**Proof.**  Fix $b$.  By (3), legal $a$ are the projective points in

$$
(W(b)+\langle b\rangle)^\perp.
$$

If $r=\dim W(b)$ and $e=\mathbf1_{\{b\subseteq W(b)\}}$, then

$$
\dim(W(b)+\langle b\rangle)=r+1-e.
$$

Nondegeneracy makes the orthogonal complement have dimension
$t-r+e$, hence it contains $[t-r+e]_q$ projective points.  Sum over $b$
and group equal $(r,e)$ cells. $\square$

The vector $(M_{r,e})$ strictly refines the rank/cutoff profile because it
retains whether the label point lies in its own assigned subspace.  Formula
(14) is an exact one-step domination input.  The next proposition shows why
it cannot simply be iterated.

## Proposition 4: the self-incidence profile is not lumpable

Take $t=2,q=2$ and identify the seven projective points with their unique
nonzero vectors in $\mathbb F_2^3$.  The following two length-three
consistent histories are legal:

$$
\begin{aligned}
\sigma={}&((001,010),(010,001),(100,011)),\\
\tau={}&((001,010),(100,001),(010,101)).
\end{aligned}
\tag{15}
$$

Their full states, in point order
$001,010,011,100,101,110,111$, are

| $y$ | $W^\sigma(y)$ | $W^\tau(y)$ |
|---|---|---|
| $001$ | $\langle010,001\rangle$ | $\langle100,001\rangle$ |
| $010$ | $\langle010,001\rangle$ | $\langle010,001\rangle$ |
| $011$ | $\langle011\rangle$ | $\langle001\rangle$ |
| $100$ | $\langle010,001\rangle$ | $\langle101,010\rangle$ |
| $101$ | $\langle001\rangle$ | $\langle101\rangle$ |
| $110$ | $\langle010\rangle$ | $\langle010\rangle$ |
| $111$ | $0$ | $0$ |

Both have, in the order

$$
(M_{0,0},M_{0,1},M_{1,0},M_{1,1},
  M_{2,0},M_{2,1},M_{3,0},M_{3,1}),
$$

the same profile

$$
P=(1,0,2,1,1,2,0,0).
\tag{16}
$$

By (14), both have current fanout $10$.  Nevertheless, the successor
profile

$$
Q=(0,0,1,2,2,1,0,1)
\tag{17}
$$

has multiplicity two from $\sigma$, via labels

$$
(101,111),\quad(110,111),
$$

but multiplicity one from $\tau$, via only

$$
(110,111).
$$

Therefore two states with the same $(M_{r,e})$ have different
multiplicity distributions over successor $(M_{r,e})$ profiles.  This
refinement is not a strong lumping and is not a closed Markov state.
$\square$

Every entry in (15)--(17) follows by the pointwise rule (4).  The checker
below independently reconstructs the histories, legal labels, profiles,
and successor multiplicities; the counterexample does not depend on a
floating-point or optimization calculation.

## Exact finite diagnostics

Run

```bash
python3 routes/lower/full_state_quotient_check.py --t 2 --q 2
python3 routes/lower/full_state_quotient_check.py --t 2 --q 3 --depth 2
```

The checker uses prime-field arithmetic and the standard dot product, as in
the earlier exact state explorer.  Results:

| field | tested state set | projective orthogonal actions | represented orbit classes | orbit lumping | self-incidence lumping |
|---|---:|---:|---:|---|---|
| $t=2,q=2$ | all $23{,}962$ reachable states | $6$ | $4{,}243$ | PASS | FAIL, witness (15) |
| $t=2,q=3$ | $1{,}314$ states reachable through depth $2$ | $24$ | $91$ | PASS | no failure at this shallow depth |

For $q=3$, the $1{,}314$ states consist of $1,52,1261$ newly reached
states at depths $0,1,2$.  This is explicitly a bounded diagnostic, not a
claim that the small profile lumps the complete $q=3$ graph.  The orbit
lumping PASS is a check of Theorem 1, whose proof is field-independent.

## What is resolved and what remains open

- **Full-state Markov rule:** exact, as in the preceding cross-type audit.
- **Projective-orthogonal orbit quotient:** **PROVABLE AS STATED** and exact
  with pair-label multiplicities.
- **Restriction to orbit-invariant positive weights:** **PROVABLE AS
  STATED**; no Perron/supersolution power is lost.
- **Self-incidence profile determines present fanout:** **PROVABLE AS
  STATED**, by (14).
- **Self-incidence profile is a closed transfer state:** **FALSE**, by the
  reachable $t=2,q=2$ counterexample.
- **A smaller incidence/intersection quotient with a uniform asymptotic
  domination inequality:** **OPEN / NOT CURRENTLY JUSTIFIED**.
- **Forced diversification by $A_tq\log q$ for some sufficiently large
  constant $A_t$:** **OPEN**.  Nothing in the finite counterexample or the
  orbit lemma proves or disproves this eventual statement.
- **Bradač tuple threshold improved from $q(\log q)^2$ to $q\log q$:**
  **NOT CURRENTLY JUSTIFIED**.
- **New Ramsey lower bound:** **NONE**.

The next proof-bearing cut is now narrower: construct an orbit-invariant
weight that uses correlations beyond $(M_{r,e})$, or prove a domination
inequality for a labelled incidence statistic such as the joint data of
$W(b)$ with the hyperplane sections $W(y)$ on $y\perp a$.  Merely adding
unlabelled rank or self-incidence histograms cannot reproduce the required
successor correlations.
