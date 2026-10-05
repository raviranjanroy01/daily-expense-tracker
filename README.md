# Daily Expense Tracker

A simple command-line based expense management application developed using Python. The project allows users to record, view, search, delete, and analyze their daily expenses.

## Features

- Add new expenses
- View all saved expenses
- Search expenses by category or description
- Delete an expense
- Calculate total spending
- Generate monthly expense summaries
- Generate category-wise expense summaries
- Store data permanently using JSON
- Input validation and exception handling
- Command-line argument support

## Technologies Used

- Python 3
- JSON
- argparse
- File Handling
- Exception Handling
- Python Standard Library

## Project Structure

```text
daily_expense_tracker/
│
├── main.py
├── expense_manager.py
├── storage.py
├── expenses.json
├── README.md
└── requirements.txt
```

## Description of Files

### `main.py`

The main program file. It displays the menu, handles user choices, and processes command-line arguments.

### `expense_manager.py`

Contains the main expense management functions such as:

- Adding expenses
- Viewing expenses
- Searching expenses
- Deleting expenses
- Calculating total spending
- Monthly summaries
- Category-wise summaries
- Input validation

### `storage.py`

Handles reading and writing expense data to the JSON file.

### `expenses.json`

Stores all expense records permanently in JSON format.

### `requirements.txt`

Contains information about the project's external dependencies.

The project currently uses only Python's standard library, so no external packages are required.

## How to Run

Make sure Python is installed.

Open a terminal in the project directory and run:

```bash
python main.py
```

On Windows, you can also use:

```powershell
py main.py
```

## Interactive Menu

When the program starts, the following menu is displayed:

```text
==============================
      DAILY EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Search Expenses
4. Delete Expense
5. Total Spending
6. Monthly Summary
7. Category-wise Summary
8. Exit
```

## Command-Line Arguments

The application also supports command-line arguments.

### Display help

```powershell
py main.py --help
```

### Display total spending

```powershell
py main.py --total
```

### Display expenses from a category

```powershell
py main.py --category Food
```

### Display spending for a particular month

Use the `MM-YYYY` format:

```powershell
py main.py --month 10-2026
```

## Data Format

Expenses are stored in `expenses.json`.

Example:

```json
[
    {
        "date": "05-10-2026",
        "category": "Food",
        "description": "Lunch",
        "amount": 150.0
    }
]
```

Each expense contains:

| Field | Description |
|---|---|
| `date` | Date of the expense |
| `category` | Expense category |
| `description` | Description of the expense |
| `amount` | Amount spent |

## Input Validation

The application validates user input to prevent invalid data.

Examples:

- Date must follow `DD-MM-YYYY` format.
- Amount must be a valid number.
- Amount must be greater than zero.
- Category cannot be empty.
- Description cannot be empty.
- Invalid menu choices are rejected.
- Invalid expense numbers are handled safely.

## Concepts Demonstrated

This project demonstrates the following Python concepts:

- Variables and data types
- Lists
- Dictionaries
- Functions
- Modules
- Loops
- Conditional statements
- File handling
- JSON data storage
- Exception handling
- Input validation
- Command-line arguments
- Basic data processing

## Future Improvements

Possible future improvements include:

- Graphical user interface
- Expense editing
- Budget limits and alerts
- Export reports to CSV
- Expense charts and graphs
- User authentication
- Database support using SQLite

