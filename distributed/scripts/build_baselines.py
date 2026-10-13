#!/usr/bin/env python3
"""Materialize two explicitly known baselines and actual replay receipts.

The external certificate is included with its pinned primary-source metadata
and CC BY 4.0 license. This command performs no download and makes no new-record
claim. Regeneration changes run timings and therefore receipt hashes.
"""
import hashlib
import json
from pathlib import Path

from verify_certificate import verify

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(relative, value):
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")
    return {"path": relative, "sha256": digest(path)}


def describe(relative):
    return {"path": relative, "sha256": digest(ROOT / relative)}


def main():
    (ROOT / "certificates").mkdir(exist_ok=True)
    c5 = [["0"] * 5 for _ in range(5)]
    for i in range(5):
        c5[i][(i + 1) % 5] = c5[(i + 1) % 5][i] = "1"
    (ROOT / "certificates/c5.txt").write_text("\n".join("".join(row) for row in c5) + "\n")
    external = ROOT / "upstream/cremer/n134-gpt-6.1-sol.txt"
    assert digest(external) == "8ef378ad4d66478c33939e438d3a64572ec2cf7d1647ae29d3568817fedfc982"
    (ROOT / "certificates/cremer-r6s8-n134.txt").write_bytes(external.read_bytes())
    source_manifest = write_json("evidence/source-manifest.json", {
        "schema_version": 1,
        "files": [describe("scripts/build_baselines.py"), describe("scripts/verify_certificate.py"),
                  describe("upstream/cremer/SOURCE.json"), describe("upstream/cremer/LICENSE"),
                  describe("upstream/cremer/README.md"), describe("upstream/cremer/n134-gpt-6.1-sol.txt")],
    })
    examples = [
        ("known-c5-r3s3", 3, 3, 5, "certificates/c5.txt",
         {"repository": None, "revision": "local-cycle-construction-v1", "attribution": "Known cycle C5; deterministic toy fixture, not a new Ramsey result", "license_path": "LICENSE_CODE.md"}),
        ("known-cremer-r6s8-n134", 6, 8, 134, "certificates/cremer-r6s8-n134.txt",
         {"repository": "https://github.com/fritzcremer/ramsey-lower-bounds", "revision": "9382a5eb8e6ec634873cea0850b133764e0eecbf", "attribution": "Fritz Cremer, arXiv:2610.12122v1; existing witness independently replayed", "license_path": "upstream/cremer/LICENSE"}),
    ]
    for identifier, r, s, n, relative, origin in examples:
        claim = {"r": r, "s": s, "n": n, "lower_bound": n + 1, "kind": "known_baseline"}
        descriptor = describe(relative)
        result = verify(ROOT / relative, r, s, 5)
        assert result["status"] == "PASS"
        budget = {"wall_seconds": 5, "cpu_count": 1}
        receipt = write_json(f"evidence/runs/{identifier}.json", {
            "schema_version": 1, "submission_id": identifier, "claim": claim,
            "certificate_sha256": descriptor["sha256"], "source_manifest_sha256": source_manifest["sha256"],
            "seed_sha256": [descriptor["sha256"]], "budget": budget,
            "observed": {"status": "COMPLETED", "exit_code": 0, "elapsed_seconds": result["elapsed_seconds"]},
        })
        write_json(f"evidence/checks/{identifier}.json", result)
        write_json(f"submissions/{identifier}.json", {
            "schema_version": 1, "submission_id": identifier, "claim": claim,
            "certificate": descriptor,
            "provenance": {"origin": origin, "source_manifest": source_manifest, "seeds": [descriptor],
                           "run_receipt": receipt, "budget": budget},
        })
        print(identifier, "known baseline PASS")


if __name__ == "__main__":
    main()
