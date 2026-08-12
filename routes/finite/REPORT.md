# Specific Ramsey-number route: record audit and first CPU experiments

Snapshot date: **2026-08-12**

## Outcome

No new global Ramsey-number bound is claimed.  The useful outcomes are:

1. Two post-survey record claims were independently validated from their raw
   adjacency matrices:
   - \(R(3,17)\ge93\), using a 92-vertex graph with
     \(\omega=2,\alpha=16\);
   - \(R(4,15)\ge160\), using a 159-vertex graph with
     \(\omega=3,\alpha=14\).
2. \(R(3,13)\ge62\) was selected as the local-CPU target.
3. The public 60-vertex AlphaEvolve \((3,13)\)-graph cannot be extended by
   freezing it and adding only one new vertex.  CaDiCaL and Glucose independently
   return UNSAT.
4. Within that frozen extension family, exact bounded-conflict SAT proves that
   0 through 9 triangles are impossible, while a 10-triangle / zero-\(I_{13}\)
   near miss exists.  The exact frozen optimum is therefore **10**.
5. A structured 11-triangle / zero-\(I_{13}\) near miss has all triangles on one
   hub edge.  Deleting the hub edge and allowing arbitrary add-only repair is
   UNSAT in two solvers.  More strongly, allowing arbitrary additions and up to
   **eight deletions** from that near miss is exact-SAT UNSAT.
6. At deletion budget nine the hub edge is logically forced.  Removing it
   creates exactly 25,685 independent 13-set witnesses, all containing both
   hub endpoints.  A one-million-conflict interruptible run ended `UNKNOWN`;
   it found no model and proves no new global bound.
7. A shared-deficit/Benders master produced 24,832 reusable conditional
   `I_13` cuts and 81,345 strict pairwise addition incompatibilities.  Its
   pinned replay stopped at a one-million-conflict limit with status `UNKNOWN`,
   zero heuristic exclusions, and no candidate.
8. A higher-order follow-up exhaustively checked 341,376 addition triples and
   materialized 57,879 genuine ternary shared-deficit cuts. Its separately
   bounded master replay also returned `UNKNOWN`, with no candidate and no
   heuristic exclusion.
9. A 90-second exact-delta bounded-uphill walk made 193 accepted moves but did
   not improve score 11.  This is a negative run, not an improvement claim.
10. A new fixed-base k=11 near miss has no (I_{13}), eleven triangles, and no
    single edge common to all eleven. Exact repair with arbitrary additions
    now proves that repairing this seed requires at least **eleven** old-edge
    deletions.  At budget ten, three hub-deleted residual-eight branches and
    one CNF merging exactly all 512 hub-retained transversals are Glucose- and
    CaDiCaL-UNSAT; all four frozen DRAT traces were independently replayed as
    `VERIFIED`. The proposed k=10 non-hub entrance
    remains `UNKNOWN`, because
    the existing k=10 file is itself a hub near miss.
11. The independently checked 99-vertex AlphaEvolve `(3,18)` graph certifies
    the already-known bound \(R(3,18)\ge100\).  Its frozen 100-vertex extension
    has no \(I_{18}\) and exactly one triangle.  Three exhaustive branches,
    one for each edge deleted from that triangle, have reconstructed CNFs and
    `drat-trim`-verified UNSAT proofs.  Hence arbitrary additions plus at most
    five input-edge deletions cannot repair this fixed near miss.  At exact
    budget six, all three fixed-edge branches have frozen CNFs and complete
    replayed DRAT UNSAT proofs. Hence the complete fixed-seed budget-six ball
    is excluded and the local deletion radius is at least seven. This does not
    prove that a seven-deletion repair exists, and no claim
    \(R(3,18)\ge101\) is made.

## Live provenance audit

### Source hierarchy

1. **Curated survey:** Stanisław Radziszowski, *Small Ramsey Numbers*, Dynamic
   Survey DS1.18, 24 April 2026.  Downloaded PDF SHA-256:
   `9519a676ee381f02f03269c22e3f101162b2fdcc9d432e4103cb1192fdff91bc`.
   Source: <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS1/pdf>
2. **Official AlphaEvolve certificate directory:** pinned at Google Research
   commit `015539128d9a7dbe14b5f5308a198a15da808949`.
   Source: <https://github.com/google-research/google-research/tree/master/ramsey_number_bounds/improved_bounds>
   Associated preprint: <https://arxiv.org/abs/2603.09172>
3. **Post-survey third-party certificate repository:** Yiping Wang's
   ScaleAutoResearch-Ramsey, pinned at commit
   `6d6d76a44c14321882a8640ed9e86d4f791e31d3`.
   Source: <https://github.com/ypwang61/ScaleAutoResearch-Ramsey>

The third source is not a peer-reviewed paper and was not incorporated into the
April survey.  Its graph claims are nevertheless finite mathematical
certificates, so their correctness can be checked independently of authorship or
publication status.  This report calls them **independently validated public
certificates**, not survey-incorporated records.

### Bounds affected by the live audit

| Cell | April 2026 survey | Later public certificate | Live working interval |
|---|---:|---:|---:|
| \(R(3,13)\) | \(61\)–\(68\) | AlphaEvolve matrix independently rechecked | \(61\)–\(68\) |
| \(R(3,17)\) | \(92\)–\(109\) | ScaleAutoResearch: \(\ge93\) | **\(93\)–\(109\)** |
| \(R(3,18)\) | \(100\)–\(120\) | AlphaEvolve matrix independently rechecked | \(100\)–\(120\) |
| \(R(4,15)\) | \(159\)–\(364\) | ScaleAutoResearch: \(\ge160\) | **\(160\)–\(364\)** |

The pinned files, raw URLs, hashes, orders, and claimed parameters are in
`certificate_manifest.json`.  `fetch_certificates.py` refuses a download whose
SHA-256 differs from the manifest.

## Independent certificate results

The checker validates square 0/1 format, zero diagonal, symmetry, absence of
\(K_r\), and absence of \(K_s\) in the complement.  It also finds boundary
witnesses for \(K_{r-1}\) and independent \((s-1)\)-sets.

| Certificate | Vertices | Edges | Exact \(\omega\) | Exact \(\alpha\) | Result |
|---|---:|---:|---:|---:|---|
| AlphaEvolve \(R(3,13)\ge61\) | 60 | 349 | 2 | 12 | valid |
| AlphaEvolve \(R(3,18)\ge100\) | 99 | 809 | 2 | 17 | valid |
| AlphaEvolve \(R(4,15)\ge159\) | 158 | 3742 | 3 | 14 | valid |
| Scale \(R(3,17)\ge93\) | 92 | 727 | 2 | 16 | valid |
| Scale \(R(4,15)\ge160\) | 159 | 3761 | 3 | 14 | valid |

The checker was compared with exhaustive clique enumeration on every graph up
to five vertices and 2,000 deterministic random six-vertex graphs.  A second
vertex-selection SAT checker independently confirms the \(R(3,13)\ge61\) seed
and the post-survey \(R(4,15)\ge160\) certificate.
The SAT extension and repair encodings were also checked against complete
truth-table searches on small graphs.  The canonical test suite contains thirteen
passing tests.

## Why target \(R(3,13)\ge62\)

- The current interval \(61\)–\(68\) leaves real room.
- A stable, public, independently checked 60-vertex seed exists.
- Exact \(K_3\) and \(I_{13}\) checks take fractions of a second locally.
- Unlike \(R(5,5)\), this target does not require an enormous enumeration just
  to establish a useful experimental baseline.
- No indexed primary source or checked public matrix found in the live search
  already proves \(R(3,13)\ge62\).  This is a search finding, not a guarantee
  that no unindexed claim exists.

## Exact diagnostics

### Frozen one-vertex extension

For a fixed \((r,s)\)-graph, variables encode the new vertex's neighborhood.
Every base \((r-1)\)-clique gives a red hard clause.  Independent
\((s-1)\)-sets are found lazily and added as blue hard clauses.

| Fixed base | Result | Independent solver agreement |
|---|---|---|
| AlphaEvolve 60-vertex \((3,13)\)-graph | UNSAT | CaDiCaL + Glucose42 |
| Scale 92-vertex \((3,17)\)-graph | UNSAT | CaDiCaL + Glucose42 |
| Scale 159-vertex \((4,15)\)-graph | UNSAT | CaDiCaL; 14,084 red clauses, 913 discovered blue clauses |

These results prove only non-extendability of the named fixed bases.  They are
not upper bounds on the corresponding Ramsey numbers.

### \(R(3,13)\) near frontier

Exact cardinality SAT gives:

- bounds 0,1,...,9 on the number of new triangles: UNSAT;
- bound 10: SAT, yielding `r3_13_n61_frozen_nearmiss_k10.txt` with exactly ten
  triangles and no independent 13-set;
- hence the frozen optimum is exactly 10.

Here `k10` records only triangle count. Exact reconstruction shows that all ten
triangles in that file share edge ((34,60)); it is not a non-hub seed. A
separate fully preloaded exact-ten/non-hub SAT search ended
`UNKNOWN_GLOBAL_WALL_LIMIT`, not UNSAT. Relaxing to exact eleven triangles
produced a seed whose maximum shared-edge multiplicity is ten. Exact
arbitrary-addition repair was first shown UNSAT through seven deleted seed edges; see
`NEW_BASIN_SEARCH.md` and the per-budget machine JSON records.  The seed itself
has 61 vertices, 363 edges, eleven triangles, and no independent 13-set.  The
edit formula exposes all 1,830 possible final edges, charges only deleted seed
edges, installs all 35,990 triangle clauses, and separates independent
13-sets exactly.  An independent audit reconstructed the seed, exhaustively
cross-checked the encoding on 1,896 small cases, and replayed budgets two
through seven.  Its verdict is `PASS WITH IMPORTED SOLVER DEPENDENCY`: the
retained CaDiCaL `UNSAT` answers have no independently checkable proof traces.

The former budget-eight `TIME_LIMIT` is superseded by
`BUDGET8_NEXT.md`.  Ten triangles share edge $(28,60)$ with pairwise-disjoint
spoke pairs, so budget eight forces deletion of that edge.  The only remaining
input triangle, $(37,46,60)$, forces one of three further deletions.  With the
remaining six-deletion budget and all independent 13-sets of each fixed branch
preloaded, the three necessary-condition CNFs are UNSAT before any lazy cut.
Glucose and bounded CaDiCaL agree; all three Glucose DRAT traces pass
`drat-trim`.  The stronger `BUDGET9_NONSTAR.md` replay uses the same exhaustive
split with a residual-seven counter; all three formulas are again
Glucose/CaDiCaL-UNSAT and have `drat-trim`-verified proof traces.  Hence the
exact fixed-seed deletion lower bound is ten, still without any global Ramsey
consequence.
An independent reviewer reconstructed the three CNFs clause by clause,
re-enumerated each fixed-base `I13` bank, and reran all three frozen proofs with
the pinned `drat-trim`; see `INDEPENDENT_BUDGET9_REFEREE.md`.

An earlier bound-11 solution has eleven triangles
\((x,56,60)\), all sharing edge \((56,60)\).  That structure enabled two stronger
repair diagnostics:

- delete \((56,60)\), then add any set of edges while enforcing final
  triangle-freeness: UNSAT (CaDiCaL and Glucose42);
- allow any additions and at most \(d\) deletions from the full near miss:
  exact UNSAT for every \(d=1,\ldots,8\).

Thus a successful construction in this basin must change at least nine of the
near miss's existing edges, or leave this basin entirely.  Arbitrary additions
were already allowed in this statement.

The old budget-9 attempt used a 600-second external wall cap which expired
during one non-interruptible SAT call.  It was therefore only `UNKNOWN`.
A replacement solver now uses persistent MiniSat learned clauses, 5,000-
conflict slices, an eight-second per-call interrupt, and explicit global
limits.  Before solving, exact structure gives:

- the eleven triangle spoke-pairs are edge-disjoint, so retaining the common
  hub would require at least eleven deletions;
- every budget-nine solution must therefore delete the hub and, because
  budget eight is UNSAT, exactly eight additional original edges;
- deleting the hub produces exactly 25,685 \(I_{13}\) witnesses, all preloaded
  as 77-literal hitting clauses.

The bounded run completed 200 slices and stopped normally at 1,000,000
conflicts after 219.699 seconds, with zero timer interrupts and zero SAT
models.  Its status is **`UNKNOWN_GLOBAL_CONFLICT_LIMIT`**, not UNSAT.  No
candidate graph was emitted.  See `BUDGET9_CORE_GUIDED.md` and
`budget9_core_guided.json` for the frozen evidence.

### \(R(3,18)\) one-point near miss

The frozen 99-point certificate has no direct triangle-free, `I18`-free
one-point extension.  Its minimum-conflict extension used here has 100
vertices, 827 edges, no independent 18-set, and the unique triangle
`{97,98,99}`.  Any triangle-free repair deletes at least one of those three
edges, so the budget-five edit family splits exhaustively into three branches.
Each branch fixes that deletion, permits four further input-edge deletions,
and leaves all original nonedges free to be added.  Reconstructed CNFs contain
every triangle clause and a finite bank of necessary `I18`-hitting clauses;
all three frozen DRAT traces pass the pinned official checker.  Therefore the
named near miss requires at least six input-edge deletions.  See
`R3_18_EXTENSION_REPAIR.md`.  An independent referee reconstructed all three
formula semantics and replayed every proof with both the packaged binary and
a fresh build; see `INDEPENDENT_R3_18_EXTENSION_REFEREE.md`.  This local radius
neither supplies a 100-point Ramsey graph nor excludes one elsewhere.

The exact budget-six continuation is fully closed. Using the prior
budget-five proof, any new solution must delete exactly six input edges.  The
branch fixing `(98,99)` absent and exactly five additional input-edge deletions
has a 13,160-variable, 183,543-clause finite relaxation; its 146 MB compressed
DRAT proof independently replays as `VERIFIED`.  A later continuation closed
the `(97,99)` branch with a 13,160-variable, 242,064-clause CNF and a complete
433 MB compressed DRAT proof; a fresh replay reported `s VERIFIED`. The old
interrupted partial proof remains quarantined and unused. Finally, a validated
union of 251,771 universal $I_{18}$ cuts closed the `(97,98)` branch with a
13,160-variable, 429,892-clause CNF and a complete 656 MB compressed DRAT
replayed to `s VERIFIED`. Therefore the fixed-seed deletion radius is at least
seven, although existence at exactly seven is unknown. See
`R3_18_BUDGET6_AUDIT.md`, `INDEPENDENT_R3_18_BUDGET6_REFEREE.md`, and
`R3_18_BUDGET6_BRANCH1_PROOF.md`, with branch-0 closure in
`R3_18_BUDGET6_BRANCH0_UNION_PROOF.md` and a separate clause-level review in
`INDEPENDENT_R3_18_BUDGET6_BRANCH1_REFEREE.md`.

## Search mechanism and cross-route transfer

The experiments support a combined mechanism drawn from both newer record
searches:

1. **Diagnose before optimizing.**  First solve the fixed-base extension as an
   exact SAT problem.  Do not spend compute optimizing an unreachable frozen
   family.
2. **Approach from both constraint sides.**  For \(R(3,t)\), maintain either a
   triangle-free graph with a few independent-set conflicts or a graph with
   zero independent-set conflicts and a few triangles.
3. **Use exact edge deltas.**  Adding an edge destroys all independent sets that
   contain its endpoints and creates exactly their common-neighbor triangles;
   deleting an edge has the reverse exact count.
4. **Cross low barriers with bounded uphill chains.**  Greedy or strictly
   triangle-free moves cannot leave the observed basin.  Use tabu, compound
   deletion-repair chains, and anchored restart to the best fully verified
   state.
5. **Use SAT to select release edges.**  The proved deletion radius says the
   next search must release at least nine base edges.  Extracting UNSAT cores
   or solving a hitting-set relaxation should choose those edges more
   intelligently than uniform random flips.

That shared-deficit/Benders master has now been implemented.  Conditional
`I_13` cuts cover independent sets created by the residual deletions, while
binary incompatibility cuts aggregate the common-neighbor spoke costs of two
additions without double counting. A higher-order pass adds a ternary no-good
when the union of three additions' spoke-pair requirements has exact
vertex-cover number greater than the residual deletion budget. The bounded
runs still did not reach a
fixed-deletion subproblem, but its 24,832 strict masks are persisted and
resumable. See `BENDERS_BUDGET9.md`, `BENDERS_NEXT.md`, and their JSON records.
Future
checkpoints remain acceptable only after independent reconstruction by
`verify_ramsey.py`.

## Claim boundary

- **Established here:** correctness of four pinned finite certificates under an
  independent checker, plus the official 99-point `(3,18)` certificate; exact
  fixed-base UNSAT statements; the old hub seed's
  exact local deletion radius through eight; the new non-star seed's
  proof-carrying local deletion radius through ten with arbitrary additions;
  existence of a ten-conflict near miss; and the
  forced-hub/residual-eight structure at budget nine; 24,832 strict
  conditional cuts; 81,345 strict pairwise shared-deficit cuts; and 57,879
  strict ternary shared-deficit cuts among the selected addition set; and the
  proof-carrying budget-five exclusion around the named 100-point `(3,18)`
  near miss.
- **Not established:** \(R(3,13)\ge62\), any new global Ramsey bound, a
  budget-eleven completion of the new seed, \(R(3,18)\ge101\), a budget-six
  repair of its near miss, or survey acceptance of the two later public
  certificates.
