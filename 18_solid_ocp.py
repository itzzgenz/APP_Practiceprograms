# Scenario: A store can add new discount types without changing checkout logic.
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, amount):
        pass

class NoDiscount(Discount):
    def apply(self, amount):
        return amount

class FestivalDiscount(Discount):
    def apply(self, amount):
        return amount * 0.80

def checkout(amount, discount):
    return discount.apply(amount)

print("Festival price: Rs.", checkout(1000, FestivalDiscount()))
