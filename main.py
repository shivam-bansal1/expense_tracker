from argparse import ArgumentParser
from utils import ExpenseManager
import shlex

def help() -> None:
    help_text = """
        Available Commands:
          add                   - Add expense description and amount
          update                - Update expense
          delete                - Delete expense
          list                  - View all the expenses
          summary               - View summary of all expenses
          summary month         - View summary of specific month
          help                  - Show this help message
          exit / quit           - Exit the program
    """

    print(help_text)

def interactive_mode():
    expense_manager = ExpenseManager()
    parser = main()

    print("=" * 50)
    print("Expense Tracker")
    print("=" * 50)
    print("Type 'help' for available commands or 'exit' to quit\n")

    while True:
        user_input = input("expense-tracker > ").strip()

        if not user_input:
            continue

        if user_input.strip().lower() in ["exit", "quit", "q"] :
            print("Goodbye!")
            break

        if user_input.strip().lower() == "help":
            help()
            continue


        argv = shlex.split(user_input)
        args = parser.parse_args(argv)

        if args.command == "add":
            description = "".join(args.description)
            amount = args.amount

            if not description or not amount :
                print("Error: Please provide a expense description and amount.")
                print("Usage: add <description> <amount>")
            else:
                expense_manager.add_expense(description, amount)

        elif args.command == "update":
            if not args.description and not args.amount :
                print("Error: Please provide updated expense description or amount or both.")
                print("Usage: update <id> <description> <amount>")
            else:
                expense_id = args.id
                description = args.description if args.description else None
                amount = args.amount if args.amount else None
                expense_manager.update_expense(expense_id, description, amount)

        elif args.command == "delete" :
            expense_manager.delete_expense(args.id)
        #
        elif args.command == "list" :
                expense_manager.list_expenses()

        elif args.command == "summary" :
            month = args.month
            expense_manager.summary_expense(month)



def main():

    parser = ArgumentParser(description="Expense tracker CLI")
    subparser = parser.add_subparsers(dest="command")

    add_parser = subparser.add_parser("add", help="Add expense description")
    add_parser.add_argument("description", nargs="+", type=str, help="Expense details")
    add_parser.add_argument("amount", type=float, help="Expense amount")

    update_parser = subparser.add_parser("update", help="Update expense")
    update_parser.add_argument("id", type=int, help="Expense id")
    update_parser.add_argument("description", nargs="?", type=str, help="Expense updated details")
    update_parser.add_argument("amount", nargs="?", type=float, default=None, help="Expense updated amount")

    delete_parser = subparser.add_parser("delete", help="Delete expense")
    delete_parser.add_argument("id", type=int, help="Expense id")

    list_parser = subparser.add_parser("list", help="list expenses")

    summary_parser = subparser.add_parser("summary", help="Summary of expenses")
    summary_parser.add_argument("month", nargs="?", type=int, help="Expense month")

    return parser


if __name__ == "__main__":
    exit(interactive_mode())
