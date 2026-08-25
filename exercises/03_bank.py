"""Exercise 3 — tiny domain model (your Java OOP, Python shape).

Implement Account with:
- deposit(amount)
- withdraw(amount) raising ValueError if insufficient
- transfer(other, amount)

Use a dataclass or a plain class. Add type hints.
Write tests in tests/test_exercises.py (or run this file).
"""

from __future__ import annotations


class Account:
    def __init__(self, owner: str, balance: int = 0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int) -> None:
        raise NotImplementedError

    def withdraw(self, amount: int) -> None:
        raise NotImplementedError

    def transfer(self, other: Account, amount: int) -> None:
        raise NotImplementedError
