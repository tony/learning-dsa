#!/usr/bin/env python
"""
8. Hash Tables (Python dict).

Data Structure: Hash Table (Python's built-in dict)

Concepts:
A hash table uses a hash function to map keys to buckets. Python's dict is a dynamic hash table.
- Average complexity: O(1) for insert, search, delete.
- Worst case: O(n) if all elements end up in the same bucket (rare due to good hash distribution).
- Space: O(n) to store n key-value pairs.

Complexities:
- Insert: Average O(1), Worst O(n)
- Search: Average O(1), Worst O(n)
- Delete: Average O(1), Worst O(n)
- Space: O(n)

Narrative:
Storing metadata tags, product IDs, or quick reference lookups in a data analytics pipeline is common.
A hash table (dict) allows these lookups to be O(1) on average, keeping the pipeline responsive even
as data grows large. This is critical for fast queries on large sets of tags or identifiers.

Doctests:
Show inserting, searching, and deleting from a dict.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit


def demonstrate_dict_operations() -> None:
    """
    Examples
    --------
    >>> d = {}
    >>> d['apple'] = 10  # insert O(1) average
    >>> d['banana'] = 20
    >>> 'apple' in d  # search O(1) average
    True
    >>> d['apple']
    10
    >>> del d['banana']  # delete O(1) average
    >>> 'banana' in d
    False
    """


def main() -> None:
    """
    Main demonstration:
    We'll measure insertion and lookup times in a Python dict for large n.
    Should show O(1) average performance.

    Narrative:
    For large sets of tags or keys in the pipeline, dict operations remain O(1) on average,
    ensuring quick metadata queries as data expands.
    """
    n = 1_000_000
    d: dict[int, int] = {}
    # Time inserting n items
    insert_time = timeit.timeit(lambda: d.__setitem__(len(d), 1), number=n)

    # Time searching an existing key (like n-1) multiple times
    search_time = timeit.timeit(lambda: (n - 1 in d), number=1000)

    print(
        f"Inserting {n} items into dict took: {insert_time:.5f}s total (~{insert_time / n:.9f}s per insert)",
    )
    print(
        f"Checking membership of a key 1000 times took: {search_time:.5f}s (~{search_time / 1000:.9f}s per check)",
    )
    print(
        "Average O(1) behavior demonstrated. Worst-case O(n) is rare with good hash distribution.",
    )


if __name__ == "__main__":
    main()
