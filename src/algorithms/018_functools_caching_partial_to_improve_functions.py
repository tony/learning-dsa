#!/usr/bin/env python
"""
18. Using `functools` (Caching / Partial) to Improve Simple Functions.

Algorithm: Simple caching with `functools.lru_cache`

Concepts:
- We can decorate a function with `@lru_cache(None)` to cache its results. Repeated
calls with
  the same arguments return the cached value, avoiding recomputation.
- Complexity depends on the underlying function. If it's expensive (e.g., CPU-bound or
complex),
  caching drastically reduces repeated-call overhead.
- For memory usage, the cache grows up to its maxsize if set (None = unbounded).

Narrative:
In an SRAS pipeline or similar environment, certain repeated computations (like route costs between
the same warehouses) can benefit from caching. Once computed, further calls with the same inputs
return immediately from cache, accelerating the pipeline significantly.

Doctests:
We'll define a function that simulates an expensive operation (e.g. a route cost).
We confirm repeated calls yield the same result, and highlight that the second call is
fast due to caching. We also check the approximate distance for a known input.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import random
import time
import timeit
from functools import lru_cache
from itertools import starmap


@lru_cache(None)
def route_cost(
    warehouse_a: tuple[float, float],
    warehouse_b: tuple[float, float],
) -> float:
    """
    Simulate a CPU-bound or complex route cost computation.

    We'll sleep a short random time to emulate 'work', then
    return a distance measure (like Euclidean distance).

    Examples
    --------
    >>> cost = route_cost((0, 0), (3, 4))  # emulate a single call
    >>> round(cost, 3)
    5.0
    >>> # The second call with the same args should return instantly from cache:
    >>> cost_again = route_cost((0, 0), (3, 4))
    >>> cost == cost_again
    True
    """
    # Emulate some 'heavy' computation by sleeping a random short time:
    delay = random.uniform(0.005, 0.01)  # 5-10 ms
    time.sleep(delay)

    # Calculate and return a float distance:
    dx = warehouse_a[0] - warehouse_b[0]
    dy = warehouse_a[1] - warehouse_b[1]

    return float(((dx * dx) + (dy * dy)) ** 0.5)


def main() -> None:
    """
    Demonstrate main functionality.

    We'll measure the time for repeated calls to route_cost with or without the cache.

    Narrative:
    If we call route_cost many times with the same arguments in an SRAS pipeline,
    caching avoids repeated 'heavy' computations, drastically reducing total time.
    """
    # We'll define some repeated calls to route_cost with the same pairs
    pairs = [
        ((10.0, 5.0), (3.0, 4.0)),
        ((10.0, 5.0), (3.0, 4.0)),  # repeated
        ((2.0, 2.0), (2.0, 2.0)),
        ((10.0, 5.0), (3.0, 4.0)),  # repeated
        ((5.0, 1.0), (5.0, 10.0)),
        ((10.0, 5.0), (3.0, 4.0)),  # repeated
    ]

    # Time repeated calls with caching (the function is already decorated)
    cache_time = timeit.timeit(lambda: list(starmap(route_cost, pairs)), number=1)
    print(f"Time for repeated route_cost calls with caching: {cache_time:.5f}s")

    # A version without caching for comparison:
    def route_cost_no_cache(a: tuple[float, float], b: tuple[float, float]) -> float:
        delay = random.uniform(0.005, 0.01)
        time.sleep(delay)
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        return float(((dx * dx) + (dy * dy)) ** 0.5)

    def run_no_cache() -> None:
        for p in pairs:
            route_cost_no_cache(*p)

    no_cache_time = timeit.timeit(run_no_cache, number=1)
    print(f"Time for repeated route_cost calls without caching: {no_cache_time:.5f}s")


if __name__ == "__main__":
    main()
