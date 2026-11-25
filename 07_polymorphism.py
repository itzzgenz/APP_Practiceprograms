# Scenario: An online store accepts multiple payment types through one interface.
class CardPayment:
    def pay(self, amount):
        print(f"Paid Rs.{amount} using card")

class UpiPayment:
    def pay(self, amount):
        print(f"Paid Rs.{amount} using UPI")

class WalletPayment:
    def pay(self, amount):
        print(f"Paid Rs.{amount} using wallet")

def checkout(payment_method, amount):
    payment_method.pay(amount)

for method in (CardPayment(), UpiPayment(), WalletPayment()):
    checkout(method, 750)
