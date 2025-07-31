"""
Nested Dictionaries

A nested dictionary is a dictionary within a dictionary. It allows you to organize complex data structures, making it easier to work with related information.

Example:

students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"}
}

# Accessing a nested value
print(students["Alice"]["age"])  # Output: 20

# Adding a new key-value pair to a nested dictionary
students["Alice"]["major"] = "Math"
print(students["Alice"])  # Output: {'age': 20, 'grade': 'A', 'major': 'Math'}
Nested dictionaries are useful when you need to group related information together, such as storing details about students, employees, or products.
"""
