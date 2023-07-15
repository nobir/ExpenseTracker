def calculate_total_expenses(expense_data):
    
    print("Calculate Total Expenses:")
    print("1. Calculate total for all expenses")
    print("2. Calculate total within a date range")
    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
         # Calculate total expenses for all expenses

        total = sum(expense['Amount'] for expense in expense_data)
         # Sum the 'Amount' field for each expense in expense_data

        print(f"Total Expenses: {total:.2f}")
         # Print the total expenses with two decimal places

    elif choice == 2:
         # Calculate total expenses within a specific date range

        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        total = sum(expense['Amount']
                    for expense in expense_data if start_date <= expense['Date'] <= end_date)
        print(
            f"Total Expenses within {start_date} and {end_date}: {total:.2f}")
    else:
        print("Invalid choice.")
