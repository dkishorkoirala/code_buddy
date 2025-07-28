"""
Calculating The Tip And Total


Challenge


Calculate the total, including the tip, print the result in the end.

Check the hint for help!
"""

print("Bill Split Calculator")

bill_amount = float(input())
tip_percentage = float(input())

result = round(bill_amount + (bill_amount * tip_percentage / 100), 5)
print(result)
