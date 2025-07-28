"""
Recap - Factorial

Factorial is a mathematical operation.

Factorial of n is the product of all positive integers less than or equal to n.

Examples,

Factorial of 3: 6 = 1 * 2 * 3

Factorial of 6: 720 = 1 * 2 * 3 * 4 * 5 * 6

Factorial of 2: 2 = 1 * 2


Challenge

Write a program that receives one input, an integer, calculates the factorial of the input and prints it.

For example, for input 5, the output should be 120 because 1 * 2 * 3 * 4  * 5 = 120.
"""

num = int(input())

res = 1
for i in range(1, num + 1):
    res = res * i
print(res)
