"""Shared exact bitset graph utilities for the finite Ramsey route."""

from __future__ import annotations

from pathlib import Path


def enumerate_cliques(
    adjacency: list[int],
    size: int,
    candidates: int | None = None,
    limit: int | None = None,
) -> list[int]:
    """Return size-cliques once as bit masks, optionally restricted/capped."""
    found: list[int] = []
    n = len(adjacency)

    def visit(prefix: int, remaining: int, need: int) -> None:
        if limit is not None and len(found) >= limit:
            return
        if need == 0:
            found.append(prefix)
            return
        while remaining.bit_count() >= need:
            bit = remaining & -remaining
            remaining ^= bit
            v = bit.bit_length() - 1
            visit(prefix | bit, remaining & adjacency[v], need - 1)
            if limit is not None and len(found) >= limit:
                return

    if candidates is None:
        candidates = (1 << n) - 1
    visit(0, candidates, size)
    return found


def add_vertex(rows: list[int], neighborhood: list[int]) -> list[int]:
    n = len(rows)
    result = rows.copy() + [0]
    for v in neighborhood:
        result[v] |= 1 << n
        result[n] |= 1 << v
    return result


def write_matrix(rows: list[int], path: Path) -> None:
    n = len(rows)
    text = "\n".join(
        " ".join("1" if (row >> j) & 1 else "0" for j in range(n))
        for row in rows
    )
    path.write_text(text + "\n", encoding="utf-8")
