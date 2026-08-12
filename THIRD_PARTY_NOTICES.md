# Third-party sources and tools

This repository contains original proof specifications, verification code,
manuscripts, and derived machine records.  It does not vendor the source of
the external papers on which the source-relative arguments depend.  Their
versioned source archives and SHA-256 identities are listed in
`external_sources/manifest.json` and can be fetched with
`scripts/fetch_external_sources.py`.

The finite graph certificates under `routes/finite/certificates/` originate
from the repositories and immutable commits recorded in
`routes/finite/certificate_manifest.json`.  They are redistributed only as
research evidence with their provenance preserved; the upstream repository
terms continue to apply.

The finite proof replay uses CaDiCaL and `drat-trim`.  The proof reports pin
CaDiCaL source commit `c60730422e758ef1cebe7aeddf2dda31c996bf04` and
`drat-trim` source commit `2e3b2dc0ecf938addbd779d42877b6ed69d9a985`.
Compiled-binary hashes in historical logs record the original run and are not
a substitute for the upstream licenses or source commits.

Python package versions are fixed in `uv.lock` and
`requirements-repro.txt`.  Each package remains subject to its own license.
No endorsement by the authors of those packages or papers is implied.
