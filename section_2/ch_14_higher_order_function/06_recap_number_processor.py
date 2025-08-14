"""
Recap - Number Processor


Challenge

Create function named process_numbers that takes a list of numbers and processes them according to specific rules.

Requirements:

First filter out all negative numbers and zero
Then for the remaining positive numbers:
Double even numbers
Triple odd numbers
Use map() and filter() to solve the problem.
"""


def process_numbers(numbers):
    # Write your code below
    filtered = list(filter((lambda x: x > 0), numbers))

    processed_numbers = map(lambda x: x * 2 if x % 2 == 0 else x * 3, filtered)
    return list(processed_numbers)
