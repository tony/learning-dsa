#!/usr/bin/env python
"""
13. Recursion vs. Iteration: Tail Recursion Elimination Example.

Algorithm: Tail Recursion conversion to Iteration

Concepts:
- A tail-recursive function is one where the final operation is the recursive call itself.
- In many languages, tail calls can be optimized to reuse the same stack frame, but Python doesn't do this.
- Converting tail recursion to iteration avoids deep recursion overhead and stack limits for large n.

Complexities:
- Both tail recursion and iterative approach typically run in O(n) if the underlying operation is O(1) each iteration step.
- Space: Iteration uses O(1) additional space, while naive recursion in Python can use O(n) call stack.

Narrative:
In an SRAS pipeline, certain tasks may conceptually be written recursively. However, large data
or deep calls can exceed Python’s recursion limit or cause overhead. Transforming tail recursion
into iteration helps keep memory usage low and avoid hitting recursion limits.

Doctests:
We'll define a simple sum_to_n function in both recursive (tail) style and iterative style
to illustrate correctness. Then we'll time them on moderate n in main().

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import sys
import timeit

sys.setrecursionlimit(
    10**7,
)  # just to reduce chance of hitting recursion limit for moderate tests


def tail_recursive_sum(n: int, accumulator: int = 0) -> int:
    """
    Sums integers from 1 to n using a tail-recursive approach.

    Python doesn't optimize tail calls, so large n can cause deep recursion.

    Examples
    --------
    >>> tail_recursive_sum(1)
    1
    >>> tail_recursive_sum(5)
    15
    >>> tail_recursive_sum(0)
    0
    >>> tail_recursive_sum(10)
    55
    """
    if n == 0:
        return accumulator
    return tail_recursive_sum(n - 1, accumulator + n)


def iterative_sum(n: int) -> int:
    """
    Sums integers from 1 to n in an iterative manner, avoiding recursion entirely.

    Examples
    --------
    >>> iterative_sum(1)
    1
    >>> iterative_sum(5)
    15
    >>> iterative_sum(0)
    0
    >>> iterative_sum(10)
    55
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def main() -> None:
    """
    Main demonstration:

    We'll pick a moderately large n, time both the tail-recursive approach
    and the iterative approach to sum 1..n. We illustrate that Python’s tail recursion
    doesn't get optimized, so iteration may be faster and won't risk hitting recursion depth limits.

    Narrative:
    In an SRAS pipeline, rewriting tail recursion as iteration
    avoids stack overflows and overhead for large data tasks.
    """
    n = 200_000

    # Time tail recursion
    tail_time = timeit.timeit(lambda: tail_recursive_sum(n), number=1)
    # Time iteration
    iter_time = timeit.timeit(lambda: iterative_sum(n), number=1)

    print(f"Tail-recursive sum(1..{n}) took: {tail_time:.5f}s")
    print(f"Iterative sum(1..{n}) took:      {iter_time:.5f}s")


if __name__ == "__main__":
    main()
