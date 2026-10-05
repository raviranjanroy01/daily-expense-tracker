import argparse

from expense_manager import (
    add_expense,
    view_expenses,
    search_expenses,
    delete_expense,
    total_expense,
    monthly_summary,
    category_summary,
    category_expenses,
    get_monthly_total
)


def show_menu():
    print("\n==============================")
    print("      DAILY EXPENSE TRACKER")
    print("==============================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expenses")
    print("4. Delete Expense")
    print("5. Total Spending")
    print("6. Monthly Summary")
    print("7. Category-wise Summary")
    print("8. Exit")


def handle_arguments():
    parser = argparse.ArgumentParser(
        description="Daily Expense Tracker"
    )

    parser.add_argument(
        "--total",
        action="store_true",
        help="Display total spending"
    )

    parser.add_argument(
        "--category",
        type=str,
        help="Display expenses for a category"
    )

    parser.add_argument(
        "--month",
        type=str,
        help="Display total spending for a month (MM-YYYY)"
    )

    args = parser.parse_args()

    if args.total:
        total_expense()
        return True

    if args.category:
        category_expenses(args.category)
        return True

    if args.month:
        month = args.month

        try:
            from datetime import datetime
            datetime.strptime(month, "%m-%Y")
        except ValueError:
            print("Invalid month. Please use MM-YYYY format.")
            return True

        total, found = get_monthly_total(month)

        if found:
            print(f"Total spending for {month}: ₹{total:.2f}")
        else:
            print(f"No expenses found for {month}.")

        return True

    return False


def main():
    if handle_arguments():
        return

    while True:

        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expenses()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            total_expense()

        elif choice == "6":
            monthly_summary()

        elif choice == "7":
            category_summary()

        elif choice == "8":
            print("Exiting Expense Tracker...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()