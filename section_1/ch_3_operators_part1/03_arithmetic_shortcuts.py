"""
Arithmetic Shortcuts

Python created a cool shortcut for self-arithmetic operations.

For example, instead of writing:

a = 5
a = a + 3 # a holds 8
We can simplify it by writing +=:

a = 5
a += 3 # a holds 8
The += operator adds the value 3 to a.

This operation is valid for all arithmetic operations:

Operator	Shortcut
+	+=
-	-=
*	*=
/	/=
%	%=


Challenge

You are given a code with initialization of count. (Don't delete this line!)

Your task is to add the following operations, in this order:

Add 4 to count
Multiply count by 2
Subtract 1 from count
Use the arithmetic shortcuts to do so!
"""

# Type your code below
count = 0
count += 4
count *= 2
count -= 1

# Don't change the line below
print(f"count = {count}")
