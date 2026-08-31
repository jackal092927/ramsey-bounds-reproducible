"""Regressions for the independent bounded structural-projection audit."""

from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from .check_r3_18_budget7_branch1_structural_projection import (
    AuditError,
    EXPECTED_PROPAGATED_NEGATIVE_EDGES,
    FIXED_EDGE,
    FORCED_POSITIVE_EDGES,
    ORDER,
    RESIDUAL_DELETIONS,
    _canonical_sha256,
    build_audit,
    common_neighbour_audit,
    edge_rows,
    full_no_addition_audit,
    load_tracked_ledger,
    propagated_negative_edges,
    read_seed,
)


HERE = Path(__file__).resolve().parent
SEED = HERE / "certificates" / "r3_18_n100_nearmiss.txt"
BANK = HERE / "r3_18_budget6_branch_0_universal_union.cuts.json"
LEDGER = HERE / "r3_18_budget7_branch1_structural_projection.json"
HISTORY = HERE / "r3_18_budget7_branch1_cegar_history_exclusion.json"
APLUS = HERE / "r3_18_budget7_branch1_cegar_Aplus_batch.json"


class StructuralProjectionAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = build_audit(SEED, BANK, HISTORY, APLUS)
        _, original_edges, _ = read_seed(SEED)
        cls.base_edges = frozenset(original_edges - {FIXED_EDGE})
        cls.base_rows = edge_rows(cls.base_edges, ORDER)

    def test_tracked_machine_ledger_matches_independent_reconstruction(self) -> None:
        tracked = load_tracked_ledger(LEDGER)
        self.assertEqual(tracked, self.audit)
        digest_basis = copy.deepcopy(tracked)
        digest = digest_basis.pop("record_sha256")
        self.assertEqual(_canonical_sha256(digest_basis), digest)

    def test_projection_lemma_has_exact_machine_premises(self) -> None:
        projection = self.audit["triangle_and_degree_projection"]
        self.assertEqual(projection["seed_triangles"], [[97, 98, 99]])
        self.assertEqual(projection["fixed_base_triangle_count"], 0)
        self.assertEqual(
            projection["fixed_base_degree_distribution"],
            {"16": 49, "17": 50, "18": 1},
        )
        self.assertEqual(projection["vertices_above_degree_cap"], [98])
        self.assertEqual(
            projection["endpoint_degrees"],
            {"11": 17, "18": 17, "61": 16, "62": 16,
             "64": 16, "69": 16, "98": 18},
        )
        self.assertTrue(
            projection["support_conditions_complete_for_triangle_degree_subsystem"]
        )

    def test_four_positive_units_propagate_exactly_three_negative_units(self) -> None:
        self.assertEqual(
            propagated_negative_edges(FORCED_POSITIVE_EDGES),
            EXPECTED_PROPAGATED_NEGATIVE_EDGES,
        )
        self.assertEqual(
            self.audit["forced_unit_triangle_propagation"]["negative_edges"],
            [[61, 64], [61, 69], [64, 69]],
        )

    def test_common_neighbour_threshold_units_are_exact_and_wedge_disjoint(self) -> None:
        derived, info = common_neighbour_audit(self.base_rows, self.base_edges)
        self.assertEqual(info["fixed_base_nonedges_including_fixed_unit_edge"], 4124)
        self.assertEqual(
            info["common_neighbour_count_distribution"],
            {"1": 738, "2": 1498, "3": 209, "4": 1132,
             "5": 150, "6": 9, "8": 352, "9": 36},
        )
        self.assertEqual(len(derived), 388)
        self.assertEqual(
            info["derived_edge_list_sha256"],
            "e4cf70c1cb970b637982268fc169b82a98c4f45f207487cb24b94c31122c9f68",
        )
        for u, v in derived:
            common = self.base_rows[u] & self.base_rows[v]
            self.assertGreater(common.bit_count(), RESIDUAL_DELETIONS)
            wedge_edges = set()
            while common:
                bit = common & -common
                common ^= bit
                w = bit.bit_length() - 1
                wedge_edges.add(tuple(sorted((u, w))))
                wedge_edges.add(tuple(sorted((v, w))))
            self.assertEqual(len(wedge_edges), 2 * (self.base_rows[u] & self.base_rows[v]).bit_count())
            self.assertTrue(wedge_edges <= self.base_edges)

    def test_full_396_no_addition_closure_is_exact(self) -> None:
        common, _ = common_neighbour_audit(self.base_rows, self.base_edges)
        units, info = full_no_addition_audit(
            self.base_rows, self.base_edges, common
        )
        self.assertEqual(len(units), 396)
        self.assertEqual(
            info["edge_list_sha256"],
            "ff387efadc49230f2920e842972522683d31ddab7d496d8a0380f6a2704b4492",
        )
        self.assertEqual(
            info["breakdown"],
            {
                "common_neighbours_greater_than_six": 388,
                "direct_triangle_units_not_in_common_threshold": 2,
                "coupled_degree_vertex98_budget_units": 6,
            },
        )
        self.assertEqual(
            info["minimum_local_deletions_distribution"],
            {
                "2": 729,
                "3": 1584,
                "4": 166,
                "5": 1146,
                "6": 103,
                "7": 6,
                "9": 363,
                "10": 24,
                "infeasible": 3,
            },
        )
        self.assertEqual(
            info["coupled_degree_vertex98_budget_edges"],
            [[55, 97], [56, 97], [57, 97], [88, 99], [89, 99], [90, 99]],
        )

    def test_bank_incidence_and_residual_ranges_are_frozen(self) -> None:
        bank = self.audit["universal_bank_local_substitution"]
        self.assertEqual(
            bank["forced_positive_edge_incidence"],
            {"11-62": 64, "18-61": 16, "18-64": 6, "18-69": 16},
        )
        self.assertEqual(bank["clauses_satisfied_by_forced_positive_units"], 102)
        self.assertEqual(bank["unresolved_clauses"], 251_669)
        self.assertEqual(
            bank["propagated_negative_edge_incidence_among_unresolved"],
            {"61-64": 1154, "61-69": 6249, "64-69": 702},
        )
        self.assertEqual(
            bank["residual_original_nonedge_addition_literals_after_direct_units"],
            {"range": [146, 152], "clauses_with_zero": 0},
        )
        self.assertEqual(
            bank["residual_original_nonedge_addition_literals_after_all_local_units"],
            {
                "range": [115, 140],
                "clauses_with_zero": 0,
                "minimum_clause": {
                    "mask_hex": "a832130504404000000040441",
                    "fixed_base_seed_edge_literals": 3,
                    "original_seed_edge_literals_including_fixed_unit": 4,
                    "forbidden_no_addition_literals": 34,
                    "free_addition_literals": 115,
                },
            },
        )
        self.assertEqual(
            bank["full_396_no_addition_units_per_unresolved_mask"]["range"],
            [12, 34],
        )
        self.assertFalse(bank["support_only_clause_created_by_local_substitution"])

    def test_local_swap_is_not_misreported_as_a_global_counterexample(self) -> None:
        probe = self.audit["local_swap_probe"]
        self.assertTrue(probe["exact_six_residual_deletions"])
        self.assertTrue(probe["forced_positive_edges_retained"])
        self.assertTrue(probe["deletion_support_hits_vertex_98"])
        self.assertFalse(probe["deletion_support_hits_vertex_18"])
        self.assertEqual(probe["triangle_count"], 0)
        self.assertEqual(probe["maximum_degree"], 17)
        self.assertFalse(probe["universal_bank_satisfied"])
        self.assertEqual(probe["violated_universal_bank_masks_count"], 12)
        self.assertEqual(
            probe["violated_universal_bank_masks_sha256"],
            "0781584d5e22dbeb508c879ef03d26c639269072a378f3457acd1156e98fe13f",
        )
        self.assertEqual(
            probe["single_edge_direct_repairs_preserving_triangle_and_degree_caps"],
            0,
        )
        self.assertFalse(probe["violates_full_local_no_addition_closure"])

    def test_domination_lift_finds_one_new_checked_common_model_cut(self) -> None:
        lift = self.audit["domination_lift"]
        self.assertEqual(lift["degree_distribution"], {"16": 50, "17": 50})
        self.assertEqual(lift["degree_17_violations"], 1)
        self.assertEqual(lift["degree_16_nonclique_violations"], 0)
        self.assertEqual(
            lift["Z_size_distribution_at_degree_17"], {"0": 49, "1": 1}
        )
        self.assertEqual(
            lift["Z_size_distribution_at_degree_16"], {"0": 49, "1": 1}
        )
        self.assertEqual(
            lift["unique_violation"],
            {
                "vertex": 86,
                "Z_vertex": 37,
                "mask_vertices": [5, 13, 17, 23, 25, 31, 32, 35, 37,
                                  40, 43, 44, 50, 52, 58, 62, 70, 97],
                "mask_hex": "2000000404414192982822020",
                "mask_line_sha256": "31881b3f9667899000e686f2c09b3adb02a305225e561820a457f03870dd9be4",
                "common_model_internal_edges": 0,
                "fixed_base_internal_edges": 3,
            },
        )
        self.assertTrue(lift["zero_overlap_verified"])
        self.assertEqual(lift["common_model_universal_bank_violations"], 0)
        self.assertTrue(lift["common_model_forced_positive_units_retained"])
        self.assertEqual(
            lift["overlap_with_frozen_families"],
            {
                "universal_bank": False,
                "historical_learned_union": False,
                "Aplus_batch": False,
                "exhaustive_fixed_base_family": False,
            },
        )
        self.assertTrue(lift["strict_common_relaxation_strengthening"])

    def test_claim_boundary_explicitly_rejects_the_two_unsafe_upgrades(self) -> None:
        boundary = self.audit["claim_boundary"]
        self.assertFalse(boundary["vertex_18_hit_proved"])
        self.assertFalse(boundary["no_stronger_global_support_lift_proved"])
        self.assertFalse(boundary["global_addition_elimination_performed"])

    def test_changed_or_symlinked_inputs_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ramsey-structural-audit-test-") as tmp:
            root = Path(tmp)
            changed = root / "seed.txt"
            changed.write_bytes(SEED.read_bytes() + b"\n")
            with self.assertRaisesRegex(AuditError, "SHA-256"):
                read_seed(changed)
            symlink = root / "seed-link.txt"
            symlink.symlink_to(SEED)
            with self.assertRaisesRegex(AuditError, "non-symlink"):
                read_seed(symlink)


if __name__ == "__main__":
    unittest.main()
