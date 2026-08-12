#!/usr/bin/env python3
"""Independent state checker for the first exact-seven R(3,18) portfolio."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


EXPECTED_INPUT_SHA256 = (
    "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
)
EXPECTED_BUDGET6_SUMMARY_SHA256 = (
    "0abd30457c039c1c5fbba5890153c8a0c5d8558e196e7c0561410cefe37afa6a"
)
EXPECTED_BUDGET6_REFEREE_SHA256 = (
    "1bb634ed1a6181064ac2ae0277ea6582cd2627a76a92208907cc1532d49bfede"
)
EXPECTED_UNIVERSAL_BANK_SHA256 = (
    "91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b"
)
EXPECTED_UNIVERSAL_ORDERED_SHA256 = (
    "f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa"
)
EXPECTED_EMPTY_MASKS_SHA256 = hashlib.sha256(b"").hexdigest()
EXPECTED_BRANCHES = (
    {
        "branch": 0,
        "edge": [97, 98],
        "solver": "cadical195",
        "json_sha256": "97e777da32b82a83b8e999c9af1f927c87b67689b8fb72f8b31ded07b39a2f7f",
        "checkpoint_sha256": "918dc1cc80860d97b3209f6d969a156b9df5fb8b4df7f0fa910e72fdc5778098",
    },
    {
        "branch": 1,
        "edge": [97, 99],
        "solver": "glucose42",
        "json_sha256": "81734a23298ea9c3364a047c3b7b10910bcd44faf9ff55c3a251fd709f6ac64f",
        "checkpoint_sha256": "8491cbd5e073170b6f7a503efb3d6af6c077b6d72defbf9cd6feb6f06e85fc7f",
    },
    {
        "branch": 2,
        "edge": [98, 99],
        "solver": "maplechrono",
        "json_sha256": "92e2c948892d6f298e0ca3a5055cf31cf3eea361b6eee8197ba536922e437554",
        "checkpoint_sha256": "9e8ea23904378ec1bfc6e4c486fd32f10ccc99c1646855c7589c21cc3c9b9f5c",
    },
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_universal_bank(path: Path) -> dict[str, Any]:
    require(sha256(path) == EXPECTED_UNIVERSAL_BANK_SHA256, "universal bank hash")
    payload = json.loads(path.read_text(encoding="utf-8"))
    values = payload.get("masks")
    require(isinstance(values, list) and len(values) == 251_771, "universal bank count")
    digest = hashlib.sha256()
    seen: set[int] = set()
    for value in values:
        require(isinstance(value, str) and len(value) == 25, "mask representation")
        mask = int(value, 16)
        require(mask.bit_count() == 18 and mask >> 100 == 0, "mask semantics")
        require(mask not in seen, "duplicate universal mask")
        seen.add(mask)
        digest.update(f"{mask:016x}\n".encode("ascii"))
    ordered = digest.hexdigest()
    require(ordered == EXPECTED_UNIVERSAL_ORDERED_SHA256, "ordered mask digest")
    require(payload.get("masks_sha256") == ordered, "stored ordered mask digest")
    return {"masks": len(values), "ordered_masks_sha256": ordered}


def validate_branch(directory: Path, expected: dict[str, Any]) -> dict[str, Any]:
    branch = expected["branch"]
    result_path = directory / f"r3_18_budget7_branch_{branch}.json"
    checkpoint_path = directory / f"r3_18_budget7_branch_{branch}.checkpoint.json"
    require(sha256(result_path) == expected["json_sha256"], f"branch {branch} result hash")
    require(
        sha256(checkpoint_path) == expected["checkpoint_sha256"],
        f"branch {branch} checkpoint hash",
    )
    result = json.loads(result_path.read_text(encoding="utf-8"))
    checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    require(result.get("branch") == branch, f"branch {branch} identity")
    require(result.get("fixed_deleted_edge") == expected["edge"], f"branch {branch} edge")
    require(result.get("input_sha256") == EXPECTED_INPUT_SHA256, f"branch {branch} input")
    require(result.get("exact_total_input_edge_deletions") == 7, f"branch {branch} total")
    require(result.get("exact_residual_input_edge_deletions") == 6, f"branch {branch} residual")
    require(result.get("arbitrary_original_nonedge_additions_allowed") is True, f"branch {branch} additions")
    require(result.get("status") == "UNKNOWN", f"branch {branch} top status")
    require(result.get("global_ramsey_implication") is None, f"branch {branch} implication")
    dependency = result.get("budget_at_most_6_proof_dependency", {})
    require(dependency.get("sha256") == EXPECTED_BUDGET6_SUMMARY_SHA256, f"branch {branch} summary dependency")
    require(dependency.get("complete_referee_sha256") == EXPECTED_BUDGET6_REFEREE_SHA256, f"branch {branch} referee dependency")
    require(dependency.get("all_three_branch_identities_cross_checked") is True, f"branch {branch} dependency audit")
    require(result.get("tools", {}).get("discovery_solver") == expected["solver"], f"branch {branch} solver")
    require(result.get("limits", {}).get("discovery_wall_seconds") == 300.0, f"branch {branch} wall")
    discovery = result.get("discovery", {})
    require(discovery.get("status") == "UNKNOWN_DISCOVERY_WALL_LIMIT", f"branch {branch} endpoint")
    require(discovery.get("wall_limit_seconds") == 300.0, f"branch {branch} endpoint wall")
    require(300.0 <= discovery.get("elapsed_seconds", 0) < 301.0, f"branch {branch} elapsed")
    require(discovery.get("last_checkpoint") == checkpoint, f"branch {branch} checkpoint embedding")
    require(checkpoint.get("status") == "READY", f"branch {branch} checkpoint state")
    require(checkpoint.get("fixed_deleted_edge") == expected["edge"], f"branch {branch} checkpoint edge")
    require(checkpoint.get("iterations_this_run") == 0, f"branch {branch} iterations")
    require(checkpoint.get("new_masks") == [], f"branch {branch} new masks")
    require(checkpoint.get("new_masks_sha256") == EXPECTED_EMPTY_MASKS_SHA256, f"branch {branch} new-mask digest")
    formula = checkpoint.get("formula", {})
    exact_formula = {
        "edge_variables": 4_950,
        "auxiliary_variables": 9_840,
        "maximum_variable": 14_790,
        "triangle_clauses": 161_700,
        "exact_six_residual_counter_literals": 826,
        "exact_six_residual_counter_clauses": 19_680,
        "fixed_negative_units": 1,
        "structural_clauses": 181_381,
        "base_universal_I18_clauses": 251_771,
        "resumed_additional_I18_clauses": 0,
        "initial_total_clauses": 433_152,
        "original_nonedge_variables_in_deletion_counter": 0,
    }
    for key, value in exact_formula.items():
        require(formula.get(key) == value, f"branch {branch} formula {key}")
    require(formula.get("arbitrary_original_nonedge_additions_allowed") is True, f"branch {branch} formula additions")
    return {
        "branch": branch,
        "fixed_deleted_edge": expected["edge"],
        "solver": expected["solver"],
        "status": "UNKNOWN_DISCOVERY_WALL_LIMIT",
        "elapsed_seconds": discovery["elapsed_seconds"],
        "iterations": 0,
        "new_masks": 0,
        "result_sha256": expected["json_sha256"],
        "checkpoint_sha256": expected["checkpoint_sha256"],
    }


def validate_directory(directory: Path) -> dict[str, Any]:
    require(
        sha256(directory / "certificates" / "r3_18_n100_nearmiss.txt")
        == EXPECTED_INPUT_SHA256,
        "input identity",
    )
    require(
        sha256(directory / "r3_18_budget6_summary.json")
        == EXPECTED_BUDGET6_SUMMARY_SHA256,
        "budget-six summary identity",
    )
    require(
        sha256(directory / "INDEPENDENT_R3_18_BUDGET6_COMPLETE_REFEREE.md")
        == EXPECTED_BUDGET6_REFEREE_SHA256,
        "budget-six referee identity",
    )
    bank = validate_universal_bank(
        directory / "r3_18_budget6_branch_0_universal_union.cuts.json"
    )
    branches = [validate_branch(directory, expected) for expected in EXPECTED_BRANCHES]
    return {
        "schema": "ramsey-r3-18-n100-exact-budget7-first-round-check-v1",
        "status": "FIRST_ROUND_STATE_VERIFIED",
        "universal_bank": bank,
        "branches": branches,
        "all_three_branches_unknown": True,
        "sat_witness_found": False,
        "unsat_proof_verified": False,
        "global_ramsey_implication": None,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "directory",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parent,
    )
    args = parser.parse_args()
    print(json.dumps(validate_directory(args.directory.resolve()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
