# Scenario: A sensor system streams readings without storing every reading in a list.
def temperature_readings():
    for reading in (24.5, 25.0, 25.8, 26.1):
        yield reading

for value in temperature_readings():
    print("Temperature:", value, "°C")
