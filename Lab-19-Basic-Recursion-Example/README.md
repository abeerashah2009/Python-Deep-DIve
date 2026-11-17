# Lab 19: Basic Recursion Example

## 1. Introduction

Recursion is a programming technique in which a function calls itself to solve a problem.

A recursive function has two important parts:

- **Base Case:** Stops the recursive calls.
- **Recursive Case:** Calls the same function with a smaller or modified input.

In this lab, Python is used to calculate factorials using recursion, iteration, and tail recursion.

## 2. Objectives

- Understand the concept of recursion.
- Implement a recursive factorial function.
- Understand the difference between recursion and iteration.
- Explore tail recursion.
- Understand Python's recursion limit.
- Calculate large factorials safely using iteration.

## 3. Environment

- Operating System: Ubuntu 24.04
- Programming Language: Python
- Python Version: 3.12.3
- Working Directory: Lab-19-Basic-Recursion-Example

## 4. Understanding Factorial

The factorial of a non-negative integer is the product of all positive integers up to that number.

For example:

- 0! = 1
- 1! = 1
- 3! = 3 × 2 × 1 = 6
- 5! = 5 × 4 × 3 × 2 × 1 = 120

## 5. Task 1: Introduction to Recursion

Recursion allows a function to solve a problem by calling itself.

The factorial function uses:

- A base case: `n <= 1`
- A recursive case: `n * factorial(n - 1)`

The base case prevents infinite recursion.

## 6. Task 2: Recursive Factorial Function

The `factorial()` function calculates a number's factorial by repeatedly calling itself with a smaller number.

Example:

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

Output:

```text
The factorial of 5 is: 120
Factorials of 0..7: [1, 1, 2, 6, 24, 120, 720, 5040]
```

## 7. Task 3: Recursion vs Iteration

**Recursion:**
- A function calls itself.
- Uses the call stack.
- Can make naturally recursive problems easier to understand.
- Deep recursion can cause `RecursionError`.

**Iteration:**
- Uses loops such as `for` and `while`.
- Does not create a new recursive function call for each iteration.
- Is generally more memory-efficient for this factorial example.

The iterative factorial function:

```python
def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

Output:

```text
The factorial of 5 using iteration is: 120
Recursive equals iterative: True
```

## 8. Task 4: Tail Recursion and Large Numbers

Tail recursion is a form of recursion where the recursive call is the final operation.

An accumulator stores the intermediate result.

```python
def tail_recursive_factorial(n, accumulator=1):
    if n <= 1:
        return accumulator
    return tail_recursive_factorial(n - 1, n * accumulator)
```

Output:

```text
The factorial of 5 using tail recursion is: 120
```

### Python Recursion Limit

Python does not optimise tail calls. Both ordinary and tail recursion can exceed the recursion limit.

The lab demonstrated:

```text
Recursion limit: 1000
RecursionError: maximum recursion depth exceeded
Tail recursion also fails: maximum recursion depth exceeded
```

### Large Factorials Using Iteration

Iteration avoids the recursive call-stack limit.

The lab calculated factorial of 5000 and compared it with Python's standard library:

```text
Iterative factorial(5000) has 54233 bits
Matches math.factorial: True
Three methods for 5: 120 120 120
```

A modest recursion-limit test also passed:

```text
factorial(1500) works with limit 2000: True
```

A very high recursion limit can be dangerous because it may exhaust the interpreter's real stack. Iteration is preferred for large inputs.

## 9. Complete Python Program

The complete practical implementation is available in `recursion.py`.

It includes:

1. Recursive factorial.
2. Tests from 0 to 7.
3. Iterative factorial.
4. Comparison of recursive and iterative results.
5. Tail-recursive factorial.
6. Recursion limit and error handling.
7. Large factorial calculation.
8. Comparison with `math.factorial()`.

## 10. Evidence Files

The `evidence/` directory contains:

- `compile-check.txt` — Python syntax verification.
- `program-output.txt` — Complete program output.
- `python-version.txt` — Installed Python version.
- `function-structure.txt` — Function and import structure.

## 11. Interview Questions and Answers

**Q1. What is recursion?**

Recursion is a technique where a function calls itself to solve a problem.

**Q2. What is a base case?**

A base case is the condition that stops recursive calls.

**Q3. What is a recursive case?**

It is the part of a function that calls itself with a modified input.

**Q4. What is factorial?**

Factorial is the product of all positive integers up to a given non-negative integer.

**Q5. What is iteration?**

Iteration repeats instructions using loops such as `for` and `while`.

**Q6. What is the difference between recursion and iteration?**

Recursion uses function calls, while iteration uses loops.

**Q7. What is tail recursion?**

Tail recursion occurs when the recursive call is the final operation in a function.

**Q8. Does Python optimise tail recursion?**

No. Python does not perform tail-call optimisation.

**Q9. What is RecursionError?**

It is an error raised when recursive calls exceed Python's recursion limit.

**Q10. Which method is suitable for large factorials in Python?**

Iteration or the standard library `math.factorial()` is suitable because it avoids recursive call-stack limits.

## 12. Conclusion

In this lab, I learned how recursion works and implemented factorial calculations using ordinary recursion, iteration, and tail recursion.

I also explored Python's recursion limit and demonstrated why iteration is a safer choice for large factorial calculations.

All practical tests and Python syntax checks passed successfully.
