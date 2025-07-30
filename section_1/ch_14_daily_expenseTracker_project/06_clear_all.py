"""
Clear All


Challenge

Handle the option to clear all expenses (4).

After you clear the expenses list, output:

All expenses cleared.
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

    elif choice == 3:
        total = 0
        average = 0
        if not exp:
            print("No expenses recorded yet.")
        else:
            for i in exp:
                total += i
                average = total / len(exp)

            print("Total expense:", total)
            print("Average expense:", average)

    elif choice == 4:
        exp.clear()
        print("All expenses cleared.")

    elif choice == 5:
        print(EXIT)
        break
