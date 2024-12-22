#!/usr/bin/env python
"""
15. Priority Queue from BST / Treap.

Concepts:
- A BST (Treap) uses a key for BST ordering and a random priority for heap ordering.
- Priority queue operations (insert, extract-min, extract-max) are O(log n) on average,
  as the treap remains balanced in expected sense.
- We show a min-oriented approach here (extract-min).

Algorithm:
- Insert:
  1) BST insert by key.
  2) Assign random priority.
  3) Rotate up if child’s priority outranks parent (for a “min-heap” style, we want parent’s priority <= children).
- Extract-Min:
  1) Find min by going left.
  2) Rotate that min node up (by rotating it with parents) until it’s root.
  3) Pop the root (which is min). Merge subtrees if needed or reassign root.

Complexities:
- O(log n) average for all standard priority queue ops.

Narrative:
If SRAS needs both BST lookups and a priority-queue structure, a treap unifies them.
We can do BFS/DFS by key, also can quickly extract the min or max by rotating them to root and popping.
"""

from __future__ import annotations

import random


class TreapNode:
    """
    A node in the Treap:
    - key: BST key
    - priority: random float (for min-heap or max-heap logic)
    - left, right: child pointers.
    """

    def __init__(self, key: int) -> None:
        self.key = key
        self.priority = random.random()
        self.left: TreapNode | None = None
        self.right: TreapNode | None = None


def rotate_right(root: TreapNode) -> TreapNode:
    """
    Right-rotate at 'root' (which must have root.left != None).
    Return the new root of this subtree.
    """
    y = root.left
    if y is None:
        return root
    root.left = y.right
    y.right = root
    return y


def rotate_left(root: TreapNode) -> TreapNode:
    """
    Left-rotate at 'root' (which must have root.right != None).
    Return the new root of this subtree.
    """
    y = root.right
    if y is None:
        return root
    root.right = y.left
    y.left = root
    return y


def treap_insert(root: TreapNode | None, key: int) -> TreapNode:
    """
    Insert 'key' into the treap. We do a BST insert by 'key',
    then we rotate if needed to maintain min-heap property on 'priority'.
    """
    if root is None:
        return TreapNode(key)
    if key < root.key:
        root.left = treap_insert(root.left, key)
        # for min-heap logic, parent's priority should be <= child's
        # if parent's priority > child's => rotate
        if root.left and root.left.priority < root.priority:
            root = rotate_right(root)
    else:
        root.right = treap_insert(root.right, key)
        if root.right and root.right.priority < root.priority:
            root = rotate_left(root)
    return root


def find_min(root: TreapNode | None) -> TreapNode | None:
    """Return the node with the minimum key (leftmost)."""
    cur = root
    while cur and cur.left:
        cur = cur.left
    return cur


def treap_splay_to_root(root: TreapNode | None, key: int) -> TreapNode | None:
    """
    Splay-like approach: rotate the node with 'key' up to root if found,
    by repeated left/right rotations (like Zig steps).
    This is simpler than full splay, we just bubble it up by checking parents in recursion.
    For demonstration only.
    """
    if root is None or root.key == key:
        return root or None
    if key < root.key and root.left:
        # bubble up from left
        if root.left.key == key:
            # rotate right
            return rotate_right(root)
        # else we recursively move deeper
        root.left = treap_splay_to_root(root.left, key)
        # then rotate
        return rotate_right(root)
    if key > root.key and root.right:
        if root.right.key == key:
            return rotate_left(root)
        root.right = treap_splay_to_root(root.right, key)
        return rotate_left(root)
    return root  # key not found or no child => no change


def extract_min(root: TreapNode | None) -> tuple[TreapNode | None, int | None]:
    """
    Extract the minimum key from the treap:
    1) Find min key, rotate it up to the root (treap_splay_to_root),
    2) Then remove the root and merge left/right subtrees if needed.
    Return (new_root, min_key).
    """
    if not root:
        return (None, None)
    # find min node
    min_node = find_min(root)
    if not min_node:
        return (root, None)
    min_key = min_node.key
    # rotate that node to root
    root = treap_splay_to_root(root, min_key)
    assert root is not None
    # now root.key == min_key => remove root
    # left subtree, right subtree
    left_sub = root.left
    right_sub = root.right
    # discard root
    root = merge_treap(left_sub, right_sub)
    return (root, min_key)


def merge_treap(
    left: TreapNode | None,
    right: TreapNode | None,
) -> TreapNode | None:
    """
    Merge two treaps 'left' and 'right' (all keys in left < all keys in right).
    We'll do a priority-based merge:
     - if left is None => return right
     - if right is None => return left
     - if left.priority < right.priority => left.right = merge_treap(left.right, right)
       else => right.left = merge_treap(left, right.left).
    """
    if not left:
        return right
    if not right:
        return left
    # min-heap logic => parent's priority <= child's
    # so we compare and unify
    if left.priority < right.priority:
        # left is root
        left.right = merge_treap(left.right, right)
        return left
    right.left = merge_treap(left, right.left)
    return right


def treap_inorder(root: TreapNode | None, out: list[int]) -> None:
    """In-order traversal to confirm BST ordering."""
    if not root:
        return
    treap_inorder(root.left, out)
    out.append(root.key)
    treap_inorder(root.right, out)


def main() -> None:
    """
    Demonstration: We create a treap, then do some insertions,
    extract-min a couple times, and confirm the BST property.
    """
    data = [20, 5, 15, 2, 7, 25, 1, 3]
    root: TreapNode | None = None
    # Insert
    for x in data:
        root = treap_insert(root, x)

    arr: list[int] = []
    treap_inorder(root, arr)
    print("Treap inorder after inserts:", arr)

    # Extract min multiple times
    root, mn1 = extract_min(root)
    root, mn2 = extract_min(root)
    print("Extracted mins:", mn1, mn2)

    arr2: list[int] = []
    treap_inorder(root, arr2)
    print("Treap inorder after extracting min twice:", arr2)


if __name__ == "__main__":
    main()
