# Scenario: An organization has general employees and specialized managers.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee: {self.name}, Salary: Rs.{self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def approve_leave(self):
        print(self.name, "can approve leave in", self.department)

m = Manager("Aarav", 65000, "IT")
m.show_details()
m.approve_leave()
