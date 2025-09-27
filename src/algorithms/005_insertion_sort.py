#!/usr/bin/env python
"""
5. Insertion Sort.

Algorithm: Insertion Sort

Concepts:
Insertion sort builds the sorted portion of the list incrementally by inserting one new item
into the already-sorted portion. In nearly sorted lists, each insertion is quick (few shifts),
leading to a best-case of O(n). However, in general or worst-case scenarios, it must shift
multiple elements per insertion, yielding O(n^2) time complexity.

Complexities:
- Best Case: O(n) if the list is already nearly sorted (each insertion does minimal
shifting).
- Average Case: O(n^2)
- Worst Case: O(n^2)
- Space: O(1), sorting in-place.

Narrative:
In certain real-world scenarios, such as a deliveries list that remains "almost sorted" but
occasionally gets new items, insertion sort can outperform selection sort practically. In the SRAS
pipeline, if a small portion of new deliveries arrive in roughly sorted order, insertion sort can
insert them quickly. Still, for fully random or large-scale data, O(n^2) eventually becomes a
bottleneck.

Doctests:
Check correctness on small and empty lists.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit


def insertion_sort(data: list[int]) -> None:
    """
    In-place insertion sort. Sorts 'data' in ascending order.

    Complexity:
    - Best: O(n) if nearly sorted
    - Average: O(n^2)
    - Worst: O(n^2)
    - Space: O(1)

    Examples
    --------
    >>> nums = [5, 2, 4, 1, 3]
    >>> insertion_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5]
    >>> nums2 = []
    >>> insertion_sort(nums2)
    >>> nums2
    []
    >>> nums3 = [10]
    >>> insertion_sort(nums3)
    >>> nums3
    [10]
    >>> nums4 = [1,2,3]
    >>> insertion_sort(nums4)
    >>> nums4  # Already sorted is O(n) best case
    [1, 2, 3]
    """
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        # Shift elements of data[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def main() -> None:
    """
    Demonstrate main functionality.

    We'll time insertion sort on moderately sized lists, illustrating O(n^2) behavior in general.
    For small or nearly sorted data, insertion sort can be quite efficient.

    Narrative:
    If deliveries or records are often partially sorted, insertion sort's near O(n) best case
    can be advantageous. But for large or random data, O(n^2) is a big limitation,
    motivating more efficient sorts in future chapters.
    """
    sizes = [1000, 2000]
    for n in sizes:
        # We'll use reverse-sorted as a near worst-case scenario.
        data = list(range(n, 0, -1))
        exec_time = timeit.timeit(
            "insertion_sort(data)",
            globals={**globals(), **locals()},
            number=1,
        )
        print(f"Insertion sort on {n} elements took: {exec_time:.5f}s.")


if __name__ == "__main__":
    main()
