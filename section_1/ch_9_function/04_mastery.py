"""
Arguments


Challenge

Create a program that calculates the area of a rectangle. The program should take two inputs: the length and width of the rectangle.

Define a function that accepts two arguments (length and width), calculates the area of the rectangle (length * width), and prints the result.

After defining the function, prompt the user for the length and width inputs, and then call your function with these inputs.

Remember: Define your function before calling it in your code.
"""


def calculate_area(length, width):
    # Write your code below
    result = length * width
    print(result)


length = float(input())
width = float(input())
# Call the function below
calculate_area(length, width)
