#!/usr/bin/env python
"""
2. BST Search Variations and Handling Edge Cases.

Concepts
--------
- Recursive vs. iterative BST search implementation details.
- Edge cases: empty tree, searching for min or max, or searching in a single-node tree.
- Finding successor (next-larger key) and predecessor (next-smaller key):
  * If the node has a right subtree, successor is the leftmost node in the right
  subtree.
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
- Space: O(h) recursion stack for the recursive approach (h = tree height), or O(1)
iterative.

Narrative
---------
SRAS might require range queries or quick neighbor lookups (“find next-larger product ID”).
We demonstrate both recursive and iterative search code and show how to handle edge cases
(empty, min/max, single-node). Successor/predecessor logic helps in range queries or
“next-larger” ID queries.
"""

import timeit
from typing import Any


class BSTNode:
    """
    A node in the binary search tree.

    Stores:
    - key
    - pointers: left, right
    - optional pointer to parent (for easy successor/predecessor).
    """

    def __init__(self, key: Any, parent: BSTNode | None = None) -> None:
        self.key = key
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None
        self.parent: BSTNode | None = parent


class BST:
    """
    A BST with both recursive and iterative search, plus methods to find.

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
        """Search for key using recursive approach."""
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
        """Search for key using iterative approach."""
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
        """Return the BSTNode for the given key instead of just True/False."""
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
        Return the node's in-order successor (next-larger).

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
        Return the node's in-order predecessor (next-smaller).

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
    Demonstrate main functionality.

    We'll insert some data, compare recursive vs iterative search times,
    show min/max, and check successor/predecessor.

    Also prints complexity details as a reference:
    * Time: O(log n) average, O(n) worst if skewed
    * Space: O(h) recursion stack or O(1) iterative

    We then run doctests to verify correctness.
    """
    import random

    print("Complexities for BST Search Variations and Edge Cases:")
    print(" - Average Time Complexity: O(log n) for random or balanced data.")
    print(" - Worst Case Time Complexity: O(n) if the tree is skewed.")
    print(
        " - Space Complexity: O(h) for recursion, or O(1) iterative, where h = tree height.\n",
    )

    # Build a BST with some random values
    values = [random.randint(0, 50) for _ in range(10)]
    bst = BST()
    for val in values:
        bst.insert(val)

    # Demonstrate searches
    target = values[len(values) // 2]  # pick some item from the list
    rec_time = timeit.timeit(lambda: bst.search_recursive(target), number=1000)
    itr_time = timeit.timeit(lambda: bst.search_iterative(target), number=1000)

    print(f"Recursive search for {target} repeated 1000 times: {rec_time:.5f}s")
    print(f"Iterative search for {target} repeated 1000 times: {itr_time:.5f}s")

    # Show min, max
    mn = bst.min_node()
    mx = bst.max_node()
    print("Min node key:", mn.key if mn else "None")
    print("Max node key:", mx.key if mx else "None")

    # Check successor/predecessor if exist
    if mn and mx and mn != mx:
        succ = bst.successor(mn)
        if succ:
            print(f"Successor of min node ({mn.key}): {succ.key}")
        pred = bst.predecessor(mx)
        if pred:
            print(f"Predecessor of max node ({mx.key}): {pred.key}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
