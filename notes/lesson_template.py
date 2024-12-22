#!/usr/bin/env python
"""
[Lesson Title].

[Context]
- State the concept: e.g., "This lesson shows how to use asyncio.Lock to ensure safe concurrent access."
- Prerequisites: e.g., familiarity with `asyncio.run()`, basic async/await syntax, event loop model.
- References:
  - Official docs: https://docs.python.org/3/library/asyncio.html
  - Possibly link to previous lessons or advanced usage docs.

[Summary]
- Briefly summarize what learners will take away:
  e.g., "By the end, you'll understand how to protect shared state in async code
         using a lock to avoid race conditions."

Doctests
--------
- Include doctests that demonstrate usage (like usage within a single-file example).
- If concurrency or timing might reorder output, use ellipses (e.g., `# doctest: +ELLIPSIS`).
- Keep sleeps minimal and rely on ellipses for variable concurrency output.
- Ensure `pytest --doctest-modules` or `python -m doctest -v thisfile.py` passes.

Type Hints & Mypy
----------------
- **All annotations** must be **mypy strict compliant** (e.g., `mypy --strict thisfile.py`)
- Add type hints to core functions (e.g. `async def demonstrate_concept() -> str:`).
- For tasks or advanced structures, use `Awaitable`, `Callable`, etc.
- Optionally consider running `mypy --strict thisfile.py` if you want static analysis.

Execution
---------
- Running `python thisfile.py` should execute `main()` and demonstrate the concept.
- Keep the example minimal yet instructive.
- If measuring performance or complexities, print relevant info in `main()` (like timeit).

Additional Notes
---------------
- Comment on tricky parts. If multiple coroutines are used, clarify how concurrency or error handling is structured.
- If an exception is intentionally illustrated, show how to catch or handle it.
"""

import asyncio

# 1. Provide an async function demonstrating the core concept.


async def demonstrate_concept() -> str:
    """
    [Function Purpose]
    This function simulates a short async operation (like a small I/O wait),
    returning a predefined result. Demonstrates the fundamental async/await usage.

    Examples
    --------
    >>> import asyncio
    >>> asyncio.run(demonstrate_concept())
    'Expected Result'
    """
    # Simulate a brief async operation
    await asyncio.sleep(0.001)
    return "Expected Result"


# 2. Provide a 'main()' coroutine that orchestrates the demonstration.


async def main() -> None:
    """
    Main entrypoint for this lesson.

    In more complex lessons, `main()` may handle multiple tasks, concurrency,
    error handling, or advanced synchronization. For now, it just calls the core function
    and prints the result.

    Examples
    --------
    >>> import asyncio
    >>> asyncio.run(main())
    Expected Result
    """
    result = await demonstrate_concept()
    print(result)


# 3. Provide a __main__ guard to allow direct execution and doctesting.

if __name__ == "__main__":
    import doctest

    # (Optional) Print complexity or performance notes:
    print("Complexities: Best is O(...) if concurrency is small, ... etc.")
    # e.g. show a quick timeit measure or concurrency example if desired

    # Run doctests:
    doctest.testmod()

    # Finally, run the main coroutine
    asyncio.run(main())
