"""The *args


The *args parameter allows a method to accept any number of positional arguments. The asterisk collects all extra positional arguments into a tuple.

Here is an example of a method using *args:

class Calculator:
    def add_numbers(self, *args):
        return sum(args)

    def show_numbers(self, *args):
        for i, num in enumerate(args):
            print(f"Number {i+1}: {num}")
Call the method with different numbers of arguments:

calc = Calculator()
result1 = calc.add_numbers(1, 2, 3)
result2 = calc.add_numbers(10, 20, 30, 40, 50)
print(result1)  # 6
print(result2)  # 150
The *args collects all arguments into a tuple:

calc.show_numbers(5, 10, 15, 20)
Output:

Number 1: 5
Number 2: 10
Number 3: 15
Number 4: 20
Combine regular parameters with *args:

class Logger:
    def log_message(self, level, *messages):
        print(f"[{level}]", end=" ")
        for message in messages:
            print(message, end=" ")
        print()  # New line

logger = Logger()
logger.log_message("INFO", "User", "logged", "in")
logger.log_message("ERROR", "Connection", "failed")
Use *args in constructor methods:

class Team:
    def __init__(self, team_name, *players):
        self.team_name = team_name
        self.players = list(players)

    def show_team(self):
        print(f"Team: {self.team_name}")
        for player in self.players:
            print(f"- {player}")

team = Team("Warriors", "Alice", "Bob", "Charlie", "Diana")
team.show_team()
Output:

6
150
Number 1: 5
Number 2: 10
Number 3: 15
Number 4: 20
[INFO] User logged in
[ERROR] Connection failed
Team: Warriors
- Alice
- Bob
- Charlie
- Diana
You can also unpack arguments when calling methods:

numbers = [1, 2, 3, 4, 5]
result = calc.add_numbers(*numbers)  # Unpacks the list
print(result)  # 15
Key Point: *args collects any number of positional arguments into a tuple. Use it when you don't know how many arguments will be passed to a method. The name args is conventional - you could use any name after the asterisk, but args is the standard.

Challenge

In this challenge, you'll implement a flexible number utility function.

Edit the number_utils.py file to implement the sum_all_numbers function that accepts any number of numeric arguments and returns their sum. The function should:

Return 0 if no arguments are provided
Print "Error: All arguments must be numbers" and return None if any non-numeric arguments are provided
The number_utils.py file contains detailed TODO comments to guide your implementation. Follow these comments carefully to ensure your solution meets all requirements.
"""
