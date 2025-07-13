#!/usr/bin/env python
"""
11. Greedy Algorithms: Introduction with a Simple Interval Scheduling.

Algorithm: Interval Scheduling using Earliest Finishing Time

Concepts:
- We have a set of intervals, each with a start and finish time.
- A greedy approach to maximize the number of non-overlapping intervals is:
  1) Sort intervals by ascending finish time.
  2) Iteratively pick each interval that starts after the last chosen interval's finish.

Complexities:
- Sorting by finish time: O(n log n)
- Selecting intervals: O(n)
- Overall: O(n log n)
- Space: O(n) if storing intervals, or O(1) with in-place sorting.

Narrative:
In SRAS, each interval might be a delivery window. By sorting them by their finish times
and greedily choosing intervals that don't overlap with already chosen ones,
we schedule the maximum number of deliveries efficiently.

Doctests:
Because multiple valid solutions may exist if intervals have ties or partial overlaps,
we only test that we get a maximum set of non-overlapping intervals (length 3 here),
not a specific arrangement.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import operator
import random
import timeit


def interval_scheduling(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Perform interval scheduling using the earliest finishing time greedy approach.

    Returns a maximal set of non-overlapping intervals.

    intervals: list of (start, finish) times

    Steps:
      - Sort intervals by their finish times.
      - Iterate in ascending finish order, picking an interval if its start
        is >= the finish of the last chosen interval.

    Complexity:
      - Sort: O(n log n)
      - Selection pass: O(n)
      - Overall: O(n log n)

    Examples
    --------
    >>> ivals = [(0,3), (5,9), (1,2), (3,5), (2,4)]
    >>> chosen = interval_scheduling(ivals)
    >>> len(chosen)
    3
    >>> # We expect 3 intervals in the optimal solution, though multiple solutions
    >>> # are correct if they have length 3 and remain non-overlapping.

    >>> # Verify chosen intervals do not overlap:
    >>> all(chosen[i][1] <= chosen[i+1][0] for i in range(len(chosen)-1))
    True
    """
    # Sort intervals by finish time
    intervals.sort(key=operator.itemgetter(1))

    chosen = []
    last_finish = -1

    for start, finish in intervals:
        if start >= last_finish:
            chosen.append((start, finish))
            last_finish = finish

    return chosen


def main() -> None:
    """
    Main demonstration:

    Creates random intervals, applies interval_scheduling, and measures O(n log n) sorting time.

    Narrative:
    If each interval is a potential delivery window, earliest finishing time picking yields
    the maximum number of non-overlapping deliveries, ensuring efficient resource usage.
    """
    n = 10_000
    intervals = []
    # Create random intervals with random start times and short durations
    for _ in range(n):
        start = random.randint(0, 50_000)
        duration = random.randint(1, 100)
        finish = start + duration
        intervals.append((start, finish))

    exec_time = timeit.timeit(lambda: interval_scheduling(intervals), number=1)
    print(
        f"Scheduling {n} intervals took: {exec_time:.5f}s (O(n log n) due to sorting).",
    )


if __name__ == "__main__":
    main()
