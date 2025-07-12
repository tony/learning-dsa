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
uv run pytest src/algorithms/001_linear_search.py

# Lint and format code
uv run ruff check .
uv run ruff format .

# Type checking
uv run mypy .

# Run doctests for a specific file
python -m doctest -v src/algorithms/001_linear_search.py
```

## Code Architecture

This is an educational project for learning data structures and algorithms, organized as numbered lessons with a consistent structure:

### Project Structure
- `src/algorithms/`: Algorithm implementations (001-019 + bst subfolder)
- `src/data_structures/`: Data structure implementations (001-010)
- Each lesson is a self-contained module that can be run with `python filename.py`

### Lesson Pattern
Each lesson follows the template in `notes/lesson_template.py` with:
1. Comprehensive module docstring explaining the concept
2. Context narrative tied to a "Data Analytics Pipeline" scenario
3. Implementation with strict type hints (mypy strict compliant)
4. Complexity analysis (Big-O notation)
5. Doctests for inline testing
6. Main function with timeit performance measurements

### Key Development Practices
- All code must pass `mypy --strict`
- Use numpy docstring convention
- Include doctests in all implementations
- Follow the numbered progression outlined in `notes/progression-*.md` files
- Each module should be runnable standalone with meaningful output

### Testing Strategy
- Doctests are the primary testing method (automatically run by pytest)
- Tests should demonstrate usage and edge cases
- Performance timing in main() functions helps understand complexity