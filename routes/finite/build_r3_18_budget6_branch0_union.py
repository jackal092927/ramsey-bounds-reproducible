#!/usr/bin/env python3
"""Build an audited universal-I18 union CNF for budget-six branch 0.

Every 18-vertex set yields the universally valid hitting clause saying that
at least one of its 153 pairs is an edge.  Consequently, masks discovered in
the other triangle-edge branches can be transferred to branch 0.  This script
validates and deduplicates all frozen sources, reconstructs the exact branch-0
formula, and writes deterministic checkpoint/CNF artifacts atomically.  It
does not import any SAT/UNSAT solver label.
"""

from __future__ import annotations

import gzip
import hashlib
import itertools
import json
import os
from pathlib import Path
from typing import Iterable

try:
    from .bounded_deletion_sat_cegar import build_variables
    from .budget8_next import deterministic_gzip_text, dimacs_lines, masks_hash, sha256
    from .new_basin_search import edge_present
    from .r3_18_branch0_two_stage import atomic_json
    from .r3_18_budget5_branch import EXPECTED_INPUT_SHA256
    from .r3_18_budget6_branch import BRANCH_EDGES, exact_branch_formula
    from .verify_ramsey import read_matrix, verify
except ImportError:  # pragma: no cover - direct execution
    from bounded_deletion_sat_cegar import build_variables
    from budget8_next import deterministic_gzip_text, dimacs_lines, masks_hash, sha256
    from new_basin_search import edge_present
    from r3_18_branch0_two_stage import atomic_json
    from r3_18_budget5_branch import EXPECTED_INPUT_SHA256
    from r3_18_budget6_branch import BRANCH_EDGES, exact_branch_formula
    from verify_ramsey import read_matrix, verify


SCHEMA = "ramsey-r3-18-n100-exact-budget6-branch0-universal-union-v1"
EXPECTED_PROOF_ARTIFACTS = {
    "r3_18_budget6_branch_1.cnf.gz": "a438c9fef4d99ae516829e4405da8c9f079398501361f9c5f69f46a494ffad14",
    "r3_18_budget6_branch_1.drat.gz": "cfe694fd728903ee9ac9f08a66ade64faf7e68763246d1d52ca29a85727494ec",
    "r3_18_budget6_branch_2.cnf.gz": "c51fed43eeca3becf64bcdfbe747a4fdf3e516ce0e6a02d7d867941b87a99c06",
    "r3_18_budget6_branch_2.drat.gz": "c9648a4e38c17dcdfe97d873095eda002abc689b3b3bd93f02fc8a369198c4b9",
}


def complete_mask(clause: list[int], inverse: dict[int, tuple[int, int]]) -> int:
    if len(clause) != 153 or len(set(clause)) != 153 or any(literal <= 0 for literal in clause):
        raise AssertionError("source I18 clause is not 153 distinct positive literals")
    try:
        edges = {inverse[literal] for literal in clause}
    except KeyError as error:
        raise AssertionError("source I18 clause uses an auxiliary variable") from error
    vertices = {vertex for edge in edges for vertex in edge}
    if len(vertices) != 18 or edges != set(itertools.combinations(sorted(vertices), 2)):
        raise AssertionError("source I18 clause is not the complete pair set of an 18-set")
    return sum(1 << vertex for vertex in vertices)


def cnf_tail_masks(path: Path, prefix_clauses: int, inverse: dict[int, tuple[int, int]]) -> list[int]:
    masks: list[int] = []
    with gzip.open(path, "rt", encoding="ascii") as source:
        header = source.readline().split()
        if len(header) != 4 or header[:2] != ["p", "cnf"]:
            raise AssertionError(f"invalid DIMACS header in {path.name}")
        for _ in range(prefix_clauses):
            next(source)
        for line in source:
            values = [int(value) for value in line.split()]
            if not values or values[-1] != 0:
                raise AssertionError(f"malformed clause in {path.name}")
            masks.append(complete_mask(values[:-1], inverse))
    return masks


def json_masks(path: Path) -> list[int]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    values: list[int | str] = []
    if payload.get("all_lazy_masks") is not None:
        values.extend(payload["all_lazy_masks"])
    elif payload.get("masks") is not None:
        values.extend(payload["masks"])
    else:
        values.extend(payload.get("preloaded_masks", []))
        values.extend(payload.get("lazy_masks", []))
    return [int(value, 16) if isinstance(value, str) else int(value) for value in values]


def validate_masks(values: Iterable[int]) -> list[int]:
    result = list(values)
    if any(mask < 0 or mask >= 1 << 100 or mask.bit_count() != 18 for mask in result):
        raise AssertionError("source contains a mask other than an 18-subset of [100]")
    return result


def atomic_deterministic_cnf(path: Path, clauses: list[list[int]], variables: int) -> dict:
    temporary = path.with_name(path.name + f".tmp.{os.getpid()}")
    raw_hash, gzip_hash, raw_bytes, lines = deterministic_gzip_text(
        temporary, dimacs_lines(clauses, variables)
    )
    temporary.replace(path)
    return {
        "path": str(path.resolve()),
        "gzip_sha256": gzip_hash,
        "raw_sha256": raw_hash,
        "gzip_bytes": path.stat().st_size,
        "raw_bytes": raw_bytes,
        "lines_including_header": lines,
    }


def main() -> None:
    directory = Path(__file__).parent
    seed_path = directory / "certificates/r3_18_n100_nearmiss.txt"
    if sha256(seed_path) != EXPECTED_INPUT_SHA256:
        raise AssertionError("near-miss seed hash mismatch")
    rows = read_matrix(seed_path)
    seed_check = verify(seed_path, 3, 18)
    if seed_check["searches"]["forbidden_independent_set"]["exists"]:
        raise AssertionError("near-miss seed unexpectedly has I18")
    for name, expected in EXPECTED_PROOF_ARTIFACTS.items():
        path = directory / name
        if sha256(path) != expected:
            raise AssertionError(f"proof dependency artifact hash mismatch: {name}")
        with gzip.open(path, "rb") as source:
            while source.read(1024 * 1024):
                pass
    for record in ("r3_18_budget6_branch_1_proof.json", "r3_18_budget6_branch_2.json"):
        payload = json.loads((directory / record).read_text(encoding="utf-8"))
        if payload.get("status") != "UNSAT_PROOF_VERIFIED":
            raise AssertionError(f"proof dependency is not verified: {record}")
    prior = json.loads((directory / "r3_18_extension_repair_check.json").read_text())
    if not prior.get("fixed_seed_budget5_repair_ball_unsat"):
        raise AssertionError("checked budget-five dependency is missing")

    variables, pairs = build_variables(100)
    inverse = {value: edge for edge, value in variables.items()}
    sources: list[tuple[str, list[int]]] = [
        (
            "r3_18_budget6_branch_0.checkpoint.json",
            json_masks(directory / "r3_18_budget6_branch_0.checkpoint.json"),
        ),
        (
            "r3_18_budget6_branch_0.cuts.json",
            json_masks(directory / "r3_18_budget6_branch_0.cuts.json"),
        ),
        (
            "r3_18_budget6_branch_1.cuts.json",
            json_masks(directory / "r3_18_budget6_branch_1.cuts.json"),
        ),
        (
            "r3_18_budget6_branch_2.cuts.json",
            json_masks(directory / "r3_18_budget6_branch_2.cuts.json"),
        ),
        (
            "r3_18_budget5_branch_0_twostage.cuts.json",
            json_masks(directory / "r3_18_budget5_branch_0_twostage.cuts.json"),
        ),
        (
            "r3_18_budget5_branch_1.cnf.gz:I18-tail",
            cnf_tail_masks(
                directory / "r3_18_budget5_branch_1.cnf.gz",
                161700 + 7394 + 1,
                inverse,
            ),
        ),
        (
            "r3_18_budget5_branch_2.cnf.gz:I18-tail",
            cnf_tail_masks(
                directory / "r3_18_budget5_branch_2.cnf.gz",
                161700 + 7394 + 1,
                inverse,
            ),
        ),
    ]
    union: set[int] = set()
    source_ledger: list[dict] = []
    for name, raw_values in sources:
        values = validate_masks(raw_values)
        before = len(union)
        union.update(values)
        source_path = directory / name.split(":", 1)[0]
        source_ledger.append(
            {
                "source": name,
                "source_sha256": sha256(source_path),
                "source_masks": len(values),
                "distinct_within_source": len(set(values)),
                "new_union_masks": len(union) - before,
                "union_after_source": len(union),
            }
        )
    ordered = sorted(union)
    if len(ordered) != 251771:
        raise AssertionError(f"unexpected universal union size: {len(ordered)}")

    checkpoint = directory / "r3_18_budget6_branch_0_universal_union.checkpoint.json"
    atomic_json(
        checkpoint,
        {
            "schema": SCHEMA,
            "status": "AUDITED_UNIVERSAL_I18_UNION",
            "branch": 0,
            "fixed_deleted_edge": list(BRANCH_EDGES[0]),
            "all_lazy_masks": ordered,
            "all_lazy_masks_sha256": masks_hash(ordered),
            "all_masks_are_18_sets": True,
            "source_ledger": source_ledger,
            "transfer_justification": (
                "For every 18-subset S, every I18-free graph satisfies the universal "
                "hitting clause OR_{e in binom(S,2)} x_e, independent of branch."
            ),
            "solver_conclusion_imported": False,
        },
    )

    original = {edge for edge in pairs if edge_present(rows, *edge)}
    clauses, maximum_variable, installed, formula = exact_branch_formula(
        rows,
        variables,
        pairs,
        original,
        BRANCH_EDGES[0],
        4096,
        ordered,
    )
    if set(installed) != set(ordered) or len(installed) != len(ordered):
        raise AssertionError("branch-0 preload introduced a mask outside the union")
    cut_path = directory / "r3_18_budget6_branch_0_universal_union.cuts.json"
    atomic_json(
        cut_path,
        {
            "schema": SCHEMA,
            "fixed_deleted_edge": list(BRANCH_EDGES[0]),
            "masks": [f"{mask:025x}" for mask in installed],
            "masks_sha256": masks_hash(installed),
            "all_masks_are_18_sets": True,
        },
    )
    cnf_path = directory / "r3_18_budget6_branch_0_universal_union.cnf.gz"
    cnf = atomic_deterministic_cnf(cnf_path, clauses, maximum_variable)
    result = {
        "schema": SCHEMA,
        "status": "AUDITED_FINITE_RELAXATION_BUILT_NO_SOLVER_CONCLUSION",
        "input_sha256": EXPECTED_INPUT_SHA256,
        "branch": 0,
        "fixed_deleted_edge": list(BRANCH_EDGES[0]),
        "exact_total_input_edge_deletions": 6,
        "exact_residual_input_edge_deletions": 5,
        "arbitrary_original_nonedge_additions_allowed": True,
        "budget5_dependency_checked": True,
        "branch1_and_branch2_proof_artifact_identities_checked": True,
        "source_ledger": source_ledger,
        "union": {
            "distinct_I18_masks": len(ordered),
            "ordered_masks_sha256": masks_hash(ordered),
            "checkpoint": str(checkpoint.resolve()),
            "checkpoint_sha256": sha256(checkpoint),
            "cut_bank": str(cut_path.resolve()),
            "cut_bank_sha256": sha256(cut_path),
        },
        "formula": {
            **formula,
            "final_clause_count": len(clauses),
            "cnf": cnf,
        },
        "global_ramsey_implication": None,
    }
    result_path = directory / "r3_18_budget6_branch_0_universal_union.json"
    atomic_json(result_path, result)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
