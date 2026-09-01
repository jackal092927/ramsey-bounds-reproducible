# Paper sources

`unified/` is the archival manuscript containing all four logically
independent results in one document.

`quantum/` is also the canonical standalone ITCS 2027 submission source for
the quantum-query result.  It has its own anonymous `main.tex`, paper plan,
appendices, bibliography, and reproducibility instructions.  The same section
sources are materialized into `unified/`, preventing proof drift between the
standalone and archival presentations.

`upper/`, `lower/`, and `finite/` are retained as historical source components
and provenance records.  Their section and appendix files are deterministically
materialized into the unified manuscript by
`scripts/materialize_unified_paper.py`; they are not separate submission
targets.
