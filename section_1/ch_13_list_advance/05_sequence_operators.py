"""
Sequence Operators

Python provides several operators that can be used with sequences like lists, strings, and tuples.

Concatenation with the + operator joins two sequences together:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
After executing the above code, combined_list contains:

[1, 2, 3, 4, 5, 6]
Repetition with the * operator repeats a sequence a specified number of times:

numbers = [1, 2, 3]
repeated_numbers = numbers * 3
After executing the above code, repeated_numbers contains:

[1, 2, 3, 1, 2, 3, 1, 2, 3]
These operators work with other sequences too:

# String concatenation
greeting = "Hello" + " " + "World"  # "Hello World"

# String repetition
stars = "*" * 5  # "*****"

Challenge

Create a function named create_pattern that takes two arguments:

A list of numbers (numbers).
An integer (repeats).
The function should:

Concatenate the list with itself (list + list).
Repeat the resulting list repeats times using the * operator.
Return the final pattern.
"""


def create_pattern(numbers, repeats):
    # Write your code here
    newlist = numbers + numbers
    r_new = newlist * repeats
    return r_new
