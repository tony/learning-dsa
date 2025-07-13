#!/usr/bin/env python
"""
4. Stacks.

Data Structure: Stack (LIFO)

Concepts:
A stack is a Last-In-First-Out data structure. We push items onto the top and pop items from the
top.
We can implement a stack in Python using `collections.deque` or a list. Using `deque` is typically
more efficient for push/pop at the ends.

Complexities:
- Push (append at end): O(1) amortized
- Pop (pop at end): O(1) amortized
- Peek (check top): O(1)
- Search (if needed): O(n) if we must scan
- Space: O(n)

No best/average/worst differences for push/pop in amortized terms-they're consistently O(1)
amortized with deque.
Worst case scenario: if large memory reallocations occur rarely in a list, push/pop could degrade,
but with `deque` this is stable O(1).

Narrative:
In our data analytics pipeline, a stack can help manage tasks in a LIFO manner. For example, if we
have a series of transformation steps and want to easily undo the most recent step, a stack provides
O(1) push/pop operations, making undo operations efficient.

Doctests:
Check basic stack operations: push, pop, peek (just check the last element), and confirm the LIFO
order.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

from collections import deque
from typing import Any


class Stack:
    """
    A simple Stack using collections.deque for O(1) amortized push/pop operations.

    Examples
    --------
    >>> s = Stack()
    >>> s.is_empty()
    True
    >>> s.push(10)
    >>> s.push(20)
    >>> s.peek()
    20
    >>> s.pop()
    20
    >>> s.peek()
    10
    >>> s.is_empty()
    False
    >>> s.pop()
    10
    >>> s.is_empty()
    True
    >>> try:
    ...     s.pop()
    ... except IndexError as e:
    ...     print(e)
    pop from empty stack
    >>> try:
    ...     s.peek()
    ... except IndexError as e:
    ...     print(e)
    peek from empty stack
    """

    def __init__(self) -> None:
        self._data = deque()  # type: deque[Any]

    def push(self, item: Any) -> None:
        """Push an item onto the stack."""
        self._data.append(item)

    def pop(self) -> Any:
        """Pop and return the top item from the stack.

        Raises
        ------
        IndexError
            If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any:
        """Return the top item without removing it.

        Raises
        ------
        IndexError
            If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Return the number of items in the stack."""
        return len(self._data)


def main() -> None:
    """
    Demonstrate main functionality.

    We'll show timing of multiple push/pop operations to highlight O(1) amortized complexity.

    Narrative:
    If we need a quick structure to revert transformations or hold temporary tasks in LIFO order,
    stacks fit perfectly into the analytics pipeline. Even if we have thousands of steps,
    O(1) push/pop ensures quick undo/redo or backtracking steps.
    """
    import timeit

    n = 1_000_000
    s = Stack()

    # Time pushing n items
    push_time = timeit.timeit(lambda: s.push(1), number=n)
    # Time popping n items
    pop_time = timeit.timeit(s.pop, number=n)

    print(
        f"Pushing {n} items took: {push_time:.5f}s for {n} operations (~{push_time / n:.9f}s each)",
    )
    print(
        f"Popping {n} items took: {pop_time:.5f}s for {n} operations (~{pop_time / n:.9f}s each)",
    )
    print("Both push and pop show O(1) amortized performance.")


if __name__ == "__main__":
    main()
