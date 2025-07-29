"""
The Enumerate Function


Challenge

Write a program that receives a list of words as input (given), and prints a list of the indices of the words that are either longer than 3 characters or start with the letter 'a' (case-sensitive).

To check if a string starts with some substring use: str.startswith("substring")
"""

lst = input().split()
# Write your code below
# print(lst)
index_ = []
for index, item in enumerate(lst):
    if len(item) > 3 or item.startswith("a"):
        index_.append(index)
print(index_)
