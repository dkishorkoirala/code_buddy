"""
Average Grade


Challenge

Create a function named calculate_average_grade that takes one argument: name (string). The function should:

Check if the student name exists in the student_records dictionary.
If it does not exist, print "Student '<name>' not found." and return None.
If the name exists, calculate the average of the grades in the student's grades set.
If the grades set is empty, return 0.
Otherwise, calculate and return the average grade as a float.
Add (replace) the following block of code at the bottom of your code:

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
print(calculate_average_grade("Alice"))  # Should return 87.5
print(calculate_average_grade("Bob"))  # Should return 75.0
print(calculate_average_grade("Charlie"))  # Non-existent student, should print message and return None
print(calculate_average_grade("Alice"))  # Should return 87.5 again

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


def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")


def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False

    return course in student_records[name]["courses"]


def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None

    grades = student_records[name]["grades"]
    if not grades:
        return 0
    return sum(grades) / len(grades)


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
print(calculate_average_grade("Alice"))  # Should return 87.5
print(calculate_average_grade("Bob"))  # Should return 75.0
print(
    calculate_average_grade("Charlie")
)  # Non-existent student, should print message and return None
print(calculate_average_grade("Alice"))  # Should return 87.5 again
