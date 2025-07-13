#!/usr/bin/env python
"""
19. Linear Search Revisited: Best Use Cases and Limitations.

Algorithm: Linear Search (Unsorted Data), revisited

Concepts:
- Scanning each element until we find the target or reach the end (O(n)) is trivial,
  but it grows linearly with n, which can be too slow for large lists.
- Best if n is small, or if lookups are rare.

Complexities:
- Best Case: O(1) if target is the first element
- Average Case: O(n)
- Worst Case: O(n) if target is at the end or not present
- Space: O(1)

Narrative:
In an SRAS pipeline or similar system, we might deal with small, "rare" product sets or
unsorted data that isn't worth fully indexing or sorting. Linear search is often simplest and
sufficient for these small use cases. But as data grows large, O(n) time becomes a bottleneck,
pushing us toward more efficient data structures or sorting-based searches.

Doctests:
We'll retest a basic linear search function, reaffirming correctness on small lists.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit
from typing import Any


def linear_search_small(data: list[Any], target: Any) -> bool:
    """
    Perform a linear search on an unsorted list, best used for small or "rare" data.

    Complexity:
    - Best: O(1) if target is at the start
    - Average: O(n)
    - Worst: O(n)
    - Space: O(1)

    Examples
    --------
    >>> linear_search_small([1, 2, 3], 2)
    True
    >>> linear_search_small([1, 2, 3], 4)
    False
    >>> linear_search_small([], 10)
    False
    """
    return any(item == target for item in data)


def main() -> None:
    """
    Main demonstration:

    We'll demonstrate linear search on smaller data sets,
    highlighting that for small n, O(n) is often acceptable.

    Narrative:
    If the dataset is small (like a rare product set), or lookups are infrequent,
    linear search's overhead is minimal, so we keep the code simple and memory usage at O(1).
    """
    sizes = [100, 1000, 5000]  # smaller scales than massive production data
    target = -1  # ensure worst-case scenario (not present)

    for n in sizes:
        data = list(range(n))
        exec_time = timeit.timeit(lambda: linear_search_small(data, target), number=50)
        print(
            f"List size {n}, repeated 50 runs: {exec_time:.5f} seconds total "
            f"(~{exec_time / 50:.5f}s per run).",
        )

    print(
        "\nFor small data sets, linear search's O(n) cost is minimal. "
        "If data grows larger, consider better structures or sorting.",
    )


if __name__ == "__main__":
    main()
