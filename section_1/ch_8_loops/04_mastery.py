"""
While Loop


Challenge

Write a program that gets one input, float number.

Use a while loop to divide the input by 3 as long as the number is bigger or equal to 2.5.

Print the first number that is smaller than 2.5.
"""

number = float(input())
# Write your code below

while number >= 2.5:
    number = number / 3

print(number)
