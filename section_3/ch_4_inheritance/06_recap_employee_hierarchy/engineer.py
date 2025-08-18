from employee import Employee


class Engineer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def code(self):
        return f"Coding in {self.programming_language}."
