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

Both scripts use only the Python standard library.

