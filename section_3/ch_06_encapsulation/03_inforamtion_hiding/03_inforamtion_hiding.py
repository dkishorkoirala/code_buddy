'''
Information Hiding


Information hiding restricts direct access to object components, requiring all interactions to occur through well-defined interfaces. This protects internal data from unauthorized access.

Here is an example of a class with different levels of information hiding:

class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner                    # Public - can be accessed directly
        self._balance = initial_balance       # Protected - internal use
        self.__account_number = "ACC123456"   # Private - hidden from outside
Add methods that provide controlled access to hidden data:

class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self._balance = initial_balance
        self.__account_number = "ACC123456"
        
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self._balance
    
    def get_account_info(self):
        # Safe way to show partial private data
        return f"Owner: {self.owner}, Account: ***{self.__account_number[-4:]}"
Use the class through its public interface:

account = BankAccount("Alice", 1000)
Access public data directly:

print(account.owner)  # Alice - public access OK
Use controlled methods for protected data:

print(account.get_balance())  # 1000 - controlled access
account.deposit(500)
print(account.get_balance())  # 1500 - balance changed safely
Try to access hidden data:

print(account.get_account_info())  # Owner: Alice, Account: ***3456
# print(account.__account_number)  # AttributeError - hidden
The private attribute is name-mangled but still technically accessible:

# This works but violates information hiding:
print(account._BankAccount__account_number)  # ACC123456
Output:

Alice
1000
1500
Owner: Alice, Account: ***3456
ACC123456
Key Point: Information hiding protects internal data by making it private or protected, then providing controlled access through public methods. This prevents direct manipulation of sensitive data and ensures data integrity through validation in the access methods.

Challenge

In this challenge, you'll implement a secure messaging system with comprehensive testing to validate your solution.

You need to edit securemessenger.py to implement the SecureMessenger class following information hiding principles. The file contains detailed TODO comments to guide your implementation.

Key requirements include:

Proper encapsulation of credentials and messages
Authentication before allowing message operations
Security monitoring through login attempt tracking
Precise return messages as specified in the TODOs
'''