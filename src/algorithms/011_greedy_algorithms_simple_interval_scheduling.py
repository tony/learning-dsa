#!/usr/bin/env python
"""
11. Greedy Algorithms: Introduction with a Simple Interval Scheduling

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
- Space: O(n) if storing intervals; or O(1) in-place sorting (depending on implementation details).

Narrative:
In SRAS, each interval could represent a potential delivery window. By sorting these by their
finish times and greedily choosing intervals that don't overlap with already chosen ones,
we schedule the maximum number of deliveries. This approach ensures efficient resource use.

Doctests:
We define a small set of intervals, run the scheduling function, and verify the output.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit
import random
from typing import List, Tuple


def interval_scheduling(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Performs interval scheduling using the earliest finishing time greedy approach.
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
    >>> sorted(chosen)  # for consistent test output
    [(0, 3), (3, 5), (5, 9)]
    >>> # Explanation: after sorting by finish time => (1,2), (2,4), (0,3), (3,5), (5,9)
    >>> # The chosen intervals typically would be (1,2), (3,5), and (5,9) or
    >>> # (0,3), (3,5), (5,9) depending on tie ordering. The result is a maximal
    >>> # non-overlapping set. We'll get a set of size 3.
    """
    # Sort intervals by finish time
    intervals.sort(key=lambda x: x[1])

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
    We create a random list of intervals, apply interval_scheduling,
    and measure its time. This showcases O(n log n) for sorting.

    Narrative:
    If each interval represents a possible delivery window, the earliest finishing time
    greedy picks the maximum number of non-overlapping deliveries quickly and efficiently.
    """
    n = 10_000
    intervals = []
    # Create random intervals with random start time, short random duration
    for _ in range(n):
        start = random.randint(0, 50_000)
        duration = random.randint(1, 100)
        finish = start + duration
        intervals.append((start, finish))

    exec_time = timeit.timeit(lambda: interval_scheduling(intervals), number=1)
    print(
        f"Scheduling {n} intervals took: {exec_time:.5f}s (O(n log n) due to sorting)."
    )


if __name__ == "__main__":
    main()
