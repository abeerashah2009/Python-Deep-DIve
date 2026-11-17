# Lab 5: Understanding Conditionals (if, elif, else)

## 1. Overview

In this lab, I learned how to use conditional statements in Python to control program execution.

Conditional statements allow a program to make decisions based on whether a condition is True or False.

Python provides three main conditional keywords:

- `if`
- `elif`
- `else`

I created two Python programs:

1. `classify.py` – Classifies a number as positive, negative, or zero.
2. `grade.py` – Determines a student's letter grade based on their score.

## 2. Objectives

- Understand conditional logic using `if`, `elif`, and `else`.
- Learn how to check multiple conditions.
- Understand how Python selects the first matching condition.
- Practice accepting user input and command-line arguments.
- Handle invalid input using `try` and `except`.
- Apply conditional statements to number classification and grading.

## 3. Environment

| Component | Details |
|---|---|
| Operating System | Ubuntu 24.04 |
| Python Version | 3.12.3 |
| Programming Language | Python |
| Working Directory | Lab-05-Understanding-Conditionals |

## 4. Understanding Conditional Statements

Conditional statements allow Python to execute different blocks of code depending on a condition.

### 4.1 if Statement

The `if` statement checks a condition.

If the condition is True, its code block executes.

Example:

```python
number = 10

if number > 0:
    print("Positive")
```

Output:

```text
Positive
```

### 4.2 elif Statement

`elif` means "else if".

It checks another condition when the previous `if` or `elif` condition is False.

Example:

```python
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
```

Output:

```text
Negative
```

### 4.3 else Statement

The `else` statement executes when none of the previous conditions is True.

Example:

```python
number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

Output:

```text
Zero
```

## 5. Task 1: User Input and Number Classification

### Objective

Create a Python program that determines whether a number is positive, negative, or zero.

### Step 1: Import the sys Module

```python
import sys
```

The `sys` module provides access to command-line arguments through `sys.argv`.

### Step 2: Read User Input

```python
if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    text = input("Enter a number: ")
```

Explanation:

- `sys.argv` stores command-line arguments.
- `sys.argv[1]` reads the first supplied argument.
- `input()` prompts the user when no argument is supplied.

### Step 3: Convert Input into a Number

```python
try:
    number = float(text)
except ValueError:
    print("Invalid number")
    sys.exit(1)
```

Explanation:

- `float()` converts numeric text into a floating-point number.
- `try` executes code that may produce an error.
- `except ValueError` handles input that cannot be converted into a number.
- `sys.exit(1)` exits the program with an error status.

### Step 4: Classify the Number

```python
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

Explanation:

- If the number is greater than zero, it is Positive.
- If the number is less than zero, it is Negative.
- Otherwise, it is Zero.

### Complete Program: classify.py

```python
import sys

if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    text = input("Enter a number: ")

try:
    number = float(text)
except ValueError:
    print("Invalid number")
    sys.exit(1)

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### Testing classify.py

Positive number:

```bash
printf '15\n' | python3 classify.py
```

Output:

```text
Enter a number: Positive
```

Negative number:

```bash
echo -5 | python3 classify.py
```

Output:

```text
Enter a number: Negative
```

Zero:

```bash
echo 0 | python3 classify.py
```

Output:

```text
Enter a number: Zero
```

Decimal number:

```bash
python3 classify.py 7.5
```

Output:

```text
Positive
```

Invalid input:

```bash
echo abc | python3 classify.py
```

Output:

```text
Enter a number: Invalid number
```

## 6. Task 2: Exploring Multiple Conditions with elif

### Objective

Create a grading program that assigns a letter grade based on a student's score.

### Grade Classification

| Score | Grade |
|---|---|
| 90 and above | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

### Step 1: Read the Score

```python
if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    text = input("Enter your score: ")
```

This allows the user to enter a score through the terminal or keyboard.

### Step 2: Convert the Score into an Integer

```python
try:
    score = int(text)
except ValueError:
    print("Invalid score")
    sys.exit(1)
```

The `int()` function converts the score into an integer.

Invalid text is handled using `ValueError`.

### Step 3: Apply Conditional Logic

```python
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

Python checks each condition from top to bottom.

Once it finds the first True condition, it executes that block and skips the remaining conditions.

### Complete Program: grade.py

```python
import sys

if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    text = input("Enter your score: ")

try:
    score = int(text)
except ValueError:
    print("Invalid score")
    sys.exit(1)

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

## 7. Testing Grade Classification

Interactive input:

```bash
echo 85 | python3 grade.py
```

Output:

```text
Enter your score: Grade: B
```

Testing grade boundaries:

```bash
for s in 95 80 70 60 59; do
    python3 grade.py "$s"
done
```

Output:

```text
Grade: A
Grade: B
Grade: C
Grade: D
Grade: F
```

Invalid score:

```bash
python3 grade.py ten
```

Output:

```text
Invalid score
```

## 8. Case Study: Importance of Condition Order

Consider this incorrect condition order:

```python
if score >= 70:
    print("Grade: C")
elif score >= 90:
    print("Grade: A")
```

For a score of 95, the first condition is already True.

Therefore, Python prints:

```text
Grade: C
```

The second condition is skipped.

This is incorrect because a score of 95 should receive Grade A.

The correct approach is to check the highest score first:

```python
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

**Key lesson:** When using multiple overlapping conditions, arrange them carefully so that more specific or higher-priority conditions are checked first.

## 9. Python Concepts Learned

| Concept | Explanation |
|---|---|
| `if` | Checks the first condition |
| `elif` | Checks another condition |
| `else` | Executes when previous conditions are False |
| `sys.argv` | Reads command-line arguments |
| `input()` | Accepts keyboard input |
| `float()` | Converts a value into a floating-point number |
| `int()` | Converts a value into an integer |
| `try` | Executes code that may raise an exception |
| `except` | Handles an exception |
| `ValueError` | Error caused by an invalid conversion |
| `sys.exit(1)` | Exits the program with an error status |

## 10. Syntax Verification

Both Python scripts were checked using:

```bash
python3 -m py_compile classify.py grade.py
```

The command completed without errors.

Python version:

```text
Python 3.12.3
```

## 11. Repository Structure

```text
Lab-05-Understanding-Conditionals/
│
├── classify.py
├── grade.py
├── README.md
│
└── evidence/
    ├── classification-tests.txt
    ├── grade-tests.txt
    ├── elif-order-challenge.txt
    ├── python-version.txt
    └── syntax-check.txt
```

## 12. Conclusion

In this lab, I practiced using Python conditional statements to make decisions based on user input.

I created a number classification program and a student grading program.

I also learned how `if`, `elif`, and `else` work together, how Python handles invalid input, and why the order of conditions matters.

Both programs were tested, and their outputs matched the expected results.
