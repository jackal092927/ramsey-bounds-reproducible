from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from routes.finite.check_r3_18_budget7_branch1_maximal_union_probe import (
    AuditError,
    audit,
)


HERE = Path(__file__).resolve().parent
RECORD = HERE / "r3_18_budget7_branch1_maximal_union_probe.json"
ARTIFACTS = HERE / "certificates" / "r3_18_budget7_branch1_maximal_union_probe"


class MaximalUnionProbeAuditTests(unittest.TestCase):
    def test_frozen_endpoint_passes(self) -> None:
        result = audit(RECORD, ARTIFACTS)
        self.assertEqual(
            result["status"], "VERIFIED_MAXIMAL_UNION_TIMEOUT_UNKNOWN_ENDPOINT"
        )
        self.assertEqual(result["claim"], "UNKNOWN_NO_CUT_NO_BRANCH_CLOSURE")

    def test_retained_proof_prefix_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            copy = Path(name) / "artifacts"
            shutil.copytree(ARTIFACTS, copy)
            (copy / "solver_proof.drat").write_bytes(b"not a certificate\n")
            with self.assertRaisesRegex(AuditError, "must not be retained"):
                audit(RECORD, copy)

    def test_promoted_claim_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            record = Path(name) / "record.json"
            payload = json.loads(RECORD.read_text(encoding="ascii"))
            payload["claim_boundary"]["branch1_closed"] = True
            record.write_text(
                json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="ascii"
            )
            with self.assertRaisesRegex(AuditError, "promoted"):
                audit(record, ARTIFACTS)


if __name__ == "__main__":
    unittest.main()
