"""Asset-free regressions for the historical f24 endpoint auditor."""

from __future__ import annotations

import copy
import gzip
import hashlib
import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from .audit_r3_18_budget7_branch1_cegar_f24_endpoint import (
    EXPECTED_CLAIM_BOUNDARY,
    EXPECTED_STATE_MACHINE,
    GATE_SCHEMA,
    STATUS_SAT_WITNESS,
    STATUS_UNKNOWN_WALL,
    STATUS_UNSAT_UNCHECKED,
    FrozenProfile,
    _direct_graph_audit,
    audit_endpoint,
)
from .check_r3_18_budget7_branch1_common_sat import parse_complete_model
from .check_r3_18_budget7_branch1_core_cnf import AuditError


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _gzip(raw: bytes) -> bytes:
    return gzip.compress(raw, compresslevel=9, mtime=0)


def _gzip_record(path: Path) -> dict[str, object]:
    compressed = path.read_bytes()
    raw = gzip.decompress(compressed)
    return {
        "basename": path.name,
        "bytes": len(compressed),
        "sha256": _sha256(compressed),
        "uncompressed_bytes": len(raw),
        "uncompressed_sha256": _sha256(raw),
    }


class HistoricalF24EndpointAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="ramsey-f24-audit-test-")
        self.root = Path(self.temporary.name)
        self.endpoint = self.root / "endpoint"
        self.endpoint.mkdir()
        self.runner = self.root / "historical.py"
        self.runner.write_bytes(b"historical runner snapshot\n")
        self.cnf_raw = b"p cnf 6 1\n1 0\n"
        (self.endpoint / "branch1_cegar_augmented.cnf").write_bytes(self.cnf_raw)
        base = FrozenProfile()
        self.profile = replace(
            base,
            runner_basename=self.runner.name,
            runner_sha256=_sha256(self.runner.read_bytes()),
            order=4,
            independent_target=3,
            maximum_variable=6,
            augmented_cnf_sha256=_sha256(self.cnf_raw),
            augmented_cnf_bytes=len(self.cnf_raw),
            augmented_cnf_clauses=1,
            common_cnf_sha256="1" * 64,
            common_model_sha256="2" * 64,
            bank_masks=3,
            bank_ordered_sha256="3" * 64,
            history_masks=4,
            history_raw_masks=5,
            history_sources=2,
            history_file_sha256="4" * 64,
            history_ordered_sha256="5" * 64,
            fixed_base_masks=6,
            fixed_base_ordered_sha256="6" * 64,
            new_masks=0,
            mask_batch_file_sha256="7" * 64,
            mask_batch_ordered_sha256="8" * 64,
            positive_edges=((0, 1),),
            positive_units=(1,),
            cadical_sha256="9" * 64,
            cadical_commit="a" * 40,
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _checker(self) -> dict[str, object]:
        marker = (self.profile.cadical_commit + "\n").encode("ascii")
        return {
            "basename": "cadical",
            "sha256": self.profile.cadical_sha256,
            "source_commit": self.profile.cadical_commit,
            "source_commit_marker_sha256": _sha256(marker),
        }

    def _inputs(self) -> dict[str, object]:
        return {
            "common_cnf": {
                "basename": "common.cnf.gz",
                "bytes": 11,
                "sha256": self.profile.common_cnf_sha256,
            },
            "common_model": {
                "basename": "common.model.gz",
                "bytes": 12,
                "sha256": self.profile.common_model_sha256,
            },
            "common_model_audit_status": (
                "VERIFIED_BRANCH1_COMMON_RELAXATION_SAT_MODEL"
            ),
            "common_model_assignment_literals": self.profile.maximum_variable,
            "universal_bank": {
                "basename": "bank.json",
                "masks": self.profile.bank_masks,
                "ordered_masks_sha256": self.profile.bank_ordered_sha256,
            },
            "historical_exclusion": {
                "basename": "history.json",
                "bytes": 13,
                "sha256": self.profile.history_file_sha256,
                "masks": self.profile.history_masks,
                "ordered_masks_sha256": self.profile.history_ordered_sha256,
                "source_checkpoints": self.profile.history_sources,
                "source_raw_masks": self.profile.history_raw_masks,
                "within_source_duplicates": 0,
            },
            "fixed_branch1_base_exclusion": {
                "masks": self.profile.fixed_base_masks,
                "ordered_masks_sha256": self.profile.fixed_base_ordered_sha256,
                "membership_check": (
                    "direct pairwise independence test in the authenticated seed "
                    "with edge (97,99) removed"
                ),
            },
            "new_mask_batch": {
                "basename": "batch.json",
                "bytes": 14,
                "sha256": self.profile.mask_batch_file_sha256,
                "masks": self.profile.new_masks,
                "ordered_masks_sha256": self.profile.mask_batch_ordered_sha256,
                "canonical_hex_width": (self.profile.order + 3) // 4,
                "all_new_relative_to_three_frozen_exclusion_families": True,
                "all_independent_in_frozen_model": True,
                "three_family_overlap_counts": {
                    "universal_bank": 0,
                    "historical_learned_union": 0,
                    "exhaustive_fixed_branch1_base_family": 0,
                },
                "three_family_zero_overlap_verified": True,
            },
        }

    def _augmentation(self) -> dict[str, object]:
        return {
            "positive_edges": [list(edge) for edge in self.profile.positive_edges],
            "positive_units": list(self.profile.positive_units),
            "new_I18_clauses": self.profile.new_masks,
            "augmented_cnf": {
                "basename": "branch1_cegar_augmented.cnf",
                "bytes": self.profile.augmented_cnf_bytes,
                "sha256": self.profile.augmented_cnf_sha256,
                "variables": self.profile.maximum_variable,
                "clauses": self.profile.augmented_cnf_clauses,
                "header_and_clause_lines": self.profile.augmented_cnf_clauses + 1,
                "clause_order": [
                    "frozen_common_clauses",
                    "four_proved_positive_units",
                    "ordered_new_I18_hitting_clauses",
                ],
            },
        }

    def _finished_base(self, status: str, exitcode: int) -> dict[str, object]:
        return {
            "status": status,
            "exitcode": exitcode,
            "wall_limit_seconds": 60.0,
            "elapsed_seconds": 5.0,
            "stdout_sha256": "b" * 64,
            "stderr_sha256": "c" * 64,
            "stdout_tail": "",
            "stderr_tail": "",
            "checker": self._checker(),
            "learned_masks": [],
        }

    def _gate(self, solver: dict[str, object]) -> dict[str, object]:
        return {
            "schema": GATE_SCHEMA,
            "status": solver["status"],
            "state_machine": EXPECTED_STATE_MACHINE,
            "claim_boundary": EXPECTED_CLAIM_BOUNDARY,
            "inputs": self._inputs(),
            "augmentation": self._augmentation(),
            "solver": solver,
            "learned_masks": [],
            "proof_verified": False,
            "exact_seven_repair_exists": None,
            "global_ramsey_implication": None,
        }

    def _write_gate(self, gate: dict[str, object]) -> None:
        (self.endpoint / "branch1_cegar_gate.json").write_text(
            json.dumps(gate, sort_keys=True) + "\n", encoding="utf-8"
        )

    def _audit(self) -> dict[str, object]:
        return audit_endpoint(
            endpoint_dir=self.endpoint,
            historical_runner=self.runner,
            expected_wall_seconds=60.0,
            profile=self.profile,
        )

    def test_unknown_wall_authenticates_endpoint_but_no_claim(self) -> None:
        solver = {
            "status": STATUS_UNKNOWN_WALL,
            "exitcode": -9,
            "wall_limit_seconds": 60.0,
            "elapsed_seconds": 60.1,
            "stdout_sha256": "b" * 64,
            "stderr_sha256": "c" * 64,
            "checker": self._checker(),
            "learned_masks": [],
        }
        self._write_gate(self._gate(solver))
        result = self._audit()
        self.assertEqual(
            result["status"], "F24_UNKNOWN_ENDPOINT_AUTHENTICATED_NO_CLAIM"
        )
        self.assertFalse(result["sat_claim_accepted"])
        self.assertFalse(result["unsat_claim_accepted"])
        self.assertEqual(result["learned_masks"], [])

    def test_gate_tampering_is_rejected_fail_closed(self) -> None:
        solver = {
            "status": STATUS_UNKNOWN_WALL,
            "exitcode": -9,
            "wall_limit_seconds": 60.0,
            "elapsed_seconds": 60.0,
            "stdout_sha256": "b" * 64,
            "stderr_sha256": "c" * 64,
            "checker": self._checker(),
            "learned_masks": [],
        }
        pristine = self._gate(solver)
        cases: list[tuple[str, dict[str, object]]] = []
        extra = copy.deepcopy(pristine)
        extra["unrecognized"] = True
        cases.append(("extra root field", extra))
        learned = copy.deepcopy(pristine)
        learned["solver"]["learned_masks"] = [1]  # type: ignore[index]
        cases.append(("learned mask", learned))
        input_hash = copy.deepcopy(pristine)
        input_hash["inputs"]["new_mask_batch"]["sha256"] = "0" * 64  # type: ignore[index]
        cases.append(("input hash", input_hash))
        checker = copy.deepcopy(pristine)
        checker["solver"]["checker"]["sha256"] = "0" * 64  # type: ignore[index]
        cases.append(("checker hash", checker))
        wall = copy.deepcopy(pristine)
        wall["solver"]["wall_limit_seconds"] = 59.0  # type: ignore[index]
        cases.append(("wall", wall))
        for name, gate in cases:
            with self.subTest(name=name):
                self._write_gate(gate)
                with self.assertRaises(AuditError):
                    self._audit()

    def test_duplicate_json_key_and_changed_runner_or_cnf_are_rejected(self) -> None:
        gate_path = self.endpoint / "branch1_cegar_gate.json"
        gate_path.write_text('{"schema":"x","schema":"y"}\n', encoding="ascii")
        with self.assertRaisesRegex(AuditError, "duplicate key"):
            self._audit()

        solver = {
            "status": STATUS_UNKNOWN_WALL,
            "exitcode": -9,
            "wall_limit_seconds": 60.0,
            "elapsed_seconds": 60.0,
            "stdout_sha256": "b" * 64,
            "stderr_sha256": "c" * 64,
            "checker": self._checker(),
            "learned_masks": [],
        }
        self._write_gate(self._gate(solver))
        self.runner.write_bytes(b"changed runner\n")
        with self.assertRaisesRegex(AuditError, "runner snapshot"):
            self._audit()
        self.runner.write_bytes(b"historical runner snapshot\n")
        (self.endpoint / "branch1_cegar_augmented.cnf").write_bytes(
            self.cnf_raw + b"2 0\n"
        )
        with self.assertRaisesRegex(AuditError, "CNF identity"):
            self._audit()

    def _install_sat_model(self, first_literal: int = 1) -> dict[str, object]:
        literals = [first_literal, -2, -3, -4, -5, -6]
        raw = ("s SATISFIABLE\nv " + " ".join(map(str, literals)) + " 0\n").encode(
            "ascii"
        )
        path = self.endpoint / "branch1_cegar_sat.model.gz"
        path.write_bytes(_gzip(raw))
        return _gzip_record(path)

    def _recorded_i18(self, model_path: Path) -> dict[str, object]:
        assignment, _ = parse_complete_model(model_path, self.profile.maximum_variable)
        graph = _direct_graph_audit(assignment, self.profile)
        witness = graph["independent_set_witness"]
        assert isinstance(witness, list)
        mask = sum(1 << vertex for vertex in witness)
        return {
            "independent_set_exists": True,
            "witness": witness,
            "mask_hex": f"{mask:01x}",
            "search_nodes": graph["search_nodes"],
            "pairwise_independence_checked": True,
            "new_relative_to_all_installed_masks": True,
            "overlap_with_exclusion_families": {
                "universal_bank": False,
                "historical_learned_union": False,
                "exhaustive_fixed_branch1_base_family": False,
                "new_gate_batch": False,
            },
            "known_from_historical_learned_union": False,
            "known_from_exhaustive_fixed_base_family": False,
            "new_relative_to_three_frozen_exclusion_families": True,
            "installed_or_learned_by_this_gate": False,
        }

    def test_sat_is_reparsed_fully_evaluated_and_graph_checked(self) -> None:
        model = self._install_sat_model()
        solver = self._finished_base(STATUS_SAT_WITNESS, 10)
        solver.update(
            {
                "model": model,
                "model_evaluation": {
                    "all_clauses_satisfied": True,
                    "clauses_evaluated": 1,
                },
                "I18_search": self._recorded_i18(
                    self.endpoint / "branch1_cegar_sat.model.gz"
                ),
            }
        )
        self._write_gate(self._gate(solver))
        result = self._audit()
        self.assertEqual(
            result["status"], "F24_SAT_REAUDITED_I18_WITNESS_NO_LOWER_BOUND"
        )
        self.assertTrue(result["sat_claim_accepted"])
        self.assertTrue(result["full_cnf_evaluation"]["all_clauses_satisfied"])
        self.assertFalse(result["direct_graph_audit"]["triangle_exists"])
        self.assertTrue(result["direct_graph_audit"]["independent_set_exists"])

    def test_sat_record_cannot_hide_a_model_that_falsifies_the_cnf(self) -> None:
        model = self._install_sat_model(first_literal=-1)
        solver = self._finished_base(STATUS_SAT_WITNESS, 10)
        solver.update(
            {
                "model": model,
                "model_evaluation": {
                    "all_clauses_satisfied": True,
                    "clauses_evaluated": 1,
                },
                "I18_search": self._recorded_i18(
                    self.endpoint / "branch1_cegar_sat.model.gz"
                ),
            }
        )
        self._write_gate(self._gate(solver))
        with self.assertRaisesRegex(AuditError, "falsifies augmented clause"):
            self._audit()

    def test_unsat_only_binds_proof_and_remains_promotion_pending(self) -> None:
        proof_path = self.endpoint / "branch1_cegar_unsat.drat.gz"
        proof_path.write_bytes(_gzip(b"0\n"))
        solver = self._finished_base(STATUS_UNSAT_UNCHECKED, 20)
        solver.update(
            {
                "proof": _gzip_record(proof_path),
                "proof_checked_by_drat_trim": False,
                "unsat_claim_accepted": False,
            }
        )
        self._write_gate(self._gate(solver))
        result = self._audit()
        self.assertEqual(
            result["status"], "F24_UNSAT_ENDPOINT_AUTHENTICATED_PROMOTION_PENDING"
        )
        self.assertFalse(result["proof_verified"])
        self.assertFalse(result["unsat_claim_accepted"])
        self.assertEqual(
            result["promotion"]["proof_gzip_sha256"], _sha256(proof_path.read_bytes())
        )
        proof_path.write_bytes(_gzip(b"d 1 0\n"))
        with self.assertRaisesRegex(AuditError, "proof identity"):
            self._audit()

    def test_optional_local_cadical_copy_is_rehashed_but_not_executed(self) -> None:
        binary_dir = self.root / "cadical-build"
        binary_dir.mkdir()
        binary = binary_dir / "cadical"
        binary.write_bytes(b"pinned checker bytes\n")
        (binary_dir / "SOURCE_COMMIT").write_text(
            self.profile.cadical_commit + "\n", encoding="ascii"
        )
        self.profile = replace(
            self.profile, cadical_sha256=_sha256(binary.read_bytes())
        )
        solver = {
            "status": STATUS_UNKNOWN_WALL,
            "exitcode": -9,
            "wall_limit_seconds": 60.0,
            "elapsed_seconds": 60.0,
            "stdout_sha256": "b" * 64,
            "stderr_sha256": "c" * 64,
            "checker": self._checker(),
            "learned_masks": [],
        }
        self._write_gate(self._gate(solver))
        result = audit_endpoint(
            endpoint_dir=self.endpoint,
            historical_runner=self.runner,
            expected_wall_seconds=60.0,
            cadical=binary,
            profile=self.profile,
        )
        self.assertEqual(
            result["local_cadical_rehash"]["binary"]["sha256"],
            self.profile.cadical_sha256,
        )
        self.assertFalse(result["local_cadical_rehash"]["executed_by_auditor"])


if __name__ == "__main__":
    unittest.main()
