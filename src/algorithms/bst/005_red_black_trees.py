#!/usr/bin/env python
"""
5. Red-Black Trees: Balanced BST with Simpler Balancing Rules.

Concepts:
- Red-Black properties: each node is red or black, no two consecutive reds,
  and every path from root to a leaf has the same number of black nodes (black-height).
- Insert & delete rebalancing revolve around recoloring and rotations when color constraints are violated.

Algorithm:
- Insert a new node as red, then fix color violations with recolors/rotations while moving upward if needed.
- Delete also rebalances if there's a "black deficit," but omitted here for brevity.

Complexities:
- Worst-case O(log n) for search/insert/delete. The tree remains balanced in height.

Narrative:
A simpler set of rebalancing steps than AVL, widely used in practice (e.g., C++ std::map, Java’s TreeMap).
In an SRAS pipeline, if a standard library provides a red-black tree, we can rely on guaranteed O(log n) operations.
"""

from __future__ import annotations

RED = True
BLACK = False


class RBNode:
    """
    A Node in a Red-Black Tree, storing:
    - key: the value
    - color: RED or BLACK
    - left, right, parent: pointers to child and parent nodes.

    We'll use a sentinel NIL node for leaves or child references, but keep
    it minimal here with None checks. The code must check if child is not None
    before accessing child attributes.
    """

    def __init__(self, key: int, color: bool = RED) -> None:
        self.key = key
        self.color = color
        self.left: RBNode | None = None
        self.right: RBNode | None = None
        self.parent: RBNode | None = None


def rotate_left(root: RBNode, x: RBNode) -> RBNode:
    """
    Left-rotate at node x.
    Returns the (possibly new) root of the entire tree if it changed.
    """
    y = x.right
    if y is None:
        return root  # can't rotate if x.right is None

    # y's left subtree becomes x's right subtree
    x.right = y.left
    if y.left:
        y.left.parent = x
    y.parent = x.parent

    if x.parent is None:
        # x was root
        root = y
    elif x is x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y
    return root


def rotate_right(root: RBNode, x: RBNode) -> RBNode:
    """
    Right-rotate at node x.
    Returns the (possibly new) root of the entire tree if it changed.
    """
    y = x.left
    if y is None:
        return root  # can't rotate if x.left is None

    x.left = y.right
    if y.right:
        y.right.parent = x
    y.parent = x.parent

    if x.parent is None:
        root = y
    elif x is x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y

    y.right = x
    x.parent = y
    return root


def insert_rb(root: RBNode | None, key: int) -> RBNode:
    """
    Insert 'key' into the Red-Black tree with root 'root' (which may be None).
    Returns the new root after insertion (which might change).

    Examples
    --------
    >>> root = None
    >>> for x in [10, 20, 30, 15]:
    ...     root = insert_rb(root, x)
    >>> inorder_vals = []
    >>> def inorder(n):
    ...     if not n: return
    ...     inorder(n.left)
    ...     inorder_vals.append(n.key)
    ...     inorder(n.right)
    >>> inorder(root)
    >>> inorder_vals
    [10, 15, 20, 30]
    """
    # 1) BST insert (iterative)
    new_node = RBNode(key, RED)
    if not root:
        root = new_node
        # root will be recolored to BLACK in fixup
    else:
        current = root
        while current:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            elif current.right is None:
                current.right = new_node
                new_node.parent = current
                break
            else:
                current = current.right

    # 2) Fix up the red-black properties
    return insert_fixup(root, new_node)


def insert_fixup(root: RBNode, x: RBNode) -> RBNode:
    """
    Fix red-black violations after inserting node x, walking up if needed.
    Returns possibly new root.
    """
    while x.parent and x.parent.color == RED:
        grand = x.parent.parent
        if grand and x.parent is grand.left:
            # uncle is grand.right
            uncle = grand.right
            if uncle and uncle.color == RED:
                # Case 1: uncle is red => recolor
                x.parent.color = BLACK
                uncle.color = BLACK
                grand.color = RED
                x = grand
            else:
                # Case 2 or 3: uncle is black => rotate
                if x is x.parent.right:
                    # left rotation on x.parent
                    root = rotate_left(root, x.parent)
                    x = x.left or x
                # Right rotation on grand
                x.parent.color = BLACK
                grand.color = RED
                root = rotate_right(root, grand)
        elif grand and x.parent is grand.right:
            # uncle is grand.left
            uncle = grand.left
            if uncle and uncle.color == RED:
                # Case 1 mirror
                x.parent.color = BLACK
                uncle.color = BLACK
                grand.color = RED
                x = grand
            else:
                # Case 2 or 3 mirror
                if x is x.parent.left:
                    root = rotate_right(root, x.parent)
                    x = x.right or x
                x.parent.color = BLACK
                grand.color = RED
                root = rotate_left(root, grand)
        else:
            # might happen if no grand, e.g. x's parent is root
            break

    # Ensure root is always black
    root.color = BLACK
    return root


def inorder(root: RBNode | None, result: list[int]) -> None:
    """In-order traversal for debugging or checking BST property."""
    if not root:
        return
    inorder(root.left, result)
    result.append(root.key)
    inorder(root.right, result)


def node_color_str(n: RBNode | None) -> str:
    """Return 'R' or 'B' for the node color, or 'NIL' if n is None."""
    if not n:
        return "NIL"
    return "R" if n.color == RED else "B"


def main() -> None:
    """
    Main demonstration:
    We'll insert a few items and show the in-order traversal.
    The tree remains balanced near O(log n) height thanks to red-black rebalancing.
    """
    root = None
    for x in [10, 20, 30, 15]:
        root = insert_rb(root, x)

    vals: list[int] = []
    inorder(root, vals)
    print("In-order of final Red-Black Tree:", vals)

    # We could show color of root, children's colors, etc.
    print(f"Root = {root.key}, color={node_color_str(root)}")
    if root.left:
        print(f"Root.left = {root.left.key}, color={node_color_str(root.left)}")
    if root.right:
        print(f"Root.right = {root.right.key}, color={node_color_str(root.right)}")


if __name__ == "__main__":
    main()
