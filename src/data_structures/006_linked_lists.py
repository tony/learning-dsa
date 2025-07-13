#!/usr/bin/env python
"""
6. Linked Lists (Singly Linked).

Data Structure: Singly Linked List

Concepts:
A singly linked list is a sequence of nodes where each node holds a value and a pointer
to the next node. Insertion at the head is O(1), as we just adjust the head pointer.
If we also keep a tail pointer, insertion at the tail can be O(1). Without a tail pointer,
inserting at the tail would require O(n) to find the end.

Searching or accessing an element by index is O(n), as we must traverse from the head.
No random access is available. Space is O(n) to store n nodes.

Complexities:
- Insert at head: O(1)
- Insert at tail:
  - O(1) if tail pointer is maintained
  - O(n) if we must traverse to find the end
- Search: O(n)
- Space: O(n)

Narrative:
In our pipeline, a singly linked list might manage certain specialized pipelines or store
undo operations. For example, we can quickly add steps at the head or tail if we maintain
a tail pointer, but searching through the list is O(n), so it's less suitable for quick lookups
than arrays or balanced trees. Still, O(1) insertion at ends can be handy for certain tasks.

Doctests:
We'll show inserting at head, tail (with tail pointer), and searching.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

from collections.abc import Generator
from typing import Any


class Node:
    """A node in a singly linked list."""

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Node | None = None


class SinglyLinkedList:
    """
    A singly linked list with head and tail pointers for O(1) insertion at both ends.

    Examples
    --------
    >>> lst = SinglyLinkedList()
    >>> lst.is_empty()
    True
    >>> lst.insert_head(10)
    >>> lst.insert_head(5)
    >>> lst.insert_tail(20)
    >>> lst.is_empty()
    False
    >>> len(lst)
    3
    >>> lst.search(10)
    True
    >>> lst.search(99)
    False
    >>> # Check order: head should be 5, then 10, then 20 at tail.
    >>> [node for node in lst]  # iterate through
    [5, 10, 20]
    """

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size = 0

    def insert_head(self, value: Any) -> None:
        """Insert a new node at the head of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self._size == 0:
            self.tail = new_node
        self._size += 1

    def insert_tail(self, value: Any) -> None:
        """Insert a new node at the tail of the list."""
        new_node = Node(value)
        if self.tail is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            # list is empty, so new node is both head and tail
            self.head = new_node
            self.tail = new_node
        self._size += 1

    def search(self, value: Any) -> bool:
        """Search for a value in the list."""
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self._size == 0

    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        return self._size

    def __iter__(self) -> Generator[str]:
        """Iterate through the linked list values."""
        current = self.head
        while current:
            yield current.value
            current = current.next


def main() -> None:
    """
    Demonstrate main functionality.

    We'll show timing for insertion at head and tail vs searching.
    Insertions at head and tail are O(1) with tail pointer.
    Searching is O(n).

    Narrative:
    If we need a structure where we frequently add steps at start or end (like an undo log),
    a singly linked list works well for insertion. But searching for a particular value
    requires O(n).
    This trade-off might be acceptable depending on the pipeline's needs.
    """
    import timeit

    n = 100_000
    lst = SinglyLinkedList()

    # Time insertions at head
    head_insert_time = timeit.timeit(lambda: lst.insert_head(1), number=n)
    # Time insertions at tail
    tail_insert_time = timeit.timeit(lambda: lst.insert_tail(1), number=n)
    # Populate the list fully for searching
    # After these insertions, list length = 2*n
    search_time = timeit.timeit(lambda: lst.search(n - 1), number=10)

    print(
        f"Inserting {n} items at head: {head_insert_time:.5f} s total "
        f"(~{head_insert_time / n:.9f} s per op)",
    )
    print(
        f"Inserting {n} items at tail: {tail_insert_time:.5f} s total "
        f"(~{tail_insert_time / n:.9f} s per op)",
    )
    print("Both near O(1) operations per insertion due to tail pointer.")
    print(
        f"Searching in a list of size {len(lst)}: {search_time:.5f} s for 10 searches "
        f"(~{search_time / 10:.9f} s per search)",
    )
    print("Searching is O(n), as expected.")


if __name__ == "__main__":
    main()
