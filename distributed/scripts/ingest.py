#!/usr/bin/env python3
"""Validate provenance bytes and independently verify every submitted graph.

Standard-library-only; never executes submitted producers or downloads files.
The leaderboard calls this validator again rather than trusting edited ledgers.
"""
from __future__ import annotations

import argparse
import copy
import datetime
import hashlib
import json
import math
import re
from pathlib import Path

from verify_certificate import read_matrix, verify


class Rejection(ValueError):
    pass


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise Rejection(message)


def exact_keys(obj, keys, label):
    require(isinstance(obj, dict) and set(obj) == set(keys), f"{label}: missing or unexpected fields")


def integer(value, minimum, maximum, label):
    require(type(value) is int and minimum <= value <= maximum, f"{label}: invalid integer")


def finite_number(value, minimum, label):
    require(type(value) in (float, int) and math.isfinite(value) and value >= minimum,
            f"{label}: invalid finite number")


def safe_path(root, relative):
    require(isinstance(relative, str) and relative and not Path(relative).is_absolute(), "path must be relative")
    require(".." not in Path(relative).parts, "parent traversal is forbidden")
    target = (root / relative).resolve()
    require(target.is_relative_to(root.resolve()), "path escapes project root")
    require(target.is_file(), f"missing file: {relative}")
    require(target.stat().st_size <= 4_000_000, f"file exceeds intake limit: {relative}")
    return target


def bound_file(root, descriptor, label):
    exact_keys(descriptor, ("path", "sha256"), label)
    require(isinstance(descriptor["sha256"], str) and re.fullmatch(r"[0-9a-f]{64}", descriptor["sha256"]), f"{label}: invalid hash")
    path = safe_path(root, descriptor["path"])
    require(sha256(path) == descriptor["sha256"], f"{label}: source hash mismatch")
    return path


def load_json(path):
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=unique_object)


def same_json(first, second):
    return json.dumps(first, sort_keys=True, allow_nan=False) == json.dumps(second, sort_keys=True, allow_nan=False)


def validate_submission(root, submission, max_seconds=5.0):
    require(math.isfinite(max_seconds) and max_seconds > 0, "positive verification budget required")
    exact_keys(submission, ("schema_version", "submission_id", "claim", "certificate", "provenance"), "submission")
    require(type(submission["schema_version"]) is int and submission["schema_version"] == 1, "unsupported schema version")
    require(isinstance(submission["submission_id"], str) and re.fullmatch(r"[a-z0-9][a-z0-9-]{2,79}", submission["submission_id"]), "invalid submission id")
    claim = submission["claim"]
    exact_keys(claim, ("r", "s", "n", "lower_bound", "kind"), "claim")
    integer(claim["r"], 2, 20, "r")
    integer(claim["s"], 2, 20, "s")
    integer(claim["n"], 1, 600, "n")
    require(type(claim["lower_bound"]) is int and claim["lower_bound"] == claim["n"] + 1, "lower bound must be n+1")
    require(claim["kind"] in ("known_baseline", "candidate"), "unknown claim kind")
    certificate = bound_file(root, submission["certificate"], "certificate")
    provenance = submission["provenance"]
    exact_keys(provenance, ("origin", "source_manifest", "seeds", "run_receipt", "budget"), "provenance")
    origin = provenance["origin"]
    exact_keys(origin, ("repository", "revision", "attribution", "license_path"), "origin")
    require(origin["repository"] is None or (isinstance(origin["repository"], str) and origin["repository"].startswith("https://")), "repository must be null or an HTTPS URL")
    require(isinstance(origin["revision"], str) and origin["revision"], "missing source revision")
    require(isinstance(origin["attribution"], str) and origin["attribution"], "missing attribution")
    safe_path(root, origin["license_path"])
    source_manifest = bound_file(root, provenance["source_manifest"], "source manifest")
    source = load_json(source_manifest)
    exact_keys(source, ("schema_version", "files"), "source manifest")
    require(type(source["schema_version"]) is int and source["schema_version"] == 1 and isinstance(source["files"], list) and source["files"], "empty source manifest")
    source_paths = []
    for item in source["files"]:
        bound_file(root, item, "producer source")
        source_paths.append(item["path"])
    require(len(set(source_paths)) == len(source_paths), "duplicate source manifest path")
    require(isinstance(provenance["seeds"], list) and provenance["seeds"], "missing seed provenance")
    for seed in provenance["seeds"]:
        bound_file(root, seed, "seed")
    budget = provenance["budget"]
    exact_keys(budget, ("wall_seconds", "cpu_count"), "budget")
    finite_number(budget["wall_seconds"], 0.000001, "wall budget")
    integer(budget["cpu_count"], 1, 4096, "cpu count")
    receipt = load_json(bound_file(root, provenance["run_receipt"], "run receipt"))
    exact_keys(receipt, ("schema_version", "submission_id", "claim", "certificate_sha256", "source_manifest_sha256", "seed_sha256", "budget", "observed"), "run receipt")
    require(type(receipt["schema_version"]) is int and receipt["schema_version"] == 1 and receipt["submission_id"] == submission["submission_id"], "run identity mismatch")
    require(same_json(receipt["claim"], claim), "run objective mismatch")
    require(receipt["certificate_sha256"] == submission["certificate"]["sha256"], "run certificate hash mismatch")
    require(receipt["source_manifest_sha256"] == provenance["source_manifest"]["sha256"], "run source manifest mismatch")
    require(receipt["seed_sha256"] == [seed["sha256"] for seed in provenance["seeds"]], "run seed hash mismatch")
    require(same_json(receipt["budget"], budget), "run budget mismatch")
    observed = receipt["observed"]
    exact_keys(observed, ("status", "exit_code", "elapsed_seconds"), "run observation")
    require(observed["status"] == "COMPLETED" and type(observed["exit_code"]) is int and observed["exit_code"] == 0, "run did not complete successfully")
    finite_number(observed["elapsed_seconds"], 0, "run elapsed time")
    require(observed["elapsed_seconds"] <= budget["wall_seconds"], "reported run exceeds wall budget")
    rows = read_matrix(certificate)
    require(len(rows) == claim["n"], "matrix order differs from claim")
    check = verify(certificate, claim["r"], claim["s"], max_seconds)
    canonical = "\n".join("".join("1" if row & (1 << j) else "0" for j in range(len(rows))) for row in rows) + "\n"
    status = {"PASS": "ACCEPTED", "FAIL": "REJECTED", "UNKNOWN": "UNKNOWN"}[check["status"]]
    return {"submission_id": submission["submission_id"], "claim": copy.deepcopy(claim),
            "status": status, "reason": {"PASS": "VERIFIED_WITNESS", "FAIL": "FORBIDDEN_CLIQUE", "UNKNOWN": "VERIFICATION_DEADLINE"}[check["status"]],
            "provenance_bound": True, "certificate_sha256": submission["certificate"]["sha256"],
            "canonical_graph_sha256": hashlib.sha256(canonical.encode()).hexdigest(),
            "verification": check, "is_global_record": None}


def ingest_all(root, max_seconds=5.0):
    records, identifiers = [], set()
    paths = sorted((root / "submissions").glob("*.json"))
    require(paths, "no submissions found")
    for path in paths:
        try:
            submission = load_json(path)
            record = validate_submission(root, submission, max_seconds)
            require(record["submission_id"] not in identifiers, "duplicate submission id")
            identifiers.add(record["submission_id"])
        except (ValueError, OSError, TypeError, KeyError, OverflowError) as error:
            record = {"submission_id": path.stem, "status": "REJECTED", "reason": str(error), "provenance_bound": False}
        record["submission_path"] = str(path.relative_to(root))
        records.append(record)
    return {"schema_version": 1, "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "validator_sha256": sha256(Path(__file__)), "verification_budget_per_submission_seconds": max_seconds,
            "records": records, "denominator": len(records),
            "accepted": sum(r["status"] == "ACCEPTED" for r in records),
            "unknown": sum(r["status"] == "UNKNOWN" for r in records),
            "rejected": sum(r["status"] == "REJECTED" for r in records)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("results/ingest.json"))
    parser.add_argument("--max-seconds", type=float, default=5)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    require(math.isfinite(args.max_seconds) and args.max_seconds > 0, "positive verification budget required")
    result = ingest_all(args.root.resolve(), args.max_seconds)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("denominator", "accepted", "unknown", "rejected")}))
    raise SystemExit(1 if args.strict and result["accepted"] != result["denominator"] else 0)


if __name__ == "__main__":
    main()
