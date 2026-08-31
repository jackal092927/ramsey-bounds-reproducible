# Refinement Report

## Starting idea

Use quantum algorithms, perhaps aided by topology, to construct or refute Ramsey colorings, improve finite bounds, and validate the theory with small simulations for an ITCS submission.

## Refinement path

### Round 0

Proposed quantum flaw repair for implicit monochromatic-clique events. The direct target was a Grover-accelerated Moser--Tardos loop.

### Round 1

Novelty review found direct collisions with adiabatic Ramsey algorithms, quantum annealing/QUBO work, generic quantum backtracking, and fixed-subgraph detection. The Grover repair bound reduced to a generic square-root neighborhood scan.

### Round 2

A walk-amortization route was tested. Measurement, resampling, history-dependent state representations, and markedness cost blocked the proposed speedup. A universal no-amortization lower bound was suggested, then refuted.

### Round 3

The exact conditional resampling identity was derived. It showed that product-measure \(dp\) reasoning cannot be applied pointwise to adaptive states. A reproducible \(n=10,k=6\) counterexample was obtained.

### Round 4

The review was corrected to preserve only a possible dirty-neighborhood overlap mechanism. The queue invariant and all-marked enumeration baseline were made explicit.

### Round 5

A two-line double-counting theorem capped standard valid-batch overlap by \(\binom k2\). Exact pairwise formulas showed moderate batches have \(g=1+o(1)\) in the diagonal Ramsey--LLL regime. The current positive program was therefore closed.

## Why no quantum circuit was built

A \(K_5/K_6\) Grover or QAOA simulation would reproduce existing ideas and would not test the missing structural theorem. The two implemented diagnostics directly test the mathematical assumptions that failed:

- exact conditional dirty-flaw expectation;
- exact valid-state reconfiguration topology.

## Final research decision

- Do not submit this direction to ITCS 2027.
- Do not add it to the unified Ramsey manuscript as a positive result.
- Preserve the exact identities, counterexamples, and overlap cap as scoped technical notes.
- Restart quantum work only after a new Ramsey-specific structural theorem appears independently of a generic quantum wrapper.
- Continue the classical exact-seven program as the primary paper path.

