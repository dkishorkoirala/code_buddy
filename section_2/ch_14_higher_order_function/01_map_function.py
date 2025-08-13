"""
The Map Function

The map() function takes two main things:

A function (which contains instructions for what to do)
A sequence of items (like a list, or any collection of elements)
It then applies that function to each item in your sequence, one by one, and gives you back all the results.

For example:

def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5]  # This is just a list of numbers
squared_numbers = map(square, numbers)
print(list(squared_numbers))
# Output: [1, 4, 9, 16, 25]
What happened here:

We have a list of numbers: [1, 2, 3, 4, 5]
The map() function takes each number, one at a time
It puts each number through our square function
It collects all the results in order
You can think of it like an assembly line:

Number 1 goes in → square function makes it 1
Number 2 goes in → square function makes it 4
Number 3 goes in → square function makes it 9 And so on...
You can also use a lambda function instead of defining a separate function:

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda n: n * n, numbers)
print(list(squared_numbers))
# Output: [1, 4, 9, 16, 25]
The map() function works with any collection of items - not just numbers. It could be strings, or any other type of data you want to process in the same way.

Challenge

Create a function named convert_to_uppercase that takes a list of strings strings as an argument. The function should use the map() function along with a lambda function to convert each string in the list to uppercase. The function should return a list containing the uppercase strings.
"""


def convert_to_uppercase(strings):
    # Use map() with a lambda function to convert strings to uppercase
    uppercase_strings = map(lambda s: s.upper(), strings)

    # Return the list of uppercase strings
    return list(uppercase_strings)
