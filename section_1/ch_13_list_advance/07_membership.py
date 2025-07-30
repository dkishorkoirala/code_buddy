"""
Membership

You can check whether an element is in the a list or not (in, not in):

2 in [1, 2]      # True
3 not in [1, 2]  # True
3 in [1, 2]      # False

Challenge

Create a program that receives two lists and prints a new list of all elements that are in the first list but NOT in the second list.
"""

lst1 = input().split(",")
lst2 = input().split(",")
# Write your code below

new_list = []

for item in lst1:
    if item not in lst2:
        new_list.append(item)
print(new_list)
