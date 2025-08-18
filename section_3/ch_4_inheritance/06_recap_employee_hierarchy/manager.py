from employee import Employee


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def calculate_paycheck(self):
        return self.salary * 1.2 / 12

    def manage_team(self):
        return f"Managing the {self.department} department."
