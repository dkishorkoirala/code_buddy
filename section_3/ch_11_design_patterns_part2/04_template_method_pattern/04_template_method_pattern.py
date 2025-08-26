'''Template Method Pattern


The Template Method Pattern defines the skeleton of an algorithm in a base class, letting subclasses override specific steps without changing the algorithm's structure.

Here is a base class with a template method:

class DataProcessor:
    def process(self):
        """Template method defining the algorithm structure"""
        self.read_data()
        self.process_data()
        self.save_data()

    def read_data(self):
        print("Reading data...")

    def process_data(self):
        raise NotImplementedError("Subclasses must implement this")

    def save_data(self):
        print("Saving data...")
The template method process() defines the algorithm steps, while process_data() is left for subclasses to implement.

Create concrete classes that implement the abstract method:

class CSVProcessor(DataProcessor):
    def process_data(self):
        print("Processing CSV data")

class JSONProcessor(DataProcessor):
    def process_data(self):
        print("Processing JSON data")
Each concrete class provides its own implementation of the required step.

Use the template method:

csv_processor = CSVProcessor()
csv_processor.process()

print()  # Empty line

json_processor = JSONProcessor()
json_processor.process()
Create another example with a game template:

class Game:
    def play(self):
        """Template method for playing a game"""
        self.start_game()
        self.play_game()
        self.end_game()

    def start_game(self):
        print("Game started!")

    def play_game(self):
        raise NotImplementedError("Define the game rules")

    def end_game(self):
        print("Game ended!")

class Chess(Game):
    def play_game(self):
        print("Playing chess - thinking strategically...")

class Soccer(Game):
    def play_game(self):
        print("Playing soccer - running and kicking...")

chess = Chess()
chess.play()
Output:

Reading data...
Processing CSV data
Saving data...

Reading data...
Processing JSON data
Saving data...
Game started!
Playing chess - thinking strategically...
Game ended!
Key Point: The Template Method Pattern defines a common algorithm structure in the parent class while letting subclasses customize specific steps. The parent class controls the overall flow, but subclasses provide the specific implementations. This ensures consistent structure while allowing flexibility in individual steps.

Challenge


Implement the template.py and driver.py with proper encapsulation and methods. Follow the TODO comments for step-by-step guidance.
'''
