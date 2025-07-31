"""
Round Numbers


Challenge

Create a function named calculate_discount that takes two parameters:

price: The original price of an item (float)
discount_percentage: The discount percentage (float)
The function should:

Calculate the discount amount
Subtract the discount amount from the original price
Round the result to 2 decimal places
Return the final discounted price
For example, if the original price is $100 and the discount is 20%, the function should return $80.00.
"""


def calculate_discount(price, discount_percentage):
    # Write code here
    dis_amt = (discount_percentage / 100) * price
    dis_amt2 = price - dis_amt
    return round(dis_amt2, 2)
