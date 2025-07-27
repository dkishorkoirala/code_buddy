# Logical Operators Part 3

# In Python, you can combine multiple conditions using logical operators (and, or, not) to create more complex expressions.

# Let's create a condition that checks if a number is both positive and even:

# number = 6
# Now let's check if the number is positive:

# is_positive = number > 0
# Let's also check if the number is even:

# is_even = number % 2 == 0
# We can combine these conditions using the and operator:

# result = is_positive and is_even
# This evaluates to True because 6 is both positive and even.

# For a more direct approach, you can combine conditions without intermediate variables:

# result = number > 0 and number % 2 == 0
# Similarly, you can use the or operator to check if at least one condition is true:

# number = -4
# is_negative_or_odd = number < 0 or number % 2 != 0
# This evaluates to True because -4 is negative (even though it's not odd).


# Challenge

# Write code that checks if a person is eligible to drive. A person is eligible to drive if ALL of the following conditions are met:

# The person is at least 18 years old
# The person has a license
# The person has insurance
# Your program should:

# Read an integer age from the first line of input
# Read a string has_license from the second line of input (either "true" or "false")
# Read a string has_insurance from the third line of input (either "true" or "false")
# Convert the license and insurance inputs to boolean values
# Check all three conditions and store the result in a variable named result
# Print the final result (should be True or False)

age = int(input())
has_license = input().lower() == "true"
has_insurance = input().lower() == "true"

result = (
    (age >= 18) and (has_license) and (has_insurance)
)  # Complete this line to check if all conditions are met

print(result)
