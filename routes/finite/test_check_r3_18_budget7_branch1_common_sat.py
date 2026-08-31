from __future__ import annotations

import gzip
import tempfile
import unittest
from pathlib import Path

from .check_r3_18_budget7_branch1_common_sat import (
    AuditError,
    _literal_true,
    parse_complete_model,
)


class CommonSatWitnessCheckerTests(unittest.TestCase):
    def _model(self, text: str) -> Path:
        root = Path(tempfile.mkdtemp(prefix="ramsey-common-model-test-"))
        path = root / "model.gz"
        with path.open("wb") as raw:
            with gzip.GzipFile(
                filename="", mode="wb", fileobj=raw, mtime=0
            ) as sink:
                sink.write(text.encode("ascii"))
        # ``unittest`` runs cleanups in LIFO order: register the directory
        # first so that the compressed model is removed before ``rmdir``.
        self.addCleanup(lambda: root.rmdir())
        self.addCleanup(lambda: path.unlink(missing_ok=True))
        return path

    def test_complete_model_is_accepted(self) -> None:
        assignment, info = parse_complete_model(
            self._model("s SATISFIABLE\nv 1 -2\nv 3 0\n"), 3
        )
        self.assertEqual(assignment, [None, True, False, True])
        self.assertEqual(info["assignment_literals"], 3)
        self.assertTrue(_literal_true(1, assignment))
        self.assertTrue(_literal_true(-2, assignment))
        self.assertFalse(_literal_true(2, assignment))

    def test_duplicate_or_missing_variable_fails(self) -> None:
        for text in (
            "s SATISFIABLE\nv 1 -1 2 0\n",
            "s SATISFIABLE\nv 1 3 0\n",
        ):
            with self.subTest(text=text), self.assertRaises(AuditError):
                parse_complete_model(self._model(text), 3)

    def test_status_and_zero_terminator_are_strict(self) -> None:
        for text in (
            "s SAT\nv 1 2 3 0\n",
            "s SATISFIABLE\nv 1 0 2 3\n",
            "s SATISFIABLE\nv 1 2 3\n",
            "s SATISFIABLE\nc comment\nv 1 2 3 0\n",
        ):
            with self.subTest(text=text), self.assertRaises(AuditError):
                parse_complete_model(self._model(text), 3)

    def test_out_of_range_literal_fails(self) -> None:
        with self.assertRaises(AuditError):
            parse_complete_model(
                self._model("s SATISFIABLE\nv 1 2 4 0\n"), 3
            )


if __name__ == "__main__":
    unittest.main()
