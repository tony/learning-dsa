#!/usr/bin/env python
"""
1. BST Fundamentals: Insert, Search, Delete, and Traversals.

Concepts
--------
- Definition of a basic Binary Search Tree (BST): nodes have left < root < right by key.
- Core operations: insert, search, delete.
- Common traversals: in-order, pre-order, post-order with their complexities.

Algorithm
---------
Insert:
  1. Compare new value with current node’s key.
  2. Move left or right accordingly until a leaf position.
  3. Insert once you find a None pointer.

Search:
  1. Compare the target with the current node’s key.
  2. Move left or right until found or None is reached.

Delete:
  1. Find the node.
  2. If 0 children, remove directly.
  3. If 1 child, replace it with the child.
  4. If 2 children, swap with successor (or predecessor), then remove swapped node.

Traversals:
- In-order (left, root, right)
- Pre-order (root, left, right)
- Post-order (left, right, root)

Complexities
------------
- Worst-case: O(n) if the tree is skewed (like inserting sorted data).
- Average case: O(log n) for balanced or random data inserts.

Narrative
---------
In an SRAS pipeline or data system, a simple BST may suffice for moderate, random data. But skewed
inserts degrade performance to O(n), motivating self-balancing strategies later.
"""

import timeit
from typing import Any


class BSTNode:
    """
    A node in the binary search tree.

    Attributes
    ----------
    key : Any
        The key used to order nodes in the BST (left < root < right).
    left : Optional[BSTNode]
        Left subtree pointer.
    right : Optional[BSTNode]
        Right subtree pointer.
    """

    def __init__(self, key: Any) -> None:
        self.key = key
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


class BST:
    """
    A simple Binary Search Tree implementation with insert, search, and delete operations,
    plus in-order, pre-order, and post-order traversals.

    Examples
    --------
    >>> bst = BST()
    >>> bst.insert(5)
    >>> bst.insert(2)
    >>> bst.insert(8)
    >>> bst.insert(1)
    >>> bst.insert(3)
    >>> bst.search(3)
    True
    >>> bst.search(10)
    False
    >>> bst.in_order()  # In-order yields sorted keys
    [1, 2, 3, 5, 8]
    >>> bst.delete(2)
    >>> bst.in_order()
    [1, 3, 5, 8]
    >>> bst.delete(5)
    >>> bst.in_order()
    [1, 3, 8]
    """

    def __init__(self) -> None:
        self.root: BSTNode | None = None

    def insert(self, key: Any) -> None:
        """
        Insert a new key into the BST. If key already exists, this example does not handle duplicates
        (either skip or define your own policy).
        """
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node: BSTNode | None, key: Any) -> BSTNode:
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        # if key == node.key: define policy for duplicates (skip, count, etc.)
        return node

    def search(self, key: Any) -> bool:
        """
        Search for a key in the BST.

        Returns True if found, False otherwise.

        Complexity:
        - Worst-case O(n) if skewed,
        - Average O(log n).
        """
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            current = current.left if key < current.key else current.right
        return False

    def delete(self, key: Any) -> None:
        """Delete a key from the BST if it exists."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node: BSTNode | None, key: Any) -> BSTNode | None:
        if node is None:
            return None  # key not found
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        # key == node.key: remove this node
        elif node.left is None and node.right is None:
            return None  # no children
        elif node.left is None:
            return node.right  # one child (right)
        elif node.right is None:
            return node.left  # one child (left)
        else:
            # two children: swap with successor (smallest in right subtree)
            successor = self._find_min(node.right)
            node.key = successor.key
            node.right = self._delete_recursive(node.right, successor.key)
        return node

    def _find_min(self, node: BSTNode) -> BSTNode:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def in_order(self) -> list[int]:
        """Return a list of keys from an in-order traversal (left, root, right)."""
        result: list[int] = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node: BSTNode | None, result: list[int]) -> None:
        if node is not None:
            self._in_order_recursive(node.left, result)
            result.append(node.key)
            self._in_order_recursive(node.right, result)

    def pre_order(self) -> list[int]:
        """Return a list of keys from a pre-order traversal (root, left, right)."""
        result: list[int] = []
        self._pre_order_recursive(self.root, result)
        return result

    def _pre_order_recursive(self, node: BSTNode | None, result: list[int]) -> None:
        if node is not None:
            result.append(node.key)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)

    def post_order(self) -> list[int]:
        """Return a list of keys from a post-order traversal (left, right, root)."""
        result: list[int] = []
        self._post_order_recursive(self.root, result)
        return result

    def _post_order_recursive(self, node: BSTNode | None, result: list[int]) -> None:
        if node is not None:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.key)


def main() -> None:
    """
    Main demonstration:
    We'll insert some data into the BST, then do a quick timing of search operations.

    Narrative:
    A small demonstration of how a BST might be used in an SRAS system for moderate random data.
    For large or potentially skewed data, self-balancing is essential to keep these operations O(log n).
    """
    import random

    # Create a BST and insert random data
    bst = BST()
    data = [random.randint(0, 9999) for _ in range(50)]  # moderate
    for val in data:
        bst.insert(val)

    # Time searching for a value that may or may not exist
    search_val = data[len(data) // 2]  # pick a middle value
    search_time = timeit.timeit(lambda: bst.search(search_val), number=1000)
    print(f"Searching for {search_val} 1000 times took {search_time:.5f} seconds.")
    print("In-order traversal (showing sorted data):", bst.in_order())


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
