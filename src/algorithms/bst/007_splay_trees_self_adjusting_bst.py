#!/usr/bin/env python
"""
7. Splay Trees: Self-Adjusting BST.

Concepts:
- Splaying: any access (search, insert, or delete) brings the accessed node to root
  via rotations (zig, zig-zig, zig-zag).
- Amortized O(log n) time, though a single operation can degrade to O(n) if the tree is
  extremely unbalanced prior to splaying.

Algorithm:
- Access (Search/Insert): After finding or creating the node, splay it to the root.
- Delete (omitted here): Splay the node, remove it, then reattach subtrees.

Complexities:
- Amortized O(log n), single operation can be O(n).

Narrative:
In SRAS, if we repeatedly access the same product IDs, splay trees move those “hot” items
near the root, making repeated accesses faster than a standard BST. Over time, we get near
log n performance on average.
"""

from __future__ import annotations


class SplayNode:
    """
    A node in the Splay Tree, storing:

    - key: BST key
    - left, right, parent: pointers to children and parent.
    """

    def __init__(self, key: int) -> None:
        self.key = key
        self.left: SplayNode | None = None
        self.right: SplayNode | None = None
        self.parent: SplayNode | None = None


def rotate_left(x: SplayNode) -> None:
    """
    Rotate left at node x. x.right must be non-None.

    The parent's child pointer to x is updated to x.right.
    x.right's left becomes x's right. Then x becomes left child of x.right.
    """
    y = x.right
    if y is None:
        return  # can't rotate if x.right is None
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent is None:
        # x was root, no update needed here for a global root, since we handle in splay
        pass
    elif x is x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y


def rotate_right(x: SplayNode) -> None:
    """Rotate right at node x. x.left must be non-None."""
    y = x.left

    if y is None:
        return
    x.left = y.right
    if y.right is not None:
        y.right.parent = x
    y.parent = x.parent
    if x.parent is None:
        pass
    elif x is x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.right = x
    x.parent = y


def splay(x: SplayNode) -> None:
    """
    Splay node x to the root of its tree using standard zig/zig-zig/zig-zag steps.

    We do not return the new root here, but the caller can find it by climbing up
    if needed. In practice, we might reassign the global root after splay if x.parent is None.
    """
    while x.parent is not None:
        p = x.parent
        gp = p.parent
        if gp is None:
            # Zig step: x has a parent but no grandparent
            if x is p.left:
                rotate_right(p)
            else:
                rotate_left(p)
        # x has both parent and grandparent => Zig-zig or Zig-zag
        elif x is p.left and p is gp.left:
            # Zig-zig (left-left)
            rotate_right(gp)
            rotate_right(p)
        elif x is p.right and p is gp.right:
            # Zig-zig (right-right)
            rotate_left(gp)
            rotate_left(p)
        elif x is p.right and p is gp.left:
            # Zig-zag (left-right)
            rotate_left(p)
            rotate_right(gp)
        else:
            # Zig-zag (right-left)
            rotate_right(p)
            rotate_left(gp)


def insert_splay(root: SplayNode | None, key: int) -> SplayNode:
    """
    Insert 'key' into the Splay Tree, then splay the inserted node to root.

    Returns the new root after insertion.

    Examples
    --------
    >>> root = None
    >>> for x in [10, 20, 5, 15]:
    ...     root = insert_splay(root, x)
    >>> # The final inserted node '15' should be splayed to the root
    >>> root.key
    15
    """
    if root is None:
        return SplayNode(key)

    # Standard BST insertion
    cur: SplayNode | None = root
    parent: SplayNode | None = None
    while cur is not None:
        parent = cur
        cur = cur.left if key < cur.key else cur.right

    new_node = SplayNode(key)
    new_node.parent = parent
    if parent is not None:
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    # Now splay the new_node
    splay(new_node)
    # new_node might now be root or near root; find actual root
    top = new_node
    while top.parent is not None:
        top = top.parent
    return top


def search_splay(root: SplayNode | None, key: int) -> SplayNode | None:
    """
    Search for 'key' in the splay tree. If found, splay that node to root.

    If not found, splay the last accessed node (the would-be parent).

    Returns the new root after splay, which might be the found node or the last accessed.
    """
    cur = root

    last = None
    while cur is not None:
        last = cur
        if key == cur.key:
            splay(cur)
            # after splay, find actual root
            top = cur
            while top.parent is not None:
                top = top.parent
            return top
        cur = cur.left if key < cur.key else cur.right

    # key not found, splay last
    if last is not None:
        splay(last)
        while last.parent is not None:
            last = last.parent
        return last
    return None


def inorder(root: SplayNode | None, out: list[int]) -> None:
    """Simple in-order traversal for verifying BST property."""
    if root:
        inorder(root.left, out)
        out.append(root.key)
        inorder(root.right, out)


def main() -> None:
    """
    Main demonstration:

    Insert a few items, do an in-order print.
    Then search for one of them to show it splayed to root.
    """
    root = None
    for x in [10, 20, 5, 15, 25]:
        root = insert_splay(root, x)

    vals: list[int] = []
    inorder(root, vals)
    print("Splay tree in-order after inserts:", vals)
    print("Current root:", root.key if root else None)

    # Now search for key=5, it should be splayed to root
    root = search_splay(root, 5)
    vals2: list[int] = []
    inorder(root, vals2)
    print("Splay tree in-order after searching 5:", vals2)
    print("Current root:", root.key if root else None)


if __name__ == "__main__":
    main()
