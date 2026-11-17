# Lab 11 – Modules & Packages in Python

## 1. Introduction

Python provides modules and packages to organize code into reusable and manageable sections.

Instead of writing an entire program in one file, we can divide code into separate files and import functions when required.

In this lab, we learn how to:

- Create a Python module.
- Define and use functions from a module.
- Import a module into another Python script.
- Create a Python package.
- Use modules inside a package.
- Verify Python imports and package locations.

## 2. Lab Objectives

After completing this lab, we should understand:

1. The concept of Python modules.
2. How to create and use a module.
3. How to import functions from another file.
4. The purpose of Python packages.
5. How to create a package using `__init__.py`.
6. How to import a module from a package.

## 3. Environment and Prerequisites

### Operating System

Ubuntu 24.04 LTS

### Programming Language

Python 3.12.3

### Tools Used

- Linux terminal
- Python 3
- Nano text editor
- Git and GitHub

### Check Python Version

Command:

```bash
python3 --version
```

Output:

```text
Python 3.12.3
```

Python was already installed, so no additional installation was required.

## 4. Understanding Python Modules

### 4.1 What Is a Module?

A Python module is a file containing Python code, such as functions, variables, and statements.

A module normally has the `.py` extension.

For example:

```text
mymodule.py
```

We can import a module into another Python program and reuse its code.

### 4.2 Why Do We Use Modules?

Modules help us:

- Reuse existing code.
- Organize programs.
- Avoid repeating the same code.
- Make programs easier to maintain.
- Separate different programming tasks.

### 4.3 Module Import

The `import` statement allows us to use code from another module.

Example:

```python
import mymodule
```

We can call a function from the module using dot notation:

```python
mymodule.add(5, 3)
```

## 5. Task 1 – Creating a Python Module

### 5.1 Lab Workspace

The lab workspace was created inside the GitHub portfolio repository:

```text
~/Python-Deep-DIve/Lab-11-Modules-and-Packages
```

All practical tasks were completed inside this directory.

### 5.2 Create mymodule.py

We created a Python file named `mymodule.py`.

Code:

```python
# Filename: mymodule.py

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b
```

### 5.3 Understanding the Code

- `def` defines a function.
- `add` is the function name.
- `a` and `b` are parameters.
- `return` sends the calculated result back.
- `a + b` performs addition.
- The docstring describes the purpose of the function.

### 5.4 Check the Module File

Command:

```bash
ls -l mymodule.py
```

This command displays file permissions, ownership, size, and modification details.

### 5.5 Test the Module Directly

Command:

```bash
python3 -c 'import mymodule; print(mymodule.add(5, 3))'
```

Output:

```text
8
```

Result: The module was successfully imported, and its function returned the correct result.

## 6. Task 1 – Using the Module in a Script

### 6.1 Create main.py

We created another Python file named `main.py`.

Initial code:

```python
# Filename: main.py

import mymodule

# Call the add function from mymodule
result = mymodule.add(5, 3)
print(f"The sum of 5 and 3 is {result}")
```

### 6.2 Understanding the Code

**Import statement**

```python
import mymodule
```

Imports the module so its functions can be used.

**Function call**

```python
result = mymodule.add(5, 3)
```

Calls the `add()` function and stores its returned value in `result`.

**Print statement**

```python
print(f"The sum of 5 and 3 is {result}")
```

Displays the result using an f-string.

### 6.3 Run the Program

Command:

```bash
python3 main.py
```

Expected output:

```text
The sum of 5 and 3 is 8
```

### 6.4 Find the Module Location

Command:

```bash
python3 -c 'import mymodule; print(mymodule.__file__)'
```

This displays the actual file path from which Python imported the module.

Initially, the module was located directly inside the Lab 11 directory.

## 7. Understanding Python Packages

### 7.1 What Is a Package?

A Python package is a way to organize related modules into directories.

A package helps developers structure larger applications logically.

For example:

```text
mypackage/
    __init__.py
    mymodule.py
```

Here:

- `mypackage` is the package directory.
- `__init__.py` marks it as a regular Python package.
- `mymodule.py` contains the reusable function.

### 7.2 What Is `__init__.py`?

The `__init__.py` file is used to mark a directory as a regular Python package.

It can be empty or contain initialization code.

Python 3 also supports namespace packages without this file, but using `__init__.py` is a common and explicit package structure.

## 8. Task 2 – Creating a Python Package

### 8.1 Create the Package Directory

Command:

```bash
mkdir -p mypackage
```

### 8.2 Create `__init__.py`

Command:

```bash
touch mypackage/__init__.py
```

The `touch` command creates an empty file if it does not already exist.

### 8.3 Check the Package

Command:

```bash
ls -la mypackage
```

Expected file:

```text
__init__.py
```

### 8.4 Move the Module into the Package

Command:

```bash
mv mymodule.py mypackage/
```

This moves the existing module into the package directory.

Check the directory:

```bash
ls -l mypackage/
```

Expected structure:

```text
__init__.py
mymodule.py
```

## 9. Importing a Module from a Package

### 9.1 Update main.py

We changed the import statement to:

```python
from mypackage import mymodule
```

Complete final code:

```python
# Filename: main.py

from mypackage import mymodule

result = mymodule.add(5, 3)
print(f"The sum of 5 and 3 is {result}")
```

### 9.2 Understanding the Import

```python
from mypackage import mymodule
```

- `from` identifies the package.
- `mypackage` is the package name.
- `import` tells Python what to load.
- `mymodule` is the module inside the package.

We can then call the function using:

```python
mymodule.add(5, 3)
```

### 9.3 Run the Updated Program

Command:

```bash
python3 main.py
```

Output:

```text
The sum of 5 and 3 is 8
```

Result: The program successfully imported and used a module from a package.

## 10. Verify the Package Location

Command:

```bash
python3 -c 'import mypackage; print(mypackage.__file__)'
```

Output:

```text
/home/ubuntu/Python-Deep-DIve/Lab-11-Modules-and-Packages/mypackage/__init__.py
```

This confirms that Python successfully located the package.

## 11. Important Python Concepts

### 11.1 Module

A module is a Python file containing reusable code.

Example:

```text
mymodule.py
```

### 11.2 Package

A package organizes related Python modules inside a directory.

Example:

```text
mypackage/
```

### 11.3 Import

The `import` statement loads a module.

Example:

```python
import mymodule
```

### 11.4 From Import

The `from ... import ...` statement imports a specific module or object from another module or package.

Example:

```python
from mypackage import mymodule
```

### 11.5 Dot Notation

Dot notation accesses functions and objects inside a module or package.

Example:

```python
mymodule.add(5, 3)
```

### 11.6 `__file__`

The `__file__` attribute provides the path of the imported module or package file when available.

Example:

```python
print(mypackage.__file__)
```

### 11.7 `__init__.py`

This file marks a directory as a regular Python package and can contain package initialization code.

## 12. Module vs Package

| Module | Package |
|---|---|
| A Python file | A directory containing related modules |
| Usually ends with `.py` | Organizes Python modules |
| Stores reusable code | Organizes multiple modules |
| Example: `mymodule.py` | Example: `mypackage/` |

## 13. Common Errors and Troubleshooting

### 13.1 ModuleNotFoundError

Possible reason:

Python cannot find the requested module.

Solution:

Check the current directory:

```bash
pwd
```

Move into the lab directory:

```bash
cd ~/Python-Deep-DIve/Lab-11-Modules-and-Packages
```

Run the program again:

```bash
python3 main.py
```

### 13.2 Command Not Found: from

Possible reason:

Python code was entered directly into the Linux terminal.

Incorrect:

```bash
from mypackage import mymodule
```

Correct:

Place the statement inside a Python file such as `main.py`, then run:

```bash
python3 main.py
```

### 13.3 IndentationError

Possible reason:

Python code has incorrect indentation.

Solution:

Use consistent indentation inside functions.

Correct:

```python
def add(a, b):
    return a + b
```

### 13.4 Incorrect Package Structure

Check the package:

```bash
ls -la mypackage
```

It should contain:

```text
__init__.py
mymodule.py
```

## 14. Testing and Verification

### 14.1 Check Python Version

```bash
python3 --version
```

Expected:

```text
Python 3.12.3
```

### 14.2 Check Python Syntax

```bash
python3 -m py_compile main.py mypackage/__init__.py mypackage/mymodule.py
```

No output means the syntax compilation completed successfully.

### 14.3 Run the Final Program

```bash
python3 main.py
```

Expected:

```text
The sum of 5 and 3 is 8
```

### 14.4 Verify Package Location

```bash
python3 -c 'import mypackage; print(mypackage.__file__)'
```

Expected:

```text
/home/ubuntu/Python-Deep-DIve/Lab-11-Modules-and-Packages/mypackage/__init__.py
```

### 14.5 Remove Generated Cache Files

```bash
rm -rf __pycache__ mypackage/__pycache__
```

This removes generated Python bytecode cache directories from the portfolio.

## 15. Evidence and Repository Structure

Final Lab 11 structure:

```text
Lab-11-Modules-and-Packages/
│
├── README.md
│
├── main.py
│
├── mypackage/
│   ├── __init__.py
│   └── mymodule.py
│
└── evidence/
    ├── package-location.txt
    ├── package-output.txt
    ├── python-version.txt
    └── syntax-check.txt
```

### Evidence Files

- `package-output.txt`: Records the final program output.
- `package-location.txt`: Records the package location.
- `python-version.txt`: Records the Python version.
- `syntax-check.txt`: Records the successful Python syntax verification.

## 16. Practical Case Study – Reusable Calculation Module

Imagine a small business application that needs to calculate totals in different parts of its program.

Instead of writing the addition logic repeatedly, we can create a reusable module.

Example module:

```python
def add(a, b):
    return a + b
```

Different scripts can import and use this function.

Benefits:

- Less repeated code.
- Easier maintenance.
- Better organization.
- Reusable functionality.

This is one of the practical reasons developers use Python modules and packages in real applications.

## 17. Interview Questions and Answers

**Q1. What is a Python module?**

A module is a Python file containing reusable code, such as functions and variables.

**Q2. What is a Python package?**

A package is a directory that organizes related Python modules.

**Q3. What is the purpose of the import statement?**

It allows us to use code from another module.

**Q4. How do you create a Python module?**

Create a file with a `.py` extension and write Python code inside it.

**Q5. What is `__init__.py`?**

It is a file commonly used to mark a directory as a regular Python package.

**Q6. What is the difference between a module and a package?**

A module is a Python file, while a package organizes multiple modules inside a directory.

**Q7. How do you import a module?**

Use:

```python
import mymodule
```

**Q8. How do you import a module from a package?**

Use:

```python
from mypackage import mymodule
```

**Q9. What does `__file__` do?**

It provides the path of an imported module or package file when available.

**Q10. What is ModuleNotFoundError?**

It occurs when Python cannot locate the requested module or package.

**Q11. Why are modules useful?**

They improve code reuse, organization, and maintainability.

**Q12. Can a package contain multiple modules?**

Yes. A package can contain multiple related Python modules.

**Q13. What is dot notation?**

Dot notation accesses a function or object inside a module.

Example:

```python
mymodule.add(5, 3)
```

**Q14. What does py_compile do?**

It checks Python source files by compiling them into bytecode.

**Q15. Why should we organize large Python programs into packages?**

Packages make large applications easier to understand, maintain, and extend.

## 18. Conclusion

In this lab, we learned how to create and use Python modules and packages.

We created a reusable addition function inside `mymodule.py`, imported it into `main.py`, and successfully tested the program.

We then created a package named `mypackage`, added `__init__.py`, moved the module into the package, and imported it using:

```python
from mypackage import mymodule
```

The final program produced the expected output:

```text
The sum of 5 and 3 is 8
```

We also verified Python syntax, the package location, and all four evidence files.

**Lab 11 – Modules & Packages: Practical tasks completed and verified.**
