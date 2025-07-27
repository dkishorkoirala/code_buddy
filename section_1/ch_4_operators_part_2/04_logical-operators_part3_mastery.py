# Logical Operators Part 3


# Challenge

# You're helping a weather app determine suitable outdoor activities based on weather conditions. Create a program that uses logical operations to determine if certain activities are possible.

# Initialize the following variables:

# is_sunny with the value True
# temperature with the value 25
# wind_speed with the value 10
# water_temperature with the value 22
# Write the following logical expressions to determine if:

# can_go_hiking: It's sunny AND temperature is above 15°C AND wind speed is below 20 km/h
# can_go_swimming: It's sunny AND temperature is above 20°C AND water temperature is above 18°C
# cannot_go_outside: It's NOT sunny OR temperature is below 10°C OR wind speed is above 30 km/h

# Initialize variables
is_sunny = True
temperature = 25
wind_speed = 10
water_temperature = 22

# Calculate conditions
can_go_hiking = (is_sunny) and (temperature > 15) and (wind_speed < 20)
can_go_swimming = (is_sunny) and (temperature > 20) and (water_temperature > 18)
cannot_go_outside = (not is_sunny) or (temperature < 10) or (wind_speed > 30)

# Don't delete the lines below
print("Can go hiking:", can_go_hiking)
print("Can go swimming:", can_go_swimming)
print("Cannot go outside:", cannot_go_outside)
