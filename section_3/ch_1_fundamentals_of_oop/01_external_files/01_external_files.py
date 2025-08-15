'''
External Files


External files let you organize your classes in separate Python files and import them into your main program.

Create a separate Python file called my_class.py

class MyClass:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}"
Import the class into your main file

from my_class import MyClass
Create an instance and use it

obj = MyClass("Alice")
print(obj.greet())
Output:

Hello, I'm Alice
The from my_class import MyClass statement connects the my_class.py file to your program. The first my_class is the filename (without .py), and MyClass is the class name inside that file.

Challenge

You are given Python files (my_class.py and driver.py), add an import statement in the driver.py file to connect the files and use the class from the external file!
'''

'''check 01_02_driver.py and 01_01_myclass.py'''