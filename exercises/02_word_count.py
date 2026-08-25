"""Exercise 2 — word count (HashMap muscle).

Count words in a string, case-insensitive, ignoring punctuation.

Hint: str.split(), str.lower(), collections.Counter
"""

from __future__ import annotations

import string
from collections import Counter


def word_count(text: str) -> dict[str, int]:
    raise NotImplementedError("your turn")


def _strip_punct(word: str) -> str:
    return word.strip(string.punctuation)


def main() -> None:
    sample = "Ada Ada, ada! Grace."
    print(word_count(sample))  # expect {'ada': 3, 'grace': 1}


if __name__ == "__main__":
    main()
