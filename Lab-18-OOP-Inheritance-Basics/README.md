

# Lab 18: OOP – Inheritance Basics

## 1. Introduction

Inheritance is an important concept in Object-Oriented Programming (OOP).

It allows one class to inherit attributes and methods from another class.

In this lab, I created a parent class named `Car` and a child class named `ElectricCar`.

The child class inherits the properties and methods of the parent class and adds its own battery functionality.

## 2. Objectives

- Understand inheritance in Python.
- Create a base class and a subclass.
- Reuse parent class attributes and methods.
- Understand the `super()` function.
- Override a method in a subclass.
- Create objects and verify inheritance using assertions.

## 3. Environment

| Component | Details |
|---|---|
| Operating system | Ubuntu |
| Programming language | Python |
| Python version | 3.12.3 |
| Editor | Nano |
| External packages | Not required |

## 4. What is Inheritance?

Inheritance is a feature of OOP that allows a child class to reuse the properties and methods of a parent class.

It helps reduce code duplication and makes programs easier to maintain.

**Example:** An electric car is a type of car. It has normal car properties and additional electric battery information.

## 5. Parent Class

A parent class is also called a base class.

In this lab, `Car` is the parent class.

It contains three attributes:

- `make`
- `model`
- `year`

It also contains the `describe_car()` method.

## 6. Child Class

A child class is also called a subclass.

In this lab, `ElectricCar` is the child class.

```python
class ElectricCar(Car):
    pass
```

The syntax `ElectricCar(Car)` means that `ElectricCar` inherits from `Car`.

## 7. Understanding super()

The `super()` function provides access to methods from the parent class.

In this lab:

```python
super().__init__(make, model, year)
```

This calls the constructor of the parent class and initializes the inherited attributes.

## 8. Additional Attribute

The `ElectricCar` class introduces an additional attribute:

```python
self.battery_size = battery_size
```

The default battery size is 75 kWh.

This attribute belongs to the electric car object.

## 9. Method Overriding

Method overriding happens when a child class defines a method with the same name as a method in its parent class.

In this lab, `ElectricCar` overrides `describe_car()`.

```python
def describe_car(self):
    super().describe_car()
    self.describe_battery()
```

The overridden method first displays the parent car details and then displays the battery information.

## 10. Task 1: Create the Base Class

I created the `Car` class with:

- A constructor (`__init__`).
- `make`, `model`, and `year` attributes.
- A `describe_car()` method.

The base class was tested independently.

Expected output:

```text
2020 Toyota Corolla
```

## 11. Task 2: Create ElectricCar

I created the `ElectricCar` subclass.

It inherits from `Car`, uses `super()` to initialize parent attributes, and adds `battery_size`.

The default battery size is 75 kWh.

## 12. Task 3: Override describe_car()

I added a new `describe_car()` method inside `ElectricCar`.

It calls the parent method through `super()` and then calls `describe_battery()`.

This demonstrates method overriding.

## 13. Task 4: Create and Test an Object

I created an electric car object:

```python
my_tesla = ElectricCar('Tesla', 'Model S', 2022)
```

I tested the object using three assertions:

```python
assert isinstance(my_tesla, Car)
assert my_tesla.battery_size == 75
assert ElectricCar.describe_car is not Car.describe_car
```

These checks verify inheritance, the default battery value, and method overriding.

## 14. Final Python Program

```python
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
```

## 15. Program Output

```text
2022 Tesla Model S
This car has a 75-kWh battery.
All checks passed.
```

## 16. Verification Results

- Python syntax compilation passed.
- Parent class test passed.
- Child class inheritance test passed.
- Parent constructor was called using `super()`.
- Battery attribute was initialized successfully.
- Method overriding was verified.
- All three assertions passed.

## 17. Evidence Files

The `evidence/` folder contains:

| File | Purpose |
|---|---|
| `python-version.txt` | Python version |
| `compile-check.txt` | Syntax compilation result |
| `program-output.txt` | Actual program output |
| `class-structure.txt` | Classes and methods |

## 18. Real-World Applications

Inheritance is useful in many software applications:

- Vehicle management systems.
- Banking applications.
- Employee management systems.
- School management systems.
- Online shopping applications.

For example, a `Vehicle` parent class could be inherited by `Car`, `Truck`, and `Motorcycle` classes.

## 19. Interview Questions

**Q1. What is inheritance?**

Inheritance allows a child class to reuse attributes and methods from a parent class.

**Q2. What is a parent class?**

A parent class is the base class from which another class inherits.

**Q3. What is a child class?**

A child class is a class that inherits from another class.

**Q4. What is `super()`?**

`super()` is used to access methods from the parent class.

**Q5. What is method overriding?**

Method overriding occurs when a child class provides its own implementation of a parent class method.

**Q6. What is the benefit of inheritance?**

It promotes code reuse and reduces duplication.

**Q7. What does `ElectricCar(Car)` mean?**

It means that `ElectricCar` inherits from the `Car` class.

**Q8. What is the purpose of `isinstance()`?**

It checks whether an object is an instance of a particular class or its subclasses.

**Q9. Can a child class have its own attributes?**

Yes. In this lab, `battery_size` is an additional attribute of `ElectricCar`.

**Q10. Can a child class override a parent method?**

Yes. `ElectricCar` overrides `describe_car()`.

## 20. Conclusion

In this lab, I learned how inheritance works in Python.

I created a parent class named `Car` and a child class named `ElectricCar`.

I practiced using `super()`, adding new attributes, and overriding methods.

All required practical checks and assertions passed successfully.

**Lab 18 completed successfully.**
