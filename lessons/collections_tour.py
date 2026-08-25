"""Java → Python: list, dict, set, tuple, comprehensions.

Run: python lessons/collections_tour.py
"""

from __future__ import annotations

from collections import defaultdict, Counter


def main() -> None:
    # list == ArrayList. Heterogeneous at runtime; type hints keep you honest.
    nums: list[int] = [1, 2, 3]
    nums.append(4)
    nums.extend([5, 6])
    assert nums[0] == 1
    assert nums[-1] == 6  # last element
    assert nums[1:3] == [2, 3]  # slice: start inclusive, end exclusive (like substring)

    # tuple == immutable list. Good for records / dict keys.
    point: tuple[int, int] = (10, 20)
    x, y = point  # destructuring
    assert x == 10 and y == 20

    # dict == HashMap. Insertion-ordered since 3.7.
    ages: dict[str, int] = {"Ada": 36, "Grace": 85}
    ages["Alan"] = 41
    assert ages.get("Missing") is None  # no exception (contrast Map.get in some APIs)
    assert ages.get("Missing", 0) == 0
    assert "Ada" in ages  # containsKey

    for name, age in ages.items():  # Map.entrySet()
        assert isinstance(name, str) and isinstance(age, int)

    # set == HashSet
    tags: set[str] = {"java", "python"}
    tags.add("python")  # no-op, unique
    assert tags == {"java", "python"}

    # Comprehensions replace many for-loops (like streams, but eager).
    squares = [n * n for n in nums if n % 2 == 0]
    assert squares == [4, 16, 36]

    name_lengths = {name: len(name) for name in ages}
    assert name_lengths["Ada"] == 3

    # defaultdict / Counter replace a lot of get-or-create Java boilerplate.
    groups: dict[str, list[int]] = defaultdict(list)
    groups["even"].append(2)
    assert groups["odd"] == []  # missing key → empty list, not KeyError

    counts = Counter(["a", "b", "a"])
    assert counts["a"] == 2

    # Copy vs alias (the bug Java people hit on day one).
    a = [1, 2]
    b = a  # same object (like assigning a List reference)
    b.append(3)
    assert a == [1, 2, 3]
    c = a.copy()  # shallow copy
    c.append(4)
    assert a == [1, 2, 3]

    print("02_collections: ok")


if __name__ == "__main__":
    main()
