# Logical Operators Part 4


# Challenge

# You're helping a transportation company create a system to determine if a person can drive certain vehicles.

# Initialize the following variables:

# has_license with the value True
# has_experience with the value False
# has_clean_record with the value True
# Write the following logical expressions to determine if:

# can_drive_car: Person needs a license AND a clean record
# can_drive_truck: Person needs a license AND experience AND a clean record
# cannot_drive_any: Person has NO license OR NO clean record

# Initialize variables
has_license = True
has_experience = False
has_clean_record = True

# Calculate conditions
can_drive_car = has_license and has_clean_record
can_drive_truck = has_license and has_experience and has_clean_record
cannot_drive_any = not has_license or not has_clean_record

# Don't delete the lines below
print("Can drive car:", can_drive_car)
print("Can drive truck:", can_drive_truck)
print("Cannot drive any:", cannot_drive_any)
