"""
Recap - Elements Of Freedom


Challenge

Create a function named elements_of_freedom that processes a list of string elements according to specific rules.

Your function should:

Filter out elements that have fewer than 5 characters
Convert the remaining elements to uppercase
Remove any duplicate elements
Return a list of the unique uppercase elements
Use list operations to efficiently process the data.

Example:
Input: ["apple", "banana", "cherry", "date", "apple", "banana", "grape", "fig"]
Output: ['APPLE', 'BANANA', 'CHERRY', 'GRAPE']
"""


def elements_of_freedom(elements):
    filtered = [e.upper() for e in elements if len(e) >= 5]

    # Step 3: Remove duplicates while preserving order
    unique = []
    seen = set()
    for item in filtered:
        if item not in seen:
            unique.append(item)
            seen.add(item)

    return unique
