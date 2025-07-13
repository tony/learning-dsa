#!/usr/bin/env python
"""
5. Red-Black Trees: Balanced BST with Simpler Balancing Rules.

Concepts:
- Red-Black properties: each node is red or black, no two consecutive reds,
  and every path from root to a leaf has the same number of black nodes (black-height).
- Insert & delete rebalancing revolve around recoloring and rotations when color
constraints are violated.

Algorithm:
- Insert a new node as red, then fix color violations with recolors/rotations while
moving upward if needed.
- Delete also rebalances if there's a "black deficit," but omitted for brevity.

Complexities:
- Worst-case O(log n) for search/insert/delete. The tree remains balanced in height.

Narrative:
A simpler set of rebalancing steps than AVL, widely used in practice (e.g., C++ std::map, Java's TreeMap).
In an SRAS pipeline, if a standard library provides a red-black tree, we can rely on guaranteed O(log n) operations.
"""

from __future__ import annotations

RED = True
BLACK = False


class RBNode:
    """
    A Node in a Red-Black Tree.

    Stores:
    - key: integer value
    - color: RED (True) or BLACK (False)
    - left, right, parent: pointers to children/parent, or None if absent.

    We'll rely on None checks to avoid a sentinel approach. Before accessing .color or .left/.right,
    confirm the node is not None.
    """

    def __init__(self, key: int, color: bool = RED) -> None:
        self.key = key
        self.color = color
        self.left: RBNode | None = None
        self.right: RBNode | None = None
        self.parent: RBNode | None = None


def is_red(node: RBNode | None) -> bool:
    """Return True if node is non-None and node.color == RED."""
    return (node is not None) and (node.color == RED)


def safe_rotate_left(root: RBNode, x: RBNode) -> RBNode:
    """
    Left-rotate at node x. Return possibly new root if x was root.

    We only rotate if x.right is not None. If x.right is None, do nothing.
    """
    y = x.right

    if y is None:
        return root  # no rotation possible
    # y.left becomes x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    y.parent = x.parent

    if x.parent is None:
        root = y
    elif x.parent.left is x:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y
    return root


def safe_rotate_right(root: RBNode, x: RBNode) -> RBNode:
    """
    Right-rotate at node x. Return possibly new root if x was root.

    Only rotate if x.left is not None.
    """
    y = x.left

    if y is None:
        return root
    # y.right becomes x.left
    x.left = y.right
    if y.right is not None:
        y.right.parent = x
    y.parent = x.parent

    if x.parent is None:
        root = y
    elif x.parent.right is x:
        x.parent.right = y
    else:
        x.parent.left = y

    y.right = x
    x.parent = y
    return root


def insert_rb(root: RBNode | None, key: int) -> RBNode:
    """
    Insert 'key' into the Red-Black tree with root 'root' (may be None).

    Returns the new root after insertion (which might change).

    Examples
    --------
    >>> root = None
    >>> for x in [10, 20, 30, 15]:
    ...     root = insert_rb(root, x)
    >>> vals = []
    >>> def inorder(n):
    ...     if n: inorder(n.left); vals.append(n.key); inorder(n.right)
    >>> inorder(root)
    >>> vals
    [10, 15, 20, 30]
    """
    new_node = RBNode(key, RED)

    if root is None:
        # new_node becomes root, fixup will recolor it black
        return insert_fixup(new_node, new_node)

    # standard BST insert (iterative)
    curr = root
    while True:
        if key < curr.key:
            if curr.left is None:
                curr.left = new_node
                new_node.parent = curr
                break
            curr = curr.left
        else:
            if curr.right is None:
                curr.right = new_node
                new_node.parent = curr
                break
            curr = curr.right

    return insert_fixup(root, new_node)


def insert_fixup(root: RBNode, x: RBNode) -> RBNode:
    """Fix red-black violations after inserting node x, possibly changing the root."""
    while True:
        p = x.parent
        if p is None or not is_red(p):
            break  # no violation if parent is black or doesn't exist
        # Now parent is red => check grandparent
        g = p.parent
        if g is None:
            break  # no grand => no uncle => done?

        if p is g.left:
            # uncle is g.right
            u = g.right
            if is_red(u):
                # recolor parent, uncle to black, grand to red => move x up
                p.color = BLACK
                if u:
                    u.color = BLACK
                g.color = RED
                x = g
            else:
                # uncle is black => rotate
                if x is p.right:
                    root = safe_rotate_left(root, p)
                    x = p  # after rotate, x might shift
                    if x.left:
                        x = x.left  # move x to "inserted" pos
                # now do right rotation on grand
                p2 = x.parent
                if p2:  # re-check
                    p2.color = BLACK
                g.color = RED
                root = safe_rotate_right(root, g)
        else:
            # p is g.right => symmetrical
            u = g.left
            if is_red(u):
                p.color = BLACK
                if u:
                    u.color = BLACK
                g.color = RED
                x = g
            else:
                if x is p.left:
                    root = safe_rotate_right(root, p)
                    x = p
                    if x.right:
                        x = x.right
                if x.parent:
                    x.parent.color = BLACK
                g.color = RED
                root = safe_rotate_left(root, g)

    # ensure final root is black
    # find root top
    top = root
    while top.parent is not None:
        top = top.parent
    top.color = BLACK
    return top


def inorder(root: RBNode | None, out: list[int]) -> None:
    """In-order traversal for verifying BST property or debugging."""
    if root:
        inorder(root.left, out)
        out.append(root.key)
        inorder(root.right, out)


def main() -> None:
    """
    Demonstrate main functionality.

    Insert a few items, show in-order. The final tree remains balanced O(log n).
    """
    root = None

    for x in [10, 20, 30, 15]:
        root = insert_rb(root, x)

    vals: list[int] = []
    inorder(root, vals)
    print("In-order of final Red-Black Tree:", vals)


if __name__ == "__main__":
    main()
