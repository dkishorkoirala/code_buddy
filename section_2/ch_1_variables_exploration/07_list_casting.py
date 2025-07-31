"""
List Casting

You can use the list() function to cast iterables like tuples, strings, or ranges into lists. This is useful for working with elements in a modifiable format.

Casting a tuple to a list:

my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # [1, 2, 3]
Casting a string splits it into individual characters:

my_string = "hello"
my_list = list(my_string)
print(my_list)  # ['h', 'e', 'l', 'l', 'o']
Casting a range to a list gives all the numbers at once:

my_range = range(5)
my_list = list(my_range)
print(my_list)  # [0, 1, 2, 3, 4]
You can also cast to other types like set or dict, but you’ll explore those later. For now, focus on list() to handle and transform data flexibly!

Challenge

Convert the following data into lists using the list() function:

A tuple: (10, 20, 30)
A string: "python"
A range: range(1, 6)
Print the resulting lists.

Example Output:

[10, 20, 30]
['p', 'y', 't', 'h', 'o', 'n']
[1, 2, 3, 4, 5]
This challenge reinforces using list() to cast different iterables into lists.
"""

# Write code here
t = (10, 20, 30)
s = "python"
r = range(1, 6)
print(list(t))
print(list(s))
print(list(r))
