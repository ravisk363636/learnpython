"""Java → Python: classes, dataclasses, Protocol, exceptions.

Run: python lessons/oop.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


class Greeter(Protocol):
    """Structural interface: any object with greet(str) -> str qualifies.

    No `implements` clause. The type checker checks the shape.
    """

    def greet(self, name: str) -> str: ...


class Robot:
    def __init__(self, serial: str) -> None:
        # __init__ == constructor. self == this.
        self.serial = serial

    def greet(self, name: str) -> str:
        return f"{self.serial} says hi to {name}"

    def __repr__(self) -> str:
        # unambiguous debug string (like toString for logs)
        return f"Robot(serial={self.serial!r})"


@dataclass(frozen=True)
class User:
    """frozen=True ≈ final fields + value equality.

    You get __init__, __repr__, __eq__, and __hash__ for free.
    """

    name: str
    roles: list[str] = field(default_factory=list)  # NOT default_factory-less mutable default


class InsufficientFunds(Exception):
    """Custom exception == a class. Unchecked by nature."""


class Account:
    def __init__(self, balance: int) -> None:
        self._balance = balance  # leading _ == "protected by convention", not JVM private

    @property
    def balance(self) -> int:
        return self._balance

    def withdraw(self, amount: int) -> None:
        if amount > self._balance:
            raise InsufficientFunds(f"need {amount}, have {self._balance}")
        self._balance -= amount


def shout(g: Greeter, name: str) -> str:
    return g.greet(name).upper()


def main() -> None:
    bot = Robot("R2")
    assert shout(bot, "Ada") == "R2 SAYS HI TO ADA"

    u = User(name="Ada", roles=["admin"])
    u2 = User(name="Ada", roles=["admin"])
    assert u == u2  # dataclass equality is by value

    acct = Account(100)
    acct.withdraw(40)
    assert acct.balance == 60

    try:
        acct.withdraw(1000)
        raise AssertionError("should have failed")
    except InsufficientFunds:
        pass

    print("03_oop: ok")


if __name__ == "__main__":
    main()
