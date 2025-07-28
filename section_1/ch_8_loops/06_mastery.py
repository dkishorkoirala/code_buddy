"""
Break


Challenge
Write a program that:

Takes two numbers as input
Creates a list of numbers from the first input to the second input (not including)
Finds and prints the first even number greater than 5
Then, in a separate loop, find and print the first number divisible by 7
Output the result in the following format:

First even number greater than 5: [...]
First number divisible by 7: [...]
"""

num1 = int(input())
num2 = int(input())

for i in range(num1, num2):
    if i % 2 == 0 and i > 5:
        print(f"First even number greater than 5: {i}")
        break

for num in range(num1, num2):
    if num % 7 == 0:
        print("First number divisible by 7:", num)
        break
