# Lab 8: Tuples & Sets in Python

---

## 1. Overview

Python provides several built-in data structures for storing and organizing information. Two important data structures are tuples and sets.

A **tuple** is an ordered and immutable collection of elements. Once a tuple is created, its elements cannot be changed.

A **set** is an unordered and mutable collection that stores unique elements. Sets automatically remove duplicate values.

In this lab, we explored tuple creation, tuple unpacking, immutability, set creation, duplicate handling, set operations, and hashability.

## 2. Objectives

The objectives of this lab are:

- Understand the properties and usage of Python tuples.
- Understand the properties and usage of Python sets.
- Create and unpack tuples.
- Demonstrate tuple immutability.
- Use tuples as dictionary keys.
- Create sets containing unique values.
- Add elements and understand duplicate handling.
- Perform union, intersection, and difference operations.
- Understand hashable and unhashable objects.

## 3. Prerequisites

- Basic knowledge of Python programming.
- Familiarity with lists and basic data structures.
- Ubuntu 24.04 Linux environment.
- Python 3.12 installed.
- Basic knowledge of Linux terminal commands.

## 4. Environment and Tools

### 4.1 Operating System

Ubuntu 24.04 LTS.

### 4.2 Python Version

Python 3.12.3.

### 4.3 Verify Python Installation

Command:

```bash
python3 --version
```

Output:

```text
Python 3.12.3
```

### 4.4 Create the Working Directory

Command:

```bash
mkdir -p ~/tuples-sets
cd ~/tuples-sets
```

For this GitHub portfolio lab, the working directory was created inside the repository:

```text
~/Python-Deep-DIve/Lab-08-Tuples-and-Sets
```

## 5. Introduction to Tuples

### 5.1 What Is a Tuple?

A tuple is a built-in Python data structure used to store multiple values in a single variable.

Tuples are:

- Ordered: Elements maintain their positions.
- Immutable: Elements cannot be modified after creation.
- Allow duplicates: The same value can appear more than once.
- Able to store different data types.

Example:

```python
student = ("Abeera", 20, "Python")
print(student)
```

### 5.2 Tuple Syntax

Tuples are commonly created using parentheses:

```python
numbers = (10, 20, 30)
```

A tuple with one element requires a trailing comma:

```python
single_item = (10,)
```

Without the comma, `(10)` is simply an integer inside parentheses.

### 5.3 Tuple Immutability

Immutability means that the elements of a tuple cannot be changed after creation.

Example:

```python
coordinates = (10, 20, 30)
coordinates[0] = 100
```

This produces a `TypeError` because tuple elements do not support item assignment.

### 5.4 Tuple Unpacking

Tuple unpacking assigns individual tuple elements to separate variables.

Example:

```python
coordinates = (10, 20, 30)

x, y, z = coordinates

print(x, y, z)
```

Output:

```text
10 20 30
```

## 6. Task 1: Working with Tuples

### 6.1 Subtask 1.1: Create a Tuple of Coordinates

Objective:

Create a tuple containing three coordinate values and unpack its elements into separate variables.

File: `tuples.py`

Code:

```python
# Creating a tuple representing coordinates (x, y, z)
coordinates = (10, 20, 30)
print("Coordinates Tuple:", coordinates)

# Tuple unpacking
x, y, z = coordinates
print("Unpacked:", x, y, z)
```

Execution:

```bash
python3 tuples.py
```

Output:

```text
Coordinates Tuple: (10, 20, 30)
Unpacked: 10 20 30
```

Explanation:

- `coordinates` stores three values.
- Parentheses are used to define the tuple.
- `x, y, z` receive the corresponding values.
- The values are printed separately.

### 6.2 Subtask 1.2: Confirm Tuple Immutability

Objective:

Attempt to modify an element and observe the error.

Code added to `tuples.py`:

```python
# Attempt to change the x-coordinate
try:
    coordinates[0] = 100
except TypeError as e:
    print("Error:", e)

# A tuple can be a dictionary key
locations = {coordinates: "origin marker"}
print("Dict with tuple key:", locations)
```

Execution:

```bash
python3 tuples.py
```

Additional output:

```text
Error: 'tuple' object does not support item assignment
Dict with tuple key: {(10, 20, 30): 'origin marker'}
```

Explanation:

- `coordinates[0]` accesses the first tuple element.
- Assigning `100` attempts to modify the tuple.
- Python raises a `TypeError` because tuples are immutable.
- The `try` and `except` blocks handle the error without stopping the program.
- The tuple is used as a dictionary key because its elements are hashable.

### 6.3 Complete Tuple Program

```python
# Creating a tuple representing coordinates (x, y, z)
coordinates = (10, 20, 30)
print("Coordinates Tuple:", coordinates)

# Tuple unpacking
x, y, z = coordinates
print("Unpacked:", x, y, z)

# Attempt to change the x-coordinate
try:
    coordinates[0] = 100
except TypeError as e:
    print("Error:", e)

# A tuple can be a dictionary key
locations = {coordinates: "origin marker"}
print("Dict with tuple key:", locations)
```

### 6.4 Complete Tuple Output

```text
Coordinates Tuple: (10, 20, 30)
Unpacked: 10 20 30
Error: 'tuple' object does not support item assignment
Dict with tuple key: {(10, 20, 30): 'origin marker'}
```

## 7. Introduction to Sets

### 7.1 What Is a Set?

A set is a built-in Python data structure used to store unique elements.

Sets have the following characteristics:

- Unordered: They do not guarantee a particular display order.
- Unique: Duplicate elements are automatically removed.
- Mutable: Elements can be added or removed.
- No indexing: Elements cannot be accessed by numerical positions.
- Elements must be hashable.

### 7.2 Set Syntax

Sets are commonly created using curly braces:

```python
numbers = {1, 2, 3, 4, 5}
```

An empty set must be created using:

```python
empty_set = set()
```

Using `{}` creates an empty dictionary, not an empty set.

### 7.3 Unique Elements

Sets automatically eliminate duplicate values.

Example:

```python
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)
```

The set contains only unique values:

```text
{1, 2, 3, 4}
```

## 8. Task 2: Working with Sets

### 8.1 Subtask 2.1: Create a Set of Numbers

Objective:

Create a set containing five numbers and print it.

File: `sets.py`

Code:

```python
# Create a set of numbers
number_set = {1, 2, 3, 4, 5}
print("Initial Set:", number_set)
```

Execution:

```bash
python3 sets.py
```

Output:

```text
Initial Set: {1, 2, 3, 4, 5}
```

Explanation:

- Curly braces define the set.
- The set contains five unique integers.
- `print()` displays the set.

### 8.2 Subtask 2.2: Add a Duplicate and Observe Behavior

Objective:

Attempt to add a duplicate number and verify that the set size remains unchanged.

Code:

```python
# Attempt to add a duplicate number to the set
size_before = len(number_set)
number_set.add(3)
print("Set after adding duplicate:", number_set)
assert len(number_set) == size_before
print("Length unchanged:", len(number_set))
```

Output:

```text
Set after adding duplicate: {1, 2, 3, 4, 5}
Length unchanged: 5
```

Explanation:

- `len()` returns the number of elements.
- `add(3)` attempts to add the number `3`.
- The number already exists, so no new element is added.
- `assert` checks that the set length has not changed.
- If the condition is false, Python raises an `AssertionError`.

### 8.3 Set Operations

Python supports mathematical operations on sets.

The second set used in this lab:

```python
other = {4, 5, 6, 7}
```

**Union**

Union combines all unique elements from both sets.

```python
print("Union:", number_set | other)
```

Output:

```text
Union: {1, 2, 3, 4, 5, 6, 7}
```

**Intersection**

Intersection returns elements that exist in both sets.

```python
print("Intersection:", number_set & other)
```

Output:

```text
Intersection: {4, 5}
```

**Difference**

Difference returns elements that exist in the first set but not in the second set.

```python
print("Difference:", number_set - other)
```

Output:

```text
Difference: {1, 2, 3}
```

### 8.4 Hashable and Unhashable Elements

Set elements must be hashable.

A list is mutable and unhashable, so it cannot be stored directly inside a set.

Example:

```python
try:
    bad = {[1, 2], 3}
except TypeError as e:
    print("Error:", e)
```

Output:

```text
Error: unhashable type: 'list'
```

A tuple containing hashable elements can be stored inside a set.

Example:

```python
print("Tuple in set:", {(1, 2), 3})
```

Output:

```text
Tuple in set: {3, (1, 2)}
```

Note: The order of set elements can vary.

### 8.5 Complete Set Program

```python
# Create a set of numbers
number_set = {1, 2, 3, 4, 5}
print("Initial Set:", number_set)

# Attempt to add a duplicate number to the set
size_before = len(number_set)
number_set.add(3)
print("Set after adding duplicate:", number_set)
assert len(number_set) == size_before
print("Length unchanged:", len(number_set))

# Set operations
other = {4, 5, 6, 7}
print("Union:", number_set | other)
print("Intersection:", number_set & other)
print("Difference:", number_set - other)

# Sets need hashable items
try:
    bad = {[1, 2], 3}
except TypeError as e:
    print("Error:", e)

print("Tuple in set:", {(1, 2), 3})
```

### 8.6 Complete Set Output

```text
Initial Set: {1, 2, 3, 4, 5}
Set after adding duplicate: {1, 2, 3, 4, 5}
Length unchanged: 5
Union: {1, 2, 3, 4, 5, 6, 7}
Intersection: {4, 5}
Difference: {1, 2, 3}
Error: unhashable type: 'list'
Tuple in set: {3, (1, 2)}
```

## 9. Common Tuple and Set Methods

### 9.1 Common Tuple Operations

| Operation | Description |
|---|---|
| `len(tuple)` | Returns the number of elements |
| `tuple[index]` | Accesses an element |
| `tuple.count(value)` | Counts occurrences |
| `tuple.index(value)` | Returns the first matching position |

Tuples are immutable, so they do not provide methods such as `append()` or `remove()`.

### 9.2 Common Set Methods

| Method | Description |
|---|---|
| `add()` | Adds an element |
| `remove()` | Removes an element; raises KeyError if missing |
| `discard()` | Removes an element without an error if missing |
| `clear()` | Removes all elements |
| `union()` | Combines sets |
| `intersection()` | Finds common elements |
| `difference()` | Finds elements in the first set only |

## 10. Typical Usage

### 10.1 When to Use Tuples

Tuples are useful when data should remain fixed.

Examples:

- Coordinates.
- Fixed records.
- Configuration values.
- Dictionary keys when all tuple elements are hashable.

### 10.2 When to Use Sets

Sets are useful when unique values are required.

Examples:

- Removing duplicate records.
- Checking membership.
- Comparing collections.
- Finding common or different elements.

## 11. Difference Between Tuples and Sets

| Feature | Tuple | Set |
|---|---|---|
| Syntax | `()` | `{}` |
| Order | Ordered | Unordered |
| Mutable | No | Yes |
| Duplicates | Allowed | Not allowed |
| Indexing | Supported | Not supported |
| Main purpose | Fixed data | Unique data |
| Elements | Any objects | Hashable objects only |

## 12. Common Mistakes and Troubleshooting

### 12.1 Trying to Modify a Tuple

Incorrect:

```python
coordinates = (10, 20, 30)
coordinates[0] = 100
```

Reason: Tuples are immutable.

Solution: Create a new tuple if different values are required.

### 12.2 Forgetting the Comma in a Single-Element Tuple

Incorrect:

```python
single = (10)
```

Correct:

```python
single = (10,)
```

### 12.3 Expecting Duplicate Values in a Set

A set automatically removes duplicate values.

```python
numbers = {1, 2, 2, 3}
```

The set contains only three unique values.

### 12.4 Using an Unhashable List Inside a Set

Incorrect:

```python
bad = {[1, 2], 3}
```

Reason: Lists are mutable and unhashable.

Solution:

```python
good = {(1, 2), 3}
```

### 12.5 Expecting a Fixed Set Display Order

Sets do not guarantee a particular display order.

Always check membership or compare sets rather than relying on their printed order.

## 13. Python Concepts Learned

After completing this lab, the following concepts were practiced:

1. Creating tuples.
2. Accessing tuple values.
3. Tuple unpacking.
4. Tuple immutability.
5. Using tuples as dictionary keys.
6. Creating sets.
7. Unique elements in sets.
8. Adding duplicate values.
9. Checking collection length.
10. Using assertions.
11. Union operation.
12. Intersection operation.
13. Difference operation.
14. Hashable and unhashable objects.
15. Handling `TypeError` using exception handling.

## 14. Syntax Verification

Command:

```bash
python3 -m py_compile tuples.py sets.py
```

Result:

```text
Python syntax check: PASSED
```

Both Python files passed the syntax verification without errors.

## 15. Testing and Verification Summary

| Test | Result |
|---|---|
| Python version check | Passed |
| Tuple creation | Passed |
| Tuple unpacking | Passed |
| Tuple immutability | Passed |
| Tuple dictionary key | Passed |
| Set creation | Passed |
| Duplicate handling | Passed |
| Set length assertion | Passed |
| Union operation | Passed |
| Intersection operation | Passed |
| Difference operation | Passed |
| Unhashable list test | Passed |
| Tuple inside set | Passed |
| Python syntax check | Passed |

## 16. Interview Questions and Answers

### Q1. What is a tuple in Python?

A tuple is an ordered and immutable collection used to store multiple values.

### Q2. How do you create a tuple?

A tuple is commonly created using parentheses.

```python
numbers = (10, 20, 30)
```

### Q3. Are tuples mutable?

No. Tuples are immutable, which means their elements cannot be changed after creation.

### Q4. What is tuple unpacking?

Tuple unpacking assigns individual tuple elements to separate variables.

### Q5. Can a tuple be used as a dictionary key?

Yes, if all its elements are hashable.

### Q6. What is a set in Python?

A set is an unordered collection of unique elements.

### Q7. Do sets allow duplicate values?

No. Sets automatically remove duplicate values.

### Q8. How do you add an element to a set?

Use the `add()` method.

```python
numbers.add(6)
```

### Q9. What is union?

Union combines unique elements from two sets using `|` or `union()`.

### Q10. What is intersection?

Intersection returns common elements using `&` or `intersection()`.

### Q11. What is difference?

Difference returns elements present in the first set but not in the second set.

### Q12. Why can't a list be stored directly inside a set?

Lists are mutable and unhashable. Set elements must be hashable.

### Q13. Can a tuple be stored inside a set?

Yes, if all its elements are hashable.

### Q14. What is the difference between a tuple and a set?

A tuple is ordered and immutable and allows duplicates. A set is unordered, mutable, and stores unique elements.

### Q15. What does `assert` do?

The `assert` statement checks whether a condition is true. If the condition is false, Python raises an `AssertionError`.

## 17. Repository Structure

The completed lab folder contains:

```text
Lab-08-Tuples-and-Sets/
├── README.md
├── tuples.py
├── sets.py
└── evidence/
    ├── python-version.txt
    ├── tuples-output.txt
    ├── sets-output.txt
    └── syntax-check.txt
```

### Evidence Files

- `python-version.txt`: Records the installed Python version.
- `tuples-output.txt`: Records tuple program output.
- `sets-output.txt`: Records set program output.
- `syntax-check.txt`: Records the Python syntax verification result.

## 18. Conclusion

In this lab, we explored two important Python data structures: tuples and sets.

We learned that tuples are ordered and immutable collections suitable for storing fixed data. We also learned that tuples can be used as dictionary keys when their elements are hashable.

We explored sets as mutable collections that store unique elements. We practiced adding duplicate values, checking set length, performing union, intersection, and difference operations, and understanding hashability.

Both Python programs were executed successfully, and syntax verification passed.

This lab improved our understanding of Python data structures and their practical usage in programming.
