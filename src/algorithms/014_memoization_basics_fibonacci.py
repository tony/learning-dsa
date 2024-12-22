#!/usr/bin/env python
"""
14. Memoization Basics (Fibonacci Example).

Algorithm: Memoized Fibonacci

Concepts:
- A naive recursive Fibonacci implementation has O(2^n) time, as it recomputes many subproblems.
- By storing previously computed results (memoization), each subproblem is solved once, reducing time to O(n).
- Space: O(n) for the memo, storing fib(k) for k=0..n.

Narrative:
In an SRAS or similar pipeline, repeated calculations (like certain route costs) can benefit from
memoization. By caching results of subproblems, we avoid redundant work and reduce time complexity
from exponential to linear in many dynamic programming scenarios.

Doctests:
We demonstrate naive_fib vs. memo_fib on small n, ensuring correct outputs.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit
from functools import lru_cache


def naive_fib(n: int) -> int:
    """
    Naive recursive Fibonacci: fib(0)=0, fib(1)=1.
    This is O(2^n) time due to repeated subproblem calculations.

    Examples
    --------
    >>> naive_fib(0)
    0
    >>> naive_fib(1)
    1
    >>> naive_fib(5)
    5
    """
    if n < 2:
        return n
    return naive_fib(n - 1) + naive_fib(n - 2)


def memo_fib(n: int, memo: dict[int, int] | None = None) -> int:
    """
    Memoized Fibonacci, O(n) time, O(n) space for memo.

    Examples
    --------
    >>> memo_fib(0)
    0
    >>> memo_fib(1)
    1
    >>> memo_fib(5)
    5
    """
    if memo is None:
        memo = {}
    if n < 2:
        return n
    if n not in memo:
        memo[n] = memo_fib(n - 1, memo) + memo_fib(n - 2, memo)
    return memo[n]


@lru_cache(None)
def fib_lru(n: int) -> int:
    """
    A version using functools.lru_cache for memoization.

    Examples
    --------
    >>> fib_lru(0)
    0
    >>> fib_lru(1)
    1
    >>> fib_lru(5)
    5
    """
    if n < 2:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)


def main() -> None:
    """
    Main demonstration:
    We'll compare times for naive_fib (exponential) vs. memo_fib (linear) on moderately large n.

    Narrative:
    In a large pipeline, naive recursion leads to exponential time for repeated subproblem calculations.
    Memoization caches results, dropping time to O(n). We see a big difference for even moderate n.
    """
    n = 30  # naive fib(30) is still feasible, but we show the time difference

    naive_time = timeit.timeit(lambda: naive_fib(n), number=1)
    memo_time = timeit.timeit(lambda: memo_fib(n), number=1)

    print(f"Naive fib({n}) took:  {naive_time:.5f}s (exponential ~O(2^n))")
    print(f"Memo fib({n}) took:   {memo_time:.5f}s (linear O(n))")


if __name__ == "__main__":
    main()
