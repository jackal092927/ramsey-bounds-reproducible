#!/usr/bin/env python3
"""Bounded exact Ramsey witness verifier, independent of the producer's code.

Input is a labelled adjacency matrix (compact or space-separated). PASS proves
only that this concrete n-vertex graph certifies R(r,s) >= n+1. UNKNOWN never
certifies a bound. Standard bitset branch-and-bound with greedy coloring.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import time
from pathlib import Path


def read_matrix(path: Path) -> list[int]:
    lines = ["".join(line.split()) for line in path.read_text().splitlines() if line.strip()]
    n = len(lines)
    if not n or any(len(row) != n or set(row) - {"0", "1"} for row in lines):
        raise ValueError("expected a nonempty square 0/1 adjacency matrix")
    if any(row[i] != "0" for i, row in enumerate(lines)):
        raise ValueError("nonzero diagonal")
    if any(lines[i][j] != lines[j][i] for i in range(n) for j in range(i)):
        raise ValueError("asymmetric adjacency matrix")
    return [sum(1 << j for j, bit in enumerate(row) if bit == "1") for row in lines]


def complement(rows: list[int]) -> list[int]:
    mask = (1 << len(rows)) - 1
    return [(mask ^ row) & ~(1 << i) for i, row in enumerate(rows)]


def find_clique(rows: list[int], target: int, deadline: float) -> dict:
    nodes = 0
    started = time.monotonic()

    def recurse(chosen: list[int], candidates: int):
        nonlocal nodes
        nodes += 1
        if nodes % 1024 == 1 and time.monotonic() >= deadline:
            raise TimeoutError
        need = target - len(chosen)
        if need == 0:
            return chosen
        if candidates.bit_count() < need:
            return None
        remaining = candidates
        order, bounds = [], []
        color = 0
        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                vertex = bit.bit_length() - 1
                remaining ^= bit
                available &= ~bit & ~rows[vertex]
                order.append(vertex)
                bounds.append(color)
        for vertex, upper_bound in zip(reversed(order), reversed(bounds)):
            if upper_bound < need:
                break
            bit = 1 << vertex
            result = recurse(chosen + [vertex], candidates & rows[vertex])
            if result is not None:
                return result
            candidates ^= bit
        return None

    try:
        witness = recurse([], (1 << len(rows)) - 1)
        status = "PRESENT" if witness is not None else "ABSENT"
    except TimeoutError:
        witness, status = None, "UNKNOWN"
    return {"target": target, "status": status, "witness": witness,
            "nodes": nodes, "elapsed_seconds": time.monotonic() - started}


def verify(path: Path, r: int, s: int, max_seconds: float) -> dict:
    started = time.monotonic()
    deadline = started + max_seconds
    raw = path.read_bytes()
    rows = read_matrix(path)
    red = find_clique(rows, r, deadline)
    blue = find_clique(complement(rows), s, deadline)
    statuses = {red["status"], blue["status"]}
    status = "FAIL" if "PRESENT" in statuses else ("UNKNOWN" if "UNKNOWN" in statuses else "PASS")
    return {"schema_version": 1, "status": status, "r": r, "s": s,
            "vertices": len(rows), "edges": sum(x.bit_count() for x in rows) // 2,
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "certified_lower_bound": len(rows) + 1 if status == "PASS" else None,
            "searches": {"red_clique": red, "blue_clique": blue},
            "budget_seconds": max_seconds, "elapsed_seconds": time.monotonic() - started}


def self_check() -> dict:
    # Exhaustive independent oracle: all labelled graphs through n=5; every
    # forbidden target is evaluated directly over combinations of vertices.
    cases = 0
    for n in range(1, 6):
        edges = list(itertools.combinations(range(n), 2))
        for mask in range(1 << len(edges)):
            rows = [0] * n
            for j, (u, v) in enumerate(edges):
                if mask & (1 << j):
                    rows[u] |= 1 << v
                    rows[v] |= 1 << u
            for adjacency in (rows, complement(rows)):
                for target in range(2, n + 2):
                    expected = any(all(adjacency[u] & (1 << v)
                                       for u, v in itertools.combinations(vertices, 2))
                                   for vertices in itertools.combinations(range(n), target))
                    actual = find_clique(adjacency, target, time.monotonic() + 10)
                    assert actual["status"] == ("PRESENT" if expected else "ABSENT")
                    if actual["witness"]:
                        assert all(adjacency[u] & (1 << v)
                                   for u, v in itertools.combinations(actual["witness"], 2))
                    cases += 1
    return {"status": "PASS", "exhaustive_graph_orders": [1, 2, 3, 4, 5], "target_checks": cases}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path, nargs="?")
    parser.add_argument("r", type=int, nargs="?")
    parser.add_argument("s", type=int, nargs="?")
    parser.add_argument("--max-seconds", type=float, default=60)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        result = self_check()
    else:
        if args.matrix is None or args.r is None or args.s is None or min(args.r, args.s) < 2 or args.max_seconds <= 0:
            parser.error("matrix, r>=2, s>=2 and positive --max-seconds are required")
        result = verify(args.matrix, args.r, args.s, args.max_seconds)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(rendered, end="")
    if args.json:
        args.json.write_text(rendered)
    raise SystemExit({"PASS": 0, "FAIL": 1, "UNKNOWN": 2}[result["status"]])


if __name__ == "__main__":
    main()
