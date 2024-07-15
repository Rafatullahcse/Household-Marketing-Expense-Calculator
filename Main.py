import expenses
import calculator


def main():
    tracker = expenses.ExpenseTracker()

    while True:
        print("1. Add Category")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter category name: ")
            tracker.add_category(name)
        elif choice == "2":
            category_name = input("Enter category name: ")
            amount = float(input("Enter expense amount: "))
            category = tracker.get_category(category_name)
            if category:
                category.add_expense(amount)
            else:
                print("Category not found!")
        elif choice == "3":
            print(calculator.generate_summary(tracker))
        elif choice == "4":
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
