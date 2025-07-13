#!/usr/bin/env python
"""
12. 2-3 Trees & Other Multiway Balanced Structures.

Concepts:
- A 2-3 Tree node can hold 1 or 2 keys (thus 2 or 3 children).
- Perfect height balance is maintained, ensuring O(log n) operations.
- Insertion merges or splits nodes to keep each node with 1 or 2 keys.
- A stepping-stone to more general B-Trees.

Algorithm (Insertion Outline):
1) If root is full (has 2 keys) and needs a new key, split root, create a new root with 1 key.
2) Descend to the correct child, possibly splitting along the way if a child is full.
3) Insert the new key in the correct leaf in sorted order, ensuring the node has at most 2 keys.

Complexities:
- O(log n) for search/insert/delete. The height remains small as all leaves are at the same level.

Narrative:
If SRAS is fully in-memory yet needs shallow multiway balancing, a 2-3 tree is simpler than
a B-tree. Each node has at most 2 keys, 3 children. This demonstration omits deletion,
focusing on insertion to illustrate the 2-3 approach.
"""

from __future__ import annotations


class Two3Node:
    """
    A node in a 2-3 tree.

    Stores:
    - keys: list of up to 2 sorted keys
    - children: up to 3 children (2 or 3 pointers), each child is a Two3Node
    - leaf: indicates whether this node has no children.
    """

    def __init__(self, leaf: bool) -> None:
        self.keys: list[int] = []
        self.children: list[Two3Node] = []
        self.leaf = leaf


def is_full_2keys(node: Two3Node) -> bool:
    """Return True if node already has 2 keys."""
    return len(node.keys) == 2


def split_2node(parent: Two3Node, index: int) -> None:
    """
    Split the full child parent.children[index] (which must have 2 keys, then we add 1 =>
    total 3 keys).

    We'll create a new sibling node and push the middle key up into parent.
    """
    child = parent.children[index]

    # child has 3 keys after insertion => pick middle key for parent
    mid_key = child.keys[1]

    new_node = Two3Node(child.leaf)
    # left child keeps child.keys[0], new_node gets child.keys[2]
    left_key = child.keys[0]
    right_key = child.keys[2]

    # reorganize child & new_node
    child.keys = [left_key]
    new_node.keys = [right_key]

    if not child.leaf:
        # child had 3 children => split them
        # child.children => 3 or 4?
        # if child was full, we expect 3 children after insertion. We'll move the last
        # child to new_node. Actually, if it's 2-3 node, after insertion child might have
        # up to 3 children. We do a simple approach.
        # We'll assume child had exactly 3 children if it is full.
        new_node.children = child.children[2:]
        child.children = child.children[:2]

    # Insert mid_key into parent
    parent.keys.insert(index, mid_key)
    parent.children.insert(index + 1, new_node)


def insert_nonfull_2node(node: Two3Node, key: int) -> None:
    """
    Insert 'key' into a node that is not full (has <=1 or 2 keys).

    If leaf, just place the key in sorted order.
    Else find child to descend, split if child is full, then insert in child.
    """
    if node.leaf:
        # Insert key in sorted order in node.keys (which has at most 1 key if we are
        # guaranteed not full).
        node.keys.append(key)
        node.keys.sort()
    else:
        # find child index to descend
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        # if the chosen child is full => split
        if is_full_2keys(node.children[i]):
            # must do a pre-split so we have space
            # first we insert a dummy key in that child => leading to 3 keys => then split
            insert_nonfull_2node(node.children[i], key)
            # now child[i] has 3 keys => split
            split_2node(node, i)
            # after splitting, we see which side to descend
            if key > node.keys[i]:
                i += 1
        else:
            # child not full => just descend
            pass
        # but if we already inserted, we might not need to re-insert?
        # Actually we handle the case that we tried to insert in child (which might not be full).
        # We'll do a second pass if the child had 2 keys but didn't cause a split yet.
        # We'll do a simpler approach:
        if len(node.children) > i:  # double-check bounds
            if len(node.children[i].keys) < 2:  # still not full
                insert_nonfull_2node(node.children[i], key)
        else:
            # fallback in case something changes
            pass


def insert_23(root: Two3Node | None, key: int) -> Two3Node:
    """
    Insert key into a 2-3 tree with root 'root'.

    If root is full, create new root node and split root.
    Return new root after insertion.
    """
    if root is None:
        # empty tree
        new_root = Two3Node(True)
        new_root.keys = [key]
        return new_root

    # if root is full (2 keys), we do a top-level split approach:
    if is_full_2keys(root):
        # create a new parent
        new_parent = Two3Node(False)
        new_parent.children.append(root)
        # forced insert key into child => might cause child to have 3 keys => then we do split
        insert_nonfull_2node(root, key)
        # see if root has 3 keys => split
        if len(root.keys) == 3:
            split_2node(new_parent, 0)
        return new_parent
    # root not full => just insert
    insert_nonfull_2node(root, key)
    return root


def inorder(node: Two3Node | None, arr: list[int]) -> None:
    """In-order traversal for a 2-3 tree: for each key, we traverse child i, then key i, etc."""
    if not node:
        return
    # in a 2-3 node, we might have 1 or 2 keys, 2 or 3 children
    # If node has 1 key => children can be up to 2
    if len(node.keys) == 1:
        #  up to 2 children => child[0], key[0], child[1]
        if len(node.children) > 0:
            inorder(node.children[0], arr)
        arr.append(node.keys[0])
        if len(node.children) > 1:
            inorder(node.children[1], arr)
    elif len(node.keys) == 2:
        # up to 3 children => c[0], k[0], c[1], k[1], c[2]
        if len(node.children) > 0:
            inorder(node.children[0], arr)
        arr.append(node.keys[0])
        if len(node.children) > 1:
            inorder(node.children[1], arr)
        arr.append(node.keys[1])
        if len(node.children) > 2:
            inorder(node.children[2], arr)


def main() -> None:
    """
    Minimal demonstration of 2-3 tree insertion (no deletion).

    We'll insert keys => see an in-order output is sorted.
    The structure is simplistic, not all corner cases are handled, but
    it shows the idea of 2-3 tree: each node 1 or 2 keys, splitted if 3 keys appear.
    """
    data = [5, 1, 2, 10, 6, 7, 20, 15]
    root: Two3Node | None = None
    for x in data:
        root = insert_23(root, x)

    arr: list[int] = []
    inorder(root, arr)
    print("2-3 Tree in-order traversal:", arr)


if __name__ == "__main__":
    main()
