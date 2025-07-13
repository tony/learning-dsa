#!/usr/bin/env python
"""
1. Introduction to Algorithms and Complexity.

Context
-------
This lesson introduces what algorithms are and why their complexity is important. We'll explore
Big-O notation as a way to describe how algorithm performance scales with input size. Understanding
complexity is crucial as the Smart Routing and Analytics System (SRAS) must respond quickly to queries,
and inefficient algorithms will degrade response times as data grows.

Prerequisites:
- Basic Python knowledge (functions, loops).
- No advanced data structures or algorithms required yet.

References
----------
- Big-O notation: https://en.wikipedia.org/wiki/Big_O_notation
- timeit module: https://docs.python.org/3/library/timeit.html

Summary
-------
We will:
- Define what an algorithm is and why complexity (Big-O) matters.
- Show a trivial linear search algorithm.
- Use `timeit` to measure runtime for different input sizes, illustrating that more
data means
  longer run times, thus motivating complexity analysis.

Narrative:
The SRAS will soon handle many locations and routes. If we pick an algorithm with poor complexity,
our system might become slow or unresponsive when data scales. By understanding complexity now, we
lay the groundwork for making better algorithmic choices as SRAS evolves.

Doctests:
- We'll provide doctests to verify our trivial search function works correctly.
- Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to test.
"""

import timeit
from typing import Any


def linear_search(data: list[Any], target: Any) -> bool:
    """
    Check each element until finding the target or reaching the end.

    Complexity:
    - Time: O(n), where n is the length of the list.
    - For large n, runtime grows linearly.

    Examples
    --------
    >>> linear_search([1, 2, 3], 2)
    True
    >>> linear_search([1, 2, 3], 4)
    False
    >>> linear_search([], 'test')
    False
    """
    return any(item == target for item in data)


def main() -> None:
    """
    Demonstrate main functionality for this lesson.

    - Explain what an algorithm is: a finite procedure to solve a problem.
    - Measure runtime of linear_search on different input sizes using `timeit`.
    - Show that as input size increases, runtime also increases linearly (O(n)).

    This demonstration highlights why complexity matters: if SRAS uses slow algorithms
    when data grows, response times become unacceptably long.
    """
    print("Introduction to Algorithms and Complexity:")
    print("An algorithm is a set of steps to solve a problem.")
    print(
        "Big-O notation describes how runtime or space requirements scale with input size.",
    )
    print()

    small_data = list(range(10_000))
    large_data = list(range(1_000_000))

    # We'll search for a target near the end to ensure worst-case scenario.
    target = 999999

    # Time the small_data run
    small_time = timeit.timeit(lambda: linear_search(small_data, target), number=10)
    # Time the large_data run
    large_time = timeit.timeit(lambda: linear_search(large_data, target), number=10)

    print(
        f"Time for searching in small_data (n=10,000), 10 runs: {small_time:.5f} seconds",
    )
    print(
        f"Time for searching in large_data (n=1,000,000), 10 runs: {large_time:.5f} seconds",
    )
    print()
    print(
        "As input size increases, runtime grows linearly, illustrating O(n) complexity.",
    )
    print(
        "This matters because in a real system (like SRAS), as we handle more locations/routes,",
    )
    print("we need algorithms that remain fast at large scales.")


if __name__ == "__main__":
    main()
