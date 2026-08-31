"""Semantic regression tests for the exact-seven branch-1 Benders pilot."""

from __future__ import annotations

import itertools
import json
import tempfile
import unittest
from pathlib import Path

from pysat.formula import IDPool
from pysat.solvers import Solver

from .benders_budget9 import (
    conditional_cut_truth,
    edge_set,
    enumerate_cliques_interruptible,
    make_conditional_clause,
    master_support,
    vertices,
)
from .budget8_next import masks_hash
from .graph_utils import enumerate_cliques
from .r3_18_budget7_benders_branch1 import (
    EXPECTED_ADDITION_PAIRS,
    EXPECTED_BASE_EDGES,
    EXPECTED_FIXED_BASE_I18,
    EXPECTED_FIXED_BASE_I18_SHA256,
    EXPECTED_INPUT_SHA256,
    FIXED_EDGE,
    RESIDUAL_DELETIONS,
    branch1_base,
    build_master_formula,
    encode_degree_upper_bounds,
    enumerate_cliques_with_order,
    exact_add_only_subproblem,
    fixed_base_i18_masks,
    initial_cut_bank_identity,
    load_resume_state,
    run_branch1_benders,
    shareable_path,
    strict_no_good_clause,
    validate_frozen_seed,
    validate_limited_solver,
    vertex_selection_sat_checks,
)
from .verify_ramsey import complement, read_matrix


HERE = Path(__file__).resolve().parent
SEED = HERE / "certificates" / "r3_18_n100_nearmiss.txt"


def rows_from_edges(n: int, edges: list[tuple[int, int]]) -> list[int]:
    rows = [0] * n
    for u, v in edges:
        rows[u] |= 1 << v
        rows[v] |= 1 << u
    return rows


class Budget7Branch1BendersTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = read_matrix(SEED)
        validate_frozen_seed(cls.rows)
        cls.base = branch1_base(cls.rows)
        cls.fixed_masks = fixed_base_i18_masks(cls.rows)

    @staticmethod
    def initial_metadata() -> dict[str, object]:
        return {
            "fixed_base_I18_total": EXPECTED_FIXED_BASE_I18,
            "fixed_base_I18_sha256": EXPECTED_FIXED_BASE_I18_SHA256,
            "fixed_base_I18_preloaded": 0,
            "universal_bank": None,
            "deduplicated_initial_masks": 0,
            "deduplicated_initial_masks_sha256": masks_hash([]),
            "subproblem_seed_mask_prefix": 0,
            "subproblem_seed_mask_prefix_sha256": masks_hash([]),
            "subproblem_seed_priority": "fixed-base masks, then universal bank",
            "ordering": "ascending integer vertex mask",
        }

    def test_fixed_base_i18_family_is_canonical_and_complete(self) -> None:
        masks = self.fixed_masks
        self.assertEqual(len(masks), EXPECTED_FIXED_BASE_I18)
        self.assertEqual(masks, sorted(set(masks)))
        self.assertEqual(masks_hash(masks), EXPECTED_FIXED_BASE_I18_SHA256)
        self.assertTrue(all(mask >> FIXED_EDGE[0] & 1 for mask in masks))
        self.assertTrue(all(mask >> FIXED_EDGE[1] & 1 for mask in masks))

    def test_deep_supports_are_not_reverse_order_oracle_unknowns(self) -> None:
        # These are the two replayable supports whose historical ascending
        # separator and first fixed-D subproblem model each reached 20,000,001
        # nodes without a witness.  The candidate graph is reconstructed from
        # the recorded D and selected-y support, not read from a mutable run.
        cases = (
            (
                {
                    (3, 97), (9, 97), (10, 97),
                    (11, 97), (27, 98), (40, 99),
                },
                {(27, 97), (56, 99), (72, 97)},
            ),
            (
                {
                    (17, 98), (30, 98), (33, 99),
                    (37, 99), (41, 99), (46, 99),
                },
                {(30, 99), (53, 99), (57, 99), (65, 99)},
            ),
        )
        expected = tuple(range(81, 98)) + (99,)
        for deleted, selected_y in cases:
            with self.subTest(deleted=sorted(deleted)):
                support = master_support(self.base, deleted, selected_y)
                adjacency = complement(support)
                historical = enumerate_cliques_interruptible(
                    adjacency, 18, 1, 64, 1.0
                )
                ascending, ascending_log = enumerate_cliques_with_order(
                    adjacency, 18, 1, 64, 1.0, "ascending"
                )
                self.assertEqual(ascending.witnesses, historical.witnesses)
                self.assertEqual(ascending.complete, historical.complete)
                self.assertEqual(ascending.reason, historical.reason)
                self.assertEqual(
                    ascending.recursive_nodes, historical.recursive_nodes
                )
                self.assertEqual(ascending.witnesses, [])
                self.assertFalse(ascending.complete)
                self.assertEqual(ascending.reason, "NODE_LIMIT")
                self.assertEqual(
                    [record["order"] for record in ascending_log["passes"]],
                    ["ascending"],
                )

                for strategy in ("reverse", "bidirectional"):
                    found, telemetry = enumerate_cliques_with_order(
                        adjacency, 18, 1, 64, 1.0, strategy
                    )
                    self.assertFalse(found.complete)
                    self.assertEqual(found.reason, "WITNESS_LIMIT")
                    self.assertEqual(len(found.witnesses), 1)
                    witness = found.witnesses[0]
                    chosen = tuple(vertices(witness))
                    self.assertEqual(chosen, expected)
                    # Independent validation uses the original support rows,
                    # not the relabeled complement searched by the oracle.
                    self.assertEqual(witness.bit_count(), 18)
                    self.assertTrue(
                        all(
                            not ((support[u] >> v) & 1)
                            for u, v in itertools.combinations(chosen, 2)
                        )
                    )
                    self.assertEqual(telemetry["strategy"], strategy)
                    self.assertEqual(
                        telemetry["passes"][0]["order"], "reverse"
                    )

    def test_bidirectional_second_pass_and_complete_composition(self) -> None:
        # With only the low-label edge, reverse exhausts its half-node budget
        # before reaching the sole K2; the historical ascending pass finds it.
        low_edge = rows_from_edges(4, [(0, 1)])
        found, telemetry = enumerate_cliques_with_order(
            low_edge, 2, 1, 7, 1.0, "bidirectional"
        )
        self.assertEqual(
            [record["order"] for record in telemetry["passes"]],
            ["reverse", "ascending"],
        )
        self.assertEqual(telemetry["passes"][0]["reason"], "NODE_LIMIT")
        self.assertEqual(found.witnesses, [(1 << 0) | (1 << 1)])
        self.assertFalse(found.complete)
        self.assertEqual(found.reason, "WITNESS_LIMIT")
        self.assertLessEqual(found.recursive_nodes, 8)

        # Reverse is again incomplete, but ascending exhausts this triangle-free
        # graph.  A complete second pass may therefore certify global absence.
        path = rows_from_edges(3, [(0, 2), (1, 2)])
        exhausted, telemetry = enumerate_cliques_with_order(
            path, 3, 10, 5, 1.0, "bidirectional"
        )
        self.assertEqual(
            [record["order"] for record in telemetry["passes"]],
            ["reverse", "ascending"],
        )
        self.assertFalse(telemetry["passes"][0]["complete"])
        self.assertTrue(telemetry["passes"][1]["complete"])
        self.assertEqual(exhausted.witnesses, [])
        self.assertTrue(exhausted.complete)
        self.assertEqual(exhausted.reason, "EXHAUSTED")
        self.assertLessEqual(exhausted.recursive_nodes, 6)

    def test_all_oracle_orders_against_small_graph_brute_force(self) -> None:
        for n in range(1, 5):
            pairs = list(itertools.combinations(range(n), 2))
            for graph_mask in range(1 << len(pairs)):
                adjacency = rows_from_edges(
                    n,
                    [edge for i, edge in enumerate(pairs) if graph_mask >> i & 1],
                )
                for target in range(n + 2):
                    expected = {
                        sum(1 << vertex for vertex in subset)
                        for subset in itertools.combinations(range(n), target)
                        if all(
                            (adjacency[u] >> v) & 1
                            for u, v in itertools.combinations(subset, 2)
                        )
                    }
                    for strategy in ("ascending", "reverse", "bidirectional"):
                        found, _ = enumerate_cliques_with_order(
                            adjacency,
                            target,
                            max(1, len(expected) + 1),
                            10000,
                            1.0,
                            strategy,
                        )
                        self.assertTrue(found.complete)
                        self.assertEqual(set(found.witnesses), expected)

    def test_master_dimensions_and_exact_six_cardinality(self) -> None:
        clauses, dvars, yvars, _, metadata = build_master_formula(
            self.base, {FIXED_EDGE}, RESIDUAL_DELETIONS
        )
        self.assertEqual(len(dvars), EXPECTED_BASE_EDGES)
        self.assertEqual(len(yvars), EXPECTED_ADDITION_PAIRS)
        self.assertEqual(metadata["exact_cardinality_clauses"], 19680)
        self.assertEqual(metadata["local_eligibility_clauses"], 12832)
        self.assertEqual(metadata["degree_cap"], 17)
        self.assertEqual(metadata["degree_cardinality_blocks"], 100)
        self.assertGreater(metadata["degree_cardinality_clauses"], 0)
        self.assertEqual(metadata["degree_impossible_vertices"], [])
        self.assertEqual(
            metadata["fixed_base_degree_histogram"],
            {"16": 49, "17": 50, "18": 1},
        )
        self.assertEqual(metadata["fixed_base_vertices_above_degree_cap"], [98])
        self.assertEqual(
            metadata["common_neighbor_wedge_histogram"],
            {"1": 737, "2": 1498, "3": 209, "4": 1132,
             "5": 150, "6": 9, "8": 352, "9": 36},
        )
        ordered = sorted(dvars)
        incident_98 = next(edge for edge in ordered if 98 in edge)
        degree_feasible_order = [incident_98] + [
            edge for edge in ordered if edge != incident_98
        ]
        for count, expected in ((5, False), (6, True), (7, False)):
            deleted = set(degree_feasible_order[:count])
            assumptions = [
                dvars[edge] if edge in deleted else -dvars[edge]
                for edge in ordered
            ]
            assumptions.extend(-variable for variable in yvars.values())
            with Solver(name="minisat22", bootstrap_with=clauses) as solver:
                self.assertEqual(solver.solve(assumptions=assumptions), expected)

        nonincident_98 = set(edge for edge in ordered if 98 not in edge)
        deleted = set(sorted(nonincident_98)[:RESIDUAL_DELETIONS])
        assumptions = [
            dvars[edge] if edge in deleted else -dvars[edge]
            for edge in ordered
        ] + [-variable for variable in yvars.values()]
        with Solver(name="minisat22", bootstrap_with=clauses) as solver:
            self.assertFalse(solver.solve(assumptions=assumptions))

    def test_degree_cap_encoding_has_exact_projection_semantics(self) -> None:
        dvars = {(0, 1): 1, (1, 2): 2, (2, 3): 3}
        yvars = {(0, 2): 4, (0, 3): 5, (1, 3): 6}
        pool = IDPool(start_from=7)
        clauses, metadata = encode_degree_upper_bounds(
            4, dvars, yvars, 1, pool
        )
        self.assertGreater(metadata["degree_cardinality_clauses"], 0)
        self.assertGreater(metadata["degree_cardinality_auxiliary_variables"], 0)
        self.assertGreaterEqual(pool.top, 6)

        ditems = sorted(dvars.items())
        yitems = sorted(yvars.items())
        with Solver(name="minisat22", bootstrap_with=clauses) as solver:
            for bits in range(1 << (len(ditems) + len(yitems))):
                deleted = {
                    edge
                    for index, (edge, _) in enumerate(ditems)
                    if bits >> index & 1
                }
                selected = {
                    edge
                    for index, (edge, _) in enumerate(yitems, len(ditems))
                    if bits >> index & 1
                }
                assumptions = [
                    variable if edge in deleted else -variable
                    for edge, variable in ditems
                ] + [
                    variable if edge in selected else -variable
                    for edge, variable in yitems
                ]
                degrees = [0] * 4
                for edge in set(dvars) - deleted:
                    for vertex in edge:
                        degrees[vertex] += 1
                for edge in selected:
                    for vertex in edge:
                        degrees[vertex] += 1
                self.assertEqual(
                    solver.solve(assumptions=assumptions),
                    max(degrees) <= 1,
                    (deleted, selected, degrees),
                )

        offset_pool = IDPool(start_from=7)
        offset_clauses, offset_metadata = encode_degree_upper_bounds(
            4, {}, yvars, 2, offset_pool, [2, 1, 1, 0]
        )
        self.assertEqual(
            offset_metadata["degree_residual_bound_histogram"],
            {"0": 1, "1": 2, "2": 1},
        )
        with Solver(name="minisat22", bootstrap_with=offset_clauses) as solver:
            for bits in range(1 << len(yitems)):
                selected = {
                    edge
                    for index, (edge, _) in enumerate(yitems)
                    if bits >> index & 1
                }
                assumptions = [
                    variable if edge in selected else -variable
                    for edge, variable in yitems
                ]
                degrees = [2, 1, 1, 0]
                for edge in selected:
                    for vertex in edge:
                        degrees[vertex] += 1
                self.assertEqual(
                    solver.solve(assumptions=assumptions),
                    max(degrees) <= 2,
                    (selected, degrees),
                )

    def test_general_conditional_cut_clause_matches_semantic_truth(self) -> None:
        base = rows_from_edges(4, [(0, 1), (1, 2), (2, 3)])
        dvars = {edge: index + 1 for index, edge in enumerate(sorted(edge_set(base)))}
        nonedges = sorted(
            set(itertools.combinations(range(4), 2)) - set(dvars)
        )
        yvars = {
            edge: len(dvars) + index + 1
            for index, edge in enumerate(nonedges)
        }
        clause = make_conditional_clause((1 << 4) - 1, base, dvars, yvars)
        ditems = sorted(dvars.items())
        yitems = sorted(yvars.items())
        for bits in range(1 << (len(ditems) + len(yitems))):
            deleted = {
                edge
                for index, (edge, _) in enumerate(ditems)
                if bits >> index & 1
            }
            selected = {
                edge
                for index, (edge, _) in enumerate(yitems, len(ditems))
                if bits >> index & 1
            }
            true_variables = {
                variable
                for edge, variable in ditems
                if edge in deleted
            } | {
                variable
                for edge, variable in yitems
                if edge in selected
            }
            encoded_truth = any(
                (literal > 0 and literal in true_variables)
                or (literal < 0 and -literal not in true_variables)
                for literal in clause
            )
            self.assertEqual(
                encoded_truth,
                conditional_cut_truth(base, deleted, selected, range(4)),
            )

    def test_fixed_base_mask_becomes_a_pure_eligible_addition_cut(self) -> None:
        mask = self.fixed_masks[0]
        clauses, dvars, yvars, _, _ = build_master_formula(
            self.base, {FIXED_EDGE}, RESIDUAL_DELETIONS
        )
        del clauses  # The semantic assertion concerns the translated cut.
        clause = make_conditional_clause(mask, self.base, dvars, yvars)
        self.assertEqual(len(clause), 152)  # C(18,2) minus fixed (97,99).
        self.assertTrue(set(clause) <= set(yvars.values()))
        self.assertTrue(
            all(
                not (self.base[vertex] & mask)
                for vertex in vertices(mask)
            )
        )

    def test_eligibility_clause_matches_common_neighbor_wedge(self) -> None:
        clauses, dvars, yvars, requirements, _ = build_master_formula(
            self.base, {FIXED_EDGE}, RESIDUAL_DELETIONS
        )
        addition = next(
            edge
            for edge in sorted(yvars)
            if len(requirements[edge]) == 1
            and all(self.base[vertex].bit_count() <= 16 for vertex in edge)
        )
        first, second = requirements[addition][0]
        unrelated = [
            edge for edge in sorted(dvars) if edge not in {first, second}
        ]
        incident_98 = next(edge for edge in unrelated if 98 in edge)
        filler = [edge for edge in unrelated if edge != incident_98]

        misses_wedge = {incident_98, *filler[: RESIDUAL_DELETIONS - 1]}
        hits_wedge = {
            first,
            incident_98,
            *filler[: RESIDUAL_DELETIONS - 2],
        }
        for deleted, expected in ((misses_wedge, False), (hits_wedge, True)):
            assumptions = [
                dvars[edge] if edge in deleted else -dvars[edge]
                for edge in sorted(dvars)
            ]
            assumptions.append(yvars[addition])
            with Solver(name="minisat22", bootstrap_with=clauses) as solver:
                self.assertEqual(solver.solve(assumptions=assumptions), expected)

    def test_exact_add_only_subproblem_sat_and_unsat_oracles(self) -> None:
        # Empty K3 with alpha target 2 would need all three additions, which
        # the triangle clause forbids.
        empty = rows_from_edges(3, [])
        pair_masks = enumerate_cliques(complement(empty), 2)
        unsat, candidate = exact_add_only_subproblem(
            empty, set(), set(), 2, pair_masks, "minisat22",
            100, 1000, 1.0, 2.0, 10000, 1.0,
        )
        self.assertEqual(unsat["status"], "UNSAT")
        self.assertIsNone(candidate)

        # C5 is already triangle-free with alpha 2, so it is an exact SAT
        # instance for target s=3 with no additions.
        cycle = rows_from_edges(
            5, [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]
        )
        sat, candidate = exact_add_only_subproblem(
            cycle, set(), set(), 3, [], "minisat22",
            100, 1000, 1.0, 2.0, 10000, 1.0,
        )
        self.assertEqual(sat["status"], "SAT")
        self.assertIsNotNone(candidate)
        self.assertEqual(edge_set(candidate), edge_set(cycle))
        self.assertEqual(sat["oracle_order"], "bidirectional")
        self.assertEqual(
            sat["last_oracle_search"]["strategy"], "bidirectional"
        )
        self.assertTrue(
            vertex_selection_sat_checks(cycle, 3, "cadical195")[
                "valid_ramsey_certificate"
            ]
        )

    def test_unknown_never_produces_a_deletion_no_good(self) -> None:
        _, dvars, _, _, _ = build_master_formula(
            self.base, {FIXED_EDGE}, RESIDUAL_DELETIONS
        )
        deleted = set(sorted(dvars)[:RESIDUAL_DELETIONS])
        for status in (
            "UNKNOWN_WALL_LIMIT",
            "UNKNOWN_CONFLICT_LIMIT",
            "UNKNOWN_ORACLE_WALL_LIMIT",
            "SAT",
        ):
            self.assertIsNone(strict_no_good_clause(status, deleted, dvars))
        clause = strict_no_good_clause("UNSAT", deleted, dvars)
        self.assertEqual(clause, [-dvars[edge] for edge in sorted(deleted)])
        with self.assertRaisesRegex(ValueError, "invalid fixed-deletion"):
            strict_no_good_clause("UNSAT", set(sorted(dvars)[:5]), dvars)

    def test_runner_rejects_backend_without_bounded_slice_support(self) -> None:
        validate_limited_solver("minisat22")
        with self.assertRaisesRegex(ValueError, "does not support"):
            validate_limited_solver("cadical195")

    def test_tiny_global_wall_writes_clean_deterministic_checkpoint(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.json"
            result, candidate = run_branch1_benders(
                self.rows,
                EXPECTED_INPUT_SHA256,
                [],
                self.initial_metadata(),
                [],
                checkpoint,
                "minisat22",
                10,
                10,
                0.01,
                0.001,
                1,
                1,
                100,
                0.01,
                "minisat22",
                10,
                10,
                0.01,
                0.01,
            )
            self.assertEqual(result["status"], "UNKNOWN_GLOBAL_WALL_LIMIT")
            self.assertIsNone(candidate)
            strict = result["strict_state"]
            self.assertTrue(strict["heuristic_exclusion_free"])
            self.assertFalse(
                strict["subproblem_unsat_no_goods_proof_checked"]
            )
            self.assertEqual(strict["unknown_subproblem_no_goods"], 0)
            self.assertEqual(strict["additional_conditional_masks_hex"], [])
            self.assertEqual(strict["fixed_deletion_unsat_no_goods"], [])
            self.assertTrue(checkpoint.is_file())

    def test_separator_checkpoint_is_dynamic_and_resume_is_strict(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.json"
            result, candidate = run_branch1_benders(
                self.rows, EXPECTED_INPUT_SHA256, [], self.initial_metadata(), [],
                checkpoint, "minisat22", 1000, 10000, 1.0, 5.0, 1, 1,
                100000, 1.0, "minisat22", 100, 1000, 0.1, 0.1,
            )
            self.assertEqual(result["status"], "UNKNOWN_MASTER_ITERATION_LIMIT")
            self.assertIsNone(candidate)
            self.assertEqual(result["progress"]["new_conditional_I18_masks"], 1)
            self.assertEqual(result["formula"]["installed_conditional_I18_clauses"], 1)
            self.assertEqual(result["formula"]["new_conditional_I18_clauses_this_run"], 1)
            self.assertEqual(
                result["formula"]["current_total_clauses"],
                result["formula"]["structural_clauses"] + 1,
            )
            model = result["progress"]["last_master_models"][-1]
            selected = model["selected_eligible_addition_edges"]
            self.assertEqual(len(selected), model["selected_eligible_additions"])
            self.assertEqual(selected, sorted(selected))
            self.assertEqual(result["oracle"]["vertex_order"], "bidirectional")
            self.assertEqual(result["limits"]["oracle_order"], "bidirectional")
            self.assertEqual(model["oracle_order"], "bidirectional")
            self.assertEqual(
                model["oracle_order_telemetry"]["strategy"], "bidirectional"
            )

            _, dvars, _, _, metadata = build_master_formula(
                self.base, {FIXED_EDGE}, RESIDUAL_DELETIONS
            )
            bank_identity = initial_cut_bank_identity(self.initial_metadata())
            self.assertEqual(result["initial_cut_bank_identity"], bank_identity)
            masks, no_goods, info = load_resume_state(
                checkpoint,
                EXPECTED_INPUT_SHA256,
                metadata["structural_fingerprint_sha256"],
                set(dvars),
                bank_identity,
            )
            self.assertEqual(len(masks), 1)
            self.assertEqual(no_goods, [])
            self.assertEqual(info["path"], "checkpoint.json")
            self.assertEqual(info["source_oracle_order"], "bidirectional")
            self.assertTrue(info["source_oracle_order_explicitly_recorded"])
            self.assertEqual(
                info["initial_cut_bank_validation"]["source_identity_mode"],
                "explicit_identity_v1",
            )

            payload = json.loads(checkpoint.read_text(encoding="utf-8"))
            legacy = Path(directory) / "legacy.json"
            del payload["initial_cut_bank_identity"]
            legacy.write_text(json.dumps(payload), encoding="utf-8")
            _, _, legacy_info = load_resume_state(
                legacy,
                EXPECTED_INPUT_SHA256,
                metadata["structural_fingerprint_sha256"],
                set(dvars),
                bank_identity,
            )
            self.assertEqual(
                legacy_info["initial_cut_bank_validation"]["source_identity_mode"],
                "legacy_metadata_reconstructed",
            )

            mismatched_metadata = dict(self.initial_metadata())
            mismatched_metadata.update(
                {
                    "fixed_base_I18_preloaded": 1,
                    "deduplicated_initial_masks": 1,
                    "deduplicated_initial_masks_sha256": masks_hash(
                        [self.fixed_masks[0]]
                    ),
                }
            )
            with self.assertRaisesRegex(ValueError, "different initial cut bank"):
                load_resume_state(
                    checkpoint,
                    EXPECTED_INPUT_SHA256,
                    metadata["structural_fingerprint_sha256"],
                    set(dvars),
                    initial_cut_bank_identity(mismatched_metadata),
                )

            corrupt_identity = Path(directory) / "corrupt-identity.json"
            payload = json.loads(checkpoint.read_text(encoding="utf-8"))
            payload["initial_cut_bank_identity"]["identity_sha256"] = "0" * 64
            corrupt_identity.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "identity is corrupt"):
                load_resume_state(
                    corrupt_identity,
                    EXPECTED_INPUT_SHA256,
                    metadata["structural_fingerprint_sha256"],
                    set(dvars),
                    bank_identity,
                )

            damaged = Path(directory) / "damaged.json"
            payload = json.loads(checkpoint.read_text(encoding="utf-8"))
            payload["strict_state"]["strict_state_sha256"] = "0" * 64
            damaged.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "digest mismatch"):
                load_resume_state(
                    damaged,
                    EXPECTED_INPUT_SHA256,
                    metadata["structural_fingerprint_sha256"],
                    set(dvars),
                    bank_identity,
                )

    def test_incomplete_master_oracle_falls_back_without_unknown_no_good(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.json"
            result, candidate = run_branch1_benders(
                self.rows, EXPECTED_INPUT_SHA256, [], self.initial_metadata(), [],
                checkpoint, "minisat22", 1000, 10000, 1.0, 5.0, 2, 1,
                1, 1.0, "minisat22", 100, 1000, 0.1, 0.000001,
            )
            self.assertTrue(result["status"].startswith("UNKNOWN_SUBPROBLEM_"))
            self.assertIsNone(candidate)
            self.assertEqual(
                result["progress"]["master_oracle_incomplete_fallbacks"], 1
            )
            model = result["progress"]["last_master_models"][-1]
            self.assertEqual(
                model["control_flow"],
                "MASTER_ORACLE_INCOMPLETE_FALLBACK_TO_EXACT_SUBPROBLEM",
            )
            self.assertTrue(model["master_oracle_incomplete_reason"])
            self.assertEqual(
                result["strict_state"]["fixed_deletion_unsat_no_goods"], []
            )
            self.assertEqual(result["strict_state"]["unknown_subproblem_no_goods"], 0)
            self.assertTrue(result["progress"]["last_subproblem"]["status"].startswith("UNKNOWN_"))

    def test_shareable_paths_never_expose_external_parent_directories(self) -> None:
        self.assertEqual(
            shareable_path(SEED),
            "routes/finite/certificates/r3_18_n100_nearmiss.txt",
        )
        with tempfile.TemporaryDirectory() as directory:
            external = Path(directory) / "private" / "checkpoint.json"
            self.assertEqual(shareable_path(external), "checkpoint.json")


if __name__ == "__main__":
    unittest.main()
