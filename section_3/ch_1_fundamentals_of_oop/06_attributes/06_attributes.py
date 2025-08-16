"""
Attributes


Attributes are data or variables that belong to a class or its objects. They store information about the object's state.

There are two types of attributes:

Class attributes - shared by all objects of the class:

class Student:
    school_name = "Python Academy"  # class attribute
Instance attributes - unique to each object:

class Student:
    school_name = "Python Academy"

    def set_info(self, name, age):
        self.name = name    # instance attribute
        self.age = age      # instance attribute
Create student objects and set their individual data:

student1 = Student()
student2 = Student()

student1.set_info("Alice", 20)
student2.set_info("Bob", 22)
Access instance attributes (unique to each object):

print(student1.name)    # Alice
print(student2.name)    # Bob
print(student1.age)     # 20
Access class attributes (same for all objects):

print(student1.school_name)    # Python Academy
print(student2.school_name)    # Python Academy
print(Student.school_name)     # Python Academy
Output:

Alice
Bob
20
Python Academy
Python Academy
Python Academy
Key Difference: Class attributes are shared by all objects, while instance attributes are unique to each object. Use self.attribute_name for instance attributes and just attribute_name for class attributes.
"""
