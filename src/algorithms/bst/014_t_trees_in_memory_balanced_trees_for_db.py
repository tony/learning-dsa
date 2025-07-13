#!/usr/bin/env python
"""
14. Tree Sort: Sorting by Inserting into a BST + In-Order Traversal.

Algorithm:
1) Insert all elements into a BST (preferably self-balancing).
2) Perform an in-order traversal to collect them in sorted order.

Complexities:
- With a self-balancing BST: O(n log n).
- With a naive BST if unlucky: O(n^2).

Narrative:
If an SRAS app already maintains data in a balanced BST, we can produce sorted output
just by doing an in-order traversal. But typically mergesort, quicksort, or Timsort is easier
if we only need sorting once, rather than maintaining a BST.
"""

from __future__ import annotations


class BSTNode:
    """
    A simple BST node for demonstration.

    Stores:
    - key: the value
    - left, right: child pointers.
    """

    def __init__(self, key: int) -> None:
        self.key = key
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


def bst_insert(root: BSTNode | None, key: int) -> BSTNode:
    """
    Insert 'key' into a naive BST. Returns the new root.

    (Not self-balancing, can degrade to O(n^2) in worst case.).
    """
    if root is None:
        return BSTNode(key)
    if key < root.key:
        root.left = bst_insert(root.left, key)
    else:
        root.right = bst_insert(root.right, key)
    return root


def inorder_traverse(root: BSTNode | None, out: list[int]) -> None:
    """In-order traversal to collect keys in sorted order."""
    if root is None:
        return
    inorder_traverse(root.left, out)
    out.append(root.key)
    inorder_traverse(root.right, out)


def tree_sort(arr: list[int]) -> list[int]:
    """
    Perform Tree Sort on arr using a naive BST for demonstration.

    If arr is large or potentially sorted, a self-balancing BST (AVL, Red-Black) is recommended
    to maintain O(n log n) performance. This naive approach can degrade to O(n^2).
    """
    # 1) Insert all elements into BST

    root: BSTNode | None = None
    for x in arr:
        root = bst_insert(root, x)

    # 2) In-order traversal to get sorted result
    sorted_out: list[int] = []
    inorder_traverse(root, sorted_out)
    return sorted_out


def main() -> None:
    """Demonstration of Tree Sort on a small list."""
    data = [30, 10, 20, 40, 15]
    print("Original list:", data)

    # Tree Sort
    sorted_list = tree_sort(data)
    print("Sorted list via Tree Sort:", sorted_list)


if __name__ == "__main__":
    main()
