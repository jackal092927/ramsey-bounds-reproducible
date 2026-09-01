#!/usr/bin/env python3
"""Reproducible audit of the implicit-majority quantum Ramsey theorem.

The quantum algorithm keeps the current candidate vertex set only through a
membership predicate.  Quantum search samples from that implicit set, while
ordinary sampling estimates which colour class is nearly the majority.  A
scale-aware error schedule spends more accuracy at cheap early levels and
less at expensive deep levels.  This file does *not* simulate a
fault-tolerant quantum computer.  It checks the exact size recurrence, the
combinatorial output invariant, and the resulting query-cost formula; its
Monte Carlo component substitutes an ideal uniform marked-item sampler for
the standard quantum-search primitive.

All theorem-critical recurrence calculations use fractions.  Floating-point
values are used only for readable cost proxies and Monte Carlo sampling.
"""

from __future__ import annotations

import argparse
import json
import math
import random
from collections.abc import Callable
from fractions import Fraction
from functools import lru_cache


EdgeOracle = Callable[[int, int], int]


def ceil_fraction(value: Fraction) -> int:
    """Return ceil(value) without converting to floating point."""

    return -(-value.numerator // value.denominator)


def size_biased_lower_bound(candidate_count: int, rounds: int) -> Fraction:
    """Closed-form lower bound for the estimation-free recursion."""

    if candidate_count < 1 or rounds < 0:
        raise ValueError("candidate_count must be positive and rounds nonnegative")
    return Fraction(max(0, candidate_count - 2**rounds + 1), candidate_count)


@lru_cache(maxsize=None)
def exact_worst_size_biased_survival(candidate_count: int, rounds: int) -> Fraction:
    """Exact dynamic program over all adaptive two-colour split trees.

    This is a finite diagnostic of the analytic size-biased survival lemma.
    It is deliberately limited to small inputs by the command-line driver.
    """

    if candidate_count < 0 or rounds < 0:
        raise ValueError("arguments must be nonnegative")
    if rounds == 0:
        return Fraction(int(candidate_count >= 1))
    if candidate_count <= 1:
        return Fraction(0)

    remainder = candidate_count - 1
    values = []
    for first_side in range(remainder + 1):
        second_side = remainder - first_side
        numerator = (
            first_side
            * exact_worst_size_biased_survival(first_side, rounds - 1)
            + second_side
            * exact_worst_size_biased_survival(second_side, rounds - 1)
        )
        values.append(numerator / remainder)
    return min(values)


def size_biased_audit(max_rounds: int = 9) -> list[dict[str, object]]:
    """Compare the exact worst split tree with the proved closed-form bound."""

    rows = []
    for rounds in range(1, max_rounds + 1):
        candidate_count = 2 ** (rounds + 1)
        exact = exact_worst_size_biased_survival(candidate_count, rounds)
        lower = size_biased_lower_bound(candidate_count, rounds)
        assert exact >= lower
        rows.append(
            {
                "rounds": rounds,
                "candidate_count": candidate_count,
                "proved_lower_bound": str(lower),
                "exact_worst_survival": str(exact),
                "exact_worst_survival_float": float(exact),
            }
        )
    return rows


def weak_compositions(total: int, parts: int):
    """Yield all ordered weak compositions of total into `parts` terms."""

    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for suffix in weak_compositions(total - first, parts - 1):
            yield (first, *suffix)


def geometric_threshold(colours: int, rounds: int) -> int:
    """Return B_d=1+q+...+q^(d-1), with B_0=0."""

    if colours < 2 or rounds < 0:
        raise ValueError("colours must be at least two and rounds nonnegative")
    return (colours**rounds - 1) // (colours - 1)


@lru_cache(maxsize=None)
def exact_worst_multicolour_survival(
    candidate_count: int,
    rounds: int,
    colours: int,
) -> Fraction:
    """Exact small-instance DP over all q-colour adaptive split trees."""

    if candidate_count < 0 or rounds < 0 or colours < 2:
        raise ValueError("invalid multicolour DP arguments")
    if rounds == 0:
        return Fraction(int(candidate_count >= 1))
    if candidate_count <= 1:
        return Fraction(0)

    remainder = candidate_count - 1
    values = []
    for split in weak_compositions(remainder, colours):
        numerator = sum(
            side
            * exact_worst_multicolour_survival(side, rounds - 1, colours)
            for side in split
        )
        values.append(numerator / remainder)
    return min(values)


def multicolour_size_biased_audit(
    colours: int = 3,
    max_rounds: int = 4,
) -> list[dict[str, object]]:
    """Check the q-colour survival formula against exact split-tree DPs."""

    rows = []
    for rounds in range(1, max_rounds + 1):
        threshold = geometric_threshold(colours, rounds)
        candidate_count = 1 << (2 * threshold - 1).bit_length()
        exact = exact_worst_multicolour_survival(
            candidate_count,
            rounds,
            colours,
        )
        lower = Fraction(
            max(0, candidate_count - threshold),
            candidate_count - 1,
        )
        assert exact >= lower
        rows.append(
            {
                "colours": colours,
                "rounds": rounds,
                "geometric_threshold": threshold,
                "power_of_two_candidate_count": candidate_count,
                "proved_lower_bound": str(lower),
                "exact_worst_survival": str(exact),
                "exact_worst_survival_float": float(exact),
            }
        )
    return rows


def recurrence_data(k: int) -> dict[str, object]:
    """Compute the exact scale-aware near-majority recurrence.

    We use r=2k-3 branch decisions and a total error budget E=1/16.  Levels
    are grouped into blocks of six from the deepest level.  The error weight
    halves from one six-level block to the preceding block, which is an exact
    rational schedule and yields the optimized O(k 2^k log(k/eta)) query
    bound.  If level i retains at least a_i=1/2-epsilon_i, then

        L_0 = 4^(k-1),
        L_{i+1} = a_i (L_i - 1)

    lower-bounds the actual candidate-set size at every level.
    """

    if k < 2:
        raise ValueError("k must be at least 2")

    rounds = 2 * k - 3
    total_error_budget = Fraction(1, 16)
    block_distances = [
        (rounds - 1 - level + 5) // 6 for level in range(rounds)
    ]
    raw_weights = [Fraction(1, 2**distance) for distance in block_distances]
    weight_sum = sum(raw_weights, start=Fraction(0))
    epsilons = [
        total_error_budget * weight / weight_sum for weight in raw_weights
    ]
    retained_fractions = [Fraction(1, 2) - epsilon for epsilon in epsilons]
    vertex_count = 4 ** (k - 1)
    bounds = [Fraction(vertex_count)]
    prefix_products = [Fraction(1)]
    for retained_fraction in retained_fractions:
        bounds.append(retained_fraction * (bounds[-1] - 1))
        prefix_products.append(prefix_products[-1] * retained_fraction)

    assert sum(epsilons, start=Fraction(0)) == total_error_budget
    assert all(
        product >= Fraction(7, 8) * Fraction(1, 2**level)
        for level, product in enumerate(prefix_products)
    )
    assert all(
        bound > vertex_count * product - 1
        for bound, product in zip(bounds, prefix_products, strict=True)
    )

    # Hoeffding counts for simultaneous total estimation error at most 0.01.
    total_failure = Fraction(1, 100)
    sample_counts = [
        math.ceil(
            math.log(2 * rounds / float(total_failure))
            / (2 * float(epsilon) ** 2)
        )
        for epsilon in epsilons
    ]

    # This is an auditable leading-order proxy, not an exact circuit count.
    # One implicit membership test at level i makes i edge queries.  The
    # square-root factor is the marked-item sampling cost.  We use the
    # predetermined density (3/8)2^-i, because the pivot is removed before
    # the Hoeffding samples are drawn.  The proxy omits absolute BBHT and
    # batch-tail constants.
    query_proxy = 0
    for level in range(rounds + 1):
        membership_queries = max(1, level)
        samples = sample_counts[level] + 1 if level < rounds else 1
        inverse_density = Fraction(8 * 2**level, 3)
        query_proxy += (
            samples
            * membership_queries
            * math.ceil(math.sqrt(float(inverse_density)))
        )

    return {
        "k": k,
        "vertices": vertex_count,
        "rounds": rounds,
        "total_error_budget": str(total_error_budget),
        "error_schedule": [str(value) for value in epsilons],
        "retained_fraction_schedule": [
            str(value) for value in retained_fractions
        ],
        "six_level_block_distances": block_distances,
        "final_exact_lower_bound": str(bounds[-1]),
        "final_ceiling_lower_bound": ceil_fraction(bounds[-1]),
        "final_bound_is_positive": bounds[-1] > 0,
        "all_levels_positive": all(value > 0 for value in bounds),
        "hoeffding_samples_by_round_for_failure_0.01": sample_counts,
        "idealized_quantum_query_proxy": query_proxy,
        "classical_exact_majority_upper_proxy": 2 * vertex_count,
        "query_proxy_over_sqrt_vertices": query_proxy / math.sqrt(vertex_count),
    }


def collision_reduction_exponents(max_collision: int = 12) -> list[dict[str, object]]:
    """Audit the direct JLRX-plus-Liu--Zhandry parameter substitution.

    JLRX's Ramsey reduction uses a host size M approximately B^(4t), where B
    is the range size of a t-collision instance.  Liu--Zhandry's exponent in B
    is (2^(t-1)-1)/(2^t-1).  Expressed in M, the direct exponent is therefore
    divided by 4t.  This table does not assert a lower bound outside the
    hypotheses of those papers; it only makes the advertised substitution
    transparent and reproducible.
    """

    if max_collision < 2:
        raise ValueError("max_collision must be at least 2")
    rows = []
    for collision_size in range(2, max_collision + 1):
        lz_exponent = Fraction(
            2 ** (collision_size - 1) - 1,
            2**collision_size - 1,
        )
        host_exponent = lz_exponent / (4 * collision_size)
        rows.append(
            {
                "collision_size": collision_size,
                "liu_zhandry_range_exponent": str(lz_exponent),
                "direct_ramsey_host_exponent": str(host_exponent),
                "direct_ramsey_host_exponent_float": float(host_exponent),
            }
        )
    return rows


def grover_statevector(
    universe_size: int,
    marked: tuple[int, ...],
    iterations: int,
) -> list[float]:
    """Evolve a tiny real state vector through Grover iterations.

    This dependency-free routine audits only the permutation symmetry behind
    conditional uniformity of the capped sampler.  It is not used to estimate
    the asymptotic query complexity.
    """

    if universe_size < 1 or universe_size & (universe_size - 1):
        raise ValueError("universe_size must be a positive power of two")
    if iterations < 0 or not marked:
        raise ValueError("iterations must be nonnegative and marked nonempty")
    if len(set(marked)) != len(marked) or any(
        index < 0 or index >= universe_size for index in marked
    ):
        raise ValueError("marked indices must be distinct elements of the universe")

    state = [1 / math.sqrt(universe_size)] * universe_size
    marked_set = set(marked)
    for _ in range(iterations):
        for index in marked_set:
            state[index] = -state[index]
        mean_amplitude = math.fsum(state) / universe_size
        state = [2 * mean_amplitude - amplitude for amplitude in state]

    norm = math.fsum(amplitude * amplitude for amplitude in state)
    assert abs(norm - 1.0) < 1e-12
    return state


def statevector_uniformity_audit(universe_size: int = 16) -> list[dict[str, object]]:
    """Check uniform marked-item output in a small Grover mixture.

    We average measurement distributions for a uniformly random iteration
    count in ``{0, ..., ceil(sqrt(M))}``.  BBHT uses a geometric schedule,
    but each component has the same symmetry checked here, so any mixture is
    conditionally uniform on the marked set.
    """

    if universe_size < 2 or universe_size & (universe_size - 1):
        raise ValueError("universe_size must be a power of two at least two")
    maximum_iterations = math.ceil(math.sqrt(universe_size))
    marked_counts = sorted(
        {1, 2, 3, universe_size // 4, universe_size // 2, universe_size - 1}
    )
    rows = []
    for marked_count in marked_counts:
        marked = tuple(range(marked_count))
        mixture = [0.0] * universe_size
        for iterations in range(maximum_iterations + 1):
            state = grover_statevector(universe_size, marked, iterations)
            for index, amplitude in enumerate(state):
                mixture[index] += amplitude * amplitude / (maximum_iterations + 1)

        marked_success = math.fsum(mixture[index] for index in marked)
        conditional = [mixture[index] / marked_success for index in marked]
        target = 1 / marked_count
        deviation = max(abs(probability - target) for probability in conditional)
        assert deviation < 1e-12
        rows.append(
            {
                "universe_size": universe_size,
                "marked_count": marked_count,
                "iteration_counts_averaged": maximum_iterations + 1,
                "mixture_marked_success_probability": marked_success,
                "maximum_conditional_uniformity_error": deviation,
            }
        )
    return rows


def make_graph(kind: str, n: int, seed: int) -> EdgeOracle:
    """Create a deterministic test graph oracle."""

    if kind == "complete":
        return lambda u, v: int(u != v)
    if kind == "empty":
        return lambda u, v: 0
    if kind == "parity":
        return lambda u, v: (u ^ v).bit_count() & 1
    if kind != "random":
        raise ValueError(f"unknown graph kind: {kind}")

    rng = random.Random(seed)
    colors: dict[tuple[int, int], int] = {}
    for u in range(n):
        for v in range(u + 1, n):
            colors[(u, v)] = rng.randrange(2)

    def oracle(u: int, v: int) -> int:
        if u == v:
            return 0
        edge = (u, v) if u < v else (v, u)
        return colors[edge]

    return oracle


def is_homogeneous(vertices: list[int], oracle: EdgeOracle) -> bool:
    """Check whether all edges induced by vertices have one colour."""

    colors = {
        oracle(vertices[i], vertices[j])
        for i in range(len(vertices))
        for j in range(i + 1, len(vertices))
    }
    return len(colors) <= 1


def ideal_sampler_trial(
    oracle: EdgeOracle,
    n: int,
    k: int,
    rng: random.Random,
    sample_counts: list[int],
) -> dict[str, object]:
    """Simulate one run using an ideal uniform marked-item sampler.

    Explicit Python lists stand in for the implicit sets.  Therefore this is a
    correctness diagnostic, not a claim about classical running time.
    """

    rounds = 2 * k - 3
    current = list(range(n))
    pivots: list[int] = []
    labels: list[int] = []
    sizes = [len(current)]

    if len(sample_counts) != rounds:
        raise ValueError("sample_counts must contain one value per round")

    for level in range(rounds):
        if len(current) < 2:
            return {
                "success": False,
                "reason": "candidate_set_exhausted",
                "sizes": sizes,
            }
        pivot = rng.choice(current)
        remainder = [vertex for vertex in current if vertex != pivot]
        red_samples = sum(
            oracle(pivot, rng.choice(remainder))
            for _ in range(sample_counts[level])
        )
        label = int(2 * red_samples >= sample_counts[level])
        current = [vertex for vertex in remainder if oracle(pivot, vertex) == label]
        pivots.append(pivot)
        labels.append(label)
        sizes.append(len(current))

    if not current:
        return {
            "success": False,
            "reason": "candidate_set_exhausted",
            "sizes": sizes,
        }

    majority_label = int(2 * sum(labels) >= len(labels))
    selected = [
        pivot for pivot, label in zip(pivots, labels, strict=True) if label == majority_label
    ][: k - 1]
    selected.append(rng.choice(current))
    return {
        "success": len(selected) == k and is_homogeneous(selected, oracle),
        "reason": "ok",
        "sizes": sizes,
        "output": selected,
        "output_color": majority_label,
    }


def simulation_summary(k: int, trials: int, seed: int) -> dict[str, object]:
    """Run small ideal-sampler diagnostics on several graph families."""

    n = 4 ** (k - 1)
    schedule = recurrence_data(k)
    sample_counts = schedule[
        "hoeffding_samples_by_round_for_failure_0.01"
    ]
    results: dict[str, object] = {}
    graph_kinds = ("complete", "empty", "parity", "random", "random_resampled")
    for graph_index, kind in enumerate(graph_kinds):
        fixed_oracle = (
            None
            if kind == "random_resampled"
            else make_graph(kind, n, seed + graph_index)
        )
        failures = []
        minimum_final_size = n
        for trial in range(trials):
            oracle = (
                make_graph("random", n, seed + 1_000_000 + trial)
                if kind == "random_resampled"
                else fixed_oracle
            )
            assert oracle is not None
            trial_rng = random.Random(seed + 10_000 * graph_index + trial)
            result = ideal_sampler_trial(oracle, n, k, trial_rng, sample_counts)
            minimum_final_size = min(minimum_final_size, result["sizes"][-1])
            if not result["success"]:
                failures.append({"trial": trial, **result})
        results[kind] = {
            "trials": trials,
            "failures": len(failures),
            "first_failure": failures[0] if failures else None,
            "minimum_final_candidate_size": minimum_final_size,
            "graph_sampling": (
                "one fresh G(n,1/2) graph per trial"
                if kind == "random_resampled"
                else "one fixed graph across all algorithmic trials"
            ),
        }

    return {
        "k": k,
        "vertices": n,
        "samples_by_round": sample_counts,
        "note": "ideal uniform marked-item sampling; not a state-vector simulation",
        "graphs": results,
    }


def self_check() -> None:
    for k in range(2, 65):
        data = recurrence_data(k)
        assert data["all_levels_positive"]
        assert data["final_bound_is_positive"]
        assert data["final_ceiling_lower_bound"] >= 1

    for kind in ("complete", "empty", "parity", "random"):
        oracle = make_graph(kind, 16, 20260831)
        result = ideal_sampler_trial(
            oracle=oracle,
            n=16,
            k=2,
            rng=random.Random(20260831),
            sample_counts=[512],
        )
        assert result["success"], (kind, result)

    exponents = collision_reduction_exponents()
    assert exponents[0]["direct_ramsey_host_exponent"] == "1/24"
    assert max(row["direct_ramsey_host_exponent_float"] for row in exponents) == 1 / 24
    size_biased_audit()
    multicolour_size_biased_audit()
    statevector_uniformity_audit()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-k", type=int, default=12)
    parser.add_argument("--simulate-k", type=int, default=3)
    parser.add_argument("--trials", type=int, default=20)
    parser.add_argument("--seed", type=int, default=20260831)
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument(
        "--simulation-only",
        action="store_true",
        help="emit only the small state-vector and end-to-end diagnostics",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="run assertions and print only the pass marker",
    )
    args = parser.parse_args()

    if args.max_k < 2:
        parser.error("max-k must be at least 2")
    if not 2 <= args.simulate_k <= 4:
        parser.error("simulate-k must lie in [2, 4]")
    if args.trials < 1:
        parser.error("trials must be positive")
    if args.self_check:
        self_check()
    if args.check_only:
        if not args.self_check:
            parser.error("check-only requires --self-check")
        print("QUANTUM_RAMSEY_AUDIT_PASS")
        return
    if args.simulation_only:
        output = {
            "small_statevector_sampler_audit": statevector_uniformity_audit(),
            "simulation": simulation_summary(args.simulate_k, args.trials, args.seed),
        }
        print(json.dumps(output, indent=2))
        return

    output = {
        "small_statevector_sampler_audit": statevector_uniformity_audit(),
        "size_biased_survival": size_biased_audit(),
        "three_colour_size_biased_survival": multicolour_size_biased_audit(),
        "recurrences": [recurrence_data(k) for k in range(2, args.max_k + 1)],
        "collision_reduction_parameter_audit": collision_reduction_exponents(),
        "simulation": simulation_summary(args.simulate_k, args.trials, args.seed),
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
