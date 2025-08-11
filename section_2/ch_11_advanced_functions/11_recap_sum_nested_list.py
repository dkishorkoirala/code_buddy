"""
Recap - Sum Nested List


Challenge

Write a recursive function named sum_nested that takes a nested list nested_list as an argument. The function should:

Add all the integers in the list, including integers in any sublists.
Return the total sum as an integer.
You can check if an element is a list using isinstance(element, list)

Example Input:

nested_list = [1, [2, 3], [4, [5, 6]], 7]
Example Output:

28
"""


def sum_nested(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            total += sum_nested(element)
        else:
            total += element
    return total
