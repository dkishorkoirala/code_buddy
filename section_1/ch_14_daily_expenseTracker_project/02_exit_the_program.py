"""
Exit The Program


Challenge


Now let's create the actual program!

Create an infinite while loop (refer the hint if not sure how to do so)
In each iteration of the loop, get input from the user, this will be the choice (1 - 5 from the menu)
Handle the first case, if the choice is equal to 5, exit the program (loop) and output:
Exiting the Daily Expense Tracker. Goodbye!
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
while True:
    choice = int(input())

    if choice == 5:
        print(EXIT)
        break
