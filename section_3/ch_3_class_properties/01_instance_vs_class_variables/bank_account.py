class BankAccount:
    # TODO: Add class variable interest_rate set to 0.02 (2%)
    interest_rate = 0.02

    def __init__(self, account_holder, balance):
        # TODO: Initialize instance variables:
        self.account_holder = account_holder
        self.balance = balance
        # - account_holder: the name of the account holder
        # - balance: the account balance

    def display_info(self):
        # TODO: Print account information in this exact format:
        print(f"Account: {self.account_holder}")
        # "Account: [account_holder]"
        print(f"Balance: ${self.balance}")
        # "Balance: $[balance]"
        print(f"Interest Rate: {self.interest_rate * 100}%")
        # "Interest Rate: [interest_rate]%"
        # Don't forget to multiply interest_rate by 100 for percentage display
        # Add a blank line after the information
        print()
