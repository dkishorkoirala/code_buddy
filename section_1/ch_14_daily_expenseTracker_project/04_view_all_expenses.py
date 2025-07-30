"""
View All Expenses


Challenge

Handle the option to view all the expenses (2).

If the expenses list is empty, output:

No expenses recorded yet.
Otherwise, output the list in the following format:

Your expenses:
1. 23.1
2. 35.5
3. 99.99
4. 15.2
Assuming the expenses entered before were 23.1, 35.5, 99.99 and 15.2. (In that order!)
"""

MENU = """
Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit"""

EXIT = "Exiting the Daily Expense Tracker. Goodbye!"

print("Welcome to the Daily Expense Tracker!")
print(MENU)
exp = []
while True:
    choice = int(input())

    if choice == 1:
        expense = float(input())
        exp.append(expense)
        print("Expense added successfully!")

    elif choice == 2:
        if not exp:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for k, v in enumerate(exp, start=1):
                print(f"{k}. {v}")

    elif choice == 5:
        print(EXIT)
        break
