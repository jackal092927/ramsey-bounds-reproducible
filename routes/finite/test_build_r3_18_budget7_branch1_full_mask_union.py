#!/usr/bin/env python3
"""Regression tests for the solver-free branch-1 full-mask union route."""

from __future__ import annotations

import gzip
import io
import itertools
import json
import tempfile
import unittest
from pathlib import Path

from . import build_r3_18_budget7_branch1_full_mask_union as union


class FullMaskUnionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.here = Path(union.__file__).resolve().parent
        cls.audit, cls.extra = union.audit_production_sources(
            matrix=cls.here / "certificates" / "r3_18_n100_nearmiss.txt",
            seed_verification=cls.here / "r3_18_n100_nearmiss_verification.json",
            universal=cls.here / "r3_18_budget6_branch_0_universal_union.cuts.json",
            history=cls.here / "r3_18_budget7_branch1_cegar_history_exclusion.json",
            aplus=cls.here / "r3_18_budget7_branch1_cegar_Aplus_batch.json",
            core_summary=cls.here / "r3_18_budget7_branch1_core_proof_summary.json",
            aplus_endpoint_audit=(
                cls.here
                / "r3_18_budget7_branch1_cegar_Aplus_f24_endpoint_audit.json"
            ),
        )

    def test_production_union_counts_overlaps_and_digests(self) -> None:
        dedup = self.audit["deduplication"]
        self.assertEqual(dedup["three_family_union"]["masks"], 526_429)
        self.assertEqual(dedup["full_union"]["masks"], 530_525)
        self.assertEqual(dedup["duplicates_removed_three_families"], 25_437)
        self.assertEqual(dedup["universal_history_fixed_base_intersection"], 646)
        self.assertTrue(dedup["A+"]["zero_overlap_with_three_family_union"])
        self.assertEqual(len(self.extra), 278_754)
        self.assertEqual(
            union.ordered_masks_sha256(self.extra), union.EXPECTED_EXTRA_SHA256
        )

    def test_every_family_has_universal_I18_clause_semantics(self) -> None:
        soundness = self.audit["mathematical_soundness"]
        self.assertTrue(soundness["all_four_families_are_18_subsets_of_[100]"])
        self.assertTrue(soundness["provenance_not_needed_for_clause_validity"])
        self.assertTrue(soundness["valid_for_every_exact_seven_target"])
        self.assertEqual(soundness["literals_per_mask"], 153)

    def test_hitting_clause_is_153_distinct_positive_edge_variables(self) -> None:
        mask = sum(1 << vertex for vertex in range(18))
        variables = union.lexicographic_edge_variables()
        line = union.hitting_clause_line(mask, variables)
        values = [int(value) for value in line.split()]
        self.assertEqual(values[-1], 0)
        self.assertEqual(len(values[:-1]), 153)
        self.assertEqual(len(set(values[:-1])), 153)
        self.assertTrue(all(value > 0 for value in values[:-1]))
        expected = [
            variables[edge] for edge in itertools.combinations(range(18), 2)
        ]
        self.assertEqual(values[:-1], expected)

    def test_Aplus_same_count_replacement_and_symlink_are_rejected(self) -> None:
        source = self.here / "r3_18_budget7_branch1_cegar_Aplus_batch.json"
        with tempfile.TemporaryDirectory() as temporary_name:
            temporary = Path(temporary_name)
            payload = json.loads(source.read_text(encoding="utf-8"))
            payload["masks"][0], payload["masks"][1] = (
                payload["masks"][1],
                payload["masks"][0],
            )
            replacement = temporary / "same_count_replacement.json"
            replacement.write_text(
                json.dumps(payload, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            self.assertEqual(len(payload["masks"]), union.APLUS_COUNT)
            with self.assertRaisesRegex(union.AuditError, "SHA-256 mismatch"):
                union.load_aplus(replacement)

            link = temporary / "aplus-link.json"
            link.symlink_to(source)
            with self.assertRaisesRegex(union.AuditError, "symlink"):
                union.load_aplus(link)

    def test_duplicate_JSON_keys_and_duplicate_masks_are_rejected(self) -> None:
        with self.assertRaisesRegex(union.AuditError, "duplicate key"):
            union.strict_json_bytes(b'{"masks":[],"masks":[]}', "fixture")
        value = f"{sum(1 << vertex for vertex in range(18)):025x}"
        with self.assertRaisesRegex(union.AuditError, "duplicate masks"):
            union.canonical_mask_array(
                [value, value],
                description="fixture",
                expected_count=2,
                require_sorted=False,
            )

    def test_small_clique_enumerator_matches_bruteforce(self) -> None:
        order = 7
        edges = {(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (4, 5)}
        rows = [0] * order
        for u, v in edges:
            rows[u] |= 1 << v
            rows[v] |= 1 << u
        candidates = (1 << order) - 1
        actual, nodes = union.enumerate_k_cliques(rows, candidates, 3)
        expected = [
            sum(1 << vertex for vertex in group)
            for group in itertools.combinations(range(order), 3)
            if all(tuple(sorted(edge)) in edges for edge in itertools.combinations(group, 2))
        ]
        self.assertEqual(sorted(actual), expected)
        self.assertGreater(nodes, 0)

    def test_parameterized_stream_constructor_has_exact_order(self) -> None:
        common_header = b"p cnf 154190 1\n"
        final_header = b"p cnf 154190 3\n"
        raw_common = common_header + b"1 0\n"
        mask = sum(1 << vertex for vertex in range(18))
        variables = union.lexicographic_edge_variables()
        sink = io.BytesIO()
        identity = union.write_augmented_cnf_stream(
            sink,
            raw_common=raw_common,
            common_header=common_header,
            final_header=final_header,
            positive_units=[2],
            extra_masks=[mask],
            variables=variables,
        )
        expected = (
            final_header
            + b"1 0\n"
            + b"2 0\n"
            + union.hitting_clause_line(mask, variables)
        )
        self.assertEqual(sink.getvalue(), expected)
        self.assertEqual(identity["bytes"], len(expected))
        self.assertEqual(identity["lines"], 4)
        self.assertEqual(identity["sha256"], union.sha256_bytes(expected))

    def test_constructor_refuses_existing_output_before_any_input_read(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_name:
            destination = Path(temporary_name) / "already-there.cnf"
            destination.write_bytes(b"do not overwrite\n")
            with self.assertRaises(FileExistsError):
                union.emit_full_cnf(
                    Path(temporary_name) / "missing-common.cnf.gz",
                    destination,
                    [],
                )
            self.assertEqual(destination.read_bytes(), b"do not overwrite\n")

    def test_common_CNF_identity_and_full_CNF_symlink_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_name:
            temporary = Path(temporary_name)
            fake_common = temporary / "common.cnf.gz"
            fake_common.write_bytes(gzip.compress(b"p cnf 1 1\n1 0\n"))
            with self.assertRaisesRegex(union.AuditError, "gzip identity mismatch"):
                union.inspect_common_cnf_gzip(fake_common)

            real = temporary / "full.cnf"
            real.write_bytes(b"p cnf 1 0\n")
            link = temporary / "full-link.cnf"
            link.symlink_to(real)
            with self.assertRaisesRegex(union.AuditError, "symlink"):
                list(union.iter_regular_lines(link))

    def test_existing_route_comparison_and_bounded_stop_rule(self) -> None:
        comparison = self.audit["comparison_with_existing_routes"]
        self.assertEqual(
            comparison["existing_A+_gate"]["full_union_adds_clauses"], 274_658
        )
        benders = comparison["Benders_universal_plus_all_fixed_base"]
        self.assertEqual(benders["deduplicated_masks"], 482_815)
        self.assertEqual(benders["full_union_additional_masks"], 47_710)
        self.assertFalse(benders["is_byte_or_formula_duplicate"])
        gate = self.audit["bounded_go_no_go"]
        self.assertEqual(gate["decision"], "GO_BUILD_AND_AUDIT__NO_GO_LONG_SOLVE_YET")
        self.assertEqual(gate["optional_probe"]["maximum_runs"], 1)
        self.assertEqual(gate["optional_probe"]["maximum_wall_seconds"], 300)
        self.assertTrue(gate["optional_probe"]["no_resume_no_solver_swap_no_cap_increase"])

    def test_formula_identity_and_claim_boundary_are_frozen(self) -> None:
        plan = self.audit["formula_plan"]
        self.assertEqual(plan["final_clauses"], 997_210)
        self.assertEqual(plan["expected_plain_CNF_bytes"], 390_604_816)
        self.assertEqual(
            plan["expected_plain_CNF_sha256"],
            "4f7e8f5b724a657888c7814d2c25cac41c283c3db356fb8f1a15f4c7322c375d",
        )
        self.assertFalse(plan["solver_invoked"])
        self.assertIsNone(self.audit["exact_seven_repair_exists"])
        self.assertIsNone(self.audit["global_ramsey_implication"])


if __name__ == "__main__":
    unittest.main()
