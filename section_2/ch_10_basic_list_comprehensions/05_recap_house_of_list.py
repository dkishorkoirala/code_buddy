"""
Recap - House Of Lists


Challenge

Create a function named house_of_lists that takes a list of lists list_of_lists as an argument. Each inner list contains numbers. The function should use list comprehensions to perform the following operations:

Filter out inner lists that have a sum greater than 50.
From the remaining inner lists, extract numbers that are less than 5.
Combine all extracted numbers into a single list.
Return the combined list of numbers.
"""


def house_of_lists(list_of_lists):
    # Write code here
    lst = [l for l in list_of_lists if sum(l) <= 50]
    number = [num for l1 in lst for num in l1 if num < 5]
    return number
