from __future__ import annotations

from exercises.solutions.bank import Account
from exercises.solutions.fizzbuzz import fizzbuzz
from exercises.solutions.word_count import word_count


def test_fizzbuzz() -> None:
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"


def test_word_count() -> None:
    assert word_count("Ada Ada, ada! Grace.") == {"ada": 3, "grace": 1}


def test_bank_transfer() -> None:
    a = Account("Ada", 100)
    b = Account("Grace", 0)
    a.transfer(b, 40)
    assert a.balance == 60
    assert b.balance == 40


def test_bank_overdraft() -> None:
    a = Account("Ada", 10)
    try:
        a.withdraw(50)
        raise AssertionError("expected ValueError")
    except ValueError:
        assert a.balance == 10
