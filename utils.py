from pathlib import Path
import json
import os
from typing import List, Any, Optional
from datetime import datetime
import pandas as pd


class ExpenseManager:

    DATE_FORMAT = "%d-%m-%Y"

    def __init__(self, file="expenses.json"):
        self.file_path = Path(file)

    def _load_expenses(self) -> List[dict | Any]:
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r") as file:
                expenses = json.load(file)
                return expenses
        except json.JSONDecodeError:
            print("Expenses file is corrupt!")
            return []
        except Exception as e:
            raise IOError("Error reading expenses file: {}".format(e))

    def _save_expenses(self, expenses: List[dict | Any]) -> None:
        try:
            with open(self.file_path, "w") as file:
                json.dump(expenses, file)
        except Exception as e:
            raise IOError(f"Error writing tasks file: {e}")

    def _get_next_id(self, expenses) -> int:
        return max((expense["id"] for expense in expenses), default=0) + 1

    def _get_expense_index(self, id: int) -> Optional[int]:
        expenses = self._load_expenses()
        if not expenses:
            print("No expenses found!")
            return None

        for idx, expense in enumerate(expenses) :
            if expense["id"] == id:
                return idx

        return None


    def add_expense(self, description: str, amount: float) -> None:
        if not description or not description.strip():
            print("Error: Expense description cannot be empty!")
            return

        if amount <= 0:
            print("Error: Expense amount must be greater than zero!")
            return

        description = description.strip()
        expenses = self._load_expenses()
        expense_id = self._get_next_id(expenses)

        new_expense = {
            "id": expense_id,
            "date": datetime.now().strftime(self.DATE_FORMAT),
            "description": description,
            "amount": amount,
        }

        expenses.append(new_expense)
        self._save_expenses(expenses)
        print(f"Expense added successfully (ID: {expense_id})")

    def update_expense(self, expense_id: int, description: str, amount: float) -> None:

        if amount is not None and amount <= 0:
            print("Error: Expense amount must be greater than zero!")
            return

        if description is not None:
            description = description.strip()
            if not description:
                print("Error: Expense description cannot be empty!")
                return

        expenses = self._load_expenses()
        expense_index = self._get_expense_index(expense_id)

        if expense_index is None:
            print(f"Error: Expense with ID {expense_id} does not exist!")
            return

        if description is not None :
            expenses[expense_index]["description"] = description
        if amount is not None:
            expenses[expense_index]["amount"] = amount

        expenses[expense_index]["date"] = datetime.now().strftime(self.DATE_FORMAT)
        self._save_expenses(expenses)
        print(f"Expense updated successfully (ID: {expense_id})")

    def delete_expense(self, expense_id: int) -> None:
        expenses = self._load_expenses()
        if not expenses:
            print("Error: No expenses found!")
            return

        expense_index = self._get_expense_index(expense_id)
        if expense_index is None:
            print(f"Error: Expense with ID {expense_id} does not exist!")
            return

        expenses.pop(expense_index)
        self._save_expenses(expenses)
        print(f"Expense deleted successfully (ID: {expense_id})")

    def list_expenses(self) -> None:
        expenses = self._load_expenses()
        if not expenses:
            print("Expenses not found!")
            return

        expenses_table = pd.DataFrame(expenses)

        print(expenses_table)
        return


    def summary_expense(self, month: int=None) -> None:
        expenses = self._load_expenses()
        if not expenses:
            print("Expenses not found!")
            return

        if month is not None:
            if not 1 <= month <= 12:
                print("Error: Month must be between 1 and 12!")
                return

            filtered_expenses = [
                expense for expense in expenses
                if datetime.strptime(expense["date"], self.DATE_FORMAT).month == month
            ]

            if not filtered_expenses:
                print(f"No expenses found for month {month}!")
                return

            total = sum(expense["amount"] for expense in filtered_expenses)
            print(f"\nTotal expenses for month {month}: ${total:.2f}")
            print(f"Number of expenses: {len(filtered_expenses)}\n")
        else:
            total = sum(expense["amount"] for expense in expenses)
            print(f"\nTotal expenses: ${total:.2f}")
            print(f"Number of expenses: {len(expenses)}\n")
