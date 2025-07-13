#!/usr/bin/env python
"""
16. Using `bisect` for Insertion in Sorted Lists.

Algorithm: Bisect-based insertion (binary search for position)

Concepts:
- We maintain a sorted list.
- `bisect_left` (or `bisect_right`) from the `bisect` module finds the position to
insert a new element to keep the list sorted.
- This is O(log n) for finding the position, but list insertion in Python is O(n) due
to shifting elements.
- Overall cost is O(n).

Complexities:
- Search for insertion position: O(log n)
- Actual insertion: O(n)
- Space: O(1) additional

Narrative:
If we have a sorted list of product IDs in an SRAS pipeline and only occasionally insert a new ID,
using `bisect` helps us find the correct position quickly. However, the actual insertion is still
O(n), which is fine for small lists or rare insertions, but can become expensive if we do many
insertions.

Doctests:
We'll define a function `sorted_insert` that uses `bisect_left` to find the insertion index,
then inserts.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import bisect
import timeit


def sorted_insert(lst: list[int], x: int) -> None:
    """
    Insert 'x' into the sorted list 'lst', keeping it sorted.

    Uses bisect_left to find the position in O(log n),
    then list.insert in O(n).

    Examples
    --------
    >>> data = [1, 3, 5, 7]
    >>> sorted_insert(data, 4)
    >>> data
    [1, 3, 4, 5, 7]
    >>> sorted_insert(data, 0)
    >>> data
    [0, 1, 3, 4, 5, 7]
    >>> sorted_insert(data, 10)
    >>> data
    [0, 1, 3, 4, 5, 7, 10]
    """
    idx = bisect.bisect_left(lst, x)
    lst.insert(idx, x)


def main() -> None:
    """
    Demonstrate main functionality.

    We'll maintain a sorted list of size n, then do m random insertions
    using sorted_insert. We'll measure the time. Despite O(log n) position finding,
    each insertion is O(n). So total is O(m * n).

    Narrative:
    bisect finds insertion index quickly, but Python list insertion is O(n).
    For large n with frequent insertions, consider other data structures.
    """
    import random

    n = 10_000
    m = 1_000

    # Start with a sorted list of size n
    data = list(range(n))

    # We'll measure the cost of inserting m random new elements
    random_values = [random.randint(0, n * 2) for _ in range(m)]

    def perform_insertions() -> None:
        # We'll copy data each time so it's the same scenario for each run
        data_copy = data[:]
        for val in random_values:
            sorted_insert(data_copy, val)

    exec_time = timeit.timeit(perform_insertions, number=1)
    print(
        f"Inserting {m} elements into a sorted list of size {n} took: {exec_time:.5f}s",
    )
    print("Position find: O(log n), insertion shift: O(n). So total: O(m * n).")


if __name__ == "__main__":
    main()
