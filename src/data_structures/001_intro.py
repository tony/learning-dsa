#!/usr/bin/env python
"""
1. Introduction to Data Structures and Complexity.

Context
-------
Before diving into actual data structures, we need to understand why they matter and how to
evaluate their performance. We'll discuss what algorithms and data structures are, introduce
Big-O notation for complexity, and explain why complexity is crucial for scaling performance
as data grows.

Data Structure: *None* (conceptual introduction)
- We are not implementing a specific data structure in this chapter.
- Instead, we introduce the concept of complexity analysis, which applies to all data
structures.

Complexity Details:
- At this stage, we only discuss complexity conceptually.
- Big-O notation: O(n), O(log n), O(n²), etc., describe how runtime or space usage
grows with input size.
- We'll learn that as data grows, certain complexities lead to performance issues.

Narrative:
Our Data Analytics Pipeline (or SRAS scenario) starts small, but as it handles more data (e.g., more
rows, more products, more queries), poor algorithmic complexity leads to slowdowns. Understanding
complexity now ensures we choose data structures that keep performance stable at large scales.

Doctests:
No specific data structure to test. We may just show that the file runs and a trivial function works.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` if needed.
"""

import timeit


def trivial_operation() -> int:
    """
    Provide a trivial function that does a small, fixed amount of work.

    Not an algorithm or data structure, just a placeholder.

    Complexity: O(1), since it does a constant amount of work.
    """
    total = 0
    for i in range(10):
        total += i
    return total


def main() -> None:
    """
    Demonstrate main functionality.

    - Explain what data structures and algorithms are.
    - Introduce Big-O notation for complexity.
    - Show timing a trivial operation to illustrate that we can measure runtime,
      though this does not scale or show complexity differences yet.

    By understanding complexity now, we set the foundation to analyze actual data structures
    (arrays, lists, trees, hash tables, etc.) in later chapters.
    """
    print("Introduction to Data Structures and Complexity")
    print("------------------------------------------------")
    print("Algorithms: Defined procedures to solve problems.")
    print("Data Structures: Organized ways to store and manage data.")
    print(
        "Complexity (Big-O notation): A tool to describe how runtime or space grows with input size.",
    )
    print()
    print("Timing a trivial operation (purely for demonstration):")
    exec_time = timeit.timeit(trivial_operation, number=100000)
    print(f"Running trivial_operation 100,000 times took: {exec_time:.5f} seconds.")
    print()
    print("This doesn't show scaling yet. Later chapters will apply Big-O notation")
    print(
        "to real data structures as input sizes grow, and we'll see differences between O(n), O(log n), etc.",
    )
    print(
        "This understanding ensures good performance choices in our data analytics pipeline.",
    )


if __name__ == "__main__":
    main()
