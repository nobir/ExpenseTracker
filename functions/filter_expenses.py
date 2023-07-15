def filter_expenses(expense_data):
    print("Filter Expenses:")
    print("1. Filter by Date Range")
    print("2. Filter by Category")
    print("3. Filter by Date Range and Category")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        filtered_expenses = [
            expense for expense in expense_data if start_date <= expense['Date'] <= end_date]
    elif choice == 2:
        category = input("Enter category: ")
        filtered_expenses = [
            expense for expense in expense_data if expense['Category'] == category]
    elif choice == 3:
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        filtered_expenses = [expense for expense in expense_data if start_date <=
                             expense['Date'] <= end_date and expense['Category'] == category]
    else:
        print("Invalid choice.")
        return

    print("Filtered Expense List:")
    print("----------------------")
    print("ID  Date        Category      Description      Amount")
    print("--------------------------------------------------")
    for expense in filtered_expenses:
        print(
            f"{expense['ID']}   {expense['Date']}  {expense['Category']:13} {expense['Description']:15} {expense['Amount']}")
