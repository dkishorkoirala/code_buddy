"""
Iterating Over Strings Part 1


Challenge

Create a program that receives a string as input, and it prints how many times the character s is in the string.

Some chars might be uppercase, use char.lower() to convert it to lowercase.
"""

text = input()
# Write your code below
count = 0
for char in text:
    if char.lower() == "s":
        count += 1
print(count)
