
# Lab 26: Decorators - Basic Usage

## Overview

This lab introduces Python decorators and demonstrates how they can extend the functionality of existing functions without modifying their original code.

**Python Version:** 3.12.3

## Objectives

- Understand Python decorators and their syntax.
- Create a basic logging decorator.
- Apply a decorator using the `@` symbol.
- Understand `functools.wraps`.
- Explore logging and caching.

## Prerequisites

- Basic Python knowledge.
- Understanding of functions and function calls.
- Python 3.12 installed.

## Project Structure

```text
Lab-26-Decorators-Basic-Usage/
├── README.md
├── deco.py
└── evidence/
    ├── 01-decorator-output.txt
    ├── 02-function-name-check.txt
    ├── 03-caching-demo.txt
    ├── 04-syntax-check.txt
    └── 05-lms-score.txt
```

## Task 1: Introduction to Decorators

A decorator is a function that wraps another function to add extra functionality.

Decorators help keep code clean and reusable.

## Task 2: Writing a Basic Decorator

Created `log_decorator()` to print messages before and after a function executes.

Important concepts:

- `func`: The original function passed to the decorator.
- `wrapper`: The inner function that adds extra behavior.
- `*args` and `**kwargs`: Accept positional and keyword arguments.
- `functools.wraps`: Preserves the original function's name and docstring.

## Task 3: Applying the Decorator

Applied the decorator using:

```python
@log_decorator
def say_hello(name):
    print(f"Hello, {name}!")
```

### Expected Output

```text
Start
Hello, Alice!
End
```

### Function Name Verification

Used `functools.wraps` to preserve the original function name.

```text
say_hello
```

## Task 4: Benefits of Decorators

### Logging

Decorators can log function execution without changing the original function code.

### Caching

Caching stores previously calculated results and helps avoid repeated calculations.

### Caching Demonstration

Used Python's built-in `functools.lru_cache`.

Expected result:

```text
computing 4
CacheInfo(hits=1, misses=1, maxsize=None, currsize=1)
```

The second call uses the cached result.

## Verification

The following checks were completed successfully:

- Python 3.12.3 verified.
- Basic decorator implemented.
- Decorator applied successfully.
- Expected output verified.
- Function name preservation verified.
- Caching demonstration completed.
- Python syntax check passed.

## Lab Result

**LMS Score: 100/100**

**Status: Passed**

## Key Learning Outcomes

- Understanding Python decorators.
- Creating reusable wrapper functions.
- Using `functools.wraps`.
- Applying decorators with `@`.
- Understanding logging and caching.

## Conclusion

Python decorators provide a reusable way to extend function behavior. They help developers manage cross-cutting concerns such as logging and caching while keeping code clean and modular.
