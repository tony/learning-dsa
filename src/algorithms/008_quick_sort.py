#!/usr/bin/env python
"""
8. Quick Sort (Divide and Conquer) with Random Pivot.

Algorithm: Quick Sort

Concepts:
Quick sort partitions the list around a pivot element. Elements less than the pivot go to the left,
elements greater go to the right, and then we recursively sort both sides. The average and best cases
are O(n log n), but choosing a poor pivot can degrade performance to O(n^2). Randomized or median-of-three
pivots often mitigate this.

Complexities:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n^2) if we always pick a poor pivot (e.g., sorted or reverse-sorted data with naive pivot choice).
- Space: O(log n) average (due to recursive calls).

Narrative:
In an SRAS (Smart Routing and Analytics System), quick sort often outperforms merge sort in practice for
random or average distributions because of good locality and less overhead, but it can suffer if
the pivot selection is unlucky. With a good pivot strategy, quick sort remains a top choice for
fast in-place sorting of large datasets.

Doctests:
We test quick_sort on small lists to confirm correctness.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import random
import timeit


def quick_sort(data: list[int]) -> None:
    """
    In-place quick sort. Sorts 'data' in ascending order.

    Complexity:
    - Best: O(n log n)
    - Average: O(n log n)
    - Worst: O(n^2) if extremely unluck with random pivot
    - Space: O(log n) average for recursion

    Examples
    --------
    >>> nums = [5, 2, 8, 1, 3]
    >>> quick_sort(nums)
    >>> nums
    [1, 2, 3, 5, 8]
    >>> nums2 = []
    >>> quick_sort(nums2)
    >>> nums2
    []
    >>> nums3 = [10]
    >>> quick_sort(nums3)
    >>> nums3
    [10]
    >>> nums4 = [3, 1, 2]
    >>> quick_sort(nums4)
    >>> nums4
    [1, 2, 3]
    """
    _quick_sort_helper(data, 0, len(data) - 1)


def _quick_sort_helper(data: list[int], low: int, high: int) -> None:
    if low < high:
        pivot_index = _partition(data, low, high)
        _quick_sort_helper(data, low, pivot_index - 1)
        _quick_sort_helper(data, pivot_index + 1, high)


def _partition(data: list[int], low: int, high: int) -> int:
    # Pick a random pivot between low and high
    pivot_index = random.randint(low, high)
    # Swap pivot into the end
    data[pivot_index], data[high] = data[high], data[pivot_index]
    # We'll pick the last element as pivot (simple strategy).
    # For better performance, consider randomizing or median-of-three pivot selection.
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


def main() -> None:
    """
    Main demonstration:
    We'll use quick_sort on moderately sized lists to illustrate O(n log n) behavior
    in average cases. For reverse-sorted lists, this naive pivot choice can degrade
    to O(n^2). However, we'll still show typical usage with moderate n.

    Narrative:
    Quick sort often outperforms merge sort in average scenarios, but pivot choice is key
    to avoiding worst-case performance. In the SRAS pipeline, it can speed up sorting route
    IDs or other numeric data in place.
    """
    sizes = [10_000, 20_000]
    for n in sizes:
        data = list(range(n, 0, -1))  # worst-case with naive pivot
        exec_time = timeit.timeit(lambda: quick_sort(data), number=1)
        print(
            f"Quick sort on {n} elements took: {exec_time:.5f}s. (Pivot=last element)",
        )


if __name__ == "__main__":
    main()
