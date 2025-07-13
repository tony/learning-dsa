#!/usr/bin/env python
"""
17. Using `itertools` for Combinatorial Generation.

Algorithm: Generating permutations/combinations with itertools

Concepts:
- `itertools.permutations(iterable, r)` generates r-length permutations of the given
iterable,
  in O(n!) time for the full length permutations.
- `itertools.combinations(iterable, r)` generates r-length combinations in O(C(n, r)).
- These methods are powerful for enumerating possibilities, but factorial growth means
  we must be careful when n is more than a small handful.

Complexities:
- Generating all permutations of length n: O(n!) time, each permutation is an O(n)
tuple space.
- Generating combinations of length r from n: O(C(n, r)) which can also be large.
- Memory usage: For each yielded permutation/combination, we hold an O(r) tuple.

Narrative:
In an SRAS pipeline, we might want to generate candidate groupings of deliveries or possible routes.
While `itertools` is convenient for small or moderate n, factorial or combinatorial growth
quickly becomes infeasible for large n. This is still invaluable for exploring smaller subsets
or partial solutions.

Doctests:
We show small examples of permutations and combinations.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import itertools
import timeit
from typing import Any


def demonstrate_permutations(data: list[Any], r: int) -> None:
    """
    Print permutations of the list 'data' taken r at a time.

    Examples
    --------
    >>> demonstrate_permutations([1, 2, 3], 2)
    (1, 2)
    (1, 3)
    (2, 1)
    (2, 3)
    (3, 1)
    (3, 2)
    """
    for perm in itertools.permutations(data, r):
        print(perm)


def demonstrate_combinations(data: list[Any], r: int) -> None:
    """
    Print combinations of the list 'data' taken r at a time.

    Examples
    --------
    >>> demonstrate_combinations([1, 2, 3], 2)
    (1, 2)
    (1, 3)
    (2, 3)
    """
    for comb in itertools.combinations(data, r):
        print(comb)


def main() -> None:
    """
    Main demonstration:

    We'll measure time for generating permutations of a small list.
    Even for moderate n, factorial growth can become large quickly.

    Narrative:
    For generating route permutations or candidate groupings in SRAS,
    itertools is invaluable for smaller sets, but remember n! is huge even at modest n.
    """
    n = 8  # permutations of 8 items => 40320 permutations
    data = list(range(n))

    # We'll measure how long it takes to just iterate over permutations
    exec_time = timeit.timeit(lambda: list(itertools.permutations(data)), number=1)
    print(
        f"Iterating over all permutations of {n} items took: {exec_time:.5f}s (there are {len(list(itertools.permutations(data)))})",
    )

    # Similarly for combinations
    r = 4
    comb_time = timeit.timeit(lambda: list(itertools.combinations(data, r)), number=1)
    print(
        f"Iterating over combinations C({n},{r}) took: {comb_time:.5f}s. (count={len(list(itertools.combinations(data, r)))})",
    )


if __name__ == "__main__":
    main()
