#!/usr/bin/env python
"""
2. BST Search Variations and Handling Edge Cases.

Concepts
--------
- Recursive vs. iterative BST search implementation details.
- Edge cases: empty tree, searching for min or max, or searching in a single-node tree.
- Finding successor (next-larger key) and predecessor (next-smaller key):
  * If the node has a right subtree, successor is the leftmost node in the right subtree.
  * Otherwise, follow parent pointers upward until you traverse from left to right.

Algorithm
---------
Recursive Search (conceptual):
    searchBST(node, target):
        if node is None:
            return False
        elif node.key == target:
            return True
        elif target < node.key:
            return searchBST(node.left, target)
        else:
            return searchBST(node.right, target)

Iterative Search:
    current = root
    while current is not None:
        if current.key == target:
            return True
        elif target < current.key:
            current = current.left
        else:
            current = current.right
    return False

Successor & Predecessor:
    - If node has a right subtree, successor is the min of right subtree.
      Otherwise, move up parent pointers until we come from a left child.
    - Similarly, predecessor can be found with a left subtree's max or parent path.

Complexities
-----------
- Time: Best/Average O(log n), but can degrade to O(n) in a skewed tree.
- Space: O(h) recursion stack for the recursive approach (h = tree height), or O(1) iterative.

Narrative
---------
SRAS might require range queries or quick neighbor lookups (“find next-larger product ID”).
We demonstrate both recursive and iterative search code and show how to handle edge cases
(empty, min/max, single-node). Successor/predecessor logic helps in range queries or
“next-larger” ID queries.
"""

from typing import Any, Optional


class BSTNode:
    """
    A node in the binary search tree, storing:
    - key
    - pointers: left, right
    - optional pointer to parent (for easy successor/predecessor).
    """

    def __init__(self, key: Any, parent: Optional["BSTNode"] = None) -> None:
        self.key = key
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None
        self.parent: BSTNode | None = parent


class BST:
    """
    A BST with both recursive and iterative search, plus methods to find
    minimum, maximum, successor, and predecessor.

    We'll reuse an insert method (like in Chapter 1) but add a 'parent' pointer
    to support easy successor/predecessor logic.

    Examples
    --------
    >>> tree = BST()
    >>> for val in [5, 2, 8, 1, 3, 7, 9]:
    ...     tree.insert(val)
    >>> tree.search_recursive(3)
    True
    >>> tree.search_recursive(6)
    False
    >>> tree.search_iterative(8)
    True
    >>> tree.search_iterative(10)
    False

    # Edge cases: empty tree, single-node:
    >>> empty_tree = BST()
    >>> empty_tree.search_recursive(10)
    False
    >>> single_node_tree = BST()
    >>> single_node_tree.insert(42)
    >>> single_node_tree.search_recursive(42)
    True
    >>> single_node_tree.min_node().key
    42
    >>> single_node_tree.max_node().key
    42

    # Successor/Predecessor checks:
    >>> node_3 = tree.find_node(3)
    >>> succ_of_3 = tree.successor(node_3)
    >>> succ_of_3.key
    5
    >>> node_9 = tree.find_node(9)
    >>> tree.successor(node_9) is None
    True
    >>> node_7 = tree.find_node(7)
    >>> pred_of_7 = tree.predecessor(node_7)
    >>> pred_of_7.key
    5
    """

    def __init__(self) -> None:
        self.root: BSTNode | None = None

    def insert(self, key: Any) -> None:
        """Insert a key into the BST, maintaining parent pointers."""
        if self.root is None:
            self.root = BSTNode(key)
            return

        current: BSTNode | None = self.root
        parent: BSTNode | None = None
        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                # duplicates not handled; do nothing or define a policy
                return

        # create new node
        new_node = BSTNode(key, parent)
        assert parent is not None
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    # -----------------------------
    # Recursive search
    # -----------------------------
    def search_recursive(self, key: Any) -> bool:
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: BSTNode | None, key: Any) -> bool:
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    # -----------------------------
    # Iterative search
    # -----------------------------
    def search_iterative(self, key: Any) -> bool:
        current = self.root
        while current:
            if current.key == key:
                return True
            current = current.left if key < current.key else current.right
        return False

    # -----------------------------
    # Min / Max
    # -----------------------------
    def min_node(self) -> BSTNode | None:
        """Return the node with minimum key (leftmost). None if tree empty."""
        current = self.root
        if current is None:
            return None
        while current.left:
            current = current.left
        return current

    def max_node(self) -> BSTNode | None:
        """Return the node with maximum key (rightmost). None if tree empty."""
        current = self.root
        if current is None:
            return None
        while current.right:
            current = current.right
        return current

    def find_node(self, key: Any) -> BSTNode | None:
        """Utility to return the BSTNode instead of just True/False."""
        current = self.root
        while current:
            if current.key == key:
                return current
            current = current.left if key < current.key else current.right
        return None

    # -----------------------------
    # Successor / Predecessor
    # -----------------------------
    def successor(self, node: BSTNode) -> BSTNode | None:
        """
        Return the node’s in-order successor (next-larger).
        If node has a right subtree, it's the min of that subtree.
        Otherwise, move up parents until we come from the left side.
        """
        if node.right:
            return self._min_node_subtree(node.right)
        # move up parents
        current = node
        while current.parent and current == current.parent.right:
            current = current.parent
        return current.parent  # might be None if we're at the maximum

    def predecessor(self, node: BSTNode) -> BSTNode | None:
        """
        Return the node’s in-order predecessor (next-smaller).
        If node has a left subtree, it's the max of that subtree.
        Otherwise, move up parents until we come from the right side.
        """
        if node.left:
            return self._max_node_subtree(node.left)
        # move up parents
        current = node
        while current.parent and current == current.parent.left:
            current = current.parent
        return current.parent  # might be None if we're at the minimum

    def _min_node_subtree(self, node: BSTNode) -> BSTNode:
        current = node
        while current.left:
            current = current.left
        return current

    def _max_node_subtree(self, node: BSTNode) -> BSTNode:
        current = node
        while current.right:
            current = current.right
        return current


def main() -> None:
    """
    Main demonstration:
    We'll insert random data, demonstrate recursive vs. iterative search times,
    and show min/max plus successor/predecessor on a known node.

    Narrative:
    If SRAS needs quick neighbor lookups or range queries, we might rely on successor/predecessor.
    For big data, self-balancing is essential, but the logic of searching remains similar.
    """
    # Build a small BST
    values = [5, 2, 8, 1, 3, 7, 9, 6, 4]
    bst = BST()
    for val in values:
        bst.insert(val)

    # Compare recursive vs iterative search for a target
    target = 6
    rec_result = bst.search_recursive(target)
    itr_result = bst.search_iterative(target)
    print(f"Recursive search for {target}: {rec_result}")
    print(f"Iterative search for {target}: {itr_result}")

    # Show min and max
    node_min = bst.min_node()
    node_max = bst.max_node()
    print("Min node key:", node_min.key if node_min else "None")
    print("Max node key:", node_max.key if node_max else "None")

    # Show successor of 3
    node_3 = bst.find_node(3)
    if node_3:
        succ_3 = bst.successor(node_3)
        print(f"Successor of 3: {succ_3.key if succ_3 else 'None'}")

    # Show predecessor of 7
    node_7 = bst.find_node(7)
    if node_7:
        pred_7 = bst.predecessor(node_7)
        print(f"Predecessor of 7: {pred_7.key if pred_7 else 'None'}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
