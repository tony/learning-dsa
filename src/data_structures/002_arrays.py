#!/usr/bin/env python
"""
2. Arrays and Python Lists.

Context
-------
This lesson explores the difference between fixed-size arrays (common in lower-level languages)
and Python’s dynamic `list` type, which automatically resizes as needed. We’ll implement a
simple dynamic array from scratch to show the underlying concept, then compare it with Python’s
built-in `list`.

Prerequisites:
- Basic understanding of Python lists and indexing.
- Familiarity with the concept of complexity from the previous lesson.

References
----------
- Python lists: https://docs.python.org/3/tutorial/datastructures.html
- Array vs. list concepts: https://en.wikipedia.org/wiki/Dynamic_array

Summary
-------
We will:
- Discuss how arrays are typically fixed-size and how a dynamic array grows to accommodate more elements.
- Implement a simplified dynamic array in Python.
- Compare insertion performance and usage with Python’s `list`.
- Narrative scenario: Imagine streaming data lines from a CSV file. Initially, we don’t know how many lines
  we’ll receive, so a dynamic structure is beneficial.

By the end, learners will understand why Python’s `list` is so convenient, how it achieves amortized O(1) append,
and the difference between a low-level fixed array and a high-level dynamic structure.

Doctests:
- We’ll test basic functionality of our custom dynamic array.
- Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit
from typing import Any


class DynamicArray:
    """
    A simplified dynamic array implementation.

    Internally:
    - Uses a Python list as a static array to store elements.
    - When capacity is reached, it creates a new, larger list and copies elements over.

    Complexity:
    - Amortized O(1) append, similar to Python’s built-in list.
    - O(n) worst-case when resizing.

    Examples
    --------
    >>> arr = DynamicArray()
    >>> arr.append(10)
    >>> arr.append(20)
    >>> arr[0]
    10
    >>> arr[1]
    20
    >>> len(arr)
    2
    """

    def __init__(self) -> None:
        self._capacity = 1
        self._size = 0
        self._array = [None] * self._capacity

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> Any:
        if 0 <= index < self._size:
            return self._array[index]
        msg = "Index out of bounds"
        raise IndexError(msg)

    def append(self, value: Any) -> None:
        if self._size == self._capacity:
            self._resize(2 * self._capacity)  # Double capacity
        self._array[self._size] = value
        self._size += 1

    def _resize(self, new_capacity: int) -> None:
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity


def main() -> None:
    """
    Main demonstration for this lesson.

    We will:
    - Show how to use our DynamicArray.
    - Compare append performance vs. Python’s built-in list.
    - Narrative: Imagine reading lines from a CSV (simulated with range of strings).

    This demonstration highlights how dynamic resizing works behind the scenes
    and how Python’s list, being a dynamic array, suits scenarios where data size is unknown.
    """
    # Simulate incoming CSV lines
    csv_lines = [f"line_{i}" for i in range(100_000)]

    # Using our DynamicArray
    arr = DynamicArray()
    start = timeit.default_timer()
    for line in csv_lines:
        arr.append(line)
    custom_time = timeit.default_timer() - start

    # Using Python’s list
    py_list = []
    start = timeit.default_timer()
    for line in csv_lines:
        py_list.append(line)
    built_in_time = timeit.default_timer() - start

    print("DynamicArray size:", len(arr))
    print("Python list size:", len(py_list))
    print(f"DynamicArray append time: {custom_time:.5f} s")
    print(f"Python list append time: {built_in_time:.5f} s")

    # Note: Times will vary by machine, but Python’s list should be
    # well-optimized and likely faster than our naive implementation.
    # Both scale linearly and offer amortized O(1) appends,
    # showing the principle behind dynamic arrays.


if __name__ == "__main__":
    main()
