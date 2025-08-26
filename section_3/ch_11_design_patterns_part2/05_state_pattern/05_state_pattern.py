"""State Pattern


The State Pattern allows an object to change its behavior when its internal state changes. The object appears to change its class based on its current state.

Here are simple state classes for a traffic light:

class RedState:
    def next_state(self, light):
        print("Red -> Green")
        light.state = GreenState()

    def current_color(self):
        return "Red"

class GreenState:
    def next_state(self, light):
        print("Green -> Yellow")
        light.state = YellowState()

    def current_color(self):
        return "Green"

class YellowState:
    def next_state(self, light):
        print("Yellow -> Red")
        light.state = RedState()

    def current_color(self):
        return "Yellow"
Each state defines what happens when transitioning to the next state.

Create a context class that holds the current state:

class TrafficLight:
    def __init__(self):
        self.state = RedState()  # Start with red

    def change(self):
        self.state.next_state(self)

    def get_color(self):
        return self.state.current_color()
The traffic light delegates behavior to its current state object.

Use the traffic light:

light = TrafficLight()
print(f"Current: {light.get_color()}")

light.change()  # Red -> Green
print(f"Current: {light.get_color()}")

light.change()  # Green -> Yellow
print(f"Current: {light.get_color()}")

light.change()  # Yellow -> Red
print(f"Current: {light.get_color()}")
Create another example with a simple player:

class PlayingState:
    def play(self, player):
        print("Already playing")

    def stop(self, player):
        print("Stopping music")
        player.state = StoppedState()

class StoppedState:
    def play(self, player):
        print("Starting music")
        player.state = PlayingState()

    def stop(self, player):
        print("Already stopped")

class MusicPlayer:
    def __init__(self):
        self.state = StoppedState()

    def play(self):
        self.state.play(self)

    def stop(self):
        self.state.stop(self)

player = MusicPlayer()
player.play()   # Starting music
player.play()   # Already playing
player.stop()   # Stopping music
player.stop()   # Already stopped
Output:

Current: Red
Red -> Green
Current: Green
Green -> Yellow
Current: Yellow
Yellow -> Red
Current: Red
Starting music
Already playing
Stopping music
Already stopped
Key Point: The State Pattern encapsulates state-specific behavior in separate classes and lets the context object delegate to the current state. When the state changes, the behavior changes automatically. This eliminates complex if/else statements and makes adding new states easier.


Challenge

In this challenge, you'll implement the State class in state.py with proper encapsulation and methods. The file contains detailed TODO comments to guide your implementation step-by-step.

The test suite is designed to verify your implementation meets all requirements and handles exceptional conditions correctly. Use the test results to understand expected behavior and refine your solution.
"""
