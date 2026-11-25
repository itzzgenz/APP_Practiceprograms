# Scenario: A hospital creates patient records when a patient is registered.
class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age

    def display(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

patient1 = Patient("P101", "Riya", 21)
patient1.display()
