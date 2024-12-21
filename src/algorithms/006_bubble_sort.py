#!/usr/bin/env python
r"""
6. Bubble Sort.

Algorithm: Bubble Sort

Concepts:
Bubble sort repeatedly swaps adjacent elements if they are out of order, thus "bubbling up"
the largest element in each pass to the end. It continues until no swaps are needed or until
n-1 passes have occurred.

Complexities:
- Best Case: O(n) if the list is already sorted (we detect no swaps in the first pass).
- Average Case: O(n^2)
- Worst Case: O(n^2)
- Space: O(1), since we do in-place swapping.

Narrative:
In an SRAS or similar data pipeline, bubble sort is straightforward but becomes very slow
for large or random data sets. Its best case of \(O(n)\) if the list is already sorted
is occasionally beneficial, but overall it's typically replaced by more efficient sorting
techniques as data scales.

Doctests:
We’ll test `bubble_sort` on small lists to confirm correctness.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit


def bubble_sort(data: list[int]) -> None:
    """
    In-place bubble sort. Sorts 'data' in ascending order.

    Complexity:
    - Best: O(n), if already sorted (no swaps in first pass).
    - Average: O(n^2)
    - Worst: O(n^2)
    - Space: O(1)

    Examples
    --------
    >>> nums = [5, 2, 8, 1, 3]
    >>> bubble_sort(nums)
    >>> nums
    [1, 2, 3, 5, 8]
    >>> nums2 = []
    >>> bubble_sort(nums2)
    >>> nums2
    []
    >>> nums3 = [10]
    >>> bubble_sort(nums3)
    >>> nums3
    [10]
    >>> nums4 = [1, 2, 3]
    >>> bubble_sort(nums4)
    >>> nums4  # Already sorted is O(n) best case if no swaps
    [1, 2, 3]
    """
    n = len(data)
    # We can stop earlier if no swaps occurred (best case)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break


def main() -> None:
    """
    Main demonstration:
    We'll run bubble sort on moderately sized lists, illustrating O(n^2) behavior
    for random or reverse-sorted data. If data is nearly sorted, bubble sort can
    detect it early and terminate in ~O(n).

    Narrative:
    Another basic O(n^2) sorting method that might be acceptable on very small data
    or nearly sorted arrays, but quickly becomes impractical for large sets in SRAS.
    """
    sizes = [1000, 2000]
    for n in sizes:
        data = list(range(n, 0, -1))  # worst-case: reverse-sorted
        exec_time = timeit.timeit(lambda: bubble_sort(data), number=1)
        print(f"Bubble sort on {n} elements took: {exec_time:.5f}s.")


if __name__ == "__main__":
    main()
