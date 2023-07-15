import re


def add_expense(expense_data, categories):
    print("Enter expense details:")


    while True:
        date = input("Date (YYYY-MM-DD): ")

        # Validate date format
        date_regex = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(date_regex, date):
            print("Invalid date format.")
            continue
        else:
            break


    while True:
        category = input("Enter the new category: ")

        # Validation rules
        if not category:
            print("Category cannot be empty. Please enter a category.")
            continue
        elif len(category) < 3:
            print("Category must be at least 3 characters long.")
            continue
        elif category in categories:
            break
        else:
            categories.append(category)
            break


    while True:
        description = input("Description: ")

        # Validate description
        if not description:
            print("Description cannot be empty.")
            continue
        elif len(description) < 5:
            print("Description must be at least 5 characters long.")
            continue
        else:
            break


    while True:
        amount = input("Amount: ")

        # Validate amount
        if not is_numeric_positive_float(amount):
            print("Invalid amount. Amount must be positive numeric")
            continue
        elif float(amount) < 0:
            print("Invalid amount. Amount can't be negative value")
            continue
        else:
            break

    expense = {
        'ID': len(expense_data) + 1,
        'Date': date,
        'Category': category,
        'Description': description,
        'Amount': amount
    }
    expense_data.append(expense)
    print("Expense added successfully!")


def is_numeric_positive_float(string):
    try:
        value = float(string)
        if value >= 0.0:
            return True
        else:
            return False
    except ValueError:
        return False
