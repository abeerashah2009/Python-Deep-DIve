# Lab 7: Lists & List Methods in Python

---

## 1. Overview

Python lists are one of the most commonly used data structures in Python programming.

A list is used to store multiple values in a single variable. Lists allow programmers to organize, access, modify, add, and remove data.

In this lab, we created a list of fruits and performed different operations using Python's built-in list methods.

We also learned how to safely remove an item, sort list elements alphabetically, and iterate through a list using a `for` loop.

## 2. Objectives

The objectives of this lab are:

- Understand the basic concept of Python lists.
- Learn how to create and print lists.
- Add elements using the `append()` method.
- Remove elements using the `remove()` method.
- Understand the `ValueError` exception.
- Use membership checking to prevent removal errors.
- Sort list elements using the `sort()` method.
- Iterate over lists using a `for` loop.
- Execute and verify Python programs from the Linux terminal.

## 3. Environment and Tools

### 3.1 Operating Environment

| Component | Details |
|---|---|
| Operating environment | Ubuntu Linux |
| Programming language | Python |
| Python version | Python 3.12.3 |
| Interpreter | `/usr/bin/python3` |
| Text editor | nano |
| Terminal | Linux terminal |
| Repository | Python-Deep-DIve |

### 3.2 Verify Python Version

Command:

```bash
python3 --version
```

Expected output:

```text
Python 3.12.3
```

### 3.3 Create the Lab Directory

Command:

```bash
mkdir -p ~/Python-Deep-DIve/Lab-07-Lists-and-List-Methods
cd ~/Python-Deep-DIve/Lab-07-Lists-and-List-Methods
```

Check the current directory:

```bash
pwd
```

Expected location:

```text
/home/ubuntu/Python-Deep-DIve/Lab-07-Lists-and-List-Methods
```

## 4. Introduction to Python Lists

### 4.1 What Is a List?

A list is a collection of elements stored in a single variable.

Lists are created using square brackets `[]`.

Example:

```python
fruits = ["apple", "banana", "cherry"]
```

Here:

- `fruits` is the variable name.
- Square brackets define the list.
- `"apple"`, `"banana"`, and `"cherry"` are list elements.

### 4.2 Characteristics of Lists

Python lists have several important characteristics:

1. **Ordered:** Elements maintain their position in the list.
2. **Mutable:** Elements can be added, removed, or changed.
3. **Allow duplicates:** The same value can appear more than once.
4. **Multiple data types:** A list can contain strings, integers, and other Python objects.

Example:

```python
my_list = ["apple", 10, "banana", 20]
print(my_list)
```

Output:

```text
['apple', 10, 'banana', 20]
```

### 4.3 Common List Methods

| Method | Purpose |
|---|---|
| `append()` | Adds an element at the end |
| `remove()` | Removes the first matching element |
| `sort()` | Sorts elements in place |
| `insert()` | Adds an element at a specific position |
| `pop()` | Removes and returns an element |
| `clear()` | Removes all elements |

## 5. Task 1: Create a List of Fruits

### 5.1 Objective

Create a list containing three fruits and display the list using the `print()` function.

### 5.2 Create the Python File

Command:

```bash
cat > lists.py <<'EOF'
fruits = ["apple", "banana", "cherry"]
print("Initial list of fruits:", fruits)
EOF
```

### 5.3 Code Explanation

```python
fruits = ["apple", "banana", "cherry"]
print("Initial list of fruits:", fruits)
```

Explanation:

- `fruits` creates a variable.
- `[]` creates a Python list.
- Each fruit is stored as a string.
- `print()` displays the list contents.

### 5.4 Execute the Program

Command:

```bash
python3 lists.py
```

Expected output:

```text
Initial list of fruits: ['apple', 'banana', 'cherry']
```

### 5.5 Task 1 Result

The program successfully created and displayed a list containing three fruits.

## 6. Task 2: Append a New Fruit

### 6.1 Objective

Use the `append()` method to add `"orange"` to the end of the existing list.

### 6.2 Add Code to the Existing File

Command:

```bash
cat >> lists.py <<'EOF'

fruits.append("orange")
print("List after appending 'orange':", fruits)
EOF
```

### 6.3 Understanding append()

The `append()` method adds one new element to the end of an existing list.

Syntax:

```python
list_name.append(element)
```

Example:

```python
fruits.append("orange")
```

Before append:

```python
["apple", "banana", "cherry"]
```

After append:

```python
["apple", "banana", "cherry", "orange"]
```

Important points:

- `append()` modifies the original list.
- It adds the element at the end.
- It adds one element per call.

### 6.4 Execute the Program

Command:

```bash
python3 lists.py
```

Expected output:

```text
Initial list of fruits: ['apple', 'banana', 'cherry']
List after appending 'orange': ['apple', 'banana', 'cherry', 'orange']
```

### 6.5 Task 2 Result

The `append()` method successfully added `"orange"` to the fruit list.

## 7. Task 3: Remove a Fruit by Name

### 7.1 Objective

Use the `remove()` method to delete `"banana"` from the list.

### 7.2 Add Code to the Existing File

Command:

```bash
cat >> lists.py <<'EOF'

fruits.remove("banana")
print("List after removing 'banana':", fruits)
EOF
```

### 7.3 Understanding remove()

The `remove()` method deletes the first matching element from a list.

Syntax:

```python
list_name.remove(element)
```

Example:

```python
fruits.remove("banana")
```

Before removal:

```python
["apple", "banana", "cherry", "orange"]
```

After removal:

```python
["apple", "cherry", "orange"]
```

Important points:

- `remove()` modifies the original list.
- It removes the first matching occurrence.
- It raises `ValueError` if the requested element does not exist.

### 7.4 Execute the Program

Command:

```bash
python3 lists.py
```

Expected output for the removal operation:

```text
List after removing 'banana': ['apple', 'cherry', 'orange']
```

### 7.5 Test ValueError for a Missing Element

The lab also requires testing what happens when we remove an element that does not exist.

Command:

```bash
python3 -c 'f=["apple"]; f.remove("grape")'
```

Expected error:

```text
ValueError: list.remove(x): x not in list
```

Explanation:

- The list contains only `"apple"`.
- The program attempts to remove `"grape"`.
- Since `"grape"` does not exist, Python raises `ValueError`.

### 7.6 Safe Removal Using Membership Checking

We can prevent this error by checking whether an element exists before removing it.

Add the following code:

```python
if "grape" in fruits:
    fruits.remove("grape")
else:
    print("'grape' not in list, nothing removed")
```

Explanation:

- `if` checks a condition.
- `in` checks whether an element exists in a list.
- If `"grape"` exists, it is removed.
- Otherwise, the `else` block displays a message.

### 7.7 Add the Safe Removal Code

Command:

```bash
cat >> lists.py <<'EOF'

if "grape" in fruits:
    fruits.remove("grape")
else:
    print("'grape' not in list, nothing removed")
EOF
```

Execute:

```bash
python3 lists.py
```

Expected output:

```text
'grape' not in list, nothing removed
```

### 7.8 Task 3 Result

The program successfully removed `"banana"` and safely handled the missing `"grape"` element without crashing.

## 8. Task 4: Sort the List

### 8.1 Objective

Use the `sort()` method to arrange the fruits in ascending alphabetical order.

### 8.2 Add Code to the Existing File

Command:

```bash
cat >> lists.py <<'EOF'

fruits.sort()
print("Sorted list of fruits:", fruits)
EOF
```

### 8.3 Understanding sort()

The `sort()` method arranges elements of a list in ascending order by default.

Syntax:

```python
list_name.sort()
```

Example:

```python
fruits.sort()
```

Before sorting:

```python
["orange", "cherry", "apple"]
```

After sorting:

```python
["apple", "cherry", "orange"]
```

### 8.4 Important Concept: sort() Returns None

The `sort()` method changes the original list directly.

It does not return a new sorted list.

Incorrect example:

```python
fruits = fruits.sort()
```

This replaces `fruits` with `None`.

Correct example:

```python
fruits.sort()
print(fruits)
```

If we need a separate sorted list without changing the original, we can use:

```python
new_fruits = sorted(fruits)
```

### 8.5 Execute the Program

Command:

```bash
python3 lists.py
```

Expected output:

```text
Sorted list of fruits: ['apple', 'cherry', 'orange']
```

### 8.6 Task 4 Result

The `sort()` method successfully arranged the remaining fruits alphabetically.

## 9. Task 5: Iterate Over the List

### 9.1 Objective

Use a `for` loop to access and print each element of the list.

### 9.2 Add Code to the Existing File

Command:

```bash
cat >> lists.py <<'EOF'

for fruit in fruits:
    print("Fruit:", fruit)
EOF
```

### 9.3 Understanding List Iteration

Iteration means accessing elements one by one.

A `for` loop can be used to traverse a list.

Syntax:

```python
for item in list_name:
    print(item)
```

Our example:

```python
for fruit in fruits:
    print("Fruit:", fruit)
```

Explanation:

- `for` starts the loop.
- `fruit` is the loop variable.
- `in fruits` tells Python to take elements from the list.
- `print()` displays each element.
- The loop ends automatically after the last element.

### 9.4 Execute the Program

Command:

```bash
python3 lists.py
```

Expected final output:

```text
Fruit: apple
Fruit: cherry
Fruit: orange
```

### 9.5 Verify the Sorted List

Command:

```bash
python3 lists.py | grep "Sorted"
```

Expected output:

```text
Sorted list of fruits: ['apple', 'cherry', 'orange']
```

### 9.6 Task 5 Result

The `for` loop successfully accessed and printed every fruit in the sorted list.

## 10. Complete Python Program

The final `lists.py` program:

```python
fruits = ["apple", "banana", "cherry"]
print("Initial list of fruits:", fruits)

fruits.append("orange")
print("List after appending 'orange':", fruits)

fruits.remove("banana")
print("List after removing 'banana':", fruits)

if "grape" in fruits:
    fruits.remove("grape")
else:
    print("'grape' not in list, nothing removed")

fruits.sort()
print("Sorted list of fruits:", fruits)

for fruit in fruits:
    print("Fruit:", fruit)
```

## 11. Complete Program Output

Command:

```bash
python3 lists.py
```

Expected output:

```text
Initial list of fruits: ['apple', 'banana', 'cherry']
List after appending 'orange': ['apple', 'banana', 'cherry', 'orange']
List after removing 'banana': ['apple', 'cherry', 'orange']
'grape' not in list, nothing removed
Sorted list of fruits: ['apple', 'cherry', 'orange']
Fruit: apple
Fruit: cherry
Fruit: orange
```

## 12. Common Mistakes and Troubleshooting

### 12.1 Using Curly Brackets Instead of Square Brackets

Lists use square brackets `[]`.

Example:

```python
fruits = ["apple", "banana"]
```

### 12.2 Removing an Element That Does Not Exist

Incorrect:

```python
fruits.remove("grape")
```

If `"grape"` is missing, Python raises `ValueError`.

Correct:

```python
if "grape" in fruits:
    fruits.remove("grape")
```

### 12.3 Incorrect Indentation

Python uses indentation to define code blocks.

Correct:

```python
for fruit in fruits:
    print(fruit)
```

### 12.4 Assigning the Result of sort()

Incorrect:

```python
fruits = fruits.sort()
```

Correct:

```python
fruits.sort()
```

Remember that `sort()` returns `None`.

### 12.5 Misspelling List Methods

Python method names are case-sensitive.

Correct:

```python
fruits.append("orange")
fruits.remove("banana")
fruits.sort()
```

## 13. Python Concepts Learned

During this lab, I learned:

1. How to create lists using square brackets.
2. How to store multiple elements in one variable.
3. How to display list contents using `print()`.
4. How to add elements using `append()`.
5. How to remove elements using `remove()`.
6. How to identify and understand `ValueError`.
7. How to check list membership using `in`.
8. How to sort elements using `sort()`.
9. Why `sort()` returns `None`.
10. How to iterate through lists using a `for` loop.
11. How to execute Python scripts from the Linux terminal.
12. How to verify program output using `grep`.

## 14. Syntax Verification

Python syntax was checked using:

```bash
python3 -m py_compile lists.py
```

Result:

```text
Python syntax check: PASSED
```

No syntax errors were reported.

## 15. Testing and Verification Summary

| Test | Expected Result | Status |
|---|---|---|
| Python version | Python 3.12.3 | Passed |
| Create fruit list | Three fruits displayed | Passed |
| Append orange | Orange added at the end | Passed |
| Remove banana | Banana removed | Passed |
| Test missing item | ValueError generated | Passed |
| Safe grape removal | Missing-item message displayed | Passed |
| Sort list | Alphabetical order | Passed |
| Iterate over list | Three fruits printed | Passed |
| Verify sorted output | Correct sorted list | Passed |
| Python syntax check | No syntax errors | Passed |

## 16. Interview Questions and Answers

### Q1. What is a list in Python?

A list is a collection of elements stored in a single variable. Lists are created using square brackets.

### Q2. How do you create a list?

Example:

```python
fruits = ["apple", "banana", "cherry"]
```

### Q3. Are Python lists mutable?

Yes. Lists are mutable, which means we can add, remove, or modify their elements.

### Q4. What does append() do?

The `append()` method adds an element to the end of a list.

Example:

```python
fruits.append("orange")
```

### Q5. What does remove() do?

The `remove()` method deletes the first matching element from a list.

Example:

```python
fruits.remove("banana")
```

### Q6. What happens if remove() cannot find an element?

Python raises a `ValueError` exception.

### Q7. How can we check whether an item exists in a list?

We can use the `in` membership operator.

Example:

```python
if "apple" in fruits:
    print("Apple exists")
```

### Q8. What does sort() do?

The `sort()` method arranges list elements in ascending order by default.

### Q9. Does sort() return a new list?

No. It sorts the original list in place and returns `None`.

### Q10. What is the difference between sort() and sorted()?

- `sort()` modifies the original list.
- `sorted()` returns a new sorted list and leaves the original unchanged.

### Q11. How do you iterate through a list?

We can use a `for` loop.

Example:

```python
for fruit in fruits:
    print(fruit)
```

### Q12. What is the purpose of the in operator?

The `in` operator checks whether an element exists in a collection.

## 17. Repository Structure

The completed Lab 7 folder contains:

```text
Lab-07-Lists-and-List-Methods/
│
├── lists.py
├── README.md
│
└── evidence/
    ├── python-version.txt
    ├── syntax-check.txt
    ├── list-creation-and-append.txt
    └── removal-sorting-and-iteration.txt
```

### Evidence Files

- `python-version.txt`: Records the installed Python version.
- `syntax-check.txt`: Records the Python syntax verification.
- `list-creation-and-append.txt`: Records Task 1 and Task 2 outputs.
- `removal-sorting-and-iteration.txt`: Records Task 3, Task 4, and Task 5 outputs.

## 18. Conclusion

In this lab, I learned how to create, modify, manage, and iterate over Python lists.

I practiced the `append()`, `remove()`, and `sort()` methods and learned how to handle a missing list element safely using membership checking.

I also learned how to traverse a list using a `for` loop and verify program output through the Linux terminal.

These concepts provide a foundation for working with collections of data in Python and will be useful in future programming, automation, and data science tasks.

**Lab 7: Lists & List Methods — Practical tasks completed and verified.**
