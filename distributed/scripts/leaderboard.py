#!/usr/bin/env python3
"""Revalidate submissions, then build per-(r,s) corpus maxima, not global records."""
import argparse
import json
from pathlib import Path

from ingest import ingest_all


def build_board(ledger):
    pairs = {}
    for record in ledger["records"]:
        if record["status"] != "ACCEPTED" or not record["provenance_bound"] or record["verification"]["status"] != "PASS":
            continue
        claim = record["claim"]
        pair = (claim["r"], claim["s"])
        entry = pairs.setdefault(pair, {"r": pair[0], "s": pair[1], "accepted_submissions": [], "unique_witnesses": {}, "baseline_bounds": []})
        entry["accepted_submissions"].append(record["submission_id"])
        identity = record["canonical_graph_sha256"]
        witness = entry["unique_witnesses"].setdefault(identity, {"lower_bound": claim["lower_bound"], "submission_ids": []})
        witness["submission_ids"].append(record["submission_id"])
        if claim["kind"] == "known_baseline":
            entry["baseline_bounds"].append(claim["lower_bound"])
    result = []
    for pair, entry in sorted(pairs.items()):
        entry["best_verified_bound_in_corpus"] = max(w["lower_bound"] for w in entry["unique_witnesses"].values())
        entry["best_declared_baseline"] = max(entry.pop("baseline_bounds"), default=None)
        entry["unique_labelled_witness_count"] = len(entry["unique_witnesses"])
        entry["improvement_over_declared_baseline"] = None if entry["best_declared_baseline"] is None else entry["best_verified_bound_in_corpus"] - entry["best_declared_baseline"]
        result.append(entry)
    return {"schema_version": 1, "checked_at": ledger["checked_at"],
            "scope": "independently verified submitted corpus; no global-record or novelty assertion",
            "denominator": ledger["denominator"], "accepted": ledger["accepted"],
            "rejected": ledger["rejected"], "unknown": ledger["unknown"], "pairs": result}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("results/leaderboard.json"))
    parser.add_argument("--max-seconds", type=float, default=5)
    args = parser.parse_args()
    # Never trust a previous or contributor-edited ACCEPTED ledger.
    ledger = ingest_all(args.root.resolve(), args.max_seconds)
    board = build_board(ledger)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(board, indent=2) + "\n")
    print(json.dumps({"pairs": len(board["pairs"]), "accepted": board["accepted"], "unknown": board["unknown"], "rejected": board["rejected"]}))


if __name__ == "__main__":
    main()
