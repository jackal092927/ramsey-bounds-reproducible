# Branch-1 bounded structural-projection audit

Date: 2026-08-30

This ledger records solver-free or model-evaluation checks around the four
proof-verified branch-1 retention units.  It is deliberately narrower than a
branch closure.  In particular, it does **not** prove a vertex-18 deletion hit,
does **not** prove that no stronger support inequality exists, and does **not**
promote the exact-seven layer beyond `UNKNOWN`.

## Reproduction

The canonical checker uses only the Python standard library.  The domination
record requires the frozen complete common-model artifact; the 391,052-byte
gzip is a release/run asset and is intentionally not duplicated in Git.

```bash
python routes/finite/check_r3_18_budget7_branch1_structural_projection.py \
  --common-model /path/to/branch1_common.model.gz

python -m unittest \
  routes.finite.test_check_r3_18_budget7_branch1_structural_projection -v
```

The canonical run returned

```text
VERIFIED_BOUNDED_STRUCTURAL_PROJECTION_FACTS: record=06fd57c94c5d21a1a9f9c50845ae0126ccbc5e9e5880fa54db752819afadf617 no_add=396 domination_cuts=1 local_bank_violations=12
```

Frozen input identities are:

| input | bytes/count | SHA-256 or ordered-mask SHA-256 |
|---|---:|---|
| seed matrix | 20,000 bytes | `e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e` |
| universal bank | 251,771 masks | file `91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b`; ordered `f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa` |
| historical union | 64,591 masks | file `d5100bb5dce48da3ca8ab3810290ff553ebb9d6c87ff9df1f287700563f456b0`; ordered `74b4b99c18e925a7a1bbb0e4a1636dad4bf8741ba67623c2164f3607a65172a8` |
| A+ batch | 4,096 masks | file `835137c2df19bc851618761cc0af92400b3fa2677dd00c47101d1074c7406e8b`; ordered `a3cff8d8a4c77c6effb49c03e76065a17f754d0a7de727d229652276b6e8cda0` |
| common SAT model | 391,052 bytes | gzip `9057db25b785640345e6f724cb1c79313642bb62ec2a19d9f310e25700de024d`; raw `51e7832b69a18b29db817d1e180f1a071f771fbb50e358de4fb57a3810cd737e` |

The checker, tests, and machine ledger have SHA-256 values
`84c86184dcb83264b4f84c2a669c8065c74db0e3dffac30b4273ac8cf987f134`,
`3c2774cadba243ea0f25c4180f620206626c10b519d7a98a9a5d1eadb842e62e`,
and `25a4120d85b58ac8afc93d6047dee3acf917917647bca447c736cd064ec3ab4d`,
respectively.

## Triangle-and-degree projection

After fixing `(97,99)` absent, the 826-edge base is triangle-free.  Its degree
distribution is 49 vertices of degree 16, 50 of degree 17, and only vertex 98
of degree 18.  Hence the degree cap gives the deletion-support condition

```text
D intersects delta(98).
```

Together with exact six residual seed deletions and the four retention units,
this condition is also sufficient for the triangle-and-degree subsystem: take
all original nonedges absent.  Deleting seed edges cannot create a triangle or
increase a degree.  Thus this subsystem yields no stronger support-only
condition than exact six, the four forbidden deletions, and the vertex-98 hit.
This is a projection statement about that subsystem only; the I18 bank is not
being projected here.

The four positive edges form the isolated edge `11-62` and the three-edge star
centered at 18.  Triangle clauses directly imply exactly

```text
x_61,64 = x_61,69 = x_64,69 = 0.
```

## Complete bounded no-addition closure

There are 4,124 fixed-base nonedges when the already-fixed `(97,99)` variable
is included.  Their fixed-base common-neighbour distribution is

```text
1:738, 2:1498, 3:209, 4:1132, 5:150, 6:9, 8:352, 9:36.
```

If `uv` is added, each common neighbour supplies a disjoint two-edge wedge
that the deletion support must hit.  More generally, the checker computes the
exact local deletion minimum after also imposing endpoint degree quotas, the
independent vertex-98 degree hit, and the four retention units.  This gives 396
entailed no-addition units:

| source | units |
|---|---:|
| more than six common neighbours | 388 |
| direct forced-star triangle units not already among those 388 | 2 |
| coupled degree/vertex-98/budget consequences | 6 |
| total | 396 |

The six coupled edges are `(55,97)`, `(56,97)`, `(57,97)`, `(88,99)`,
`(89,99)`, and `(90,99)`.  The sorted edge-list hash, using lines `u v\n`, is
`ff387efadc49230f2920e842972522683d31ddab7d496d8a0380f6a2704b4492`.

These units are logically redundant for the full SAT encoding: they are
entailed by constraints already installed.  They are nevertheless a clean,
explicit structural propagation rule.

After the four positive units, 102 universal-bank clauses are immediately
satisfied and 251,669 remain.  Substituting all 396 no-addition units gives:

- forbidden-unit incidence per unresolved clause: 12--34;
- free original-nonedge addition literals per unresolved clause: 115--140;
- clauses reduced to a deletion-support-only clause: zero.

The unique shortest residual clause has mask
`a832130504404000000040441`, three fixed-base seed literals, the fixed negative
seed literal, 34 no-addition literals, and 115 free addition literals.  Thus the
bounded local closure is useful propagation but does not by itself produce a
new support inequality from the bank.

## Domination lift and one genuinely new cut

For any triangle-free graph `F`, define

```text
Z_v = {u != v : uv is absent and N(u) intersects N(v) is empty}.
```

There are no edges between `N(v)` and `Z_v`, and `N(v)` is independent.
Therefore `alpha(F)<18` implies

```text
alpha(F[Z_v]) <= 17 - d(v).
```

In particular, degree 17 forces `Z_v` empty; degree 16 forces `F[Z_v]` to be a
clique, so triangle-freeness gives `|Z_v|<=2`.

The checker authenticates and parses all 154,190 assignments in the frozen
common model.  Its primary graph has degree distribution `16:50, 17:50`.  The
degree-16 test has zero nonclique violations.  The degree-17 test has exactly
one violation: `v=86`, `Z_v={37}`.  It yields the independent set

```text
{5,13,17,23,25,31,32,35,37,40,43,44,50,52,58,62,70,97}
```

with mask `2000000404414192982822020` and line hash
`31881b3f9667899000e686f2c09b3adb02a305225e561820a457f03870dd9be4`.
Direct membership checks show zero overlap with the universal bank, the
64,591-mask historical union, the A+ batch, and the exhaustive 235,504-mask
fixed-base family.

This is a genuine strict strengthening of the authenticated common relaxation:
the common graph satisfies its universal bank and all four retention units,
while the universally valid hitting clause for that 18-set excludes it.  The
zero-overlap checks also show that the cut is not listed in any later frozen cut
inventory.  Because the A+ clauses already exclude the source common model,
inventory novelty alone does not prove a strict semantic shrinkage of the later
A+-augmented formula.  This is not a branch-UNSAT proof, and a single separated
cut is not being presented as a complete algorithmic breakthrough.

## Bounded local swap probe

The ledger also records one graph obtained with the fixed deletion, six
residual deletions avoiding vertex 18, and four additions.  It is triangle-free,
has maximum degree 17, retains all four forced edges, and respects the complete
396-unit no-addition closure.  It nevertheless violates 12 universal-bank
clauses, whose ordered-mask hash is
`0781584d5e22dbeb508c879ef03d26c639269072a378f3457acd1156e98fe13f`.
No single edge can repair one of those displayed witnesses while immediately
preserving both triangle-freeness and the degree cap.  This probe is neither a
finite-relaxation model nor evidence against a possible vertex-18 support hit.

## Non-normative seed-automorphism telemetry

The standard-library checker intentionally does not depend on a graph
isomorphism package.  As a separate non-normative replication on Sirius,
NetworkX 3.6.1 `GraphMatcher(G,G).isomorphisms_iter()` enumerated the complete
automorphism group of the exact seed hash
`e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e`.
For the 100-vertex, 827-edge seed it returned one mapping, and that mapping was
the identity.  Runtime was 0.109 seconds.  A reproduction needs NetworkX 3.6.1,
loads the authenticated matrix, builds edges `(u,v)` for `u<v` at matrix value
one, and exhausts

```python
nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter()
```

This telemetry supports “no nontrivial seed-vertex automorphism” but is not a
dependency of the normative structural ledger.
