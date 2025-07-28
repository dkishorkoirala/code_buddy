"""
Formatted Output


Challenge
The last step of this project is to format the output!

For example, for the following input:

100
5
2
Output in the following format:

Bill Split Calculator
Total (including tip): $105.0
Each person pays: $52.5
Note: the output should be exactly the same, so note all the uppercase letters and symbols added!

Keep in mind that when numbers are converted to float type, they will always show at least one decimal place in the output, even for whole numbers. For example, 105 will be displayed as 105.0
"""

print("Bill Split Calculator")

bill_amount = float(input())
tip_percentage = float(input())
users = int(input())

result = bill_amount + ((tip_percentage / 100) * bill_amount)
print(f"Total (including tip): ${result}")
new_result = result / users
print(f"Each person pays: ${new_result}")
