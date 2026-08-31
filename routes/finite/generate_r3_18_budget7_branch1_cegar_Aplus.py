#!/usr/bin/env python3
"""Reproduce the frozen reverse-first A+ branch-1 CEGAR mask batch.

The tracked history union is authenticated by the production gate.  This
script independently rebuilds the universal and exhaustive fixed-base
families, reconstructs the graph in the frozen complete common SAT model,
enumerates the first 6,512 reverse-order independent 18-sets, filters all
three exclusion families in discovery order, and writes the first 4,096
survivors in canonical sorted order.  It never invokes a SAT solver.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Sequence

try:
    from .check_r3_18_budget7_branch1_common_sat import parse_complete_model
    from .check_r3_18_budget7_branch1_core_cnf import (
        EXPECTED_BANK_SHA256,
        EXPECTED_INPUT_SHA256,
        EXPECTED_ORDERED_MASKS_SHA256,
        lexicographic_edge_variables,
        load_ordered_bank,
        read_seed_matrix,
    )
    from .r3_18_budget7_branch1_cegar_gate import (
        MASK_BATCH_SCHEMA,
        FIXED_BRANCH1_BASE_MASKS,
        FIXED_BRANCH1_BASE_ORDERED_SHA256,
        FROZEN_COMMON_MODEL_GZIP_SHA256,
        FROZEN_HISTORY_EXCLUSION_FILE_SHA256,
        FROZEN_MASK_BATCH_FILE_SHA256,
        FROZEN_MASK_BATCH_ORDERED_SHA256,
        HISTORY_EXCLUSION_ORDERED_SHA256,
        PRODUCTION_BANK_MASKS,
        PRODUCTION_MAXIMUM_VARIABLE,
        load_history_exclusion,
        ordered_masks_sha256,
    )
    from .r3_18_budget7_benders_branch1 import (
        _oracle_pass,
        fixed_base_i18_masks,
    )
    from .verify_ramsey import complement
except ImportError:  # pragma: no cover - direct execution
    from check_r3_18_budget7_branch1_common_sat import parse_complete_model
    from check_r3_18_budget7_branch1_core_cnf import (
        EXPECTED_BANK_SHA256,
        EXPECTED_INPUT_SHA256,
        EXPECTED_ORDERED_MASKS_SHA256,
        lexicographic_edge_variables,
        load_ordered_bank,
        read_seed_matrix,
    )
    from r3_18_budget7_branch1_cegar_gate import (
        MASK_BATCH_SCHEMA,
        FIXED_BRANCH1_BASE_MASKS,
        FIXED_BRANCH1_BASE_ORDERED_SHA256,
        FROZEN_COMMON_MODEL_GZIP_SHA256,
        FROZEN_HISTORY_EXCLUSION_FILE_SHA256,
        FROZEN_MASK_BATCH_FILE_SHA256,
        FROZEN_MASK_BATCH_ORDERED_SHA256,
        HISTORY_EXCLUSION_ORDERED_SHA256,
        PRODUCTION_BANK_MASKS,
        PRODUCTION_MAXIMUM_VARIABLE,
        load_history_exclusion,
        ordered_masks_sha256,
    )
    from r3_18_budget7_benders_branch1 import _oracle_pass, fixed_base_i18_masks
    from verify_ramsey import complement


SCANNED_WITNESSES = 6_512
ACCEPTED_WITNESSES = 4_096
EXPECTED_RECURSIVE_NODES = 192_166
EXPECTED_DISCOVERY_SHA256 = (
    "4ec142e9b0b49fbecca876535b53f131053cf9a5c508113dc224a197656f1133"
)
EXPECTED_EXCLUDED = 2_416


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _atomic_json(path: Path, payload: dict[str, Any]) -> None:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as sink:
            json.dump(payload, sink, indent=2, sort_keys=True)
            sink.write("\n")
            sink.flush()
            os.fsync(sink.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def reproduce(
    *,
    model_path: Path,
    history_path: Path,
    matrix_path: Path,
    bank_path: Path,
    output_path: Path,
) -> dict[str, Any]:
    if _sha256(model_path) != FROZEN_COMMON_MODEL_GZIP_SHA256:
        raise ValueError("common model gzip identity mismatch")
    assignment, _ = parse_complete_model(model_path, PRODUCTION_MAXIMUM_VARIABLE)
    variables, pairs = lexicographic_edge_variables(100)
    final_rows = [0] * 100
    for variable, (u, v) in enumerate(pairs, start=1):
        if assignment[variable]:
            final_rows[u] |= 1 << v
            final_rows[v] |= 1 << u

    rows = read_seed_matrix(matrix_path, EXPECTED_INPUT_SHA256)
    universal, universal_hash = load_ordered_bank(
        bank_path,
        order=100,
        set_size=18,
        expected_sha256=EXPECTED_BANK_SHA256,
        expected_ordered_sha256=EXPECTED_ORDERED_MASKS_SHA256,
    )
    if len(universal) != PRODUCTION_BANK_MASKS:
        raise ValueError("universal bank count mismatch")
    history, _ = load_history_exclusion(
        history_path,
        expected_file_sha256=FROZEN_HISTORY_EXCLUSION_FILE_SHA256,
    )
    fixed_base = fixed_base_i18_masks(rows)
    if (
        len(fixed_base) != FIXED_BRANCH1_BASE_MASKS
        or ordered_masks_sha256(fixed_base, 25)
        != FIXED_BRANCH1_BASE_ORDERED_SHA256
    ):
        raise ValueError("fixed-base exclusion family mismatch")

    raw, telemetry = _oracle_pass(
        complement(final_rows),
        18,
        SCANNED_WITNESSES,
        100_000_000,
        120.0,
        "reverse",
    )
    if (
        raw.reason != "WITNESS_LIMIT"
        or len(raw.witnesses) != SCANNED_WITNESSES
        or raw.recursive_nodes != EXPECTED_RECURSIVE_NODES
    ):
        raise ValueError("reverse enumeration identity mismatch")

    universal_set = set(universal)
    history_set = set(history)
    fixed_set = set(fixed_base)
    accepted_discovery = [
        mask
        for mask in raw.witnesses
        if mask not in universal_set
        and mask not in history_set
        and mask not in fixed_set
    ]
    if len(raw.witnesses) - len(accepted_discovery) != EXPECTED_EXCLUDED:
        raise ValueError("three-family exclusion count mismatch")
    accepted_discovery = accepted_discovery[:ACCEPTED_WITNESSES]
    if len(accepted_discovery) != ACCEPTED_WITNESSES:
        raise ValueError("fewer than 4096 accepted witnesses")
    discovery_hash = ordered_masks_sha256(accepted_discovery, 25)
    if discovery_hash != EXPECTED_DISCOVERY_SHA256:
        raise ValueError("accepted discovery-order digest mismatch")
    masks = sorted(accepted_discovery)
    ordered_hash = ordered_masks_sha256(masks, 25)
    if ordered_hash != FROZEN_MASK_BATCH_ORDERED_SHA256:
        raise ValueError("accepted sorted digest mismatch")

    payload = {
        "schema": MASK_BATCH_SCHEMA,
        "masks": [f"{mask:025x}" for mask in masks],
        "masks_count": len(masks),
        "ordered_masks_sha256": ordered_hash,
        "enumeration": "reverse-first",
        "exclusions": {
            "base_universal_bank": {
                "masks": len(universal),
                "ordered_masks_sha256": universal_hash,
            },
            "historical_union": {
                "masks": len(history),
                "ordered_masks_sha256": HISTORY_EXCLUSION_ORDERED_SHA256,
            },
            "fixed_branch1_base_family": {
                "masks": len(fixed_base),
                "ordered_masks_sha256": FIXED_BRANCH1_BASE_ORDERED_SHA256,
            },
        },
    }
    _atomic_json(output_path, payload)
    file_hash = _sha256(output_path)
    if file_hash != FROZEN_MASK_BATCH_FILE_SHA256:
        raise ValueError("reproduced batch file digest mismatch")
    return {
        "status": "REPRODUCED_FROZEN_A_PLUS_BATCH",
        "output": str(output_path),
        "file_sha256": file_hash,
        "ordered_masks_sha256": ordered_hash,
        "discovery_order_sha256": discovery_hash,
        "recursive_nodes": raw.recursive_nodes,
        "witnesses_scanned": len(raw.witnesses),
        "witnesses_excluded": EXPECTED_EXCLUDED,
        "witnesses_accepted": len(masks),
        "solver_invoked": False,
        "enumerator_telemetry": telemetry,
    }


def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--common-model", type=Path, required=True)
    parser.add_argument(
        "--history-exclusion",
        type=Path,
        default=here / "r3_18_budget7_branch1_cegar_history_exclusion.json",
    )
    parser.add_argument(
        "--matrix",
        type=Path,
        default=here / "certificates" / "r3_18_n100_nearmiss.txt",
    )
    parser.add_argument(
        "--universal-bank",
        type=Path,
        default=here / "r3_18_budget6_branch_0_universal_union.cuts.json",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    result = reproduce(
        model_path=args.common_model.resolve(),
        history_path=args.history_exclusion.resolve(),
        matrix_path=args.matrix.resolve(),
        bank_path=args.universal_bank.resolve(),
        output_path=args.output.resolve(),
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
