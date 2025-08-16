"""
Class Method Decorator


The @classmethod decorator creates methods that receive the class itself as the first parameter (cls) instead of an instance (self).

Here is an example of a class with class methods:

class Student:
    school_name = "Python Academy"
    student_count = 0

    def __init__(self, name):
        self.name = name
        Student.student_count += 1

    @classmethod
    def get_school_info(cls):
        return f"School: {cls.school_name}, Students: {cls.student_count}"

    @classmethod
    def create_guest_student(cls):
        return cls("Guest")
Call class methods using the class name:

info = Student.get_school_info()
print(info)
Create some students:

alice = Student("Alice")
bob = Student("Bob")

updated_info = Student.get_school_info()
print(updated_info)
Use class methods as alternative constructors:

guest = Student.create_guest_student()
print(guest.name)
print(Student.get_school_info())
Output:

School: Python Academy, Students: 0
School: Python Academy, Students: 2
Guest
School: Python Academy, Students: 3
Class methods can also be called from instances:

alice = Student("Alice")
info_from_instance = alice.get_school_info()
print(info_from_instance)
Output:

School: Python Academy, Students: 1
Key Point: Use @classmethod when you need to access class attributes or create alternative ways to construct objects. The first parameter is cls (the class itself), not self.
"""
