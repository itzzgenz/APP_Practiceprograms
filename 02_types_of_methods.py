# Scenario: A college portal manages student records and admission rules.
class Student:
    college = "MIT ADT University"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):                    # instance method
        return "Pass" if self.marks >= 40 else "Fail"

    @classmethod
    def change_college(cls, name):       # class method
        cls.college = name

    @staticmethod
    def valid_marks(marks):              # static method
        return 0 <= marks <= 100

s = Student("Anushka", 86)
print("Valid marks:", Student.valid_marks(s.marks))
print("Student:", s.name, "| Result:", s.result())
Student.change_college("MIT ADT Pune")
print("College:", Student.college)
