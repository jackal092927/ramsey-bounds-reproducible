.PHONY: bootstrap verify-fast verify-full verify-upper verify-lower verify-finite verify-quantum paper papers clean

bootstrap:
	bash scripts/bootstrap.sh

verify-fast:
	.venv/bin/python reproduce.py quick

verify-full:
	.venv/bin/python reproduce.py full

verify-upper:
	bash scripts/reproduce_upper.sh

verify-lower:
	bash scripts/reproduce_lower.sh

verify-finite:
	bash scripts/reproduce_finite_light.sh

verify-quantum:
	.venv/bin/python experiments/quantum_ramsey/implicit_majority_audit.py --self-check --check-only

paper:
	bash scripts/compile_papers.sh

papers: paper

clean:
	latexmk -C -cd papers/unified/main.tex
