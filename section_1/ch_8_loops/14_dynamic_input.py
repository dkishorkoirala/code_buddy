"""
Recap - Dynamic Input

Let's get dynamic number of input values!


Challenge


Write a program that gets a dynamic number of input values.

The first input is a number that represents the number of the input values following it. The next input values are whole numbers.

In the end, print the sum of all the input numbers (not including the first input).



For example,

Input:

3
1
5
6
Expected output: 12

Explanation:

 1 + 5 + 6 = 12, and there are exactly 3 numbers following the first input number (3).
"""

how_much = int(input())
result = 0
for i in range(how_much):
    values = int(input())

    result += values
print(result)
