"""
Recap - Product List


Challenge

Write a function named prod which gets a list of numbers as argument and returns the product of all the numbers in the list.

Reminder, product is the multiplication of all the numbers, for [1, 2, 3], return 6 = 1 * 2 * 3.

"""


def prod(lst):
    # Write code here
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
    print(product)
