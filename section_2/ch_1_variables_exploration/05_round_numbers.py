"""
Round Numbers

The round() function rounds numbers to the nearest value.

round(number, ndigits)
number: The value to round.
ndigits: Decimal places to keep (optional).
Examples:

print(round(4.567))     # 5
print(round(4.567, 2))  # 4.57
print(round(456.78, -1))  # 460
Python rounds halfway cases to the nearest even number:

print(round(2.5))  # 2
print(round(3.5))  # 4

Challenge

Write a program that:

Takes a number as input from the user (float).
Takes the number of decimal places to round to (integer).
Outputs the rounded number.
"""

# Write code here
num = float(input())
n = int(input())
print(round(num, n))
