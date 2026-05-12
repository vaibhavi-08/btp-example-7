def load_expenses(file_path):
    expenses = []

    with open(file_path, "r") as file:
        for line in file:
            name, amount = line.strip().split(",")

            expenses.append({
                "name": name,
                "amount": float(amount)
            })

    return expenses


def total_expense(expenses):
    return sum(item["amount"] for item in expenses)


def highest_expense(expenses):
    return max(expenses, key=lambda item: item["amount"])