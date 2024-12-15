#!/usr/bin/env python
"""
1. Introduction to Data Structures and Complexity.

Context
-------
This lesson introduces the concept of algorithmic complexity (Big-O notation) and why it matters
when choosing data structures or algorithms. We explore how to reason about space and time
trade-offs. Understanding complexity helps us predict how code will scale as data grows.

Prerequisites:
- Familiarity with basic Python syntax and running Python scripts.
- No previous knowledge of complex data structures required.

References
----------
- Official Python docs: https://docs.python.org/3/library/timeit.html
- Big-O notation guide: https://en.wikipedia.org/wiki/Big_O_notation

Summary
-------
We will:
- Introduce Big-O notation as a way to describe algorithmic growth.
- Show how to measure runtime of a simple function using the `timeit` module.
- Discuss space vs. time trade-offs conceptually.

By the end, learners will understand that complexity analysis is crucial for making informed
decisions about which data structures or algorithms to use as the size of input data increases.

Doctests:
- We provide a simple doctest that checks the correctness of our sample function.
- Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit


def sample_function(data: list[int]) -> int:
    """
    A sample function: sum the elements of a list.

    Complexity:
    - Time: O(n), where n is the length of the input list.
    - Space: O(1) additional space, not counting the input storage.

    This function demonstrates a linear-time operation, as it must visit each element once.

    Examples
    --------
    >>> sample_function([1, 2, 3])
    6
    >>> sample_function([])
    0
    >>> sample_function([10])
    10
    """
    return sum(data)


def main() -> None:
    """
    Main demonstration for this lesson.

    We will:
    - Explain Big-O briefly.
    - Show how to time `sample_function` with `timeit` for a small and large input,
      illustrating how runtime grows with input size.

    Examples
    --------
    (This is a conceptual demo, so no fixed output is tested. Run and observe the printed output.)
    """
    print("Introduction to Complexity:")
    print(
        "Big-O notation describes how runtime or space usage grows as input size increases.",
    )

    small_data = list(range(10_000))  # small scale data
    large_data = list(range(1_000_000))  # larger scale data

    # Time the small_data run
    small_time = timeit.timeit(lambda: sample_function(small_data), number=10)
    # Time the large_data run
    large_time = timeit.timeit(lambda: sample_function(large_data), number=10)

    print(f"Time for small_data (n=10,000), 10 runs: {small_time:.5f} seconds")
    print(f"Time for large_data (n=1,000,000), 10 runs: {large_time:.5f} seconds")

    print(
        "\nAs input size grows, runtime increases roughly proportionally (linear in this case).",
    )
    print("This illustrates O(n) complexity: doubling n roughly doubles the runtime.")


if __name__ == "__main__":
    main()
