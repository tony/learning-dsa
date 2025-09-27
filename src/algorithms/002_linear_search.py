#!/usr/bin/env python
"""
2. Linear Search (Unsorted Data).

Algorithm: Linear Search

Concepts:
- We scan through the list element by element until we find the target or reach the end.
- Best case: O(1) if the target is at the beginning.
- Average case: O(n) where n is the list size (target near middle or random).
- Worst case: O(n) if the target is at the end or not present.
- Space complexity: O(1), as we don't need extra storage apart from variables.

Narrative:
When the dataset is small or we have no knowledge of its order, we might do a linear scan.
In the early days of our product ID pipeline, scanning a short list is fine. But as the pipeline
grows to store thousands or millions of product IDs, a linear O(n) search quickly becomes a
bottleneck, leading us to seek more efficient methods in future chapters.

Doctests:
We test a simple linear_search function with a few scenarios.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit
from typing import Any


def linear_search(data: list[Any], target: Any) -> bool:
    """
    Perform a linear search on an unsorted list.

    - Check each element until we find the target or reach the end.
    - Return True if found, False otherwise.

    Complexity:
    - Best: O(1) if target is at the start
    - Average: O(n)
    - Worst: O(n) if the target is at the end or absent
    - Space: O(1)

    Examples
    --------
    >>> linear_search([1, 2, 3], 2)
    True
    >>> linear_search([1, 2, 3], 4)
    False
    >>> linear_search([], 10)
    False
    """
    return any(item == target for item in data)


def main() -> None:
    """
    Demonstrate main functionality.

    - We'll create different-sized lists and measure the time it takes for linear_search
      to find a target near the end (worst-case scenario).

    Narrative:
    Initially, scanning a short list of product IDs might be acceptable in the pipeline.
    But as data grows, O(n) search time becomes problematic, pushing us to find better solutions.
    """
    sizes = [10_000, 100_000, 1_000_000]

    for n in sizes:
        data = list(range(n))
        target = -1  # a value not in the lists, ensuring worst-case O(n) scenario
        exec_time = timeit.timeit(
            "linear_search(data, target)",
            globals={**globals(), **locals()},
            number=10,
        )
        print(
            f"List size {n}, repeated 10 runs: {exec_time:.5f} seconds total "
            f"(~{exec_time / 10:.5f}s per run).",
        )


if __name__ == "__main__":
    main()
