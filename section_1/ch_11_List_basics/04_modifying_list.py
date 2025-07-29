"""
Modifying Lists

In addition to accessing the elements of a list, you can also modify them. To modify a specific element in a list, you can assign a new value to it using its index.

Here's an example:

my_list = ["apple", "banana", "cherry"]
my_list[1] = "orange"
print(my_list)
Output:

["apple", "orange", "cherry"]
banana was changed to an orange

Challenge

Create a function named change_element that receives 3 arguments:

First argument is a list
Second argument is an index
Third argument is a new element
The function will return a modified list by changing the element in an index that is stored in the second argument with the value in the third argument.

For example with the following arguments: change_element([1, 2, 3], 0, 9) the function will return [9, 2, 3]

"""


def change_element(lst, index, new_element):
    # Write code here
    lst[index] = new_element
    print(lst)
