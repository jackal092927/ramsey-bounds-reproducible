# Quantum constructive Ramsey search

This directory is the standalone anonymous ITCS 2027 submission source for
the quantum-query result.  It intentionally excludes the classical
asymptotic-bound and finite `R(3,18)` parts of the unified Ramsey manuscript.

Build from the repository root:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -cd \
  papers/quantum/main.tex
```

Run the theorem-specific executable audit:

```sh
.venv/bin/python experiments/quantum_ramsey/implicit_majority_audit.py \
  --self-check --check-only
```

Reproduce the small proof-of-concept experiment reported in the paper:

```sh
.venv/bin/python experiments/quantum_ramsey/implicit_majority_audit.py \
  --simulation-only --simulate-k 3 --trials 1000 --seed 20260831
```

The PDF is `papers/quantum/main.pdf`.  The submission build is anonymous and
uses 11pt single-column text.  `PAPER_PLAN.md` records the claims-evidence
matrix, exclusions, and submission gates.
