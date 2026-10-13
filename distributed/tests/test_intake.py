"""Independent toy positives and rejection controls for certificate intake."""
import copy
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "scripts"))
from ingest import Rejection, ingest_all, validate_submission
from leaderboard import build_board
from verify_certificate import self_check


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class IntakeControls(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "project"
        shutil.copytree(PROJECT, self.root, ignore=shutil.ignore_patterns("__pycache__", "results"))
        self.descriptor = self.root / "submissions/known-c5-r3s3.json"
        self.submission = json.loads(self.descriptor.read_text())

    def tearDown(self):
        self.tmp.cleanup()

    def rebind_receipt(self):
        path = self.root / self.submission["provenance"]["run_receipt"]["path"]
        receipt = json.loads(path.read_text())
        receipt["submission_id"] = self.submission["submission_id"]
        receipt["claim"] = self.submission["claim"]
        receipt["certificate_sha256"] = self.submission["certificate"]["sha256"]
        receipt["seed_sha256"] = [seed["sha256"] for seed in self.submission["provenance"]["seeds"]]
        path.write_text(json.dumps(receipt))
        self.submission["provenance"]["run_receipt"]["sha256"] = digest(path)

    def replace_matrix(self, text):
        path = self.root / self.submission["certificate"]["path"]
        path.write_text(text)
        self.submission["certificate"]["sha256"] = digest(path)
        self.submission["provenance"]["seeds"] = [copy.deepcopy(self.submission["certificate"])]
        self.rebind_receipt()

    def test_known_c5_positive(self):
        result = validate_submission(self.root, self.submission)
        self.assertEqual(result["status"], "ACCEPTED")
        self.assertEqual(result["verification"]["certified_lower_bound"], 6)
        self.assertIsNone(result["is_global_record"])

    def test_forbidden_clique_rejected_even_with_consistent_provenance(self):
        self.replace_matrix("01111\n10111\n11011\n11101\n11110\n")
        result = validate_submission(self.root, self.submission)
        self.assertEqual(result["status"], "REJECTED")
        self.assertEqual(result["reason"], "FORBIDDEN_CLIQUE")
        self.assertIsNone(result["verification"]["certified_lower_bound"])

    def test_asymmetric_rejected(self):
        self.replace_matrix("00000\n10000\n00000\n00000\n00000\n")
        with self.assertRaisesRegex(ValueError, "asymmetric"):
            validate_submission(self.root, self.submission)

    def test_missing_provenance_rejected(self):
        del self.submission["provenance"]
        with self.assertRaises(Rejection):
            validate_submission(self.root, self.submission)

    def test_changed_source_bytes_rejected(self):
        with (self.root / "scripts/build_baselines.py").open("a") as stream:
            stream.write("\n# altered after the recorded run\n")
        with self.assertRaisesRegex(Rejection, "source hash mismatch"):
            validate_submission(self.root, self.submission)

    def test_run_objective_mismatch_rejected(self):
        path = self.root / self.submission["provenance"]["run_receipt"]["path"]
        receipt = json.loads(path.read_text())
        receipt["claim"]["s"] = 4
        path.write_text(json.dumps(receipt))
        self.submission["provenance"]["run_receipt"]["sha256"] = digest(path)
        with self.assertRaisesRegex(Rejection, "run objective mismatch"):
            validate_submission(self.root, self.submission)

    def test_unknown_run_endpoint_rejected(self):
        path = self.root / self.submission["provenance"]["run_receipt"]["path"]
        receipt = json.loads(path.read_text())
        receipt["observed"]["status"] = "UNKNOWN"
        path.write_text(json.dumps(receipt))
        self.submission["provenance"]["run_receipt"]["sha256"] = digest(path)
        with self.assertRaisesRegex(Rejection, "did not complete"):
            validate_submission(self.root, self.submission)

    def test_deadline_unknown_cannot_enter_board(self):
        result = validate_submission(self.root, self.submission, max_seconds=1e-12)
        self.assertEqual(result["status"], "UNKNOWN")
        self.assertIsNone(result["verification"]["certified_lower_bound"])
        board = build_board({"checked_at": "test", "records": [result], "denominator": 1,
                             "accepted": 0, "unknown": 1, "rejected": 0})
        self.assertEqual(board["pairs"], [])

    def test_path_traversal_rejected(self):
        self.submission["certificate"]["path"] = "../escape.txt"
        with self.assertRaisesRegex(Rejection, "traversal"):
            validate_submission(self.root, self.submission)

    def test_nonfinite_budget_rejected(self):
        self.submission["provenance"]["budget"]["wall_seconds"] = float("nan")
        with self.assertRaisesRegex(Rejection, "finite number"):
            validate_submission(self.root, self.submission)

    def test_pair_separation(self):
        first = validate_submission(self.root, self.submission)
        self.submission["claim"]["s"] = 4
        self.submission["submission_id"] = "known-c5-r3s4"
        self.rebind_receipt()
        second = validate_submission(self.root, self.submission)
        board = build_board({"checked_at": "test", "records": [first, second],
                             "denominator": 2, "accepted": 2, "unknown": 0, "rejected": 0})
        self.assertEqual([(entry["r"], entry["s"]) for entry in board["pairs"]], [(3, 3), (3, 4)])

    def test_duplicate_whitespace_counts_one_labelled_witness(self):
        first = validate_submission(self.root, self.submission)
        text = (self.root / self.submission["certificate"]["path"]).read_text()
        self.replace_matrix("\n".join(" ".join(row) for row in text.splitlines()) + "\n")
        self.submission["submission_id"] = "known-c5-whitespace-duplicate"
        self.rebind_receipt()
        second = validate_submission(self.root, self.submission)
        board = build_board({"checked_at": "test", "records": [first, second],
                             "denominator": 2, "accepted": 2, "unknown": 0, "rejected": 0})
        self.assertEqual(board["pairs"][0]["unique_labelled_witness_count"], 1)

    def test_rejected_submission_stays_in_denominator(self):
        self.submission.pop("provenance")
        self.descriptor.write_text(json.dumps(self.submission))
        ledger = ingest_all(self.root)
        self.assertEqual((ledger["denominator"], ledger["accepted"], ledger["rejected"]), (2, 1, 1))


class ExhaustiveVerifierOracle(unittest.TestCase):
    def test_all_labelled_graphs_up_to_five_match_bruteforce(self):
        result = self_check()
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["target_checks"], 10810)


if __name__ == "__main__":
    unittest.main()
