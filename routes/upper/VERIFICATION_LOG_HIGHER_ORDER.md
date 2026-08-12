# Frozen verification log: three-stage quintic/quintic/sextic descent

## Hashes

```text
2664bc421cd0cb7489289caa283a3a3f22830580f7c21bf0e6cbe092910bc277  certificate-higher-order-quintic-v1.json
b5b595b4dcc9d1bdc2b5714f68fef99ec1c566bbd612d35ca19100d173d41c4d  certificate-higher-order-quintic-chain-v2.json
2052952c3af98074d5442fb736c7a2952146e92051a43fab84e75f099d9e00d7  certificate-higher-order-sextic-chain-v3.json
281a3f41d8e5347fdf54aa89e3e1b96f5e6c7e1ba51a715f7107b123206ef8d6  search_chained_target.py
6c4ca964a8fc98eff5bb19a74caa00f7f7628fbd8bc6fe4d8fabb67456124b1b  generate_higher_order_certificate.py
879ce15f4518f1d6737fdbba09d04f7433c96c4c3d81efcd3c666a35fdaae981  verify_arb.py
f4e2c8663022a82ed22c41677e71d4b609b0a9eace1770c56deb12351faf3494  verify_chain_arb.py
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
b0d4f0cb94bb816ca3342e6076dd8223d1003e661757481442fe166eb2330bfe  audit_tests.py
```

The search programs are search-only. The proof consists of the frozen JSON inputs
and the three verification commands below.

## Exact-link chain replay

Command:

```text
.venv/bin/python verify_chain_arb.py \
  certificate-higher-order-quintic-v1.json \
  certificate-higher-order-quintic-chain-v2.json \
  certificate-higher-order-sextic-chain-v3.json
```

Output:

```text
PASS: verified 3-stage Ramsey-rate certificate chain
stage 0:
  prior -> target:
    [-0.25, 0.08, 0.08] ->
    [-0.25, 0.062797738895, -0.032456368039,
     0.102292138999, -0.028160790049]
  target small slack/lambda: 0.0034410087628560810...
  standard region: (0.0001087940012958612, 5)
  swapped region: (0.00010994822689528693, 23052)
  large main: (9.667544669720171e-05, 65535)
  growth base: 3.7914853930774899343626155087867436...

stage 1:
  prior -> target:
    [-0.25, 0.062797738895, -0.032456368039,
     0.102292138999, -0.028160790049] ->
    [-0.25, -0.008578629273557, 0.127585140806616,
     -0.029829210000000, 0.010085181421050]
  target small slack/lambda: 0.0038270889416388282...
  standard region: (0.00010960144273955114, 118)
  swapped region: (0.00011009250090651343, 22485)
  large main: (0.00010520468957159067, 21842)
  growth base: 3.7842250653748521911439944463870320...

stage 2:
  prior -> target:
    [-0.25, -0.008578629273557, 0.127585140806616,
     -0.029829210000000, 0.010085181421050] ->
    [-0.250000000000000, -0.003330465213687,
      0.091728978292451, 0.040555948334794,
     -0.053458127305523, 0.021783259992867]
  target small slack/lambda: 0.0038903585040936769...
  standard region: (6.960077165064378e-05, 6)
  swapped region: (7.016617229398231e-05, 22533)
  large main: (0.00016510787819556342, 65535)
  growth base: 3.7814656158401685107275297311637231...
```

## Independent direct replay: stage 1

```text
PASS: independent direct two-sided Ramsey-region replay
prior U'' worst certified upper bound: -0.40795020415189553
segments: 65536
worst_standard_exponent_slack: (1.54983120140414e-06, 0)
worst_swapped_exponent_slack: (0.00010994822689528693, 23052)
```

## Independent direct replay: stage 2

```text
PASS: independent direct two-sided Ramsey-region replay
prior U'' worst certified upper bound: -0.36862975299624107
segments: 65536
worst_standard_exponent_slack: (1.5614231112089097e-06, 0)
worst_swapped_exponent_slack: (0.00011009250090651343, 22485)
```

## Independent direct replay: stage 3

```text
PASS: independent direct two-sided Ramsey-region replay
prior U'' worst certified upper bound: -0.37184261548417713
segments: 65536
worst_standard_exponent_slack: (9.911774569389889e-07, 0)
worst_swapped_exponent_slack: (7.016617229398231e-05, 22533)
```

## Regressions

```text
PASS: derivative sign regression; X base is positive iff F'>0
PASS: arbitrary-degree polynomial derivative regression
PASS: Horizon union-gap test
```
