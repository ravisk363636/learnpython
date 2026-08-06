# Best Learning Links — Python Fundamentals

Curated **best starting links** for each topic in this repo’s learning path. Prefer official docs + one strong tutorial; use videos when you learn better by watching.

Suggested order: **install → IDE → venv → pip/poetry → types → strings → I/O → deep concepts**.

---

## 1. Python installation (Python 3.11+)

| Type | Resource | Why it’s good |
|------|----------|---------------|
| Download | [python.org downloads](https://www.python.org/downloads/) | Official installer; pick **3.11+** (or latest stable) |
| Guide | [How to Install Python — Real Python](https://realpython.com/installing-python/) | Clear Windows / macOS / Linux walkthrough |
| Docs | [Using Python on Windows](https://docs.python.org/3/using/windows.html) | PATH, `py` launcher, Windows specifics |
| Docs | [Using Python on Unix](https://docs.python.org/3/using/unix.html) | macOS / Linux notes |
| Video | [Install Python (Mac & Windows) — Corey Schafer](https://www.youtube.com/watch?v=YYXdXT2l-Gg) | Best first video: download, PATH, verify |

**Verify after install**

```bash
python --version    # or: python3 --version
python -m pip --version
```

---

## 2. Virtual environments (venv, conda)

| Type | Resource | Why it’s good |
|------|----------|---------------|
| Docs | [venv tutorial (official)](https://docs.python.org/3/tutorial/venv.html) | Short, authoritative intro |
| Docs | [`venv` module reference](https://docs.python.org/3/library/venv.html) | Create / activate details |
| Guide | [Python Virtual Environments: A Primer — Real Python](https://realpython.com/python-virtual-environments-a-primer/) | Deep dive: why + how |
| Docs | [Conda: managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) | Official conda env workflow |
| Video | [venv on Mac & Linux — Corey Schafer](https://www.youtube.com/watch?v=Kg1Yvry_Ydk) | Hands-on create / activate / deactivate |
| Video | [venv on Windows — Corey Schafer](https://www.youtube.com/watch?v=APOPm01BVrk) | Windows `Scripts\activate` |

**Quick start (`venv`)**

```bash
python -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate           # Windows
deactivate
```

---

## 3. Package management (pip, poetry)

| Type | Resource | Why it’s good |
|------|----------|---------------|
| Docs | [pip user guide](https://pip.pypa.io/en/stable/user_guide/) | Official: install, freeze, requirements |
| Docs | [Installing packages (official)](https://docs.python.org/3/installing/index.html) | How pip + venv fit together |
| Guide | [What Is pip? — Real Python](https://realpython.com/what-is-pip/) | Beginner-friendly pip overview |
| Docs | [Poetry documentation](https://python-poetry.org/docs/) | Modern projects, lockfiles, `pyproject.toml` |
| Guide | [Poetry: Dependency Management — Real Python](https://realpython.com/dependency-management-python-poetry/) | When and how to use Poetry |
| Index | [PyPI](https://pypi.org/) | Find packages to install |

**Quick start**

```bash
# pip (inside an activated venv)
python -m pip install requests
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt

# poetry
pipx install poetry
poetry init
poetry add requests
poetry install
```

---

## 4. IDEs setup (VS Code, PyCharm)

| Type | Resource | Why it’s good |
|------|----------|---------------|
| Docs | [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial) | Official: extension, interpreter, run, debug |
| Docs | [VS Code Python environments](https://code.visualstudio.com/docs/python/environments) | Select venv / conda inside VS Code |
| Video | [Getting Started with Python in VS Code — Microsoft](https://www.youtube.com/watch?v=D2cwvpJSBX4) | ~10 min official setup |
| Docs | [PyCharm: first Python project](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html) | Official first-project guide |
| Guide | [Getting Started with PyCharm — JetBrains](https://www.jetbrains.com/guide/python/tutorials/getting-started-pycharm/) | Install, interpreter, run, debug |
| Download | [VS Code](https://code.visualstudio.com/) · [PyCharm Community](https://www.jetbrains.com/pycharm/download/) | Free editors to install |

**Goal:** run `print("Hello")` from the IDE and set one breakpoint.

---

## 5. Variables, data types, type hints

| Type | Resource | Why it’s good |
|------|----------|---------------|
| Docs | [Official tutorial — Data structures](https://docs.python.org/3/tutorial/datastructures.html) | Lists, dicts, sets, tuples |
| Docs | [Built-in types](https://docs.python.org/3/library/stdtypes.html) | Numbers, strings, sequences, mappings |
| Guide | [Variables in Python — Real Python](https://realpython.com/python-variables/) | Names, assignment, dynamic typing |
| Guide | [Basic Data Types in Python — Real Python](https://realpython.com/python-data-types/) | `int`, `float`, `str`, `bool`, etc. |
| Guide | [Python Type Checking — Real Python](https://realpython.com/python-type-checking/) | Type hints + mypy overview |
| Docs | [`typing` module](https://docs.python.org/3/library/typing.html) | Official type-hint reference |
| Video | [Integers & floats — Corey Schafer](https://www.youtube.com/watch?v=khKv-8q7YmY) | Numeric types |
| Video | [Lists, tuples, sets — Corey Schafer](https://www.youtube.com/watch?v=W8KRzm-HUcc) | Collection types |
| Video | [Dictionaries — Corey Schafer](https://www.youtube.com/watch?v=daefaLgNkw0) | Key–value pairs |

**Mini example**

```python
name: str = "Ada"
age: int = 36
scores: list[int] = [90, 85, 88]

def greet(person: str) -> str:
    return f"Hello, {person}"
```

---

## 6. String manipulation and f-strings

| Type | Resource | Why it’s good |
|------|----------|---------------|
| Docs | [Strings (`str`) — official](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) | Methods: `split`, `replace`, `strip`, … |
| Docs | [f-strings (formatted string literals)](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) | Official syntax rules |
| Docs | [Input and Output tutorial § formatting](https://docs.python.org/3/tutorial/inputoutput.html) | f-strings + `.format()` in context |
| Guide | [Python String Formatting Best Practices — Real Python](https://realpython.com/python-string-formatting/) | Compare styles; prefer f-strings |
| Guide | [Strings and Character Data — Real Python](https://realpython.com/python-strings/) | Indexing, slicing, methods |
| Video | [Strings — Corey Schafer](https://www.youtube.com/watch?v=k9TUPpGqYTo) | Indexing, methods, intro f-strings |
| Video | [String formatting — Corey Schafer](https://www.youtube.com/watch?v=vTX3IwquFkc) | f-strings, numbers, dates |

**Mini example**

```python
name = "Ada"
print(f"Hello, {name}!")
print(f"Pi ≈ {3.14159:.2f}")
print(name.upper(), name[0:2], name.replace("A", "a"))
```

---

## 7. Input/output operations

| Type | Resource | Why it’s good |
|------|----------|---------------|
| Docs | [Input and Output — official tutorial](https://docs.python.org/3/tutorial/inputoutput.html) | `print`, formatting, reading/writing files |
| Docs | [`input()`](https://docs.python.org/3/library/functions.html#input) · [`print()`](https://docs.python.org/3/library/functions.html#print) | Built-in function references |
| Guide | [Reading and Writing Files — Real Python](https://realpython.com/read-write-files-python/) | `open`, `with`, text vs binary |
| Guide | [Basic Input and Output — Real Python](https://realpython.com/python-input-output/) | Console `input()` / `print()` |
| Video | [Printing, input, and variables](https://www.youtube.com/watch?v=WnCBW_Im2UU) | `print`, `input`, casting with `int()` |

**Mini example**

```python
name = input("Your name: ")
age = int(input("Your age: "))
print(f"{name} is {age} years old.")

with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Hello, file!\n")

with open("notes.txt", encoding="utf-8") as f:
    print(f.read())
```

---

## Deep Concepts

After the fundamentals above, dig into how Python really works and how to write idiomatic code.

### 8. Memory management and garbage collection

| Type | Resource | Why it’s good |
|------|----------|---------------|
| Guide | [Memory Management in Python — Real Python](https://realpython.com/python-memory-management/) | Best deep dive: reference counting, cycles, arenas |
| Docs | [`gc` module](https://docs.python.org/3/library/gc.html) | Control / inspect the cyclic garbage collector |
| Docs | [Memory management (C API)](https://docs.python.org/3/c-api/memory.html) | How CPython allocates object memory |
| Glossary | [garbage collection — Real Python](https://realpython.com/ref/glossary/garbage-collection/) | Short mental model + cycle example |
| Internal | [CPython GC internals](https://github.com/python/cpython/blob/main/InternalDocs/garbage_collector.md) | How the cycle detector works under the hood |

**Key ideas**
- CPython primarily uses **reference counting** (free when refcount hits 0).
- A **cyclic GC** cleans up reference cycles that refcounting alone cannot.
- Objects live on the **heap**; names/variables hold references.

```python
import gc
import sys

x = []
print(sys.getrefcount(x))  # how many references exist
gc.collect()               # run a collection manually
```

---

### 9. Dynamic typing vs static typing

| Type | Resource | Why it’s good |
|------|----------|---------------|
| Guide | [Python Type Checking — Real Python](https://realpython.com/python-type-checking/) | Dynamic vs static, gradual typing, mypy |
| Docs | [Type system concepts](https://typing.python.org/en/latest/spec/concepts.html) | Official: runtime types, gradual typing, `Any` |
| Docs | [`typing` module](https://docs.python.org/3/library/typing.html) | Type-hint vocabulary |
| Docs | [mypy: dynamic vs static typing](https://mypy.readthedocs.io/en/stable/getting_started.html#dynamic-vs-static-typing) | Practical static checking workflow |
| Spec | [PEP 484 — Type Hints](https://peps.python.org/pep-0484/) | Why optional static checking was added |

**Key ideas**
- Python is **dynamically typed**: types are checked at runtime; a name can point to different types over time.
- **Type hints** do not change runtime behavior; tools like **mypy** / **Pyright** do static checks.
- Prefer **gradual typing**: add hints where they help, leave the rest dynamic.

```python
# Dynamic: type can change
value = 42
value = "forty-two"

# Optional static hints (checked by mypy, not by Python at runtime)
def double(n: int) -> int:
    return n * 2
```

---

### 10. The `__name__` variable and execution context

| Type | Resource | Why it’s good |
|------|----------|---------------|
| Guide | [What Does `if __name__ == "__main__"` Do? — Real Python](https://realpython.com/if-name-main-python/) | Clearest explanation of the idiom |
| Guide | [Defining Main Functions in Python — Real Python](https://realpython.com/python-main-function/) | Structure scripts with `main()` + guard |
| Docs | [`__main__` — top-level code environment](https://docs.python.org/3/library/__main__.html) | Official module docs |
| Docs | [Modules tutorial](https://docs.python.org/3/tutorial/modules.html) | How `__name__` works when importing |
| Video | [`if __name__ == '__main__'` — Corey Schafer](https://www.youtube.com/watch?v=sugvnHA7ElY) | Clear walkthrough of script vs import |

**Key ideas**
- When you **run** a file, `__name__` is `"__main__"`.
- When you **import** it, `__name__` is the module name (e.g. `"mymodule"`).
- Put runnable/demo code under `if __name__ == "__main__":` so imports stay side-effect free.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def main() -> None:
    print(greet("Ada"))

if __name__ == "__main__":
    main()
```

---

### 11. PEP 8 and code style guidelines

| Type | Resource | Why it’s good |
|------|----------|---------------|
| Spec | [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/) | The official style guide — start here |
| Guide | [Beautiful Python With PEP 8 — Real Python](https://realpython.com/python-pep8/) | Friendly walkthrough of the important rules |
| Tool | [Ruff](https://docs.astral.sh/ruff/) | Fast linter/formatter that enforces PEP 8-style rules |
| Tool | [pycodestyle](https://pycodestyle.pycqa.org/en/latest/) | Classic PEP 8 checker |
| Docs | [Black code style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html) | Opinionated autoformatter (PEP 8–aligned) |
| Video | [Ruff linter & formatter — Corey Schafer](https://www.youtube.com/watch?v=828S-DMQog8) | Modern way to enforce PEP 8–style rules automatically |

**Key ideas (cheat sheet)**
- Indent with **4 spaces**; keep lines ~**79–88** characters when practical.
- Names: `snake_case` functions/vars, `CapWords` classes, `UPPER_CASE` constants.
- Imports at the top; one statement per line; spaces around operators.
- Use a formatter (`ruff format` / `black`) so style is automatic.

```bash
pip install ruff
ruff check .
ruff format .
```

---

## Full courses / playlists (optional binge)

Use these if you want one continuous path instead of topic-by-topic links.

| Resource | Link | Notes |
|----------|------|-------|
| Official Python tutorial | [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/) | Best free written course from the language authors |
| Corey Schafer — Beginner series | [YouTube playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7) | Excellent topic-by-topic videos |
| Microsoft — Python for Beginners | [aka.ms/PythonBeginnerSeries](https://aka.ms/PythonBeginnerSeries) | Short official video series |
| freeCodeCamp — Python for Beginners | [YouTube (~4–5 hrs)](https://www.youtube.com/watch?v=eWRfhZUzrAc) | One long beginner course |
| freeCodeCamp Python curriculum | [freecodecamp.org/learn](https://www.freecodecamp.org/learn/scientific-computing-with-python/) | Interactive practice + projects |

---

## How to use this list

1. Work **one topic at a time** in the order above (fundamentals first, then deep concepts).
2. Read the **Docs** row first, then one **Guide**, then a **Video** if stuck.
3. After each topic, write a tiny script that uses what you learned.
4. Prefer practicing inside a **venv** once you’ve finished topic 2.
