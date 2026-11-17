# Lab 21: List and Dictionary Comprehensions

## Objectives

- Understand list comprehensions in Python.
- Create lists using concise expressions.
- Learn dictionary comprehensions.
- Filter list and dictionary values using conditions.
- Compare comprehensions with traditional loops.
- Understand the readability and performance benefits of comprehensions.

## 1. Introduction

Comprehensions are a concise way to create new lists and dictionaries from existing iterables.

They can replace many traditional loops and make code shorter and easier to read.

Python supports:
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Generator expressions

This lab focuses on list and dictionary comprehensions.

## 2. List Comprehension

A list comprehension creates a new list using an expression and an iterable.

### Syntax

```python
[expression for item in iterable]
```

### Example: Generate Squares

```python
squares = [x**2 for x in range(10)]
print(squares)
```

Output:

```text
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Explanation:
- `range(10)` generates numbers from 0 to 9.
- `x**2` calculates the square of each number.
- The resulting values are stored in a new list.

## 3. Filtering with List Comprehension

A list comprehension can include an `if` condition.

### Syntax

```python
[expression for item in iterable if condition]
```

### Example: Even Squares

```python
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)
```

Output:

```text
[0, 4, 16, 36, 64]
```

The condition `x % 2 == 0` selects even numbers before calculating their squares.

## 4. Dictionary Comprehension

Dictionary comprehensions create dictionaries using key-value pairs.

### Syntax

```python
{key_expression: value_expression for item in iterable}
```

### Example: Word Lengths

```python
words = ["apple", "banana", "cherry", "date"]
lengths = {word: len(word) for word in words}
print(lengths)
```

Output:

```text
{'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}
```

Explanation:
- Each word becomes a dictionary key.
- `len(word)` calculates the length of that word.
- The length becomes the dictionary value.

## 5. Filtering a Dictionary

Dictionary comprehensions can also use conditions.

Example:

```python
long_words = {word: len(word) for word in words if len(word) > 4}
print(long_words)
```

Output:

```text
{'apple': 5, 'banana': 6, 'cherry': 6}
```

The condition `len(word) > 4` excludes words with four or fewer letters.

## 6. Traditional Loop vs List Comprehension

A list can also be created using a traditional `for` loop.

### Traditional Loop

```python
squares_loop = []

for x in range(10):
    squares_loop.append(x**2)
```

### List Comprehension

```python
squares_comp = [x**2 for x in range(10)]
```

### Compare Results

```python
print(squares_loop == squares_comp)
```

Output:

```text
True
```

Both methods produce the same list of squares.

## 7. Practical Implementation

### Python File

`comprehensions.py`

### Complete Code

```python
# Task 1: list comprehension to generate squares
squares = [x**2 for x in range(10)]
print(squares)

# Filtered comprehension: only even numbers
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# Task 2: dictionary comprehension
words = ["apple", "banana", "cherry", "date"]
lengths = {word: len(word) for word in words}
print(lengths)

# Filtered dictionary comprehension: words longer than 4 letters
long_words = {word: len(word) for word in words if len(word) > 4}
print(long_words)

# Task 3: loop vs comprehension
squares_loop = []
for x in range(10):
    squares_loop.append(x**2)

squares_comp = [x**2 for x in range(10)]
print(squares_loop == squares_comp)
```

## 8. Execution

Run the script:

```bash
python3 comprehensions.py
```

### Expected Output

```text
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 4, 16, 36, 64]
{'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}
{'apple': 5, 'banana': 6, 'cherry': 6}
True
```

## 9. Verification

Python syntax was checked using:

```bash
python3 -m py_compile comprehensions.py
```

The first two output lines were checked using:

```bash
python3 comprehensions.py | head -n 2
```

Dictionary output was checked using:

```bash
python3 comprehensions.py | grep "'banana': 6"
```

The final comparison was checked using:

```bash
python3 comprehensions.py | tail -n 1
```

All checks passed.

## 10. Advantages of Comprehensions

1. **Readability:** They can make simple transformations easier to understand.
2. **Conciseness:** They often replace several lines of loop code.
3. **Maintainability:** Short and clear expressions can be easier to maintain.
4. **Filtering:** Conditions can be included directly.
5. **Performance:** Comprehensions can be faster than equivalent loops in some cases, although readability is often the main reason to use them.

## 11. Evidence Files

The `evidence/` directory contains:

| File | Purpose |
|---|---|
| `program-output.txt` | Complete program output |
| `compile-check.txt` | Python syntax check |
| `python-version.txt` | Python version used |
| `code-structure.txt` | Important code statements |

## 12. Interview Questions and Answers

**Q1. What is a list comprehension?**

A concise way to create a new list from an iterable.

**Q2. What is the basic syntax of a list comprehension?**

`[expression for item in iterable]`

**Q3. What is dictionary comprehension?**

A concise way to create a dictionary using key-value expressions.

**Q4. What is the syntax of dictionary comprehension?**

`{key: value for item in iterable}`

**Q5. Can we use conditions in comprehensions?**

Yes. An `if` clause can filter items based on a condition.

**Q6. What does `range(10)` generate?**

Numbers from 0 through 9.

**Q7. What does `x**2` mean?**

It calculates the square of `x`.

**Q8. What does `len(word)` do?**

It returns the number of characters in a string.

**Q9. What is the difference between a loop and a comprehension?**

A traditional loop uses multiple statements, while a comprehension creates a collection using a concise expression.

**Q10. Why are comprehensions useful?**

They can make data transformation and filtering code shorter and easier to read.

## Conclusion

In this lab, I practiced list and dictionary comprehensions, generated squares, filtered even squares, created dictionaries from strings, and compared a traditional loop with a list comprehension.

All practical tasks and verification checks completed successfully.
