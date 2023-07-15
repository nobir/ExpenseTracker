def view_expense_list(expense_data):
    print("Expense List:")
    print("-------------")
    print("ID  Date        Category      Description      Amount")
    print("--------------------------------------------------")
    for expense in expense_data:
        print(
            f"{expense['ID']}   {expense['Date']}  {expense['Category']:13} {expense['Description']:15} {expense['Amount']}")

