"""
Recap - Reversed List


Challenge

Write a function named reverse which gets a list of numbers as argument and returns the reversed list.

For example, for [1, 2, 3], the expected output is [3, 2, 1].

Don't use the reverse list builtin function!
"""


def reverse(lst):
    # Write code here
    rev = []
    for i in range(len(lst)):
        rev.append(lst[len(lst) - i - 1])

    # rev.reverse()
    print(rev)
