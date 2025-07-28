"""
Splitting The Bill

Now we have a working program that calculates the total bill! The missing part is the splitting feature.


Challenge

Add to the program a splitting feature:

It will take an additional number (int) from the user that indicates the number of people splitting the bill. (This will be the third input)
Calculate the amount per person by dividing the total amount by the number of people.
In the end, add another print of the amount per person.
"""

print("Bill Split Calculator")

bill_amount = float(input())
tip_percentage = float(input())
users = int(input())

result = bill_amount + ((tip_percentage / 100) * bill_amount)
print(result)
new_result = result / users
print(new_result)
