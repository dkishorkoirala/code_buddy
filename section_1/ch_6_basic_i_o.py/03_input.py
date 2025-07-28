"""
Input

As of now we stored values that we thought about in variables. Programs usually don't work this way. We receive values from an outer source, a user for example.

To get input from a user or the system we need to write:

var = input()
This will store the input in the variable var.

The input is always of type string. For example, if the input is 56 then var will hold the string "56".

Challenge

Write a program that get input from the user (their name), and then outputs Hello, followed by a space and the user's inputted name.

For example, if the user inputs Bob, the expected output is Hello, Bob.

You will need to:

Use input() to get input from the user.
Store the input in a variable.
Print Hello, and the stored variable in the end (add a space after the comma).
"""

# Write code here
name = input()
print(f"Hello, {name}")
