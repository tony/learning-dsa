#!/usr/bin/env python
"""
3. Binary Search (Sorted Data).

Algorithm: Binary Search

Concepts:
Binary search operates on a sorted list by repeatedly dividing the search interval in half.
- Best case: O(1) if the target is the very middle element initially checked.
- Average case: O(log n)
- Worst case: O(log n) (we keep halving until we find or exhaust the search space)
- Space complexity: O(1), as we do it in-place (unless using recursive variant which adds O(log n) stack space).

Narrative:
If we sort product IDs or any sorted collection, we can confirm existence of a particular ID
in O(log n) rather than O(n). For SRAS (Smart Routing and Analytics System), that’s a huge improvement
over linear scanning. This keeps the system responsive even if the list grows large.

Doctests:
We test the binary_search function on sorted lists to confirm correctness.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit
from typing import Any


def binary_search(sorted_data: list[Any], target: Any) -> bool:
    """
    Perform a binary search on a sorted list for the target element.

    Returns True if found, False otherwise.

    Complexity:
    - Best: O(1) if the middle is the target on the first check.
    - Average: O(log n)
    - Worst: O(log n)
    - Space: O(1)

    Examples
    --------
    >>> data = list(range(10))
    >>> binary_search(data, 5)
    True
    >>> binary_search(data, 10)
    False
    >>> binary_search([], 0)
    False
    """
    low = 0
    high = len(sorted_data) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_data[mid] == target:
            return True
        if sorted_data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


def main() -> None:
    """
    Main demonstration:

    We'll time the binary_search on large sorted lists to show O(log n) performance.
    For bigger n, time growth is logarithmic rather than linear.

    Narrative:
    Sorting product IDs once lets us repeatedly do O(log n) searches. This
    is significantly more efficient than linear scanning, especially when
    we do many membership checks in a large dataset.
    """
    # We'll create sorted lists of different sizes and measure search time
    sizes = [10_000, 100_000, 1_000_000]
    target = -1  # Not in the list, ensuring full search

    for n in sizes:
        data = list(range(n))  # Sorted
        exec_time = timeit.timeit(lambda: binary_search(data, target), number=100)
        print(
            f"Sorted list size {n}, repeated 100 runs: {exec_time:.5f} seconds total "
            f"(~{exec_time / 100:.5f}s per run). This scales ~O(log n).",
        )


if __name__ == "__main__":
    main()
