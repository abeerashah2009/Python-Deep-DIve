

# Lab 17: OOP – Defining Classes

## 1. Introduction

Object-Oriented Programming (OOP) is a programming approach that organizes code using classes and objects.

In Python, a class acts as a blueprint. Objects are created from that class and can store their own data and use its methods.

In this lab, I created a `Car` class and two car objects using Python.

## 2. Objectives

- Understand the basics of Object-Oriented Programming.
- Learn how to define a Python class.
- Understand constructors using `__init__()`.
- Understand the `self` parameter.
- Create and use objects.
- Differentiate between class attributes and instance attributes.
- Use methods to perform actions.

## 3. Environment

| Component | Details |
|---|---|
| Operating system | Ubuntu |
| Programming language | Python |
| Python version | 3.12.3 |
| Editor | Nano |
| External packages | Not required |

## 4. What is OOP?

OOP stands for Object-Oriented Programming.

It is a programming method based on classes and objects.

OOP helps organize code, reuse code, and represent real-world things in programs.

**Example:** A car has properties such as brand and model. It also has actions such as driving.

## 5. What is a Class?

A class is a blueprint used to create objects.

In this lab, `Car` is the class.

```python
class Car:
    pass
```

## 6. What is an Object?

An object is an instance of a class.

For example:

```python
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
```

Here, `car1` and `car2` are two different objects of the same class.

## 7. Understanding __init__()

The `__init__()` method is a special method in Python.

It runs automatically when a new object is created.

It initializes the object's attributes.

```python
def __init__(self, brand, model):
    self.brand = brand
    self.model = model
```

## 8. Understanding self

`self` refers to the current object.

It allows each object to access its own attributes and methods.

For example:

```python
self.brand = brand
self.model = model
```

Each car object can have a different brand and model.

## 9. Instance Attributes

Instance attributes belong to individual objects.

In this lab:

- `brand` is an instance attribute.
- `model` is an instance attribute.

The Toyota object has its own brand and model. The Honda object has its own brand and model.

## 10. Class Attributes

Class attributes are shared through the class.

In this lab:

```python
class Car:
    wheels = 4
```

The `wheels` attribute belongs to the class and can be accessed using:

```python
Car.wheels
car1.wheels
car2.wheels
```

All three return `4` in this example.

## 11. Class Attribute vs Instance Attribute

| Class Attribute | Instance Attribute |
|---|---|
| Defined inside the class | Usually initialized using `self` |
| Shared through the class | Belongs to an individual object |
| Example: `wheels` | Examples: `brand`, `model` |

## 12. Task 1: Define the Car Class

I created a class named `Car`.

It contains:
- A constructor named `__init__()`.
- Two instance attributes: `brand` and `model`.
- A method named `drive()`.

## 13. Task 2: Create Car Objects

I created two objects:

```python
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
```

I called the `drive()` method for both objects and printed their brands.

## 14. Task 3: Add a Class Attribute

I added the class attribute:

```python
wheels = 4
```

I accessed it through the class and both objects.

I also used assertions to verify the class and instance attributes.

## 15. Final Python Program

```python
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
```

## 16. Program Output

```text
The Toyota Corolla is now driving.
The Honda Civic is now driving.
Car 1 brand: Toyota
Car 2 brand: Honda
Number of wheels: 4
```

## 17. Verification

The following checks were completed successfully:

- Python syntax compilation passed.
- Both car objects were created successfully.
- Both `drive()` method calls worked.
- Both instance attribute checks passed.
- Class attribute check passed.
- Both objects accessed the four-wheel class attribute.
- Driving output count was `2`.

## 18. Evidence Files

The `evidence/` folder contains:

| File | Purpose |
|---|---|
| `python-version.txt` | Python version |
| `compile-check.txt` | Syntax compilation result |
| `car-output.txt` | Actual program output |
| `driving-count.txt` | Number of driving messages |

## 19. Real-World Applications

Classes and objects can be used to represent:

- Cars and vehicles.
- Students and teachers.
- Bank accounts.
- Employees.
- Products in an online store.

For example, a `Student` class could store a student's name, roll number, and marks.

## 20. Interview Questions

**Q1. What is OOP?**

OOP is a programming approach based on classes and objects.

**Q2. What is a class?**

A class is a blueprint for creating objects.

**Q3. What is an object?**

An object is an instance of a class.

**Q4. What is `__init__()`?**

It is a special method that initializes an object when it is created.

**Q5. What is `self`?**

`self` refers to the current object.

**Q6. What is an instance attribute?**

An instance attribute belongs to an individual object.

**Q7. What is a class attribute?**

A class attribute is defined inside a class and is shared through the class.

**Q8. What is the difference between a class and an object?**

A class is a blueprint, while an object is an instance created from that blueprint.

**Q9. Can two objects have different instance attributes?**

Yes. For example, the Toyota and Honda objects have different brands and models.

**Q10. How can we access a class attribute?**

We can access it using the class name, such as `Car.wheels`, or through an object, such as `car1.wheels`.

## 21. Conclusion

In this lab, I learned how to define a class and create objects in Python.

I practiced constructors, the `self` parameter, instance attributes, class attributes, and methods.

I successfully created two car objects and verified their behavior using assertions.

**Lab 17 completed successfully.**
