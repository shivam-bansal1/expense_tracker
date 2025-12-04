# expense_tracker# 💰 Expense Tracker CLI

A simple yet powerful command-line expense tracking application built with Python. Track your daily expenses, view summaries, and manage your financial records with ease.

## ✨ Features

- ➕ **Add Expenses** - Record expenses with descriptions and amounts
- ✏️ **Update Expenses** - Modify existing expense details
- 🗑️ **Delete Expenses** - Remove unwanted expense records
- 📋 **List Expenses** - View all expenses in a formatted table
- 📊 **Expense Summary** - Get total expenses (overall or by month)
- 🔄 **Interactive Mode** - User-friendly command-line interface
- 💾 **JSON Storage** - Simple, portable data storage

## 📋 Requirements

- Python 3.8+
- pandas

## 🚀 Installation

1. Clone or download this repository

2. Install required dependencies:
```expense_manager
pip install pandas
```

3. Run the application:
```expense_manager
python main.py
```

## 💻 Usage

### Interactive Mode

Start the application in interactive mode:

```expense_manager
python main.py
```

You'll see a prompt where you can enter commands:

```
==================================================
Expense Tracker - Interactive Mode
==================================================
Type 'help' for available commands or 'exit' to quit

expense-tracker >
```

### Available Commands

#### Add an Expense
```expense_manager
add "Grocery shopping" 45.50
add "Coffee" 5.00
add "Netflix subscription" 12.99
```

#### Update an Expense
```expense_manager
# Update description only
update 1 "Weekly groceries"

# Update amount only
update 1 50.00

# Update both
update 1 "Monthly groceries" 150.00
```

#### Delete an Expense
```expense_manager
delete 1
```

#### List All Expenses
```expense_manager
list
```

Output example:
```
 id       date  description           amount
  1  05-12-2025  Grocery shopping      45.50
  2  05-12-2025  Coffee                 5.00
  3  05-12-2025  Netflix subscription  12.99
```

#### View Expense Summary
```expense_manager
# Total of all expenses
summary

# Total for a specific month (1-12)
summary 12
```

#### Get Help
```expense_manager
help
```

#### Exit the Application
```expense_manager
exit
# or
quit
# or
q
```

## 📁 Project Structure

```
expense-tracker/
├── main.py              # Entry point and CLI interface
├── utils.py             # ExpenseManager class
└── expenses.json        # Data storage (auto-created)
```

## 🗂️ Data Storage

Expenses are stored in a `expenses.json` file in the following format:

```json
[
  {
    "id": 1,
    "date": "05-12-2025",
    "description": "Grocery shopping",
    "amount": 45.5
  },
  {
    "id": 2,
    "date": "05-12-2025",
    "description": "Coffee",
    "amount": 5.0
  }
]
```

## 🙏 Acknowledgments
Inspired by [Expense Tracker Project](https://roadmap.sh/projects/expense-tracker)

# **Happy tracking! 📊💰**