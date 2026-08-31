# A+ f24 endpoint audit — 2026-08-30

## Outcome

The single authorized 3,600-second A+ call returned a complete SAT model after
2,532.3617309331894 seconds.  This is **not** an exact-seven Ramsey witness.
The independently re-audited graph is triangle-free but contains the
independent 18-set

```text
81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 99
```

The endpoint therefore has status
`F24_SAT_REAUDITED_I18_WITNESS_NO_LOWER_BOUND`: it neither proves
`R(3,18) >= 101` nor closes branch 1, and it learns no cut.

## Frozen identities

| object | bytes | SHA-256 |
|---|---:|---|
| augmented CNF | 183,161,315 | `6fbe630343afcf31a5affa9a70a315e3033bc077b24fc9a58d5084e63fdd389f` |
| historical f24 gate JSON | 9,955 | `d46115036cb6aba0411a50659f7bfca9efcd2dad739ba75d51f3b3286d3d36b3` |
| deterministic SAT model gzip | 384,949 | `19db55d05fe0b907ab77dc9645cf9356fd383bdbb83d91aa7690c6473965ffd3` |
| historical f24 runner snapshot | 52,480 | `f24ec77a4d4a5d516f138c98e7d3117f6438e968dcae5d4ef1bcfaf1c339a69b` |
| endpoint auditor | — | `4a389a5c013a361eb073023e571d69d93671d7daca164db3e9009a9390152d6c` |
| endpoint-auditor tests | — | `bbc4d423e7d538b53bfb0f1e2fd4ff3bfedded8962e5f30e15f5a969647a20a8` |
| pinned CaDiCaL | 1,715,096 | `f5e2cf978a3b9ebf17601b9a7a25f298c684c18841846b66bdd6a6e20951fb2a` |
| CaDiCaL `SOURCE_COMMIT` | 41 | `63b647d0d86b4ee4d8bdbd619505b4053d6ebecfe52a5db75fe5f2a49dc2e762` |
| committed independent audit JSON | 3,189 | `b1f1732dfcdd1274c84c83aa7237d8385156c260b1f5e78f90b39a3e4f24ab82` |

The pinned CaDiCaL source commit is
`c60730422e758ef1cebe7aeddf2dda31c996bf04`.

## Independent checks

The fail-closed auditor did not execute a solver.  It instead:

1. authenticated the historical f24 runner, exact gate JSON, augmented CNF,
   pinned CaDiCaL binary, and source marker;
2. reparsed all 154,190 assignment literals from the compressed model;
3. evaluated every one of the 722,552 exact CNF clauses;
4. rebuilt the 100-vertex graph from the first 4,950 edge variables;
5. directly checked triangle-freeness; and
6. ran exact complement-clique search and pairwise checked the displayed
   independent set.

The reconstructed graph has 823 edges.  The A+ witness overlaps the historical
learned-cut union and the exhaustive fixed-base family, but not the universal
bank or the 4,096-mask A+ batch.  This explains why it satisfies the installed
finite relaxation while still violating the target condition.

The 28 combined gate/auditor unit tests passed.  The augmented CNF was also
rebuilt from the tracked hardened reproducer without invoking a solver; the
fresh byte stream had the same SHA-256 shown above.  Combining that rebuilt
CNF with the two committed endpoint files produced a second audit JSON that
was byte-identical to the committed audit record.

## Claim boundary

This is an authenticated negative experiment result about one finite cut
bank.  It does not show that branch 1 is SAT or UNSAT, does not establish an
exact-seven repair, and does not justify another A+ prefix or a longer repeat.
