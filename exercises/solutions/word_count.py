from __future__ import annotations

import string
from collections import Counter


def word_count(text: str) -> dict[str, int]:
    words = [w.strip(string.punctuation).lower() for w in text.split()]
    words = [w for w in words if w]
    return dict(Counter(words))
