def add_expense(expense_data, categories):
    print("Enter expense details:")
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    description = input("Description: ")
    amount = float(input("Amount: "))

    # Validate input
    if amount < 0:
        print("Invalid amount. Expense not added.")
        return

    # Check if category exists, add if it doesn't
    if category not in categories:
        categories.append(category)

    expense = {
        'ID': len(expense_data) + 1,
        'Date': date,
        'Category': category,
        'Description': description,
        'Amount': amount
    }
    expense_data.append(expense)
    print("Expense added successfully!")
