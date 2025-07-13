#!/usr/bin/env python
"""
5. Queues.

Data Structure: Queue (FIFO) implemented via `collections.deque`

Concepts:
A queue is a First-In-First-Out (FIFO) data structure. We enqueue (append) items at one end and
dequeue (popleft) them from the other end.
Using `collections.deque`, both enqueue and dequeue operations are O(1) amortized.

Complexities:
- Enqueue (append): O(1) amortized
- Dequeue (popleft): O(1) amortized
- Peek (front element): O(1) by accessing the leftmost item
- Worst-case and best-case are effectively O(1) amortized for these operations.
- Space: O(n) to store n items.

Narrative:
In a data analytics pipeline, a queue can manage tasks in the order they arrive. For example, we
can queue raw data lines for processing. Each line is processed in arrival order, ensuring fairness
and predictability. The O(1) amortized operations keep the pipeline efficient, even as the number
of tasks grows large.

Doctests:
Check enqueue/dequeue operations and ensure FIFO order.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to test.
"""

from collections import deque
from typing import Any


class Queue:
    """
    A simple Queue using collections.deque for O(1) amortized enqueue/dequeue operations.

    Examples
    --------
    >>> q = Queue()
    >>> q.is_empty()
    True
    >>> q.enqueue(10)
    >>> q.enqueue(20)
    >>> q.peek()
    10
    >>> q.dequeue()
    10
    >>> q.peek()
    20
    >>> q.is_empty()
    False
    >>> q.dequeue()
    20
    >>> q.is_empty()
    True
    >>> try:
    ...     q.dequeue()
    ... except IndexError as e:
    ...     print(e)
    dequeue from empty queue
    >>> try:
    ...     q.peek()
    ... except IndexError as e:
    ...     print(e)
    peek from empty queue
    """

    def __init__(self) -> None:
        self._data = deque()  # type: deque[Any]

    def enqueue(self, item: Any) -> None:
        """Add an item to the rear of the queue."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """Remove and return the item at the front of the queue.

        Raises
        ------
        IndexError
            If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Any:
        """Return the front item without removing it.

        Raises
        ------
        IndexError
            If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Return the number of items in the queue."""
        return len(self._data)


def main() -> None:
    """
    Demonstrate main functionality.

    We'll measure enqueue/dequeue times for large n to show O(1) amortized performance.

    Narrative:
    By efficiently managing incoming tasks in FIFO order, the queue ensures that
    the pipeline processes data as it arrives without delay from reordering steps.
    O(1) amortized enqueue/dequeue keeps this scaling well as n grows.
    """
    import timeit

    n = 1_000_000
    q = Queue()

    # Time enqueuing n items
    enqueue_time = timeit.timeit(lambda: q.enqueue(1), number=n)
    # Time dequeuing n items
    dequeue_time = timeit.timeit(q.dequeue, number=n)

    print(
        f"Enqueuing {n} items took: {enqueue_time:.5f}s (~{enqueue_time / n:.9f}s each)",
    )
    print(
        f"Dequeuing {n} items took: {dequeue_time:.5f}s (~{dequeue_time / n:.9f}s each)",
    )
    print("Both enqueue and dequeue show O(1) amortized performance for large n.")


if __name__ == "__main__":
    main()
