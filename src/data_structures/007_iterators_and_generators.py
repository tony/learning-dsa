#!/usr/bin/env python
"""
7. Iterators and Generators for Data Traversal.

Data Structure: *Conceptual* (Iterator/Generator protocol, not a separate data structure)

Concepts:
- Iterators in Python follow the iterator protocol, providing __iter__() and __next__() methods.
- Generators are a high-level way to create iterators using 'yield'.
- Complexity: Typically O(1) to move to the next element, as we just fetch the next item.
- Space: O(1) for iterator state, since we don't store the entire dataset at once.
- Best case: If the underlying data allows O(1) retrieval of the next item, iteration steps are
  O(1).
- Worst case: If underlying data access is expensive, complexity reflects that. But the iterator
  itself adds minimal overhead.

Narrative:
In a large data analytics pipeline, using iterators and generators lets us handle massive datasets
lazily. Instead of loading millions of lines into memory at once, we yield lines one by one.
Processing can start immediately, memory usage stays low, and complexity per step is O(1).
This approach supports scalable, memory-efficient streaming of large datasets.

Doctests:
We'll show a custom iterator and a generator function to demonstrate iteration.
Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

from collections.abc import Iterator
from typing import Any


class MyIterator:
    """
    A simple custom iterator class that yields elements from a provided list, one at a time.

    Complexity:
    - next() call: O(1) to return the next element and advance state
    - Space: O(1) for state, the original list is externally stored

    Examples
    --------
    >>> it = MyIterator([10,20,30])
    >>> next(it)
    10
    >>> next(it)
    20
    >>> next(it)
    30
    >>> # StopIteration after last element:
    >>> next(it)
    Traceback (most recent call last):
    ...
    StopIteration
    """

    def __init__(self, data: list[Any]) -> None:
        self._data = data
        self._index = 0

    def __iter__(self) -> "MyIterator":
        """Return the iterator object itself."""
        return self

    def __next__(self) -> Any:
        """Return the next item from the iterator."""
        if self._index < len(self._data):
            val = self._data[self._index]
            self._index += 1
            return val
        raise StopIteration


def my_generator(data: list[Any]) -> Iterator[Any]:
    """
    Yield elements from the provided list.

    Complexity per next element: O(1) to yield and advance.
    Space: O(1).

    Examples
    --------
    >>> gen = my_generator([1,2,3])
    >>> next(gen)
    1
    >>> next(gen)
    2
    >>> next(gen)
    3
    >>> next(gen)
    Traceback (most recent call last):
    ...
    StopIteration
    """
    yield from data


def main() -> None:
    """
    Demonstrate main functionality.

    We'll show that iterating over a large list using an iterator or generator
    doesn't require holding all processed data in memory at once, and each step is O(1).

    Narrative:
    For huge datasets, we can start processing lines as soon as we fetch them,
    keeping memory usage low and complexity per step O(1) (just the next element retrieval).
    """
    import timeit

    n = 1_000_000
    data = list(range(n))

    # Measure iteration over data using a generator expression:
    # O(1) per iteration step, total O(n) for n steps.
    iteration_time = timeit.timeit(lambda: sum(my_generator(data)), number=1)
    print(f"Summing {n} elements using a generator: {iteration_time:.5f}s")
    # Just demonstrates that we can handle large data iteratively without huge memory overhead.


if __name__ == "__main__":
    main()
