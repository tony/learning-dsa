#!/usr/bin/env python
"""
9. Stability in Sorting & Stable Partitioning.

Concept: Stable sorting and its importance.
Algorithm (Conceptual): Stable partitioning approach

Concepts:
- A stable sort (or stable partition) preserves the relative order of elements that compare
  equal or fall in the same logical group.
- This is crucial if data has already been grouped or partially sorted by one criterion,
  and we apply a second criterion while wanting to keep ties in the original order.

Here, we demonstrate a "stable partition" approach that divides elements into two groups
while preserving the relative order of elements within each group.

Complexities:
- Time: O(n) for the partition itself if we do it in one pass with extra space.
- Space: O(n) to store the partitioned data before copying back.
- If we integrate stable partitioning within a stable sorting algorithm, the sorting complexity
  might be O(n log n), e.g., for mergesort. But here, we only show the conceptual partition step.

Narrative:
In an SRAS pipeline, we might first sort orders by region. Then, within each region,
we want to separate "high-priority" from "low-priority" tasks but preserve the original order
for ties. A stable partition ensures tasks within each priority group remain in the order
they appeared. This is essential if multiple sorting/passes are done sequentially,
and we do not want to lose the tie order from a previous pass.

Doctests:
We show a stable_partition function that groups elements meeting a condition in front
without breaking their original ordering.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

from collections.abc import Callable


def stable_partition(data: list[int], predicate: Callable[[int], bool]) -> None:
    """
    Reorders 'data' so that all elements for which predicate(x) is True come first,

    but the relative ordering among True-Group and False-Group elements remains the same.
    This is done in O(n) time with O(n) extra space, preserving stability.

    Complexity:
    - Time: O(n)
    - Space: O(n) for the extra storage

    Examples
    --------
    >>> nums = [5, 2, 8, 1, 3, 7]
    >>> # Suppose we want to partition all even numbers to the front,
    >>> # but keep their relative order among evens/odds.
    >>> stable_partition(nums, predicate=lambda x: x % 2 == 0)
    >>> nums  # Even elements (2,8) stay in their relative order, odd (5,1,3,7) remain in relative order
    [2, 8, 5, 1, 3, 7]

    >>> nums2 = []
    >>> stable_partition(nums2, lambda x: x < 0)
    >>> nums2
    []
    >>> nums3 = [1, 2, 3]
    >>> stable_partition(nums3, lambda x: x > 5)
    >>> nums3  # no elements match, no reorder
    [1, 2, 3]
    """
    true_group = []
    false_group = []
    for x in data:
        if predicate(x):
            true_group.append(x)
        else:
            false_group.append(x)
    # Combine them, preserving order in each group
    data[:] = true_group + false_group


def main() -> None:
    """
    Main demonstration:

    We'll show stable_partition dividing a list into two groups
    (for example, region A vs. region B in SRAS scenario),
    ensuring each group retains the original relative order of its elements.

    Narrative:
    If we first sorted tasks by one criterion and now want to group them
    by a second criterion without losing the tie ordering from the first,
    stable partition is beneficial. It's O(n) with extra space usage.
    """
    nums = [10, 5, 8, 3, 15, 2, 2, 20, 5]
    print("Original list:", nums)
    # Partition so that elements <= 5 come first, preserving order in each group
    stable_partition(nums, predicate=lambda x: x <= 5)
    print("After stable partition (x <= 5 first):", nums)


if __name__ == "__main__":
    main()
