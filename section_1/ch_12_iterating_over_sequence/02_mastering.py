"""
Iterating Over Elements

Challenge

Create a program that receives a list of numbers as input (given), and prints the sum of all even numbers in the list.
"""

numbers = input().split(",")
# Write your code below
add = 0
for i in range(len(numbers)):
    if int(numbers[i]) % 2 == 0:
        add += int(numbers[i])
print(add)
