'''Container Magic Methods


Container magic methods allow your classes to behave like built-in containers (lists, dictionaries, etc.). They enable indexing, length checking, and iteration on your custom objects.

Here is an example of a class with container magic methods:

class CustomList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __iter__(self):
        return iter(self.items)
    
    def __contains__(self, item):
        return item in self.items
The __len__ method makes len() work:

my_list = CustomList([1, 2, 3, 4])
print(len(my_list))  # 4
The __getitem__ method enables indexing for retrieval:

print(my_list[2])    # 3
print(my_list[0])    # 1
The __setitem__ method enables indexing for assignment:

my_list[1] = 10
print(my_list[1])    # 10
The __contains__ method makes the in operator work:

print(3 in my_list)     # True
print(100 in my_list)   # False
The __iter__ method enables iteration:

for item in my_list:
    print(item)
Output:

4
3
1
10
True
False
1
10
3
4
Key Point: Container magic methods like __len__, __getitem__, __setitem__, __iter__, and __contains__ make your custom classes behave like built-in containers. This provides intuitive indexing, iteration, and membership testing for your objects.

Challenge

In this challenge, you'll implement a Deck class that simulates a deck of playing cards with comprehensive functionality and proper Python conventions.

You only need to edit the deck.py file. Follow the TODO comments in the code which guide you through implementing:

A standard 52-card deck initialization (using strings like "2H", "KD", "AS")
Support for Python's built-in operations:
Indexing (deck[0])
Length checking (len(deck))
Iteration (for card in deck)
Membership testing ("AS" in deck)
A shuffle method to randomize card order
'''