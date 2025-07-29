"""
List Methods

Lists are packed with many methods (functionalities). To access a method, write:

some_list.method()
Here is a list of the basic methods:

append(element) - adds an element to the end of the list
clear() - removes all elements from the list
pop(index) - removes an element at the specified index
reverse() - reverses the order of the list
sort() - sorts the list in ascending order
Here is an example of how to use the append method:

my_list = ["orange", "banana", "apple"]
my_list.append("strawberry")
print(my_list)
This will output ["orange", "banana", "apple", "strawberry"].

Example of the clear method:

my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)
This will output [].

Example of the sort method:

my_list = [1, 9, 2, 3]
my_list.sort()
print(my_list)
This will output [1, 2, 3, 9].

Challenge

Create a function named merge that receives two lists as arguments. The function merges the two lists into one sorted list and returns it.

For example the following arguments: merge([1, 4, 2], [2, 5, 9]) will return [1, 2, 2, 4, 5, 9]
"""


def merge(lst1, lst2):
    # Write code here
    new_list = []
    for i in range(len(lst1)):
        new_list.append(lst1[i])

    for j in range(len(lst2)):
        new_list.append(lst2[j])

    new_list.sort()
    print(new_list)
