#!/usr/bin/env python3
"""Bounded fail-closed CEGAR engine for domination witnesses.

The engine is deliberately solver-agnostic.  A backend returns one of SAT,
UNSAT, or UNKNOWN together with a complete graph for SAT.  Every SAT graph is
audited and separated by the degree--distance-two witness generator.  The
fixed production limits are:

* at most 16 returned SAT models;
* at most 65,536 novel domination masks;
* at most 4,096 degree-16 masks from one model;
* a 900-second aggregate wall;
* after eight models, stop if fewer than two novel masks were learned or if
  fewer than 25 percent of emitted structural witnesses were novel.

No endpoint is silently promoted.  A SAT model with no domination witness is
only SAT for this structural separator, not a Ramsey witness.  Every solver
UNSAT remains ``UNSAT_UNCHECKED`` until a separate authenticated promotion
record replays the proof. Every limit, backend error, malformed model, stale
model, or incomplete degree-16 scan is UNKNOWN and learns no theorem.

The command-line interface replays scripted backend events for deterministic
testing and integration.  It does not launch a SAT solver by itself.  A live
solver adapter can call :func:`run_bounded_cegar` while preserving the same
state machine and limits.
"""

from __future__ import annotations

import argparse
import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Protocol, Sequence

try:
    from .check_r3_18_budget7_branch1_domination_witnesses import (
        AuditError,
        DominationWitness,
        EXPECTED_APLUS_FILE_SHA256,
        EXPECTED_APLUS_MASKS,
        EXPECTED_HISTORY_FILE_SHA256,
        EXPECTED_HISTORY_MASKS,
        EXPECTED_UNIVERSAL_FILE_SHA256,
        EXPECTED_UNIVERSAL_MASKS,
        domination_witnesses,
        fixed_base_contains,
        is_independent,
        lexicographic_pairs,
        load_mask_family_with_identity,
        read_seed_matrix,
        strict_json,
        validate_rows,
    )
except ImportError:  # pragma: no cover - direct script execution
    from check_r3_18_budget7_branch1_domination_witnesses import (
        AuditError,
        DominationWitness,
        EXPECTED_APLUS_FILE_SHA256,
        EXPECTED_APLUS_MASKS,
        EXPECTED_HISTORY_FILE_SHA256,
        EXPECTED_HISTORY_MASKS,
        EXPECTED_UNIVERSAL_FILE_SHA256,
        EXPECTED_UNIVERSAL_MASKS,
        domination_witnesses,
        fixed_base_contains,
        is_independent,
        lexicographic_pairs,
        load_mask_family_with_identity,
        read_seed_matrix,
        strict_json,
        validate_rows,
    )


SCHEMA = "ramsey-r3-18-branch1-domination-cegar-v1"
EVENT_SCHEMA = "ramsey-r3-18-domination-scripted-events-v1"

MAX_MODELS = 16
MAX_MASKS = 65_536
D16_PER_MODEL_CAP = 4_096
WALL_SECONDS = 900.0
EARLY_STOP_AFTER_MODELS = 8
EARLY_STOP_MIN_NOVEL = 2
EARLY_STOP_MIN_NOVEL_RATIO = 0.25

SAT = "SAT"
UNSAT = "UNSAT"
UNKNOWN = "UNKNOWN"

ENDPOINT_SAT_STRUCTURAL_CLOSED = "SAT_DOMINATION_SEPARATOR_CLOSED_MODEL"
ENDPOINT_UNSAT_UNCHECKED = "UNSAT_UNCHECKED_DOMINATION_FORMULA"
ENDPOINT_UNKNOWN_BACKEND = "UNKNOWN_BACKEND"
ENDPOINT_UNKNOWN_INVALID_MODEL = "UNKNOWN_INVALID_MODEL"
ENDPOINT_UNKNOWN_STALE_MODEL = "UNKNOWN_STALE_MODEL"
ENDPOINT_UNKNOWN_WALL = "UNKNOWN_WALL_LIMIT"
ENDPOINT_UNKNOWN_MODEL_CAP = "UNKNOWN_MODEL_CAP"
ENDPOINT_UNKNOWN_MASK_CAP = "UNKNOWN_MASK_CAP"
ENDPOINT_UNKNOWN_D16_CAP = "UNKNOWN_D16_WITNESS_CAP"
ENDPOINT_UNKNOWN_NO_NOVEL = "UNKNOWN_NO_NOVEL_STRUCTURAL_MASK"
ENDPOINT_UNKNOWN_LOW_PRODUCTIVITY = "UNKNOWN_LOW_PRODUCTIVITY_STOP"


@dataclass(frozen=True)
class SolveEvent:
    """One fail-closed backend response."""

    status: str
    rows: tuple[int, ...] | None = None
    proof_checked: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


class SolverBackend(Protocol):
    """Minimal live or scripted backend contract."""

    def solve(
        self, added_clauses: Sequence[tuple[int, ...]], remaining_seconds: float
    ) -> SolveEvent:
        ...


@dataclass
class CegarLedger:
    models_seen: int = 0
    candidate_masks_seen: int = 0
    novel_masks_added: int = 0
    degree17_candidates: int = 0
    degree16_candidates: int = 0
    degree16_truncated_models: int = 0
    learned_masks: set[int] = field(default_factory=set)
    added_clauses: list[tuple[int, ...]] = field(default_factory=list)
    iterations: list[dict[str, Any]] = field(default_factory=list)


def edge_variables(order: int) -> dict[tuple[int, int], int]:
    return {edge: index for index, edge in enumerate(lexicographic_pairs(order), 1)}


def hitting_clause(mask: int, *, order: int) -> tuple[int, ...]:
    vertices = [vertex for vertex in range(order) if mask >> vertex & 1]
    if len(vertices) != 18:
        raise AuditError("domination mask is not an 18-set")
    variables = edge_variables(order)
    return tuple(
        variables[(u, v)]
        for first, u in enumerate(vertices)
        for v in vertices[first + 1 :]
    )


def _endpoint(
    status: str,
    ledger: CegarLedger,
    *,
    elapsed: float,
    exact_seven_repair_exists: bool | None = None,
    detail: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "schema": SCHEMA,
        "status": status,
        "claim_boundary": (
            "SAT means only that one model has no witness in this bounded "
            "domination family. UNSAT is theorem evidence only when its exact "
            "CNF and proof are independently authenticated. UNKNOWN learns "
            "nothing and cannot be resumed by inference."
        ),
        "exact_seven_repair_exists": exact_seven_repair_exists,
        "limits": {
            "max_models": MAX_MODELS,
            "max_masks": MAX_MASKS,
            "degree16_masks_per_model": D16_PER_MODEL_CAP,
            "wall_seconds": WALL_SECONDS,
            "early_stop_after_models": EARLY_STOP_AFTER_MODELS,
            "early_stop_min_novel_masks": EARLY_STOP_MIN_NOVEL,
            "early_stop_min_novel_ratio": EARLY_STOP_MIN_NOVEL_RATIO,
        },
        "telemetry": {
            "elapsed_seconds": elapsed,
            "models_seen": ledger.models_seen,
            "candidate_masks_seen": ledger.candidate_masks_seen,
            "novel_masks_added": ledger.novel_masks_added,
            "degree17_candidates": ledger.degree17_candidates,
            "degree16_candidates": ledger.degree16_candidates,
            "degree16_truncated_models": ledger.degree16_truncated_models,
            "iterations": ledger.iterations,
        },
        "detail": detail or {},
    }


def _validate_fresh_model(rows: Sequence[int], ledger: CegarLedger) -> None:
    validate_rows(rows)
    for mask in ledger.learned_masks:
        if is_independent(rows, mask):
            raise AuditError("backend returned a model violating a learned clause")


def run_bounded_cegar(
    backend: SolverBackend,
    *,
    excluded_masks: set[int] | None = None,
    exclusion_predicate: Callable[[int], bool] | None = None,
    clock: Callable[[], float] = time.monotonic,
    witness_generator: Callable[
        ..., tuple[list[DominationWitness], dict[str, Any]]
    ] = domination_witnesses,
) -> dict[str, Any]:
    """Run the fixed bounded state machine without weakening any stop rule."""

    frozen_exclusions = set(excluded_masks or ())
    ledger = CegarLedger()
    start = clock()

    while True:
        elapsed = clock() - start
        if elapsed >= WALL_SECONDS:
            return _endpoint(ENDPOINT_UNKNOWN_WALL, ledger, elapsed=elapsed)
        if ledger.models_seen >= MAX_MODELS:
            return _endpoint(ENDPOINT_UNKNOWN_MODEL_CAP, ledger, elapsed=elapsed)
        if ledger.novel_masks_added >= MAX_MASKS:
            return _endpoint(ENDPOINT_UNKNOWN_MASK_CAP, ledger, elapsed=elapsed)

        try:
            event = backend.solve(
                tuple(ledger.added_clauses), max(0.0, WALL_SECONDS - elapsed)
            )
        except Exception as error:  # fail closed across backend boundaries
            return _endpoint(
                ENDPOINT_UNKNOWN_BACKEND,
                ledger,
                elapsed=clock() - start,
                detail={"error": type(error).__name__},
            )

        elapsed = clock() - start
        if elapsed >= WALL_SECONDS:
            return _endpoint(ENDPOINT_UNKNOWN_WALL, ledger, elapsed=elapsed)
        if event.status == UNKNOWN:
            return _endpoint(
                ENDPOINT_UNKNOWN_BACKEND,
                ledger,
                elapsed=elapsed,
                detail={"backend": event.metadata},
            )
        if event.status == UNSAT:
            return _endpoint(
                ENDPOINT_UNSAT_UNCHECKED,
                ledger,
                elapsed=elapsed,
                detail={
                    "backend": event.metadata,
                    "backend_claimed_proof_checked": event.proof_checked,
                    "promotion_required": (
                        "The CEGAR engine never self-promotes solver UNSAT. "
                        "Authenticate and replay the exact final CNF/proof in "
                        "a separate promotion record."
                    ),
                },
            )
        if event.status != SAT or event.rows is None:
            return _endpoint(
                ENDPOINT_UNKNOWN_BACKEND,
                ledger,
                elapsed=elapsed,
                detail={"error": "invalid backend status or missing SAT rows"},
            )

        try:
            _validate_fresh_model(event.rows, ledger)
            witnesses, generation = witness_generator(
                event.rows, d16_limit=D16_PER_MODEL_CAP
            )
        except (AuditError, ValueError, TypeError) as error:
            return _endpoint(
                ENDPOINT_UNKNOWN_INVALID_MODEL,
                ledger,
                elapsed=clock() - start,
                detail={"error": str(error)},
            )

        ledger.models_seen += 1
        candidates = {witness.mask: witness for witness in witnesses}
        ledger.candidate_masks_seen += len(candidates)
        ledger.degree17_candidates += generation.get("degree17_candidates", 0)
        ledger.degree16_candidates += generation.get("degree16_candidates_emitted", 0)
        truncated = bool(generation.get("degree16_truncated"))
        if truncated:
            ledger.degree16_truncated_models += 1

        old = frozen_exclusions | ledger.learned_masks
        novel = [
            candidates[mask]
            for mask in sorted(candidates)
            if mask not in old
            and not (exclusion_predicate(mask) if exclusion_predicate else False)
        ]
        iteration = {
            "model_index": ledger.models_seen,
            "candidate_masks": len(candidates),
            "novel_masks": len(novel),
            "degree17_candidates": generation.get("degree17_candidates", 0),
            "degree16_candidates_emitted": generation.get(
                "degree16_candidates_emitted", 0
            ),
            "degree16_truncated": truncated,
        }
        ledger.iterations.append(iteration)

        if not candidates:
            if truncated:
                return _endpoint(ENDPOINT_UNKNOWN_D16_CAP, ledger, elapsed=clock() - start)
            return _endpoint(
                ENDPOINT_SAT_STRUCTURAL_CLOSED,
                ledger,
                elapsed=clock() - start,
                exact_seven_repair_exists=None,
                detail={"backend": event.metadata},
            )
        if not novel:
            return _endpoint(
                ENDPOINT_UNKNOWN_NO_NOVEL,
                ledger,
                elapsed=clock() - start,
                detail={"degree16_truncated": truncated},
            )
        if ledger.novel_masks_added + len(novel) > MAX_MASKS:
            return _endpoint(
                ENDPOINT_UNKNOWN_MASK_CAP,
                ledger,
                elapsed=clock() - start,
                detail={"rejected_batch_masks": len(novel)},
            )

        order = len(event.rows)
        try:
            clauses = [hitting_clause(witness.mask, order=order) for witness in novel]
        except AuditError as error:
            return _endpoint(
                ENDPOINT_UNKNOWN_INVALID_MODEL,
                ledger,
                elapsed=clock() - start,
                detail={"error": str(error)},
            )
        ledger.learned_masks.update(witness.mask for witness in novel)
        ledger.added_clauses.extend(clauses)
        ledger.novel_masks_added += len(novel)

        if ledger.models_seen >= EARLY_STOP_AFTER_MODELS:
            ratio = (
                ledger.novel_masks_added / ledger.candidate_masks_seen
                if ledger.candidate_masks_seen
                else 0.0
            )
            if (
                ledger.novel_masks_added < EARLY_STOP_MIN_NOVEL
                or ratio < EARLY_STOP_MIN_NOVEL_RATIO
            ):
                return _endpoint(
                    ENDPOINT_UNKNOWN_LOW_PRODUCTIVITY,
                    ledger,
                    elapsed=clock() - start,
                    detail={"novel_ratio": ratio},
                )
        if truncated and ledger.novel_masks_added >= MAX_MASKS:
            return _endpoint(ENDPOINT_UNKNOWN_D16_CAP, ledger, elapsed=clock() - start)


class ScriptedBackend:
    """Deterministic event source for integration tests and dry runs."""

    def __init__(self, events: Sequence[SolveEvent]) -> None:
        self.events = list(events)
        self.index = 0

    def solve(
        self, added_clauses: Sequence[tuple[int, ...]], remaining_seconds: float
    ) -> SolveEvent:
        del added_clauses, remaining_seconds
        if self.index >= len(self.events):
            return SolveEvent(UNKNOWN, metadata={"reason": "script exhausted"})
        event = self.events[self.index]
        self.index += 1
        return event


def _scripted_events(path: Path) -> list[SolveEvent]:
    payload = strict_json(path)
    if not isinstance(payload, dict) or payload.get("schema") != EVENT_SCHEMA:
        raise AuditError("scripted-event schema mismatch")
    raw_events = payload.get("events")
    if not isinstance(raw_events, list) or not raw_events:
        raise AuditError("scripted event list is empty")
    result: list[SolveEvent] = []
    for raw in raw_events:
        if not isinstance(raw, dict) or raw.get("status") not in (SAT, UNSAT, UNKNOWN):
            raise AuditError("invalid scripted event")
        rows_raw = raw.get("rows_hex")
        rows: tuple[int, ...] | None = None
        if rows_raw is not None:
            if not isinstance(rows_raw, list) or any(
                not isinstance(item, str) for item in rows_raw
            ):
                raise AuditError("invalid scripted rows")
            try:
                rows = tuple(int(item, 16) for item in rows_raw)
            except ValueError as error:
                raise AuditError("invalid hexadecimal scripted row") from error
        metadata = raw.get("metadata", {})
        if not isinstance(metadata, dict):
            raise AuditError("scripted metadata is not an object")
        result.append(
            SolveEvent(
                raw["status"],
                rows=rows,
                proof_checked=raw.get("proof_checked") is True,
                metadata=metadata,
            )
        )
    return result


def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scripted-events", type=Path, required=True)
    parser.add_argument(
        "--universal",
        type=Path,
        default=here / "r3_18_budget6_branch_0_universal_union.cuts.json",
    )
    parser.add_argument(
        "--history",
        type=Path,
        default=here / "r3_18_budget7_branch1_cegar_history_exclusion.json",
    )
    parser.add_argument(
        "--aplus",
        type=Path,
        default=here / "r3_18_budget7_branch1_cegar_Aplus_batch.json",
    )
    parser.add_argument(
        "--matrix",
        type=Path,
        default=here / "certificates" / "r3_18_n100_nearmiss.txt",
    )
    args = parser.parse_args(argv)
    try:
        universal, _ = load_mask_family_with_identity(
            args.universal.resolve(),
            expected_sha256=EXPECTED_UNIVERSAL_FILE_SHA256,
            expected_count=EXPECTED_UNIVERSAL_MASKS,
        )
        history, _ = load_mask_family_with_identity(
            args.history.resolve(),
            expected_sha256=EXPECTED_HISTORY_FILE_SHA256,
            expected_count=EXPECTED_HISTORY_MASKS,
        )
        aplus, _ = load_mask_family_with_identity(
            args.aplus.resolve(),
            expected_sha256=EXPECTED_APLUS_FILE_SHA256,
            expected_count=EXPECTED_APLUS_MASKS,
        )
        exclusions = universal | history | aplus
        seed_rows, _ = read_seed_matrix(args.matrix.resolve())
        backend = ScriptedBackend(_scripted_events(args.scripted_events.resolve()))
        payload = run_bounded_cegar(
            backend,
            excluded_masks=exclusions,
            exclusion_predicate=lambda mask: fixed_base_contains(seed_rows, mask),
        )
    except (AuditError, OSError) as error:
        payload = {
            "schema": SCHEMA,
            "status": ENDPOINT_UNKNOWN_BACKEND,
            "error": str(error),
            "exact_seven_repair_exists": None,
        }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["status"] == ENDPOINT_SAT_STRUCTURAL_CLOSED else 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
