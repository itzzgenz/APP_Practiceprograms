# Scenario: A weather station notifies subscribed displays when temperature changes.
class WeatherStation:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def set_temperature(self, temperature):
        print("Temperature updated:", temperature)
        for observer in self.observers:
            observer.update(temperature)

class Display:
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"{self.name} display: {temperature}°C")

station = WeatherStation()
station.subscribe(Display("Indoor"))
station.subscribe(Display("Mobile"))
station.set_temperature(29)
