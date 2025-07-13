#!/usr/bin/env python
"""
2. Fixed-Size Arrays.

Data Structure: Fixed-Size Array

Concepts:
A fixed-size array is a contiguous block of memory storing elements of the same type. Its size is determined at creation and cannot be changed. While Python doesn't have a native fixed-size array without resizing, we can simulate it or imagine a lower-level language scenario.

Complexities:
- Access by index: O(1) (direct indexing)
- Insert at end: O(n) if we must copy into a larger array since size is fixed (no
amortized benefit)
- Insert at arbitrary position: O(n) due to shifting elements
- Search (linear): O(n) if we must scan the array
- Space: O(n) where n is the fixed capacity
No amortized improvements since size is not dynamic.

Narrative:
In our Data Analytics Pipeline, initially, we might just load a fixed number of data lines into a fixed-size array (imagine a CSV with a known row count). Access is constant time by index, but adding more items beyond the fixed capacity is costly (we must allocate a bigger array and copy). As data grows unpredictably, fixed-size arrays become inconvenient, prompting us to consider dynamic arrays (Python lists) next.

Doctests:
We’ll show basic access and update operations. No resizing is possible here.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to test.
"""

import timeit


def fixed_size_array_example() -> None:
    """
    Simulate a fixed-size array by creating a Python list of fixed length.

    and treating it as if we cannot change its size.

    We'll show basic O(1) access and O(n) insertion at arbitrary position (simulated),
    though we won't actually resize here since it's fixed-size.

    Examples
    --------
    >>> arr = [None] * 5  # fixed-size array of length 5
    >>> arr[0] = 10       # O(1) assignment
    >>> arr[0]
    10
    >>> arr[4] = 20       # assign at end still O(1)
    >>> arr[4]
    20
    >>> # Searching (linear):
    >>> 10 in arr
    True
    >>> 99 in arr
    False
    """


def main() -> None:
    """
    Main demonstration:

    We will measure access and search times on a fixed-size array simulation.
    Access by index is O(1), searching requires O(n) scanning.

    Narrative:
    Initially, if we know the exact number of lines we’ll process (e.g., a fixed-size dataset),
    a fixed-size array might suffice. Access is O(1) and simple. But if we need to insert beyond
    the fixed capacity or frequently rearrange, O(n) operations and complete copies become a bottleneck
    as data scales. This sets the stage for dynamic arrays (covered next), which handle unknown growth better.
    """
    # Simulate a fixed-size array of a given size
    n = 100_000
    arr = list(range(n))  # fixed-size array simulation with known elements

    # Access time measurement (random index)
    access_time = timeit.timeit(lambda: arr[n // 2], number=1_000_000)
    print(
        f"Accessing a fixed-size array element 1,000,000 times took: {access_time:.5f} seconds (O(1) each).",
    )

    # Searching (linear)
    # Searching for a value near the end ensures O(n) behavior
    search_time = timeit.timeit(lambda: (n - 1 in arr), number=10)
    print(
        f"Searching for an element near the end of the array 10 times took: {search_time:.5f} seconds.",
    )
    print("As n grows, searching scales linearly, O(n).")

    print()
    print("Fixed-size arrays provide O(1) index access but no easy resizing.")
    print(
        "As data grows unpredictably, fixed-size arrays force costly O(n) operations when resizing or inserting.",
    )
    print("This motivates using dynamic arrays (Python lists) in the next chapter.")


if __name__ == "__main__":
    main()
