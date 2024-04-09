expenses = []

def add_expense():
    desc = input("Enter expense description: ")
    while True:
        try:
            amt = float(input("Enter expense amount: "))
            if amt <= 0:
                print("Amount must be greater than 0.")
                continue
            expenses.append((desc, amt))
            print("Expense added successfully!")
            break
        except ValueError:
            print("Invalid input, Please enter a valid amount.")

def display_expenses():
    if expenses:
        for i, (desc, amt) in enumerate(expenses, start=1):
            print(f"{i}. {desc}: ${amt}")
    else:
        print("No expenses added.")

def calculate_total():
    total = sum(amt for _, amt in expenses)
    print(f"Total expenses: ${total}")

while True:
    print("\n===== Expense Tracker Menu =====")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_expense()
    elif choice == '2':
        display_expenses()
    elif choice == '3':
        calculate_total()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")

#Sources: https://www.makeuseof.com/python-expense-tracker-build/
#Enumarate: https://www.geeksforgeeks.org/enumerate-in-python/
#Amount: https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/get-started-using-python/variables/