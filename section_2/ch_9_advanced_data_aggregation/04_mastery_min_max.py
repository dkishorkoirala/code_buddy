"""
Finding Minimum and Maximum


Challenge


You are given two lists: temperatures containing daily temperatures in Fahrenheit, and humidity containing daily humidity percentages. Your task is to write a program that:

Finds and prints the highest and lowest temperature from the temperatures list using max() and min().
Finds and prints the highest and lowest humidity from the humidity list using max() and min().
Check the test cases for output format
"""

temperatures = [72, 68, 75, 80, 65, 70, 78]
humidity = [60, 55, 65, 70, 50, 58, 62]

# Write code here
hig = max(temperatures)
low = min(temperatures)

h = max(humidity)
l = min(humidity)

print(f"Highest temperature: {hig}°F")
print(f"Lowest temperature: {low}°F")
print(f"Highest humidity: {h}%")
print(f"Lowest humidity: {l}%")
