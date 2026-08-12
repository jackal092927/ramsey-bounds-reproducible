#!/usr/bin/env python3
"""Independent semantic audit of the frozen exact-budget-six branch-2 proof."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path
from typing import Iterator

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

try:
    from .bounded_deletion_sat_cegar import build_variables
    from .budget8_next import verify_drat_trace
    from .new_basin_search import edge_present
    from .r3_18_budget5_branch import EXPECTED_INPUT_SHA256, EXPECTED_TRIANGLE
    from .verify_ramsey import read_matrix, verify
except ImportError:  # pragma: no cover
    from bounded_deletion_sat_cegar import build_variables
    from budget8_next import verify_drat_trace
    from new_basin_search import edge_present
    from r3_18_budget5_branch import EXPECTED_INPUT_SHA256, EXPECTED_TRIANGLE
    from verify_ramsey import read_matrix, verify


EXPECTED_BRANCH = 2
EXPECTED_FIXED_EDGE = (98, 99)
EXPECTED_CNF_SHA256 = "c51fed43eeca3becf64bcdfbe747a4fdf3e516ce0e6a02d7d867941b87a99c06"
EXPECTED_DRAT_SHA256 = "c9648a4e38c17dcdfe97d873095eda002abc689b3b3bd93f02fc8a369198c4b9"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clauses(path: Path) -> tuple[tuple[int, int], Iterator[list[int]]]:
    source = gzip.open(path, "rt", encoding="ascii")
    header = source.readline().split()
    if len(header) != 4 or header[:2] != ["p", "cnf"]:
        source.close()
        raise AssertionError("invalid DIMACS header")

    def iterator() -> Iterator[list[int]]:
        try:
            for line in source:
                values = [int(value) for value in line.split()]
                if not values or values[-1] != 0:
                    raise AssertionError("invalid DIMACS clause")
                yield values[:-1]
        finally:
            source.close()

    return (int(header[2]), int(header[3])), iterator()


def assert_i18_clause(clause: list[int], inverse: dict[int, tuple[int, int]]) -> None:
    if len(clause) != 153 or len(set(clause)) != 153 or any(lit <= 0 for lit in clause):
        raise AssertionError("I18 clause is not 153 distinct positive literals")
    try:
        pairs = {inverse[lit] for lit in clause}
    except KeyError as error:
        raise AssertionError("I18 clause uses a counter variable") from error
    vertices = {vertex for pair in pairs for vertex in pair}
    if len(vertices) != 18 or pairs != set(itertools.combinations(sorted(vertices), 2)):
        raise AssertionError("I18 clause is not the complete edge set of an 18-set")


def audit_cnf(cnf: Path, rows: list[int]) -> dict:
    if sha256(cnf) != EXPECTED_CNF_SHA256:
        raise AssertionError("frozen CNF hash mismatch")
    variables, pairs = build_variables(len(rows))
    inverse = {variable: edge for edge, variable in variables.items()}
    original = {edge for edge in pairs if edge_present(rows, *edge)}
    residual = sorted(original - {EXPECTED_FIXED_EDGE})
    pool = IDPool(start_from=len(pairs) + 1)
    exact_five = CardEnc.equals(
        lits=[-variables[edge] for edge in residual],
        bound=5,
        vpool=pool,
        encoding=EncType.seqcounter,
    ).clauses
    header, stream = clauses(cnf)
    if header[0] != pool.top:
        raise AssertionError("maximum variable differs from exact-five reconstruction")

    seen = 0
    for a, b, c in itertools.combinations(range(len(rows)), 3):
        expected = [-variables[(a, b)], -variables[(a, c)], -variables[(b, c)]]
        if next(stream) != expected:
            raise AssertionError("triangle prefix differs from reconstruction")
        seen += 1
    for expected in exact_five:
        if next(stream) != expected:
            raise AssertionError("exact-five counter differs from reconstruction")
        seen += 1
    if next(stream) != [-variables[EXPECTED_FIXED_EDGE]]:
        raise AssertionError("fixed triangle edge is not a negative unit")
    seen += 1
    blue = 0
    for clause in stream:
        assert_i18_clause(clause, inverse)
        blue += 1
        seen += 1
    if seen != header[1] or blue == 0:
        raise AssertionError("clause count mismatch or empty I18 bank")
    return {
        "status": "SEMANTICS_VERIFIED",
        "maximum_variable": header[0],
        "clauses": header[1],
        "triangle_clauses": 161700,
        "exact_five_residual_deletion_clauses": len(exact_five),
        "fixed_negative_units": 1,
        "I18_hitting_clauses": blue,
        "arbitrary_original_nonedges_absent_from_deletion_counter": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-dir", type=Path, default=Path(__file__).parent)
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--drat-seconds", type=float, default=300.0)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    directory = args.artifact_dir
    matrix = directory / "certificates/r3_18_n100_nearmiss.txt"
    cnf = directory / "r3_18_budget6_branch_2.cnf.gz"
    drat = directory / "r3_18_budget6_branch_2.drat.gz"
    run = json.loads((directory / "r3_18_budget6_branch_2.json").read_text())
    old = json.loads((directory / "r3_18_extension_repair_check.json").read_text())
    if sha256(matrix) != EXPECTED_INPUT_SHA256:
        raise AssertionError("near-miss hash mismatch")
    if sha256(drat) != EXPECTED_DRAT_SHA256:
        raise AssertionError("frozen DRAT hash mismatch")
    if run.get("branch") != EXPECTED_BRANCH or run.get("status") != "UNSAT_PROOF_VERIFIED":
        raise AssertionError("stored branch-2 result is not proof-verified UNSAT")
    if not old.get("fixed_seed_budget5_repair_ball_unsat"):
        raise AssertionError("checked budget-five dependency is absent")
    rows = read_matrix(matrix)
    seed = verify(matrix, 3, 18)
    if seed["searches"]["forbidden_independent_set"]["exists"]:
        raise AssertionError("near miss unexpectedly has I18")
    semantics = audit_cnf(cnf, rows)
    proof = {"status": "NOT_RERUN"}
    if args.drat_trim is not None:
        proof = verify_drat_trace(args.drat_trim, cnf, drat, args.drat_seconds)
        if proof["status"] != "VERIFIED":
            raise AssertionError("DRAT replay failed")
    result = {
        "status": "BRANCH2_EXACT_BUDGET6_PROOF_VERIFIED",
        "fixed_deleted_edge": list(EXPECTED_FIXED_EDGE),
        "semantics": semantics,
        "proof": proof,
        "budget5_dependency_checked": True,
        "overall_budget6_three_branch_status": "UNKNOWN_BRANCHES_0_AND_1",
        "global_ramsey_bound_improvement": False,
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.json is not None:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
