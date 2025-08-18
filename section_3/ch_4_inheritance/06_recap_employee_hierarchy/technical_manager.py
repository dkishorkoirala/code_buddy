from manager import Manager
from engineer import Engineer
from person import Person


class TechnicalManager(Manager, Engineer):
    def __init__(
        self, name, age, employee_id, salary, department, programming_language
    ):
        # Initialize the Person part
        Person.__init__(self, name, age)
        # Set all other attributes directly
        self.employee_id = employee_id
        self.salary = salary
        self.department = department
        self.programming_language = programming_language
