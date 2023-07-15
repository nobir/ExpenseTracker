from functions.add_expense import add_expense
from functions.view_expense_list import view_expense_list
from functions.filter_expenses import filter_expenses
from functions.calculate_total_expenses import calculate_total_expenses
from functions.delete_expense import delete_expense
from functions.export_expense_data import export_expense_data
from functions.add_category import add_category


expense_data = []
categories = []


def main():
    while True:
        print("\nExpense Tracker")
        print("---------------")
        print("1. Add an Expense")
        print("2. View Expense List")
        print("3. Filter Expenses")
        print("4. Calculate Total Expenses")
        print("5. Delete an Expense")
        print("6. Export Expense Data")
        print("7. Add categories")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if not str.isdigit(choice):
            print("Invalid choice.")
            continue
        else:
            choice = int(choice)

        if choice == 1:
            add_expense(expense_data, categories)
        elif choice == 2:
            view_expense_list(expense_data)
        elif choice == 3:
            filter_expenses(expense_data)
        elif choice == 4:
            calculate_total_expenses(expense_data)
        elif choice == 5:
            delete_expense(expense_data)
        elif choice == 6:
            export_expense_data(expense_data)
        elif choice == 7:
            add_category(categories)
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
            continue


if __name__ == "__main__":
    main()
