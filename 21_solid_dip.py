# Scenario: An order service depends on a payment interface, not a specific provider.
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UpiGateway(PaymentGateway):
    def pay(self, amount):
        print(f"UPI gateway processed Rs.{amount}")

class OrderService:
    def __init__(self, gateway):
        self.gateway = gateway

    def place_order(self, amount):
        self.gateway.pay(amount)

service = OrderService(UpiGateway())
service.place_order(1800)
