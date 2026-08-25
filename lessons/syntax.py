"""Java → Python: syntax, types, None, and control flow.

Run: python lessons/syntax.py
"""

from __future__ import annotations


def greet(name: str, excited: bool = False) -> str:
    # Default args replace method overloading for simple cases.
    suffix = "!" if excited else "."
    return f"Hello, {name}{suffix}"  # f-string == Java String.formatted / STR."..."


def divide(a: float, b: float) -> float | None:
    # No checked exceptions. Return None or raise.
    if b == 0:
        return None
    return a / b  # True division. Integer division is //


def classify(n: int) -> str:
    # if / elif / else. No switch required; 3.10+ has match.
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    else:
        return "positive"


def match_status(code: int) -> str:
    match code:
        case 200:
            return "ok"
        case 404:
            return "missing"
        case _:
            return "other"


def main() -> None:
    assert greet("Ada") == "Hello, Ada."
    assert greet("Ada", excited=True) == "Hello, Ada!"

    x = divide(10, 2)
    assert x == 5.0
    assert divide(1, 0) is None  # identity check for None

    # Truthiness: empty list/str/0/None are False (unlike Java primitives).
    names: list[str] = []
    if not names:
        names.append("Ada")

    # Chained comparisons work: 0 < n < 10
    n = 5
    assert 0 < n < 10

    # Ternary: value_if_true if cond else value_if_false
    label = "even" if n % 2 == 0 else "odd"
    assert label == "odd"

    assert classify(-1) == "negative"
    assert match_status(404) == "missing"

    print("01_syntax: ok")


if __name__ == "__main__":
    # Java: public static void main(String[] args)
    # This guard means "only run when executed as a script, not when imported."
    main()
