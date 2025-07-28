"""
Input


Challenge

Create a program that receives that user's name and age, then calculates and prints how old they will be in 10 years.

The output should be in the format: "In 10 years, [name] will be [age] years old."

You will need to:

Use input() to get the user's name and age.
Store the inputs in variables.
Convert the age to an integer and add 10 to it.
Print the result using an f-string.

"""

name = input()
age = int(input())
# Write code here
print(f"In 10 years, {name} will be {age + 10} years old.")
