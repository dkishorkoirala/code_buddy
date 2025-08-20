'''Property Decorators Advanced


Advanced property decorators provide more sophisticated control over attribute access, including computed properties, deleters, and full property management.

Here is an example of computed properties that derive values from other attributes:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
Use computed properties like regular attributes:

rect = Rectangle(5, 3)
print(rect.area)      # 15 - calculated automatically
print(rect.perimeter) # 16 - calculated automatically
Create a property with getter, setter, and deleter:

class Temperature:
    def __init__(self):
        self._temp = 0
    
    @property
    def temperature(self):
        return self._temp
    
    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._temp = value
    
    @temperature.deleter
    def temperature(self):
        print("Resetting temperature to 0")
        self._temp = 0
Use the full property functionality:

temp = Temperature()
Use the setter with validation:

temp.temperature = 25
print(temp.temperature)  # 25

# temp.temperature = -300  # Would raise ValueError
Use the deleter:

del temp.temperature
print(temp.temperature)  # 0
Create a more complex example with a game score:

class Player:
    def __init__(self, name):
        self.name = name
        self._score = 0
        self._level = 1
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if value >= 0:
            self._score = value
            self._level = (value // 1000) + 1
        else:
            raise ValueError("Score cannot be negative")
    
    @score.deleter
    def score(self):
        print(f"Resetting {self.name}'s progress")
        self._score = 0
        self._level = 1
    
    @property
    def level(self):
        return self._level

player = Player("Alice")
player.score = 2500
print(f"Score: {player.score}, Level: {player.level}")  # Score: 2500, Level: 3

del player.score
print(f"Score: {player.score}, Level: {player.level}")  # Score: 0, Level: 1
Output:

15
16
25
Resetting temperature to 0
0
Score: 2500, Level: 3
Resetting Alice's progress
Score: 0, Level: 1
Key Point: Advanced property decorators allow computed properties (calculated from other data), property deletion with @property.deleter, and full control over getting, setting, and deleting attributes. This creates intuitive interfaces while maintaining strong data validation and encapsulation.

Challenge


In this challenge, you'll implement a Rectangle class with proper encapsulation and property validation.

rectangle.py - This is the file you need to edit, containing TODO comments to guide your implementation
driver.py - Contains extensive test scenarios (do not modify)
Implement private attributes for _width and _height
Create properties for width and height with validation (must be positive)
Raise appropriate ValueError messages as specified in the TODOs
Implement read-only properties for area and perimeter
Create a dimensions property with getter, setter, and deleter functionality as described in the TODOs
'''
