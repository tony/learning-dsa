#!/usr/bin/env python
"""
12. Divide and Conquer Beyond Sorting: Closest Pair of Points.

Algorithm: Closest Pair of Points (Divide and Conquer)

Concepts:
- We have a set of 2D points.
- We split them by x-coordinate into two halves, recursively find the closest pair in
each half,
  then inspect points near the dividing line (within distance d) for a potentially closer pair.
- This yields O(n log n) time, which is better than the naive O(n^2).

Complexities:
- Time: O(n log n)
- Space: O(n) due to recursion, auxiliary arrays/lists.
- For very small subsets (like 2 or 3 points), a direct O(n^2) check is simpler.

Narrative:
In SRAS or a logistics pipeline, we might want to find two shipments or warehouses that are
closest geographically, possibly to dispatch them together or plan routes efficiently. The
divide-and-conquer approach ensures we can handle large sets of points (e.g., thousands)
in O(n log n) rather than O(n^2), saving significant time.

Doctests:
We'll test a small set of points. We confirm we get the minimal distance accurately.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import math
import operator
import random
import timeit


def dist(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """Euclidean distance between two 2D points."""
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def closest_pair(points: list[tuple[float, float]]) -> float:
    """
    Return the minimal distance between any two points in the list using.

    a divide-and-conquer approach.

    Complexity: O(n log n)
    Space: O(n)

    Examples
    --------
    >>> pts = [(0,0), (3,4), (1,1), (2,2)]
    >>> round(closest_pair(pts), 4)
    1.4142
    >>> # Explanation: points (1,1) and (2,2) are sqrt(2)=1.4142... apart,
    >>> # which is the minimal distance.
    """
    # Sort points by x-coordinate initially

    pts_sorted_x = sorted(points, key=operator.itemgetter(0))
    # A helper array sorted by y will be used in recursion or we can do it on the fly
    return _closest_pair_rec(pts_sorted_x)


def _closest_pair_rec(pts_x: list[tuple[float, float]]) -> float:
    n = len(pts_x)
    # Base case: If 2 or 3 points, do a naive O(n^2) check
    if n <= 3:
        return _naive_closest_pair(pts_x)

    mid = n // 2
    left_half = pts_x[:mid]
    right_half = pts_x[mid:]

    # Recurse on left and right
    d_left = _closest_pair_rec(left_half)
    d_right = _closest_pair_rec(right_half)
    d = min(d_left, d_right)

    # Determine the dividing x-line (the mid point's x)
    mid_x = pts_x[mid][0]

    # Build a "strip" of points whose x is within d of mid_x
    strip = [p for p in pts_x if abs(p[0] - mid_x) < d]

    # Sort strip by y
    strip.sort(key=operator.itemgetter(1))

    # Check at most next 6 points in the strip, for each point, per standard proof
    d_strip = _closest_strip_pair(strip, d)
    return min(d, d_strip)


def _naive_closest_pair(pts: list[tuple[float, float]]) -> float:
    min_d = float("inf")
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            min_d = min(min_d, dist(pts[i], pts[j]))
    return min_d


def _closest_strip_pair(strip: list[tuple[float, float]], d: float) -> float:
    """
    For points in the strip (sorted by y),.

    check each point against up to next 6 points in the strip to find a smaller distance.
    """
    min_d = d

    n = len(strip)
    for i in range(n):
        j = i + 1
        while j < n and (strip[j][1] - strip[i][1]) < min_d:
            min_d = min(min_d, dist(strip[i], strip[j]))
            j += 1
    return min_d


def main() -> None:
    """
    Demonstrate main functionality.

    We'll create n random 2D points, measure time for finding the closest pair via
    the divide-and-conquer approach. This demonstrates O(n log n) complexity.

    Narrative:
    Finding the two geographically closest shipments among thousands in SRAS can be done
    in O(n log n) instead of O(n^2), saving significant computation time for large data sets.
    """
    n = 5000

    points = [(random.uniform(0, 10000), random.uniform(0, 10000)) for _ in range(n)]

    exec_time = timeit.timeit(lambda: closest_pair(points), number=1)
    print(f"Closest pair among {n} points took: {exec_time:.5f}s (O(n log n)).")


if __name__ == "__main__":
    main()
