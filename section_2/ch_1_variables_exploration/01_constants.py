"""
Constants

In programming, a constant is a type of variable whose value cannot be changed during the execution of a program. Constants are useful for defining values that are used multiple times throughout a program, such as mathematical constants like PI or the number of hours in a day.

In Python, there is no strict enforcement of constants like in some other languages (such as c++). However, there is a widely adopted convention to indicate that a variable should be treated as a constant. This is done by writing the variable name in all uppercase letters, often with underscores to separate words. For example:

PI = 3.14159
HOURS_IN_A_DAY = 24
MAX_USERS = 100
When you see variables named this way in Python code, it's a signal that these values should not be altered. This convention helps make the code more readable and maintainable. It's important to note that this is just a naming convention; the Python interpreter itself does not prevent you from changing the value of these variables.

Challenge

Create a Python program that calculates the area of a circle using a constant for the value of PI. Define a constant named PI and set its value to 3.14159. Then, prompt the user to enter the radius of the circle. Calculate the area of the circle using the formula (area = PI * radius**2) and print the result.

Remember to follow the naming convention for constants by using all uppercase letters for the variable PI.
"""

# Write code here
PI = 3.14159


def area(radius):
    return f"{PI * radius**2}"


r = float(input())
print(area(r))
