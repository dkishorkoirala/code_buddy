"""
Nested Loop


Challenge

Write a program that finds all pairs of numbers that multiply to give n using numbers from 1 to n.
The program should show all possible combinations, including duplicate pairs in reverse order. For example, both "1 6" and "6 1" should be shown, as they are considered different arrangements of the same pair. Numbers can also be paired with themselves if their product equals n.

For example if n = 12, the output should be:

1 12
2 6
3 4
4 3
6 2
12 1
Because:

1 * 12 = 12
2 * 6 = 12
3 * 4 = 12
4 * 3 = 12
6 * 2 = 12
12 * 1 = 12
"""

n = int(input())
# Write your code below
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j == n:
            print(i, j)
