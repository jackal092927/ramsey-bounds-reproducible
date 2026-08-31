# Frozen A+ f24 SAT endpoint

This directory keeps the small, exact endpoint files from the single bounded
A+ exploration call.  They are telemetry, not a Ramsey certificate:

- `branch1_cegar_gate.json` has SHA-256
  `d46115036cb6aba0411a50659f7bfca9efcd2dad739ba75d51f3b3286d3d36b3`;
- `branch1_cegar_sat.model.gz` has SHA-256
  `19db55d05fe0b907ab77dc9645cf9356fd383bdbb83d91aa7690c6473965ffd3`.

The authenticated model satisfies the exact 154,190-variable,
722,552-clause augmented CNF, but it contains the independent 18-set

```text
81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 99
```

so the endpoint does not prove `R(3,18) >= 101` and does not close branch 1.

The 183,161,315-byte augmented CNF is deterministically reconstructible and
is intentionally not stored in Git.  Run the hardened A+ gate without a
`--cadical` argument, using the release `branch1_common.cnf.gz` and
`branch1_common.model.gz` assets, the four units `1085`, `1672`, `1675`, and
`1680`, and the tracked A+ batch/history files.  The reconstructed CNF must
have SHA-256
`6fbe630343afcf31a5affa9a70a315e3033bc077b24fc9a58d5084e63fdd389f`.
Copy the two frozen endpoint files in this directory beside that CNF, then run
`audit_r3_18_budget7_branch1_cegar_f24_endpoint.py` with the pinned CaDiCaL
binary.  The committed audit record is
`r3_18_budget7_branch1_cegar_Aplus_f24_endpoint_audit.json`.
