#!/usr/bin/env python
r"""
4. Selection Sort.

Algorithm: Selection Sort

Concepts:
Selection sort repeatedly finds the minimum element (or maximum, depending on sorting order)
and places it at the beginning of the list. This results in O(n²) time complexity regardless
of input distribution.

Complexities:
- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)
- Space: O(1)

Narrative:
For very small datasets in an early-stage SRAS (Smart Routing and Analytics System), an O(n²)
sort might be acceptable. Its simplicity can be appealing, but as data grows, selection sort
becomes too slow, motivating more efficient sorts (e.g., merge sort, quicksort) with
\( O(n \log n) \).

Doctests:
We'll test selection_sort on small inputs to confirm correctness.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit


def selection_sort(data: list[int]) -> None:
    """
    In-place selection sort. Sorts 'data' in ascending order.

    Complexity: O(n²) in best, average, and worst case.
    Space: O(1)

    Examples
    --------
    >>> nums = [5, 2, 8, 1, 3]
    >>> selection_sort(nums)
    >>> nums
    [1, 2, 3, 5, 8]
    >>> nums2 = []
    >>> selection_sort(nums2)
    >>> nums2
    []
    >>> nums3 = [10]
    >>> selection_sort(nums3)
    >>> nums3
    [10]
    """
    n = len(data)
    for i in range(n):
        # Find the minimum element in data[i...n-1]
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        # Swap
        data[i], data[min_index] = data[min_index], data[i]


def main() -> None:
    """
    Demonstrate main functionality.

    We'll run selection sort on moderate-sized lists and time it, illustrating O(n²) growth.
    For large n, selection sort becomes quite slow.

    Narrative:
    If we only have small data sets in an early pipeline stage, selection sort's simplicity
    may suffice. But once data grows, O(n²) sorting quickly becomes a performance bottleneck,
    leading us to adopt more efficient sorts.
    """
    sizes = [1000, 2000]  # keep fairly small; selection sort is O(n^2)
    for n in sizes:
        data = list(range(n, 0, -1))  # worst-case: reverse-sorted
        exec_time = timeit.timeit(
            "selection_sort(data)", globals={**globals(), **locals()}, number=1
        )
        print(f"Selection sort on {n} elements took: {exec_time:.5f}s.")


if __name__ == "__main__":
    main()
