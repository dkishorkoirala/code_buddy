"""
Sorting Data Efficiently


Challenge

Create a function named analyze_grades that takes a dictionary of student grades as an argument. The dictionary keys are student names, and the values are their corresponding grades. The function should perform the following operations:

Calculate the average grade of all students.
Find the highest and lowest grades.
Identify the student(s) with the highest and lowest grades.
Return a dictionary containing the following information:
'average': The average grade (rounded to 2 decimal places)
'highest': The highest grade
'lowest': The lowest grade
'top_student': The name of the student with the highest grade
'bottom_student': The name of the student with the lowest grade
Test your function with the following dictionary:

student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
Print the result of the function call.
"""


def analyze_grades(grades):
    d = {}
    lst = list(grades.values())
    d["average"] = sum(lst) / len(lst)
    d["highest"] = max(lst)
    d["lowest"] = min(lst)
    d["top_student"] = max(grades, key=grades.get)
    d["bottom_student"] = min(grades, key=grades.get)

    return d


# Test the function
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95, "Eve": 88}
result = analyze_grades(student_grades)
print(result)
