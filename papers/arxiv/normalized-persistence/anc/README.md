# Computational supplement

This directory contains the finite-certificate and small-fixture checks used by
the preprint. It contains no author names, private paths, browser
transcripts, credentials, or version-control history.

## Environment

- Python 3.10 or newer
- NumPy and SciPy, as listed in `requirements.txt`

Run the following commands from this directory:

1. `python3 certify_representative_bulk.py --offline`
2. `python3 certify_remaining_active_atoms.py --offline`
3. `python3 check_active_hadamard_orbit.py`
4. `python3 check_selected_cycle_guard.py`
5. `python3 check_exact_filling_coercivity.py`
6. `python3 check_weighted_history.py`
7. `python3 check_kernel_filtration.py`
8. `python3 check_common_blowup.py`
9. `python3 check_padded_bulk.py`

Every command must terminate with a PASS status. The certificate scripts use
exact integer or rational linear algebra where stated. Floating-point spectral
calculations are small-fixture consistency checks and are not substituted for
the paper's symbolic proofs.

## Provenance boundary

The representative source fixture was derived from Dorian Rudolph's public
`QMA1-gateset-paper` repository at immutable commit
`30ac70e5dacdecce97c38d801c128ec3ed93a96a`. The corresponding downloaded
source file had SHA-256 digest
`c8918f9e037ae79796bb65640170c8e60f31883625d24348f3476f7644dcd29a`.
No third-party source code is redistributed in this supplement.
