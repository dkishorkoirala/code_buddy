"""
Total And Average


Challenge

Handle the option to calculate the total and average expense (3).

If the expenses list is empty, output:

No expenses recorded yet.
Otherwise, output the list in the following format:

Total expense: 600.0
Average expense: 200.0
Assuming the expenses entered before were 300, 200 and 100. (In that order!)
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
        if exp == []:
            print("No expenses recorded yet.")
        else:
            for i in exp:
                total += i
                average = total / len(exp)

            print("Total expense:", total)
            print("Average expense:", average)

    elif choice == 5:
        print(EXIT)
        break
