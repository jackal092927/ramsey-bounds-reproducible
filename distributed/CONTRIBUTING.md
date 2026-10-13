# Contributing finite Ramsey witnesses

Each submission concerns one exact `(r,s,n)` and a labelled adjacency matrix on
n vertices. No K_r and no independent s-set proves R(r,s)>=n+1. Quantum query
exponents, asymptotic diagonal upper bounds, near misses, speedups, and fixed-seed
UNSAT exclusions have different proof obligations and do not enter this board.

## Lifecycle

Use these distinct states: PREPARED source/config; RUNNING worker; COMPLETED,
FAILED or UNKNOWN endpoint; CANDIDATE graph; independently ACCEPTED witness;
reviewed PR; incorporated commit; published result. A submitted PR, elapsed
solver run, merged commit or published graph does not establish every later state.

The validator accepts only a completed successful run receipt bound to a valid
graph. Even if the producer reports PASS, the graph is rechecked independently.
UNKNOWN, an incomplete trace, an unsat solver message, or a near miss cannot
earn a numerical lower bound. Solver UNSAT without semantic reconstruction and
proof replay is not a proof-carrying exclusion. Even a verified fixed-family
exclusion is not a global Ramsey upper bound.

## Submission files and required provenance

Add a JSON file under `submissions/` with the exact v1 fields and accompanying
files within this package root. Paths must be relative, cannot traverse parents
or escape through symlinks, and each referenced intake file must be <=4 MB.

The descriptor includes:

- Exact r, s, n, lower bound n+1, and `known_baseline` or `candidate` status.
- Full symmetric binary adjacency matrix with zero diagonal and raw SHA-256.
- Original repository and revision, attribution, and retained license path.
- Nonempty producer source manifest with every source file's exact hash.
- Nonempty seed list and every seed's exact hash; a certificate-replay baseline
  can name the original witness as its seed.
- Run identity, exact objective, certificate/source/seed hashes, CPU count,
  wall budget, observed completion, exit code and elapsed time. UNKNOWN or
  failed endpoints must be preserved in campaign ledgers but cannot be submitted
  as successful numerical certificates.

Hashes bind submitted bytes and make contradictions detectable. They do not
authenticate an author's self-reported origin, token usage or elapsed-time claim.
Verification proves the concrete mathematical witness; claims about search
efficiency or collaboration need separately measured, complete campaign data.

Run `python3 scripts/ingest.py --root . --strict` and the tests before opening
the PR. Results beyond the default five-second verification budget remain
UNKNOWN until a reviewer deliberately allocates and records a longer check.
Do not edit source or receipt hashes to hide a failed run. Intake executes no
contributor-supplied producer code and requires no credentials.

## Duplicates and ancestry

An identical labelled graph remains one witness within each `(r,s)`; whitespace
changes do not create new contributions. Include predecessors when your graph
extends, mutates or repairs an existing witness. Isomorphic relabelings are
reviewed duplicates until a mathematical distinction is established. Different
graphs proving the same bound can be retained for diversity and reproduction;
they are not extra numerical improvements. Each `(r,s)` is kept separately.

Near misses and negative endpoints should go into an experiment archive with
their full budgets and source/seed ancestry, outside `submissions/`. The board
retains all intake outcomes in its denominator and awards no points for UNKNOWN.
No token-volume, agent-count or merged-PR-count ranking is used as evidence of
scientific improvement.

## Review and publication

CI is a reproducible intake gate, followed by review of the precise statement,
source/license attribution, possible duplicates and prior bounds. A candidate's
corpus improvement is not necessarily a new global record. Refresh the dynamic
survey and recent public witnesses before making that claim. Preserve the
independent verification receipt in the reviewed source snapshot. Human peer
review, repository incorporation and publication remain separate events.

This public contribution lane preserves the existing repository license policy.
It grants no additional reuse rights for existing project material. Cremer's imported data retain CC BY 4.0 and
the original author/paper/repository attribution.
