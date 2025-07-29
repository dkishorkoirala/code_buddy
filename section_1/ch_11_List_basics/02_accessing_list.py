"""
Accessing List Elements

In Python, we use lists to store multiple values in a single variable. Each value in a list is called an element, and each element has an index. The indices start from 0 to the length of the list minus one. For example take a look at the next list:

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
Element a is at index 0
Element b is at index 1
...
Element g is at index 6
To access an element of a list, we can use its index within square brackets. For example, to access the first element of a list named my_list, we would use my_list[0].

Here's an example:

my_list = [10, 20, 30, 40, 50]
element = my_list[2]
The variable element will hold the value 30 because it access the third element (which has an index of 2).

Challenge

Create a function named values that receives a list as an argument and prints all of the items in the list one after the other.

To iterate over a list use the len() function inside the range() function:

my_list = [10, 20, 30, 40, 50]
for i in range(len(my_list)):
        my_list[i]
This way, i will iterate from 0 to len(my_list) (not including) which is exactly all of the list indices.
"""


def values(lst):
    # Write code here
    for i in range(len(lst)):
        print(lst[i])
