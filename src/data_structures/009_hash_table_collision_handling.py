#!/usr/bin/env python
"""
9. Hash Table Collision Handling (Chaining).

Data Structure: Hash Table with Chaining

Concepts:
When a hash collision occurs (two keys hash to the same bucket), chaining stores collided elements
in a linked list at that bucket. Average complexity stays O(1) for insert/search/delete if the
chains remain short. Worst-case O(n) if all keys cluster in the same chain.

Complexities:
- Insert: Average O(1), Worst O(n) if unlucky distribution
- Search: Average O(1), Worst O(n)
- Delete: Average O(1), Worst O(n)
- Space: O(n) for storing all elements plus linked lists for chains.

Narrative:
As our data grows large (e.g., large volumes of tags or product IDs), even with hash tables we must handle collisions.
Chaining provides a simple method: keep a linked list for all keys that share a bucket. Usually keys distribute well,
preserving O(1) operations on average. If too many collide, performance can degrade, prompting better hash functions
or resizing strategies.

Doctests:
We'll use `print(h.search("key"))` to ensure the return value is shown as output.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

from typing import Any


class ChainedHashTable:
    """
    A basic hash table using chaining for collision resolution.

    We'll use Python's built-in hash and modulo a fixed size for simplicity.
    In practice, you'd resize and rehash as needed, but we focus on collision strategy here.

    Examples
    --------
    >>> h = ChainedHashTable(size=10)
    >>> h.insert("apple", 10)
    >>> h.insert("banana", 20)
    >>> print(h.search("apple"))
    10
    >>> print(h.search("banana"))
    20
    >>> print(h.search("cherry"))
    None
    >>> h.delete("banana")
    True
    >>> print(h.search("banana"))
    None
    """

    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.table: list[list[tuple[Any, Any]]] = [[] for _ in range(self.size)]

    def _hash(self, key: Any) -> int:
        return hash(key) % self.size

    def insert(self, key: Any, value: Any) -> None:
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        chain = self.table[index]
        for i, (k, _v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return
        chain.append((key, value))

    def search(self, key: Any) -> Any | None:
        """Search for a key and return its value if found."""
        index = self._hash(key)
        chain = self.table[index]
        for k, v in chain:
            if k == key:
                return v
        return None

    def delete(self, key: Any) -> bool:
        """Delete a key-value pair and return True if successful."""
        index = self._hash(key)
        chain = self.table[index]
        for i, (k, _v) in enumerate(chain):
            if k == key:
                del chain[i]
                return True
        return False


def main() -> None:
    """
    Demonstrate main functionality.

    We'll measure insert/search times. Insertions remain O(1) average if distribution is good.
    Searching is O(1) average, but can degrade if many items collide in the same chain.

    Narrative:
    With chaining, we can handle collisions gracefully. Large volumes of tags or keys will
    still operate near O(1) unless they cluster badly. In a stable scenario, chaining keeps
    hash operations fast, aiding the pipeline's quick lookups.
    """
    import timeit

    n = 100_000
    h = ChainedHashTable(size=10000)  # Larger table reduces collision probability

    # Insert n items
    insert_time = timeit.timeit(lambda: h.insert(hash(len(h.table)), 1), number=n)
    # Search a key known to exist (not realistic but demonstrates O(1) average)
    search_time = timeit.timeit(lambda: h.search(hash(len(h.table)) - 1), number=1000)

    print(
        f"Inserting {n} items took: {insert_time:.5f} s total (~{insert_time / n:.9f} s/insert)",
    )
    print(
        f"Searching an existing key 1000 times took: {search_time:.5f} s (~{search_time / 1000:.9f} s/search)",
    )
    print("Operations show near O(1) average performance with good distribution.")


if __name__ == "__main__":
    main()
