from app.expenses import (
    load_expenses,
    total_expense,
    highest_expense,
)


def main():
    expenses = load_expenses("data/expenses.txt")

    print("Total Expense:", total_expense(expenses))

    highest = highest_expense(expenses)

    print(
        f"Highest Expense: {highest['name']} - {highest['amount']}"
    )


if __name__ == "__main__":
    main()