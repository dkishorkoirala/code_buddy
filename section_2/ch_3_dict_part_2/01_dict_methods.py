"""
Dictionary Methods

Dictionaries, just like lists, come equipped with a variety of built-in methods to perform common operations. These methods can help you manipulate dictionaries more efficiently. Let's explore some of the key methods:

keys(): Returns a view object that displays a list of all the keys in the dictionary.

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
keys = my_dict.keys()
print(keys)
# Output: dict_keys(['name', 'age', 'city'])
values(): Returns a view object that displays a list of all the values in the dictionary.

values = my_dict.values()
print(values)
# Output: dict_values(['Alice', 30, 'New York'])
items(): Returns a view object that displays a list of a dictionary's key-value tuple pairs.

items = my_dict.items()
print(items)
# Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
get(key, default): Returns the value for the specified key. If the key is not found, it returns the default value (or None if no default is specified).

age = my_dict.get('age')
print(age)
# Output: 30

country = my_dict.get('country', 'USA')
print(country)
# Output: USA
pop(key): Removes the element with the specified key and returns its value.

city = my_dict.pop('city')
print(city)
# Output: 'New York'
print(my_dict)
# Output: {'name': 'Alice', 'age': 30}

Challenge

In this challenge, you'll work with a dictionary of student grades to practice essential dictionary operations.

Follow these steps:

Create a dictionary named grades with these initial key-value pairs:
"Alice": 85
"Bob": 90
"Charlie": 78
Print all student names (keys) and grades (values) using dictionary methods.
Add a new student "Diana" with a grade of 92.
Use the get() method to retrieve and print Bob's grade.
Remove "Charlie" from the dictionary using the pop() method and print the updated dictionary.
Ensure your output matches the expected format shown in the example.

Example Output:
Students: dict_keys(['Alice', 'Bob', 'Charlie'])
Grades: dict_values([85, 90, 78])
Bob's grade: 90
Updated grades: {'Alice': 85, 'Bob': 90, 'Diana': 92}

"""

# Step 1: Create the Grades Dictionary
grades = {
    # Add initial student grades here
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
}

# Step 2: Access All Keys and Values
# Print all students and grades
print("Students:", grades.keys())
print("Grades:", grades.values())

# Step 3: Add a New Student
# Add Diana with a grade of 92
grades["Diana"] = 92

# Step 4: Retrieve a Student's Grade
# Get Bob's grade using get() method
print("Bob's grade:", grades.get("Bob", "none"))

# Step 5: Remove a Student
# Remove Charlie using pop() method
# Print the updated dictionary
remove = grades.pop("Charlie")
print("Updated grades:", grades)
