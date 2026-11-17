# Lab 03 – Data Types & Variables

## Overview

This lab demonstrates the fundamentals of Python data types, variables, and type casting using Python 3.12 on Ubuntu 24.04.

The practical exercises cover creating variables, checking their data types, performing implicit and explicit type conversions, and applying these concepts to a customer data intake scenario.

## Objectives

- Understand Python variables and data types.
- Create and manipulate different types of variables.
- Identify data types using the `type()` function.
- Understand implicit type casting.
- Perform explicit type casting using Python conversion functions.
- Apply type conversion to a practical customer data example.

## Environment

| Component | Details |
|---|---|
| Operating System | Ubuntu 24.04 LTS |
| Python Version | 3.12.3 |
| Programming Language | Python |
| Main Script | `vars.py` |

## Lab Tasks

### Task 1 – Understanding and Creating Variables

Created variables using four fundamental Python data types:

| Variable | Value | Data Type |
|---|---|---|
| `name` | John Doe | String (`str`) |
| `age` | 25 | Integer (`int`) |
| `is_student` | True | Boolean (`bool`) |
| `height` | 175.5 | Float (`float`) |

Used `print()` to display variable values and `type()` to identify their data types.

### Task 2 – Implicit and Explicit Type Casting

**Implicit Type Casting**

Python automatically converted an integer into a float during an arithmetic operation.

```python
a = 10
b = 10.5
result = a + b
```

Output:

```text
Result: 20.5 Type: <class 'float'>
```

**Explicit Type Casting**

Used Python conversion functions to manually change data types.

- `str()` converts a value into a string.
- `int()` converts a value into an integer.

Examples:

```python
age_str = str(age)

number_str = "100"
number_int = int(number_str)
```

### Task 3 – Case Study: Customer Data Intake

Created a customer data example containing:

- Customer name: Alice Johnson
- Customer age: 30
- Membership status: True

Converted the customer age from a string into an integer using `int()`.

Converted the membership text into a Boolean using a comparison:

```python
customer_membership = customer_membership == "True"
```

**Important Python concept:**

`bool("False")` returns `True` because a non-empty string is considered truthy in Python.

Output:

```text
bool("False") = True
```

Comparing the string with `"True"` provides the intended Boolean conversion for this example.

## Verification and Testing

The following checks were completed:

| Verification | Result |
|---|---|
| Python installation | Passed |
| Variable creation | Passed |
| Data type identification | Passed |
| Implicit type casting | Passed |
| Explicit type casting | Passed |
| Customer data conversion | Passed |
| Python syntax compilation | Passed |
| Complete script execution | Passed |

Python syntax was checked using:

```bash
python3 -m py_compile vars.py
```

The complete script was executed using:

```bash
python3 vars.py
```

## Repository Structure

```text
Python-Deep-DIve/
└── Lab-03-Data-Types-and-Variables/
    ├── vars.py
    ├── README.md
    └── evidence/
        ├── vars-output.txt
        ├── syntax-check.txt
        └── python-version.txt
```

## Key Learnings

- Variables store values that can be used throughout a Python program.
- Python supports different built-in data types, including strings, integers, floats, and Booleans.
- The `type()` function identifies the data type of a value.
- Implicit casting is performed automatically by Python.
- Explicit casting is performed manually using conversion functions.
- Non-empty strings are truthy, including the string `"False"`.

## Conclusion

Successfully completed the practical exercises for Python Data Types and Variables.

Verified the program output and Python syntax. The exercises provided practical experience with variables, data types, and type conversion in Python 3.12.
