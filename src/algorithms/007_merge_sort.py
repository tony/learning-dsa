#!/usr/bin/env python
"""
7. Merge Sort (Divide and Conquer).

Algorithm: Merge Sort

Concepts:
Merge sort splits the list roughly in half, recursively sorts each half, then merges
the two sorted halves. This yields a guaranteed O(n log n) time complexity, regardless
of data distribution. It requires additional space for the merging process.

Complexities:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)
- Space: O(n) due to auxiliary arrays while merging.

Narrative:
As data grows large, O(n²) sorts become untenable. Merge sort’s O(n log n) is a significant
improvement, providing stable performance for large datasets in the SRAS (or any data
analytics pipeline). While it needs extra memory, the predictable O(n log n) is often
worth that cost.

Doctests:
We’ll demonstrate merging and sorting small lists to confirm correctness.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit


def merge_sort(data: list[int]) -> None:
    """
    In-place merge sort (we'll implement a helper function that merges in a separate array,
    then copy back). Sorts 'data' in ascending order.

    Complexity: O(n log n) in best, average, and worst case.
    Space: O(n) for auxiliary arrays during merge.

    Examples
    --------
    >>> nums = [5, 2, 8, 1, 3]
    >>> merge_sort(nums)
    >>> nums
    [1, 2, 3, 5, 8]
    >>> nums2 = []
    >>> merge_sort(nums2)
    >>> nums2
    []
    >>> nums3 = [10]
    >>> merge_sort(nums3)
    >>> nums3
    [10]
    >>> nums4 = [3, 1, 2]
    >>> merge_sort(nums4)
    >>> nums4
    [1, 2, 3]
    """
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two halves back into 'data'
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements of left_half, if any
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements of right_half, if any
        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1


def main() -> None:
    """
    Main demonstration:
    We'll run merge sort on moderately sized lists to illustrate O(n log n) scaling.
    Even in worst-case scenarios, merge sort remains O(n log n) compared to O(n²) methods.

    Narrative:
    While mergesort requires additional O(n) space, its guaranteed O(n log n) time
    outperforms O(n²) sorts for large inputs, making it well-suited for bigger data
    sets in SRAS or a data analytics pipeline.
    """
    sizes = [10_000, 20_000]
    for n in sizes:
        data = list(range(n, 0, -1))  # reverse-sorted as a test
        exec_time = timeit.timeit(lambda: merge_sort(data), number=1)
        print(f"Merge sort on {n} elements took: {exec_time:.5f}s (O(n log n))")


if __name__ == "__main__":
    main()
