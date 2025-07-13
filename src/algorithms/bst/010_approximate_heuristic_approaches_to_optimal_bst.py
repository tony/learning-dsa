#!/usr/bin/env python
"""
10. Approximate/Heuristic Approaches to Optimal BST.

Concepts:
- Instead of the full O(n^3) DP, we can use heuristics to build a near-optimal BST.
- Example heuristics:
  1) Mehlhorn's approximation (not fully shown here),
  2) Garsia-Wachs for "alphabetic trees",
  3) A naive approach: always pick the key with the largest frequency as root,
     then recursively build left and right subtrees.

No single new algorithm here. We illustrate a naive approach for demonstration.

Complexities:
- Typically faster than the full DP approach. The search time can be near-optimal
  if frequencies are accurate and the heuristic picks good roots.

Narrative:
For large SRAS sets where full DP is infeasible, these heuristics yield almost-optimal average
search times at reduced construction cost.
"""

from __future__ import annotations


class Node:
    """
    A simple BST node.

    Stores:
    - key
    - freq: frequency for heuristic building (as a float)
    - left, right children.
    """

    def __init__(self, key: int, freq: float) -> None:
        self.key = key
        self.freq = freq
        self.left: Node | None = None
        self.right: Node | None = None


def build_heuristic_bst(keys: list[int], freqs: list[float]) -> Node | None:
    """
    Build a BST using a naive heuristic.

     1) Find the key with largest freq in [keys], make it root
     2) Recursively build left subtree from keys < root
        and right subtree from keys > root
     3) This is NOT guaranteed to be optimal, but might be decent
        if one key is truly dominant.

    Examples
    --------
    >>> ks = [10,20,30,40]
    >>> fs = [3.0,2.0,6.0,1.0]  # 30 has largest freq => becomes root
    >>> root = build_heuristic_bst(ks, fs)
    >>> inord = []
    >>> def inorder(n):
    ...     if n:
    ...         inorder(n.left)
    ...         inord.append(n.key)
    ...         inorder(n.right)
    >>> inorder(root)
    >>> inord
    [10, 20, 30, 40]
    """
    if not keys:
        return None
    # find index of largest freq
    max_i = 0
    max_f = freqs[0]
    for i in range(1, len(freqs)):
        if freqs[i] > max_f:
            max_f = freqs[i]
            max_i = i

    root = Node(keys[max_i], freqs[max_i])
    left_keys: list[int] = []
    left_freqs: list[float] = []
    right_keys: list[int] = []
    right_freqs: list[float] = []

    # partition
    for i in range(len(keys)):
        if i == max_i:
            continue
        if keys[i] < keys[max_i]:
            left_keys.append(keys[i])
            left_freqs.append(freqs[i])
        else:
            right_keys.append(keys[i])
            right_freqs.append(freqs[i])

    root.left = build_heuristic_bst(left_keys, left_freqs)
    root.right = build_heuristic_bst(right_keys, right_freqs)
    return root


def inorder(n: Node | None, out: list[int]) -> None:
    """Perform in-order traversal and collect keys in out."""
    if n is None:
        return
    inorder(n.left, out)
    out.append(n.key)
    inorder(n.right, out)


def main() -> None:
    """
    Demonstrate main functionality.

    We'll build a naive "largest freq as root" BST for demonstration,
    show that it forms a valid BST, though not truly optimal except
    in the trivial case where one freq is dominant.
    """
    # Suppose we have 5 keys with frequencies (floats)
    keys: list[int] = [5, 10, 20, 30, 40]
    freqs: list[float] = [1.0, 4.0, 2.0, 10.0, 3.0]  # 30 has highest freq=10.0 => root

    root = build_heuristic_bst(keys, freqs)
    inord: list[int] = []
    inorder(root, inord)
    print("In-order of the naive heuristic BST:", inord)


if __name__ == "__main__":
    main()
