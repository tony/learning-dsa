#!/usr/bin/env python
"""
8. Weight-Balanced / Size-Balanced BSTs.

Concepts:
- Each node maintains a “size” (number of nodes in its subtree).
- On insertion or deletion, if a subtree is too large compared to its sibling,
  we perform rotations to restore balance.
- A simple ratio check: e.g. if left_size > ratio * right_size, or vice versa.

Algorithm:
- Insert as in a normal BST.
- After insertion, update subtree sizes bottom-up.
- If a child is too large relative to its sibling, rotate to restore size balance.
- The ratio ensures the height remains O(log n) on average.

Complexities:
- Maintains O(log n) height,
  so search/insert/delete in O(log n).

Narrative:
If SRAS data arrives in bursts, a size-balanced approach can keep the BST balanced
in a straightforward way (just subtree size checks, no complex balancing factors).
"""

from __future__ import annotations


class SizeBSTNode:
    """
    Node for a Size-Balanced BST:

    - key: BST key
    - size: number of nodes in this subtree (including self)
    - left, right: child pointers.
    """

    def __init__(self, key: int) -> None:
        self.key = key
        self.size = 1
        self.left: SizeBSTNode | None = None
        self.right: SizeBSTNode | None = None


def get_size(node: SizeBSTNode | None) -> int:
    """Return node.size if node is not None, else 0."""
    return node.size if node else 0


def update_size(node: SizeBSTNode) -> None:
    """Recompute this node's size = 1 + size(left) + size(right)."""
    node.size = 1 + get_size(node.left) + get_size(node.right)


def rotate_left(root: SizeBSTNode) -> SizeBSTNode:
    """
    Rotate left around 'root'. Return the new subtree root (y).

    We'll assume root.right is not None in typical usage.
    """
    y = root.right
    if y is None:
        return root  # no rotation if right is None
    root.right = y.left
    y.left = root
    # update sizes
    update_size(root)
    update_size(y)
    return y


def rotate_right(root: SizeBSTNode) -> SizeBSTNode:
    """
    Rotate right around 'root'. Return the new subtree root (y).

    We'll assume root.left is not None in typical usage.
    """
    y = root.left
    if y is None:
        return root
    root.left = y.right
    y.right = root
    # update sizes
    update_size(root)
    update_size(y)
    return y


def fix_sizebalance(node: SizeBSTNode, ratio: float = 2.0) -> SizeBSTNode:
    """
    Check the size ratio of the left and right children.

    If one side is too big, rotate to restore balance. Re-check after rotation.

    ratio=2 means no subtree can exceed double the size of its sibling.
    """
    if node is None:
        return node

    left_size = get_size(node.left)
    right_size = get_size(node.right)

    # if left subtree is > ratio * right subtree => rotate right
    if left_size > ratio * right_size and node.left:
        # check if the left child's right is heavier => do double rotation
        left_left_sz = get_size(node.left.left)
        left_right_sz = get_size(node.left.right)
        if left_right_sz > left_left_sz:
            # rotate left on node.left
            node.left = rotate_left(node.left)
        # now rotate right on node
        node = rotate_right(node)

    # if right subtree is > ratio * left subtree => rotate left
    elif right_size > ratio * left_size and node.right:
        # check if the right child's left is heavier => do double rotation
        right_left_sz = get_size(node.right.left)
        right_right_sz = get_size(node.right.right)
        if right_left_sz > right_right_sz:
            node.right = rotate_right(node.right)
        node = rotate_left(node)

    return node


def insert_sizebst(
    root: SizeBSTNode | None,
    key: int,
    ratio: float = 2.0,
) -> SizeBSTNode:
    """
    Insert 'key' into the size-balanced BST with a given ratio, returning new root.

    Examples
    --------
    >>> root = None
    >>> for x in [10, 5, 15, 3, 7]:
    ...     root = insert_sizebst(root, x)
    >>> in_vals = []
    >>> def inorder(n):
    ...     if not n: return
    ...     inorder(n.left)
    ...     in_vals.append(n.key)
    ...     inorder(n.right)
    >>> inorder(root)
    >>> in_vals == sorted([10,5,15,3,7])
    True
    """
    if root is None:
        return SizeBSTNode(key)

    if key < root.key:
        root.left = insert_sizebst(root.left, key, ratio)
    else:
        root.right = insert_sizebst(root.right, key, ratio)

    # update size
    update_size(root)
    # fix potential imbalance
    return fix_sizebalance(root, ratio)


def inorder(root: SizeBSTNode | None, arr: list[int]) -> None:
    """In-order traversal for debugging or verifying BST property."""
    if not root:
        return
    inorder(root.left, arr)
    arr.append(root.key)
    inorder(root.right, arr)


def main() -> None:
    """
    Main demonstration:

    We'll insert a few items, ensuring the size ratio is kept at 2.0.
    Then print in-order to confirm BST property. The ratio enforcement
    keeps subtrees from getting too large, preserving O(log n) height in practice.
    """
    items = [10, 5, 15, 3, 7, 20, 6]

    root = None
    for x in items:
        root = insert_sizebst(root, x, ratio=2.0)

    arr: list[int] = []
    inorder(root, arr)
    print("In-order after size-balanced insertions:", arr)


if __name__ == "__main__":
    main()
