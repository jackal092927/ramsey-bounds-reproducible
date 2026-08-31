"""Asset-light regressions for the domination witness checker and CEGAR engine."""

from __future__ import annotations

import gzip
import hashlib
import itertools
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from .check_r3_18_budget7_branch1_domination_witnesses import (
    AuditError,
    DominationWitness,
    domination_witnesses,
    is_independent,
    load_mask_family,
    load_mask_family_with_identity,
    parse_complete_model_bytes,
)
from .r3_18_budget7_branch1_domination_cegar import (
    ENDPOINT_SAT_STRUCTURAL_CLOSED,
    ENDPOINT_UNKNOWN_BACKEND,
    ENDPOINT_UNKNOWN_D16_CAP,
    ENDPOINT_UNKNOWN_LOW_PRODUCTIVITY,
    ENDPOINT_UNKNOWN_MASK_CAP,
    ENDPOINT_UNKNOWN_MODEL_CAP,
    ENDPOINT_UNKNOWN_NO_NOVEL,
    ENDPOINT_UNKNOWN_WALL,
    ENDPOINT_UNSAT_UNCHECKED,
    SAT,
    UNKNOWN,
    UNSAT,
    ScriptedBackend,
    SolveEvent,
    hitting_clause,
    run_bounded_cegar,
)


def _rows(order: int, edges: list[tuple[int, int]]) -> tuple[int, ...]:
    rows = [0] * order
    for u, v in edges:
        rows[u] |= 1 << v
        rows[v] |= 1 << u
    return tuple(rows)


def _star(degree: int, order: int = 19) -> tuple[int, ...]:
    return _rows(order, [(0, vertex) for vertex in range(1, degree + 1)])


class DominationWitnessTests(unittest.TestCase):
    def test_degree17_witness_is_exact_and_independent(self) -> None:
        rows = _star(17)
        witnesses, info = domination_witnesses(rows)
        self.assertEqual(len(witnesses), 1)
        witness = witnesses[0]
        self.assertEqual(witness.kind, "degree17")
        self.assertEqual(witness.center, 0)
        self.assertEqual(witness.z_vertices, (18,))
        self.assertEqual(witness.mask.bit_count(), 18)
        self.assertTrue(is_independent(rows, witness.mask))
        self.assertEqual(info["degree17_candidates"], 1)
        self.assertEqual(info["degree16_candidates_total"], 0)

    def test_degree16_witness_and_bound_are_fail_closed(self) -> None:
        rows = _star(16)
        witnesses, info = domination_witnesses(rows)
        self.assertEqual(len(witnesses), 1)
        self.assertEqual(witnesses[0].kind, "degree16")
        self.assertEqual(witnesses[0].z_vertices, (17, 18))
        self.assertEqual(info["degree16_candidates_total"], 1)
        self.assertFalse(info["degree16_truncated"])

        bounded, bounded_info = domination_witnesses(rows, d16_limit=0)
        self.assertEqual(bounded, [])
        self.assertTrue(bounded_info["degree16_truncated"])
        self.assertEqual(bounded_info["degree16_candidates_total"], 1)

    def test_triangle_and_malformed_rows_are_rejected(self) -> None:
        with self.assertRaisesRegex(AuditError, "triangle"):
            domination_witnesses(_rows(19, [(0, 1), (1, 2), (0, 2)]))
        malformed = list(_rows(19, []))
        malformed[0] |= 1 << 1
        with self.assertRaisesRegex(AuditError, "symmetric"):
            domination_witnesses(malformed)

    def test_complete_model_parser_requires_every_literal_once(self) -> None:
        raw = b"s SATISFIABLE\nv 1 -2 3 0\n"
        assignment, info = parse_complete_model_bytes(gzip.compress(raw), 3)
        self.assertEqual(assignment, [None, True, False, True])
        self.assertEqual(info["assignment_literals"], 3)
        with self.assertRaisesRegex(AuditError, "more than once"):
            parse_complete_model_bytes(
                gzip.compress(b"s SATISFIABLE\nv 1 -1 2 3 0\n"), 3
            )
        with self.assertRaisesRegex(AuditError, "does not assign every"):
            parse_complete_model_bytes(gzip.compress(b"s SATISFIABLE\nv 1 0\n"), 3)

    def test_hitting_clause_has_all_153_positive_edge_variables(self) -> None:
        mask = sum(1 << vertex for vertex in range(18))
        clause = hitting_clause(mask, order=19)
        self.assertEqual(len(clause), 153)
        self.assertEqual(len(set(clause)), 153)
        self.assertTrue(all(literal > 0 for literal in clause))

    def test_overlap_family_accepts_source_order_but_rejects_duplicates(self) -> None:
        with tempfile.TemporaryDirectory(prefix="domination-family-test-") as root:
            path = Path(root) / "family.json"
            path.write_text(
                json.dumps({"masks": ["0" * 24 + "2", "0" * 24 + "1"]}),
                encoding="utf-8",
            )
            self.assertEqual(load_mask_family(path), {1, 2})
            path.write_text(
                json.dumps({"masks": ["0" * 24 + "1", "0" * 24 + "1"]}),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(AuditError, "duplicate mask"):
                load_mask_family(path)

    def test_production_family_identity_rejects_same_count_tamper_and_symlink(self) -> None:
        with tempfile.TemporaryDirectory(prefix="domination-tamper-test-") as root:
            directory = Path(root)
            path = directory / "family.json"
            original = json.dumps(
                {"masks": ["0" * 24 + "1", "0" * 24 + "2"]},
                separators=(",", ":"),
            ).encode("utf-8")
            path.write_bytes(original)
            expected_hash = hashlib.sha256(original).hexdigest()
            masks, identity = load_mask_family_with_identity(
                path, expected_sha256=expected_hash, expected_count=2
            )
            self.assertEqual(masks, {1, 2})
            self.assertEqual(identity["sha256"], expected_hash)
            self.assertEqual(identity["masks"], 2)

            replacement = json.dumps(
                {"masks": ["0" * 24 + "3", "0" * 24 + "4"]},
                separators=(",", ":"),
            ).encode("utf-8")
            path.write_bytes(replacement)
            with self.assertRaisesRegex(AuditError, "SHA-256 mismatch"):
                load_mask_family_with_identity(
                    path, expected_sha256=expected_hash, expected_count=2
                )

            path.write_text(
                '{"masks":["0000000000000000000000001"],'
                '"masks":["0000000000000000000000002"]}',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(AuditError, "duplicate JSON key"):
                load_mask_family(path)

            target = directory / "target.json"
            target.write_bytes(original)
            link = directory / "link.json"
            link.symlink_to(target)
            with self.assertRaisesRegex(AuditError, "symlink"):
                load_mask_family(link)


class DominationCegarTests(unittest.TestCase):
    def test_sat_means_only_structural_separator_closed(self) -> None:
        backend = ScriptedBackend([SolveEvent(SAT, rows=_rows(19, []))])
        result = run_bounded_cegar(backend, clock=lambda: 0.0)
        self.assertEqual(result["status"], ENDPOINT_SAT_STRUCTURAL_CLOSED)
        self.assertIsNone(result["exact_seven_repair_exists"])
        self.assertEqual(result["telemetry"]["models_seen"], 1)

    def test_solver_unsat_never_self_promotes_from_backend_boolean(self) -> None:
        claimed_checked = run_bounded_cegar(
            ScriptedBackend([SolveEvent(UNSAT, proof_checked=True)]),
            clock=lambda: 0.0,
        )
        unchecked = run_bounded_cegar(
            ScriptedBackend([SolveEvent(UNSAT, proof_checked=False)]),
            clock=lambda: 0.0,
        )
        self.assertEqual(claimed_checked["status"], ENDPOINT_UNSAT_UNCHECKED)
        self.assertEqual(unchecked["status"], ENDPOINT_UNSAT_UNCHECKED)
        self.assertTrue(
            claimed_checked["detail"]["backend_claimed_proof_checked"]
        )
        self.assertIn("never self-promotes", claimed_checked["detail"]["promotion_required"])
        self.assertIsNone(unchecked["exact_seven_repair_exists"])

    def test_unknown_backend_is_fail_closed(self) -> None:
        result = run_bounded_cegar(
            ScriptedBackend([SolveEvent(UNKNOWN, metadata={"reason": "timeout"})]),
            clock=lambda: 0.0,
        )
        self.assertEqual(result["status"], ENDPOINT_UNKNOWN_BACKEND)
        self.assertIsNone(result["exact_seven_repair_exists"])

    def test_fixed_family_predicate_is_part_of_no_repeat_filter(self) -> None:
        result = run_bounded_cegar(
            ScriptedBackend([SolveEvent(SAT, rows=_star(17))]),
            exclusion_predicate=lambda mask: mask.bit_count() == 18,
            clock=lambda: 0.0,
        )
        self.assertEqual(result["status"], ENDPOINT_UNKNOWN_NO_NOVEL)
        self.assertEqual(result["telemetry"]["novel_masks_added"], 0)

    def test_mask_and_model_caps_stop_without_an_extra_solve(self) -> None:
        event = SolveEvent(SAT, rows=_star(17))
        with mock.patch(
            "routes.finite.r3_18_budget7_branch1_domination_cegar.MAX_MASKS", 1
        ):
            mask_result = run_bounded_cegar(
                ScriptedBackend([event]), clock=lambda: 0.0
            )
        self.assertEqual(mask_result["status"], ENDPOINT_UNKNOWN_MASK_CAP)
        self.assertEqual(mask_result["telemetry"]["novel_masks_added"], 1)

        with mock.patch(
            "routes.finite.r3_18_budget7_branch1_domination_cegar.MAX_MODELS", 1
        ):
            model_result = run_bounded_cegar(
                ScriptedBackend([event]), clock=lambda: 0.0
            )
        self.assertEqual(model_result["status"], ENDPOINT_UNKNOWN_MODEL_CAP)
        self.assertEqual(model_result["telemetry"]["models_seen"], 1)

    def test_degree16_truncation_never_becomes_sat(self) -> None:
        def truncated_generator(rows, *, d16_limit):
            del rows, d16_limit
            return [], {
                "degree17_candidates": 0,
                "degree16_candidates_emitted": 0,
                "degree16_truncated": True,
            }

        result = run_bounded_cegar(
            ScriptedBackend([SolveEvent(SAT, rows=_rows(19, []))]),
            clock=lambda: 0.0,
            witness_generator=truncated_generator,
        )
        self.assertEqual(result["status"], ENDPOINT_UNKNOWN_D16_CAP)

    def test_wall_is_aggregate_and_fail_closed(self) -> None:
        moments = iter([0.0, 0.0, 901.0])
        result = run_bounded_cegar(
            ScriptedBackend([SolveEvent(SAT, rows=_rows(19, []))]),
            clock=lambda: next(moments),
        )
        self.assertEqual(result["status"], ENDPOINT_UNKNOWN_WALL)
        self.assertEqual(result["telemetry"]["models_seen"], 0)

    def test_low_novelty_ratio_stops_at_predeclared_checkpoint(self) -> None:
        order = 30
        all_masks = [
            sum(1 << vertex for vertex in choice)
            for choice in itertools.islice(itertools.combinations(range(order), 18), 40)
        ]
        first_novel = all_masks[0]
        first_old = all_masks[1:10]
        second_candidates = [
            sum(1 << vertex for vertex in choice)
            for choice in itertools.islice(
                itertools.combinations(range(2, order), 18), 10
            )
        ]
        self.assertEqual(len(second_candidates), 10)
        second_novel = second_candidates[0]
        exclusions = set(first_old) | set(second_candidates[1:])

        calls = iter(
            [
                [first_novel, *first_old],
                [second_novel, *second_candidates[1:]],
            ]
        )

        def generated(rows, *, d16_limit):
            del rows, d16_limit
            masks = next(calls)
            return [
                DominationWitness(mask, "degree17", 0, (29,)) for mask in masks
            ], {
                "degree17_candidates": len(masks),
                "degree16_candidates_emitted": 0,
                "degree16_truncated": False,
            }

        first_rows = _rows(order, [])
        second_rows = _rows(order, [(0, 1)])
        backend = ScriptedBackend(
            [SolveEvent(SAT, rows=first_rows), SolveEvent(SAT, rows=second_rows)]
        )
        with mock.patch(
            "routes.finite.r3_18_budget7_branch1_domination_cegar.EARLY_STOP_AFTER_MODELS",
            2,
        ):
            result = run_bounded_cegar(
                backend,
                excluded_masks=exclusions,
                clock=lambda: 0.0,
                witness_generator=generated,
            )
        self.assertEqual(result["status"], ENDPOINT_UNKNOWN_LOW_PRODUCTIVITY)
        self.assertEqual(result["telemetry"]["models_seen"], 2)
        self.assertEqual(result["telemetry"]["novel_masks_added"], 2)
        self.assertLess(result["detail"]["novel_ratio"], 0.25)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
