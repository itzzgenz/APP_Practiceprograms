# Scenario: Different delivery services can replace the base delivery service.
class Delivery:
    def deliver(self, order_id):
        return f"Order {order_id} dispatched"

class ExpressDelivery(Delivery):
    def deliver(self, order_id):
        return f"Order {order_id} dispatched by express service"

def dispatch(service, order_id):
    print(service.deliver(order_id))

dispatch(Delivery(), "A101")
dispatch(ExpressDelivery(), "A102")
