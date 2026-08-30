# Paper sources

`unified/` is the only canonical manuscript and publication output.  It
contains all three logically independent results in one paper.

`upper/`, `lower/`, and `finite/` are retained as historical source components
and provenance records.  Their section and appendix files are deterministically
materialized into the unified manuscript by
`scripts/materialize_unified_paper.py`; they are not separate submission
targets.
