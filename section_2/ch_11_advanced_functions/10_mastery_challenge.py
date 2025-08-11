"""
Recursive Functions Part 2


Challenge
Write a recursive function named sum_digits that takes a positive integer n as an argument and returns the sum of its digits. The function should work as follows:

If n is a single digit (less than 10), return that digit.
Otherwise, return the sum of the last digit of n and the result of sum_digits called with n divided by 10 (integer division).
Example Input:

n = 1234
Example Output:

10
Explanation: 1 + 2 + 3 + 4 = 10

You can use the special operator // to calculate the floor division, for example: 3 // 2 = 1
"""


def sum_digits(n):
    # Write code here
    if n < 10:
        return n

    else:
        return sum_digits(n // 10) + n % 10
