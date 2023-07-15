def add_category(categories):
    while True:
        category = input("Enter the new category: ")

        # Validation rules
        if not category:
            print("Category cannot be empty. Please enter a category.")
        elif len(category) < 3:
            print("Category must be at least 3 characters long.")
        elif category in categories:
            print("Category added successfully!")
            break
        else:
            categories.append(category)
            print("Category added successfully!")
            break
