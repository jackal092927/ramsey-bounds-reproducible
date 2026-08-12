#!/usr/bin/env python3
"""Independent exact checker for adjacency-matrix Ramsey certificates.

This checker deliberately does not import or call either certificate producer's
notebook.  It validates the matrix and uses a pure-Python bitset branch-and-bound
clique search.  Absence of K_r in G and K_s in the complement certifies that an
n-vertex input proves R(r, s) >= n + 1.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import time
from dataclasses import dataclass, asdict
from pathlib import Path


def read_matrix(path: Path) -> list[int]:
    raw = path.read_bytes()
    tokens = re.findall(rb"(?<!\d)[01](?!\d)", raw)
    n = math.isqrt(len(tokens))
    if n * n != len(tokens):
        raise ValueError(
            f"expected a square 0/1 matrix, found {len(tokens)} entries"
        )

    rows: list[int] = []
    for i in range(n):
        bits = 0
        for j, token in enumerate(tokens[i * n : (i + 1) * n]):
            if token == b"1":
                bits |= 1 << j
        rows.append(bits)

    for i, row in enumerate(rows):
        if (row >> i) & 1:
            raise ValueError(f"diagonal entry ({i},{i}) is 1")
        for j in range(i):
            if ((row >> j) & 1) != ((rows[j] >> i) & 1):
                raise ValueError(f"matrix is asymmetric at ({i},{j})")
    return rows


def complement(rows: list[int]) -> list[int]:
    mask = (1 << len(rows)) - 1
    return [(~row) & mask & ~(1 << i) for i, row in enumerate(rows)]


@dataclass
class SearchResult:
    target: int
    exists: bool
    witness: list[int] | None
    recursive_nodes: int
    colorings: int
    elapsed_seconds: float


class CliqueTargetSearch:
    """Tomita-style target clique search with greedy-color upper bounds."""

    def __init__(self, adjacency: list[int], target: int):
        self.adj = adjacency
        self.target = target
        self.nodes = 0
        self.colorings = 0
        self.answer: list[int] | None = None

    def _color_sort(self, candidates: int) -> tuple[list[int], list[int]]:
        """Greedily partition candidates into independent color classes.

        The returned prefix ending at position i has a clique upper bound of
        colors[i], which is the pruning invariant used by _expand.
        """
        self.colorings += 1
        order: list[int] = []
        bounds: list[int] = []
        remaining = candidates
        color = 0
        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                order.append(v)
                bounds.append(color)
                remaining ^= bit
                available ^= bit
                available &= ~self.adj[v]
        return order, bounds

    def _expand(self, clique: list[int], candidates: int) -> bool:
        self.nodes += 1
        need = self.target - len(clique)
        if need <= 0:
            self.answer = clique.copy()
            return True
        if candidates.bit_count() < need:
            return False

        order, bounds = self._color_sort(candidates)
        for i in range(len(order) - 1, -1, -1):
            if len(clique) + bounds[i] < self.target:
                return False
            v = order[i]
            bit = 1 << v
            if not (candidates & bit):
                continue
            clique.append(v)
            if self._expand(clique, candidates & self.adj[v]):
                return True
            clique.pop()
            candidates ^= bit
        return False

    def run(self, candidates: int | None = None) -> SearchResult:
        start = time.perf_counter()
        if candidates is None:
            candidates = (1 << len(self.adj)) - 1
        exists = self._expand([], candidates)
        return SearchResult(
            target=self.target,
            exists=exists,
            witness=self.answer,
            recursive_nodes=self.nodes,
            colorings=self.colorings,
            elapsed_seconds=time.perf_counter() - start,
        )


def edge_count(rows: list[int]) -> int:
    return sum(row.bit_count() for row in rows) // 2


def verify(path: Path, r: int, s: int) -> dict:
    raw = path.read_bytes()
    rows = read_matrix(path)
    comp = complement(rows)

    red_forbidden = CliqueTargetSearch(rows, r).run()
    blue_forbidden = CliqueTargetSearch(comp, s).run()
    # Positive boundary witnesses make the reported clique numbers exact when
    # both are found.  These are searches for r-1 and s-1, not assumptions.
    red_boundary = CliqueTargetSearch(rows, r - 1).run()
    blue_boundary = CliqueTargetSearch(comp, s - 1).run()

    valid = not red_forbidden.exists and not blue_forbidden.exists
    return {
        "input": str(path.resolve()),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "vertices": len(rows),
        "edges": edge_count(rows),
        "r": r,
        "s": s,
        "valid_ramsey_certificate": valid,
        "certified_lower_bound": len(rows) + 1 if valid else None,
        "omega_exact": r - 1
        if valid and red_boundary.exists
        else None,
        "alpha_exact": s - 1
        if valid and blue_boundary.exists
        else None,
        "searches": {
            "forbidden_clique": asdict(red_forbidden),
            "forbidden_independent_set": asdict(blue_forbidden),
            "boundary_clique": asdict(red_boundary),
            "boundary_independent_set": asdict(blue_boundary),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("r", type=int)
    parser.add_argument("s", type=int)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.r < 2 or args.s < 2:
        parser.error("r and s must be at least 2")
    result = verify(args.matrix, args.r, args.s)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")
    raise SystemExit(0 if result["valid_ramsey_certificate"] else 1)


if __name__ == "__main__":
    main()
