#!/usr/bin/env python
"""
9. Optimal BST with Known Frequencies: Knuth’s DP Algorithm.

Concepts:
- We have n sorted keys, each with a known frequency of access.
- We compute a BST that minimizes the expected search cost using dynamic programming.
- Standard approach is O(n^3) time, or O(n^2) with advanced optimization (Knuth's
trick).
- Here we show the O(n^3) version for clarity, then reconstruct the BST.

Algorithm Outline:
1) cost[i,j]: minimal cost of building an optimal BST from keys i..j
2) weight[i,j]: sum of frequencies freq[i..j]
3) root[i,j]: index of which key is the root of the optimal subtree
4) Reconstruct the tree using 'root' table.

Complexities:
- Building the DP: O(n^3) naive
- Searching in the final BST: ~ O(h) with h near log n if keys with high freq end up
near top

Narrative:
In SRAS, if certain IDs have high frequencies, placing them near the root cuts average search cost.
But we must pay O(n^3) (or O(n^2)) to compute it offline, only worthwhile if we truly know frequencies.
"""

from __future__ import annotations


class OBSTNode:
    """
    A node in the Optimal BST:

    - key: the actual key
    - left, right: children.
    """

    def __init__(self, key: int) -> None:
        self.key = key
        self.left: OBSTNode | None = None
        self.right: OBSTNode | None = None


def build_optimal_bst(keys: list[int], freq: list[float]) -> OBSTNode | None:
    """
    Build an optimal BST from sorted 'keys' with 'freq' frequencies via O(n^3) DP.

    keys[i] sorted ascending, freq[i] is frequency for that key.
    length of keys == len(freq) == n

    Returns the root of the reconstructed BST.
    """
    n = len(keys)
    # cost[i][j]: minimal weighted cost for keys i..j
    cost = [[0.0] * (n + 1) for _ in range(n + 1)]
    # weight[i][j]: sum of freq[i..j]
    weight = [[0.0] * (n + 1) for _ in range(n + 1)]
    # root[i][j]: which index k in [i..j] is root
    root_table = [[0] * (n + 1) for _ in range(n + 1)]

    # For convenience, we’ll number keys 1..n in DP, so shift index
    # cost[i][i-1] = 0, weight[i][i-1] = 0 => empty subtrees
    # We'll fill i..i in a loop, then expand j>i

    for i in range(1, n + 1):
        cost[i][i - 1] = 0.0
        weight[i][i - 1] = 0.0

    # fill for length=1 (i..i)
    for i in range(1, n + 1):
        cost[i][i] = freq[i - 1]  # freq is 0-based, DP is 1-based
        weight[i][i] = freq[i - 1]
        root_table[i][i] = i

    # Now do subtrees of length=2..n
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):  # i..i+len-1
            j = i + length - 1
            # compute weight[i][j]
            weight[i][j] = weight[i][j - 1] + freq[j - 1]
            cost[i][j] = float("inf")
            # test each k in [i..j] as root
            for k in range(i, j + 1):
                c = cost[i][k - 1] if k > i else 0.0
                c += cost[k + 1][j] if k < j else 0.0
                c += weight[i][j]  # add sum of freq for subtree
                if c < cost[i][j]:
                    cost[i][j] = c
                    root_table[i][j] = k

    # Reconstruct the BST from root_table
    return build_obst_tree(keys, root_table, 1, n)


def build_obst_tree(
    keys: list[int],
    root_table: list[list[int]],
    i: int,
    j: int,
) -> OBSTNode | None:
    """Recursively build the OBST using root_table. i..j in 1-based indexing."""
    if j < i:
        return None
    r = root_table[i][j]  # index of root in [i..j]
    node = OBSTNode(keys[r - 1])  # keys is 0-based
    node.left = build_obst_tree(keys, root_table, i, r - 1)
    node.right = build_obst_tree(keys, root_table, r + 1, j)
    return node


def inorder_traverse(root: OBSTNode | None, arr: list[int]) -> None:
    if root:
        inorder_traverse(root.left, arr)
        arr.append(root.key)
        inorder_traverse(root.right, arr)


def main() -> None:
    """
    Main demonstration:

    Suppose we have keys=[10,20,30,40], freq=[3,2,6,1].
    We'll build an optimal BST via O(n^3) DP,
    then do an inorder to show BST ordering.

    Typically, the key with highest freq (30) ends near root to minimize cost.
    """
    keys = [10, 20, 30, 40]

    freq = [3.0, 2.0, 6.0, 1.0]  # e.g. 30 is highest freq => likely root
    root = build_optimal_bst(keys, freq)

    arr: list[int] = []
    inorder_traverse(root, arr)
    print("Inorder of the resulting optimal BST:", arr)


if __name__ == "__main__":
    main()
