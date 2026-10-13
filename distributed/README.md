# Distributed Ramsey certificate lane

The community certificate-contribution lane in
[ramsey-bounds-reproducible](https://github.com/jackal092927/ramsey-bounds-reproducible).
Humans and AI-assisted contributors can propose constructions, independent audits,
search methods, negative results and reusable checkpoints through issues and PRs.
It accepts explicit classical Ramsey lower-bound witnesses and records every
submission's validation outcome. It contains two known reproduction baselines,
not new records: C5 for R(3,3)>=6 and Cremer's n134 graph for R(6,8)>=135.

Python 3.11 or later is sufficient. No install, network, SAT solver, or model API
is required for certificate intake. From this package directory:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/ingest.py --root . --output results/ingest.json --strict
python3 scripts/leaderboard.py --root . --output results/leaderboard.json
python3 scripts/verify_certificate.py certificates/c5.txt 3 3 --max-seconds 5
```

The ingester validates `submissions/*.json` against the v1 contract, hashes every
referenced source, seed, certificate and receipt, binds the run to the exact
objective and budget, and independently checks the graph. Only full PASS is
ACCEPTED. A forbidden clique is REJECTED; a deadline is UNKNOWN and cannot earn
a bound or leaderboard entry. Producer code is never executed during intake.

The leaderboard revalidates the source files and graph bytes; it does not trust
an edited previous ledger. Each ordered `(r,s)` is a separate entry. It reports
the best verified bound in this submitted corpus, never a global record or
publication claim. Identical labelled graphs with different whitespace are
deduplicated. Isomorphic relabelings require review; no author ranking or token
score is assigned.

To reproduce baseline receipt generation:

```sh
python3 scripts/build_baselines.py
python3 scripts/ingest.py --root . --output results/ingest.json --strict
```

This command regenerates actual timing receipts and their hashes. It does not
run in CI, because CI must validate the submitted evidence without repairing it.
External certificate bytes and attribution remain pinned under `upstream/cremer/`.

New contributors should read `CONTRIBUTING.md`, add their matrix and bound source
and run evidence, and create a descriptor following `schema/submission-v1.json`.
The two complete baseline descriptors are working examples. Then run intake
before opening a PR with the Ramsey template. CI checks the package and uploads
validation results without automatically merging or publishing them.

The active workflow and PR template are installed in the repository's top-level
`.github/`. Start with [COMMUNITY.md](COMMUNITY.md), then read the contribution
contract. The packaged `VALIDATION_RECEIPT.json` describes the earlier local
validation, before publication; live GitHub Actions runs are separate receipts.

The search adapter from the preceding pilot is separate. This package establishes
the contribution bus and acceptance gate; running multiworker searches needs
actual resource allocation and run receipts. No persistent agent sessions or
external repository writes are created by these scripts.
