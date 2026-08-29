# 30-Day Python Curriculum — Zero to Advanced

A daily plan to go from no Python to advanced, job-usable Python in 30 days. Each day is ~2–3 hours: **learn → code → one small challenge**. Do not skip the typing-on-the-keyboard part.

**Repo:** this `learnpython` repo is for learning Python from scratch. Use this file as the schedule.

---

## How to use this plan

| Rule | Why |
|------|-----|
| Code every day | Reading is not learning |
| Use one environment | Python 3.12+ (or 3.11+), VS Code or PyCharm, terminal |
| Keep a `day_XX/` folder | One script or notebook per day |
| Push to GitHub weekly | Habit + portfolio |
| Stuck > 20 minutes | Read docs, then try a smaller example |

**Install once**

```bash
python3 --version          # need 3.11+
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip
```

**Core books/sites (use all month)**

| Resource | Link |
|----------|------|
| Official tutorial | https://docs.python.org/3/tutorial/ |
| Official library reference | https://docs.python.org/3/library/index.html |
| python.org getting started | https://www.python.org/about/gettingstarted/ |
| Real Python | https://realpython.com/ |
| Python bytes / PEPs (later) | https://peps.python.org/ |
| Practice | https://exercism.org/tracks/python · https://leetcode.com · https://www.hackerrank.com/domains/python |
| Interactive | https://pythontutor.com/ |

**Daily rhythm (same every day)**

1. Read the listed docs (30–45 min).  
2. Type the examples yourself (45–60 min).  
3. Finish the day’s challenge without copying (45–60 min).  
4. Write 3 bullet notes: what worked, what broke, one question for tomorrow.

---

## Phase 1 — Foundations (days 1–8)

### Day 1 — Setup, REPL, first program

**Learn:** install Python, `venv`, `print`, comments, `input()`, running `python file.py`.

**Do:** a “Hello, I’m X” script that asks name and age and prints a sentence.

**Links:** [Using the interpreter](https://docs.python.org/3/tutorial/interpreter.html) · [VS Code Python](https://code.visualstudio.com/docs/languages/python)

---

### Day 2 — Types, variables, operators

**Learn:** `int`, `float`, `bool`, `str`, `None`; arithmetic; comparison; `and` / `or` / `not`; f-strings.

**Do:** a unit converter (C↔F, km↔miles) with formatted output.

**Links:** [Numbers](https://docs.python.org/3/tutorial/introduction.html#numbers) · [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

---

### Day 3 — Strings in depth

**Learn:** indexing, slicing, `split`/`join`, `strip`, `replace`, `in`, methods vs functions.

**Do:** palindrome checker + word-count for a paragraph.

**Links:** [Text sequence type](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

---

### Day 4 — Conditionals and user flow

**Learn:** `if` / `elif` / `else`; nested conditions; truthiness; early `return`.

**Do:** a number-guessing game (1–100) with high/low hints.

**Links:** [Control flow](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

---

### Day 5 — Loops

**Learn:** `for`, `while`, `range`, `break`, `continue`, `else` on loops; nested loops (lightly).

**Do:** print a multiplication table; FizzBuzz 1–100.

**Links:** [for statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

---

### Day 6 — Lists and tuples

**Learn:** mutate vs immutable; slicing; `append`/`extend`/`pop`; unpacking; `list` vs `tuple` when to use which.

**Do:** a to-do list CLI (add, list, remove by index).

**Links:** [Lists](https://docs.python.org/3/tutorial/introduction.html#lists) · [Data structures](https://docs.python.org/3/tutorial/datastructures.html)

---

### Day 7 — Dictionaries and sets

**Learn:** keys, `.get`, `.items()`, nested dicts; set operations (`|`, `&`, `-`); uniqueness.

**Do:** a contact book (name → phone) saved only in memory for now.

**Links:** [Mappings](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) · [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

---

### Day 8 — Functions

**Learn:** `def`, parameters, defaults, `*args` / `**kwargs`, `return`, scope, docstring.

**Do:** refactor days 2–7 into functions; add a `main()`.

**Links:** [Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

**Week 1 checkpoint:** you can write scripts with loops, collections, and functions without looking up syntax every line.

---

## Phase 2 — Intermediate (days 9–16)

### Day 9 — Files and paths

**Learn:** `open` + `with`, text vs binary, `pathlib.Path`, CSV read/write.

**Do:** persist the contact book to `contacts.csv`.

**Links:** [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) · [pathlib](https://docs.python.org/3/library/pathlib.html) · [csv](https://docs.python.org/3/library/csv.html)

---

### Day 10 — Errors and debugging

**Learn:** `try` / `except` / `else` / `finally`; raise; built-in exceptions; `pdb` or VS Code debugger.

**Do:** make the contact book never crash on bad input; log errors to `app.log`.

**Links:** [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html) · [logging](https://docs.python.org/3/library/logging.html) · [pdb](https://docs.python.org/3/library/pdb.html)

---

### Day 11 — Modules, packages, pip

**Learn:** `import`, `from x import y`, `__name__ == "__main__"`, stdlib vs PyPI, `requirements.txt`.

**Do:** split the contact book into `app.py`, `storage.py`, `models.py`.

**Links:** [Modules](https://docs.python.org/3/tutorial/modules.html) · [Installing packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)

---

### Day 12 — Comprehensions and iteration tools

**Learn:** list/dict/set comprehensions; generator expressions; `enumerate`, `zip`, `sorted(key=...)`.

**Do:** given a list of dicts (users), produce filtered/sorted reports in one-liners + readable functions.

**Links:** [List comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) · [itertools](https://docs.python.org/3/library/itertools.html)

---

### Day 13 — Object-oriented basics

**Learn:** `class`, `__init__`, instance vs class attributes, methods, `self`.

**Do:** `User` / `Contact` classes with `__str__`.

**Links:** [Classes](https://docs.python.org/3/tutorial/classes.html)

---

### Day 14 — OOP next: inheritance and dunders

**Learn:** inheritance, `super()`, `@property`, `__repr__`, `__eq__`, composition over deep hierarchies.

**Do:** `TextContact` vs `EmailContact` sharing a base; equality by unique id.

**Links:** [A first look at classes](https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes) · [Data model](https://docs.python.org/3/reference/datamodel.html#special-method-names)

---

### Day 15 — Virtual environments and project layout

**Learn:** `src/` layout, `pyproject.toml` (hatchling or setuptools), pinning deps.

**Do:** turn contact book into an installable package: `pip install -e .`

**Links:** [PyPA packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/) · [src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)

---

### Day 16 — Testing with pytest (intro)

**Learn:** `assert`, `test_*.py`, fixtures (light), parametrize (one example).

**Do:** tests for validators and CSV storage (happy path + one error).

**Links:** [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html) · this repo: `pytest-patterns-curriculum.md` if present · [qaskills pytest-patterns](https://qaskills.sh/skills/thetestingacademy/pytest-patterns)

**Week 2 checkpoint:** a small package with files, classes, tests, and a venv.

---

## Phase 3 — Advanced language (days 17–23)

### Day 17 — Type hints

**Learn:** `list[int]`, `dict[str, int]`, `Optional`, `TypedDict` or `@dataclass`; `mypy` or `pyright`.

**Do:** annotate the contact book; run `mypy src` (or Pyright in the IDE).

**Links:** [typing](https://docs.python.org/3/library/typing.html) · [mypy](https://mypy.readthedocs.io/) · [PEP 484](https://peps.python.org/pep-0484/)

---

### Day 18 — Dataclasses, enums, protocols

**Learn:** `@dataclass`, `Enum`, `Protocol` (structural typing).

**Do:** replace ad-hoc dicts with dataclasses; status enum (`ACTIVE`, `ARCHIVED`).

**Links:** [dataclasses](https://docs.python.org/3/library/dataclasses.html) · [enum](https://docs.python.org/3/library/enum.html) · [typing.Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

---

### Day 19 — Decorators and closures

**Learn:** functions as objects, wrappers, `@functools.wraps`, simple decorator with args.

**Do:** `@timed` decorator that prints runtime; `@retry(n=3)` for a flaky function.

**Links:** [Primer on decorators (Real Python)](https://realpython.com/primer-on-python-decorators/) · [functools](https://docs.python.org/3/library/functools.html)

---

### Day 20 — Iterators, generators, context managers

**Learn:** `__iter__` / `__next__`; `yield`; `yield from`; `@contextmanager` / `__enter__` / `__exit__`.

**Do:** generator that streams lines from a large fake log; a context manager that times a block.

**Links:** [Iterators](https://docs.python.org/3/tutorial/classes.html#iterators) · [Generators](https://docs.python.org/3/tutorial/classes.html#generators) · [contextlib](https://docs.python.org/3/library/contextlib.html)

---

### Day 21 — Comprehension of stdlib power tools

**Learn:** `collections` (`Counter`, `defaultdict`, `deque`, `namedtuple`); `json`; `datetime` (aware vs naive).

**Do:** parse a JSON API dump (file) and report top-N keys with `Counter`.

**Links:** [collections](https://docs.python.org/3/library/collections.html) · [json](https://docs.python.org/3/library/json.html) · [datetime](https://docs.python.org/3/library/datetime.html)

---

### Day 22 — Concurrency basics

**Learn:** when to use threads vs processes vs async; GIL intuition; `concurrent.futures`.

**Do:** download (or fake-download) 20 URLs with `ThreadPoolExecutor` vs sequential; print timings.

**Links:** [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) · [asyncio intro](https://docs.python.org/3/library/asyncio.html)

---

### Day 23 — asyncio (practical)

**Learn:** `async def`, `await`, `asyncio.gather`, `aiohttp` or `httpx.AsyncClient`.

**Do:** async fetch of several public JSON endpoints; merge results.

**Links:** [asyncio](https://docs.python.org/3/library/asyncio-task.html) · [httpx](https://www.python-httpx.org/) · Practice APIs: [jsonplaceholder](https://jsonplaceholder.typicode.com/) · [httpbin](https://httpbin.org/)

**Week 3 checkpoint:** you can type-hint, decorate, stream data, and run concurrent I/O.

---

## Phase 4 — Applied advanced (days 24–30)

### Day 24 — HTTP APIs (sync)

**Learn:** REST verbs, status codes, headers, `httpx` or `requests`, env vars for secrets (never commit keys).

**Do:** CLI that GETs posts and POSTs a fake item to JSONPlaceholder.

**Links:** [httpx quickstart](https://www.python-httpx.org/quickstart/) · [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)

---

### Day 25 — Build a small web API

**Learn:** FastAPI routes, Pydantic models, uvicorn.

**Do:** CRUD in memory for contacts (`GET`/`POST`/`DELETE`).

**Links:** [FastAPI](https://fastapi.tiangolo.com/tutorial/) · [Pydantic](https://docs.pydantic.dev/)

---

### Day 26 — Data crunching (pandas + matplotlib)

**Learn:** `DataFrame`, filter, groupby, simple plot saved as PNG.

**Do:** load a CSV (contacts or [sample datasets](https://github.com/mwaskom/seaborn-data)); chart counts by category.

**Links:** [pandas getting started](https://pandas.pydata.org/docs/getting_started/index.html) · [matplotlib](https://matplotlib.org/stable/tutorials/pyplot.html)

---

### Day 27 — Quality: lint, format, more tests

**Learn:** `ruff` (lint+format), pytest coverage, parametrize more cases.

**Do:** `ruff check` + `ruff format`; coverage ≥ 80% on your package.

**Links:** [Ruff](https://docs.astral.sh/ruff/) · [pytest](https://docs.pytest.org/en/stable/) · [coverage](https://coverage.readthedocs.io/)

---

### Day 28 — Git, GitHub, CI

**Learn:** commits, `.gitignore`, GitHub Actions running `ruff` + `pytest` on push.

**Do:** public repo + green CI badge.

**Links:** [Pro Git](https://git-scm.com/book/en/v2) · [GitHub Actions](https://docs.github.com/en/actions) · [Python CI example](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

---

### Day 29 — Capstone day 1 (design + core)

**Pick one project (stay with it through day 30):**

1. **CLI toolkit** — argparse/typer: file stats, JSON pretty-print, grep-like search.  
2. **Expense tracker** — CSV/SQLite, categories, monthly report.  
3. **API wrapper** — wrap a public API + cache + tests.  
4. **Mini FastAPI app** — expand day 25 with SQLite (`sqlite3` or SQLModel).

**Do today:** README, data model, first working vertical slice + tests.

**Links:** [argparse](https://docs.python.org/3/library/argparse.html) · [Typer](https://typer.tiangolo.com/) · [sqlite3](https://docs.python.org/3/library/sqlite3.html)

---

### Day 30 — Capstone day 2 (polish + demo)

**Do:** error handling, type hints, CI, sample data, 2-minute demo script in README.

**Ship:** tag `v0.1.0` and write what you would learn next (Django, pytest mastery, data science, automation).

**Advanced next tracks (after day 30)**

| Track | Start here |
|-------|------------|
| Testing | [pytest docs](https://docs.pytest.org/) · [pytest-patterns skill](https://qaskills.sh/skills/thetestingacademy/pytest-patterns) |
| Web | FastAPI in depth · [Django tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) |
| Data | pandas → [scikit-learn](https://scikit-learn.org/stable/getting_started.html) |
| Automation | [Playwright Python](https://playwright.dev/python/) |
| Internals | [CPython internals (realpython)](https://realpython.com/products/cpython-internals-book/) · [Fluent Python](https://www.fluentpython.com/) (book) |

---

## 30-day map (one screen)

| Days | Theme |
|------|--------|
| 1–8 | Syntax, types, control flow, collections, functions |
| 9–16 | Files, errors, packages, OOP, pytest intro |
| 17–23 | Types, dataclasses, decorators, generators, concurrency, asyncio |
| 24–30 | HTTP, FastAPI, pandas, quality/CI, capstone |

---

## Stretch challenges (optional)

- **Day 7+:** 3 Exercism Python exercises per week.  
- **Day 16+:** one LeetCode Easy in Python (arrays/strings) three times a week.  
- **Day 23+:** read [PEP 8](https://peps.python.org/pep-0008/) once end-to-end.

---

## Suggested folder layout in this repo

```
learnpython/
  python-30-day-curriculum.md
  day_01_hello/
  day_02_types/
  ...
  capstone/
```

Keep secrets out of git. Use `.env` locally and list `.env` in `.gitignore`.
