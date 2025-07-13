#!/usr/bin/env python
"""
13. T-Trees: In-Memory Balanced Trees for Databases.

Concepts:
- A T-tree merges AVL height balancing with B-tree-like multiple keys per node.
- Each node can hold a set (array) of keys, reducing pointer overhead and leveraging CPU
  cache better.
- Balanced using AVL-like height checks (rotate if unbalanced).

Algorithm (Sketch):
- Insert:
  1) If the key belongs in this node's range, place it in node.keys if there's space.
  2) Else, go left or right subtree (like BST).
  3) If node.keys overflows capacity, split or push a key up.
  4) Update height, do rotations if needed (like AVL).
- Omitted: advanced merges on node underflow, concurrency issues, etc.

Complexities:
- O(log n) for search/insert/delete if we keep height balanced and node capacity is enough
  to keep tree shallow.

Narrative:
In an SRAS with large memory, T-trees may reduce overhead by storing multiple route IDs
in each node. This toy example omits many real-world T-tree complexities (like partial merges).
"""

from __future__ import annotations


class TTreeNode:
    """
    A node in a toy T-Tree.

    Stores:
    - keys: a sorted list of keys (up to capacity)
    - left, right: child pointers
    - height: for AVL-like balancing
    - capacity: max number of keys allowed.
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.keys: list[int] = []
        self.left: TTreeNode | None = None
        self.right: TTreeNode | None = None
        self.height = 1


def get_height(node: TTreeNode | None) -> int:
    """Get the height of a node (0 if None)."""
    return node.height if node else 0


def update_height(node: TTreeNode) -> None:
    """Update the height of a node based on its children."""
    node.height = 1 + max(get_height(node.left), get_height(node.right))


def get_balance(node: TTreeNode | None) -> int:
    """Get the balance factor of a node."""
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def rotate_left(root: TTreeNode) -> TTreeNode:
    """
    Perform AVL-like left rotation around 'root'.

    We'll assume root.right is not None in normal usage.
    """
    y = root.right
    if y is None:
        return root  # cannot rotate if no right child
    root.right = y.left
    y.left = root
    update_height(root)
    update_height(y)
    return y


def rotate_right(root: TTreeNode) -> TTreeNode:
    """
    Perform AVL-like right rotation around 'root'.

    We'll assume root.left is not None in normal usage.
    """
    x = root.left
    if x is None:
        return root
    root.left = x.right
    x.right = root
    update_height(root)
    update_height(x)
    return x


def rebalance(node: TTreeNode) -> TTreeNode:
    """Check balance factor, do single or double rotations if needed."""
    update_height(node)

    balance = get_balance(node)
    # left heavy
    if balance > 1:
        if node.left and get_balance(node.left) < 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)
    # right heavy
    if balance < -1:
        if node.right and get_balance(node.right) > 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)
    return node


def insert_into_node(node: TTreeNode, key: int) -> bool:
    """
    Try to place 'key' into node.keys if there's space or it belongs inside range.

    Return True if the key was inserted, False if we need to go subtrees.
    We'll keep keys sorted.
    """
    if len(node.keys) == 0:
        node.keys.append(key)
        return True
    # if key is within min and max of node.keys => place it in this node if capacity allows
    if key >= node.keys[0] and key <= node.keys[-1] and len(node.keys) < node.capacity:
        # insert into node.keys in order
        i = 0
        while i < len(node.keys) and node.keys[i] < key:
            i += 1
        node.keys.insert(i, key)
        return True
    return False


def split_node(node: TTreeNode) -> tuple[int, TTreeNode]:
    """
    If node.keys exceed capacity => we 'split' it by:

    1) take middle key as 'promoted' or 'pushed up' key
    2) create a new TTreeNode for the right half.
    Return (promoted_key, new_right_node).
    For simplicity, we do a half-split.
    """
    mid_idx = len(node.keys) // 2

    mid_key = node.keys[mid_idx]
    # new node with same capacity
    new_node = TTreeNode(node.capacity)
    new_node.keys = node.keys[mid_idx + 1 :]
    node.keys = node.keys[:mid_idx]
    # we do not handle subtrees distribution here for simplicity
    update_height(node)
    update_height(new_node)
    return (mid_key, new_node)


def insert_ttree(root: TTreeNode | None, key: int, capacity: int = 4) -> TTreeNode:
    """
    Insert 'key' into a toy T-tree with node capacity=4 by default.
    If root is None, create a node.
    If node can hold the key, we do so. Else descend left or right based on BST logic.
    If node is over capacity, split it and push up (like a simplified approach).
    Then do a rebalance (AVL-like).
    """
    if root is None:
        root = TTreeNode(capacity)
        root.keys.append(key)
        return root

    # try to place in current node
    if insert_into_node(root, key):
        # check if over capacity
        if len(root.keys) > capacity:
            # we must split. The 'mid_key' we push up to the parent
            # but we have no parent pointer here => we do a top-level approach:
            mid_key, new_node = split_node(root)
            # create new root, mid_key is root's key, old root is left child,
            # new_node is right child
            new_root = TTreeNode(capacity)
            new_root.keys = [mid_key]
            new_root.left = root
            new_root.right = new_node
            return rebalance(new_root)
        # just rebalance
        return rebalance(root)

    # else, we must go left or right
    if key < root.keys[0]:
        # go left
        root.left = insert_ttree(root.left, key, capacity)
    elif key > root.keys[-1]:
        # go right
        root.right = insert_ttree(root.right, key, capacity)
    else:
        # if key is between node.keys[0] and node.keys[-1], but not inserted =>
        # we can't insert in this node because we need subtrees in a real T-tree approach
        # We'll do a naive approach: just pick left or right if key < mid or key>mid
        mid_val = root.keys[len(root.keys) // 2]
        if key < mid_val:
            root.left = insert_ttree(root.left, key, capacity)
        else:
            root.right = insert_ttree(root.right, key, capacity)

    return rebalance(root)


def inorder_traverse(node: TTreeNode | None, arr: list[int]) -> None:
    """In-order for T-tree: traverse left subtree, then node.keys, then right subtree."""
    if not node:
        return
    inorder_traverse(node.left, arr)
    arr.extend(node.keys)
    inorder_traverse(node.right, arr)


def main() -> None:
    """
    Minimal T-tree demonstration.

    We'll insert some keys. Each node can hold up to 4 keys before splitting.
    Then we do an in-order listing, verifying BST ordering across node.keys.
    This toy approach omits advanced merges or full concurrency logic.
    """
    data = [10, 5, 15, 12, 13, 1, 2, 30, 25, 20, 22]
    root: TTreeNode | None = None
    for x in data:
        root = insert_ttree(root, x, capacity=4)

    arr: list[int] = []
    inorder_traverse(root, arr)
    print("T-tree in-order listing:", arr)


if __name__ == "__main__":
    main()
