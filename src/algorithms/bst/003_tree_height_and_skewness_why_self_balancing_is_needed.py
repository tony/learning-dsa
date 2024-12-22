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

import random
import timeit
from collections import deque


class BSTNode:
    """
    A simple BST node for demonstration: each node has a value, a left child, and a right child.
    We'll keep this minimal for clarity. No balancing logic here.
    """

    def __init__(self, val: int) -> None:
        self.val = val
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


def insert_iterative(root: BSTNode | None, val: int) -> BSTNode:
    """
    Iteratively insert 'val' into the BST, avoiding deep recursion.
    Returns the (possibly new) root.

    Examples
    --------
    >>> root = None
    >>> for x in [3,1,2]:
    ...     root = insert_iterative(root, x)
    >>> # The tree might be skewed or partially skewed:
    >>> #    3
    >>> #   /
    >>> #  1
    >>> #   \
    >>> #    2
    >>> height_iterative(root)
    3
    """
    if root is None:
        return BSTNode(val)

    current = root
    while True:
        if val < current.val:
            if current.left is None:
                current.left = BSTNode(val)
                break
            current = current.left
        # duplicates go right, or assume no duplicates
        elif current.right is None:
            current.right = BSTNode(val)
            break
        else:
            current = current.right

    return root


def height_iterative(root: BSTNode | None) -> int:
    """
    Iteratively compute the height of the BST using a BFS approach.
    An empty tree has height=0. A single node has height=1.

    Examples
    --------
    >>> root = None
    >>> height_iterative(root)
    0
    >>> root = BSTNode(10)
    >>> height_iterative(root)
    1
    >>> for val in [5,4,3,2,1]:
    ...     root = insert_iterative(root, val)
    >>> height_iterative(root)  # can become large if inserted in descending order
    6
    """
    if root is None:
        return 0

    max_height = 0
    queue = deque([(root, 1)])  # (node, level)
    while queue:
        node, level = queue.popleft()
        max_height = max(level, max_height)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return max_height


def main() -> None:
    """
    Main demonstration:
    We'll construct two BSTs of size n:
      1) Insert ascending values (0..n-1), measuring final height (worst-case ~n).
      2) Insert random values, measuring final height (typical average ~O(log n)) if distribution is balanced.

    By using iterative insert and iterative height, we avoid Python recursion limits.
    We show how naive BST degrade with sorted data, emphasizing self-balancing need.
    """
    n = 2000

    # 1) Ascending insertion
    def build_ascending() -> int:
        root = None
        for i in range(n):
            root = insert_iterative(root, i)
        return height_iterative(root)

    # 2) Random insertion
    def build_random() -> int:
        root = None
        values = list(range(n))
        random.shuffle(values)
        for v in values:
            root = insert_iterative(root, v)
        return height_iterative(root)

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
        "demonstrating how naive BST can degrade in the worst-case and motivate self-balancing.",
    )


if __name__ == "__main__":
    main()
