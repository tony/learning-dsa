#!/usr/bin/env python
"""
15. Algorithm Choice Based on Data Characteristics.

Conceptual Demonstration:
We compare how different sorting algorithms (previously introduced) perform on different data
distributions: random, nearly sorted, and reverse sorted. This helps illustrate that while mergesort
or quicksort might be generally good, insertion sort can excel on nearly sorted data, and Timsort
(Python's built-in) can detect partial ordering.

Complexities:
- Each algorithm has its known complexity (insertion: O(n^2), merge sort: O(n log n),
  Timsort: O(n) best for partial ordering, O(n log n) general).
- The actual performance also depends heavily on data patterns.

Narrative:
In SRAS or any large data pipeline, data might be random, mostly sorted, or nearly reversed. We
demonstrate that the "best" choice can differ:
- For large random sets, mergesort or Timsort is usually O(n log n).
- For nearly sorted data, insertion sort might approach O(n).
- Timsort can also exploit existing runs (partially sorted segments) to sort in O(n)
best case.

Doctests:
We'll omit direct doctests here, focusing on timing demonstration across data patterns.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` if desired.
"""

import random
import timeit
import typing


# We assume the following sorts are from previous chapters:
def insertion_sort(data: list[int]) -> None:
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def merge_sort(data: list[int]) -> None:
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1


def main() -> None:
    """
    Demonstrate main functionality.

    We create three data patterns: random, nearly sorted, and reverse sorted,
    each of size n. We time insertion_sort, merge_sort, and Timsort (Python's sorted).

    By comparing times, we see how each algorithm's performance shifts with data distribution.
    """
    n = 5000

    # 1) Random data
    data_random = [random.randint(0, n) for _ in range(n)]
    # 2) Nearly sorted: ascending with small random perturbations
    data_nearly = list(range(n))
    sample_indices = random.sample(range(n), k=n // 20)  # 5% random positions
    for idx in sample_indices:
        data_nearly[idx] = random.randint(0, n)
    # 3) Reverse sorted
    data_reversed = list(range(n, 0, -1))

    # We'll define a small helper to time each sorting approach on a copy of the data
    def time_sorting(
        algorithm_name: str,
        sort_func: typing.Callable[[list[int]], None],
        base_data: list[int],
    ) -> None:
        data_copy = base_data.copy()
        t = timeit.timeit(lambda: sort_func(data_copy), number=1)
        print(f"{algorithm_name} on {len(base_data)} elements: {t:.5f}s")

    # Compare insertion_sort, merge_sort, and Timsort on each distribution
    for distribution_name, dataset in [
        ("Random", data_random),
        ("Nearly Sorted", data_nearly),
        ("Reverse Sorted", data_reversed),
    ]:
        print(f"\n== {distribution_name} Data ==")
        time_sorting("Insertion Sort", insertion_sort, dataset)
        time_sorting("Merge Sort", merge_sort, dataset)
        # Python's built-in Timsort
        time_sorting("Timsort (built-in)", lambda arr: arr.sort(), dataset)


if __name__ == "__main__":
    main()
