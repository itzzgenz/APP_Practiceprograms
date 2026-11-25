# Scenario: A travel booking system supports different ways of calculating fares.
from abc import ABC, abstractmethod

class Fare(ABC):
    @abstractmethod
    def calculate(self, distance):
        pass

class BusFare(Fare):
    def calculate(self, distance):
        return distance * 2.5

class CabFare(Fare):
    def calculate(self, distance):
        return 50 + distance * 12

for service in (BusFare(), CabFare()):
    print(type(service).__name__, "fare: Rs.", service.calculate(10))
