"""
Iterating Over Strings Part 1

Similar to lists, you can iterate over strings:

text = "Hey"
for char in text:
    print(char)
Output:

H
e
y
Using index:

for i in range(len(text)):
    print(f"position {i}: {text[i]}")
Output:

position 0: H
position 1: e
position 2: y

Challenge

Create a program that receives a string as input, and it prints how many times the character p (or P) is in the string.

Some chars might be uppercase, use char.lower() to convert it to lowercase.
"""

text = input()
# Write your code below
counter = 0
for char in range(len(text)):
    if text[char] == "p" or text[char] == "P":
        counter += 1

print(counter)
