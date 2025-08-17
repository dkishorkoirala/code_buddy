# TODO: Import the Person class from person.py
from person import Person

# TODO: Import the Employee class from employee.py
from employee import Employee


def main():
    # TODO: Create a Person object with name "Alice" and age 30
    person = Person("Alice", 30)

    # TODO: Create an Employee object with name "Bob", age 35, and job "Developer"
    employee = Employee("Bob", 35, "Developer")

    # TODO: Call the introduce() method on the Person object
    person.introduce()
    # Expected output: "Hi, I'm Alice and I'm 30 years old"
    print()
    # TODO: Call the introduce() method on the Employee object
    # Expected output:
    employee.introduce()
    # "Hi, I'm Bob and I'm 35 years old"
    # "I work as a Developer"


if __name__ == "__main__":
    main()
