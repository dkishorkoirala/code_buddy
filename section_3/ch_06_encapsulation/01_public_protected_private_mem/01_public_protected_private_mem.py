'''
Public, Protected, Private Mem


Python has three levels of access control for class members: public, protected, and private. These control how attributes and methods can be accessed.

Here is an example of a class with all three access levels:

class BankAccount:
    def __init__(self, owner, balance, account_id):
        self.owner = owner           # Public - accessible anywhere
        self._balance = balance      # Protected - internal use
        self.__account_id = account_id  # Private - class only
    
    def deposit(self, amount):       # Public method
        self._balance += amount
    
    def _calculate_interest(self):   # Protected method
        return self._balance * 0.02
    
    def __validate_transaction(self, amount):  # Private method
        return amount > 0 and amount <= self._balance
Access public members from anywhere:

account = BankAccount("Alice", 1000, "12345")
print(account.owner)        # Alice
account.deposit(500)        # Works fine
Access protected members (single underscore - convention only):

print(account._balance)     # 1500 - works but not recommended
result = account._calculate_interest()  # Works but not recommended
print(result)               # 30.0
Try to access private members (double underscore - name mangled):

# This won't work:
# print(account.__account_id)  # AttributeError

# But this works (name mangling):
print(account._BankAccount__account_id)  # 12345
Create a subclass to show protected vs private access:

class SavingsAccount(BankAccount):
    def show_balance(self):
        return self._balance        # Protected - accessible in subclass
    
    def show_id(self):
        # return self.__account_id  # This won't work - private
        return "Cannot access private member"

savings = SavingsAccount("Bob", 2000, "67890")
print(savings.show_balance())  # 2000
print(savings.show_id())       # Cannot access private member
Output:

Alice
30.0
12345
2000
Cannot access private member
Key Point: Public members have no prefix and are accessible anywhere. Protected members use single underscore (_) and should only be used within the class hierarchy. Private members use double underscore (__) and are name-mangled for stronger privacy. Python's access control is convention-based, not strictly enforced.

Challenge

In this challenge, you'll implement a BankAccount class that demonstrates proper use of public, protected, and private access levels in Python.

bankaccount.py - Contains the class definition with TODO comments guiding your implementation
Follow the TODO comments in bankaccount.py to implement the required functionality
Implement proper access levels (public, protected, private) as specified
Ensure all methods handle edge cases appropriately (negative deposits, etc.)
'''