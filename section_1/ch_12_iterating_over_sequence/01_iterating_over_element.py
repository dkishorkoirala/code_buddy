"""
Iterating Over Elements

Iteration means going through elements one by one in a sequence. With lists, we can access each element systematically using different methods.

The most common way to iterate through a list is using a for loop:

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
Output:

apple
banana
orange

Challenge

Create a program that receives a list as input (given), and prints a new list containing only the words longer than 5 characters
"""

lst = input().split(",")
# Write your code below
list_ = []
for item in range(len(lst)):
    if len(lst[item]) > 5:
        list_.append(lst[item])
print(list_)
