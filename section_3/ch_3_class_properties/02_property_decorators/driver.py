# TODO: Import the Temperature class from the temperature module
from temperature import Temperature

# Test the class:
# TODO: Create a temperature instance at 25°C
temp = Temperature(25)
# Replace with actual Temperature instance

# TODO: Print both Celsius and Fahrenheit values
print(f"{temp.celsius}°C is {temp.fahrenheit}°F")

# TODO: Use the format: "25.0°C is 77.0°F"
temp.fahrenheit = 98.6

# TODO: Set the temperature to 98.6°F

# TODO: Print both values again to confirm the conversion works
# TODO: Use the same format as before
print(f"{temp.celsius}°C is {temp.fahrenheit}°F")

# TODO: Uncomment the line below to test invalid temperature handling
# temp.celsius = -300
