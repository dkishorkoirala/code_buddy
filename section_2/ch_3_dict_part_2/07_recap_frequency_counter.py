"""
Recap - Frequency Counter


Challenge

Create a function named frequency_counter that takes a list data_list as an argument. The function should count the frequency of each item in the list and return a dictionary where the keys are the unique items from the list and the values are the counts of how many times each item appears.

For example, if the input list is [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], the function should return a dictionary like this:

{1: 1, 2: 2, 3: 3, 4: 4}
"""


def frequency_counter(data_list):
    # Write code here
    d = {}
    for data in data_list:
        if data in d:
            d[data] += 1
        else:
            d[data] = 1

    return d
