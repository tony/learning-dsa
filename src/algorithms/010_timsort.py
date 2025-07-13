#!/usr/bin/env python
"""
10. Timsort (Python's Built-In Sorting Algorithm).

Algorithm: Timsort

Concepts:
- Timsort is a hybrid of mergesort and insertion sort, designed to perform especially
well on partially sorted data.
- Python's built-in `sorted()` function and `list.sort()` implement Timsort.
- If the data contains "runs" (already sorted segments), Timsort exploits them for near
O(n) performance in the best case.
- Otherwise, it defaults to O(n log n) average and worst case.

Complexities:
- Best: O(n), if data is mostly made of sorted runs.
- Average: O(n log n)
- Worst: O(n log n)
- Space: O(n), needed for merging operations.

Narrative:
In an SRAS (Smart Routing and Analytics System), data might be partially sorted due to incremental
updates or natural ordering. Timsort quickly merges these runs, achieving near O(n) performance
for such "nearly sorted" data. Even on random or adversarial data, it remains O(n log n),
making it a highly robust, real-world friendly sorting method.

Doctests:
Demonstrate basic usage of Timsort via Python's `sorted()`. Timsort is behind the scenes.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import random
import timeit


def demonstrate_timsort() -> None:
    """
    Show examples.

    --------
    >>> data = [5, 2, 8, 1, 3]
    >>> sorted_data = sorted(data)  # Timsort behind the scenes
    >>> sorted_data
    [1, 2, 3, 5, 8]

    >>> data2 = [3, 3, 3]  # many duplicates
    >>> sorted(data2)
    [3, 3, 3]

    >>> data3 = []
    >>> sorted(data3)
    []

    >>> data4 = [10]
    >>> sorted(data4)
    [10]
    """


def main() -> None:
    """
    Demonstrate main functionality.

    We'll compare the sorting times for partially sorted data vs random data
    to showcase Timsort's advantage on already sorted or partially ordered segments.

    Narrative:
    Timsort quickly merges sorted runs, so data that is partially sorted
    (common in real pipelines) can be sorted faster than a naive O(n log n) approach
    might suggest. Even fully random data still sees an O(n log n) performance.
    """
    n = 50_000

    # 1) Partially sorted data: let's keep most of it sorted but shuffle a few elements
    data_partial: list[int] = list(range(n))
    # shuffle 10% of positions to simulate partial disorder
    sample_indices = random.sample(range(n), k=n // 10)
    for idx in sample_indices:
        data_partial[idx] = random.randint(0, n)

    # 2) Fully random data
    data_random: list[int] = [random.randint(0, n) for _ in range(n)]

    # Time sorting partially sorted data
    partial_time = timeit.timeit(lambda: sorted(data_partial), number=1)
    # Time sorting random data
    random_time = timeit.timeit(lambda: sorted(data_random), number=1)

    print(f"Sorting partially sorted data of size {n}: {partial_time:.5f}s")
    print(f"Sorting random data of size {n}: {random_time:.5f}s")
    print("Timsort can exploit runs, achieving near O(n) if data is mostly sorted,")
    print("while still guaranteeing O(n log n) in average and worst cases.")


if __name__ == "__main__":
    main()
