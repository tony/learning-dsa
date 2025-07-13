#!/usr/bin/env python
"""
4. Height-Balanced (AVL) Trees: Rotations and Invariants.

Concepts:
- AVL property: The height difference (balance factor) of left vs. right subtree at any
node is <= 1.
- Rotations (single & double) to rebalance after insertion/deletion.
- Maintaining an integer "height" or "balance factor" in each node.

Algorithm:
- Insert in BST fashion, then update heights while unwinding the recursion.
- If the node becomes unbalanced (balance factor > 1 or < -1), rotate:
  - Single rotation (left or right) if it's a simple "zig-zig" pattern.
  - Double rotation (left-right or right-left) if it's "zig-zag".
- Delete similarly rebalances (omitted here for brevity).

Complexities:
- Search/Insert/Delete: O(log n) guaranteed, because the tree is rebalanced
consistently.

Narrative:
For an SRAS pipeline with frequent inserts or random data patterns, an AVL tree
keeps operations consistently O(log n). A rotation step ensures no skew develops.
"""

from __future__ import annotations


class AVLNode:
    """
    A Node in an AVL Tree, storing:

    - key: the value
    - left, right: child pointers
    - height: cached height of this node for balancing.
    """

    def __init__(self, key: int) -> None:
        self.key = key
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None
        self.height = 1  # a newly inserted node has height=1


def get_height(node: AVLNode | None) -> int:
    return node.height if node else 0


def get_balance(node: AVLNode | None) -> int:
    """
    Balance factor = height(left subtree) - height(right subtree).

    If > 1 or < -1 => unbalanced => rotation needed.
    """
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def update_height(node: AVLNode) -> None:
    """Recompute node.height based on children."""
    node.height = 1 + max(get_height(node.left), get_height(node.right))


def rotate_left(z: AVLNode) -> AVLNode:
    """
    Perform a left rotation on node z, returning the new root (y).

    Usually done when z is "heavier" on the right side.
    """
    y = z.right

    if y is None:
        return z  # shouldn't happen if we call rotate_left properly
    # Perform rotation
    z.right = y.left
    y.left = z
    # Update heights
    update_height(z)
    update_height(y)
    return y  # y is now the root


def rotate_right(z: AVLNode) -> AVLNode:
    """
    Perform a right rotation on node z, returning the new root (y).

    Usually done when z is "heavier" on the left side.
    """
    y = z.left

    if y is None:
        return z  # shouldn't happen if we call rotate_right properly
    # Perform rotation
    z.left = y.right
    y.right = z
    # Update heights
    update_height(z)
    update_height(y)
    return y  # y is now the root


def insert_avl(root: AVLNode | None, key: int) -> AVLNode:
    """
    Insert 'key' into the AVL tree rooted at 'root', ensuring rebalancing.

    Returns the new root after insertion (which might change due to rotations).

    Examples
    --------
    >>> root = None
    >>> for x in [10, 20, 30]:
    ...     root = insert_avl(root, x)
    >>> # The insertion of 10,20,30 in ascending order triggers a rotation
    >>> # The tree remains balanced, e.g., root could be 20 with left=10, right=30
    >>> inorder_vals = []
    >>> def inorder(n):
    ...     if not n: return
    ...     inorder(n.left)
    ...     inorder_vals.append(n.key)
    ...     inorder(n.right)
    >>> inorder(root)
    >>> inorder_vals
    [10, 20, 30]
    >>> root.height
    2
    """
    if not root:
        return AVLNode(key)

    # BST insert
    if key < root.key:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)

    # Update height of this ancestor node
    update_height(root)

    # Check balance
    balance = get_balance(root)
    # If node unbalanced => 4 cases

    # Left Left Case
    if balance > 1:
        # We must ensure root.left is not None before comparing keys
        if root.left and key < root.left.key:
            return rotate_right(root)

    # Right Right Case
    if balance < -1:
        # Ensure root.right is not None before comparing keys
        if root.right and key > root.right.key:
            return rotate_left(root)

    # Left Right Case
    if balance > 1 and root.left and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    # Right Left Case
    if balance < -1 and root.right and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root  # no rotation needed


def inorder(root: AVLNode | None, result: list[int]) -> None:
    """In-order traversal, for debugging or checking sorting property."""
    if not root:
        return
    inorder(root.left, result)
    result.append(root.key)
    inorder(root.right, result)


def main() -> None:
    """
    Demonstrate main functionality.

    We'll insert ascending data (1..20), also random data,
    and confirm we get a balanced tree of height ~ log(n).

    Narrative:
    An SRAS pipeline with random data remains balanced in O(log n)
    thanks to AVL rebalancing rotations. Inserting sorted data also
    stays balanced, avoiding naive BST skew.
    """
    import random

    values = list(range(1, 21))  # 20 items
    random_vals = values.copy()
    random.shuffle(random_vals)

    # Insert ascending
    root_asc = None
    for v in values:
        root_asc = insert_avl(root_asc, v)

    # Insert random
    root_rand = None
    for rv in random_vals:
        root_rand = insert_avl(root_rand, rv)

    inorder_asc: list[int] = []
    inorder_rand: list[int] = []
    inorder(root_asc, inorder_asc)
    inorder(root_rand, inorder_rand)

    print("AVL with ascending inserts (1..20) => Inorder:", inorder_asc)
    print(f"Final height (ascending) = {root_asc.height if root_asc else 0}")

    print("AVL with random inserts => Inorder:", inorder_rand)
    print(f"Final height (random) = {root_rand.height if root_rand else 0}")


if __name__ == "__main__":
    main()
