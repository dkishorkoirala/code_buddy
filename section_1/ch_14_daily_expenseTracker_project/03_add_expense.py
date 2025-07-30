"""
Add Expense


Challenge


Handle the option where the user adds an expense (1).

Initialize in the start of the program an empty expenses list
When the user selects 1 as a choice, get another input from the user, a float, and add its value to the expenses list.
After adding, output:
Expense added successfully!
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

    elif choice == 5:
        print(EXIT)
        break
