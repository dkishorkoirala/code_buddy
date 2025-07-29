"""
Accessing List Elements


Challenge

Create a function named sum_elements that receives a list as an argument and prints the sum of all the elements in the list.

To iterate over a list, use the len() function inside the range() function:

my_list = [10, 20, 30, 40, 50]
for i in range(len(my_list)):
        # Access elements using my_list[i]
Use this method to access each element of the list, add them together, and print the total sum.
"""


def sum_elements(lst):
    # Write code here
    sum = 0
    for i in range(len(lst)):
        sum = lst[i] + sum
    print(sum)
