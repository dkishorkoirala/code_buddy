"""
Ternary Operator


Challenge

Write a program that takes a float input temperature representing the current temperature in Celsius. Use the ternary operator to determine a warning status based on the temperature:

If the temperature is above 30°C, the warning should be "Hot".
If the temperature is 30°C or below, the warning should be "Normal".
The program should output the determined warning status.
"""

# Write your code here
t = float(input())

r = "Hot" if t > 30 else "Normal"
print(r)
