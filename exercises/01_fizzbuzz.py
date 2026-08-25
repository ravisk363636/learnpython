"""Exercise 1 — FizzBuzz (warm-up).

Print 1..100. Multiples of 3 → Fizz, 5 → Buzz, both → FizzBuzz.

Java muscle memory:
    for (int i = 1; i <= 100; i++) { ... }

Python:
    for i in range(1, 101):  # stop is exclusive

When you are done, run: python exercises/01_fizzbuzz.py
Then compare with exercises/solutions/fizzbuzz.py
"""

from __future__ import annotations


def fizzbuzz(n: int) -> str:
    """Return the FizzBuzz label for n (the number itself if no match)."""
    raise NotImplementedError("your turn")


def main() -> None:
    for i in range(1, 101):
        print(fizzbuzz(i))


if __name__ == "__main__":
    main()
