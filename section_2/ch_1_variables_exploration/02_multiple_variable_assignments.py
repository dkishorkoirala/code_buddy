"""
Multiple Variable Assignments

In Python, you can assign values to multiple variables in a single line. This feature can make your code more concise and readable. Let's explore how to use multiple variable assignments effectively.

Basic Multiple Assignments:

a, b, c = 1, 2, 3
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
Assigning the same value to multiple variables:

x = y = z = 10
print(x)  # Output: 10
print(y)  # Output: 10
print(z)  # Output: 10
Assigning values from a list:

numbers = [4, 5, 6]
a, b, c = numbers
print(a)  # Output: 4
print(b)  # Output: 5
print(c)  # Output: 6

Challenge

Write a Python program that performs the following tasks:

Assign values to three variables name, age, and city in a single line. Set name to "Alice", age to 30, and city to "New York".
Assign the value 100 to three variables x, y, and z in a single line.
Create a list named colors containing the values "red", "green", and "blue". Assign these values to three variables color1, color2, and color3 in a single line.
"""

# Assign values to name, age, and city
name, age, city = "Alice", 30, "New York"

# Assign 100 to x, y, and z
x = y = z = 100

# Create a list of colors and assign them to color1, color2, and color3
colors = ["red", "green", "blue"]
color1, color2, color3 = colors

# Don't change the code below
print(f"Name: {name}, Age: {age}, City: {city}")
print(f"x: {x}, y: {y}, z: {z}")
print(f"Colors: {color1}, {color2}, {color3}")
