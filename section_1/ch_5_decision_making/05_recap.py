"""
Recap - Simple Calculator


Challenge
You are given a code which gets as input two numbers n1 and n2 and a character op.

Note: we will learn in next lessons how to get input from the user, currently just don't touch the three first lines.



The possible values for op are '+', '-', '/' and '*'

Your task is to set the variable result based on the conditions:

if op is '+', set result with n1 + n2.
if op is '-', set result with n1 - n2.
if op is '/', set result with n1 / n2.
if op is '*', set result with n1 * n2.
"""

n1 = int(input())  # Don't change this line
n2 = int(input())  # Don't change this line
op = input()  # Don't change this line
result = 0

if op == "+":
    result = n1 + n2
elif op == "-":
    result = n1 - n2
elif op == "/":
    result = n1 / n2
elif op == "*":
    result = n1 * n2


# Don't change the line below
print(f"result = {result}")
