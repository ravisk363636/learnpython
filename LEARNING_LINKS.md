# Best Learning Links — Python Fundamentals

Curated **best starting links** for each topic in this repo’s learning path. Prefer official docs + one strong tutorial; use videos when you learn better by watching.

Suggested order: **install → IDE → venv → pip/poetry → types → strings → I/O**.

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
| Guide | [Basic Input, Output, and String Formatting — Real Python](https://realpython.com/python-basic-input-output-and-string-formatting/) | Console I/O + formatting |
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

1. Work **one topic at a time** in the order above.
2. Read the **Docs** row first, then one **Guide**, then a **Video** if stuck.
3. After each topic, write a tiny script that uses what you learned.
4. Prefer practicing inside a **venv** once you’ve finished topic 2.
