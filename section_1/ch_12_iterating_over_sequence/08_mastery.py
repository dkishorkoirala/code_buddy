"""
Iterating Over Strings Part 2


Challenge

Create a program that takes two inputs: a string of numbers separated by spaces, and a prefix string. The program should split the number string into individual numbers, add the prefix to each number, then join these modified numbers back into a single string separated by spaces. Finally, print the resulting string.
"""

numbers = input()
prefix = input()
# Write your code below
a = numbers.split()
result_nums = []

for i in a:
    result_nums.append(prefix + i)

b = " ".join(result_nums)
print(b)
