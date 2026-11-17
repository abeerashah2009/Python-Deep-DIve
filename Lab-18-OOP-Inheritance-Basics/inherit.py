class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size=75):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def describe_car(self):
        super().describe_car()
        self.describe_battery()


if __name__ == "__main__":
    my_tesla = ElectricCar('Tesla', 'Model S', 2022)
    my_tesla.describe_car()

    assert isinstance(my_tesla, Car)
    assert my_tesla.battery_size == 75
    assert ElectricCar.describe_car is not Car.describe_car
    print("All checks passed.")
