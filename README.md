# learnpython

Python from scratch, aimed at **Java developers**. You already know types, OOP, and tooling. Translate, do not restart.

## Learn it quickly (7 focused days)

Do not watch a 20-hour course first. Run code, map it to Java, then build one small thing.

| Day | Goal | Do this |
|---|---|---|
| **1** | Syntax + types | Read [`docs/java-to-python.md`](docs/java-to-python.md). Run `python lessons/syntax.py` and `python lessons/collections_tour.py`. |
| **2** | OOP without ceremony | Run `python lessons/oop.py`. Implement `exercises/03_bank.py` (peek at `exercises/solutions/` only after you try). |
| **3** | Stdlib + tests | Run `python lessons/stdlib_tour.py`. `pip install pytest` then `pytest -q`. Add a test. |
| **4** | Packaging | Create a `src/` package, `pyproject.toml`, import your own module. Google "Python pyproject.toml hatchling". |
| **5** | HTTP or CLI | Pick **one**: `httpx` + a JSON API client, or `argparse` CLI. Java analog: a tiny Spring `RestClient` or `picocli`. |
| **6** | Real Python web | Flask or FastAPI (FastAPI will feel closer to annotated Spring). One CRUD resource. |
| **7** | Port something you know | Take a Java kata or a 50-line Spring service you have written and port it. That cements the mapping. |

Daily budget: **60–90 minutes of typing**, not passive video.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install -U pip pytest
python lessons/syntax.py
pytest -q
```

Need Python 3.10+ (`match`, `int | None` syntax).

## Java reflexes → Python files

| If you want… | Open |
|---|---|
| Side-by-side mental model | [`docs/java-to-python.md`](docs/java-to-python.md) |
| Runnable mappings | [`lessons/`](lessons/) |
| Practice (blank) | [`exercises/`](exercises/) |
| Practice (answers) | [`exercises/solutions/`](exercises/solutions/) |

## What actually makes Java people fast

1. **Keep type hints.** You will hate untyped Python. Use them from day one.
2. **Prefer functions + dataclasses** over class hierarchies.
3. **Read the stdlib** (`pathlib`, `json`, `dataclasses`, `collections`) before adding libraries.
4. **pytest, not JUnit XML in your head.** `assert` is the API.
5. **Build one real script** (file rename, API scrape, log parse) in week one. Tutorials without a personal project do not stick.

## After the first week

- Official tutorial (skim, do not study): https://docs.python.org/3/tutorial/
- Type system: https://docs.python.org/3/library/typing.html
- FastAPI (if you are a Spring person): https://fastapi.tiangolo.com/
- Book when you want depth: *Fluent Python* (Ramalho) — after you can write scripts, not before.
