# AGENTS.md

`learning-dsa` is a personal collection of numbered, doctested Python lessons
teaching data structures and algorithms, each narrated through one of two
running stories.

Follow the conventions already in the tree, and keep a change scoped to what
was asked for.

## What is here

| Path | What it is |
| ---- | ---------- |
| `src/algorithms/` | Numbered algorithm lessons (`001`–`019`), plus `bst/` for binary search tree variants |
| `src/data_structures/` | Numbered data structure lessons (`001`–`010`) |
| `notes/progression-ds.md`, `notes/progression-algo.md` | Planned curricula (roadmaps); not every numbered chapter is implemented yet |
| `notes/progression-algo-binary-search-trees.md` | Roadmap for `src/algorithms/bst/` |
| `notes/lesson_template.py` | Starting skeleton for a new lesson |
| `pyproject.toml` | Dependencies, ruff/mypy config, pytest's `[tool.pytest]` doctest config |

## Which policy applies

- Documentation, user-facing text, commit messages, docstrings, and source
  comments: [.github/WRITING.md](.github/WRITING.md)
- Environment, the gates, tests, and pull requests:
  [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md)

Each of those is the single home for its subject. Where a rule seems to be
stated twice, the file listed above is the one that governs.

## Change discipline

- Make the smallest coherent change that solves the verified problem; keep
  unrelated cleanup out of it.
- Reuse an existing file, helper, API, or test before adding a new one.
- Add a file only for a durable boundary — a distinct responsibility,
  independent reuse, or splitting an oversized module — not for a
  single-use helper or a one-line re-export.
- A passing gate is evidence only once it has been shown capable of
  failing. Pair a new test with a deliberate break that proves it bites.
- Keep this file lean: delete a line whose removal would not cause a
  mistake, and push path-specific rules into a nested `AGENTS.md` instead.

A lesson file's leading digits (`002_arrays.py`) make its module stem an
invalid identifier on purpose: lessons are run as scripts and collected by
pytest, never imported, so the number can encode reading order. A lesson's
`Narrative:` section ties into one of two running stories: the Data
Analytics Pipeline for `data_structures/`, SRAS (Smart Routing and
Analytics System) for `algorithms/`.

## References

- [notes/progression-ds.md](notes/progression-ds.md) — data structures
  curriculum
- [notes/progression-algo.md](notes/progression-algo.md) — algorithms
  curriculum
- [notes/recommendations.md](notes/recommendations.md),
  [notes/cpython-algorithm-study.md](notes/cpython-algorithm-study.md) —
  supporting study notes
