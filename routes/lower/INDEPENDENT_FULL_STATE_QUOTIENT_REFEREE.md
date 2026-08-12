# Independent adversarial review: full-state quotient attempt

Date: **2026-08-12**

Reviewed artifacts:

- `FULL_STATE_QUOTIENT_ATTEMPT.md`, SHA-256
  `eaf12acab4148a5f8344e08e42cb786af1c3c74e3c1ba176f350d989b9f7a560`;
- `full_state_quotient_check.py`, SHA-256
  `20a6f135262f2a51f3d3622a13984d3965b0334c6396d40fddd90bf0e4f13e85`.

Imported exact-state dependency:

- `cross_type_transfer_check.py`, SHA-256
  `309625aab3630678445b91d5f0f378820b13e856e47b92313bebf1e12f426c52`.

## Verdict

```text
PASS
EXACT SYMMETRY QUOTIENT, BUT NO CONSTANT-DIMENSIONAL MARKOV QUOTIENT
NO NEW TUPLE ESTIMATE OR RAMSEY LOWER BOUND
```

I found no fatal gap in the analytic claims.  The projective-orthogonal
orbit partition is an exact strong lumping of the **pair-labelled** full-state
operator.  Averaging a positive supersolution is valid, and the full and
orbit-quotient operators have equal spectral radius on the finite reachable
graph.  The displayed self-incidence statistic gives the present row sum
exactly, while the two legal length-three histories really do show that it is
not a strong lumping.

The executable is a finite diagnostic only.  In particular, its complete
`q=2` enumeration and depth-two `q=3` check do not prove an asymptotic tuple
estimate, a uniform domination inequality, or the desired
`A_t q log q` threshold.  The reviewed document states this boundary
correctly.

## 1. Full-state action and reachability

For a projective isometry `g`, define

$$
(g\mathcal W)(gy)=gW(y).
$$

This is well-defined: changing vector representatives does not change a
projective point or a linear subspace, and an element of the projective image
has the same action for scalar-equivalent representatives.  Orthogonal maps
preserve both incidences used in the transition:

$$
a\perp b,\qquad a\perp W(b).
$$

They also commute with the update because

$$
g(W(y)+\langle b\rangle)=gW(y)+\langle gb\rangle.
$$

Thus `(a,b) -> (ga,gb)` is a bijection on legal pair labels and maps the
corresponding child state equivariantly.  This argument works for every full
state on which the displayed transfer rule is defined, hence in particular
for every reachable state.  The empty state is fixed, so the forward
reachable set is group-invariant and transition-closed.

**Action/reachability verdict: PASS.**

## 2. Pair-labelled strong lumping

The relevant strong-lumping quantifier is not merely equality of total
fanout.  For any two representatives in the same orbit and for **every**
successor orbit, the sum of transition multiplicities into that orbit must
agree.  The label bijection above proves exactly this: it preserves each
individual pair label and sends its child to the corresponding child orbit.
Distinct labels that produce the same full state remain distinct summands,
as required for ordered-tuple counts.

Consequently

$$
\overline T_{[\mathcal W],[\mathcal X]}
=\#\{(a,b): (a,b)\text{ legal at }\mathcal W,
             [\mathcal W^{(a,b)}]=[\mathcal X]\}
$$

does not depend on the representative.  Lifting an orbit function to a
group-invariant full-state function intertwines `T` and `\overline T`.
Since the initial state is a singleton orbit, induction gives exact equality
of the full and quotient pair-labelled path counts at every finite depth.

**Strong-lumping verdict: PASS.**

## 3. Positive supersolutions and spectral radius

Let `P_g` be the permutation action on functions.  Equivariance gives
`T P_g=P_g T`.  If `h>0` and `Th<=Lambda h`, then summing the permuted
inequalities gives

$$
T\left(\frac1{|G|}\sum_gP_gh\right)
\leq\Lambda\left(\frac1{|G|}\sum_gP_gh\right).
$$

The average remains strictly positive and is orbit-invariant.  No
irreducibility assumption is needed.

The reachable full-state set is finite because each coordinate `W(y)` ranges
over the finite subspace lattice of a finite vector space.  For the resulting
finite nonnegative matrix, Perron--Frobenius supplies a nonzero nonnegative
right eigenvector at `rho(T)`, even if the matrix is reducible.  Its group
average cannot vanish and is an invariant eigenvector at the same eigenvalue.
Therefore `rho(T)` occurs in the invariant subspace.  Conversely, every
quotient eigenvector lifts to an invariant full-state eigenvector, yielding

$$
\rho(T)=\rho(\overline T).
$$

This equality is exact for the finite reachable operator.  By itself it does
not provide a useful uniform-in-`q` bound on that spectral radius or on
finite-depth transient factors; the main document does not claim otherwise.

**Supersolution/spectral verdict: PASS.**

## 4. Exact fanout from the self-incidence profile

Fix a projective label `b` and put

$$
r=\dim W(b),\qquad e=\mathbf1_{\{b\subseteq W(b)\}}.
$$

The legal first coordinates are precisely the projective points of

$$
(W(b)+\langle b\rangle)^\perp.
$$

The space inside the perpendicular has dimension `r+1-e`; nondegeneracy
makes its orthogonal complement have dimension `t-r+e`.  It therefore
contains `[t-r+e]_q` projective points.  Summing over all `b` proves

$$
\Delta(\mathcal W)=\sum_{r,e}M_{r,e}[t-r+e]_q.
$$

The formally problematic cell `M_{t+1,0}` is impossible, because a
full-dimensional `W(b)` contains `b`; `M_{0,1}` is likewise automatically
zero.  The zero-dimensional complement at `(r,e)=(t+1,1)` contributes
`[0]_q=0` as it should.

The statistic refines the unlabelled rank profile since summing its two
`e`-cells recovers each rank count.  In an independent `t=2,q=2`
enumeration I also found reachable equal-rank states with distinct
self-incidence profiles, confirming that the refinement is strict, though
strictness is not needed for the fanout identity.

**Fanout verdict: PASS.**

## 5. Explicit failure of self-incidence lumpability

I reconstructed both advertised histories directly over `F_2^3`, using
the seven nonzero vectors as projective points.  At every step I checked

$$
a\perp b\quad\text{and}\quad a\perp W(b),
$$

so both length-three histories are reachable legal histories, not relaxed
states.  Pointwise application of the update rule reproduces the displayed
two full-state tables and the common profile

$$
P=(1,0,2,1,1,2,0,0).
$$

Both states have current labelled fanout `10`.  For the target successor
profile

$$
Q=(0,0,1,2,2,1,0,1),
$$

the first history has precisely the two legal labels

$$
(101,111),\qquad(110,111),
$$

whereas the second has only `(110,111)`.  Thus equal current profiles have
different multiplicity into the same successor-profile cell.  This is the
right quantifier to disprove strong lumpability.

The counterexample does not say that no one-sided domination based on a
richer incidence statistic exists.  It only rules out iterating this exact
small profile as a closed Markov state.

**Non-lumpability witness verdict: PASS.**

## 6. Independent finite reconstruction and checker audit

I ran the supplied checker and separately rebuilt the `t=2,q=2` state graph
with a bit-mask subspace representation rather than importing its state or
matrix routines.  The independent reconstruction gave:

```text
projective points:                 7
legal root pair labels:           21
reachable full states:        23,962
pair-labelled transitions:   134,883
projective orthogonal actions:      6
orthogonal state orbits:         4,243
fanout identity:                  PASS
orbit strong lumping:             PASS
explicit P -> Q multiplicities:   2 vs 1
```

The supplied executable also reproduced all these values.  Its bounded
`t=2,q=3` run found `1,314` states through depth two, `24` distinct
projective orthogonal actions and `91` represented orbits, with no orbit
lumping failure.  That run checks transitions from the tested states even
when children lie beyond depth two, but it is still only a bounded
diagnostic.

The implementation deliberately handles prime fields through ordinary
modular arithmetic; it is not an implementation of general finite fields.
It imports the earlier `Explorer`, so the supplied script alone is not an
independent implementation of the transition rule.  The separate bit-mask
reconstruction above resolves that independence concern for the complete
`q=2` instance.  Neither finite program is a premise of the analytic
group-action proof.

**Executable verdict: PASS AS A FINITE DIAGNOSTIC.**

## Final claim boundary

The reviewed package establishes exactly the following:

1. The full `W`-state transfer is equivariant under the projective
   orthogonal group.
2. Its orbit partition is an exact strong lumping with pair-label
   multiplicities and exact path-count preservation from the empty state.
3. Positive supersolutions may be symmetrized without loss, and the finite
   reachable full and quotient operators have equal spectral radius.
4. `(M_{r,e})` determines the present fanout exactly.
5. `(M_{r,e})` is not a closed Markov quotient, already on two reachable
   `t=2,q=2` histories.

It does **not** establish a tractably small orbit count, a constant-size
quotient, an asymptotic bound for the quotient spectral radius, forced
source-type diversification, the tuple threshold `A_t q log q`, or any new
Ramsey lower bound.  A bound-improving continuation still needs a new
orbit-invariant weight or a proved one-sided compression retaining the
missing labelled incidence correlations.
