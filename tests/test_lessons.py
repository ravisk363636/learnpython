"""pytest discovers test_*.py and functions named test_*.

Run from repo root: pytest -q
"""

from __future__ import annotations

from pathlib import Path

import lessons.collections_tour as coll
import lessons.oop as o
import lessons.stdlib_tour as st
import lessons.syntax as s


def test_lesson_scripts() -> None:
    s.main()
    coll.main()
    o.main()
    st.main()


def test_greet() -> None:
    assert s.greet("Ada") == "Hello, Ada."
    assert s.greet("Ada", excited=True) == "Hello, Ada!"


def test_divide_none_on_zero() -> None:
    assert s.divide(1, 0) is None
    assert s.divide(9, 3) == 3.0


def test_robot_is_a_greeter() -> None:
    assert o.shout(o.Robot("R2"), "Ada") == "R2 SAYS HI TO ADA"


def test_withdraw() -> None:
    acct = o.Account(10)
    try:
        acct.withdraw(50)
        raise AssertionError("expected InsufficientFunds")
    except o.InsufficientFunds:
        assert acct.balance == 10


def test_adult_names(tmp_path: Path) -> None:
    # tmp_path is a pytest fixture (no @Rule TemporaryFolder)
    people: list[dict[str, object]] = [{"name": "Ada", "age": 36}, {"name": "Kid", "age": 12}]
    assert st.adult_names(people) == ["Ada"]
    p = tmp_path / "u.json"
    st.save_users(p, [{"name": "Ada", "role": "admin"}])
    assert st.load_users(p)[0]["name"] == "Ada"
