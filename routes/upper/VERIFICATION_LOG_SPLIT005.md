# Frozen verification log: beta 0.0299, split 0.005

Date: 2026-08-12  
Platform: macOS, Python 3.11.15  
Interval package: `python-flint==0.9.0`, Arb precision 256 bits

## Frozen objects

```text
f7344d74bb2e5f033e14dbe9e943af7b90e52937d86610eb9f2dc548605aa11e  certificate-recommended-beta00299-split005.json
5bcb2443d9ba02aed34455e1a1a511bc0ec32360d0c7a0f98e2832628b81f367  verify_arb.py
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
7f577c2036e9c213a0a9c27ce2a38658731cf1233c7846b4171849cb43847b5f  audit_tests.py
8ae50ab0ea31e7925b356eafc88ae4780ebec3619abb9adbea21d9981ecc621e  generate_certificate.py
4cef508304e84c21f73cf412712165dc26e40978cb784bc08a876948b559d90d  requirements-verify.txt
```

The search generator is not part of the proof.  The certificate is accepted
only by the two proof-oriented checkers below.

## Canonical Arb replay

Command from the repository root:

```bash
.venv/bin/python routes/upper/verify_arb.py \
  routes/upper/certificate-recommended-beta00299-split005.json
```

Frozen decisive output:

```text
PASS: corrected two-sided Arb certificate
prior U'' worst certified upper bound: -0.40787039816230575
prior small-mu correction certified upper bound: 0.66048032193687622
prior elementary small-regime slack/lambda: 0.00330349733874634449...
prior elementary worst [split,1] slack: 3.1150059697914928e-08
analytic small-regime endpoint: 0.005
analytic lower bound for slack/lambda: 0.00369567987777144546...
segments: 32768
min_F: 0.03022313226845907
min_F_prime: 0.7629834735848138
worst_standard_region_margin: 5.8529290109470086e-05 at segment 10
worst_swapped_region_margin: 6.074652597491317e-05 at segment 11539
worst_large_main_slack: 4.942496275865115e-06 at segment 10953
F(1): 1.3347544514117715495789313627167324...
growth base exp(F(1)): 3.7990629773286618741009363445941409...
```

## Independent direct-slack replay

This implementation does not import `verify_arb.py` and does not use its
`A(mu)=U(mu)-mu*U'(mu)` envelope reduction.

```bash
.venv/bin/python routes/upper/verify_region_direct_arb.py \
  routes/upper/certificate-recommended-beta00299-split005.json
```

```text
PASS: independent direct two-sided Ramsey-region replay
prior U'' worst certified upper bound: -0.40795020415189553
segments: 32768
worst_standard_exponent_slack: 8.346513629711325e-07 at segment 0
worst_swapped_exponent_slack: 6.074652597491317e-05 at segment 11539
```

## Regression tests

```bash
.venv/bin/python routes/upper/audit_tests.py
```

The tests pass the derivative-sign regression and reproduce the strict
Horizon union/intersection false positive.  The exact theorem statement and
repaired finite-net proof are in `INDEPENDENT_PROOF_REPLAY.md`; source-level
BookCor repairs are in `BOOKCOR_AUDIT.md`.
