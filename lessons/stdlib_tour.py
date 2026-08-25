"""Java → Python: pathlib, json, venv-minded scripts, pytest-shaped functions.

Run: python lessons/stdlib_tour.py
"""

from __future__ import annotations

import json
from pathlib import Path


def load_users(path: Path) -> list[dict[str, str]]:
    # pathlib.Path == a sane java.nio.file.Path
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    if not isinstance(data, list):
        raise ValueError("expected a JSON array")
    return data


def save_users(path: Path, users: list[dict[str, str]]) -> None:
    path.write_text(json.dumps(users, indent=2), encoding="utf-8")


def adult_names(users: list[dict[str, object]]) -> list[str]:
    names: list[str] = []
    for u in users:
        age = u.get("age")
        name = u.get("name")
        if isinstance(age, int) and age >= 18 and isinstance(name, str):
            names.append(name)
    return names


def main() -> None:
    tmp = Path("/tmp/learnpython-users.json")
    save_users(tmp, [{"name": "Ada", "role": "admin"}])
    loaded = load_users(tmp)
    assert loaded[0]["name"] == "Ada"

    people: list[dict[str, object]] = [
        {"name": "Ada", "age": 36},
        {"name": "Kid", "age": 12},
    ]
    assert adult_names(people) == ["Ada"]

    # Context managers == try-with-resources
    with tmp.open("r", encoding="utf-8") as f:
        assert "Ada" in f.read()

    tmp.unlink(missing_ok=True)
    print("04_stdlib: ok")


if __name__ == "__main__":
    main()
