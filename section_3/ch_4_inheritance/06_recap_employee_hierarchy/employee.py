from person import Person


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def introduce(self):
        return super().introduce() + f" I work with employee ID {self.employee_id}."

    def calculate_paycheck(self):
        return self.salary / 12
