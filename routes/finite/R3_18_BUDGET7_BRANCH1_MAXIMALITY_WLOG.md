# Branch-1 maximality WLOG audit

This note records a bounded, independently reproducible audit of a
maximality normalization for the exact-seven, one-sided repair problem.  It
is a checker/design ledger, not a branch-closure claim and not a Ramsey-number
improvement.

## Setting

Let $H$ be the authenticated 100-vertex seed graph and let $F$ be a
triangle-free graph on the same vertex set.  The one-sided distance is

\[
d_H(F)=|E(H)\setminus E(F)|.
\]

Thus adding an original nonedge of $H$ is free.  An exact-seven target has
$d_H(F)=7$ and $\alpha(F)<18$.  The branch-1 relaxation additionally fixes
$(97,99)\notin E(F)$, but this branch unit is not part of the definition of a
global target.

## Layer A: original-nonedge saturation

Suppose $uv\notin E(H)\cup E(F)$ and $u,v$ have no common neighbour in
$F$.  Add $uv$.

1. No triangle is created, because any new triangle would provide a common
   neighbour of $u,v$ before the addition.
2. Adding an edge cannot create a new independent set, so the independence
   number does not increase.
3. Because $uv\notin E(H)$, the set $E(H)\setminus E(F)$, including its
   exact cardinality and its full deletion support, is unchanged.

Repeat this operation in lexicographic order.  The finite edge universe makes
the process terminate.  At termination every still-absent original nonedge
has a common neighbour.  Consequently the existence of an exact-seven target
is equivalent to the existence of one that is saturated on original
nonedges.  This is a WLOG existence statement; it does **not** say that every
raw target is already saturated.  It uses no radius lower bound.

There is no conflict with the degree-17 cap.  In a genuine triangle-free
target, every neighbourhood is independent, so $\alpha(F)<18$ itself implies
$\Delta(F)\le17$.  A triangle-safe addition that produced degree 18 would
exhibit an independent 18-neighbourhood and therefore cannot arise from a
genuine target.  It can arise in an incomplete finite-bank relaxation; in
that case the original relaxation assignment is eliminated by the saturation
constraint, and its degree-18 completion is not asserted to remain a model of
the degree-capped relaxation.

## Layer B: full maximal triangle-freeness

The authenticated budget-six summary excludes every target at one-sided
distance at most six while allowing arbitrary original-nonedge additions.
Therefore every deleted seed edge of an exact-seven target already has a
common neighbour: if one could be safely added back, triangle-freeness and
$\alpha<18$ would persist while the one-sided distance became exactly six.

This argument also covers the fixed branch edge $(97,99)$.  If it could be
safely added, at least one of the other two edges of the seed's unique triangle
on $97,98,99$ would still be absent.  The resulting six-deletion graph is
therefore covered by one of the authenticated global three branch cases; it
need not remain in branch 1.

Layer-A additions cannot destroy an existing common neighbour.  Combining the
two layers gives the conditional equivalence

\[
\text{exact-seven target exists}
\quad\Longleftrightarrow\quad
\text{exact-seven maximal triangle-free target exists},
\]

where only the right-to-left direction is immediate and the left-to-right
normalization uses the checked budget-six dependency for deleted seed edges.
For order 100, maximal triangle-free is equivalent to every nonedge having a
common neighbour, and hence to connected diameter at most two.

## Certifiable selector encoding

For a scoped pair $uv$, introduce a Boolean $y_{uv,w}$ for every
$w\notin\{u,v\}$ and add

\[
x_{uv}\vee\bigvee_w y_{uv,w},\qquad
\neg y_{uv,w}\vee x_{uw},\qquad
\neg y_{uv,w}\vee x_{vw}.
\]

If $uv$ is absent, the long clause selects a real common neighbour.  If it
is present, all witnesses may be false.  Reverse Tseitin implications are not
needed: the auxiliaries are existential witnesses, and the displayed clauses
are satisfiable for a fixed primary graph exactly when the scoped pair is
present or has a common neighbour.

The safer first encoding is Layer A only: 4,123 original nonedges, 404,054
auxiliaries and 812,231 clauses.  Applied to the common formula it has
1,530,683 clauses; applied to A+ it has 1,534,783.  Full Layer B covers all
4,950 pairs and uses 485,100 auxiliaries and 975,150 clauses.  A single lazy
pair costs 98 auxiliaries and 197 clauses.

A lazy run is claim-safe only if its discovered pair set is frozen and sorted,
the auxiliary variables are deterministically renumbered after variable
154,190, and one deterministic final CNF is rebuilt.  UNSAT needs independent
DRAT/LRAT replay.  SAT needs a complete model plus a direct maximality scan.
UNKNOWN, timeout, malformed output, or unchecked UNSAT supports no claim.

## Authenticated model telemetry

The common model has degree distribution $50\times16+50\times17$ and one
Layer-A violation, $(37,86)$, with endpoint degrees 16 and 17.  Adding it is
triangle-safe and preserves the seven-edge deletion support, but produces one
degree-18 vertex.  This pair is exactly the prior domination witness, with
I18 mask `2000000404414192982822020`; it diagnoses the incomplete bank rather
than producing a surviving degree-capped completion.

The checked A+ assignment has degree distribution $54\times16+46\times17$
and exactly three Layer-A violations:

- `(16,64)`;
- `(32,98)`;
- `(40,89)`.

All six endpoints have degree 16.  Adding these three pairs yields a
triangle-free maximal completion with the same deletion support and degree
distribution $48\times16+52\times17$.  Therefore Layer A excludes the
**current exact assignment**, but the **same deletion support survives** by a
deterministic primary-graph completion.  The old DIMACS auxiliary assignment
is not reused; a solver-ready CNF would re-extend the unchanged deletion and
degree counts with fresh counter auxiliaries.  The completion also retains
the already known
historical/fixed-base independent-18 witness
`bfffe00000000000000000000`.  This is not a branch closure.

All four observed violation pairs lie outside the frozen 396 no-addition
units; the independent local deletion-minimum audit gives two for each.  The
396 units and maximality constraints are complementary: a no-addition unit
fixes $x_{uv}=0$, while maximality then requires a common-neighbour witness.
The three A+ pairs have degree 16 at both endpoints and produce no domination
I18 separator.  Maximality normalization also does not replace ordinary I18
CEGAR: a maximal relaxation model may still contain an independent 18-set.

## Bounded decision rule

The recommended pilot is Layer-A lazy separation only, followed by at most one
300-second solve after a deterministic no-solver CNF audit.  Do not launch a
second round automatically.

A checked UNSAT result excludes only the frozen WLOG-augmented branch
relaxation.  A SAT result is telemetry unless it independently verifies a full
target with $\alpha<18$.  The deterministic three-edge completion of the
current A+ model, retention of only the known I18 witness, or UNKNOWN is a
no-go for further unbounded search.

## Reproduction

With the two authenticated gzip models available locally, run:

```bash
python3 routes/finite/check_r3_18_budget7_branch1_maximality_wlog.py \
  --common-model /tmp/ramsey-branch1-common-model-9057db25.gz \
  --Aplus-model /tmp/ramsey-branch1-Aplus-sat-model-19db55d0.gz \
  --Aplus-gate routes/finite/certificates/r3_18_budget7_branch1_cegar_Aplus_f24_endpoint/branch1_cegar_gate.json

python3 -m unittest \
  routes.finite.test_check_r3_18_budget7_branch1_maximality_wlog -v
```

The checker authenticates all small tracked dependencies and both complete
model files, reconstructs the machine ledger, and requires byte-for-byte JSON
equality.  It does not invoke a SAT solver.
