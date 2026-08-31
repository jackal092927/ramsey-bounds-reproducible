# Quantum Ramsey diagnostics

These scripts test mathematical assumptions behind proposed quantum Ramsey algorithms. They are exact classical diagnostics, not evidence of quantum advantage.

## Reconfiguration topology

~~~bash
python3 experiments/quantum_ramsey/reconfiguration_scan.py \
  --self-check --min-n 3 --max-n 6
~~~

This exhaustively enumerates red/blue colorings with no monochromatic triangle and their valid single-edge reconfiguration graph.

## Conditional dirty-flaw expectation

~~~bash
python3 experiments/quantum_ramsey/mt_dirty_expectation.py \
  --self-check --n 10 --k 6
~~~

This computes the exact one-step conditional expectation after resampling a \(k\)-set, using rational arithmetic. The self-check verifies the all-red \(n=10,k=6\) counterexample.

## Implicit-majority Ramsey recursion

~~~bash
python3 experiments/quantum_ramsey/implicit_majority_audit.py \
  --self-check --max-k 12 --simulate-k 3 --trials 20
~~~

The repository's quiet assertion gate is:

~~~bash
python3 experiments/quantum_ramsey/implicit_majority_audit.py \
  --self-check --check-only
~~~

This checks, with exact rational arithmetic, the quantum query theorem's
scale-aware error schedule and near-majority recurrence through \(k=12\)
(and through \(k=64\) in the self-check).  The schedule spends more
estimation accuracy in cheap early rounds and less in expensive late rounds,
giving the proved \(O(2^k k\log(k/\eta))\) edge-query bound.  The script also
runs an exact dynamic program over all small split trees to check the separate
size-biased survival lemma through nine rounds, and an explicit 16-state
Grover evolution checks conditional uniformity of the capped sampler.  It then
runs a deterministic-seed Monte Carlo diagnostic on complete, empty, parity,
and random graphs.  The simulator replaces quantum search by an ideal uniform
marked-item sampler, so it validates the combinatorial invariant and cost
formula rather than physical hardware or wall-clock quantum advantage; only
the isolated sampler audit evolves a state vector.

All three scripts use only the Python standard library.
