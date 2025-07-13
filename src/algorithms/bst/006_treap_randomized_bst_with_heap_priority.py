#!/usr/bin/env python
"""
6. Treap: Randomized BST with Heap Priority.

Concepts:
- Each node has a key (BST order) plus a random priority (heap property).
- Insert in BST key order, then rotate up if the child's priority violates the parent's
heap condition.
- Expected O(log n) height if priorities are uniformly random.

Algorithm:
- Insert:
  1. Insert by BST key (recursively or iteratively).
  2. Assign random priority.
  3. Rotate up (single rotations) if child's priority is “better” than its parent
     (depending on min-heap or max-heap approach).
- Delete:
  1. Rotate node down until it's a leaf, then remove it (omitted here for brevity).

Complexities:
- Expected O(log n) for all BST operations, thanks to randomization ensuring balanced
shape on average.

Narrative:
Treaps can be simpler to implement than Red-Black or AVL trees. In an SRAS environment,
if we dislike complex balancing rules, a Treap with random priorities provides expected O(log n) performance.
"""

from __future__ import annotations

import random


class TreapNode:
    """
    Node in a Treap:

    - key: BST key
    - priority: random priority, ensures heap property
    - left, right: child pointers.
    """

    def __init__(self, key: int) -> None:
        self.key = key
        self.priority = random.random()  # or random.randint(...) for int priority
        self.left: TreapNode | None = None
        self.right: TreapNode | None = None


def rotate_left(root: TreapNode) -> TreapNode:
    """
    Perform a left rotation on 'root'. Return the new subtree root (y).

    We assume root.right is not None; caller checks if needed.
    """
    y = root.right
    if y is None:
        return root  # no rotation possible
    root.right = y.left
    y.left = root
    return y  # y is new root of this subtree


def rotate_right(root: TreapNode) -> TreapNode:
    """
    Perform a right rotation on 'root'. Return the new subtree root (y).

    We assume root.left is not None; caller checks if needed.
    """
    y = root.left
    if y is None:
        return root
    root.left = y.right
    y.right = root
    return y


def insert_treap(root: TreapNode | None, key: int) -> TreapNode:
    """
    Insert 'key' into the Treap, returning the possibly new subtree root.

    1) Standard BST insert by key.
    2) Assign random priority at creation.
    3) Rotate up if child's priority is higher (for max-heap) or lower (for min-heap).
       We'll do a 'max-heap' style here, meaning if child's priority > parent's, rotate.

    Examples
    --------
    >>> root = None
    >>> for x in [10, 5, 15, 2]:
    ...     root = insert_treap(root, x)
    >>> inord = []
    >>> def inorder(n):
    ...     if n: inorder(n.left); inord.append(n.key); inorder(n.right)
    >>> inorder(root)
    >>> sorted(inord) == inord  # BST property => inord is sorted
    True
    """
    if root is None:
        return TreapNode(key)

    if key < root.key:
        root.left = insert_treap(root.left, key)
        # check priority
        if root.left and root.left.priority > root.priority:
            # rotate right
            root = rotate_right(root)
    else:
        root.right = insert_treap(root.right, key)
        if root.right and root.right.priority > root.priority:
            # rotate left
            root = rotate_left(root)
    return root


def inorder(root: TreapNode | None, out: list[int]) -> None:
    """In-order traversal to confirm BST ordering or debugging."""
    if not root:
        return
    inorder(root.left, out)
    out.append(root.key)
    inorder(root.right, out)


def main() -> None:
    """
    Demonstrate main functionality.

    Insert a few items, do an inorder to confirm BST property.
    Observe random priority yields an unpredictable shape, but expected O(log n) height.
    """
    items = [10, 5, 15, 2, 7, 13, 20]

    root = None
    for x in items:
        root = insert_treap(root, x)

    vals: list[int] = []
    inorder(root, vals)
    print("Treap in-order:", vals)


if __name__ == "__main__":
    main()
