import json
import matplotlib.pyplot as plt
from datetime import datetime

DATA_FILE = "finance_data.json"

# -------------------- Load / Save Data -------------------- #
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"transactions": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# -------------------- Add Transaction -------------------- #
def add_transaction(type):
    amount = float(input("Enter amount: ₹ "))
    category = input("Enter category (Food, Rent, Salary, Shopping): ")
    date = datetime.now().strftime("%Y-%m-%d")

    transaction = {"type": type, "amount": amount, "category": category, "date": date}

    data = load_data()
    data["transactions"].append(transaction)
    save_data(data)

    print("✔ Transaction added successfully!\n")

# -------------------- Summary -------------------- #
def view_summary():
    data = load_data()
    income = sum(t["amount"] for t in data["transactions"] if t["type"] == "income")
    expense = sum(t["amount"] for t in data["transactions"] if t["type"] == "expense")

    print("\n------ Monthly Summary ------")
    print(f"Total Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Savings: ₹{income - expense}\n")

# -------------------- Chart -------------------- #
def show_expense_chart():
    data = load_data()
    expenses = [t for t in data["transactions"] if t["type"] == "expense"]

    if not expenses:
        print("No expenses to show.\n")
        return

    categories = {}
    for e in expenses:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]

    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Expense Breakdown")
    plt.show()

# -------------------- Menu -------------------- #
def main():
    while True:
        print("\n==== Personal Finance Tracker ====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Show Expense Pie Chart")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction("income")
        elif choice == "2":
            add_transaction("expense")
        elif choice == "3":
            view_summary()
        elif choice == "4":
            show_expense_chart()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
