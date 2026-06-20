def show_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Filter by Category")
    print("5. Monthly Summary")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("Add Expense Selected")

        elif choice == "2":
            print("View Expenses Selected")

        elif choice == "3":
            print("Total Spending Selected")

        elif choice == "4":
            print("Filter by Category Selected")

        elif choice == "5":
            print("Monthly Summary Selected")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")