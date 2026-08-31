#!/usr/bin/env python3
"""Unit and CLI regression tests for strict artifact-manifest handling."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from artifact_manifest import ManifestFormatError, load_manifest


ROOT = Path(__file__).resolve().parents[1]
CURRENT_MANIFEST = ROOT / "artifacts" / "MANIFEST.tsv"
VERIFY = ROOT / "scripts" / "verify_artifacts.py"
ZERO_SHA256 = "0" * 64


class ArtifactManifestParserTests(unittest.TestCase):
    def parse_text(self, text: str):
        with tempfile.TemporaryDirectory(prefix="ramsey-manifest-parser-") as tmp:
            path = Path(tmp) / "MANIFEST.tsv"
            path.write_text(text, encoding="utf-8")
            return load_manifest(path)

    def assert_rejected(self, text: str, message: str) -> None:
        with self.assertRaisesRegex(ManifestFormatError, message):
            self.parse_text(text)

    def test_current_manifest_is_valid(self) -> None:
        entries = load_manifest(CURRENT_MANIFEST)
        self.assertGreater(len(entries), 0)
        self.assertEqual(len(entries), len({entry.name for entry in entries}))
        self.assertTrue(all(entry.size >= 0 for entry in entries))

    def test_comments_and_blank_lines_are_ignored(self) -> None:
        entries = self.parse_text(
            f"# sha256<TAB>size<TAB>name\n\n{ZERO_SHA256}\t0\tasset.bin\n"
        )
        self.assertEqual(entries, [(ZERO_SHA256, 0, "asset.bin")])

    def test_each_data_line_requires_exactly_three_fields(self) -> None:
        for text in (
            f"{ZERO_SHA256}\t0\n",
            f"{ZERO_SHA256}\t0\ta.bin\textra\n",
        ):
            with self.subTest(text=text):
                self.assert_rejected(text, "exactly three")

    def test_duplicate_name_is_rejected(self) -> None:
        self.assert_rejected(
            f"{ZERO_SHA256}\t0\ta.bin\n{ZERO_SHA256}\t1\ta.bin\n",
            "duplicate artifact name",
        )

    def test_unsafe_basename_is_rejected(self) -> None:
        unsafe_names = (
            "../escape",
            "subdir/asset",
            r"subdir\asset",
            "/absolute",
            ".",
            "..",
            "-option",
            "white space",
            ".hidden",
            "café.bin",
        )
        for name in unsafe_names:
            with self.subTest(name=name):
                self.assert_rejected(
                    f"{ZERO_SHA256}\t0\t{name}\n", "unsafe artifact basename"
                )

    def test_bad_sha256_is_rejected(self) -> None:
        bad_hashes = ("0" * 63, "0" * 65, "A" * 64, "g" * 64, "")
        for checksum in bad_hashes:
            with self.subTest(checksum=checksum):
                self.assert_rejected(
                    f"{checksum}\t0\ta.bin\n", "64 lowercase hex digits"
                )

    def test_bad_size_is_rejected(self) -> None:
        for size in ("-1", "+1", "1.0", " 1", "1 ", ""):
            with self.subTest(size=size):
                self.assert_rejected(
                    f"{ZERO_SHA256}\t{size}\ta.bin\n", "non-negative decimal"
                )


class VerifyArtifactsExactTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory(
            prefix="ramsey-artifact-verifier-"
        )
        self.root = Path(self.temporary_directory.name)
        self.assets = self.root / "assets"
        self.assets.mkdir()
        self.manifest = self.root / "MANIFEST.tsv"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def write_expected_asset(self) -> Path:
        content = b"proof-certificate\n"
        asset = self.assets / "certificate.drat.gz"
        asset.write_bytes(content)
        checksum = hashlib.sha256(content).hexdigest()
        self.manifest.write_text(
            f"{checksum}\t{len(content)}\t{asset.name}\n", encoding="utf-8"
        )
        return asset

    def run_verifier(self, *extra_args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(VERIFY),
                "--directory",
                str(self.assets),
                "--manifest",
                str(self.manifest),
                *extra_args,
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_existing_files_pass_exact_verification(self) -> None:
        self.write_expected_asset()
        result = self.run_verifier("--exact")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS certificate.drat.gz", result.stdout)
        self.assertIn("EXACT_ARTIFACT_MANIFEST_VERIFIED", result.stdout)

    def test_exact_rejects_extra_file(self) -> None:
        self.write_expected_asset()
        (self.assets / "extra.bin").write_bytes(b"not in the manifest")
        result = self.run_verifier("--exact")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("UNEXPECTED extra.bin", result.stdout + result.stderr)

    def test_exact_rejects_missing_file(self) -> None:
        asset = self.write_expected_asset()
        asset.unlink()
        result = self.run_verifier("--exact")
        self.assertNotEqual(result.returncode, 0)
        output = result.stdout + result.stderr
        self.assertEqual(output.count("MISSING certificate.drat.gz"), 1, output)

    def test_invalid_manifest_fails_before_artifact_verification(self) -> None:
        self.manifest.write_text(
            f"{ZERO_SHA256}\t0\t../escape\n", encoding="utf-8"
        )
        result = self.run_verifier("--exact")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("INVALID_MANIFEST", result.stdout + result.stderr)
        self.assertIn("unsafe artifact basename", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
