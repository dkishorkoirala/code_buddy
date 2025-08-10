"""
Recursive Functions Part 1

A recursive function is a function that calls itself to solve smaller instances of a problem. Each recursive call must bring the function closer to a base case, which stops the recursion.

Example: Summing numbers from 1 to n:

def sum_to_n(n):
    if n == 0:  # Base case
        return 0
    return n + sum_to_n(n - 1)  # Recursive step

print(sum_to_n(5))  # Output: 15

Challenge

Write a recursive function named count_down that takes a positive integer n as an argument and prints each number from n down to 0.
"""


def count_down(n):
    # Write code here
    if n < 0:
        return

    print(n)
    return count_down(n - 1)
