def delete_expense(expense_data):

    expense_id = int(input("Enter the expense ID to delete: "))

    for expense in expense_data:
        if expense['ID'] == expense_id:
            # Check if the ID of the current expense matches the expense_id to be deleted

            expense_data.remove(expense)
            # If a match is found, remove the expense from the expense_data list

            print("Expense deleted successfully!")
            return

    print("Expense not found.")
