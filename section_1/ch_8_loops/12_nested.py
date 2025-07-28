"""
Nested Loop

A nested loop is a loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.

Let's create a simple nested loop:

# Outer loop
for i in range(3):
    print(f"Outer loop iteration: {i}")

    # Inner loop
    for j in range(2):
        print(f"  Inner loop iteration: {j}")
When you run this code, you'll see:

Outer loop iteration: 0
  Inner loop iteration: 0
  Inner loop iteration: 1
Outer loop iteration: 1
  Inner loop iteration: 0
  Inner loop iteration: 1
Outer loop iteration: 2
  Inner loop iteration: 0
  Inner loop iteration: 1
Notice that for each iteration of the outer loop, the inner loop completes all of its iterations.

Challenge

Write a function named print_pattern that prints a rectangle pattern of stars (*).

The function should:

Take two parameters: rows and cols (both integers)
Use nested loops to print a rectangle with the given dimensions
Each row should contain cols stars
The pattern should have rows rows in total
Example output for print_pattern(3, 4):

****
****
****
"""


def print_pattern(rows, cols):
    # Write your code here
    for i in range(rows):
        print()
        for j in range(cols):
            print("*", end="")


# Get input for rows and columns
rows = int(input())
cols = int(input())

# Call the function
print_pattern(rows, cols)
