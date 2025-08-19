# TODO: Import PaymentMethod class from paymentmethod.py
from paymentmethod import PaymentMethod
# Use: from paymentmethod import PaymentMethod

class CreditCard(PaymentMethod):
    # TODO: Create __init__ method that accepts card_number parameter
    # and stores it as an instance attribute (self.card_number)
    def __init__(self, card_number):
        self.card_number = card_number
    
    # TODO: Implement process_payment(self, amount) method that:
    # - Returns a string in format: "Processing credit card payment of $[amount]"
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"
    
    # TODO: Implement payment_details(self) method that:
    # - Extracts the last 4 digits of the card number
    # - Masks the rest of the digits with asterisks (*)
    # - Returns a string in format: "Credit Card: [masked_number]"
    # - Example: "1234567890123456" becomes "************3456"
    def payment_details(self):
        result = ((len(self.card_number)-4)*"*")+self.card_number[-4:]
        return f"Credit Card: {result}"
    