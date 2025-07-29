"""
The Enumerate Function

The enumerate() function allows you to loop through a sequence (like a list, tuple, or string) while keeping track of the index position of each item.

without enumerate() we would access both the index and the value the following way:

fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
enumerate() is a more elegant way to get both index and value:

fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
Both examples will output:

Index 0: apple
Index 1: banana
Index 2: orange

Challenge

Write a program that receives a list of numbers as input (given), and prints a list of the indices of the numbers that are either below 50 or they are divisible by 5.
"""

lst = list(map(int, input().split(",")))
# Write your code below
indeces = []
for num, value in enumerate(lst):
    if lst[num] < 50 or lst[num] % 5 == 0:
        indeces.append(num)
print(indeces)
