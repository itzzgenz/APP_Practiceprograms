# Scenario: A car is composed of an engine; the car owns and uses the engine.
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()

    def start_car(self):
        print(self.model, "-", self.engine.start())

car = Car("City Hatchback")
car.start_car()
