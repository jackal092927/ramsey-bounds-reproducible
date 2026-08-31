#!/usr/bin/env python3
"""Regression tests for the branch-1 maximality-WLOG audit."""

from __future__ import annotations

import itertools
import gzip
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from routes.finite import check_r3_18_budget7_branch1_maximality_wlog as audit


HERE = Path(__file__).resolve().parent
EXPECTED_RECORD_SHA256 = (
    "d63f0cedb7a72533581d00b1a6cf25e8705efe240d6224b41de4d5572ede7b3b"
)
EXPECTED_LEDGER_SHA256 = (
    "9eeda3123dd0d2095135e10cb2fff40c37c0a7d6592fcfa3c2403ac0fb12eed7"
)


def _clause_satisfied(clause: list[int], assignment: dict[int, bool]) -> bool:
    return any(assignment[abs(literal)] == (literal > 0) for literal in clause)


class MaximalityWlogAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = audit.build_ledger(
            seed_path=HERE / "certificates" / "r3_18_n100_nearmiss.txt",
            budget6_path=HERE / "r3_18_budget6_summary.json",
            bank_path=HERE / "r3_18_budget6_branch_0_universal_union.cuts.json",
            history_path=HERE
            / "r3_18_budget7_branch1_cegar_history_exclusion.json",
            aplus_batch_path=HERE
            / "r3_18_budget7_branch1_cegar_Aplus_batch.json",
            structural_ledger_path=HERE
            / "r3_18_budget7_branch1_structural_projection.json",
            aplus_gate_path=HERE
            / "certificates"
            / "r3_18_budget7_branch1_cegar_Aplus_f24_endpoint"
            / "branch1_cegar_gate.json",
        )

    def test_tracked_ledger_is_exact_reconstruction(self) -> None:
        ledger_path = HERE / "r3_18_budget7_branch1_maximality_wlog.json"
        raw = ledger_path.read_bytes()
        self.assertEqual(audit.EXPECTED_LEDGER_SHA256, EXPECTED_LEDGER_SHA256)
        self.assertEqual(audit._sha256(raw), EXPECTED_LEDGER_SHA256)
        self.assertEqual(audit.load_ledger(ledger_path), self.payload)
        self.assertEqual(self.payload["record_sha256"], EXPECTED_RECORD_SHA256)

    def test_two_layer_theorem_and_claim_firewall(self) -> None:
        self.assertEqual(
            self.payload["inputs"]["seed"]["unique_triangle_vertices"],
            [97, 98, 99],
        )
        self.assertEqual(self.payload["inputs"]["seed"]["triangles"], 1)
        theorem = self.payload["theorem"]
        self.assertFalse(
            theorem["layer_A_original_nonedge_saturation"][
                "dependency_on_radius_lower_bound"
            ]
        )
        self.assertTrue(
            theorem["layer_A_original_nonedge_saturation"]["WLOG_equisatisfiable"]
        )
        self.assertEqual(
            theorem["layer_B_full_maximal_triangle_free"][
                "dependency_budget6_summary_sha256"
            ],
            audit.EXPECTED_BUDGET6_SHA256,
        )
        self.assertTrue(
            theorem["layer_B_full_maximal_triangle_free"][
                "fixed_branch_addback_covered_by_global_three_branch_certificate"
            ]
        )
        boundary = self.payload["claim_boundary"]
        self.assertFalse(boundary["every_raw_target_is_maximal"])
        self.assertFalse(boundary["layer_A_requires_rho_lower_bound"])
        self.assertTrue(boundary["layer_B_requires_rho_lower_bound"])
        self.assertTrue(boundary["current_Aplus_assignment_eliminated_by_layer_A"])
        self.assertTrue(
            boundary["current_Aplus_deletion_support_has_semantic_completion"]
        )
        self.assertFalse(boundary["branch1_closed"])
        self.assertFalse(boundary["exact_seven_closed"])
        self.assertFalse(boundary["global_Ramsey_improvement"])

    def test_common_model_exact_facts(self) -> None:
        model = self.payload["models"]["common"]
        self.assertEqual(model["degree_distribution"], {"16": 50, "17": 50})
        self.assertEqual(model["maximality_violations"], 1)
        self.assertEqual(
            [item["edge"] for item in model["violation_details"]], [[37, 86]]
        )
        self.assertEqual(
            model["violation_details"][0]["endpoint_degrees"], [16, 17]
        )
        self.assertEqual(
            model["domination_cut_from_degree_17_violation"]["mask_hex"],
            "2000000404414192982822020",
        )
        self.assertFalse(model["exact_assignment_satisfies_layer_A"])
        completion = model["deterministic_layer_A_completion"]
        self.assertEqual(completion["added_edges"], [[37, 86]])
        self.assertTrue(completion["full_maximal_triangle_free"])
        self.assertEqual(completion["maximum_degree"], 18)
        self.assertFalse(
            completion[
                "same_deletion_support_primary_graph_satisfies_relaxation_semantics"
            ]
        )

    def test_Aplus_model_exact_facts_and_assignment_support_distinction(self) -> None:
        model = self.payload["models"]["Aplus"]
        self.assertEqual(model["degree_distribution"], {"16": 54, "17": 46})
        self.assertEqual(model["maximality_violations"], 3)
        self.assertEqual(
            [item["edge"] for item in model["violation_details"]],
            [[16, 64], [32, 98], [40, 89]],
        )
        self.assertTrue(
            all(
                item["endpoint_degrees"] == [16, 16]
                and item["edge_type"] == "original_nonedge"
                and not item["belongs_to_frozen_396_no_addition_units"]
                and item["minimum_local_deletions_for_396_unit_test"] == 2
                for item in model["violation_details"]
            )
        )
        self.assertFalse(model["exact_assignment_satisfies_layer_A"])
        completion = model["deterministic_layer_A_completion"]
        self.assertEqual(
            completion["added_edges"], [[16, 64], [32, 98], [40, 89]]
        )
        self.assertEqual(completion["degree_distribution"], {"16": 48, "17": 52})
        self.assertTrue(completion["full_maximal_triangle_free"])
        self.assertTrue(
            completion[
                "same_deletion_support_primary_graph_satisfies_relaxation_semantics"
            ]
        )
        self.assertFalse(completion["existing_DIMACS_auxiliary_assignment_reused"])
        self.assertFalse(completion["counter_auxiliary_reextension_materialized_here"])
        self.assertTrue(
            model["preserved_gate_I18_witness"][
                "still_independent_after_layer_A_completion"
            ]
        )

    def test_selector_counts_are_frozen(self) -> None:
        design = self.payload["selector_CNF_design"]
        self.assertEqual(
            design["layer_A_original_nonedges"],
            {
                "pairs": 4_123,
                "witnesses_per_pair": 98,
                "auxiliary_variables": 404_054,
                "clauses": 812_231,
                "long_clauses": 4_123,
                "binary_implication_clauses": 808_108,
                "maximum_variable_from_current_formula": 558_244,
                "clauses_with_common_formula": 1_530_683,
                "clauses_with_Aplus_augmented_formula": 1_534_783,
                "recommended_first_encoding": True,
                "rho_dependency": False,
            },
        )
        self.assertEqual(design["layer_B_all_pairs"]["auxiliary_variables"], 485_100)
        self.assertEqual(design["layer_B_all_pairs"]["clauses"], 975_150)

    def test_selector_CNF_is_existentially_exact_on_three_vertices(self) -> None:
        pairs = list(itertools.combinations(range(3), 2))
        variables = {edge: index for index, edge in enumerate(pairs, 1)}
        clauses = list(audit.iter_selector_clauses(3, variables, pairs, 4))
        self.assertEqual(len(clauses), 9)
        for primary_bits in range(1 << 3):
            primary = {
                variable: bool(primary_bits & (1 << (variable - 1)))
                for variable in range(1, 4)
            }
            existentially_satisfiable = False
            for witness_bits in range(1 << 3):
                assignment = {
                    **primary,
                    **{
                        variable: bool(witness_bits & (1 << (variable - 4)))
                        for variable in range(4, 7)
                    },
                }
                if all(_clause_satisfied(clause, assignment) for clause in clauses):
                    existentially_satisfiable = True
                    break
            edges = {
                edge for edge, variable in variables.items() if primary[variable]
            }
            rows = audit.edge_rows(edges, 3)
            semantic_condition = all(
                edge in edges or bool(rows[edge[0]] & rows[edge[1]])
                for edge in pairs
            )
            self.assertEqual(existentially_satisfiable, semantic_condition)

    def test_layer_A_saturation_preserves_deletion_support_exhaustively(self) -> None:
        order = 5
        pairs = list(itertools.combinations(range(order), 2))
        seed = frozenset({(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)})
        for bits in range(1 << len(pairs)):
            edges = frozenset(
                edge for index, edge in enumerate(pairs) if bits & (1 << index)
            )
            rows = audit.edge_rows(edges, order)
            if audit.triangle_count(rows):
                continue
            completion, added = audit.saturate_original_nonedges(edges, seed, order)
            self.assertEqual(seed - completion, seed - edges)
            self.assertFalse(set(added) & set(seed))
            self.assertEqual(audit.triangle_count(audit.edge_rows(completion, order)), 0)
            self.assertFalse(
                any(
                    edge not in seed
                    for edge in audit.maximality_violations(completion, order)
                )
            )

    def test_gate_parser_rejects_missing_common_model_audit(self) -> None:
        gate_path = (
            HERE
            / "certificates"
            / "r3_18_budget7_branch1_cegar_Aplus_f24_endpoint"
            / "branch1_cegar_gate.json"
        )
        payload = json.loads(gate_path.read_text())
        del payload["inputs"]["common_model_audit_status"]
        tampered = json.dumps(payload).encode()
        with mock.patch.object(audit, "_strict_regular", return_value=tampered):
            with self.assertRaisesRegex(audit.AuditError, "identity/status mismatch"):
                audit.validate_aplus_gate(Path("ignored"))

    def test_complete_model_parser_checks_every_variable_and_projection(self) -> None:
        literals = " ".join(
            str(-variable)
            for variable in range(1, audit.CURRENT_MAXIMUM_VARIABLE + 1)
        )
        raw = f"s SATISFIABLE\nv {literals} 0\n".encode("ascii")
        compressed = gzip.compress(raw, mtime=0)
        profile = audit.ModelProfile(
            label="synthetic complete model",
            gzip_sha256=audit._sha256(compressed),
            gzip_bytes=len(compressed),
            raw_sha256=audit._sha256(raw),
            raw_bytes=len(raw),
            projection_sha256=audit.projection_sha256(frozenset()),
            deletions=(),
            additions=(),
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "model.gz"
            path.write_bytes(compressed)
            self.assertEqual(audit.read_complete_model(path, profile), frozenset())

            duplicate_raw = raw.replace(b"v -1 -2", b"v -1 -1 -2", 1)
            duplicate_compressed = gzip.compress(duplicate_raw, mtime=0)
            duplicate_profile = audit.ModelProfile(
                label="synthetic duplicate model",
                gzip_sha256=audit._sha256(duplicate_compressed),
                gzip_bytes=len(duplicate_compressed),
                raw_sha256=audit._sha256(duplicate_raw),
                raw_bytes=len(duplicate_raw),
                projection_sha256=profile.projection_sha256,
                deletions=(),
                additions=(),
            )
            path.write_bytes(duplicate_compressed)
            with self.assertRaisesRegex(audit.AuditError, "twice"):
                audit.read_complete_model(path, duplicate_profile)

    def test_tracked_ledger_loader_rejects_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target.json"
            target.write_text("{}\n")
            link = root / "ledger.json"
            link.symlink_to(target)
            with self.assertRaisesRegex(audit.AuditError, "non-symlink"):
                audit.load_ledger(link)


if __name__ == "__main__":
    unittest.main()
