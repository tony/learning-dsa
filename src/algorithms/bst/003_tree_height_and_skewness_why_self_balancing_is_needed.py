#!/usr/bin/env python
"""
3. Tree Height and Skewness: Why Self-Balancing Is Needed.

Concepts:
- Height of a BST is the longest path from root to leaf.
- Inserting ascending values (1,2,3,4,...) can lead to a skewed BST shaped like a linked list.
- Skewed BST yields worst-case operations of O(n).

No single new algorithm here, but we illustrate the problem that motivates balancing.

Complexities:
- Demonstrates that naive BST can degrade from average O(log n) to worst-case O(n) if data is unlucky.

Narrative:
In SRAS, if data is partially sorted or arrives in ascending/descending order (like route IDs),
a naive BST becomes a performance bottleneck (O(n) per operation). We must consider
self-balancing BST solutions.
"""

from __future__ import annotations

import random
import timeit


class BSTNode:
    """
    A simple BST node for demonstration: each node has a value, a left child, and a right child.

    We'll keep this minimal for clarity. No balancing logic here.
    """

    def __init__(self, val: int) -> None:
        self.val = val
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


def insert(root: BSTNode | None, val: int) -> BSTNode:
    """
    Insert 'val' into the BST rooted at 'root'. Returns the (possibly new) root.

    Examples
    --------
    >>> root = None
    >>> for x in [3,1,2]:
    ...     root = insert(root, x)
    >>> # The tree is now skewed or partial:
    >>> #    3
    >>> #   /
    >>> #  1
    >>> #   \
    >>> #    2
    >>> height(root)
    3
    """
    if root is None:
        return BSTNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        # assume duplicates go right or no duplicates exist
        root.right = insert(root.right, val)
    return root


def height(root: BSTNode | None) -> int:
    """
    Return the height of the BST (longest path from root to leaf).

    An empty tree has height 0. A single node has height 1.

    Examples
    --------
    >>> root = None
    >>> height(root)
    0
    >>> root = insert(None, 10)
    >>> height(root)
    1
    >>> for val in [5,4,3,2,1]:
    ...     root = insert(root, val)
    >>> height(root)  # can become large if inserted in descending order
    6
    """
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def main() -> None:
    """
    Main demonstration:
    We'll construct two BSTs of size n:
      1) Insert ascending values (1..n), measuring final height (worst-case ~n).
      2) Insert random values, measuring final height (average ~O(log n)) if distribution is balanced.

    We illustrate how naive BST can degrade with sorted data, emphasizing why self-balancing is needed.
    """
    n = 2000

    # 1) Ascending insertion
    def build_ascending() -> int:
        root = None
        for i in range(n):
            root = insert(root, i)
        return height(root)

    # 2) Random insertion
    def build_random() -> int:
        root = None
        values = list(range(n))
        random.shuffle(values)
        for v in values:
            root = insert(root, v)
        return height(root)

    ascending_time = timeit.timeit(build_ascending, number=1)
    random_time = timeit.timeit(build_random, number=1)

    asc_height = build_ascending()
    rand_height = build_random()

    print(
        f"Inserting ascending [0..{n - 1}] took {ascending_time:.5f}s. Final height: {asc_height}",
    )
    print(
        f"Inserting random {n} values took {random_time:.5f}s. Final height: {rand_height}",
    )
    print(
        f"Observation: Ascending insertion yields near-linear height (~{asc_height}), "
        f"while random insertion typically yields a smaller height (~{rand_height}), "
        "demonstrating how naive BST can degrade in worst-case.",
    )


if __name__ == "__main__":
    main()
