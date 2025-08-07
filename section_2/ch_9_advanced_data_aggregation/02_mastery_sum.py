"""
Using Sum


Challenge

Easy
Create a function named calculate_average_score that takes a list of scores as an argument. The function should calculate and return the average of these scores. If the list is empty, the function should return 0.

Use the sum() function to calculate the total of all scores, and len() to get the number of scores. Remember to handle the case where the list might be empty to avoid division by zero."""


def calculate_average_score(scores):
    # Write code here
    if not scores:
        return 0
    else:
        total = sum(scores)
        avg = total / len(scores)
        return avg
