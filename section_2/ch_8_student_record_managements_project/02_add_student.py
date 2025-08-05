"""
Add Student


Challenge

Create a function named add_student that takes three arguments: name (string), age (integer), and courses (a list of strings). The function should:

Check if the student name already exists in the student_records dictionary. If it does, print "Student '<name>' already exists.".
If the name does not exist, add it to student_records with age, an empty set for grades, and a set of courses.
Print "Student '<name>' added successfully.".
Add the following block of code at the bottom of your code:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
print(student_records)
"""

student_records = {}


def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {
            "age": age,
            "grades": set(),
            "courses": set(courses),
        }
        print(f"Student '{name}' added successfully.")


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
print(student_records)
