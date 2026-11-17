# Lab 15 – Basic Debugging Techniques

## 1. Overview

This lab covers basic Python debugging techniques using print statements and the built-in Python Debugger (`pdb`).

The practical exercises demonstrate how to inspect variable values, identify runtime errors, step through program execution, and fix a division error.

## 2. Objectives

- Understand basic Python debugging techniques.
- Use print statements to inspect program execution.
- Understand the Python Debugger (`pdb`).
- Set breakpoints and inspect variables.
- Step through Python code.
- Identify and fix runtime errors.
- Validate Python scripts.

## 3. Lab Environment

| Component | Details |
|---|---|
| Operating System | Ubuntu 24.04 LTS |
| Programming Language | Python |
| Python Version | 3.12.3 |
| Debugging Tool | Python Debugger (`pdb`) |
| Editor | Nano |
| Environment | Ubuntu Lab VM |

## 4. Introduction to Python Debugging

Debugging is the process of finding and correcting errors in a program.

Python provides different debugging techniques, including:

- Print statements
- Breakpoints
- Variable inspection
- Step-by-step execution
- Traceback analysis

These techniques help developers understand how a program works and identify problems.

## 5. Task 1 – Print Statements for Debugging

Created `sum.py` to calculate the sum of numbers using a Python function and loop.

The program displays intermediate values using print statements.

### Code

```python
def calculate_sum(numbers):
    total = 0

    for num in numbers:
        total += num
        print("Debug: Adding", num, "Total so far:", total)

    return total


# Test the function
numbers = [5, 10, 15]
print("Final Sum:", calculate_sum(numbers))
```

### Execution

```bash
python3 sum.py
```

### Output

```text
Debug: Adding 5 Total so far: 5
Debug: Adding 10 Total so far: 15
Debug: Adding 15 Total so far: 30
Final Sum: 30
```

### Result

The print statements displayed the intermediate total after each loop iteration.

The final calculated sum was 30.

## 6. Task 2 – Introduction to Python Debugger (pdb)

Python includes a built-in debugging module called `pdb`.

It allows developers to pause program execution and inspect variables.

Created `divide.py` to practise debugging a division operation.

### Initial Code

```python
def divide_numbers(a, b):
    breakpoint()
    result = a / b
    print("Result:", result)
    return result

divide_numbers(10, 0)
```

### Starting the Debugger

```bash
printf 'p a\np b\nq\n' | python3 divide.py
```

### Variable Inspection

The debugger displayed:

```text
a = 10
b = 0
```

The `breakpoint()` function stopped execution before the division operation.

### Important pdb Commands

| Command | Description |
|---|---|
| `p variable` | Display a variable value |
| `n` | Execute the next line |
| `s` | Step into a function |
| `c` | Continue execution |
| `q` | Quit the debugger |

## 7. Understanding Breakpoints

A breakpoint pauses program execution at a specific location.

Python provides the following function:

```python
breakpoint()
```

By default, it starts the Python debugger.

To disable breakpoint calls temporarily:

```bash
PYTHONBREAKPOINT=0 python3 divide.py
```

This allows the program to execute without stopping at the breakpoint.

## 8. Understanding ZeroDivisionError

The initial function call was:

```python
divide_numbers(10, 0)
```

Python cannot divide a number by zero.

The program produced:

```text
ZeroDivisionError: division by zero
```

This error helped identify the problem in the function call.

The traceback showed the line where the error occurred.

## 9. Task 3 – Step Through Code Execution

Used the following command to inspect variables and execute the next line:

```bash
printf 'p a, b\nn\nc\n' | python3 divide.py
```

The debugger displayed:

```text
(10, 0)
ZeroDivisionError: division by zero
```

This demonstrated how stepping through execution helps locate runtime errors.

## 10. Post-Mortem Debugging

Post-mortem debugging allows developers to inspect program execution after an uncaught exception.

Command:

```bash
printf 'p a, b\nq\n' | PYTHONBREAKPOINT=0 python3 -m pdb -c continue divide.py
```

The debugger entered post-mortem mode after the division error.

Variable inspection confirmed:

```text
a = 10
b = 0
```

This helped identify the cause of the exception.

## 11. Task 4 – Fixing the Bug

Corrected the function call by changing the second argument from zero to two.

### Corrected Code

```python
def divide_numbers(a, b):
    breakpoint()
    result = a / b
    print("Result:", result)
    return result

divide_numbers(10, 2)
```

### Execution

```bash
PYTHONBREAKPOINT=0 python3 divide.py
```

### Output

```text
Result: 5.0
```

### Result

The division error was fixed successfully.

The program now executes correctly and returns 5.0.

## 12. Python Syntax Validation

Validated both Python scripts using:

```bash
python3 -m py_compile sum.py divide.py
```

The syntax check completed successfully.

Evidence:

```text
Python syntax check: PASSED
```

## 13. Evidence and Verification

The `evidence/` directory contains the following records:

| Evidence File | Description |
|---|---|
| `python-version.txt` | Python version |
| `print-debug-output.txt` | Print debugging output |
| `print-final-result.txt` | Final sum verification |
| `pdb-variable-inspection.txt` | pdb variable inspection |
| `zero-division-traceback.txt` | Division error traceback |
| `pdb-step-debugging.txt` | Step-by-step debugging |
| `pdb-postmortem.txt` | Post-mortem debugging |
| `fixed-function-call.txt` | Corrected function call |
| `fixed-output.txt` | Corrected program output |
| `syntax-check.txt` | Python syntax validation |

## 14. Project Structure

```text
Lab-15-Basic-Debugging-Techniques/
│
├── README.md
├── sum.py
├── divide.py
│
└── evidence/
    ├── python-version.txt
    ├── print-debug-output.txt
    ├── print-final-result.txt
    ├── pdb-variable-inspection.txt
    ├── zero-division-traceback.txt
    ├── pdb-step-debugging.txt
    ├── pdb-postmortem.txt
    ├── fixed-function-call.txt
    ├── fixed-output.txt
    └── syntax-check.txt
```

## 15. Conclusion

In this lab, I practised basic Python debugging techniques using print statements and the built-in Python Debugger (`pdb`).

I learned how to inspect variables, use breakpoints, step through program execution, understand tracebacks, and fix a `ZeroDivisionError`.

Both Python scripts passed syntax validation, and the final division program produced the expected result.

**Lab 15 – Basic Debugging Techniques completed successfully.**
