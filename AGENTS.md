# CLAUDE.md

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

## Git Commit Standards

### Commit Message Format
```
Component/File(commit-type[Subcomponent/method]): Concise description

why: Explanation of necessity or impact.
what:
- Specific technical changes made
- Focused on a single topic
```

### Common Commit Types
- **feat**: New features or enhancements
- **fix**: Bug fixes
- **refactor**: Code restructuring without functional change
- **docs**: Documentation updates
- **chore**: Maintenance (dependencies, tooling, config)
- **test**: Test-related updates
- **style**: Code style and formatting

### Dependencies Commit Format
- Python packages: `py(deps): Package update`
- Python dev packages: `py(deps[dev]): Dev package update`

### Examples

#### Feature Addition
```
core/schema(feat[Query]): Add fruit filtering by color

why: Users need to filter fruits by color in GraphQL queries
what:
- Add color filter parameter to fruits query
- Update resolver to handle color filtering
- Add tests for color filtering
```

#### Bug Fix
```
core/types(fix[FruitType]): Correct optional color relationship

why: Color field was incorrectly marked as required
what:
- Change color field to use Optional type
- Update tests to handle None values
```

#### Dependencies Update
```
py(deps[dev]): Add django-stubs for type checking

why: Improve type safety for Django models and ORM
what:
- Add django-stubs to dev dependencies
- Configure MyPy to use django-stubs plugin
```

### Guidelines
- Subject line: Maximum 50 characters
- Body lines: Maximum 72 characters
- Use imperative mood ("Add", "Fix", not "Added", "Fixed")
- One topic per commit
- Separate subject from body with blank line
- Mark breaking changes: `BREAKING:`
