"""
The Filter Function

The filter() function takes two main things:

A function (which contains instructions for checking each item)
A sequence of items (like a list, or any collection of elements)
It looks at each item in your sequence, one by one, and only keeps the ones that pass the function's test (when the function returns True).

For example:

def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]  # This is just a list of numbers
even_numbers = filter(is_even, numbers)
print(list(even_numbers))
# Output: [2, 4, 6]
What happened here:

We have a list of numbers: [1, 2, 3, 4, 5, 6]
The filter() function takes each number, one at a time
It puts each number through our is_even function
If the function returns True, it keeps that number
If the function returns False, it drops that number
You can think of it like a strainer:

Number 1 goes in → is_even returns False → number dropped
Number 2 goes in → is_even returns True → number kept
Number 3 goes in → is_even returns False → number dropped And so on...
You can also use a quick, one-line function (called lambda) instead of defining a separate function:

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda n: n % 2 == 0, numbers)
print(list(even_numbers))
# Output: [2, 4, 6]
The filter() function works with any collection of items - not just numbers. Here's an example with strings:

words = ["apple", "banana", "cherry", "date"]
long_words = filter(lambda word: len(word) > 5, words)
print(list(long_words))
# Output: ["banana"]

Challenge

Create a function named get_long_strings that takes a list of strings strings as an argument. The function should use the filter() function along with a lambda function to select strings that have a length greater than 5. The function should return a list containing the selected strings.
"""


def get_long_strings(strings):
    # Use filter() with a lambda function to select strings with length greater than 5
    long_strings = filter(lambda x: len(x) > 5, strings)

    # Return the list of selected strings
    return list(long_strings)
