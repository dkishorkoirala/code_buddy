"""
The Try and Except Block

The try-except block in Python allows you to handle exceptions and prevent your program from crashing. Code that might raise an exception is placed inside the try block, and the except block handles the error if it occurs.

Here’s the basic structure:

try:
    # Code that might cause an exception
    risky_code()
except ExceptionType:
    # Code to handle the exception
    handle_error()
Example:

try:
    num = int("abc")  # This raises a ValueError
except ValueError:
    print("Invalid input! Please enter a number.")
Output:

Invalid input! Please enter a number.
In this example, instead of crashing, the program catches the ValueError and prints a friendly message. Use try-except to handle specific exceptions and keep your program running smoothly.

Challenge

Write a program that prompts the user to enter a number. Use a try-except block to handle cases where the input is not a valid integer.

If the user enters a valid integer, print "You entered: <number>".
If the user enters an invalid value (e.g., a string or special character), catch the exception and print "Invalid input! Please enter a valid number.".
"""

# Write code here
try:
    num = int(input())
    print(f"You entered: {num}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
