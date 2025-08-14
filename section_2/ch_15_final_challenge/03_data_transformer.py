"""
Data Transformer


Challenge

Create a function named transform_dataset that processes a list of student records for analysis.

Each record is a dictionary containing:

student_id: A unique identifier for the student
grades: A list of numerical grades
subjects: A list of subjects the student is taking
Your function should:

Calculate the average grade for each student
Only include students who have all grades above 70 (qualified students) - you should use Python's all() function to check this condition
Create a summary of the subjects taken by qualified students, counting how many qualified students take each subject
Return a dictionary with two keys:
qualified_students: A dictionary mapping student IDs to their average grade (rounded to 2 decimal places)
subject_summary: A dictionary mapping subjects to the count of qualified students taking that subject
Note: The all() function in Python returns True only if all elements in the iterable are true. For example, all(grade > 70 for grade in grades) will return True only if every grade is above 70.

Example Input:
[
    {
        "student_id": "S123",
        "grades": [88, 92, 85],
        "subjects": ["Math", "Science", "History"]
    },
    {
        "student_id": "S124",
        "grades": [65, 95, 80],
        "subjects": ["Math", "Science", "English"]
    },
    {
        "student_id": "S125",
        "grades": [91, 89, 92],
        "subjects": ["Math", "Physics", "History"]
    }
]
Example Output:
{
    'qualified_students': {'S123': 88.33, 'S125': 90.67},
    'subject_summary': {'Math': 2, 'Science': 1, 'History': 2, 'Physics': 1}
}
"""


def transform_dataset(data):
    qualified_students = {}
    subject_summary = {}

    # Step 1: Filter and calculate averages
    for record in data:
        grades = record["grades"]
        if all(grade > 70 for grade in grades):
            avg_grade = round(sum(grades) / len(grades), 2)
            qualified_students[record["student_id"]] = avg_grade

            # Step 2: Count subjects
            for subject in record["subjects"]:
                subject_summary[subject] = subject_summary.get(subject, 0) + 1

    # Step 3: Return result
    return {
        "qualified_students": qualified_students,
        "subject_summary": subject_summary,
    }
