#!/usr/bin/env python3
"""Exact small-field diagnostics for quotients of Bradač's full W-state.

This checker has two deliberately separate jobs.

* It verifies that the projective orthogonal action gives an exact orbit
  quotient of the pair-labelled transition operator.
* It tests the much smaller rank/self-incidence profile.  That profile
  determines the present legal fanout exactly, but need not determine the
  distribution of successor profiles.

Only prime fields are implemented.  The t=2,q=2 run is over the complete
reachable state graph.  For q=3 the default is a bounded-depth diagnostic,
not an asymptotic argument.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from functools import lru_cache
from itertools import product
from typing import Iterable

from cross_type_transfer_check import Explorer, State, contains, normalize, rref


Matrix = tuple[tuple[int, ...], ...]


def mat_vec(matrix: Matrix, vector: tuple[int, ...], q: int) -> tuple[int, ...]:
    return tuple(
        sum(matrix[i][j] * vector[j] for j in range(len(vector))) % q
        for i in range(len(vector))
    )


def dot(x: tuple[int, ...], y: tuple[int, ...], q: int) -> int:
    return sum(a * b for a, b in zip(x, y, strict=True)) % q


def orthogonal_matrices(dim: int, q: int) -> tuple[Matrix, ...]:
    """Enumerate A with A^T A=I; intended only for dim=3,q in {2,3}."""
    vectors = tuple(product(range(q), repeat=dim))
    matrices: list[Matrix] = []
    for columns in product(vectors, repeat=dim):
        if any(
            dot(columns[i], columns[j], q) != int(i == j)
            for i in range(dim)
            for j in range(dim)
        ):
            continue
        matrix = tuple(
            tuple(columns[j][i] for j in range(dim)) for i in range(dim)
        )
        matrices.append(matrix)
    return tuple(matrices)


def projective_action_representatives(
    explorer: Explorer,
) -> tuple[tuple[Matrix, tuple[int, ...]], ...]:
    """Deduplicate scalar-equivalent matrices by their point permutation."""
    actions: dict[tuple[int, ...], Matrix] = {}
    for matrix in orthogonal_matrices(explorer.t + 1, explorer.q):
        permutation = tuple(
            explorer.point_index[
                normalize(mat_vec(matrix, point, explorer.q), explorer.q)
            ]
            for point in explorer.points
        )
        actions.setdefault(permutation, matrix)
    return tuple(
        (matrix, permutation) for permutation, matrix in sorted(actions.items())
    )


def act_state(
    explorer: Explorer,
    state: State,
    matrix: Matrix,
    permutation: tuple[int, ...],
) -> State:
    out: list[tuple[tuple[int, ...], ...] | None] = [None] * len(state)
    for old_i, space in enumerate(state):
        transformed = rref(
            (mat_vec(matrix, vector, explorer.q) for vector in space),
            explorer.q,
            explorer.t + 1,
        )
        out[permutation[old_i]] = transformed
    assert all(space is not None for space in out)
    return tuple(space for space in out if space is not None)


def q_integer(dimension: int, q: int) -> int:
    if dimension < 0:
        raise ValueError("negative projective dimension")
    return (q**dimension - 1) // (q - 1)


def self_incidence_profile(explorer: Explorer, state: State) -> tuple[int, ...]:
    """Counts M_{r,e}, ordered by rank r and e=0,1."""
    counts = Counter()
    for point, space in zip(explorer.points, state, strict=True):
        rank = len(space)
        is_contained = int(contains(space, point, explorer.q, explorer.t + 1))
        counts[rank, is_contained] += 1
    return tuple(
        counts[rank, is_contained]
        for rank in range(explorer.t + 2)
        for is_contained in (0, 1)
    )


def fanout_from_profile(explorer: Explorer, profile: tuple[int, ...]) -> int:
    total = 0
    for rank in range(explorer.t + 2):
        for is_contained in (0, 1):
            count = profile[2 * rank + is_contained]
            if count:
                total += count * q_integer(
                    explorer.t - rank + is_contained, explorer.q
                )
    return total


def reachable_complete(explorer: Explorer, max_states: int) -> list[State]:
    states = [explorer.zero]
    seen = {explorer.zero}
    queue = deque([explorer.zero])
    while queue:
        state = queue.popleft()
        for child in explorer.transitions(state):
            if child in seen:
                continue
            if len(states) >= max_states:
                raise RuntimeError(f"state cap {max_states} reached")
            seen.add(child)
            states.append(child)
            queue.append(child)
    return states


def reachable_to_depth(explorer: Explorer, depth: int) -> tuple[list[State], list[int]]:
    seen = {explorer.zero}
    states = [explorer.zero]
    frontier = [explorer.zero]
    level_sizes = [1]
    for _ in range(depth):
        nxt: list[State] = []
        for state in frontier:
            for child in explorer.transitions(state):
                if child in seen:
                    continue
                seen.add(child)
                states.append(child)
                nxt.append(child)
        frontier = nxt
        level_sizes.append(len(frontier))
    return states, level_sizes


def successor_signature(explorer: Explorer, state: State, key) -> tuple:
    counts: Counter[tuple] = Counter()
    for child, multiplicity in explorer.transitions(state).items():
        counts[key(child)] += multiplicity
    return tuple(sorted(counts.items()))


def first_lumping_failure(explorer: Explorer, states: Iterable[State], key):
    first: dict[tuple, tuple[int, tuple]] = {}
    for index, state in enumerate(states):
        state_key = key(state)
        signature = successor_signature(explorer, state, key)
        if state_key in first and first[state_key][1] != signature:
            old_index, old_signature = first[state_key]
            return old_index, index, state_key, old_signature, signature
        first.setdefault(state_key, (index, signature))
    return None


def check_fanout_formula(explorer: Explorer, states: Iterable[State]) -> None:
    for index, state in enumerate(states):
        profile = self_incidence_profile(explorer, state)
        predicted = fanout_from_profile(explorer, profile)
        actual = sum(explorer.transitions(state).values())
        if predicted != actual:
            raise AssertionError((index, predicted, actual, profile))


def check_explicit_q2_counterexample(explorer: Explorer) -> None:
    if (explorer.t, explorer.q) != (2, 2):
        return
    histories = (
        (
            ((0, 0, 1), (0, 1, 0)),
            ((0, 1, 0), (0, 0, 1)),
            ((1, 0, 0), (0, 1, 1)),
        ),
        (
            ((0, 0, 1), (0, 1, 0)),
            ((1, 0, 0), (0, 0, 1)),
            ((0, 1, 0), (1, 0, 1)),
        ),
    )
    states = []
    for history in histories:
        state = explorer.zero
        for a, b in history:
            a_i, b_i = explorer.point_index[a], explorer.point_index[b]
            if not explorer.legal(state, a_i, b_i):
                raise AssertionError(("illegal advertised history", history, a, b))
            state = explorer.step(state, a_i, b_i)
        states.append(state)

    common = (1, 0, 2, 1, 1, 2, 0, 0)
    target = (0, 0, 1, 2, 2, 1, 0, 1)
    if tuple(self_incidence_profile(explorer, state) for state in states) != (
        common,
        common,
    ):
        raise AssertionError("advertised common profile failed")

    label_lists = []
    for state in states:
        labels = tuple(
            (explorer.points[a_i], explorer.points[b_i])
            for a_i, b_i in explorer.vertices
            if explorer.legal(state, a_i, b_i)
            and self_incidence_profile(explorer, explorer.step(state, a_i, b_i))
            == target
        )
        label_lists.append(labels)
    expected = (
        (((1, 0, 1), (1, 1, 1)), ((1, 1, 0), (1, 1, 1))),
        (((1, 1, 0), (1, 1, 1)),),
    )
    if tuple(label_lists) != expected:
        raise AssertionError(("advertised successor multiplicities failed", label_lists))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, default=2)
    parser.add_argument("--q", type=int, default=2)
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--max-states", type=int, default=500_000)
    parser.add_argument("--complete", action="store_true")
    args = parser.parse_args()

    explorer = Explorer.build(args.t, args.q)
    complete = args.complete or (args.t, args.q) == (2, 2)
    if complete:
        states = reachable_complete(explorer, args.max_states)
        level_note = "complete reachable graph"
    else:
        states, level_sizes = reachable_to_depth(explorer, args.depth)
        level_note = f"reachable through depth {args.depth}; new states by level {level_sizes}"
    print(f"field diagnostic: t={args.t}, q={args.q}")
    print(level_note)
    print(f"states tested: {len(states)}")

    actions = projective_action_representatives(explorer)
    raw_order = len(orthogonal_matrices(args.t + 1, args.q))
    print(f"orthogonal matrices: {raw_order}")
    print(f"distinct projective orthogonal actions: {len(actions)}")

    @lru_cache(maxsize=None)
    def orbit_key(state: State) -> State:
        return min(
            act_state(explorer, state, matrix, permutation)
            for matrix, permutation in actions
        )

    check_fanout_formula(explorer, states)
    print("self-incidence fanout formula: PASS")
    check_explicit_q2_counterexample(explorer)
    if (args.t, args.q) == (2, 2):
        print("explicit reachable self-incidence counterexample: PASS")
    profile_failure = first_lumping_failure(
        explorer,
        states,
        lambda state: self_incidence_profile(explorer, state),
    )
    if profile_failure is None:
        print("self-incidence profile lumpability: no failure in tested states")
    else:
        i, j, key, old, new = profile_failure
        print("self-incidence profile lumpability: FAIL")
        print(f"first witness state indices: {i}, {j}")
        print(f"common profile: {key}")
        print(f"successor signatures: {old} != {new}")

    orbit_classes = len({orbit_key(state) for state in states})
    print(f"orbit classes represented: {orbit_classes}")
    orbit_failure = first_lumping_failure(explorer, states, orbit_key)
    if orbit_failure is not None:
        raise AssertionError(("orthogonal orbit quotient failed", orbit_failure[:3]))
    print("orthogonal orbit quotient lumpability: PASS")


if __name__ == "__main__":
    main()
