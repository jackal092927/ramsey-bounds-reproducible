"""Unit tests for resumable exact-budget-six helpers."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from .r3_18_budget6_branch import json_safe, load_resume_masks


class R318Budget6Tests(unittest.TestCase):
    def test_resume_union_is_stable_and_deduplicated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            a = root / "a.json"
            b = root / "b.json"
            a.write_text(json.dumps({"all_lazy_masks": [7, 11, 13]}))
            b.write_text(
                json.dumps({"last_checkpoint": {"all_lazy_masks": [11, 17]}})
            )
            self.assertEqual(load_resume_masks([a, b]), [7, 11, 13, 17])

    def test_json_safe_decodes_nested_bytes(self) -> None:
        self.assertEqual(
            json_safe({"tail": [b"ok", {"bad": b"\xff"}]}),
            {"tail": ["ok", {"bad": "\ufffd"}]},
        )


if __name__ == "__main__":
    unittest.main()
