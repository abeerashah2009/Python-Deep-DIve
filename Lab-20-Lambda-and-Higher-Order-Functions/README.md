# Lab 20: Lambda and Higher-Order Functions

## Objectives

- Understand the syntax and use of lambda functions in Python.
- Learn how higher-order functions work.
- Use `map()` to transform data.
- Use `filter()` to select specific values.
- Use `reduce()` to combine values into a single result.
- Compare `filter()` with list comprehension.

## 1. Introduction

Python supports lambda functions and higher-order functions. These features help us write shorter and reusable code.

A **lambda function** is a small anonymous function. It does not need a function name and is usually used for simple operations.

A **higher-order function** is a function that accepts another function as an argument or returns a function.

## 2. Lambda Function Syntax

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x * x
print(square(5))
```

Output:

```text
25
```

Here:
- `lambda` creates an anonymous function.
- `x` is the argument.
- `x * x` is the expression.
- The function returns the result automatically.

## 3. The map() Function

The `map()` function applies a function to every item in an iterable.

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
```

Output:

```text
[2, 4, 6, 8, 10]
```

**Important:** `map()` returns an iterator. We use `list()` to convert the result into a list.

## 4. The filter() Function

The `filter()` function selects items that satisfy a condition.

Syntax:

```python
filter(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

The expression `x % 2 == 0` checks whether a number is even.

### List Comprehension Alternative

The same operation can be performed using a list comprehension:

```python
even_numbers = [x for x in numbers if x % 2 == 0]
```

Both approaches select the even numbers.

## 5. The reduce() Function

The `reduce()` function repeatedly applies a function to items and produces one final result.

It is available in the `functools` module.

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)
```

Output:

```text
15
```

The function adds the numbers step by step until one total remains.

## 6. Practical Implementation

### File

`lambda_demo.py`

### Complete Code

```python
# Task 1: Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Numbers:", numbers)

# Task 2: Use map with lambda to double each number
# map returns an iterator, so convert it into a list
doubled_numbers = list(map(lambda x: x * 2, numbers))

print("Doubled Numbers:", doubled_numbers)

# Task 3: Use filter with lambda to select even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)

# Equivalent list comprehension
print("Even (comprehension):", [x for x in numbers if x % 2 == 0])

# Task 4: Import reduce from functools
from functools import reduce

# Use reduce with lambda to calculate the sum
total_sum = reduce(lambda x, y: x + y, numbers)

print("Sum of Numbers:", total_sum)
```

## 7. Execution

Run the program using:

```bash
python3 lambda_demo.py
```

### Expected Output

```text
Numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Doubled Numbers: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Even Numbers: [2, 4, 6, 8, 10]
Even (comprehension): [2, 4, 6, 8, 10]
Sum of Numbers: 55
```

## 8. Verification

Python syntax was checked with:

```bash
python3 -m py_compile lambda_demo.py
```

The required output was also checked using:

```bash
python3 lambda_demo.py | grep -E "Doubled|Even Numbers|Sum"
```

All checks passed.

## 9. Benefits

- Lambda functions make simple operations concise.
- `map()` transforms each item in a collection.
- `filter()` selects items based on a condition.
- `reduce()` combines items into one result.
- These functions support functional programming in Python.

## 10. Evidence Files

The `evidence/` directory contains:

| File | Purpose |
|---|---|
| `program-output.txt` | Complete program output |
| `compile-check.txt` | Python syntax check result |
| `python-version.txt` | Python version used |
| `code-structure.txt` | Important code statements |

## 11. Interview Questions and Answers

**Q1. What is a lambda function?**

A lambda function is a small anonymous function created using the `lambda` keyword.

**Q2. What is the syntax of lambda?**

`lambda arguments: expression`

**Q3. What is a higher-order function?**

A function that accepts another function as an argument or returns a function.

**Q4. What does map() do?**

It applies a function to every item in an iterable.

**Q5. What does filter() do?**

It selects items that satisfy a given condition.

**Q6. What does reduce() do?**

It combines iterable items into a single result by repeatedly applying a function.

**Q7. Where is reduce() available?**

It is available in the `functools` module.

**Q8. Why do we use list() with map() and filter()?**

Because these functions return iterators, and `list()` converts their results into lists.

**Q9. What is the difference between map() and filter()?**

`map()` transforms items, while `filter()` selects items based on a condition.

**Q10. What is the difference between lambda and def?**

`lambda` creates a small anonymous function with a single expression. `def` creates a named function and supports multiple statements.

## Conclusion

In this lab, I practiced lambda functions and higher-order functions using `map()`, `filter()`, and `reduce()`. I also compared filtering with list comprehension and verified the program output and Python syntax successfully.
