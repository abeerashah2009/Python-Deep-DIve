# Lab 4: Arithmetic & Expressions

## 1. Overview

In this lab, I learned how to perform basic arithmetic operations using Python.

I explored addition, subtraction, multiplication, division, integer division, modulus, exponentiation, and the `divmod()` function.

I also learned how to handle division by zero using `try` and `except`.

## 2. Objectives

- Understand basic arithmetic operations in Python.
- Perform calculations using Python operators.
- Understand the difference between integer division and float division.
- Learn how to use modulus and exponentiation.
- Use command-line arguments to provide numbers to a Python script.
- Handle division by zero using exception handling.

## 3. Environment

| Item | Details |
|---|---|
| Operating System | Ubuntu 24.04 LTS |
| Python Version | Python 3.12.3 |
| Script Name | arithmetic_operations.py |
| Working Directory | Lab-04-Arithmetic-and-Expressions |

## 4. Task 1: Basic Arithmetic Operations

### Step 1: Create a Working Directory

Command:

```bash
mkdir -p ~/python-lab4 && cd ~/python-lab4
```

For this portfolio, I stored the script inside my GitHub repository:

```text
Python-Deep-DIve/Lab-04-Arithmetic-and-Expressions/
```

### Step 2: Import the sys Module

```python
import sys
```

**Explanation:**

- `sys` is a built-in Python module.
- `sys.argv` allows a script to read command-line arguments.
- It helps provide input values when running a Python program.

### Step 3: Define Two Numbers

```python
number1 = int(sys.argv[1]) if len(sys.argv) > 1 else 17
number2 = int(sys.argv[2]) if len(sys.argv) > 2 else 5
```

**Explanation:**

- `sys.argv[1]` reads the first number.
- `sys.argv[2]` reads the second number.
- `int()` converts the input values into integers.
- If no arguments are provided, Python uses 17 and 5 as default values.

### Step 4: Addition

Operator: `+`

Addition combines two numbers.

Example:

```python
17 + 5 = 22
```

### Step 5: Subtraction

Operator: `-`

Subtraction calculates the difference between two numbers.

Example:

```python
17 - 5 = 12
```

### Step 6: Multiplication

Operator: `*`

Multiplication calculates the product of two numbers.

Example:

```python
17 * 5 = 85
```

### Step 7: Division

Operator: `/`

Division calculates the result of dividing one number by another.

Example:

```python
17 / 5 = 3.4
```

The `/` operator returns a float value.

### Step 8: Integer (Floor) Division

Operator: `//`

Integer division returns the floor of the division result.

Example:

```python
17 // 5 = 3
```

For negative numbers:

```python
-7 // 2 = -4
```

**Important:** Python floor division rounds towards negative infinity, not towards zero.

### Step 9: Modulus

Operator: `%`

Modulus returns the remainder after division.

Example:

```python
17 % 5 = 2
```

For negative numbers:

```python
-7 % 2 = 1
```

### Step 10: divmod() Function

The `divmod()` function returns the quotient and remainder together as a tuple.

Example:

```python
divmod(17, 5)
```

Output:

```text
(3, 2)
```

### Step 11: Exponentiation

Operator: `**`

Exponentiation calculates the power of a number.

Example:

```python
17 ** 5 = 1419857
```

## 5. Task 2: Division by Zero and Exception Handling

Dividing a number by zero raises a `ZeroDivisionError`.

To prevent the program from stopping unexpectedly, Python provides `try` and `except`.

Example:

```python
try:
    print(7 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output:

```text
Cannot divide by zero.
```

In my lab script, I handled division, integer division, modulus, and `divmod()` inside the same exception-handling block.

I also tested an unhandled error:

```bash
python3 -c "print(7 / 0)"
```

Python displayed:

```text
ZeroDivisionError: division by zero
```

## 6. Difference Between Float Division and Integer Division

| Operator | Description | Example | Result |
|---|---|---|---|
| `/` | Float division | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Remainder | `7 % 2` | `1` |

### Checking Data Types

Command:

```bash
python3 -c "print(type(10 / 5), type(10 // 5))"
```

Output:

```text
<class 'float'> <class 'int'>
```

**Key Learning:**

- `/` returns a float.
- `//` returns an integer when both operands are integers.

## 7. Running the Python Script

Run with default values:

```bash
python3 arithmetic_operations.py
```

Run with specific values:

```bash
python3 arithmetic_operations.py 17 5
```

Run with zero as the second number:

```bash
python3 arithmetic_operations.py 7 0
```

Run with negative numbers:

```bash
python3 arithmetic_operations.py -7 2
```

## 8. Verification and Testing

I tested the script using different inputs.

### Test 1: Default Values

Input:

```bash
python3 arithmetic_operations.py
```

Expected output:

```text
Addition: 17 + 5 = 22
Subtraction: 17 - 5 = 12
Multiplication: 17 * 5 = 85
Division: 17 / 5 = 3.4
Integer Division: 17 // 5 = 3
Modulus: 17 % 5 = 2
divmod(17, 5) = (3, 2)
Exponent: 17 ** 5 = 1419857
```

### Test 2: Division by Zero

Input:

```bash
python3 arithmetic_operations.py 7 0
```

Result:

```text
Cannot divide by zero: division, //, % and divmod are undefined.
Exponent: 7 ** 0 = 1
```

### Test 3: Negative Numbers

Input:

```bash
python3 arithmetic_operations.py -7 2
```

Important results:

```text
Division: -7 / 2 = -3.5
Integer Division: -7 // 2 = -4
Modulus: -7 % 2 = 1
divmod(-7, 2) = (-4, 1)
```

### Test 4: Python Data Types

Input:

```bash
python3 -c "print(type(10 / 5), type(10 // 5))"
```

Result:

```text
<class 'float'> <class 'int'>
```

### Test 5: Syntax Verification

Command:

```bash
python3 -m py_compile arithmetic_operations.py
```

Result: No syntax errors were reported.

## 9. Key Concepts Learned

1. **Addition (`+`):** Combines two numbers.
2. **Subtraction (`-`):** Calculates the difference.
3. **Multiplication (`*`):** Calculates the product.
4. **Division (`/`):** Returns a floating-point result.
5. **Floor Division (`//`):** Returns the floor of the division.
6. **Modulus (`%`):** Returns the remainder.
7. **Exponentiation (`**`):** Calculates a number raised to a power.
8. **divmod():** Returns quotient and remainder together.
9. **sys.argv:** Reads command-line arguments.
10. **try/except:** Handles runtime errors such as division by zero.

## 10. Repository Structure

```text
Lab-04-Arithmetic-and-Expressions/
│
├── arithmetic_operations.py
├── README.md
│
└── evidence/
    ├── python-version.txt
    ├── syntax-check.txt
    ├── default-output.txt
    ├── zero-division-output.txt
    └── negative-division-output.txt
```

## 11. Conclusion

In this lab, I learned how to perform arithmetic operations using Python.

I explored the differences between float division and floor division, tested negative numbers, and learned how Python handles division by zero.

I also practised using command-line arguments, the `divmod()` function, and exception handling.

These concepts provide a foundation for writing mathematical calculations and more advanced Python programs.
