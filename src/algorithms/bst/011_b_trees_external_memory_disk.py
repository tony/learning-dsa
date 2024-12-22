#!/usr/bin/env python
"""
11. B-Trees (External Memory / Disk).

Concepts:
- A multi-way balanced tree where each node can have up to (2t-1) keys and (2t) children (for a branching factor t).
- Minimizes disk I/O by grouping large blocks of keys into each node.
- Insert: if child is full, split it before descending. The tree height remains O(log n).
- Search: do a multiway search in node’s keys, follow the correct child pointer.

Algorithm (Insertion Outline):
1) If root is full, create a new node and split root.
2) Descend to the correct child, splitting it first if it's full.
3) Insert the new key in that leaf’s key array.

Complexities:
- O(log n) for search/insert/delete, with branching factor t => height ~ O(log_{t} n).

Narrative:
If SRAS data is so large we store it on disk or SSD, B-trees are standard. They keep height low
by storing multiple keys in each node, reducing the number of disk accesses needed to traverse.
"""

from __future__ import annotations


class BTreeNode:
    """
    A B-Tree node storing multiple keys and child pointers.
    - keys: sorted list of up to 2t-1 keys
    - children: array of child pointers of length up to 2t
    - leaf: whether this node is a leaf.
    """

    def __init__(self, t: int, leaf: bool) -> None:
        self.t = t  # branching factor
        self.leaf = leaf
        self.keys: list[int] = []
        self.children: list[BTreeNode] = []


def btree_search(node: BTreeNode | None, key: int) -> bool:
    """
    Search key in the subtree rooted at 'node'.
    Return True if found, else False.
    """
    if node is None:
        return False
    # Find the first key >= key
    i = 0
    while i < len(node.keys) and key > node.keys[i]:
        i += 1
    if i < len(node.keys) and node.keys[i] == key:
        return True
    if node.leaf:
        return False
    # Descend to child i
    return btree_search(node.children[i], key)


def split_child(parent: BTreeNode, i: int) -> None:
    """
    Split the full child parent.children[i] into two nodes, adjusting parent keys & children.
    parent.children[i] must have 2t-1 keys (full).
    We'll move the median key up to parent, and create a new sibling node for the second half of keys.
    """
    t = parent.t
    full_child = parent.children[i]
    new_node = BTreeNode(t, full_child.leaf)

    # move the last (t-1) keys of full_child to new_node
    new_node.keys = full_child.keys[t:]  # t..(2t-2)
    median_key = full_child.keys[t - 1]
    full_child.keys = full_child.keys[: t - 1]

    # if not leaf, move the last t children
    if not full_child.leaf:
        new_node.children = full_child.children[t:]
        full_child.children = full_child.children[:t]

    # insert median_key into parent.keys
    parent.keys.insert(i, median_key)
    parent.children.insert(i + 1, new_node)


def btree_insert_nonfull(node: BTreeNode, key: int) -> None:
    """
    Insert 'key' into the node (which is assumed to be NOT full).
    If it's a leaf, just put the key in the correct position.
    If not leaf, descend to the correct child, splitting it first if it is full.
    """
    i = len(node.keys) - 1
    if node.leaf:
        # insert key into node.keys in sorted position
        node.keys.append(0)  # expand the list
        while i >= 0 and key < node.keys[i]:
            node.keys[i + 1] = node.keys[i]
            i -= 1
        node.keys[i + 1] = key
    else:
        # find the child to descend
        while i >= 0 and key < node.keys[i]:
            i -= 1
        i += 1
        # if child is full => split
        if len(node.children[i].keys) == 2 * node.t - 1:
            split_child(node, i)
            # after split, decide which of the 2 children to go down
            if key > node.keys[i]:
                i += 1
        btree_insert_nonfull(node.children[i], key)


def btree_insert(root: BTreeNode | None, key: int, t: int) -> BTreeNode:
    """
    Insert 'key' into the B-Tree with root 'root', branching factor 't'.
    If root is full, we split it by creating a new root node.
    Returns the new root after insertion.
    """
    if root is None:
        # create a new root node and put key in
        root = BTreeNode(t, True)
        root.keys.append(key)
        return root

    # if root is full, split
    if len(root.keys) == 2 * t - 1:
        new_root = BTreeNode(t, False)
        new_root.children.append(root)
        split_child(new_root, 0)
        # now insert into either new_root.children[0] or [1]
        i = 0
        if key > new_root.keys[0]:
            i = 1
        btree_insert_nonfull(new_root.children[i], key)
        return new_root
    btree_insert_nonfull(root, key)
    return root


def inorder_traverse(node: BTreeNode | None, arr: list[int]) -> None:
    """
    In-order traversal for B-tree keys. We'll do a simple approach:
    for each key, traverse child i, then the key, then next child.
    """
    if node is None:
        return
    i = 0
    while i < len(node.keys):
        if i < len(node.children):
            inorder_traverse(node.children[i], arr)
        arr.append(node.keys[i])
        i += 1
    # last child
    if i < len(node.children):
        inorder_traverse(node.children[i], arr)


def main() -> None:
    """
    Main demonstration:
    We'll build a B-Tree with branching factor t=2. Insert a few items, do an inorder.
    B-Tree ensures O(log n) height by splitting nodes as soon as they fill up with 2t-1=3 keys.
    """
    t = 2  # minimal branching factor => each node up to 3 keys
    root: BTreeNode | None = None

    for x in [10, 20, 5, 6, 12, 30, 7, 17]:
        root = btree_insert(root, x, t)

    arr: list[int] = []
    inorder_traverse(root, arr)
    print("B-Tree inorder traversal:", arr)

    # Searching example
    print("Search 17 =>", btree_search(root, 17))
    print("Search 11 =>", btree_search(root, 11))


if __name__ == "__main__":
    main()
