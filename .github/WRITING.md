# Writing

How this project writes prose, for humans and agents alike. It governs
`README.md`, commit messages, docstrings, and source comments — every surface
a reader reaches. There is no `CHANGES` file and nothing here is published, so
this repository has no changelog or release-notes conventions.

For environment setup, the gates, and the pull request workflow, see
[CONTRIBUTING.md](CONTRIBUTING.md).

## Voice

Three surfaces, one voice. A docstring says what a caller may rely on; prose
says what happens; a commit message says why. All are present tense, lead
with the thing being described, and stop. Why it was built that way belongs
in the commit message, which is timestamped and attached to the diff.

The most useful editing operation is deleting the introductory sentence.

Lead with verbs and name concrete things. Put identifiers in backticks.
Prefer short declarative sentences, one operational fact each. This project
teaches data structures and algorithms, not Python syntax: do not explain
what a `for` loop does, do explain why this structure or algorithm behaves
the way it does.

Type annotations describe shape. Documentation describes meaning. A sentence
that restates a signature has said nothing.

| Instead of                       | Prefer                            |
| --------------------------------- | ---------------------------------- |
| "We added…"                       | "`Stack.pop` now raises…"          |
| "New and improved"                | "`binary_search` now…"             |
| "powerful", "seamless"            | state the capability               |
| "easily", "simply", "just"        | omit                               |
| "simple", "obvious", "intuitive"  | omit                               |
| "robust"                          | name the failure that is handled   |
| "comprehensive"                   | name what is covered               |
| "optimized", "blazingly fast"     | give the magnitude                 |
| "various fixes"                   | name the components                |
| "under the hood"                  | omit unless observable             |
| "please note that", "note that"   | state the fact                     |
| "leverage", "utilize"             | "use"                              |
| "delve into"                      | "read", or omit                    |
| "best practices"                  | name the practice                  |
| "in order to"                     | "to"                               |

## README

A README is the shortest path from "what is this?" to competent use, not the
project's autobiography.

The first sentence is a contract. It says what the reader has been handed,
concretely enough to tell this project apart from a generic DSA repository.

Get to a runnable command before anything the reader can skip. State the
minimum Python version in prose, not only in a bullet — `requires-python` in
`pyproject.toml` is the authority; the README must agree with it.

Examples are executable, not illustrative fiction, wherever the test suite
can see them. This repository's `testpaths` is `src` only (see
[Documented examples that run](#documented-examples-that-run)): a `>>> `
block placed in `README.md` would not be collected. Keep README examples as
plain shell (`console`) blocks and put any doctested Python example in a
lesson file under `src/`, where it actually runs.

Headings stay conventional and stable, because people deep-link them.

## Documented examples that run

Examples in this project are tests. This section is the contract for writing
one the suite can actually see.

**A fence tag is cosmetic. Only a `>>> ` prompt executes.** A block written
as

    ```python
    stack = Stack()
    ```

is prose that looks like a test. Nothing collects it, nothing runs it, and it
can be wrong for years. The same block written with prompts is a test:

    ```python
    >>> stack = Stack()
    ```

This is the single most expensive mistake available when editing a lesson,
because removing the prompts leaves a green test suite and a silently deleted
test. When editing a file that contains examples, count the prompts before
and after.

**The fence tag is `python`.** Not `pycon`, not bare.

**Where examples run, in this repository.** `pyproject.toml` configures
pytest through `[tool.pytest]` — pytest's native TOML table (pytest ≥ 9), not
the older `[tool.pytest.ini_options]` string format. `addopts` includes
`--doctest-modules`, and `testpaths = ["src"]`. That means every docstring
under `src/` is collected and executed by a plain `pytest` run; `README.md`
and `notes/` are not in `testpaths`, so a `>>> ` block placed there, however
correctly written, does not run. There is no `conftest.py` in this
repository, so pytest injects no `doctest_namespace` — a doctest gets no free
names. Every block imports or defines everything it uses.

**All functions and methods carry a working doctest.** Doctests are this
project's primary test suite, not an add-on. If a function resists a working
doctest, that is a signal to simplify the function, not to skip the test.

**`# doctest: +SKIP` is not permitted.** It is a workaround that tests
nothing.

**Do not downgrade a doctest to a non-executed block to make it pass.** A
`.. code-block::` or an unprompted fence does not run. If an example cannot
pass, fix the example or fix the code.

**Option flags.** `ELLIPSIS` and `NORMALIZE_WHITESPACE` are enabled globally
(`doctest_optionflags` in `pyproject.toml`), so `...` elides variable output
and whitespace differences do not fail a comparison. Reach for an inline
`# doctest: +FLAG` only for the block that needs it.

**Docstring examples** use the NumPy `Examples` section:

    Examples
    --------
    >>> data = list(range(10))
    >>> binary_search(data, 5)
    True
    >>> binary_search(data, 10)
    False

## Docstrings

The prime directive: never restate the type. The annotation is the source of
truth; the docstring carries what the annotation cannot.

This repository uses the NumPy docstring convention, enforced by ruff's
`pydocstyle` (`convention = "numpy"` in `pyproject.toml`) rather than
relitigated in review.

Document the dimensions the type system cannot encode:

- **Complexity.** Time and space, in Big-O terms — the reason a lesson
  exists.
- **Mutation.** What it changes in place.
- **Ordering.** Whether results come back in a guaranteed order.
- **Failure.** Which exceptions are raised and what triggers each.
- **Boundary behaviour.** What zero, empty, and the maximum do.
- **Units and ranges.** What a number means and what values are accepted.

The ambiguity worth resolving by example: whether "retry three times" means
three attempts or four. State it.

The first sentence stands alone; tooling truncates there. PEP 257 applies:
triple double quotes, an imperative one-line summary ending in a period, a
blank line before any extended description.

### Lesson docstrings

Every lesson module's docstring opens `N. Title.`, then names the subject
with `Algorithm:` or `Data Structure:`, then:

- **Concepts** — what it is and how it behaves, with Best/Average/Worst/Space
  complexity where the subject has one.
- **Narrative** — one paragraph connecting the concept to whichever running
  story fits: the Data Analytics Pipeline for data structures, SRAS (Smart
  Routing and Analytics System) for algorithms. This is the one place first
  person plural ("we") is the house voice — the Concepts prose and the rest
  of this file stay third person and present tense.
- **Doctests** — one line naming what the doctests below cover.

A function or method implementing an algorithm carries a `Complexity` block
(Best/Average/Worst/Space) directly above its `Examples` section. A
demonstration function that has no complexity of its own may fold that note
into its summary line instead.

**Classes with fields** — `NamedTuple`, dataclasses — document every field in
an `Attributes` section:

```python
class SearchResult(NamedTuple):
    """Outcome of one search over a structure.

    Attributes
    ----------
    index : int | None
        Position the value was found at, or ``None`` when absent.
    comparisons : int
        Comparisons performed, the figure the lesson measures.
    """
```

A type says how a field is shaped, not what it holds. Describing each one
keeps that meaning next to the code, and anything that renders the class —
autodoc, a REPL, an editor tooltip — has a description to show instead of a
bare name.

## Source comments

A comment ships only if it passes all three gates. Fail any: delete or
rewrite. Borderline: delete — borderline means the information is
reconstructible, which is what makes deletion cheap.

**Loss.** Three years from now, would losing this cost a maintainer real time
rediscovering intent, an invariant, a constraint, or a failure mode the code
and tests do not already make obvious?

**Elite.** Would SQLite, Redis, the Go standard library, or CPython write
this comment, at this length? Those projects state the constraint and stop.
They do not argue with an imagined objector.

**Upkeep.** Will it stay true without maintenance? A comment that hand-syncs
a value the code owns — a count, an offset, a line reference, a duplicated
constant — is false the first time that value moves.

### Ceiling

One or two lines. A comment reaching four is either carrying several facts,
in which case split it, or arguing, in which case cut it to the fact.

Rationale, alternatives weighed, and the story of how the code got here
belong in the commit message: timestamped, attached to the exact diff, and
free to maintain.

### Keep

- Why over how: upstream quirks, compatibility constraints, and performance
  tradeoffs still part of the contract.
- Invariants, preconditions, ordering, and boundary requirements that types
  and tests cannot express.
- Code that looks wrong but is not, so a later cleanup does not reintroduce
  the bug.
- A high-level sketch of an algorithm whose local operations do not reveal
  the whole.

### Delete

- Narration of the next lines; code translated into English.
- Restated names, types, defaults, or control flow.
- Values duplicated from the code and hand-synced.
- Justification, hedging, or apology for a choice.
- History version control already holds, including commented-out code.
- Transient observations — "currently", "for now", "the latest release" —
  that go stale with no nearby edit.

### The upkeep gate in practice

It reaches values that track our own code. It does not reach frozen external
facts.

Bad (Delete):

```python
# There are 42 doctests to write for this chapter.
```

Good (Keep):

```python
# CPython < 3.11 has no ExceptionGroup, so this branch stays.
```

### Documentation exception

Doctests, minimal usage examples, and NumPy `Parameters`, `Returns`, and
`Attributes` entries on public API are exempt from the loss gate — they serve
the caller, not the maintainer, and a doctest that runs is also a test. They
are exempt from nothing else. Ceiling: a good man page entry.

## Markdown

Prose wraps at 80 columns. Table rows and long links are exempt, because
breaking them harms rendering.

Do not use a local absolute path or an email address in anything published.

## Code blocks

Code blocks are paste-and-run units: pasting one block runs exactly one
intended action. Doctests and other executed examples are exempt — the test
suite runs them, nobody pastes them.

- **One command per block.** Multiple steps may share a block only when
  explicitly chained with `&&`, `;`, or `\` continuations — the chain is
  then one logical command.
- **Explanations go in prose above the block**, never as `#` comments inside
  it.
- **Command menus are per-command blocks with prose lead-ins**, not tables.
- **Shell commands use the `console` tag with a `$ ` prefix.** This
  separates interactive commands from scripts and enables prompt-aware copy.
- **Split long commands with `\`** — one flag or flag+value pair per
  indented continuation line, positional arguments last.

Good — show the last ten commits as a graph:

```console
$ git log \
    --max-count=10 \
    --graph \
    --oneline
```

Bad:

```console
# Show the last ten commits as a graph
$ git log --max-count=10 --graph --oneline
```

## Commits

```
Scope(type[detail]): concise description

why: Explanation of necessity or impact.

what:
- Specific technical changes made
- Focused on a single topic
```

Keep the subject to 50 characters or fewer, excluding any trailing `(#NN)`
pull request reference, and wrap body lines at 72. Separate the `why:` and
`what:` blocks with a blank line.

Mark a change that breaks an existing lesson's public behaviour with a
`BREAKING:` line in the body.

Routine maintenance commits drop the colon and take a capitalised
description, which is what distinguishes them at a glance in
`git log --oneline`:

```
py(deps[dev]) Bump dev packages
ai(rules[AGENTS]) Judge comments by three gates
```

Everything that changes behaviour keeps the colon.

Common types:

- **feat**: New features or enhancements
- **fix**: Bug fixes
- **refactor**: Code restructuring without functional change
- **docs**: Documentation updates
- **chore**: Maintenance (dependencies, tooling, config)
- **test**: Test-related updates
- **style**: Code style and formatting
- **py(deps)**: Dependencies
- **py(deps[dev])**: Dev dependencies
- **ai(rules[AGENTS])**: AI rule updates

Example:

```
Stack(feat[pop]): Raise on pop from empty stack

why: Silent None returns hid a bug in the LIFO demo.

what:
- Raise IndexError on pop from an empty Stack
- Add a doctest covering the empty case
```

For a multi-line message, use a heredoc so the formatting survives:

```console
$ git commit -m "$(cat <<'EOF'
Scope(feat[detail]): Concise description

why: Explanation of the change.

what:
- First change
- Second change
EOF
)"
```

## Slop prevention

Treat AI slop as review-hostile noise, not as proof that text or code is
wrong. The goal is to maximise information density.

- **AI signatures.** No "Generated by", no conversational filler, no
  unexplained emoji, no tool metadata.
- **Brittle references.** No hard-coded line numbers, fragile file or test
  counts, dated "as of" claims, bare SHAs, or local absolute paths — unless
  they are strict evidentiary artefacts such as a benchmark log.
- **Diff narration.** Do not restate what moved, was renamed, or was removed
  in anything the reader holds alongside the diff: code, docstrings, or
  README. The diff and the commit message already carry it.
- **Low-value scaffolding.** No ownerless TODOs, unused future-proofing,
  debug artefacts, or defensive wrappers around failure modes nothing can
  reach.
- **Prose inflation.** The diction table under [Voice](#voice) governs;
  replace an inflated word with a concrete description of behaviour,
  constraints, or trade-offs.
- **Coded labels.** Write rules and findings as plain imperatives. No `[R1]`,
  `Option B`, or any index a reader has to decode.

Preserve the "why". Never delete a comment documenting an invariant, a
platform quirk, or an upstream workaround — those are the facts
[Source comments](#source-comments) keeps, and every other comment is judged
by it.

### Durable source links

Link to a pinned revision, never to trunk. A pinned permalink is not a
brittle reference; an unlinked SHA dropped into prose is. `blob/main/…` links
rot silently — the file moves, lines shift, and the anchor lands on
unrelated code while still resolving.

- Prefer a release tag. Most durable, and it tells the reader which released
  version the claim held for.
- Otherwise use a 7-character commit ref reachable from trunk — never a
  pull-request-head SHA, which can be rebased or garbage-collected.
- Reserve `blob/main/…` for a living document meant to always show the
  latest state, such as this one.
- Line anchors (`#L120-L145`) are only safe on a pinned ref.

### The published-release test

This project has no published release, so there is no user who experienced a
prior public state — treat anything on `main` as fair game to describe
plainly, with no branch-internal narrative ("no longer", "used to") to
preserve. If that ever changes, the test becomes: did someone using a
published version experience the old name or behaviour? If no, it belongs in
the commit message, not in shipped prose.

Evidence is immune to this: preserve exact counts, dates, and doctest output
that serve as literal evidence, such as a benchmark log or an expected
doctest result.
