Below is a **comprehensive, expanded tutorial** on **binary search trees (BSTs)**. We retain the chapter-based structure, ensuring each chapter focuses on **one primary concept** or **closely related** concepts. Each chapter can be turned into a **Python file** with:

- **Docstring** summarizing the chapter’s topic,
- **Doctests** demonstrating functionality (e.g., insert, search),
- **A `main()`** method providing a quick usage or timing example when run directly.

Throughout, we reference an **SRAS (Smart Routing and Analytics System)** scenario, imagining we store and manipulate data about deliveries, routes, or product IDs in BST-based structures. This **Part II** is a stand-alone, in-depth BST tutorial, from beginner fundamentals to advanced self-balancing, heuristics, and specialized multiway trees.

---

## Part II: Binary Search Trees and Advanced Tree Concepts

### 1. **BST Fundamentals: Insert, Search, Delete, and Traversals**
- **Concepts**:  
  - Definition of a basic Binary Search Tree (BST): nodes have left < root < right by key.  
  - Overview of core operations: **insert**, **search**, **delete**.  
  - Common traversal orders: **in-order**, **pre-order**, **post-order**, with their complexities and usage.

- **Algorithm**:  
  - **Insert**:
    1. Compare the new value with the current node’s key.
    2. Recurse or iterate to the left or right subtree.
    3. Insert once you find a `None` (leaf) position.
  - **Search**:
    1. Compare the target with the current node’s key.
    2. Move left or right accordingly until found or a `None` pointer is reached.
  - **Delete**:
    1. Find the node.
    2. If 0 children, remove it directly.
    3. If 1 child, replace with the child.
    4. If 2 children, swap with successor (or predecessor), then remove the swapped node.
  - **Traversals** (in-order, pre-order, post-order) for visiting nodes in different orders.

- **Complexities**:  
  - **Worst-case**: \(O(n)\) if the tree is **skewed** (like inserting ascending data).  
  - **Average**: \(O(\log n)\) for **random** or near-balanced data.

- **Narrative**:  
  In an SRAS pipeline or data system, we might begin with a simple BST for moderate data that we insert randomly. But if the data distribution leads to skew, performance suffers. This naturally motivates **self-balancing** strategies.

---

### 2. **BST Search Variations and Handling Edge Cases**
- **Concepts**:  
  - **Recursive vs. Iterative** BST search implementation details.  
  - **Edge cases**: empty tree, searching for min or max, or searching in a single-node tree.  
  - Finding **successor** (next-larger key) and **predecessor** (next-smaller key):
    - If the node has a right subtree, successor is the leftmost node in the right subtree.
    - Otherwise, follow parent pointers upward until you traverse from left to right.

- **Algorithm**:  
  - **Recursive Search**:  
    \(\text{searchBST(node, target): if node is None return False, else if node.key == target return True, else recurse left or right.}\)  
  - **Iterative Search**:  
    \(\text{while current is not None: compare target with current.key, move left or right, or return if found.}\)
  - **Successor & Predecessor**:
    - Explore subtrees or keep a local variable tracking the “next-larger” or “next-smaller” during search.
  - **Complexities**:  
    - **Time**: Best/Average \(O(\log n)\), but can degrade to \(O(n)\) if the tree is skewed.  
    - **Space**: \(O(h)\) for recursion stack or \(O(1)\) iteratively.

- **Narrative**:  
  SRAS might want to do range queries (“find the next-larger product ID after X”). Successor/predecessor routines help. We show both **recursive** code (which is concise) and **iterative** code (which uses no extra stack).

---

### 3. **Tree Height and Skewness: Why Self-Balancing Is Needed**
- **Concepts**:  
  - **Height** of a BST is the longest path from root to leaf.  
  - Inserting ascending values (like 1,2,3,4,...) can lead to a skewed, essentially linked-list-shaped BST.  
  - Skewed BST yields **worst-case** operations of \(O(n)\).

- **No single new algorithm** here, but this sets the stage for balancing.

- **Complexities**:  
  - Demonstrates naive BST can degrade from average \(\log n\) to worst-case \(n\) time if data is unlucky.

- **Narrative**:  
  In SRAS, if data is partially sorted or arrives in ascending or descending order (like sorted route IDs), the naive BST becomes a performance bottleneck (\(O(n)\) per operation). We must consider **self-balancing** BST solutions.

---

### 4. **Height-Balanced (AVL) Trees: Rotations and Invariants**
- **Concepts**:  
  - **AVL** property: height difference of left vs. right subtree at any node is \(\le 1\).  
  - **Rotations** (single & double) to rebalance after insert/delete.  
  - Maintaining an integer “height” or “balance factor” in each node.

- **Algorithm**:  
  - **Insert** in BST fashion, then backtrack up updating heights.  
  - If balance factor goes beyond \(\pm 1\), **rotate**:
    - **Left rotation** or **right rotation** if it’s a single imbalance.
    - **Double rotation** if it’s a “zig-zag” pattern.  
  - **Delete** similarly rebalances.  

- **Complexities**:  
  - **Search/Insert/Delete** remain \(O(\log n)\) guaranteed because the tree is rebalanced constantly.  

- **Narrative**:  
  For an SRAS pipeline with frequent inserts or random data patterns, an AVL tree keeps operations consistently \(\log n\). A rotation step ensures no skew develops.

---

### 5. **Red-Black Trees: Balanced BST with Simpler Balancing Rules**
- **Concepts**:  
  - **Red-Black** properties: coloring each node red or black, no two reds in a row, black height consistent across paths.  
  - Insert & delete rebalancing revolve around recoloring, rotations if needed.

- **Algorithm**:  
  - **Insert** a new node as red, fix color violations with recolors/rotations.  
  - **Delete** might introduce a “black deficit”; fix with recolors or rotations.  

- **Complexities**:  
  - **Worst-case**: \(O(\log n)\) for search/insert/delete, keeps the tree near balanced.

- **Narrative**:  
  A simpler set of rebalancing steps compared to AVL, widely used in practice (like C++ `std::map`, Java’s `TreeMap`). For SRAS, if a standard library provides a Red-Black tree, we can rely on its guaranteed \(\log n\) operations.

---

### 6. **Treap**: Randomized BST with Heap Priority
- **Concepts**:  
  - Each node has a **key** for BST ordering, plus a random **priority** for a “heap” property.  
  - Insert in BST order, then rotate if child’s priority is higher (for max-heap) or lower (for min-heap) than its parent.

- **Algorithm**:  
  - **Insert**:
    1. Insert by BST key.
    2. Assign random priority.
    3. Rotate up if priority violates heap property.
  - **Delete**:
    1. Rotate the node down until it’s a leaf, then remove it.
  
- **Complexities**:  
  - Expected \(\log n\) height if random priorities are uniform, so all BST operations in \(O(\log n)\) on average.

- **Narrative**:  
  Treaps can be simpler to implement than Red-Black or AVL, with expected \(\log n\) performance thanks to randomization. In an SRAS environment, if we don’t want to code complex balancing rules, a Treap is a good alternative.

---

### 7. **Splay Trees**: Self-Adjusting BST
- **Concepts**:  
  - **Splaying**: any access (search, insert, or delete) brings the accessed node to root via a series of rotations (zig, zig-zig, zig-zag).  
  - **Amortized** \(\log n\) time, though any single operation can degrade to \(O(n)\) if the tree is extremely unbalanced prior to splaying.

- **Algorithm**:  
  - **Access**: search for a node, once found (or insertion point found), splay that node to root.  
  - **Delete**: find and splay the node to root, remove it, then reattach subtrees.
  
- **Complexities**:  
  - **Amortized** \(O(\log n)\), single operation might be \(O(n)\).  

- **Narrative**:  
  In SRAS, if we repeatedly access the same product IDs, splay trees move those “hot” items near the root, making repeated accesses faster than a standard BST might. Over time, we get near \(\log n\) performance on average.

---

### 8. **Weight-Balanced / Size-Balanced BSTs**
- **Concepts**:  
  - Each node maintains a “size” (number of nodes in its subtree).  
  - On insertion/deletion, if a subtree is too large compared to its sibling, perform rotations to rebalance.

- **Algorithm**:  
  - **Insert/Delete** as in BST. Then check “size balance” ratio on the way back up. If ratio is exceeded, rotate to restore balance.

- **Complexities**:  
  - Maintains \(\log n\) height, so search/insert/delete in \(O(\log n)\).

- **Narrative**:  
  If SRAS data arrives in bursts, a size-balanced approach can keep the tree balanced in a straightforward way (no complicated balancing factors, just subtree size checks).

---

### 9. **Optimal BST with Known Frequencies: Knuth’s DP Algorithm**
- **Concepts**:  
  - If each key has a known probability/frequency of access, we can build a BST that minimizes expected search cost.  
  - DP tries all possible roots for subtrees, storing minimal weighted cost.

- **Algorithm**:  
  - **Knuth’s DP** or standard “optimal BST” DP in \((n^3)\) or \((n^2)\) with advanced optimization.  
  - Once built, searches average \(\approx \log n\) or better if high-frequency keys are near root.

- **Complexities**:  
  - Building the tree: \(\;O(n^3)\) naive, \(\;O(n^2)\) with known optimization.  
  - Searching afterward: \(O(\log n)\) or at least \(O(h)\) for the resulting balanced structure.

- **Narrative**:  
  In SRAS, if certain IDs are extremely frequent, an optimal BST places them near the top for minimal average search cost. But the DP overhead means we only do this offline if we truly know the frequencies.

---

### 10. **Approximate/Heuristic Approaches to Optimal BST**
- **Concepts**:  
  - **Mehlhorn’s** approximation, or other heuristics, might build near-optimal BST without the full \((n^3)\) cost.  
  - Possibly mention **Hu–Tucker**, **Garsia–Wachs** for special cases like “alphabetic” or “linear” distributions.

- **No single new algorithm**; we discuss heuristics.

- **Complexities**:  
  - Typically faster than the full DP approach.  
  - Search time near-optimal if frequencies are accurate.

- **Narrative**:  
  For large SRAS sets where full DP is infeasible, these heuristics yield almost-optimal average search times at reduced construction cost.

---

### 11. **B-Trees (External Memory / Disk)**
- **Concepts**:  
  - A **multi-way** balanced tree where each node can hold multiple keys/children.  
  - Minimizes disk I/O by grouping large blocks of keys.

- **Algorithm**:  
  - **Insert**: if a node is full, split it; keep tree height \(\log_m n\).  
  - **Search**: do a multiway search within the node’s keys, pick the correct child pointer.

- **Complexities**:  
  - Typically \(\;O(\log n)\) for search/insert/delete, but the branching factor might be large in practice.

- **Narrative**:  
  If SRAS data is so large that we store it on disk/SSD, B-trees are standard in databases, ensuring minimal disk accesses to traverse the tree.

---

### 12. **2-3 Trees & Other Multiway Balanced Structures**
- **Concepts**:  
  - **2-3 Tree**: each node can have 2 or 3 children, maintaining perfect height balance.  
  - A stepping-stone concept to B-trees in memory-limited contexts.

- **Algorithm**:  
  - Insertion merges or splits nodes to keep 2-3 structure.  
  - Deletion fuses nodes if they become underfilled.

- **Complexities**:  
  - \(\;O(\log n)\) for standard operations.  

- **Narrative**:  
  If SRAS keeps data in memory but wants simpler multiway balancing than a B-tree, a 2-3 tree ensures shallow height, all operations \(\;O(\log n)\).

---

### 13. **T-Trees**: In-Memory Balanced Trees for Databases
- **Concepts**:  
  - Combines aspects of **AVL** (height balancing) with **B-trees** (storing multiple values per node), reducing pointer overhead.  
  - Often used in in-memory databases.

- **Algorithm**:  
  - Similar insertion/deletion as an AVL, but each node can hold an array of values.  
  - Rotations happen on node-level if unbalanced.

- **Complexities**:  
  - \(\;O(\log n)\) for search, insert, delete, all in memory.  

- **Narrative**:  
  In an SRAS with large memory, T-trees may reduce overhead. If we store multiple route IDs in each node, we have fewer pointers and better CPU cache locality.

---

### 14. **Tree Sort**: Sorting by Inserting into a BST + In-Order Traversal
- **Algorithm**:  
  - Insert all elements into a BST (preferably **self-balancing**).  
  - Perform an in-order traversal to collect them in sorted order.

- **Complexities**:  
  - With a **self-balancing BST**: \(\;O(n \log n)\).  
  - With a naive BST if unlucky: \(\;O(n^2)\).

- **Narrative**:  
  If an SRAS app already maintains data in a balanced BST, we can generate sorted output just by doing in-order traversal. But typically mergesort, quicksort, or Timsort is simpler if we only need sorting.

---

### 15. **Priority Queue from BST / Treap**
- **Concepts**:  
  - A BST (like a **treap**) can interpret node priorities as a “heap” property while keys define BST structure.  
  - Insert, extract-min/max, etc., all in \(\;O(\log n)\) expected.

- **Algorithm**:  
  - **Insert**: BST insert by key, random priority assigned, rotate if child’s priority outranks parent.  
  - **Extract-Min/Max**: splay or rotate the min/max node to the root, then pop it.

- **Complexities**:
  - Typically \(\;O(\log n)\) for all priority queue operations (expected).

- **Narrative**:  
  If SRAS needs both BST lookups and a priority queue (like picking highest-priority route first), a **treap** unifies them seamlessly.

---

**Conclusion of This BST Tutorial**  
We now have a multi-chapter deep dive on BSTs, from naive insertion/search to advanced self-balancing (AVL, Red-Black, Treaps, Splay Trees, etc.) and specialized multiway trees (B-Trees, 2-3 Trees, T-Trees). We also covered how to build or approximate an **optimal BST** if we know key frequencies, how to **sort** using a BST, and how to build a **priority queue** from a BST. This entire part can stand alone as a tutorial or be integrated into a larger course on data structures and algorithms, bridging from fundamental BST usage to advanced techniques relevant to real systems like SRAS.
