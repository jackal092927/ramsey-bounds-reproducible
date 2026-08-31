#!/usr/bin/env python3
"""Deletion-only fixed-base covering projection for branch 1.

This module builds a *necessary*, deliberately incomplete projection of a
repair of the frozen near-miss after fixing ``(97,99)`` absent.  Its primary
variables are

``d_e``
    whether a remaining seed edge is deleted, and
``g_uv``
    whether an original nonedge is declared locally eligible for addition.

Local eligibility means that every seed triangle which adding ``uv`` would
create is broken by a deletion.  Every independent 18-set already present in
the fixed base must contain at least one locally eligible pair.  This forgets
all interactions between two additions and all independent sets created by
the residual deletions, so satisfiability is not a repair certificate.

The exact-six profile is the uniform core with five residual deletions.  The
exact-seven profile has six residual deletions and additionally installs the
four separately proof-checked singleton deletion exclusions.  The singleton
units are intentionally not imported into the exact-six strength gate.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import stat
import tempfile
import threading
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Sequence

try:
    from .independent_seqcounter import encode_equals
except ImportError:  # pragma: no cover - direct script execution
    from independent_seqcounter import encode_equals


Edge = tuple[int, int]

SCHEMA = "ramsey-r3-18-n100-branch1-deletion-covering-projection-v1"
ORDER = 100
TARGET_INDEPENDENCE = 18
FIXED_EDGE: Edge = (97, 99)
DEGREE_HIT_VERTEX = 98
EXPECTED_SEED_SHA256 = (
    "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
)
EXPECTED_SEED_EDGES = 827
EXPECTED_TRIANGLE = (97, 98, 99)
EXPECTED_BASE_EDGES = 826
EXPECTED_ADDITION_PAIRS = 4_123
EXPECTED_CANDIDATE_VERTICES = 65
EXPECTED_FIXED_BASE_I18 = 235_504
EXPECTED_FIXED_BASE_I18_SHA256 = (
    "1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c"
)
FORCED_RETAINED_EDGES: tuple[Edge, ...] = (
    (11, 62),
    (18, 61),
    (18, 64),
    (18, 69),
)
PROFILES: Mapping[str, tuple[int, bool]] = {
    "exact-six": (5, False),
    "exact-seven": (6, True),
}


class ProjectionError(ValueError):
    """Fail-closed input or semantic error."""


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical_sha256(payload: Any) -> str:
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return sha256_bytes(raw)


def mask_digest(masks: Iterable[int]) -> str:
    digest = hashlib.sha256()
    for mask in masks:
        digest.update(f"{mask:016x}\n".encode("ascii"))
    return digest.hexdigest()


def edge_digest(edges: Iterable[Edge], label: str) -> str:
    digest = hashlib.sha256()
    digest.update((label + "\n").encode("ascii"))
    for u, v in edges:
        digest.update(f"{u},{v}\n".encode("ascii"))
    return digest.hexdigest()


def normalized_edge(u: int, v: int) -> Edge:
    if u == v:
        raise ProjectionError("a graph edge must have distinct endpoints")
    return (u, v) if u < v else (v, u)


def edge_rows(edges: Iterable[Edge], order: int = ORDER) -> list[int]:
    rows = [0] * order
    for u, v in edges:
        if not (0 <= u < v < order):
            raise ProjectionError("edge outside the frozen vertex set")
        rows[u] |= 1 << v
        rows[v] |= 1 << u
    return rows


def edge_set(rows: Sequence[int]) -> set[Edge]:
    return {
        (u, v)
        for u in range(len(rows))
        for v in range(u + 1, len(rows))
        if rows[u] >> v & 1
    }


def vertices(mask: int) -> list[int]:
    return [v for v in range(mask.bit_length()) if mask >> v & 1]


def strict_seed(path: Path) -> tuple[list[int], dict[str, Any]]:
    try:
        metadata = os.lstat(path)
    except OSError as error:
        raise ProjectionError("seed cannot be inspected") from error
    if not stat.S_ISREG(metadata.st_mode):
        raise ProjectionError("seed must be a non-symlink regular file")
    raw = path.read_bytes()
    if sha256_bytes(raw) != EXPECTED_SEED_SHA256:
        raise ProjectionError("seed SHA-256 mismatch")
    if not raw.endswith(b"\n") or b"\r" in raw:
        raise ProjectionError("seed must use canonical LF termination")
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeError as error:
        raise ProjectionError("seed is not ASCII") from error
    if len(lines) != ORDER:
        raise ProjectionError("seed has the wrong number of rows")
    matrix: list[list[int]] = []
    for line in lines:
        fields = line.split()
        if len(fields) != ORDER or any(x not in {"0", "1"} for x in fields):
            raise ProjectionError("seed is not a strict 100 by 100 matrix")
        matrix.append([int(x) for x in fields])
    edges: set[Edge] = set()
    for u in range(ORDER):
        if matrix[u][u]:
            raise ProjectionError("seed diagonal is not zero")
        for v in range(u + 1, ORDER):
            if matrix[u][v] != matrix[v][u]:
                raise ProjectionError("seed is not symmetric")
            if matrix[u][v]:
                edges.add((u, v))
    if len(edges) != EXPECTED_SEED_EDGES or FIXED_EDGE not in edges:
        raise ProjectionError("seed edge family mismatch")
    rows = edge_rows(edges)
    triangles = [
        (u, v, w)
        for u in range(ORDER)
        for v in range(u + 1, ORDER)
        if rows[u] >> v & 1
        for w in range(v + 1, ORDER)
        if rows[u] >> w & 1 and rows[v] >> w & 1
    ]
    if triangles != [EXPECTED_TRIANGLE]:
        raise ProjectionError("seed triangle family mismatch")
    return rows, {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": EXPECTED_SEED_SHA256,
        "vertices": ORDER,
        "edges": len(edges),
        "triangles": [list(t) for t in triangles],
    }


def branch1_base(seed_rows: Sequence[int]) -> tuple[list[int], list[Edge]]:
    edges = edge_set(seed_rows)
    edges.remove(FIXED_EDGE)
    ordered = sorted(edges)
    if len(ordered) != EXPECTED_BASE_EDGES:
        raise ProjectionError("fixed-base edge count mismatch")
    base = edge_rows(ordered)
    if any(
        base[u] >> v & 1 and base[u] >> w & 1 and base[v] >> w & 1
        for u in range(ORDER)
        for v in range(u + 1, ORDER)
        for w in range(v + 1, ORDER)
    ):
        raise ProjectionError("branch-1 fixed base is not triangle-free")
    return base, ordered


def independent_masks(
    rows: Sequence[int], candidate_mask: int, size: int
) -> list[int]:
    """Enumerate independent ``size``-sets by increasing-label DFS."""

    result: list[int] = []

    def visit(candidates: int, chosen: int, needed: int) -> None:
        if needed == 0:
            result.append(chosen)
            return
        if candidates.bit_count() < needed:
            return
        remaining = candidates
        while remaining.bit_count() >= needed:
            bit = remaining & -remaining
            remaining ^= bit
            vertex = bit.bit_length() - 1
            visit(remaining & ~rows[vertex], chosen | bit, needed - 1)

    visit(candidate_mask, 0, size)
    result.sort()
    if len(result) != len(set(result)):
        raise AssertionError("independent-set enumerator produced duplicates")
    return result


def fixed_base_i18_family(
    seed_rows: Sequence[int], base_rows: Sequence[int]
) -> tuple[list[int], dict[str, Any]]:
    """Rebuild the 65-vertex I16 family and lift it to fixed-base I18s.

    Completeness uses the separately checked premise ``alpha(H)<18``: removing
    only ``(97,99)`` means every newly created I18 contains both endpoints.
    The remaining vertices are exactly an I16 in their common non-neighbourhood.
    """

    all_vertices = (1 << ORDER) - 1
    u, v = FIXED_EDGE
    candidates = all_vertices & ~(
        seed_rows[u] | seed_rows[v] | (1 << u) | (1 << v)
    )
    if candidates.bit_count() != EXPECTED_CANDIDATE_VERTICES:
        raise ProjectionError("fixed-base candidate-vertex count mismatch")
    residual = independent_masks(seed_rows, candidates, TARGET_INDEPENDENCE - 2)
    lifted = [mask | (1 << u) | (1 << v) for mask in residual]
    if len(lifted) != EXPECTED_FIXED_BASE_I18:
        raise ProjectionError("fixed-base I18 count mismatch")
    if mask_digest(lifted) != EXPECTED_FIXED_BASE_I18_SHA256:
        raise ProjectionError("fixed-base I18 digest mismatch")
    for mask in lifted:
        if mask.bit_count() != TARGET_INDEPENDENCE:
            raise AssertionError("malformed lifted I18")
        for a, b in itertools.combinations(vertices(mask), 2):
            if base_rows[a] >> b & 1:
                raise AssertionError("lifted set is not independent in the base")
    return lifted, {
        "candidate_vertices": vertices(candidates),
        "candidate_vertices_count": candidates.bit_count(),
        "candidate_vertices_sha256": sha256_bytes(
            (" ".join(map(str, vertices(candidates))) + "\n").encode("ascii")
        ),
        "residual_I16_count": len(residual),
        "residual_I16_ordered_sha256": mask_digest(residual),
        "lifted_I18_count": len(lifted),
        "lifted_I18_ordered_sha256": mask_digest(lifted),
        "completeness_dependency": (
            "the independently checked frozen-seed fact alpha(H)<18; since "
            "B=H-(97,99), every I18 of B contains 97 and 99"
        ),
    }


def addition_pairs(seed_rows: Sequence[int]) -> list[Edge]:
    pairs = [
        (u, v)
        for u in range(ORDER)
        for v in range(u + 1, ORDER)
        if not (seed_rows[u] >> v & 1)
    ]
    if len(pairs) != EXPECTED_ADDITION_PAIRS:
        raise ProjectionError("original-nonedge count mismatch")
    return pairs


@dataclass(frozen=True)
class Projection:
    profile: str
    residual_deletions: int
    singleton_exclusions: bool
    base_rows: tuple[int, ...]
    base_edges: tuple[Edge, ...]
    additions: tuple[Edge, ...]
    fixed_masks: tuple[int, ...]
    dvars: Mapping[Edge, int]
    gvars: Mapping[Edge, int]
    counter_clauses: tuple[tuple[int, ...], ...]
    maximum_variable: int


def build_projection(seed_rows: Sequence[int], profile: str) -> Projection:
    if profile not in PROFILES:
        raise ProjectionError(f"unknown profile {profile!r}")
    residual_deletions, singleton_exclusions = PROFILES[profile]
    base_rows, base_edges = branch1_base(seed_rows)
    additions = addition_pairs(seed_rows)
    masks, _ = fixed_base_i18_family(seed_rows, base_rows)
    dvars = {edge: i + 1 for i, edge in enumerate(base_edges)}
    gvars = {
        edge: len(dvars) + i + 1 for i, edge in enumerate(additions)
    }
    counter = encode_equals(
        list(dvars.values()),
        residual_deletions,
        len(dvars) + len(gvars),
    )
    return Projection(
        profile=profile,
        residual_deletions=residual_deletions,
        singleton_exclusions=singleton_exclusions,
        base_rows=tuple(base_rows),
        base_edges=tuple(base_edges),
        additions=tuple(additions),
        fixed_masks=tuple(masks),
        dvars=dvars,
        gvars=gvars,
        counter_clauses=tuple(tuple(c) for c in counter.clauses),
        maximum_variable=counter.top_id,
    )


def eligibility_requirements(projection: Projection, edge: Edge) -> list[tuple[Edge, Edge]]:
    u, v = edge
    common = projection.base_rows[u] & projection.base_rows[v]
    requirements: list[tuple[Edge, Edge]] = []
    while common:
        bit = common & -common
        common ^= bit
        w = bit.bit_length() - 1
        requirements.append((normalized_edge(u, w), normalized_edge(v, w)))
    return requirements


def cover_clause(projection: Projection, mask: int) -> list[int]:
    clause = [
        projection.gvars[edge]
        for edge in itertools.combinations(vertices(mask), 2)
        if edge in projection.gvars
    ]
    if len(clause) != 152:
        raise AssertionError("a fixed-base I18 did not have 152 eligible pair variables")
    return clause


def iter_named_clauses(projection: Projection) -> Iterator[tuple[str, list[int]]]:
    for clause in projection.counter_clauses:
        yield "exact_residual_counter", list(clause)
    yield "vertex_98_degree_hit", [
        projection.dvars[e] for e in projection.base_edges if DEGREE_HIT_VERTEX in e
    ]
    if projection.singleton_exclusions:
        for edge in FORCED_RETAINED_EDGES:
            yield "singleton_deletion_exclusion", [-projection.dvars[edge]]
    for edge in projection.additions:
        gvar = projection.gvars[edge]
        for first, second in eligibility_requirements(projection, edge):
            yield "local_addition_eligibility", [
                -gvar,
                projection.dvars[first],
                projection.dvars[second],
            ]
    for mask in projection.fixed_masks:
        yield "fixed_base_I18_cover", cover_clause(projection, mask)


def formula_record(projection: Projection) -> dict[str, Any]:
    digest = hashlib.sha256()
    counts: Counter[str] = Counter()
    literals: Counter[str] = Counter()
    clause_count = 0
    literal_count = 0
    for name, clause in iter_named_clauses(projection):
        if not clause or any(lit == 0 or abs(lit) > projection.maximum_variable for lit in clause):
            raise AssertionError("invalid generated clause")
        raw = (" ".join(map(str, clause)) + " 0\n").encode("ascii")
        digest.update(raw)
        counts[name] += 1
        literals[name] += len(clause)
        clause_count += 1
        literal_count += len(clause)
    return {
        "profile": projection.profile,
        "residual_deletions": projection.residual_deletions,
        "singleton_exclusions_installed": projection.singleton_exclusions,
        "deletion_variables": len(projection.dvars),
        "local_eligibility_variables": len(projection.gvars),
        "auxiliary_variables": (
            projection.maximum_variable - len(projection.dvars) - len(projection.gvars)
        ),
        "maximum_variable": projection.maximum_variable,
        "clauses": clause_count,
        "literals": literal_count,
        "clause_count_by_family": dict(sorted(counts.items())),
        "literal_count_by_family": dict(sorted(literals.items())),
        "ordered_clause_body_sha256": digest.hexdigest(),
        "deletion_variable_order_sha256": edge_digest(projection.base_edges, "d"),
        "eligibility_variable_order_sha256": edge_digest(projection.additions, "g"),
    }


def locally_eligible_edges(
    projection: Projection, deleted: set[Edge]
) -> list[Edge]:
    eligible: list[Edge] = []
    for edge in projection.additions:
        if all(first in deleted or second in deleted for first, second in eligibility_requirements(projection, edge)):
            eligible.append(edge)
    return eligible


def validate_deletion_witness(
    projection: Projection, deleted_edges: Iterable[Edge]
) -> dict[str, Any]:
    deleted = {normalized_edge(*edge) for edge in deleted_edges}
    if len(deleted) != projection.residual_deletions or not deleted <= set(projection.base_edges):
        raise ProjectionError("witness is not an exact residual deletion support")
    if not any(DEGREE_HIT_VERTEX in edge for edge in deleted):
        raise ProjectionError("witness does not hit the degree-18 vertex 98")
    if projection.singleton_exclusions and deleted & set(FORCED_RETAINED_EDGES):
        raise ProjectionError("witness violates a singleton deletion exclusion")
    eligible = locally_eligible_edges(projection, deleted)
    eligible_set = set(eligible)
    uncovered: list[int] = []
    for mask in projection.fixed_masks:
        if not any(edge in eligible_set for edge in itertools.combinations(vertices(mask), 2)):
            uncovered.append(mask)
    if uncovered:
        raise ProjectionError(
            f"witness leaves {len(uncovered)} fixed-base I18 sets uncovered"
        )
    return {
        "status": "EXPLICIT_DELETION_SUPPORT_REPLAY_VERIFIED",
        "deleted_edges": [list(e) for e in sorted(deleted)],
        "deleted_edges_sha256": edge_digest(sorted(deleted), "deleted"),
        "locally_eligible_additions": len(eligible),
        "locally_eligible_additions_sha256": edge_digest(eligible, "eligible"),
        "fixed_base_I18_sets_checked": len(projection.fixed_masks),
        "uncovered_fixed_base_I18_sets": 0,
    }


def emit_dimacs(path: Path, projection: Projection, record: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(handle, "w", encoding="ascii", newline="\n") as stream:
            stream.write(f"p cnf {projection.maximum_variable} {record['clauses']}\n")
            for _, clause in iter_named_clauses(projection):
                stream.write(" ".join(map(str, clause)) + " 0\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def solve_projection(
    projection: Projection, solver_name: str, wall_seconds: float
) -> dict[str, Any]:
    """Run one bounded discovery solve; UNSAT is never promoted without DRAT."""

    if not (0.0 < wall_seconds <= 300.0):
        raise ProjectionError("solver wall limit must lie in (0,300] seconds")
    if solver_name.startswith(("cadical", "kissat", "lingeling", "cryptosat")):
        raise ProjectionError(
            "this PySAT backend does not provide the interrupt contract used "
            "here; emit DIMACS and place the external process under a hard wall"
        )
    try:
        from pysat.solvers import Solver
    except ImportError as error:  # pragma: no cover - optional search dependency
        raise ProjectionError("PySAT is required only for --solve") from error
    started = time.perf_counter()
    with Solver(name=solver_name) as solver:
        for _, clause in iter_named_clauses(projection):
            solver.add_clause(clause)
        installation_seconds = time.perf_counter() - started
        fired = threading.Event()

        def interrupt() -> None:
            fired.set()
            solver.interrupt()

        timer = threading.Timer(wall_seconds, interrupt)
        timer.daemon = True
        timer.start()
        solve_started = time.perf_counter()
        try:
            result = solver.solve_limited(expect_interrupt=True)
        finally:
            solve_seconds = time.perf_counter() - solve_started
            timer.cancel()
            timer.join()
            solver.clear_interrupt()
        diagnostic: dict[str, Any] = {
            "evidence_class": "TRUSTED_CODE_DIAGNOSTIC",
            "solver": solver_name,
            "wall_limit_seconds": wall_seconds,
            "formula_installation_seconds": installation_seconds,
            "solve_seconds": solve_seconds,
            "timer_fired": fired.is_set(),
            "solver_statistics": solver.accum_stats(),
        }
        if result is True:
            diagnostic["status"] = "SAT_MODEL_FOUND"
            positive = {literal for literal in solver.get_model() if literal > 0}
            deleted = [
                edge for edge, variable in projection.dvars.items() if variable in positive
            ]
            diagnostic["model_deletion_support"] = [list(e) for e in deleted]
            diagnostic["replay"] = validate_deletion_witness(projection, deleted)
        elif result is False:
            diagnostic["status"] = "UNSAT_ENDPOINT_NOT_PROOF_CHECKED"
            diagnostic["claim_boundary"] = (
                "No UNSAT claim: this invocation emitted no independently replayed DRAT proof."
            )
        else:
            diagnostic["status"] = "UNKNOWN_WALL_OR_BACKEND_LIMIT"
        return diagnostic


def build_record(seed_path: Path, profile: str) -> tuple[Projection, dict[str, Any]]:
    seed_rows, seed_record = strict_seed(seed_path)
    projection = build_projection(seed_rows, profile)
    _, family = fixed_base_i18_family(seed_rows, projection.base_rows)
    wedge_histogram = Counter(
        len(eligibility_requirements(projection, edge))
        for edge in projection.additions
    )
    record = {
        "schema": SCHEMA,
        "input": seed_record,
        "fixed_edge": list(FIXED_EDGE),
        "fixed_edge_cannot_be_readded": True,
        "fixed_base": {
            "edges": len(projection.base_edges),
            "edge_order_sha256": edge_digest(projection.base_edges, "base"),
            "degree_distribution": {
                str(k): v
                for k, v in sorted(Counter(r.bit_count() for r in projection.base_rows).items())
            },
            "vertex_98_degree": projection.base_rows[98].bit_count(),
        },
        "fixed_base_family": family,
        "local_eligibility": {
            "original_nonedge_pairs": len(projection.additions),
            "common_neighbor_wedge_histogram": {
                str(k): v for k, v in sorted(wedge_histogram.items())
            },
            "wedge_clauses": sum(k * v for k, v in wedge_histogram.items()),
        },
        "formula": formula_record(projection),
        "logical_status": "PROVABLE_AS_A_NECESSARY_RELAXATION",
        "necessity_dependencies": [
            "exact residual deletion count",
            "degree at most 17 in every triangle-free graph with alpha<18",
            "triangle-freeness of every actually added original nonedge",
            "every fixed-base I18 must receive an added pair",
            "the four singleton proof pairs, exact-seven profile only",
        ],
        "omitted_constraints": [
            "triangles using two or three added edges",
            "degree caps other than the forced vertex-98 deletion hit",
            "independent 18-sets created by residual deletions",
            "a single globally consistent final addition set beyond local eligibility",
        ],
        "claim_boundary": {
            "sat_implies_repair": False,
            "unchecked_unsat_implies_no_repair": False,
            "global_R_3_18_bound_improvement": False,
        },
    }
    record["record_sha256"] = canonical_sha256(record)
    return projection, record


def atomic_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            json.dump(payload, stream, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def main() -> None:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--seed", default=here / "certificates" / "r3_18_n100_nearmiss.txt", type=Path
    )
    parser.add_argument("--profile", choices=sorted(PROFILES), required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--emit-dimacs", type=Path)
    parser.add_argument("--solve", action="store_true")
    parser.add_argument("--solver", default="glucose42")
    parser.add_argument("--wall-seconds", type=float, default=60.0)
    args = parser.parse_args()

    projection, record = build_record(args.seed, args.profile)
    if args.emit_dimacs is not None:
        emit_dimacs(args.emit_dimacs, projection, record["formula"])
        record["dimacs"] = {
            "path": args.emit_dimacs.name,
            "bytes": args.emit_dimacs.stat().st_size,
            "sha256": sha256_bytes(args.emit_dimacs.read_bytes()),
        }
    if args.solve:
        record["bounded_solver_diagnostic"] = solve_projection(
            projection, args.solver, args.wall_seconds
        )
    record.pop("record_sha256", None)
    record["record_sha256"] = canonical_sha256(record)
    if args.output is None:
        print(json.dumps(record, indent=2, sort_keys=True))
    else:
        atomic_json(args.output, record)


if __name__ == "__main__":
    main()
