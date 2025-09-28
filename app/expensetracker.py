# Expense tracker
import json

expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

def show_expenses():
    try:
        with open("expenses.json", "r") as f:
            data = json.load(f)
            total = 0
            for e in data:
                print(f"{e['category']} - {e['amount']}")
                total += e['amount']
            print("Total:", total)
    except FileNotFoundError:
        print("No expenses recorded!")

add_expense(500, "Food")
add_expense(1000, "Shopping")
show_expenses()
