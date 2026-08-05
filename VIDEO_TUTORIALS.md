# Video Tutorials — Python Fundamentals

Curated YouTube tutorials for each learning point below. Prefer watching in order. Most videos are free; official docs are linked where useful.

---

## 1. Python installation (Python 3.11+)

| Resource | Link | Notes |
|----------|------|-------|
| **Install & setup (Mac & Windows)** — Corey Schafer | [Watch](https://www.youtube.com/watch?v=YYXdXT2l-Gg) | Best first video: download, PATH, verify `python`/`python3` |
| **Install Python 3.11 on Mac** — Make Data Useful | [Watch](https://www.youtube.com/watch?v=hQXQp8U-RmE) | Short walkthrough for macOS |
| **Full beginner course (includes setup)** — freeCodeCamp | [Watch](https://www.youtube.com/watch?v=eWRfhZUzrAc) | Long-form course if you want one continuous path |

**Docs:** [python.org downloads](https://www.python.org/downloads/) · [Using Python on Windows](https://docs.python.org/3.11/using/windows.html)

**Checklist**
- [ ] Install Python **3.11 or newer** from python.org (or your OS package manager / pyenv)
- [ ] On Windows: enable **Add Python to PATH**
- [ ] Verify: `python --version` or `python3 --version`
- [ ] Verify pip: `python -m pip --version`

---

## 2. Virtual environments (venv, conda)

| Resource | Link | Notes |
|----------|------|-------|
| **venv on Mac & Linux** — Corey Schafer | [Watch](https://www.youtube.com/watch?v=Kg1Yvry_Ydk) | Create, activate, deactivate with built-in `venv` |
| **venv on Windows** — Corey Schafer | [Watch](https://www.youtube.com/watch?v=APOPm01BVrk) | Windows `Scripts\activate` workflow |
| **Why virtual environments** — Corey Schafer | [Watch](https://www.youtube.com/watch?v=N5vscPTWKOk) | Motivation + `virtualenv` background |
| **Conda essentials** | [Watch](https://www.youtube.com/watch?v=sDCtY9Z1bqE) | Install conda, create/activate envs, share env files |
| **Managing envs with Conda** | [Watch](https://www.youtube.com/watch?v=EGaw6VXV3GI) | Create, list, remove conda environments |

**Docs:** [`venv`](https://docs.python.org/3/library/venv.html) · [Conda managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

**Quick commands**

```bash
# venv
python -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate           # Windows
deactivate

# conda
conda create -n myproject python=3.11
conda activate myproject
conda deactivate
```

**Checklist**
- [ ] Create a project-local `.venv` with `python -m venv`
- [ ] Activate / deactivate and confirm `( .venv )` in the prompt
- [ ] (Optional) Install Miniconda and create a named conda env

---

## 3. Package management (pip, poetry)

| Resource | Link | Notes |
|----------|------|-------|
| **Pipenv (pip + virtualenv)** — Corey Schafer | [Watch](https://www.youtube.com/watch?v=zDYL22QNiWk) | Clear intro to modern package + env workflows (pip concepts transfer) |
| **Poetry for beginners (2025)** | [Watch](https://www.youtube.com/watch?v=ZyDvBfiiFVM) | Install Poetry, `pyproject.toml`, add deps, lockfile |
| **Poetry & dependency hell** — ArjanCodes | [Watch](https://www.youtube.com/watch?v=0f3moPe_bhk) | Why Poetry helps and how to use it day to day |

**Docs:** [pip user guide](https://pip.pypa.io/en/stable/user_guide/) · [Poetry docs](https://python-poetry.org/docs/) · [Real Python: pip](https://realpython.com/what-is-pip/)

**Quick commands**

```bash
# pip (always prefer inside an activated venv)
python -m pip install requests
python -m pip install -r requirements.txt
python -m pip freeze > requirements.txt
python -m pip uninstall requests

# poetry
pipx install poetry
poetry new myproject   # or: poetry init
poetry add requests
poetry install
poetry run python main.py
```

**Checklist**
- [ ] Install a package with `python -m pip install`
- [ ] Freeze deps to `requirements.txt` and reinstall with `-r`
- [ ] (Optional) Init a Poetry project and `poetry add` a package

---

## 4. IDEs setup (VS Code, PyCharm)

| Resource | Link | Notes |
|----------|------|-------|
| **Getting Started with Python in VS Code** — Microsoft (official) | [Watch](https://www.youtube.com/watch?v=D2cwvpJSBX4) | Extension, interpreter, venv, run, debug (~10 min) |
| **Install PyCharm (Windows)** | [Watch](https://www.youtube.com/watch?v=N3Ai-6d7vDs) | Community Edition install + first project |
| **Getting Started with PyCharm** — JetBrains Guide | [Series](https://www.jetbrains.com/guide/python/tutorials/getting-started-pycharm/) | Official written + video steps (install, interpreter, run, debug) |
| **PyCharm channel** — JetBrains | [Channel](https://www.youtube.com/@PyCharm) | Search “Getting Started” for the latest official playlist |

**Docs:** [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial) · [PyCharm first project](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html)

**Checklist**
- [ ] Install **VS Code** + Microsoft **Python** extension, select interpreter
- [ ] Or install **PyCharm Community**, create a project, pick a local interpreter / venv
- [ ] Run a `print("Hello")` file from the IDE and set one breakpoint

---

## 5. Variables, data types, type hints

| Resource | Link | Notes |
|----------|------|-------|
| **Integers & floats** — Corey Schafer | [Watch](https://www.youtube.com/watch?v=khKv-8q7YmY) | Numeric types and arithmetic |
| **Lists, tuples, sets** — Corey Schafer | [Watch](https://www.youtube.com/watch?v=W8KRzm-HUcc) | Sequence & set types |
| **Dictionaries** — Corey Schafer | [Watch](https://www.youtube.com/watch?v=daefaLgNkw0) | Key–value pairs |
| **Conditionals & booleans** — Corey Schafer | [Watch](https://www.youtube.com/watch?v=DZwmZ8Usvnk) | `bool`, truthiness, `if`/`elif`/`else` |
| **Type hints for beginners** | [Watch](https://www.youtube.com/watch?v=J2z9T5bMKt8) | Annotations, `Optional`/`Union`, mypy intro |
| **Type hints explained clearly** | [Watch](https://www.youtube.com/watch?v=xoa-FlSxbgk) | Practical annotations with examples |

**Docs:** [Built-in types](https://docs.python.org/3/library/stdtypes.html) · [typing](https://docs.python.org/3/library/typing.html) · [Real Python: type checking](https://realpython.com/python-type-checking/)

**Mini examples**

```python
name: str = "Ada"
age: int = 36
pi: float = 3.14159
active: bool = True
scores: list[int] = [90, 85, 88]

def greet(person: str) -> str:
    return f"Hello, {person}"
```

**Checklist**
- [ ] Create variables for `str`, `int`, `float`, `bool`, `list`, `dict`
- [ ] Use `type()` / `isinstance()` to inspect values
- [ ] Add type hints to a small function and (optional) run `mypy`

---

## 6. String manipulation and f-strings

| Resource | Link | Notes |
|----------|------|-------|
| **Strings — textual data** — Corey Schafer | [Watch](https://www.youtube.com/watch?v=k9TUPpGqYTo) | Indexing, slicing, methods, intro to f-strings |
| **String formatting (advanced)** — Corey Schafer | [Watch](https://www.youtube.com/watch?v=vTX3IwquFkc) | `.format()`, f-strings, numbers/dates |
| **How to use f-strings** | [Watch](https://www.youtube.com/watch?v=v1W5QFaDsLc) | Focused f-string walkthrough |

**Docs:** [Text sequence type — str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) · [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

**Mini examples**

```python
name = "Ada"
print(f"Hello, {name}!")
print(f"Pi ≈ {3.14159:.2f}")
print(name.upper(), name.replace("A", "a"), name[0:2])
```

**Checklist**
- [ ] Slice and concatenate strings
- [ ] Use common methods: `upper`, `lower`, `strip`, `split`, `replace`
- [ ] Prefer f-strings for formatting (Python 3.6+)

---

## 7. Input/output operations

| Resource | Link | Notes |
|----------|------|-------|
| **Using `print`** — Microsoft Developer | [Watch](https://www.youtube.com/watch?v=FhoASwgvZHk) | Console output basics (+ brief `input`) |
| **Printing, input, and variables** | [Watch](https://www.youtube.com/watch?v=WnCBW_Im2UU) | `print`, `input`, casting with `int()` |
| **Full beginner course (I/O early on)** — freeCodeCamp | [Watch](https://www.youtube.com/watch?v=eWRfhZUzrAc) | Search the description for “input” / “print” chapter timestamps |

**Docs:** [`input()`](https://docs.python.org/3/library/functions.html#input) · [`print()`](https://docs.python.org/3/library/functions.html#print) · [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html)

**Mini examples**

```python
# console I/O
name = input("Your name: ")
age = int(input("Your age: "))
print(f"{name} is {age} years old.")

# simple file I/O
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Hello, file!\n")

with open("notes.txt", encoding="utf-8") as f:
    print(f.read())
```

**Checklist**
- [ ] Read text with `input()` and remember it returns a **string**
- [ ] Convert with `int()` / `float()` when you need numbers
- [ ] Write and read a text file with `open` + `with`

---

## Suggested watch order

1. Install Python → verify version  
2. VS Code *or* PyCharm setup  
3. venv (+ optional conda)  
4. pip basics → optional Poetry  
5. Variables & types → type hints  
6. Strings & f-strings  
7. `print` / `input` / basic file I/O  

## Full playlists (optional binge)

- [Corey Schafer — Python Programming Beginner Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7)
- [Microsoft — Python for Beginners](https://aka.ms/PythonBeginnerSeries)
- [freeCodeCamp — Python for Beginners](https://www.youtube.com/watch?v=eWRfhZUzrAc)
