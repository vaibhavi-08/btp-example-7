from app.expenses import (
    total_expense,
    highest_expense,
)


def test_total_expense():
    expenses = [
        {"name": "Food", "amount": 200},
        {"name": "Shopping", "amount": 500},
    ]

    assert total_expense(expenses) == 700


def test_highest_expense():
    expenses = [
        {"name": "Food", "amount": 200},
        {"name": "Shopping", "amount": 500},
        {"name": "Travel", "amount": 300},
    ]

    result = highest_expense(expenses)

    assert result["name"] == "Shopping"
    assert result["amount"] == 500