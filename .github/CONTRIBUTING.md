# Contributing

Thanks for looking. This is a personal learning project. The most useful
contribution right now is a bug report with a reproduction, or a note on
where a lesson's narrative, complexity claim, or doctest misled you.

How this project writes prose — README, commit messages, docstrings, and
source comments — is set out separately in [WRITING.md](WRITING.md). Read
that before changing any of it. The constraints every change is held to, and
the map of what is where, are in [AGENTS.md](../AGENTS.md).

## Getting set up

```console
$ uv sync --all-extras --dev
```

## The gates

Format:

```console
$ uv run ruff format .
```

Lint:

```console
$ uv run ruff check .
```

Type-check:

```console
$ uv run mypy .
```

Test:

```console
$ uv run pytest
```

Documentation is a gate, not a courtesy. Every docstring under `src/` is
executed by `pytest` — the doctest flags live in `[tool.pytest]` in
`pyproject.toml`, so there is no separate doctest step and a green `pytest`
is the proof. Which blocks qualify, and the one mistake that silently
removes a test, are in
[WRITING.md](WRITING.md#documented-examples-that-run).

Before claiming a test or a gate works, show it failing. A gate that has
never been red is an assumption.

## Tests

Doctests are the suite; there are no `test_*.py` files and no `conftest.py`.
`pytest`'s `addopts` already set `--tb=short --no-header --showlocals`, so a
failing doctest prints its local variables without an extra flag.

A lesson needs no external service or fixture — every doctest is
self-contained stdlib. `pytest-rerunfailures` is installed for rerunning a
timing-sensitive doctest with `--reruns`, but no gate enables it by default;
prefer `# doctest: +ELLIPSIS` on the flaky line over reaching for reruns.

Run one lesson's tests:

```console
$ uv run pytest src/algorithms/002_linear_search.py
```

Run one file's doctests verbosely, without going through pytest:

```console
$ python -m doctest -v src/algorithms/002_linear_search.py
```

Re-run automatically on save:

```console
$ uv run pytest-watcher
```

## Pull requests

One subject per pull request. Unrelated cleanup found along the way belongs
in its own commit, and usually in its own pull request.

Discuss a substantial change via an issue before making it.

Commit format is in [WRITING.md](WRITING.md#commits).

## Decorum

- Participants will be tolerant of opposing views.
- Participants must ensure that their language and actions are free of
  personal attacks and disparaging personal remarks.
- When interpreting the words and actions of others, participants should
  always assume good intentions.
- Behaviour which can be reasonably considered harassment will not be
  tolerated.

Based on [Ruby's Community Conduct Guideline](https://www.ruby-lang.org/en/conduct/).

## Security

There is no `SECURITY.md`. Report a vulnerability through GitHub's private
security advisories for this repository, not as a public issue.
