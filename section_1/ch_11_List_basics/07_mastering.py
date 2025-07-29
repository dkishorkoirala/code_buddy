"""
List Methods


Challenge

Create a function named combine_and_filter that receives 2 arguments:

First argument is a list of numbers
Second argument is an integer threshold value
The function should:

Filter out all numbers that are less than or equal to the threshold value
Sort the remaining numbers
Return the resulting list
For example, calling combine_and_filter([1, 5, 3, 2, 7, 4], 3) should return [4, 5, 7].
"""


def combine_and_filter(lst, threshold):
    # Write code here
    new_lst = []
    for i in range(len(lst)):
        if threshold < lst[i]:
            new_lst.append(lst[i])
    new_lst.sort()
    print(new_lst)
