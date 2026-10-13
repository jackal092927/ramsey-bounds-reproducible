# Community Ramsey research

We invite human and AI-assisted contributions toward explicit classical Ramsey
lower bounds. The initial lane accepts a graph on n vertices with no K_r and no
independent s-set: that graph proves R(r,s) >= n+1. Each problem (r,s) has its own
board. A search score, an unverified solver output, or a fixed-family UNSAT result
cannot establish such a lower bound.

## Join the relay

1. Choose an objective from the repository issues and record a dated prior bound.
2. Pin the seed graph, method source, configuration, resource budget and ancestry.
3. Run a bounded search; keep failed, UNKNOWN and near-miss endpoints in an
   experiment archive. Sharing a useful negative result is welcome.
4. For a successful candidate, add the graph, source/seed/run evidence and a
   descriptor under `submissions/`; follow [CONTRIBUTING.md](CONTRIBUTING.md).
5. Independently verify, open a PR with the Ramsey template, and link the target
   issue and predecessor contributions. CI performs intake; mathematical scope,
   duplication and priority still need review.

Anyone may contribute a certificate, a checker improvement, a search strategy,
a bounded reproduction, a seed-diversity analysis or a documented obstruction.
Opening an issue claims no exclusive ownership of a mathematical problem. Say
which revisions and resources you used so collaborators can continue the work.

## Initial board and open directions

Known baselines are C5 (R(3,3)>=6) and Fritz Cremer's 134-vertex graph
(R(6,8)>=135). Cremer's 344-vertex R(8,10)>=345 witness was independently
reproduced in our earlier work but is not yet part of this default five-second
CI board. These are prior results, not new records by this project.

First search directions: extend and globally repair an existing witness;
compare conflict-count and pressure-based losses; vary patch/block/crossover
moves; preserve nonisomorphic promising seeds; compare independent workers with
checkpoint sharing under matched total compute. Each campaign needs a frozen
objective, source/configuration, allocation, actual endpoint and failure ledger.

The current board is generated from the submitted corpus and must never be
advertised as a complete global record table. Check the dynamic survey and
recent papers before claiming a new record.

## Verification and collaboration

Run tests and intake from `distributed/` using the README commands. Only a
complete independent PASS can enter the board. Every row retains its certificate
and ancestry; identical labelled graphs with formatting changes count once.
The CI artifact contains all intake outcomes, including rejected or UNKNOWN
submissions. A default timeout is UNKNOWN, not proof of failure or success.

The launch supplies the contribution and verification infrastructure. It does
not claim an active global swarm, new numerical bounds, a completed multiworker
campaign or a publication. We will report those separately when evidence exists.

## Attribution

Credit original constructions, donor patches, search/checker methods and audit
work separately. Contributor account, agent role and declared model use are
separate fields; unknown is valid. Public contributions do not justify guessing
private identities or relationships. Existing manuscript claims and their source
conditions remain in the main repository README. Their copyright policy is
unchanged; imported Cremer witnesses retain CC BY 4.0.
