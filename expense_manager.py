from datetime import datetime

from storage import load_expenses, save_expenses


def get_valid_date():
    while True:
        date = input("Enter date (DD-MM-YYYY): ").strip()

        try:
            datetime.strptime(date, "%d-%m-%Y")
            return date

        except ValueError:
            print("Invalid date. Please use DD-MM-YYYY format.")


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Invalid amount. Please enter a number.")


def add_expense():
    print("\n--- Add Expense ---")

    date = get_valid_date()

    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    while True:
        description = input("Enter description: ").strip()

        if description:
            break

        print("Description cannot be empty.")

    amount = get_valid_amount()

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses = load_expenses()
    expenses.append(expense)

    if save_expenses(expenses):
        print("Expense added successfully.")
    else:
        print("Could not save the expense.")


def display_expense(number, expense):
    print(f"\nExpense #{number}")
    print(f"Date        : {expense['date']}")
    print(f"Category    : {expense['category']}")
    print(f"Description : {expense['description']}")
    print(f"Amount      : ₹{expense['amount']:.2f}")


def view_expenses():
    print("\n--- All Expenses ---")

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for number, expense in enumerate(expenses, start=1):
        display_expense(number, expense)


def search_expenses():
    print("\n--- Search Expenses ---")

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    keyword = input(
        "Enter category or description to search: "
    ).strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    found = False

    for number, expense in enumerate(expenses, start=1):

        if (
            keyword in expense["category"].lower()
            or keyword in expense["description"].lower()
        ):
            display_expense(number, expense)
            found = True

    if not found:
        print("No matching expenses found.")


def delete_expense():
    print("\n--- Delete Expense ---")

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. "
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"₹{expense['amount']:.2f}"
        )

    try:
        choice = int(input("\nEnter expense number to delete: "))

        if choice < 1 or choice > len(expenses):
            print("Invalid expense number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    deleted = expenses.pop(choice - 1)

    if save_expenses(expenses):
        print(
            f"Deleted: {deleted['description']} "
            f"(₹{deleted['amount']:.2f})"
        )
    else:
        print("Could not save changes.")


def total_expense():
    print("\n--- Total Expense ---")

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print(f"Total Spending: ₹{total:.2f}")


def get_monthly_total(month):
    expenses = load_expenses()

    total = 0
    found = False

    for expense in expenses:

        try:
            date = datetime.strptime(
                expense["date"],
                "%d-%m-%Y"
            )

            expense_month = date.strftime("%m-%Y")

            if expense_month == month:
                total += expense["amount"]
                found = True

        except ValueError:
            continue

    return total, found


def monthly_summary():
    print("\n--- Monthly Summary ---")

    month = input("Enter month and year (MM-YYYY): ").strip()

    try:
        datetime.strptime(month, "%m-%Y")

    except ValueError:
        print("Invalid month. Please use MM-YYYY format.")
        return

    total, found = get_monthly_total(month)

    if found:
        print(f"Total spending for {month}: ₹{total:.2f}")
    else:
        print(f"No expenses found for {month}.")


def category_summary():
    print("\n--- Category-wise Summary ---")

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"].strip().lower()
        amount = expense["amount"]

        categories[category] = (
            categories.get(category, 0) + amount
        )

    for category, amount in sorted(categories.items()):
        print(f"{category.title():15} ₹{amount:.2f}")


def category_expenses(category):
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    found = False
    total = 0

    print(f"\n--- Expenses in category: {category} ---")

    for number, expense in enumerate(expenses, start=1):

        if expense["category"].lower() == category.lower():
            display_expense(number, expense)

            total += expense["amount"]
            found = True

    if found:
        print(f"\nCategory Total: ₹{total:.2f}")
    else:
        print(f"No expenses found in category '{category}'.")