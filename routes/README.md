# Parallel Ramsey research routes

Snapshot date: 2026-08-12.

The persistent research objective is broader than any single candidate:

1. improve asymptotic upper bounds;
2. improve asymptotic lower bounds;
3. refresh and improve concrete two-colour Ramsey numbers.

Each route keeps its own evidence and executable artifacts:

- `upper/`: diagonal upper-bound theorem audit, independent certification, and
  constrained optimization;
- `lower/`: proof-driven lower-bound mechanisms and falsifiable lemmas;
- `finite/`: live record ledger, explicit graph search, and exact certificate
  verification.

## Evidence levels

Every numerical or mathematical claim must carry one of these labels:

| Level | Meaning |
|---|---|
| `PUBLISHED` | Peer-reviewed theorem, or an authoritative dynamic survey entry |
| `PREPRINT` | Public theorem manuscript not yet treated as settled publication |
| `EXTERNAL-CERT` | Public machine-checkable certificate independently reproduced here |
| `LOCAL-CANDIDATE` | New result accepted by at least one checker but not independently certified |
| `INDEPENDENT-CERT` | Two substantively independent checkers agree on a finite certificate |
| `PROVED` | Complete theorem-to-certificate argument has passed mathematical audit |
| `NEAR-MISS` | Verified positive conflict/constraint count; never a bound improvement |

No route may promote a claim by replacing a mathematical proof with a dense
floating-point grid or by trusting the search program as its own verifier.

## Cross-route hypotheses

1. **Frozen-manifold diagnosis.**  Before scaling a local search, prove or test
   whether its frozen representation can contain a solution.  The recent
   finite-number searches used SAT to show that a fixed old graph was not
   one-vertex extendable; the analogous upper-bound question is whether fixed
   witness functions leave any coefficient room.
2. **Two-sided feasibility repair.**  A monotone search that preserves one
   constraint at every step can be trapped.  Finite graph breakthroughs came
   from satisfying the independence constraint first and repairing triangles
   through bounded uphill compound moves.  Upper-bound optimization can test an
   analogous slack-budget continuation, while lower-bound theory can ask
   whether compound repair admits a probabilistic invariant.
3. **Search/proof separation.**  Optimizers generate candidates.  Exact graph
   checkers, interval arithmetic, SAT certificates, and written combinatorial
   derivations establish evidence.

## Coordination rule

Routes may exchange mechanisms and counterexamples, but not silently import
claim status.  A heuristic that works in one route becomes only a hypothesis in
another until that route verifies it under its own invariant.
