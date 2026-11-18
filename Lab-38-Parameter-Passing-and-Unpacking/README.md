# Lab 38: Parameter Passing & Unpacking

## 1. Lab Overview

**Topic:** Parameter Passing & Unpacking in Python

**Language:** Python 3.12

**Platform:** Ubuntu Linux

**LMS Result:** 100/100 — Passed

## 2. Learning Objectives

- Understand parameter passing in Python.
- Learn variable positional arguments using `*args`.
- Learn variable keyword arguments using `**kwargs`.
- Understand how to unpack lists and dictionaries.
- Use both unpacking operators in one function call.

## 3. Important Concepts

### A. `*args` — Variable Positional Arguments

- `*args` allows a function to accept multiple positional arguments.
- Python collects these arguments into a tuple.
- We can loop through the values or use built-in functions.

Example:

```python
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
```

### B. `**kwargs` — Variable Keyword Arguments

- `**kwargs` allows a function to accept multiple keyword arguments.
- Python collects these arguments into a dictionary.
- We can access each key and value using `.items()`.

Example:

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### C. List Unpacking with `*`

- The `*` operator unpacks a list or another iterable.
- Each item is passed as a separate positional argument.

Example:

```python
numbers = [1, 2, 3, 4]
sum_numbers(*numbers)
```

### D. Dictionary Unpacking with `**`

- The `**` operator unpacks dictionary key-value pairs.
- Each key becomes a keyword argument.

Example:

```python
data = {'name': 'John', 'age': 25}
print_kwargs(**data)
```

### E. Using Both Operators

A function can accept positional and keyword arguments together.

```python
def describe(*args, **kwargs):
    return len(args), sorted(kwargs)
```

## 4. Practical Tasks Completed

- Task 1: Created functions using `*args`.
- Task 2: Created functions using `**kwargs`.
- Task 3: Practiced list and dictionary unpacking.
- Combined `*args` and `**kwargs` in one function call.
- Verified results using Python assertions.

## 5. Expected Results

```text
add_numbers(1, 2, 3, 4, 5) = 15
--- show_info ---
name: Alice
age: 30
city: New York
sum_numbers(*numbers) = 10
--- print_kwargs(**data) ---
name: John
age: 25
--- show_info(**info) ---
occupation: Engineer
country: USA
describe(*numbers, **info) = (4, ['country', 'occupation'])
All tests passed
```

## 6. Verification

- Python syntax check: Passed
- Practical execution: Passed
- Assertions: Passed
- LMS score: 100/100

## 7. Files Included

- `params.py` — Complete Python practical.
- `evidence/verification.txt` — Python version, LMS result, syntax check and execution output.

## 8. Conclusion

In this lab, I learned how to pass multiple arguments to Python functions using `*args` and `**kwargs`. I also practiced unpacking lists and dictionaries using `*` and `**`.

All practical tests passed successfully, and I achieved **100/100** in the LMS evaluation.
