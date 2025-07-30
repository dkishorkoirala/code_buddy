"""
Pattern Finder


Challenge

Create a function named find_occurrences that:

Takes two string arguments: text and pattern
Counts how many times pattern appears in text, including overlapping occurrences
Returns a tuple containing:
A boolean indicating if the pattern was found (True/False)
The number of occurrences of the pattern
A list of starting positions where the pattern was found
For example, if text is "abababab" and pattern is "aba", your function should return (True, 3, [0, 2, 4]), since "aba" appears at positions 0, 2, and 4.

If the pattern is not found, return (False, 0, []).
"""


def find_occurrences(text, pattern):
    # Write your code here
    count = 0
    positions = []
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[i : i + m] == pattern:
            positions.append(i)
            count += 1
    found = count > 0
    return (found, count, positions)


# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)
