"""Composite Pattern


The Composite Pattern treats individual objects and groups of objects uniformly. It creates tree structures where both single items and collections of items share the same interface.

Here are simple components for a file system:

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def display(self):
        return f"File: {self.name} ({self.size}KB)"

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item):
        self.children.append(item)

    def get_size(self):
        total = 0
        for child in self.children:
            total += child.get_size()
        return total

    def display(self):
        result = f"Folder: {self.name}"
        for child in self.children:
            result += f"\n  {child.display()}"
        return result
Both files and folders have the same methods (get_size() and display()), so they can be treated uniformly.

Build a file system structure:

# Create files
file1 = File("document.txt", 10)
file2 = File("image.jpg", 50)
file3 = File("video.mp4", 200)

# Create folders
documents = Folder("Documents")
media = Folder("Media")
root = Folder("Root")

# Build the tree structure
documents.add(file1)
media.add(file2)
media.add(file3)
root.add(documents)
root.add(media)
Use the composite structure:

print(f"Root size: {root.get_size()}KB")
print(root.display())
Create another example with a menu system:

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def show(self):
        return f"{self.name}: ${self.price}"

class Menu:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get_price(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total

    def show(self):
        result = f"{self.name} Menu:"
        for item in self.items:
            result += f"\n  {item.show()}"
        return result

combo = Menu("Combo")
combo.add(MenuItem("Burger", 8))
combo.add(MenuItem("Fries", 3))
combo.add(MenuItem("Drink", 2))

print(f"Combo price: ${combo.get_price()}")
print(combo.show())
Output:

Root size: 260KB
Folder: Root
  Folder: Documents
    File: document.txt (10KB)
  Folder: Media
    File: image.jpg (50KB)
    File: video.mp4 (200KB)
Combo price: $13
Combo Menu:
  Burger: $8
  Fries: $3
  Drink: $2
Key Point: The Composite Pattern lets you treat individual objects and collections of objects the same way. Both leaves (individual items) and composites (groups) implement the same interface, making it easy to work with tree structures like file systems, menus, or organizational charts.

Challenge

In this challenge, you will implement a file system structure using the Composite design pattern. The Composite pattern allows you to compose objects into tree structures to represent part-whole hierarchies, treating individual objects and compositions of objects uniformly.

The Composite pattern consists of:

Component: An abstract class that defines the common interface for all concrete classes
Leaf: Represents end objects of a composition with no sub-elements
Composite: Defines behavior for components having children and stores child components
You will implement a file system with:

An abstract FileSystemComponent class (Component)
A File class (Leaf)
A Directory class (Composite)
A FileSystem class to manage the overall structure
Implement the abstract base class with appropriate abstract methods
Create concrete implementations for files and directories
Ensure directories can contain both files and other directories
Implement recursive operations like size calculation and display
Add path-based operations for adding, removing, and finding components
Handle error cases appropriately
Ensure proper encapsulation of component properties
"""
