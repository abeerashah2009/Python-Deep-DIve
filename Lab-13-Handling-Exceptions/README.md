# Lab 13: Handling Exceptions in Python

## 1. Overview

This lab demonstrates exception handling in Python. Exception handling allows a program to manage errors without stopping unexpectedly.

In this lab, I practised using:

- `try` blocks
- `except` blocks
- `ValueError`
- `ZeroDivisionError`
- `finally` blocks
- User input and integer conversion

## 2. Objectives

- Understand the fundamentals of exception handling.
- Learn how to use `try`, `except`, and `finally`.
- Handle invalid user input.
- Identify different types of exceptions.
- Prevent unexpected program termination when common errors occur.

## 3. Prerequisites

- Basic Python programming knowledge.
- Familiarity with variables and user input.
- Ubuntu Linux terminal.
- Python 3 installed.

## 4. Lab Environment

| Component | Details |
|---|---|
| Operating System | Ubuntu Linux |
| Python Version | 3.12.3 |
| Programming Language | Python |
| Main File | exceptions.py |
| Evidence Directory | evidence/ |

## 5. Introduction to Exception Handling

An exception is an error that occurs while a program is running.

For example, converting text such as `abc` into an integer causes a `ValueError`.

Python provides exception-handling statements to manage these situations.

The main keywords are:

- `try`: Contains code that may produce an exception.
- `except`: Handles an exception if it occurs.
- `finally`: Executes whether an exception occurs or not.

## 6. Task 1: Prompt User for Input

### Objective

Accept input from the user and display the entered value.

### Code

```python
user_input = input("Enter a number: ")
print(f"You entered: {user_input}")
```

### Explanation

- `input()` accepts information from the user.
- The entered value is stored in `user_input`.
- `print()` displays the entered value.
- Input is initially stored as a string.

### Test Command

```bash
echo "5" | python3 exceptions.py
```

### Expected Output

```text
Enter a number: You entered: 5
```

### Result

The program successfully accepted and displayed user input.

## 7. Task 2: Convert Input to Integer with Exception Handling

### Objective

Convert user input into an integer and handle invalid input using `ValueError`.

### Code

```python
user_input = input("Enter a number: ")

try:
    number = int(user_input)
    print(f"The number is {number}.")

except ValueError:
    print("Error: Input is not a valid number. Please enter an integer.")
```

### Explanation

- `int()` converts the input into an integer.
- The `try` block contains the conversion operation.
- If the user enters valid numeric input, the converted number is displayed.
- If the user enters invalid text, Python raises a `ValueError`.
- The `except ValueError` block handles that error.

### Test 1: Valid Input

```bash
echo "5" | python3 exceptions.py
```

Expected output:

```text
Enter a number: The number is 5.
```

### Test 2: Invalid Input

```bash
echo "abc" | python3 exceptions.py
```

Expected output:

```text
Enter a number: Error: Input is not a valid number. Please enter an integer.
```

### Result

The program successfully converted valid input and handled invalid input without crashing.

## 8. Task 3: Multiple Except Blocks and Finally

### Objective

Handle multiple exception types and execute a `finally` block.

### Final Code

```python
user_input = input("Enter a number: ")

try:
    result = 10 / int(user_input)
    print(f"Result is: {result}")

except ValueError:
    print("Error: Please enter numeric values!")

except ZeroDivisionError:
    print("Error: Division by zero is undefined!")

finally:
    print("Done.")
```

### Explanation

**1. try block**

Contains the operation that may produce an exception:

```python
result = 10 / int(user_input)
```

**2. except ValueError**

Handles invalid input, such as `abc`, which cannot be converted into an integer.

**3. except ZeroDivisionError**

Handles division by zero, which is not allowed in Python.

**4. finally block**

Executes after the `try` and `except` blocks, whether the operation succeeds or an exception is handled.

## 9. Task 3 Testing

### Test 1: Successful Division

Command:

```bash
echo "2" | python3 exceptions.py
```

Output:

```text
Enter a number: Result is: 5.0
Done.
```

Explanation:

The input `2` is converted into an integer. Python calculates `10 / 2` and displays `5.0`.

### Test 2: Division by Zero

Command:

```bash
echo "0" | python3 exceptions.py
```

Output:

```text
Enter a number: Error: Division by zero is undefined!
Done.
```

Explanation:

Python raises `ZeroDivisionError` because division by zero is not allowed.

The matching `except` block handles the error.

### Test 3: Invalid Input

Command:

```bash
echo "abc" | python3 exceptions.py
```

Output:

```text
Enter a number: Error: Please enter numeric values!
Done.
```

Explanation:

Python raises `ValueError` because `abc` cannot be converted into an integer.

The matching `except` block handles the error.

## 10. Understanding Exception Types

| Exception | Meaning | Example |
|---|---|---|
| ValueError | Invalid value supplied to an operation | `int("abc")` |
| ZeroDivisionError | Division by zero | `10 / 0` |

## 11. Difference Between try, except, and finally

| Keyword | Purpose |
|---|---|
| try | Executes code that may produce an exception |
| except | Handles a matching exception |
| finally | Executes after the try/except sequence |

## 12. Why Exception Handling Is Important

Exception handling is useful because:

- It prevents common errors from stopping a program unexpectedly.
- It provides meaningful error messages.
- It makes programs more reliable.
- It helps developers identify and manage errors.
- It improves the user experience.

## 13. Python Syntax Verification

Command:

```bash
python3 -m py_compile exceptions.py
```

Result:

```text
Python syntax check: PASSED
```

The Python file passed the syntax compilation check.

## 14. Evidence Files

The `evidence/` directory contains:

| File | Purpose |
|---|---|
| python-version.txt | Records Python version |
| syntax-check.txt | Records syntax verification |
| task1-output.txt | Task 1 input/output |
| task2-valid-input.txt | Task 2 valid input |
| task2-invalid-input.txt | Task 2 invalid input |
| task3-success.txt | Successful division |
| task3-zero-division.txt | Division by zero handling |
| task3-invalid-input.txt | Invalid input handling |

## 15. Project Structure

```text
Lab-13-Handling-Exceptions/
│
├── README.md
├── exceptions.py
│
└── evidence/
    ├── python-version.txt
    ├── syntax-check.txt
    ├── task1-output.txt
    ├── task2-valid-input.txt
    ├── task2-invalid-input.txt
    ├── task3-success.txt
    ├── task3-zero-division.txt
    └── task3-invalid-input.txt
```

## 16. Learning Outcomes

After completing this lab, I learned how to:

- Accept input from users.
- Convert strings into integers.
- Use `try` and `except` blocks.
- Handle `ValueError`.
- Handle `ZeroDivisionError`.
- Use multiple exception handlers.
- Execute code using `finally`.
- Test Python programs with different inputs.

## 17. Conclusion

In this lab, I practised Python exception handling through three tasks.

I learned how to handle invalid input, prevent division-by-zero errors, and execute a `finally` block.

I also verified the Python syntax and saved evidence of the test results.

**Lab 13: Handling Exceptions — Completed.**
