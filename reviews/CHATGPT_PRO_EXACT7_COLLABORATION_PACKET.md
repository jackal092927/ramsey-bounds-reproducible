# Draft ChatGPT Pro collaboration packet: exact-seven gap exploration

Status: **DRAFT ONLY — NOT SUBMITTED EXTERNALLY**  
Prepared: 2026-08-30  
Scope: the unresolved exact-seven finite search after a reviewed deletion-first
pilot, an exact diagnosis of an oracle-order artefact, four proof-checked
singleton consequences, exact structural and deletion projections, a
maximal-triangle-free normal form, the complete four-family mask union, and one
frozen maximal-union endpoint.  The packet is designed to prevent repetition
of exhausted configurations and to solicit proof-carrying, materially stronger
techniques.

This packet contains no credentials, personal identifiers, private filesystem
paths, or unpublished raw experimental data. Sending it or an attachment is
still an external transmission and requires fresh action-time confirmation and
a visible check of the destination ChatGPT account and Pro setting.

## Proposed prompt

> Act as an adversarial Ramsey-theory and proof-producing SAT collaborator.
> Design a genuinely new attack on an unresolved exact-seven repair problem
> for a fixed 100-vertex \(R(3,18)\) near miss.  Do not infer validity from
> status labels, hashes, timeouts, or prior reviews.  Separate proved
> mathematics, trusted-code checks, proof-carrying SAT results, heuristic
> observations, and open questions.  In particular, do not repeat the bounded
> solver/cut/oracle configurations listed below unless a new derivation changes
> their semantics or yields a checkable certificate.
>
> ### Exact-seven objective
>
> Find either:
>
> 1. a graph \(F\) on the labelled vertex set
>    \(\{0,\ldots,99\}\) that is triangle-free, has \(\alpha(F)<18\),
>    and deletes exactly seven edges of the frozen seed \(H\), while allowing
>    arbitrary additions of seed nonedges; or
> 2. checked UNSAT certificates for all three exact-seven branch formulas.
>
> A verified witness would be a 100-vertex \((3,18)\)-Ramsey graph and prove
> \(R(3,18)\ge101\). Checked UNSAT in all three branches would prove only
> \(\rho(H)\ge8\) for this labelled seed and one-sided edit metric; it would
> not supply a global Ramsey upper or lower bound.
>
> ### Verified seed facts and exact problem
>
> * The frozen matrix has SHA-256
>   e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e.
> * \(H\) has 100 vertices, 827 edges, 4,123 nonedges, no independent
>   18-set under an exhaustive trusted-code bitset check, and exactly one
>   triangle, \(\{97,98,99\}\).
> * The first 99 vertices form a separately frozen graph \(G_0\) with 809
>   edges, no triangle, and \(\alpha(G_0)=17\). It reproduces the known bound
>   \(R(3,18)\ge100\).
> * Vertex 99 has seed neighbourhood
>   \(\{33,34,\ldots,48,97,98\}\); the only edge induced by that
>   neighbourhood is \((97,98)\).
> * The one-sided distance is \(d_H(F)=|E(H)\setminus E(F)|\).
>   Only deleted seed edges are charged; every seed nonedge remains a free
>   Boolean final-edge variable.
> * A proof-carrying computation already excludes every completion with at
>   most six deleted seed edges. Therefore a witness in the next layer must
>   have exactly seven deletions.
> * Triangle-freeness forces at least one edge of the unique seed triangle to
>   be absent. The exhaustive, possibly overlapping branches fix respectively
>   \((97,98)\), \((97,99)\), or \((98,99)\) absent and require exactly
>   six further deletions among the other 826 seed edges.
> * **Certified branch-symmetry boundary.** A standalone deterministic,
>   degree-initialized one-dimensional Weisfeiler--Leman checker has color-class
>   counts 3, 15, and 100 at initialization, round one, and round two. Every
>   graph automorphism preserves these colors, so the 100 singleton classes
>   prove that the labelled seed has trivial automorphism group. No branch-1
>   result transfers to the other triangle-edge branches by relabelling. Do not
>   confuse auxiliary-variable symmetries of an encoding with automorphisms of
>   the underlying graph.
> * **New proof-carrying branch-1 consequence.** Let \(\Psi_1\) be the
>   authenticated branch-1 common relaxation: triangle clauses, exact-six
>   residual deletion counter, fixed unit \(\neg x_{97,99}\), all degree-at-
>   most-17 counters, and the ordered 251,771-clause universal \(I_{18}\)
>   bank. Four independently checked DRAT refutations prove
>   \[
>     \Psi_1\models x_{11,62}\wedge x_{18,61}\wedge
>                         x_{18,64}\wedge x_{18,69}.
>   \]
>   These are four singleton no-goods, stronger than the earlier pair cores.
>   Their CNFs were independently rebuilt byte for byte, and their traces were
>   replayed with separately built checker binaries on x86-64 and arm64.
> * **Non-vacuity.** A complete checked model satisfies all 718,452 clauses of
>   \(\Psi_1\) and sets all four named edges true. It also contains a checked
>   independent 18-set, so it is not a target repair. Thus the entailments are
>   not consequences of an empty relaxation, but satisfiability of \(\Psi_1\)
>   still says nothing about exact-seven existence.
> * **Exact support effect.** The degree cap and four singleton restrictions
>   together exclude 380,670,699,850,897 of the
>   \(\binom{826}{6}=433,155,188,594,590\) raw branch-1 residual supports,
>   or 87.8832136551%. The singleton results contribute 1,307,748,575,589
>   exclusions beyond the degree cap, 2.4311102136% of its survivors. These
>   are support counts, not a measured runtime speedup.
>
> ### Proof-carrying predecessor and scale
>
> The budget-at-most-five layer and the exact-six layer have three exhaustive
> triangle-edge branches each and checked DRAT refutations. For exact six,
> every branch has 4,950 primary edge variables, 8,210 sequential-counter
> auxiliaries, 161,700 triangle clauses, 16,420 exact-five counter clauses,
> and one fixed negative unit.
>
> | fixed absent edge | \(I_{18}\) clauses | total clauses | raw DRAT bytes |
> |---|---:|---:|---:|
> | \((97,98)\) | 251,771 | 429,892 | 3,493,847,713 |
> | \((97,99)\) | 63,943 | 242,064 | 2,137,671,968 |
> | \((98,99)\) | 5,422 | 183,543 | 759,008,359 |
>
> These proof sizes are an important warning: an exact-seven UNSAT route must
> budget proof production, storage, and independent checking from the start.
>
> ### Routes already tried and precise endpoints
>
> 1. **Direct extension of the frozen 99-vertex base.** A solver-trusted exact
>    lazy-CEGAR run returned `UNSAT` for a direct one-vertex
>    triangle-free/\(I_{18}\)-free extension of \(G_0\), after 2,748 iterations
>    and 2,747 discovered \(I_{17}\) clauses.  It emitted no DRAT/LRAT trace,
>    so it is diagnostic rather than proof-carrying evidence. Repeating the
>    same frozen-base extension is not new.
> 2. **Repair of the one-triangle extension through budget six.** Exploratory
>    CEGAR was replaced by exhaustive triangle-edge branch formulas. All six
>    predecessor formulas now have checked proof traces, establishing only
>    the fixed-seed bound \(\rho(H)\ge7\).
> 3. **First exact-seven portfolio.** Each branch used the same
>    251,771-clause universal \(I_{18}\) bank. Every initial formula had
>    4,950 primary variables, 9,840 counter auxiliaries, 161,700 triangle
>    clauses, 19,680 exact-six counter clauses, one fixed unit, and 251,771
>    hitting clauses: 14,790 variables and 433,152 clauses in total.
> 4. Branch 0 used CaDiCaL, branch 1 Glucose 4.2, and branch 2 MapleChrono.
>    Each received a hard 300-second discovery wall. All three remained inside
>    the first solve call until killed. No model reached the exact
>    independent-set separator, no new cut was added, and no proof was emitted.
>    All three endpoints are UNKNOWN_DISCOVERY_WALL_LIMIT.
> 5. The complete initial formula and cut bank are reproducible, but internal
>    CDCL state was not serialized. A later run reconstructs the same state
>    rather than resuming the interrupted instruction.
> 6. **Deletion-first branch-1 formulation.**  This is now implemented,
>    independently audited, and covered by 16 dedicated tests plus a 49-test
>    finite-light regression.  The historical ascending script SHA-256 is
>    `36dc3b53941605bc4ec132b70b4f61c5afbbcda13742fe9056a38ddb1683e5a0`;
>    its test SHA-256 is
>    `ed62d2318e64d6731bca343e829f2e65c058f8f484a72b027b2a87da9f2fd76f`.
>    The ordered gates used runner
>    `22ddb00aa93727aa51d2edd6d09b0e536a230e0cc17426004858e98620d6c4f8`
>    and tests
>    `b65ebc6f265de6552cdf6f8c09586f4c7c2ae01db0292908ae7998beea75a35c`.
>    The hardened release snapshot (resume-bank identity checks and additional
>    order-composition tests, with no search-semantic change) has runner
>    `eb911a5010581c16042c3853dd5ae98bda4bd7237fde3cae7f9e030730fd984b`
>    and tests
>    `14b173bf90be9bccb65554d86ba21b344aa2aac7cc4388ac5f99a338a2468f60`.
>    It fixes `(97,99)` absent, selects exactly six of 826 residual seed-edge
>    deletions, uses 4,123 addition-eligibility selectors, separates
>    conditional independent-18-set cuts in a master, and sends a fixed
>    deletion set to an exact add-only subproblem.  An incomplete oracle never
>    creates a no-good.  A solver-completed fixed-D `UNSAT` may create only a
>    strict one-D search no-good; without DRAT/LRAT it is not theorem evidence.
> 7. **Degree-cap lift.**  In a triangle-free graph with alpha below 18, every
>    open neighbourhood is independent, hence every degree is at most 17.
>    After fixing `(97,99)` absent, vertex 98 still has degree 18.  Therefore
>    every residual six-deletion set must hit one of its 18 incident edges.
>    This excludes exactly
>    `C(808,6)/C(826,6) = 0.875813014052041...` of the raw six-edge sets.
>    The master and subproblem both encode the stronger per-vertex degree
>    inequality, including additions.  This is exact combinatorial pruning,
>    not a promised wall-time ratio.
> 8. **Six-run bounded matrix after the lift.**  With a two-million-node
>    independent-set oracle cap and a 180-second global wall:
>
>    | run | endpoint | seconds | new cuts | solver-trusted fixed-D UNSAT |
>    |---|---|---:|---:|---:|
>    | g42/c0 | subproblem oracle UNKNOWN | 3.680 | 0 | 0 |
>    | g42/c4096 | subproblem oracle UNKNOWN | 9.700 | 16 | 0 |
>    | m22/c0 | subproblem oracle UNKNOWN | 15.256 | 2,816 | 0 |
>    | m22/c4096 | subproblem oracle UNKNOWN | 47.856 | 1,039 | 0 |
>    | m22/c16384 | global-wall UNKNOWN | 180.026 | 0 | 0 |
>    | Maple/c4096 | subproblem oracle UNKNOWN | 62.784 | 768 | 2 |
>
>    The two Maple fixed-D `UNSAT` endpoints have no proof trace and therefore
>    establish nothing.  They differ in one deletion:
>    `{(1,97),(10,64),(11,62),(17,98),(18,61),(18,64)}` and
>    `{(1,97),(10,64),(11,62),(17,98),(18,61),(18,69)}`.
> 9. **Predeclared positive-signal extension.**  Three checkpoint resumes used
>    MapleChrono for the fixed-D subproblem and raised the independent-set cap
>    to 20,000,000 nodes / 30 seconds, with a 300-second global wall.  Glucose
>    learned 10,780 new cuts and stopped at 20,000,001 subproblem-oracle nodes
>    after 121.884 seconds.  Maple learned 13,362 and stopped at the same node
>    endpoint after 197.868 seconds, with only the two prior unproved no-goods.
>    Minisat learned 12,800 cuts and hit the 300.095-second global wall before
>    entering a subproblem.  No run produced a candidate, a proof trace, or a
>    new completed fixed-D `UNSAT`.  The same cap-scaling route is stopped.
> 10. **Exact oracle-order diagnosis.** The two deep fixed-D supports were
>     reconstructed. With the historical ascending low-bit recursion, each
>     exhausted 2,000,001 nodes without a witness. Reversing the deterministic
>     vertex order returned 512 independently validated, original-label
>     independent 18-sets in 11,261 and 10,057 nodes, taking 0.0058 and 0.0052
>     seconds. The former 20-million-node stalls were therefore ordering
>     artefacts on these two supports, not evidence of combinatorial absence.
> 11. **Seven order-aware gates.** A fail-closed bidirectional oracle used a
>     shared aggregate node/wall budget and let only an exhausted pass certify
>     absence. The bounded results were:
>
>     | run | cut batch | endpoint | seconds | master models | new cuts |
>     |---|---:|---|---:|---:|---:|
>     | g42/bidir60 | 512 | global wall | 64.077 | 1 | 512 |
>     | Maple/bidir60 | 512 | global wall | 60.165 | 0 | 0 |
>     | g42/bidir10 | 512 | global wall | 120.218 | 5 | 2,560 |
>     | m22/bidir10 | 512 | global wall | 120.038 | 1 | 512 |
>     | Maple/bidir10 | 512 | global wall | 120.059 | 4 | 2,048 |
>     | g42/batch4096 | 4,096 | global wall | 180.200 | 4 | 16,384 |
>     | Maple/batch4096 | 4,096 | global wall | 180.089 | 3 | 12,288 |
>
>     Every invoked separator returned its full batch in 0.005--0.075 seconds.
>     None of the seven gates reached a fixed-D subproblem, found a verified
>     candidate, emitted a proof, or learned a new fixed-D no-good. Under these
>     settings the tested wall moved back to the master. This is bounded
>     telemetry, not proof that the master is intrinsically hard.
> 12. A generic vertex-selection SAT oracle is not an untried shortcut: on the
>     known fixed seed, Minisat22, Glucose42, MapleChrono, and CaDiCaL each
>     failed to complete a no-independent-18 check within 60 seconds, whereas
>     the current exact bitset check completed locally in about 8.6 seconds.
>     A new separator proposal must exploit additional structure or provide a
>     falsifiable reason it differs from this generic encoding.
> 13. **Generalized-core route, now closed more strongly.** The two historical
>     deletion supports suggested pair assumptions. Proof-producing CaDiCaL
>     runs first checked pair cores and then minimized all the way to the four
>     singleton entailments stated above. Each final CNF has 154,190 variables
>     and 718,453 clauses. The common formula contains no learned core clause;
>     the only extra clause in each proof instance is the negative unit for one
>     candidate edge. Asking merely to extract a deletion assumption core,
>     minimize the old two supports, or prove the four already named singleton
>     consequences would repeat completed work. The compressed proof sizes
>     range from 707,650,273 to 1,117,799,611 bytes; the corresponding raw
>     traces range from 3,538,873,659 to 5,577,099,956 bytes.
> 14. **A+ no-repeat gate.** From the checked model of \(\Psi_1\), reverse-first
>     deterministic enumeration produced 4,096 independent 18-sets after
>     scanning 6,512 witnesses. Every accepted set is new relative to three
>     separately authenticated families: the 251,771-mask universal bank; the
>     64,591-mask union of all cuts learned by the 18 historical branch-1
>     checkpoints; and the exhaustive 235,504-mask family independent in the
>     fixed branch-1 seed. The three overlap counts are exactly zero. The gate
>     adds these 4,096 clauses and the four proved positive units, producing a
>     deterministic 154,190-variable, 722,552-clause CNF with SHA-256
>     `6fbe630343afcf31a5affa9a70a315e3033bc077b24fc9a58d5084e63fdd389f`.
>     One 3,600-second parent-enforced CaDiCaL call is the only authorized
>     solver experiment. It never learns a cut automatically. SAT requires a
>     complete model and direct clause evaluation; the returned independent
>     set is classified against all three old families. UNKNOWN learns
>     nothing. UNSAT remains unproved until one promotion record authenticates
>     the exact augmented CNF, freshly replays its trace with pinned
>     `drat-trim`, and binds and replays the frozen singleton summary plus all
>     four singleton proofs that justify the added positive units.
>     **Final A+ endpoint.** The single bounded call returned SAT after
>     2,532.3617309331894 seconds. A fail-closed independent audit reparsed all
>     154,190 literals, evaluated all 722,552 clauses, rebuilt a triangle-free
>     823-edge graph, and found the independent 18-set
>     `{81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99}`.
>     That set is in both the historical union and exhaustive fixed-base
>     family, but not in the universal bank or A+ batch. The endpoint status is
>     `F24_SAT_REAUDITED_I18_WITNESS_NO_LOWER_BOUND`; it learns no cut, does
>     not close branch 1, and does not prove `R(3,18) >= 101`. The gate JSON,
>     model, and audit SHA-256 values are respectively
>     `d46115036cb6aba0411a50659f7bfca9efcd2dad739ba75d51f3b3286d3d36b3`,
>     `19db55d05fe0b907ab77dc9645cf9356fd383bdbb83d91aa7690c6473965ffd3`,
>     and
>     `b1f1732dfcdd1274c84c83aa7237d8385156c260b1f5e78f90b39a3e4f24ab82`.
>
> 15. **Exact local structural projection.** An independent checker projects
>     the triangle, degree, exact-six residual-deletion, vertex-98 hit, and
>     four retention-unit systems. The projection onto the deletion support
>     gives exactly the already stated support conditions. Its full local
>     no-addition closure contains 396 original-nonedge units: 388 from
>     common-neighbour counts above six, two from retained-star constraints,
>     and six only from coupled degree/budget reasoning. Substituting all 396
>     units into the finite mask bank produces no pure deletion-only clause.
>     Hence these units are valid preprocessing, not a new support no-good.
> 16. **Domination diagnostic.** For
>     \(Z_v=\{u\ne v:uv\notin E(F),\,N(u)\cap N(v)=\varnothing\}\), every
>     target satisfies
>     \(\alpha(F[Z_v])\le17-\deg(v)\). The checked common model yields one new
>     independent-18 mask,
>     2000000404414192982822020, from its unique unsafe pair (37,86).
>     The A+ model has three unsafe pairs (16,64), (32,98), and (40,89),
>     all degree 16 at both endpoints, and yields no domination mask. A
>     hardened CEGAR design exists, but no solver call was launched because
>     maximality below subsumes the target-side condition more cleanly.
> 17. **Deletion-only covering projection stopped at its control.** The exact-
>     six control has 13,159 variables and 264,757 clauses and includes all
>     235,504 fixed-base \(I_{18}\) covers. Pinned CaDiCaL reached the
>     predeclared 300-second wall with no status line. The 1,887,813,632-byte
>     incomplete proof prefix was hashed and deleted. Under the registered
>     go/no-go rule, exact seven was not run. This route is UNKNOWN and
>     DO_NOT_RUN until its control becomes discriminating.
> 18. **Maximal-triangle-free WLOG normalization.** Layer A is unconditional:
>     repeatedly add a triangle-safe absent original nonedge. This preserves
>     the exact seven-edge deletion support, triangle-freeness, and
>     \(\alpha<18\). Layer B uses the independently checked
>     \(\rho(H)\ge7\): if a deleted seed edge were safe to restore, the result
>     would be a target with six deletions. Thus an exact-seven target exists
>     iff one exists that is maximal triangle-free. This is a WLOG existence
>     statement, not a property of every raw target or every incomplete-bank
>     SAT model. The selector encoding uses
>     \(x_{uv}\lor\bigvee_w y_{uv,w}\),
>     \(\neg y_{uv,w}\lor x_{uw}\), and
>     \(\neg y_{uv,w}\lor x_{vw}\); one-way implications are existentially
>     exact. The full encoding adds 485,100 auxiliaries and 975,150 clauses.
>     A dedicated adversarial audit checked the fixed-branch-edge case, the
>     exact/at-most-six dependency, degree-cap subtlety, and a complete
>     three-vertex truth table. The deterministic completion of the A+ primary
>     graph remains maximal triangle-free with maximum degree 17 but retains
>     its historical \(I_{18}\), so maximality alone is not branch closure.
> 19. **Full mask union, not another A+ prefix.** The universal, historical,
>     and exhaustive fixed-base families deduplicate to 526,429 masks; the
>     4,096 A+ masks are disjoint, giving 530,525 total. Since the common CNF
>     already contains the universal bank, the new formula appends 278,754
>     masks and the four retention units. It has 154,190 variables, 997,210
>     clauses, 390,604,816 bytes, and SHA-256
>     4f7e8f5b724a657888c7814d2c25cac41c283c3db356fb8f1a15f4c7322c375d.
>     It directly blocks the A+ endpoint's known witness. It is also not the
>     Benders all-fixed-base-cuts formula: it uses the full edge CNF and
>     adds 43,614 history-only plus 4,096 A+ masks. Construction and an
>     independent byte-for-byte audit are complete.
> 20. **Combined full-union plus maximality gate: bounded UNKNOWN.** The frozen
>     branch-1 formula contains the authenticated common relaxation, the four
>     proof-checked retention units, all 530,525 distinct masks in the four-bank
>     union, and the full all-pair maximal-triangle-free selector encoding. It
>     has 639,290 variables, 1,972,360 clauses, 408,370,088 bytes, and SHA-256
>     `09e1784c3f43c4901dc6f6b4749fc5a74b025b08f74be58133edd1ed1096ebdb`.
>     An independent reconstruction was byte-exact. The one authorized Sirius
>     call used CaDiCaL 3.0.1 at source commit
>     `c60730422e758ef1cebe7aeddf2dda31c996bf04`, binary SHA-256
>     `bd054bcc5864fd20c9ff117f8fff94f810f5b210014ff33971a6c1db1d0eca45`,
>     non-binary DRAT, a 300-second wall, and a 10-GiB proof cap. The wrapper
>     exited 124 and the result file contained exactly `c UNKNOWN`. The run
>     recorded 13,347 conflicts, 105,834 decisions, 1,216,037,481 propagations,
>     and 1,897.78 MB peak RSS; these are resource telemetry, not evidence
>     toward SAT or UNSAT. The incomplete 922,038,097-byte proof prefix,
>     SHA-256
>     `a6693fe2b3bab57f9d0e9ebe39bd7baa3883bfe2af15a5eb33b0aded972b5438`,
>     was hashed and deleted without replay. No model, cut, or certificate was
>     obtained. Branch 1, exact seven, and the global Ramsey bound therefore
>     remain unresolved.
>
> These records do not identify the intrinsic cause of hardness. They show that
> the simple full-bank first solve is poor under the tested walls, that two
> apparent fixed-D separator stalls were order artefacts, and that the seven
> repaired gates next spent their walls in the master. The singleton
> refutations give genuine family-level pruning, but do not close branch 1.
> The A+ call is a bounded, no-repeat probe rather than a new iterative CEGAR
> campaign. These facts do not prove that
> the preload is globally helpful or harmful, that the master is the intrinsic
> bottleneck, that a model exists, or that any branch is UNSAT.
>
> ### Current frozen architecture and acceptance rules
>
> The latest frozen object is a static direct-primary CNF, not the historical
> deletion-first runner. Its production generator authenticates the common
> formula, four singleton-proof units, all four mask families, and the budget-six
> dependency; it emits the full mask union and all-pair maximality selectors in
> deterministic order. A separate implementation reconstructs all 1,972,360
> clauses byte for byte. If a SAT model returns, it must assign every variable,
> satisfy every exact clause, and pass direct graph checks for triangle-freeness,
> exact one-sided distance seven, the fixed branch unit, all four retained
> edges, maximum degree 17, maximality, and an exhaustive independent-18 search.
> If UNSAT is reported, a nonempty proof must replay against the exact frozen
> CNF with the pinned checker. Thus a terminal result is accepted only when:
>
> * a fully separated model is independently checked by both a bitset Ramsey
>   verifier and a separate vertex-selection SAT verifier; or
> * the installed finite relaxation is UNSAT and its DRAT trace is accepted by
>   pinned drat-trim against the exact CNF hash.
>
> A hitting clause for any 18-set is universally necessary. Thus the installed
> finite formula is a relaxation of the exact branch: UNSAT of the relaxation
> proves branch UNSAT, while SAT is only a candidate requiring separation.
> Solver exit text alone is never promoted. The state checkers validate hashes,
> dimensions, counter semantics, free-nonedge treatment, all-pair selector
> semantics, complete assignments, timeout records, and the deleted-prefix
> boundary. The historical CEGAR and Benders runners below are diagnostics and
> possible comparison baselines, not the current frozen architecture.
>
> **Existing-technique overlap:** the lazy \(I_{18}\) separator is already the
> basic co-certificate-learning pattern: a violating independent 18-set gives
> a universally valid clause learned by the SAT backend. The Benders pilot
> also turns such witnesses into conditional master cuts. Therefore “use CCL”
> or “add lazy independent-set clauses” alone is not a new proposal. We need
> lifted or generalized co-certificates that soundly exclude a family of
> witnesses, deletion sets, or addition patterns at once, with an independently
> checkable derivation.
>
> The reviewed deletion-first formulation uses 826 residual deletion variables
> with exact sum six and 4,123 addition-eligibility selectors.  Each
> common-neighbour wedge adds
> \(\neg y_{uv}\lor d_{uw}\lor d_{vw}\); the master also contains exact
> per-vertex degree-at-most-17 constraints and conditional \(I_{18}\) cuts.
> A fixed-deletion exact add-only subproblem checks all collective triangle and
> degree constraints and lazily separates \(I_{18}\).  Both levels use bounded
> persistent SAT slices and restartable, hash-validated checkpoints.  An
> incomplete master separator may fall back to the exact fixed-D subproblem,
> but an UNKNOWN subproblem stops without a no-good.  A candidate must pass a
> bitset verifier, an independently encoded vertex-selection SAT verifier, and
> exact edit-semantics checks.  The pilot still emits no proof trace; its two
> solver-trusted fixed-D `UNSAT` endpoints therefore remain diagnostics only.
> The current separator exposes ascending, reverse, and bidirectional schedules.
> Reverse relabels deterministically and maps every witness back to original
> labels. Bidirectional shares one aggregate resource budget; an incomplete
> pass cannot certify witness absence. Checkpoints bind the selected schedule
> and the identity of the initial cut bank.
>
> ### Questions
>
> 1. Adversarially audit the maximal-triangle-free WLOG reduction and its
>    existential selector encoding. Try to construct a counterexample to each
>    implication, paying particular attention to restoration of a deleted seed
>    edge, the fixed branch edge, exact seven versus at most six, free additions,
>    and the use of the already certified radius-at-least-seven result. State
>    whether the proof is non-circular and list every hypothesis it actually
>    needs.
> 2. Treat the maximal-union endpoint strictly as UNKNOWN. Identify concrete,
>    falsifiable mechanisms that might explain why this encoding is ineffective;
>    do not infer intrinsic hardness from its CDCL telemetry. For each mechanism,
>    permit at most one bounded diagnostic and require a predeclared stop rule,
>    independent checker, and certificate path.
> 3. Derive at least one family-level necessary condition that is genuinely
>    stronger than the four singleton units, the exact 396-unit local closure,
>    the degree cap, and ordinary independent-set hitting clauses. Give a formal
>    derivation, show a support or model excluded beyond those systems, and
>    specify how an independent checker reconstructs the constraint.
> 4. Give two materially different exact formulations beyond both the
>    deletion-first Benders/CCL system and the direct maximal-union CNF. Possible
>    families include lifted hypergraph transversals, pseudo-Boolean or MaxSAT
>    formulations, canonical maximal-triangle-free generation, or decompositions
>    coupling deletion supports with addition structure. Specify variables,
>    every implication direction, relaxation strength, SAT verification, and
>    UNSAT certification.
> 5. Reassess branches 0 and 2 independently. The seed has trivial automorphism
>    group, so no branch-1 result transfers by relabelling. Identify genuinely
>    branch-specific structure, compare the likely value of continuing branch 1
>    versus pivoting, and give a bounded test for any claimed advantage.
> 6. Design a proof-size-aware external-cut ledger and cube/partition workflow
>    anchored to one exact frozen formula hash. Require deterministic coverage,
>    reconstructible cuts, per-cube proof obligations, SAT-cube re-verification,
>    and calibration on solved exact six before any exact-seven deployment.
> 7. Return a ranked next-action plan. Each proposed route must state whether it
>    targets witness discovery, certified branch UNSAT, or both; its expected
>    logical gain; implementation and proof cost; a falsifying microbenchmark;
>    and a hard go/no-go threshold. It is acceptable to conclude that no current
>    route justifies a large run.
>
> ### Required deliverables
>
> Return one adversarial report with:
>
> 1. a ranked table of 5--8 non-redundant exact-seven techniques, each with
>    formulation, expected benefit, certificate path, implementation cost,
>    and falsifiable failure signal;
> 2. two fully specified formulations that either strictly strengthen the
>    frozen branch-1 maximal-union gate or change its decomposition semantics
>    in a checkable way; adding known masks, maximality selectors, solver time,
>    or another generic backend does not qualify;
> 3. a minimal implementation/test plan naming state artifacts, checker rules,
>    and trust boundaries;
> 4. a bounded experiment matrix with hard go/no-go rules;
> 5. exact acceptance requirements for both a SAT witness and a three-branch
>    UNSAT result; and
> 6. a short list of conclusions that the present UNKNOWN data cannot support.
>
> Label speculation as speculation. If using literature, prefer primary
> papers, official solver documentation, or official repositories and give
> direct links. Do not claim to have run code or checked a proof unless you
> actually do so.
>
> ### Explicit do-not-repeat list
>
> * Do not infer SAT, UNSAT, rarity, or nonexistence from UNKNOWN or timeout.
> * Do not rerun the frozen 639,290-variable maximal-union CNF with only a
>   longer wall, another generic CDCL solver, different seed phases, or a larger
>   proof cap. Its one authorized 300-second endpoint is UNKNOWN; a follow-up
>   must change the formulation or test a named mechanism.
> * Do not propose maximal-triangle-free completion or the existing all-pair
>   selector encoding as new. The WLOG reduction and encoding have already been
>   implemented and adversarially audited, and maximal completion of the A+
>   graph still retains an independent 18-set.
> * Do not propose a subset, prefix, reordering, or simple reinstallation of
>   the universal, historical, exhaustive fixed-base, and A+ mask families.
>   Their complete 530,525-mask union is already present in the frozen gate.
> * Do not present the 396 original-nonedge units as a new deletion-support
>   restriction: exact projection found no resulting pure deletion-only clause.
>   Do not present the domination condition alone as the next route unless it
>   yields a checked strengthening beyond full maximality.
> * Do not run the deletion-only exact-seven covering projection while its
>   exact-six control remains UNKNOWN. Its registered endpoint is `DO_NOT_RUN`
>   until the control becomes discriminating.
> * Do not transfer branch-1 masks, endpoints, or claimed difficulty to branches
>   0 or 2 by symmetry; degree-initialized 1-WL proves the seed automorphism
>   group is trivial.
> * Do not interpret conflicts, decisions, propagations, memory use, or the size
>   of an incomplete DRAT prefix as progress toward SAT or UNSAT.
> * Do not repeat the solver-trusted direct one-vertex-extension CEGAR run for
>   \(G_0\); it returned `UNSAT` without a proof trace and is not a certified
>   refutation.
> * Do not repeat the same `c0/c4096/c16384` cut-prefix matrix, the same
>   Minisat/Glucose/Maple portfolio, or a change that only raises the exact
>   \(I_{18}\) oracle node/time cap.  Those bounded variants are recorded above.
> * Do not propose reverse vertex ordering, bidirectional scheduling, or the
>   same 512/4096-cut ordered gate matrix as a new idea. Those changes were
>   implemented, regression-tested, and run; they removed the two old oracle
>   stalls but did not close the branch.
> * Do not propose the degree-at-most-17 cap as a new idea: it is already
>   proved, independently audited, encoded at both levels, and measured.
> * Do not mix original nonedges into the deletion counter, silently re-add the
>   fixed branch edge, or replace “exactly seven” by “at most seven” without
>   redoing the reduction.
> * Do not treat heuristic no-goods, incomplete cut banks, solver exit codes,
>   or unverified traces as theorem evidence.
> * Do not call the two proof-unchecked fixed-D no-goods assumption cores,
>   certificates, or evidence.  Do not treat 10,780 or 13,362 learned cuts as
>   movement toward SAT or UNSAT.
> * Do not propose generalized deletion-core extraction or minimization of the
>   two old supports as unfinished work. That route has already produced four
>   stronger proof-checked singleton entailments, and the old pair proofs are
>   strictly dominated.
> * Do not list SMS or Satsuma as a primary route merely because this is a graph
>   problem; the certified 1-WL refinement leaves no nontrivial seed-vertex
>   automorphism to exploit.
> * Do not confuse a master or fixed-D subproblem model with a fully separated,
>   independently verified final graph.  The old all-pairs portfolio returned
>   no first model; the Benders pilot did return intermediate models but no
>   verified candidate.
> * Do not rename the current lazy \(I_{18}\) clauses “co-certificate
>   learning” and present that as new. Propose a lifted/generalized clause or
>   another genuinely stronger reuse mechanism.
> * Do not claim \(\rho(H)=7\), \(\rho(H)\ge8\), or \(R(3,18)\ge101\)
>   without the corresponding witness or checked proof package.
> * Do not describe a proved S3 bridge as removing S1, S2, S4, S5, the
>   non-effective \(K\), or the fixed-\(C\) limit order.
> * Do not recommend splitting the unified manuscript.
>
> ### Public context
>
> The April 2026 *Small Ramsey Numbers* survey records the working interval
> \(100\le R(3,18)\le120\):
> <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>.
> The public 99-vertex certificate and associated search context are from the
> AlphaEvolve Ramsey work:
> <https://arxiv.org/abs/2603.09172> and
> <https://github.com/google-research/google-research/tree/master/ramsey_number_bounds>.
> Basic co-certificate learning is described by Kirchweger, Peitl, and Szeider:
> <https://arxiv.org/abs/2306.10427>. Our current lazy \(I_{18}\) loop already
> instantiates that basic witness-to-clause pattern, so the relevant question
> is generalization or lifting. Kirchweger, Xia, Peitl, and Szeider's
> *Smart Cubing for Graph Search* combines a prerun that collects learned
> constraints with later cubing:
> <https://arxiv.org/abs/2501.17201>. This is methodological guidance, not
> empirical evidence that cubing will help this exact-seven instance.

## Safe supporting-file manifest

The following project files were scanned for private home-directory strings,
credentials, tokens, passwords, and API keys; none were found. Hashes and byte
counts refer to this source snapshot.

| attachment | bytes | SHA-256 | role |
|---|---:|---|---|
| `r3_18_budget6_summary.json` | 6,140 | 0abd30457c039c1c5fbba5890153c8a0c5d8558e196e7c0561410cefe37afa6a | certified radius dependency |
| `r3_18_budget7_branch1_core_proof_summary.json` | 10,406 | 8ae4f0d9ea919c915ba642eb03ec3d418b4419a89781377509acbe925d89555a | four singleton entailments |
| `R3_18_BUDGET7_BRANCH1_STRUCTURAL_PROJECTION.md` | 8,411 | ffa9acf2b8f76911202708ffc264d590f8285fe5cad3b471a63c896e0ae4eb6b | exact 396-unit projection |
| `R3_18_BUDGET7_BRANCH1_DELETION_PROJECTION_2026-08-30.md` | 9,334 | e15ad6b102ef73e1e0f1912d2b6c8a725d781e76b992a96b549ceafb56f30cf0 | failed-control stop rule |
| `R3_18_BUDGET7_BRANCH1_MAXIMALITY_WLOG.md` | 7,813 | 6aa7f9ebe6506d65b0a993f1cd555f075c93928363ef493f81ceb98983e5b14d | mathematical normal form |
| `check_r3_18_budget7_branch1_maximality_wlog.py` | 46,134 | 27b0a41209c8343ac208f2d939e9c02920e883cb33e3397e4062cc5d3c5aac85 | normal-form model audit |
| `R3_18_BUDGET7_BRANCH1_FULL_MASK_UNION_2026-08-30.md` | 8,731 | b4440fe2e5ede983ed1348d164bd7083be84df49eea89f99859e49c47e7518e0 | four-family union ledger |
| `R3_18_BUDGET7_BRANCH1_MAXIMAL_UNION_GATE_2026-08-30.md` | 10,440 | f169c620d83a687eef0f84d8e3c4f5a6bd265179312fd074a3b023ded1c21f7f | combined gate and endpoint |
| `r3_18_budget7_branch1_maximal_union_gate.py` | 35,551 | c07c76c5c6dde10474c10d48703270b83cff5a8865d223e7674342227dbafaf4 | deterministic generator |
| `check_r3_18_budget7_branch1_maximal_union_gate.py` | 37,525 | 9458ae9cdccc380efc1d083d6a6c06c14bd7a49ac728ca43c836ee5b62bacda2 | independent CNF/model/proof checker |
| `test_r3_18_budget7_branch1_maximal_union_gate.py` | 9,459 | 2a85014c95de3e13e642ee91218cada552f4b4419c04c3e73a8b530465418df1 | 11 semantic tests |
| `r3_18_budget7_branch1_maximal_union_gate_design.json` | 6,978 | 266ca29292b61d14f033b402345cdab934d4702336cdd03fb9153b66925ed34d | solver-free design ledger |
| `r3_18_budget7_branch1_maximal_union_gate_production.json` | 7,833 | cb3eaa1ed462713e13a951dbc113555ce8f1aa8325c266658d9cc32c8dd72026 | production CNF identity |
| `cnf_audit.json` | 911 | 551e9188a4b7eb42bb40080acb0b2378ca6af69d412fb51f0c964ec2460190d2 | byte-exact independent reconstruction |
| `r3_18_budget7_branch1_maximal_union_probe.json` | 3,811 | e35f7761f92ddebdb4029553fe7a2828e31c79d68820d37b1aa2bb6ac4f80571 | sanitized UNKNOWN endpoint |
| `check_r3_18_budget7_branch1_maximal_union_probe.py` | 9,944 | 7c6879bcd9c07ed27ebf25cb601a4ce8c69e5714178e35a9fb286c740b3c2ad0 | fail-closed endpoint checker |
| `test_check_r3_18_budget7_branch1_maximal_union_probe.py` | 1,723 | 83f545543792e22d9d825ae22ee9b00883172cf902a21d8b7be368cc80e736bd | three endpoint tests |
| `r3_18_budget7_branch1_maximal_union_probe_audit.json` | 473 | 4e4e212f0c6bae101db00dfb118f602cc6f874e9d8833f3c43cc946432e2cc54 | checked endpoint summary |
| `check_r3_18_seed_automorphism_wl.py` | 5,543 | 613c902fe89fedfc2e2132e6a5d7ea182b7cc4b2fd245885861c29f36ba62f18 | 1-WL automorphism certificate |
| `test_check_r3_18_seed_automorphism_wl.py` | 1,476 | 93047e1673d73f6adca0109bb200d524191b9f9671d0ed84b7466203f66cc114 | three 1-WL tests |
| `r3_18_seed_automorphism_wl_audit.json` | 1,240 | 8ad9fbec731a3c2f3b3012695022366fc66070265c6f5a27bfc0c66f34e872ce | trivial-group audit record |

No attachment is required for the text-only advisory prompt above.  If files
are later attached after separate authorization, rehash and rescan them at
action time.  Upload only the sanitized ledgers listed above, not raw solver
result JSON, checkpoints, the 408 MB CNF, or any DRAT payload.

## Closed-gap and manuscript context

The former lower-component item S3 is no longer an open gap and is not a task
for this collaboration packet.  The canonical source now proves weighted
reverse propagation locally by the indicator-kernel conjugation and tower
property, including integrability, null-event histories, endpoint levels, and
reverse induction.  The lower theorem still depends on version-pinned source
items S1, S2, S4, and S5; it remains source-relative, fixed-large-\(C\), and
non-effective.  This transition has been materialized into the single unified
manuscript and adversarially rechecked.

The final local double build produced a byte-identical 98-page unified PDF,
SHA-256
`26b08245406ef905a38bf06d5fce6b4528b63eda2ed935d34367612f9cf7630b`.
Local build evidence does not close the separate final-tag, immutable-Release,
or credential-free replay gates.

The remaining claim firewall is unchanged: exact seven is UNKNOWN without a
verified witness or checked proof; the finite theorem is local to one labelled
seed and one-sided metric; and the project contains one unified manuscript,
not three publication outputs.
