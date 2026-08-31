#!/usr/bin/env python3
"""Check a SAT witness for the frozen branch-1 common relaxation.

This checker is deliberately independent of the production exporter and
PySAT.  It reuses only the handwritten reconstruction layer used by the
generalized-core auditor, compares the complete common CNF byte-for-byte,
parses a complete CaDiCaL model, and evaluates every reconstructed clause.

A successful audit proves that the finite-bank relaxation ``Psi_1`` is
satisfiable.  It does not prove that the represented graph has independence
number below 18; an explicit independent-18 witness is reported when one is
present.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Sequence

try:
    from .check_r3_18_budget7_branch1_core_cnf import (
        AuditError,
        EXPECTED_BANK_SHA256,
        EXPECTED_DEGREE_SHA256,
        EXPECTED_FORMULA_FINGERPRINT,
        EXPECTED_INPUT_SHA256,
        EXPECTED_MAPPING_SHA256,
        EXPECTED_ORDERED_MASKS_SHA256,
        EXPECTED_STRUCTURAL_SHA256,
        FormulaSpec,
        PRODUCTION_BANK_MASKS,
        PRODUCTION_BANK_SET_SIZE,
        PRODUCTION_COMMON_CLAUSES,
        PRODUCTION_DEGREE_CAP,
        PRODUCTION_DEGREE_CLAUSES,
        PRODUCTION_EDGE_VARIABLES,
        PRODUCTION_FIXED_EDGE,
        PRODUCTION_INPUT_EDGES,
        PRODUCTION_MAXIMUM_VARIABLE,
        PRODUCTION_ORDER,
        PRODUCTION_RESIDUAL_DELETIONS,
        PRODUCTION_RESIDUAL_EDGES,
        PRODUCTION_STRUCTURAL_CLAUSES,
        build_reconstruction_plan,
        compare_gzip_dimacs,
        iter_expected_clauses,
        load_ordered_bank,
        read_seed_matrix,
        reconstructed_formula_fingerprint,
    )
    from .verify_ramsey import CliqueTargetSearch, complement
except ImportError:  # pragma: no cover - direct script execution
    from check_r3_18_budget7_branch1_core_cnf import (
        AuditError,
        EXPECTED_BANK_SHA256,
        EXPECTED_DEGREE_SHA256,
        EXPECTED_FORMULA_FINGERPRINT,
        EXPECTED_INPUT_SHA256,
        EXPECTED_MAPPING_SHA256,
        EXPECTED_ORDERED_MASKS_SHA256,
        EXPECTED_STRUCTURAL_SHA256,
        FormulaSpec,
        PRODUCTION_BANK_MASKS,
        PRODUCTION_BANK_SET_SIZE,
        PRODUCTION_COMMON_CLAUSES,
        PRODUCTION_DEGREE_CAP,
        PRODUCTION_DEGREE_CLAUSES,
        PRODUCTION_EDGE_VARIABLES,
        PRODUCTION_FIXED_EDGE,
        PRODUCTION_INPUT_EDGES,
        PRODUCTION_MAXIMUM_VARIABLE,
        PRODUCTION_ORDER,
        PRODUCTION_RESIDUAL_DELETIONS,
        PRODUCTION_RESIDUAL_EDGES,
        PRODUCTION_STRUCTURAL_CLAUSES,
        build_reconstruction_plan,
        compare_gzip_dimacs,
        iter_expected_clauses,
        load_ordered_bank,
        read_seed_matrix,
        reconstructed_formula_fingerprint,
    )
    from verify_ramsey import CliqueTargetSearch, complement


SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-common-sat-audit-v1"
STATUS = "VERIFIED_BRANCH1_COMMON_RELAXATION_SAT_MODEL"
FORCED_EDGE_PROBES = ((11, 62), (18, 61), (18, 64), (18, 69))


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _mapping_sha256(variables: dict[tuple[int, int], int]) -> str:
    digest = hashlib.sha256()
    for (u, v), variable in sorted(variables.items()):
        digest.update(f"x {u} {v} {variable}\n".encode("ascii"))
    return digest.hexdigest()


def _artifact(path: Path, raw: bytes | None = None) -> dict[str, Any]:
    result = {
        "basename": path.name,
        "bytes": path.stat().st_size,
        "sha256": _sha256_file(path),
    }
    if raw is not None:
        result.update(
            {
                "uncompressed_bytes": len(raw),
                "uncompressed_sha256": _sha256_bytes(raw),
            }
        )
    return result


def parse_complete_model(
    model_path: Path, maximum_variable: int
) -> tuple[list[bool | None], dict[str, Any]]:
    """Parse one strict gzip model with every variable assigned exactly once."""

    if not model_path.is_file():
        raise AuditError(f"model is not a regular file: {model_path.name}")
    compressed = model_path.read_bytes()
    try:
        raw = gzip.decompress(compressed)
        text = raw.decode("ascii")
    except (OSError, EOFError, UnicodeError) as error:
        raise AuditError("model is not a complete ASCII gzip stream") from error
    if not raw.endswith(b"\n") or b"\r" in raw:
        raise AuditError("model must use complete LF-terminated lines")
    lines = text.splitlines()
    if not lines or lines[0] != "s SATISFIABLE":
        raise AuditError("model lacks the exact SAT status line")
    if any(not line.startswith("v ") for line in lines[1:]):
        raise AuditError("model contains a non-assignment line")

    tokens: list[int] = []
    for line in lines[1:]:
        fields = line.split()[1:]
        if not fields:
            raise AuditError("model contains an empty assignment line")
        try:
            tokens.extend(int(field) for field in fields)
        except ValueError as error:
            raise AuditError("model contains a non-integer token") from error
    if not tokens or tokens[-1] != 0 or any(token == 0 for token in tokens[:-1]):
        raise AuditError("model must contain one final zero terminator")

    assignment: list[bool | None] = [None] * (maximum_variable + 1)
    for literal in tokens[:-1]:
        variable = abs(literal)
        if not 1 <= variable <= maximum_variable:
            raise AuditError("model literal lies outside the DIMACS variable range")
        if assignment[variable] is not None:
            raise AuditError("model assigns a variable more than once")
        assignment[variable] = literal > 0
    missing = [index for index in range(1, maximum_variable + 1) if assignment[index] is None]
    if missing:
        raise AuditError("model does not assign every DIMACS variable")
    return assignment, {
        **_artifact(model_path, raw),
        "assignment_literals": len(tokens) - 1,
        "assignment_lines": len(lines) - 1,
        "status_line": "s SATISFIABLE",
    }


def _literal_true(literal: int, assignment: Sequence[bool | None]) -> bool:
    value = assignment[abs(literal)]
    if value is None:
        raise AuditError("clause evaluation reached an unassigned variable")
    return bool(value) if literal > 0 else not bool(value)


def audit_common_sat(
    *,
    cnf_path: Path,
    model_path: Path,
    matrix_path: Path,
    bank_path: Path,
    expected_cnf_raw_sha256: str | None = None,
    expected_cnf_gzip_sha256: str | None = None,
    expected_model_raw_sha256: str | None = None,
    expected_model_gzip_sha256: str | None = None,
) -> dict[str, Any]:
    spec = FormulaSpec(
        order=PRODUCTION_ORDER,
        fixed_edge=PRODUCTION_FIXED_EDGE,
        residual_deletions=PRODUCTION_RESIDUAL_DELETIONS,
        degree_cap=PRODUCTION_DEGREE_CAP,
        bank_set_size=PRODUCTION_BANK_SET_SIZE,
    )
    rows = read_seed_matrix(matrix_path, EXPECTED_INPUT_SHA256)
    masks, ordered_masks_sha256 = load_ordered_bank(
        bank_path,
        order=spec.order,
        set_size=spec.bank_set_size,
        expected_sha256=EXPECTED_BANK_SHA256,
        expected_ordered_sha256=EXPECTED_ORDERED_MASKS_SHA256,
    )
    plan = build_reconstruction_plan(rows, spec)
    if len(plan.original_edges) != PRODUCTION_INPUT_EDGES:
        raise AuditError("production matrix edge count mismatch")
    if len(plan.residual_edges) != PRODUCTION_RESIDUAL_EDGES:
        raise AuditError("production residual edge count mismatch")
    if len(plan.pairs) != PRODUCTION_EDGE_VARIABLES:
        raise AuditError("production edge-variable count mismatch")
    if _mapping_sha256(plan.variables) != EXPECTED_MAPPING_SHA256:
        raise AuditError("production edge-variable mapping digest mismatch")
    if plan.structural_clause_count != PRODUCTION_STRUCTURAL_CLAUSES:
        raise AuditError("production structural-clause count mismatch")
    if plan.degree_clause_count != PRODUCTION_DEGREE_CLAUSES:
        raise AuditError("production degree-clause count mismatch")
    if len(masks) != PRODUCTION_BANK_MASKS:
        raise AuditError("production universal-bank count mismatch")
    if plan.maximum_variable != PRODUCTION_MAXIMUM_VARIABLE:
        raise AuditError("production maximum-variable count mismatch")

    cnf = compare_gzip_dimacs(cnf_path, plan, masks, ())
    if cnf.clauses != PRODUCTION_COMMON_CLAUSES:
        raise AuditError("common CNF clause count mismatch")
    if cnf.structural_clauses_sha256 != EXPECTED_STRUCTURAL_SHA256:
        raise AuditError("common structural-clause digest mismatch")
    if cnf.degree_clauses_sha256 != EXPECTED_DEGREE_SHA256:
        raise AuditError("common degree-clause digest mismatch")
    if expected_cnf_raw_sha256 and cnf.uncompressed_sha256 != expected_cnf_raw_sha256:
        raise AuditError("common CNF raw digest differs from the frozen value")
    if expected_cnf_gzip_sha256 and cnf.gzip_sha256 != expected_cnf_gzip_sha256:
        raise AuditError("common CNF gzip digest differs from the frozen value")
    formula_fingerprint, _ = reconstructed_formula_fingerprint(
        plan,
        input_sha256=EXPECTED_INPUT_SHA256,
        bank_sha256=EXPECTED_BANK_SHA256,
        masks=masks,
        ordered_masks_sha256=ordered_masks_sha256,
        audit=cnf,
    )
    if formula_fingerprint != EXPECTED_FORMULA_FINGERPRINT:
        raise AuditError("common formula fingerprint mismatch")

    assignment, model = parse_complete_model(model_path, plan.maximum_variable)
    if expected_model_raw_sha256 and model["uncompressed_sha256"] != expected_model_raw_sha256:
        raise AuditError("model raw digest differs from the frozen value")
    if expected_model_gzip_sha256 and model["sha256"] != expected_model_gzip_sha256:
        raise AuditError("model gzip digest differs from the frozen value")

    checked_clauses = 0
    for checked_clauses, (_, clause) in enumerate(
        iter_expected_clauses(plan, masks, ()), start=1
    ):
        if not any(_literal_true(literal, assignment) for literal in clause):
            raise AuditError(f"model falsifies reconstructed clause {checked_clauses}")
    if checked_clauses != PRODUCTION_COMMON_CLAUSES:
        raise AuditError("model evaluation did not cover every common clause")

    final_rows = [0] * PRODUCTION_ORDER
    for variable, (u, v) in enumerate(plan.pairs, start=1):
        if assignment[variable]:
            final_rows[u] |= 1 << v
            final_rows[v] |= 1 << u
    deleted = sorted(plan.original_edges - {
        edge for variable, edge in enumerate(plan.pairs, start=1) if assignment[variable]
    })
    added = sorted({
        edge for variable, edge in enumerate(plan.pairs, start=1) if assignment[variable]
    } - plan.original_edges)
    independent = CliqueTargetSearch(complement(final_rows), 18).run()

    forced_values = {
        f"{u}-{v}": bool(assignment[plan.variables[(u, v)]])
        for u, v in FORCED_EDGE_PROBES
    }
    return {
        "schema": SCHEMA,
        "status": STATUS,
        "claim_boundary": (
            "This proves only that the frozen finite-bank common relaxation Psi_1 "
            "is satisfiable. The displayed independent 18-set shows that this "
            "particular model is not an exact-seven Ramsey repair."
        ),
        "formula": {
            "formula_fingerprint_sha256": formula_fingerprint,
            "variables": cnf.variables,
            "clauses": cnf.clauses,
            "header_and_clause_lines": cnf.lines,
            "uncompressed_bytes": cnf.uncompressed_bytes,
            "uncompressed_sha256": cnf.uncompressed_sha256,
            "gzip_bytes": cnf.gzip_bytes,
            "gzip_sha256": cnf.gzip_sha256,
            "candidate_units": 0,
            "learned_core_clauses_installed": 0,
        },
        "model": model,
        "verification": {
            "all_common_clauses_satisfied": True,
            "clauses_evaluated": checked_clauses,
            "forced_probe_edge_values": forced_values,
            "final_edges": sum(row.bit_count() for row in final_rows) // 2,
            "deleted_seed_edges": [list(edge) for edge in deleted],
            "added_seed_nonedges": [list(edge) for edge in added],
            "exact_total_seed_deletions": len(deleted),
            "independent_18_exists": independent.exists,
            "independent_18_witness": independent.witness,
            "independent_search_nodes": independent.recursive_nodes,
        },
        "common_relaxation_nonempty": True,
        "this_model_is_exact_seven_repair": not independent.exists,
        "exact_seven_repair_exists": None,
        "global_ramsey_implication": None,
        "provenance": {
            "checker": _artifact(Path(__file__).resolve()),
            "production_formula_builder_imported": False,
            "pysat_imported": False,
        },
    }


def _atomic_json(path: Path, payload: dict[str, Any], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"refusing to overwrite {path.name}")
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary_path = Path(temporary)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as sink:
            json.dump(payload, sink, indent=2, sort_keys=True)
            sink.write("\n")
            sink.flush()
            os.fsync(sink.fileno())
        os.replace(temporary_path, path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cnf", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
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
    parser.add_argument("--expected-cnf-raw-sha256")
    parser.add_argument("--expected-cnf-gzip-sha256")
    parser.add_argument("--expected-model-raw-sha256")
    parser.add_argument("--expected-model-gzip-sha256")
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    protected = {
        args.cnf.resolve(),
        args.model.resolve(),
        args.matrix.resolve(),
        args.universal_bank.resolve(),
        Path(__file__).resolve(),
        Path(__file__).resolve().with_name(
            "check_r3_18_budget7_branch1_core_cnf.py"
        ).resolve(),
        Path(__file__).resolve().with_name("independent_seqcounter.py").resolve(),
        Path(__file__).resolve().with_name("verify_ramsey.py").resolve(),
    }
    output = args.json_output.resolve() if args.json_output else None
    if output is not None:
        if output in protected:
            parser.error("JSON output collides with an authenticated checker input")
        if output.exists() and not args.overwrite:
            parser.error(f"refusing to overwrite {output.name}")

    try:
        result = audit_common_sat(
            cnf_path=args.cnf.resolve(),
            model_path=args.model.resolve(),
            matrix_path=args.matrix.resolve(),
            bank_path=args.universal_bank.resolve(),
            expected_cnf_raw_sha256=args.expected_cnf_raw_sha256,
            expected_cnf_gzip_sha256=args.expected_cnf_gzip_sha256,
            expected_model_raw_sha256=args.expected_model_raw_sha256,
            expected_model_gzip_sha256=args.expected_model_gzip_sha256,
        )
    except Exception as error:
        failure = {
            "schema": SCHEMA,
            "status": "FAILED_BRANCH1_COMMON_RELAXATION_SAT_AUDIT",
            "error_type": type(error).__name__,
            "error": str(error),
        }
        print(json.dumps(failure, sort_keys=True), file=sys.stderr)
        if output is not None:
            _atomic_json(output, failure, args.overwrite)
        return 1

    if output is not None:
        _atomic_json(output, result, args.overwrite)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
