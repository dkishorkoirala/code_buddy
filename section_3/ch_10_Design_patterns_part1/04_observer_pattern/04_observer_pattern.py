"""Observer Pattern


The Observer Pattern creates a one-to-many relationship where one object (subject) notifies multiple objects (observers) when its state changes.

Here is a simple Subject class that manages observers:

class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)
The subject keeps a list of observers and can notify them all at once.

Create simple observer classes:

class EmailNotifier:
    def update(self, message):
        print(f"Email sent: {message}")

class SMSNotifier:
    def update(self, message):
        print(f"SMS sent: {message}")
Each observer has an update method that gets called when notified.

Use the observer pattern:

# Create subject
news = Subject()

# Create observers
email = EmailNotifier()
sms = SMSNotifier()

# Add observers to subject
news.add_observer(email)
news.add_observer(sms)

# Notify all observers
news.notify("Breaking news: Python is awesome!")
Create a practical example with a stock price tracker:

class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self._price = price
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def set_price(self, price):
        self._price = price
        self.notify()

    def notify(self):
        for observer in self._observers:
            observer.update(self.symbol, self._price)

class Investor:
    def __init__(self, name):
        self.name = name

    def update(self, symbol, price):
        print(f"{self.name} notified: {symbol} is now ${price}")

# Use the stock tracker
apple_stock = Stock("AAPL", 150)

investor1 = Investor("Alice")
investor2 = Investor("Bob")

apple_stock.add_observer(investor1)
apple_stock.add_observer(investor2)

apple_stock.set_price(155)  # Notifies all investors
Output:

Email sent: Breaking news: Python is awesome!
SMS sent: Breaking news: Python is awesome!
Alice notified: AAPL is now $155
Bob notified: AAPL is now $155
Key Point: The Observer Pattern lets one object notify many others automatically when something changes. The subject maintains a list of observers and calls their update method when needed. This is useful for notifications, event systems, and keeping multiple parts of your application synchronized.

Challenge

Implement the Observer Pattern by creating a weather monitoring system. Your task is to:

Create a WeatherStation class that extends the Subject class
Add a private attribute to track the current temperature
Implement set_temperature(temperature) to update the temperature and notify observers
Implement get_temperature() to return the current temperature
Create a WeatherDisplay class that extends the Observer class
Each display should have a name
When notified of a temperature change, it should display a message
The message format for temperature updates should be exactly:

Display [name]: Current temperature is [temperature]C
For example: Display Phone: Current temperature is 25.5C

Your solution should allow multiple displays to observe a single weather station, and displays should be able to be added or removed from the station's notification list.
"""


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)


class Observer:
    def update(self, data):
        pass


# Write your WeatherStation class here
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._current_temperature = 0

    def set_temperature(self, temperature):
        self._current_temperature = temperature
        self.notify(temperature)

    def get_temperature(self):
        return self._current_temperature


# Write your WeatherDisplay class here


class WeatherDisplay(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"Display {self.name}: Current temperature is {temperature}C")
