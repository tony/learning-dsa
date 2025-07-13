#!/usr/bin/env python
"""
3. Slices, Memory, and Pythonic List Operations.

Data Structure: Python List (Focusing on Slicing)

Concepts:
- Python list slicing allows extracting sublists efficiently.
- Slicing a list of length n for a slice of length k costs O(k) time to create the new slice.
- In-place operations that involve shifting elements also depend on k, the size of the slice.
- Space complexity for creating a new slice is O(k), as it copies k elements into a new list.

Complexities:
- Slicing a list: O(k) time to copy the sliced portion.
- In-place insertions/deletions via slicing: O(k) time, plus O(n) shifting in worst cases if we replace a large slice at arbitrary positions.
- Space: O(k) for new slices since we allocate a new list of size k.
- Best case: If k is small, slicing overhead is low.
- Worst case: Large slices or frequent slicing operations can impact performance linearly with slice size.

Narrative:
When preprocessing raw data, we may have a large list of records. Pythonic slicing and list comprehensions let us quickly extract relevant portions of the data. For example, if we only need the first 100 lines or want to skip a header row, slicing makes it easy. While slicing is O(k), if k is small relative to n, it’s very convenient. As we scale to larger datasets, we must remain aware that slicing large portions can add overhead proportional to that slice size.

Doctests:
We'll show simple slicing operations and confirm they produce the expected sublists.

Run `python -m doctest -v thisfile.py` or `pytest --doctest-modules` to verify.
"""

import timeit


def demonstrate_slicing() -> None:
    """
    Examples.
    --------
    >>> data = [i for i in range(10)]
    >>> sub = data[2:5]  # slice length k=3
    >>> sub
    [2, 3, 4]
    >>> len(sub)
    3
    >>> # In-place replacement using slicing:
    >>> data[2:5] = [20,30]  # replacing k=3 elements with k=2 elements
    >>> data
    [0, 1, 20, 30, 5, 6, 7, 8, 9]
    >>> # This shifting elements beyond index 5 occurs O(n) in worst case if we consider large replacements
    """


def main() -> None:
    """
    Demonstrate main functionality.

    - We'll time slicing operations on lists of various sizes.
    - Show that slicing a segment of length k takes O(k) time to create the new slice.

    Narrative:
    For preprocessing large datasets, slicing a portion of data (like the first 10,000 lines)
    takes time proportional to the slice size. This is usually fine for moderate slices and very
    Pythonic, but repeated slicing of very large chunks can add up in a big pipeline.
    """
    # Setup
    n = 1_000_000
    data = list(range(n))
    k = 10_000  # slice length
    slice_time = timeit.timeit(lambda: data[:k], number=1000)
    print(
        f"Creating a slice of length {k} from a list of size {n}, 1000 times: {slice_time:.5f}s",
    )

    # This demonstrates O(k) complexity for the slicing operation.
    # If we double k, we’d expect roughly double the time for the same number of operations.

    print()
    print(
        "Slicing is O(k) in the length of the slice. For large k, this can be significant.",
    )
    print(
        "For our data analytics pipeline, small slices (like skipping a header row) are cheap.",
    )
    print(
        "Large slices are still linear in the slice size, which is usually manageable but must be considered.",
    )
    print(
        "This Pythonic idiom remains convenient and clear, often worth the O(k) cost for simplicity.",
    )


if __name__ == "__main__":
    main()
