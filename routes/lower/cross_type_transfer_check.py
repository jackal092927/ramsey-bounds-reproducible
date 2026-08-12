#!/usr/bin/env python3
"""Small-field exact state explorer for Bradač's D*(t,q) tuple tree.

This is an exploratory checker, not an asymptotic proof.  It uses the exact
source state W^sigma(y): a tuple can be extended by (a,b) iff a is
orthogonal to b and to W^sigma(b), and the transition adds b to W(y) for
all y orthogonal to a.

The default run explores t=2, q=2 completely, reports the reachable-state
transition graph, and checks several proposed state compressions for
lumpability.  Only prime q is supported by the compact finite-field code.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from dataclasses import dataclass
from typing import Iterable


Vector = tuple[int, ...]
Basis = tuple[Vector, ...]
State = tuple[Basis, ...]


def inv_mod(x: int, q: int) -> int:
    return pow(x % q, -1, q)


def normalize(v: Vector, q: int) -> Vector:
    for x in v:
        if x % q:
            z = inv_mod(x, q)
            return tuple((z * y) % q for y in v)
    raise ValueError("zero vector has no projective normalization")


def projective_points(dim: int, q: int) -> tuple[Vector, ...]:
    points = {
        normalize(tuple(v), q)
        for n in range(1, q**dim)
        for v in [tuple((n // (q**i)) % q for i in range(dim))]
    }
    return tuple(sorted(points))


def rref(vectors: Iterable[Vector], q: int, dim: int) -> Basis:
    rows = [list(v) for v in vectors if any(x % q for x in v)]
    pivot_row = 0
    for col in range(dim):
        pivot = next(
            (i for i in range(pivot_row, len(rows)) if rows[i][col] % q),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        z = inv_mod(rows[pivot_row][col], q)
        rows[pivot_row] = [(z * x) % q for x in rows[pivot_row]]
        for i, row in enumerate(rows):
            if i == pivot_row:
                continue
            c = row[col] % q
            if c:
                rows[i] = [
                    (x - c * y) % q
                    for x, y in zip(row, rows[pivot_row], strict=True)
                ]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    nonzero = [tuple(row) for row in rows if any(row)]
    nonzero.sort(key=lambda row: next(i for i, x in enumerate(row) if x))
    return tuple(nonzero)


def dot(x: Vector, y: Vector, q: int) -> int:
    return sum(a * b for a, b in zip(x, y, strict=True)) % q


def contains(space: Basis, v: Vector, q: int, dim: int) -> bool:
    return len(rref((*space, v), q, dim)) == len(space)


@dataclass(frozen=True)
class Explorer:
    t: int
    q: int
    points: tuple[Vector, ...]
    point_index: dict[Vector, int]
    vertices: tuple[tuple[int, int], ...]

    @classmethod
    def build(cls, t: int, q: int) -> "Explorer":
        points = projective_points(t + 1, q)
        point_index = {p: i for i, p in enumerate(points)}
        vertices = tuple(
            (i, j)
            for i, a in enumerate(points)
            for j, b in enumerate(points)
            if dot(a, b, q) == 0
        )
        return cls(t, q, points, point_index, vertices)

    @property
    def zero(self) -> State:
        return tuple(() for _ in self.points)

    def legal(self, state: State, a_i: int, b_i: int) -> bool:
        a = self.points[a_i]
        return all(dot(a, w, self.q) == 0 for w in state[b_i])

    def step(self, state: State, a_i: int, b_i: int) -> State:
        a, b = self.points[a_i], self.points[b_i]
        out = list(state)
        for y_i, y in enumerate(self.points):
            if dot(a, y, self.q) == 0 and not contains(
                out[y_i], b, self.q, self.t + 1
            ):
                out[y_i] = rref((*out[y_i], b), self.q, self.t + 1)
        return tuple(out)

    def transitions(self, state: State) -> Counter[State]:
        out: Counter[State] = Counter()
        for a_i, b_i in self.vertices:
            if self.legal(state, a_i, b_i):
                out[self.step(state, a_i, b_i)] += 1
        return out

    def rank_profile(self, state: State) -> tuple[int, ...]:
        count = Counter(map(len, state))
        return tuple(count[r] for r in range(self.t + 2))

    def u_profile(self, state: State) -> tuple[int, ...]:
        ranks = [len(space) for space in state]
        return tuple(sum(r <= ell for r in ranks) for ell in range(self.t + 1))

    def scalar_moment(self, state: State) -> tuple[int, ...]:
        """Exact counts behind sum_y q^{-r(y)}, without floating point."""
        profile = self.rank_profile(state)
        return tuple(profile[r] * self.q ** (self.t + 1 - r) for r in range(self.t + 2))


def explore(explorer: Explorer, max_states: int) -> tuple[list[State], list[Counter[State]]]:
    states = [explorer.zero]
    index = {explorer.zero: 0}
    edges: list[Counter[State]] = []
    queue = deque([explorer.zero])
    while queue:
        state = queue.popleft()
        trans = explorer.transitions(state)
        edges.append(trans)
        for child in trans:
            if child in index:
                continue
            if len(states) >= max_states:
                raise RuntimeError(f"state cap {max_states} reached")
            index[child] = len(states)
            states.append(child)
            queue.append(child)
    return states, edges


def check_lumpability(
    explorer: Explorer,
    states: list[State],
    edges: list[Counter[State]],
    key,
) -> tuple[int, tuple | None]:
    signatures: dict[tuple, tuple[tuple[tuple, int], ...]] = {}
    failures = 0
    witness = None
    for state, trans in zip(states, edges, strict=True):
        state_key = key(state)
        child_counts: Counter[tuple] = Counter()
        for child, multiplicity in trans.items():
            child_counts[key(child)] += multiplicity
        signature = tuple(sorted(child_counts.items()))
        old = signatures.setdefault(state_key, signature)
        if old != signature:
            failures += 1
            if witness is None:
                witness = (state_key, old, signature)
    return failures, witness


def path_counts(
    explorer: Explorer,
    states: list[State],
    edges: list[Counter[State]],
    depth: int,
) -> list[int]:
    index = {state: i for i, state in enumerate(states)}
    weights = [0] * len(states)
    weights[0] = 1
    totals = [1]
    for _ in range(depth):
        nxt = [0] * len(states)
        for i, trans in enumerate(edges):
            if not weights[i]:
                continue
            for child, multiplicity in trans.items():
                nxt[index[child]] += weights[i] * multiplicity
        weights = nxt
        totals.append(sum(weights))
    return totals


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, default=2)
    parser.add_argument("--q", type=int, default=2)
    parser.add_argument("--max-states", type=int, default=500_000)
    parser.add_argument("--depth", type=int, default=20)
    args = parser.parse_args()

    explorer = Explorer.build(args.t, args.q)
    states, edges = explore(explorer, args.max_states)
    transition_count = sum(sum(trans.values()) for trans in edges)
    distinct_edges = sum(len(trans) for trans in edges)
    self_loops = sum(trans.get(state, 0) for state, trans in zip(states, edges, strict=True))
    print(f"PG points: {len(explorer.points)}")
    print(f"D* vertices: {len(explorer.vertices)}")
    print(f"reachable states: {len(states)}")
    print(f"distinct state edges: {distinct_edges}")
    print(f"pair-labelled transitions: {transition_count}")
    print(f"state-neutral pair transitions: {self_loops}")

    for label, key in (
        ("rank/U profile", explorer.rank_profile),
        ("q-weighted rank moment", explorer.scalar_moment),
    ):
        failures, witness = check_lumpability(explorer, states, edges, key)
        print(f"{label} lumpability failures: {failures}")
        if witness is not None:
            print(f"first {label} witness: {witness}")

    totals = path_counts(explorer, states, edges, args.depth)
    print("path counts:")
    for k, total in enumerate(totals):
        ratio = total / totals[k - 1] if k else 1.0
        root = total ** (1 / k) if k else 1.0
        print(f"  k={k:2d}: total={total} ratio={ratio:.9f} root={root:.9f}")


if __name__ == "__main__":
    main()
