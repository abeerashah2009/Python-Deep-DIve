class Car:
    wheels = 4
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is now driving.")

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.drive()
car2.drive()

print(f"Car 1 brand: {car1.brand}")
print(f"Car 2 brand: {car2.brand}")

assert car1.brand == "Toyota"
assert car2.model == "Civic"

# Accessing the class attribute
print(f"Number of wheels: {Car.wheels}")

assert Car.wheels == 4
assert car1.wheels == car2.wheels == 4
assert car1.brand != car2.brand
