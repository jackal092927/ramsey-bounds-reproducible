# Quantum constructive Ramsey search

This directory is the standalone anonymous ITCS 2027 submission source for
the quantum-query result.  It intentionally excludes the classical
asymptotic-bound and finite `R(3,18)` parts of the unified Ramsey manuscript.

Build from the repository root:

```sh
SOURCE_DATE_EPOCH=1788073200 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error -cd papers/quantum/main.tex
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

The PDF is `papers/quantum/main.pdf`. The submission uses the official LIPIcs
v2021.1.3 class with `anonymous`, A4 single-column layout, and line numbers.
A separate review-only adapter enforces ITCS's 11pt minimum, including the
abstract and references; the official class is unmodified. `TEMPLATE.md`
records the pinned download, license, and review settings. `PAPER_PLAN.md`
records the claims-evidence matrix, exclusions, and submission gates.

## Experimental presentation in the submission

Appendix D.2 reports the experimental methods, settings, outcomes, and scope
without source-file paths, command lines, or a repository dependency. It does
not ask reviewers to run code, and the mathematical proofs are self-contained.
The commands above remain here for independent reproduction. No anonymous
code repository or code-submission requirement is assumed. On 2026-09-01,
the existing GitHub project was verified publicly viewable (the root
`LICENSE.md` does not grant an open-source reuse license), with the quantum experiment
source present on `codex/fill-ramsey-gaps`; the anonymous PDF does not link to
that author-identifying repository. Its visibility was not changed by this edit.
