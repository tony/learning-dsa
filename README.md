# Learning DSA

Numbered, doctested Python lessons that teach data structures and algorithms
through two running stories — one for data structures, one for algorithms.

## What is this?

Learning DSA teaches computer science fundamentals through:
- **Numbered lessons** that build on each other
- **Two running narratives** — a data pipeline and a logistics platform —
  that give each lesson a concrete scenario
- **Type-hinted, doctested Python** — every example in this repo is a test
- **Complexity analysis** — every lesson states Best/Average/Worst/Space in
  Big-O terms

## Getting Started

### Prerequisites
- Python 3.14 or higher
- [uv](https://docs.astral.sh/uv/)

### Installation

Clone the repository and enter it:

```console
$ git clone https://github.com/tony/learning-dsa.git && cd learning-dsa
```

Install dependencies:

```console
$ uv sync --all-extras --dev
```

### Running a Lesson

Each lesson is self-contained and can be run directly:

```console
$ uv run python src/algorithms/002_linear_search.py
```

Every lesson only imports the standard library, so a plain interpreter works
too, provided it satisfies the Python version above:

```console
$ python src/algorithms/002_linear_search.py
```

## Project Structure

```
learning-dsa/
├── src/
│   ├── algorithms/       # Algorithm implementations (searching, sorting, etc.)
│   │   └── bst/         # Binary Search Tree algorithms
│   └── data_structures/ # Data structure implementations (arrays, stacks, trees, etc.)
└── notes/              # Learning progressions and templates
```

## Learning Paths

Follow these progressions for a structured learning experience:

1. **Data Structures Journey** (`notes/progression-ds.md`)
   - Start with arrays and lists
   - Progress through stacks and queues
   - Master hash tables and trees
   - 45 chapters from basics to advanced

2. **Algorithms Adventure** (`notes/progression-algo.md`)
   - Begin with linear and binary search
   - Learn fundamental sorting algorithms
   - Explore advanced techniques
   - 205+ chapters covering everything from O(n²) to O(log n)

## Development

See [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md) for the full gate
list. The short version:

### Running Tests

Run the full suite:

```console
$ uv run pytest
```

Re-run automatically on save:

```console
$ uv run pytest-watcher
```

Test a specific file:

```console
$ uv run pytest src/algorithms/002_linear_search.py
```

### Code Quality

Type-check:

```console
$ uv run mypy .
```

Lint:

```console
$ uv run ruff check .
```

Auto-format:

```console
$ uv run ruff format .
```

## The Narratives

This project uses two storytelling frameworks to make learning memorable:

### Data Analytics Pipeline
Used for data structures - follows a company building a data analytics system:
- Raw data storage → Arrays and Lists
- Task processing → Stacks and Queues
- Efficient lookups → Hash Tables and Trees
- Advanced indexing → Specialized structures

### SRAS (Smart Routing and Analytics System)
Used for algorithms - simulates a growing logistics platform:
- Basic operations → Linear and Binary Search
- Data organization → Sorting algorithms
- Route optimization → Graph algorithms
- Real-time decisions → Dynamic programming

## Contributing

This is a personal learning project. Bug reports and suggestions are
welcome. New lessons follow the `Algorithm:`/`Data Structure:`,
`Concepts:`, `Narrative:`, `Doctests:` docstring shape already used
throughout `src/`; `notes/lesson_template.py` is a starting skeleton, not a
strict template every existing lesson matches. See
[.github/CONTRIBUTING.md](.github/CONTRIBUTING.md) and
[.github/WRITING.md](.github/WRITING.md) for the full conventions.

## License

MIT License - See LICENSE file for details

## Author

Created by Tony Narlock as a journey through computer science fundamentals.
