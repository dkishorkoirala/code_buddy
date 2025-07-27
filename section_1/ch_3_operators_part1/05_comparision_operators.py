"""
Comparison Operators

Comparison operators are used to compare between two operands.

Sometimes we need to check whether an operand is greater than, less than, or equal to another operand. The following table shows possible operators for comparison:

Operator	Meaning	Example
==	Equal	1 == 2 returns false
!=	Not Equal	1 != 2 returns true
>	Greater Than	1 > 2 returns false
<	Less Than	1 < 2 returns true
>=	Greater Than or Equal	1 >= 2 returns false
<=	Less Than or Equal	1 <= 2 returns true

The comparison operator returns True if the comparison is true and False otherwise.

For example:

var1 = 13
var2 = 12
var3 = var1 != var2
var3 will hold True because var1 and var2 are not equal

Remember the boolean type,  var3 is a boolean.

Arrow icon

Challenge


Write a script that initializes 2 variables n1 and n2 with the values 8 and 9 (accordingly).

After that initialize another variable n3 that will hold whether n1 is bigger than n2.
"""

# Type your code below
n1 = 8
n2 = 9
n3 = n1 > n2

# Don't change the line below
print(f"n1 = {n1}, n2 = {n2}, n3 = {n3}")
