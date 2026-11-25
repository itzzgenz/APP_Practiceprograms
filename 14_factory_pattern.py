# Scenario: A food delivery app creates different delivery vehicles on demand.
class Bike:
    def deliver(self, order):
        print("Bike delivering order", order)

class Van:
    def deliver(self, order):
        print("Van delivering order", order)

class VehicleFactory:
    @staticmethod
    def create(vehicle_type):
        vehicles = {"bike": Bike, "van": Van}
        if vehicle_type not in vehicles:
            raise ValueError("Unknown vehicle type")
        return vehicles[vehicle_type]()

vehicle = VehicleFactory.create("bike")
vehicle.deliver("ORD-104")
