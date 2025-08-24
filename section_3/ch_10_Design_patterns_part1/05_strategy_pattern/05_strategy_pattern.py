"""Strategy Pattern


The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. You can switch algorithms at runtime without changing the client code.

Here are simple strategy classes for different payment methods:

class CreditCard:
    def pay(self, amount):
        return f"Paid ${amount} with Credit Card"

class PayPal:
    def pay(self, amount):
        return f"Paid ${amount} with PayPal"

class Bitcoin:
    def pay(self, amount):
        return f"Paid ${amount} with Bitcoin"
Each strategy implements the same method (pay) but with different behavior.

Create a context class that uses strategies:

class ShoppingCart:
    def __init__(self):
        self.total = 0
        self.payment_strategy = None

    def add_item(self, price):
        self.total += price

    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy

    def checkout(self):
        return self.payment_strategy.pay(self.total)
The context class can switch between different payment strategies.

Use the strategy pattern:

cart = ShoppingCart()
cart.add_item(50)
cart.add_item(30)

# Use credit card strategy
cart.set_payment_strategy(CreditCard())
print(cart.checkout())

# Switch to PayPal strategy
cart.set_payment_strategy(PayPal())
print(cart.checkout())
Create another example with sorting strategies:

class BubbleSort:
    def sort(self, data):
        return f"Bubble sorted: {sorted(data)}"

class QuickSort:
    def sort(self, data):
        return f"Quick sorted: {sorted(data)}"

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)

# Use different sorting strategies
numbers = [3, 1, 4, 1, 5]

sorter = Sorter(BubbleSort())
print(sorter.sort_data(numbers))

sorter.set_strategy(QuickSort())
print(sorter.sort_data(numbers))
Output:

Paid $80 with Credit Card
Paid $80 with PayPal
Bubble sorted: [1, 1, 3, 4, 5]
Quick sorted: [1, 1, 3, 4, 5]
Key Point: The Strategy Pattern lets you swap algorithms at runtime. Define different strategies with the same interface, then let the context class choose which one to use. This makes your code flexible and easy to extend with new algorithms without changing existing code.

Challenge

Implement a new BitcoinPayment strategy for our shopping system.

Your task is to:

Create a BitcoinPayment class that implements PaymentStrategy
It should accept a wallet_address in the constructor
The pay method should print exactly: Paying $X using Bitcoin wallet: Y where X is the amount and Y is the wallet address
The pay method should return True after printing
Write a main function that:
Creates a shopping cart
Adds a laptop costing $1200 and headphones costing $100 to the cart
Creates a BitcoinPayment with the wallet address "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
Sets this payment strategy on the cart
Calls the checkout method
Follow the same structure as shown in the lesson examples. Don't forget to add the conditional if __name__ == "__main__": to call your main function.
"""

from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paying ${amount} using Credit Card: {self.card_number}")
        return True


class PayPalPayment(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def pay(self, amount):
        print(f"Paying ${amount} using PayPal account: {self.email}")
        return True


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self):
        total = sum(item["price"] for item in self.items)
        if self.payment_strategy:
            return self.payment_strategy.pay(total)
        else:
            raise ValueError("No payment strategy set")


# Create your BitcoinPayment strategy class here
class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Paying ${amount} using Bitcoin wallet: {self.wallet_address}")
        return True


# Create a main function to demonstrate the strategy pattern
def main():
    cart = ShoppingCart()
    cart.add_item("Laptop", 1200)
    cart.add_item("Headphones", 100)

    bitcoin_payment = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    cart.set_payment_strategy(bitcoin_payment)

    cart.checkout()


if __name__ == "__main__":
    main()
