import csv


def export_expense_data(expense_data):
    file_name = input("Enter the file name to export (e.g., expenses.csv): ")
    field_names = ['ID', 'Date', 'Category', 'Description', 'Amount']
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(expense_data)
    print(f"Expense data exported to {file_name} successfully!")
