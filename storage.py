import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "expenses.json")


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except (json.JSONDecodeError, OSError):
        return []


def save_expenses(expenses):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)

        return True

    except OSError:
        return False