# Scenario: An e-commerce checkout lets a customer choose a payment strategy.
class CreditCard:
    def pay(self, amount):
        print(f"Credit card payment: Rs.{amount}")

class UPI:
    def pay(self, amount):
        print(f"UPI payment: Rs.{amount}")

class Checkout:
    def __init__(self, strategy):
        self.strategy = strategy

    def complete_payment(self, amount):
        self.strategy.pay(amount)

checkout = Checkout(UPI())
checkout.complete_payment(1250)
