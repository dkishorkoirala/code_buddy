"""
Methods


Methods are functions that belong to a class. They define the behaviors or actions that objects can perform.

Here is an example of a class with methods:

class Calculator:
    def greet(self):
        print("Hello! I'm a calculator.")

    def add(self, a, b):
        return a + b

    def multiply(self, x, y):
        result = x * y
        print(f"{x} × {y} = {result}")
        return result
Create a calculator object:

my_calc = Calculator()
Call a method that doesn't need parameters:

my_calc.greet()
Call methods with parameters:

sum_result = my_calc.add(5, 3)
print(sum_result)
Call a method that both prints and returns a value:

product = my_calc.multiply(4, 7)
Output:

Hello! I'm a calculator.
8
4 × 7 = 28
Methods can:

Take parameters like add(self, a, b)
Return values like return a + b
Print output directly like print("Hello!")
Do both printing and returning
Key Point: Methods define what your objects can do. Always include self as the first parameter, but don't pass it when calling the method.

Challenge

In this challenge, you'll implement a banking system. You'll create a BankAccount class in one file and use it in another file, demonstrating how to organize your code for better maintainability.

You need to work with two files:

bank_account.py: Where you'll define your BankAccount class
driver.py: Where you'll import the class, create an account, and perform transactions
Create a BankAccount class in bank_account.py with:

A class attribute bank_name set to "Python National Bank"
A method deposit that takes an amount and adds it to the account's balance
A method withdraw that takes an amount and subtracts it from the balance
A method get_balance that returns the current balance
Then in driver.py, import your BankAccount class, create an account, deposit $100, withdraw $30, and print the balance with format: f"Current balance: ${my_account.get_balance()}"
"""
