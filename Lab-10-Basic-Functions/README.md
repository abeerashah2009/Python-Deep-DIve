# Lab 10 – Basic Functions

## 1. Introduction

A function is a reusable block of code that performs a specific task.

Functions make programs:
- Easier to read.
- Easier to understand.
- Easier to maintain.
- More organized.
- Reusable without writing the same code again.

In this lab, we learned how to define and call functions, use parameters, set default values, and pass keyword arguments.

## 2. Lab Objectives

The main objectives were:

1. Understand the concept of Python functions.
2. Define a function using the `def` keyword.
3. Call a function with different arguments.
4. Understand parameters and arguments.
5. Use default parameters.
6. Use keyword arguments.
7. Execute and verify a Python program.

## 3. Environment and Prerequisites

| Requirement | Details |
|---|---|
| Operating System | Ubuntu 24.04 |
| Programming Language | Python |
| Python Version | 3.12.3 |
| Python File | `basic_functions.py` |
| External Libraries | None |

### Check Python version

Command:

```bash
python3 --version
```

Output:

```text
Python 3.12.3
```

## 4. Understanding Functions in Python

### 4.1 What Is a Function?

A function is a named block of code that performs a particular task.

A function can receive input, process it and return a result.

### 4.2 Function Definition

The `def` keyword is used to define a function.

General syntax:

```python
def function_name(parameters):
    # Function body
    return value
```

Explanation:

- `def`: Keyword used to define a function.
- `function_name`: Name given to the function.
- `parameters`: Inputs received by the function.
- Function body: Instructions executed when the function is called.
- `return`: Sends a result back to the caller.

### 4.3 Function Call

A function call executes the function.

Example:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

Output:

```text
Hello, Alice!
```

## 5. Task 1 – Define a Function greet(name)

### Objective

Create a function named `greet` that accepts one parameter called `name`.

### Step 1: Create the working directory

```bash
mkdir -p ~/functions-lab
cd ~/functions-lab
```

For this portfolio lab, the actual working directory was:

```text
~/Python-Deep-DIve/Lab-10-Basic-Functions
```

### Step 2: Create the Python file

```bash
nano basic_functions.py
```

### Step 3: Write the function

```python
def greet(name):
    return f"Hello, {name}!"
```

### Explanation

- `greet` is the function name.
- `name` is the parameter.
- `return` sends the greeting back.
- The f-string inserts the supplied name into the greeting.

### Step 4: Verify the file

```bash
cat basic_functions.py
python3 basic_functions.py
```

Expected file content:

```python
def greet(name):
    return f"Hello, {name}!"
```

Expected behavior:

The function definition produces no output because it has not been called.

## 6. Task 2 – Call the Function and Print Results

### Objective

Call the `greet()` function using different names.

### Code

```python
print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))
```

### Explanation

- `greet("Alice")` passes Alice as an argument.
- `greet("Bob")` passes Bob as an argument.
- `greet("Charlie")` passes Charlie as an argument.
- `print()` displays the returned greeting.

### Expected Output

```text
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

### Important Concept: Parameter vs Argument

**Parameter:** A variable written in the function definition.

**Argument:** The actual value supplied when calling the function.

Example:

```python
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
```

Here:
- `name` is the parameter.
- `"Alice"` is the argument.

## 7. Task 3 – Use Default Parameters

### Objective

Give the function a default value so it can work even when no argument is provided.

### Code

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))
print(greet())
```

### Explanation

A default parameter has a predefined value.

In this example:

```python
def greet(name="Guest"):
```

The default value of `name` is `"Guest"`.

When we provide a name, Python uses that name.

When we call `greet()` without an argument, Python uses `"Guest"` automatically.

### Expected Output

```text
Hello, Alice!
Hello, Bob!
Hello, Charlie!
Hello, Guest!
```

### Important Concept

Default parameters make functions more flexible because an argument is not always required.

## 8. Task 4 – Utilize Keyword Arguments

### Objective

Call the function by specifying the parameter name.

### Code

```python
print(greet(name="Diana"))
```

### Explanation

A keyword argument passes a value using the parameter name.

In this example:

- `name` is the parameter name.
- `"Diana"` is the supplied value.

### Expected Output

```text
Hello, Diana!
```

### Benefit of Keyword Arguments

Keyword arguments make function calls easier to understand.

They are especially useful when a function has multiple parameters.

## 9. Complete Python Program

Final file: `basic_functions.py`

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))
print(greet())
print(greet(name="Diana"))
```

### Complete Program Explanation

1. The function `greet()` is defined.
2. It accepts a parameter called `name`.
3. The default parameter value is `"Guest"`.
4. The function returns a greeting using an f-string.
5. Three function calls provide different names.
6. One call uses the default value.
7. The final call uses a keyword argument.

## 10. Complete Program Output

Command:

```bash
python3 basic_functions.py
```

Actual output:

```text
Hello, Alice!
Hello, Bob!
Hello, Charlie!
Hello, Guest!
Hello, Diana!
```

All five greetings were displayed correctly.

## 11. Important Python Function Concepts

| Concept | Meaning |
|---|---|
| `def` | Defines a function |
| Function name | Identifies the function |
| Parameter | Receives input |
| Argument | Value passed to a function |
| `return` | Sends a result back |
| Function call | Executes a function |
| Default parameter | Uses a predefined value |
| Keyword argument | Passes a value using its parameter name |
| f-string | Inserts values into formatted strings |

## 12. Common Mistakes and Troubleshooting

### Mistake 1: Forgetting the colon

Incorrect:

```python
def greet(name)
```

Correct:

```python
def greet(name):
```

### Mistake 2: Incorrect indentation

Python requires correct indentation inside a function.

Correct:

```python
def greet(name):
    return f"Hello, {name}!"
```

### Mistake 3: Calling a function before defining it

Define the function before calling it in this script.

### Mistake 4: Missing quotation marks

Correct:

```python
print(greet("Alice"))
```

### Mistake 5: Forgetting the default value

Correct:

```python
def greet(name="Guest"):
    return f"Hello, {name}!"
```

## 13. Testing and Verification

### Check Python version

```bash
python3 --version
```

### Run the program

```bash
python3 basic_functions.py
```

### Check Python syntax

```bash
python3 -m py_compile basic_functions.py
```

### Save program output

```bash
python3 basic_functions.py | tee evidence/basic-functions-output.txt
```

### Save syntax verification

```bash
echo "Python syntax check: PASSED" | tee evidence/syntax-check.txt
```

### Evidence Files

- `evidence/python-version.txt`
- `evidence/basic-functions-output.txt`
- `evidence/syntax-check.txt`

## 14. Interview Questions and Answers

### Q1. What is a function in Python?

A function is a reusable block of code that performs a specific task.

### Q2. Which keyword defines a function?

The `def` keyword.

### Q3. What is a function call?

A function call executes a defined function.

### Q4. What is a parameter?

A parameter is a variable that receives input inside a function definition.

### Q5. What is an argument?

An argument is the actual value passed to a function.

### Q6. What is the purpose of return?

The `return` statement sends a result back from a function.

### Q7. What is a default parameter?

A default parameter is a parameter that has a predefined value.

### Q8. What happens when a default parameter is not supplied?

Python uses its predefined default value.

### Q9. What are keyword arguments?

Keyword arguments pass values by specifying the parameter name.

### Q10. What is an f-string?

An f-string is a formatted string that allows variables and expressions to be inserted using curly braces.

### Q11. What is the difference between print and return?

`print()` displays information on the screen, while `return` sends a result back to the caller.

### Q12. Can a function be called multiple times?

Yes. A function can be called as many times as required.

### Q13. What happens when a function is defined but never called?

Its body does not execute.

### Q14. Why are functions useful?

They improve code organization, readability, reusability and maintainability.

### Q15. What is the default value used in this lab?

The default value is `"Guest"`.

## 15. Repository Structure

```text
Lab-10-Basic-Functions/
│
├── README.md
├── basic_functions.py
│
└── evidence/
    ├── python-version.txt
    ├── basic-functions-output.txt
    └── syntax-check.txt
```

## 16. Case Study – Personalized Greeting Service

Consider a user log service that needs to generate personalized greetings.

A greeting function can generate messages for different users.

Example:

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet("Abeera"))
print(greet())
```

Output:

```text
Hello, Abeera!
Hello, Guest!
```

This example demonstrates how a reusable function can generate personalized messages.

## 17. Conclusion

In this lab, we successfully learned the fundamentals of Python functions.

We completed all four tasks:

1. Defined the `greet(name)` function.
2. Called the function with different arguments.
3. Used the default parameter `"Guest"`.
4. Used the keyword argument `name="Diana"`.

We also executed the program, checked its syntax and saved evidence of the results.

Functions are an important foundation for writing organized, reusable and maintainable Python programs.

**Lab 10 – Basic Functions completed.**
