# Learning DSA

A friendly, story-driven approach to learning Data Structures and Algorithms in Python!

## What is this?

Learning DSA is an educational project that teaches computer science fundamentals through:
- **Numbered lessons** that build on each other
- **Engaging narratives** that make concepts memorable
- **Clean Python code** with type hints and doctests
- **Performance analysis** to understand complexity in practice

## Getting Started

### Prerequisites
- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

```bash
# Clone the repository
git clone https://github.com/tony/learning-dsa.git
cd learning-dsa

# Install dependencies with uv (recommended)
uv sync --all-extras --dev

# Or with pip
pip install -e ".[dev]"
```

### Running a Lesson

Each lesson is self-contained and can be run directly:

```bash
# Run a specific lesson
python src/algorithms/002_linear_search.py

# Or with uv
uv run python src/algorithms/002_linear_search.py
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

### Running Tests

```bash
# Run all tests
uv run pytest

# Watch mode (auto-rerun on changes)
uv run pytest-watcher

# Test a specific file
uv run pytest src/algorithms/002_linear_search.py
```

### Code Quality

```bash
# Type checking
uv run mypy .

# Linting
uv run ruff check .

# Auto-format
uv run ruff format .
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

This is a personal learning project, but suggestions and improvements are welcome! Each lesson follows the template in `notes/lesson_template.py`.

## License

MIT License - See LICENSE file for details

## Author

Created by Tony Narlock as a journey through computer science fundamentals.

---

*Happy learning! Remember: understanding complexity is the key to writing efficient code.*