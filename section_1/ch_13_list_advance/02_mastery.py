"""
List Slicing Part 1


Challenge

Create a program that takes a list and prints:

For lists with 5 or more items: the first two and last two items
For lists with less than 5 items: the first and last item only
"""

input_list = input().split(", ")
# Write your code below

if len(input_list) >= 5:
    first_two = input_list[:2]
    last_two = input_list[-2:]
    final_list = first_two + last_two
    print(final_list)

else:
    first_two = input_list[:1]
    last_two = input_list[-1:]
    final_list = first_two + last_two
    print(final_list)
