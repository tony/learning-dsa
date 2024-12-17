#!/usr/bin/env python
"""
10. Sets (Python set).

Data Structure: Set (Hash-based)

Concepts:
A set is a collection of unique elements. In Python, sets are implemented as hash tables.
- Average complexity for insert, membership check, and delete is O(1).
- Worst case O(n) if hashing degenerates.
- Space is O(n).

Complexities:
- Insert: Average O(1), Worst O(n)
- Membership check: Average O(1), Worst O(n)
- Delete: Average O(1), Worst O(n)
- Space: O(n)

Narrative:
In the data analytics pipeline, we may want to ensure no duplicate records enter. By using a set,
we can quickly check if a record already exists before inserting it, preventing duplicates from
accumulating. O(1) average checks mean even with large datasets, we efficiently maintain uniqueness.

Doctests:
We’ll show inserting, checking membership, and deleting elements from a set.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit


def demonstrate_set_operations() -> None:
    """
    Examples
    --------
    >>> s = set()
    >>> s.add("apple")
    >>> "apple" in s
    True
    >>> "banana" in s
    False
    >>> s.add("banana")
    >>> s.remove("apple")
    >>> "apple" in s
    False
    """


def main() -> None:
    """
    Main demonstration:
    We'll measure insertion and membership check times for a large set.

    Narrative:
    As data grows, we can still rely on O(1) average checks to maintain uniqueness efficiently.
    """
    n = 1_000_000
    s: set[int] = set()

    # Inserting n items
    insert_time = timeit.timeit(lambda: s.add(len(s)), number=n)
    # Check membership for an item known to exist
    search_time = timeit.timeit(lambda: (n - 1 in s), number=1000)

    print(
        f"Inserting {n} items took: {insert_time:.5f} s (~{insert_time / n:.9f} s/insert) average O(1)",
    )
    print(
        f"Checking membership of a known element 1000 times: {search_time:.5f} s (~{search_time / 1000:.9f} s/check) average O(1)",
    )
    print("Demonstrates that set operations remain O(1) on average.")


if __name__ == "__main__":
    main()
