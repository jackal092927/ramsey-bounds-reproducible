#!/usr/bin/env python3
"""Exact small-instance scan of the Ramsey-coloring reconfiguration graph.

A state is a red/blue coloring of the edges of K_n with no monochromatic
triangle.  Two states are adjacent when they differ on exactly one edge and
the resulting coloring is still valid.  The script uses exhaustive integer
bit masks, so its output is an exact finite computation rather than a quantum
simulation.

This is intentionally limited to n <= 6.  It is a kill test for the tempting
idea of running a quantum walk only on valid colorings with single-edge moves.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, deque


def edge_index(n: int) -> tuple[tuple[int, int], dict[tuple[int, int], int]]:
    edges = tuple(itertools.combinations(range(n), 2))
    return edges, {edge: index for index, edge in enumerate(edges)}


def triangle_masks(n: int) -> tuple[int, ...]:
    _, index = edge_index(n)
    masks = []
    for a, b, c in itertools.combinations(range(n), 3):
        masks.append(
            (1 << index[(a, b)])
            | (1 << index[(a, c)])
            | (1 << index[(b, c)])
        )
    return tuple(masks)


def is_valid(mask: int, triangles: tuple[int, ...]) -> bool:
    return all(mask & tri not in (0, tri) for tri in triangles)


def valid_colorings(n: int) -> tuple[int, ...]:
    edges, _ = edge_index(n)
    triangles = triangle_masks(n)
    return tuple(
        mask
        for mask in range(1 << len(edges))
        if is_valid(mask, triangles)
    )


def component_sizes(states: tuple[int, ...], edge_count: int) -> tuple[list[int], int, Counter[int]]:
    state_set = set(states)
    adjacency: dict[int, list[int]] = {}
    for state in states:
        adjacency[state] = [
            state ^ (1 << edge)
            for edge in range(edge_count)
            if state ^ (1 << edge) in state_set
        ]

    unseen = set(states)
    sizes: list[int] = []
    while unseen:
        root = next(iter(unseen))
        unseen.remove(root)
        queue = deque([root])
        size = 0
        while queue:
            state = queue.popleft()
            size += 1
            for neighbor in adjacency[state]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
        sizes.append(size)

    undirected_edges = sum(map(len, adjacency.values())) // 2
    degree_histogram = Counter(map(len, adjacency.values()))
    return sorted(sizes, reverse=True), undirected_edges, degree_histogram


def summarize(n: int) -> dict[str, object]:
    edges, _ = edge_index(n)
    states = valid_colorings(n)
    sizes, reconfiguration_edges, degree_histogram = component_sizes(states, len(edges))
    minimum_interstate_distance = (
        min(
            (left ^ right).bit_count()
            for index, left in enumerate(states)
            for right in states[index + 1 :]
        )
        if len(states) >= 2
        else None
    )
    return {
        "n": n,
        "edge_variables": len(edges),
        "valid_colorings": len(states),
        "reconfiguration_edges": reconfiguration_edges,
        "components": len(sizes),
        "component_sizes": sizes,
        "degree_histogram": {str(k): v for k, v in sorted(degree_histogram.items())},
        "minimum_interstate_hamming_distance": minimum_interstate_distance,
    }


def self_check() -> None:
    n5 = summarize(5)
    assert n5["valid_colorings"] == 12
    assert n5["components"] == 12
    assert n5["reconfiguration_edges"] == 0
    assert n5["degree_histogram"] == {"0": 12}
    assert n5["minimum_interstate_hamming_distance"] == 4

    n6 = summarize(6)
    assert n6["valid_colorings"] == 0
    assert n6["components"] == 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-n", type=int, default=3)
    parser.add_argument("--max-n", type=int, default=6)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()

    if not 1 <= args.min_n <= args.max_n <= 6:
        parser.error("require 1 <= min-n <= max-n <= 6")
    if args.self_check:
        self_check()

    print(json.dumps([summarize(n) for n in range(args.min_n, args.max_n + 1)], indent=2))


if __name__ == "__main__":
    main()
