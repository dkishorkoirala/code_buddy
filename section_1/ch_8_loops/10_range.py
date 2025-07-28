"""
The Range Function

The range() function in Python generates a sequence of numbers, which is commonly used with for loops to repeat code a specific number of times.

Create a range that starts at 0 and ends at 4:

for i in range(5):
    print(i)

This will output:

0
1
2
3
4

You can also specify a start value:

for i in range(2, 6):
    print(i)

This will output:

2
3
4
5

And you can specify a step value (increment):

for i in range(1, 10, 2):
    print(i)

This will output:

1
3
5
7
9

Challenge

Create a function named print_range that takes three parameters:

start - the starting number (inclusive)
end - the ending number (exclusive)
step - the increment value
The function should print all numbers from start to end (not including end) with the given step increment, each on a new line.
"""


def print_range(start, end, step):
    # Write your code here
    for i in range(start, end, step):
        print(i)


# Get input from user
start = int(input())
end = int(input())
step = int(input())

# Call the function
print_range(start, end, step)
