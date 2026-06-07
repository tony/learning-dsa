# AGENTS.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Essential Commands
```bash
# Install dependencies
uv sync --all-extras --dev

# Run tests
uv run pytest

# Run tests with watch mode (auto-rerun on file changes)
uv run pytest-watcher

# Run a single test file
uv run pytest src/algorithms/002_linear_search.py

# Lint and format code
uv run ruff check .
uv run ruff format .

# Type checking
uv run mypy .

# Run doctests for a specific file
python -m doctest -v src/algorithms/002_linear_search.py
```

## Code Architecture

This is an educational project for learning data structures and algorithms, organized as numbered lessons with a consistent structure:

### Project Structure
- `src/algorithms/`: Algorithm implementations (001-019 + bst subfolder)
- `src/data_structures/`: Data structure implementations (001-010)
- Each lesson is a self-contained module that can be run with `python filename.py`

### Lesson Template Structure

All lessons follow the template in `notes/lesson_template.py`. The exact structure is:

```python
#!/usr/bin/env python
"""
[Lesson Number]. [Lesson Title].

Algorithm: [Algorithm Name] or Data Structure: [Structure Name]

Concepts:
- Core concept explanation
- Best case: O(?) complexity with condition
- Average case: O(?) complexity
- Worst case: O(?) complexity with condition
- Space complexity: O(?)

Narrative:
[Connection to either Data Analytics Pipeline or SRAS (Smart Routing and Analytics System)]
[Explanation of why this concept matters in the growing system]

Doctests:
[Brief description of what the doctests demonstrate]
"""

import timeit
from typing import Any

def main_concept_function(params: type) -> ReturnType:
    """
    Purpose description.
    
    Complexity:
    - Best: O(?) when condition
    - Average: O(?)
    - Worst: O(?) when condition
    - Space: O(?)
    
    Examples
    --------
    >>> main_concept_function(example_input)
    expected_output
    """
    # Implementation
    pass

def main() -> None:
    """
    Main demonstration with performance measurements.
    Shows practical examples and timing comparisons.
    """
    # Performance testing with timeit
    # Result interpretation with narrative context
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
```

### Narrative Flows

The project uses two main narrative contexts:

1. **Data Analytics Pipeline** (for data structures):
   - Starts with storing raw data (arrays, lists)
   - Progresses to task management (stacks, queues)
   - Advances to efficient lookups (hash tables, trees)
   - Culminates in specialized structures (indexes)

2. **SRAS - Smart Routing and Analytics System** (for algorithms):
   - Begins with basic searching and sorting
   - Evolves to handle growing data volumes
   - Introduces optimization techniques
   - Addresses real-world constraints

### Learning Progressions

Follow the numbered progressions in:
- `notes/progression-ds.md`: Data structures learning path
- `notes/progression-algo.md`: Algorithms learning path
- `notes/progression-algo-binary-search-trees.md`: BST-specific progression

### Key Development Practices
- All code must pass `mypy --strict`
- Use numpy docstring convention
- Include comprehensive doctests in all implementations
- Each module should be runnable standalone with meaningful output
- Always include complexity analysis (time and space)
- Connect concepts to the narrative scenarios

### Testing Strategy
- Doctests are the primary testing method (automatically run by pytest)
- Tests should demonstrate usage and edge cases
- Performance timing in main() functions helps understand complexity
- Use minimal sleeps and ellipses for concurrency tests

### Doctests

**All functions and methods MUST have working doctests.** Doctests serve as both documentation and tests.

**CRITICAL RULES:**
- Doctests MUST actually execute - never comment out function calls or similar
- Doctests MUST NOT be converted to `.. code-block::` as a workaround (code-blocks don't run)
- If you cannot create a working doctest, **STOP and ask for help**

**Available tools for doctests:**
- `doctest_namespace` fixtures: `tmp_path` (add more via `conftest.py`)
- Ellipsis for variable output: `# doctest: +ELLIPSIS`

**`# doctest: +SKIP` is NOT permitted** - it's just another workaround that doesn't test anything.

**Example doctest for DSA:**
```python
>>> def binary_search(arr, target):
...     left, right = 0, len(arr) - 1
...     while left <= right:
...         mid = (left + right) // 2
...         if arr[mid] == target:
...             return mid
...         elif arr[mid] < target:
...             left = mid + 1
...         else:
...             right = mid - 1
...     return -1
>>> binary_search([1, 2, 3, 4, 5], 3)
2
>>> binary_search([1, 2, 3, 4, 5], 6)
-1
```

## Git Commit Standards

Format commit messages as:

```
Scope(type[detail]): concise description

why: Explanation of necessity or impact.

what:
- Specific technical changes made
- Focused on a single topic
```

The blank line between the `why:` block and the `what:` block is
optional — useful when the `why:` body runs to multiple lines and the
two sections benefit from visual separation.

Common commit types:

- **feat**: New features or enhancements
- **fix**: Bug fixes
- **refactor**: Code restructuring without functional change
- **docs**: Documentation updates
- **chore**: Maintenance (dependencies, tooling, config)
- **test**: Test-related updates
- **style**: Code style and formatting
- **py(deps)**: Dependencies
- **py(deps[dev])**: Dev Dependencies
- **ai(rules[AGENTS])**: AI rule updates
- **ai(claude[rules])**: Claude Code rules (CLAUDE.md)

Subjects are plain English. Never put curriculum codes or other
repo-internal shorthand in the subject line — a reader of
`git log --oneline` should understand every title cold.

Example:

```
docs(README[setup]): Document the uv-based install

why: New clones failed on the old pip instructions.

what:
- Replace pip commands with uv equivalents
- Note the supported Python floor
```

For multi-line commits, use heredoc to preserve formatting:

```bash
git commit -m "$(cat <<'EOF'
Scope(type[detail]): concise description

why: Explanation of the change.

what:
- First change
- Second change
EOF
)"
```

Guidelines:

- Subject line at most 50 characters; body lines at most 72
- Imperative mood ("Add", "Fix" — not "Added", "Fixed")
- One topic per commit; blank line between subject and body
- Mark breaking changes with `BREAKING:`

## Documentation Standards

### Code blocks are paste-and-run units

One command per triple-backtick block, so pasting a block runs exactly
one intended action. Don't blur multiple commands annotated by comments
into the same block — explanations belong in prose above the block. A
multi-step sequence may share a block only when explicitly chained with
`;` / `; \` (the chain *is* the single action). Command menus are
per-command blocks with prose lead-ins, not tables.

## AI Slop Prevention

Treat AI slop as **review-hostile noise**, not as proof that text or
code is wrong. The goal is to maximize information density by removing
artifacts that make the repository harder to trust or navigate.

### The Anti-Slop Rubric

Before committing, audit all AI-assisted changes for these noise
patterns:

- **AI Signatures:** Remove "Generated by", footers, conversational
  filler ("Certainly!", "Here is..."), unexplained emojis (🤖, ✨), and
  AI-tool metadata.
- **Brittle References:** Avoid hard-coded line numbers, fragile
  file/test counts, dated "as of" claims, bare SHAs, and local
  absolute paths unless they are strict evidentiary artifacts (e.g.,
  benchmark logs).
- **Diff Narration:** Do not restate what moved, was renamed, or was
  removed in artifacts the downstream reader holds: code, docstrings,
  README, CHANGES, PR descriptions, or release notes. The diff and
  commit message already carry this history.
- **Branch-Internal Narrative:** Do not mention intermediate branch
  states, abandoned approaches, or "no longer" behavior unless users
  of a published release actually experienced the old state (**The
  Published-Release Test**).
- **Low-Value Scaffolding:** Remove ownerless TODOs (`TODO: revisit`),
  unused future-proofing, debug artifacts, and defensive wrappers that
  do not protect a currently reachable failure mode.
- **Prose Inflation:** Replace generic AI "tells" like *comprehensive,
  robust, seamless, production-ready, leverage, delve, tapestry,* and
  *best practices* with concrete descriptions of behavior,
  constraints, or trade-offs.

### Preservation & Context

**When unsure, leave the text in place and ask.** Subjective cleanup
must never be a reason to remove load-bearing rationale.

- **Preserve the "Why":** You MUST NOT delete comments that document
  invariants, protocol constraints, platform quirks, security
  boundaries, and upstream workarounds.
- **Evidence is Immune:** Preserve exact counts, dates, and SHAs when
  they serve as evidence in benchmark results, release notes, stack
  traces, or lockfiles.
- **Behavior Over Inventory:** A useful description explains what
  changed for the *system or user*; it does not provide an inventory
  of files or functions the diff already shows.

### The Published-Release Test

Long-running branches accumulate tactical decisions — renames,
refactors, attempts-then-reverts. When deciding what counts as
branch-internal, use trunk or the parent branch as the baseline — not
intermediate states inside the current branch. Ask:

> Did users of the most recently published release ever experience
> this old name, old behavior, or bug?

If the answer is **no**, it is branch-internal narrative. Move it to
the commit message and describe only the final state in the artifact.

**Keep in shipped artifacts:**

- Deprecations and migration guides for symbols that actually shipped.
- `### Fixes` entries for bugs that affected users of a published
  release.
- Comments explaining *why the current code looks this way*
  (invariants, platform quirks) that make sense to a reader who never
  saw the previous version.

### Cleanup in Hindsight

When applying these rules retroactively from inside a feature branch,
first establish scope by diffing against the parent branch (or trunk)
to identify which commits this branch actually introduced. Then:

- **In-branch commits:** Prompt the user with two options: `fixup!`
  commits with `git rebase --autosquash` to address each causal commit
  at its source, or a single cleanup commit at branch tip.
- **Trunk/Parent commits:** Default to leaving them alone. Act only on
  explicit user instruction. If the user opts in, fold the cleanup
  into a single commit at branch tip; do not rewrite shared history.
- **Scope guard:** If cleaning prior slop would touch a colleague's
  work or expand the branch beyond its stated goal, stay in lane:
  protect the current goal and leave prior slop alone.
