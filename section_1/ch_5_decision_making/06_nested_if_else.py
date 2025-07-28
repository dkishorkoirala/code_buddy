# Nested If - Else

# Nested If-Else statements allow you to check multiple conditions by placing one if-else statement inside another.

# Create a basic if-else statement:

# age = 18
# title = "None"
# if age >= 18:
#     title = "Adult"
# else:
#     title = "Minor"
# Now let's add a nested condition inside:

# age = 18
# title = "None"
# allowed_to_drink = False
# if age >= 18:
#     title = "Adult"
#     if age >= 21:
#         allowed_to_drink = True
#     else:
#         allowed_to_drink = False
# else:
#     title = "Minor"
# In this example, the second if-else only executes when the first condition is True.


# Challenge

# Write a program that determines eligibility for a movie based on age and parental guidance.

# Your program should:

# Create a variable age and assign it a value from input (given).
# Create a variable with_parent and assign it a True/False value from input (given).
# Create a variable named message with the value of "None" (given).
# Use nested if-else to determine what string to put in message:
# If age is 18 or older, set "You can watch any movie".
# If age is under 18:
# If with_parent is True, set "You can watch PG-13 movies".
# If with_parent is False, set "You can only watch G-rated movies".
# Get age as an integer
age = int(input())

# Get parental guidance as a boolean (True/False)
with_parent = input() == "true"

# Declare a variable named message with "None"
message = "None"

# Write your nested if-else code here
if age >= 18:
    message = "You can watch any movie"
else:
    if age < 18 and with_parent:
        message = "You can watch PG-13 movies"
    elif not with_parent:
        message = "You can only watch G-rated movies"

# Don't change below this line
print(message)
