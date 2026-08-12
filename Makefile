.PHONY: bootstrap verify-fast verify-full verify-upper verify-lower verify-finite papers clean

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

papers:
	bash scripts/compile_papers.sh

clean:
	latexmk -C -cd papers/upper/main.tex
	latexmk -C -cd papers/lower/main.tex
	latexmk -C -cd papers/finite/main.tex
