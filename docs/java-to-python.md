# Java → Python: the mental model

You already know programming. Python is a different *shape*, not a new career.

| Java habit | Python equivalent |
|---|---|
| Compile then run | Interpret (or compile to bytecode on first import) |
| `{ }` blocks | Indentation **is** the block |
| `public class Foo` per file | A `.py` file **is** a module; classes are optional |
| `null` | `None` |
| `boolean` | `bool` (`True` / `False`, capitalized) |
| `final` locals | Convention; `Final` from `typing` is a hint only |
| `interface` | `Protocol` (structural) or `ABC` (explicit) |
| `List<T>` | `list[T]` (runtime is still a plain list) |
| `Map<K,V>` | `dict[K, V]` |
| `Optional<T>` | `T \| None` |
| getters/setters | Public attributes, or `@property` |
| `equals` / `hashCode` | `__eq__` / `__hash__` (dataclasses do this) |
| `toString` | `__repr__` / `__str__` |
| checked exceptions | None. Catch what you care about |
| `package com.foo` | Directory + `__init__.py` (optional on 3.3+) |
| Maven/Gradle | `pip` + `pyproject.toml` (or `requirements.txt`) |
| JUnit | `pytest` |
| `static` methods | `@staticmethod` or module-level functions (prefer functions) |
| `synchronized` | `threading.Lock` (and you will rarely want threads first) |

## Rules that save Java people weeks

1. **Functions are first-class.** You do not need a class to hold a method.
2. **Everything is a reference.** Assignment never copies a list/dict. Use `.copy()` or `copy.deepcopy()`.
3. **Types are optional at runtime.** Add them anyway (`def f(x: int) -> str`). Run `mypy` or `pyright` like you miss the Java compiler.
4. **`==` is value equality.** Identity is `is` (use `is None`, never `== None`).
5. **Default args are evaluated once.** Never `def f(items=[])`. Use `None` and create inside.
6. **`self` is explicit.** First parameter of instance methods. It is `this`, you just write it.
7. **No overloading.** One name, one function. Use default args, `*args`, or `@singledispatch`.
8. **Multiple inheritance exists.** Prefer composition. Use `Protocol` for “can duck-type.”
9. **Virtualenv is not optional.** `python -m venv .venv && source .venv/bin/activate`.
10. **The stdlib is huge.** Read it before adding a dependency: `pathlib`, `json`, `dataclasses`, `functools`, `itertools`, `collections`, `concurrent.futures`.

## Syntax you will type every day

```java
public int add(int a, int b) {
    return a + b;
}
```

```python
def add(a: int, b: int) -> int:
    return a + b
```

```java
List<String> names = new ArrayList<>();
names.add("Ada");
Map<String, Integer> ages = Map.of("Ada", 36);
for (String n : names) { ... }
if (ages.containsKey("Ada")) { ... }
```

```python
names: list[str] = ["Ada"]
ages: dict[str, int] = {"Ada": 36}
for n in names:
    ...
if "Ada" in ages:
    ...
```

```java
public class User {
    private final String name;
    public User(String name) { this.name = name; }
    public String getName() { return name; }
}
```

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
```

## What to ignore for the first week

- Metaclasses, `__slots__`, descriptors
- Async (`asyncio`) until you have a real I/O problem
- Multiple inheritance mixins
- C extensions / Cython
- “Pythonic” golf. Write boring, typed, tested code.

## Tooling (install once)

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip pytest ruff
```

Run lessons:

```bash
python lessons/syntax.py
pytest tests/ -q
```
