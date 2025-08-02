"""
Identity Checks

In Python, the is and is not operators are used to check the identity of objects. Unlike the == operator, which checks if two variables have the same value, the is operator checks if two variables refer to the exact same object in memory.

Basic usage of is:

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # Output: True
print(a is c)  # Output: False
In this example, a and b refer to the same list object, so a is b returns True. However, a and c are different list objects with the same values, so a is c returns False.

Basic Usage of is not:

x = 5
y = 5
z = 10

print(x is not y)  # Output: False
print(x is not z)  # Output: True
Here, x and y refer to the same integer object (due to Python's optimizations for small integers), so x is not y returns False. x and z are different objects, so x is not z returns True.

Identity checks are particularly useful when you want to determine if two variables are pointing to the same object in memory, rather than just having the same value.

Challenge

Create two variables, list1 and list2, where:

list1 refers to a list [1, 2, 3].
list2 is assigned to the same object.
Use the is operator to check if list1 and list2 refer to the same object.
Use the is not operator to check if list1 and list2 refer to different objects.
Print the results of the checks.
"""

# Write code here
lst1 = [1, 2, 3]
lst2 = lst1

print(lst1 is lst2)
print(lst1 is not lst2)
