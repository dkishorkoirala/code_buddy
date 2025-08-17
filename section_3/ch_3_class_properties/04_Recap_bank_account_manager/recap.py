"""
Recap - Bank Account Manager



Challenge

Create a complete BankAccount class that demonstrates object-oriented programming concepts including class variables, private attributes, properties, getters, setters, and methods.

1. Create a BankAccount class with:
A class variable interest_rate set to 0.02 (2%)
Private instance attributes for __owner_name and __balance
A constructor that initializes these attributes
2. Implement property getters and setters:
A read-only property owner_name that returns the account owner's name
A property balance with:
A getter that returns the current balance
A setter that validates deposits (rejecting negative amounts)
If validation fails, print: "Balance cannot be negative"
3. Implement methods:
deposit(amount) that:
Adds to the balance if amount is positive
Prints "Deposit amount must be positive" and returns False if amount is not positive
Returns True on success
withdraw(amount) that:
Subtracts from the balance if amount is positive and funds are sufficient
Prints "Withdrawal amount must be positive" and returns False if amount is not positive
Prints "Insufficient funds" and returns False if amount exceeds balance
Returns True on success
apply_interest() that:
Adds interest to the balance based on the class interest rate
Returns the interest amount
display_info() that prints account details in this format:

Account Owner: [owner_name]
Balance: $[balance]
Interest Rate: [interest_rate]%
Output Format Requirements
All validation error messages must be printed exactly as specified
The display_info() method must format the output exactly as shown above
Interest rate should be displayed as a percentage (multiply by 100)
"""
