# Lab 9: Dictionaries & Key Operations in Python

## 1. Introduction

A **dictionary** is a built-in Python data type used to store information in key-value pairs.

Each item contains:
- **Key:** The name or identifier used to access data.
- **Value:** The information stored under that key.

Dictionaries are written using curly braces `{}`.

### Example

```python
user = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(user)
```

**Output:**

```text
{'name': 'Alice', 'age': 30, 'city': 'New York'}
```

### Important Points

- Dictionaries store data in key-value pairs.
- Each key must be unique.
- Values can be of different data types.
- Dictionaries are mutable, which means we can add, update, and remove items.
- Dictionaries preserve insertion order in modern Python.

---

## 2. Lab Objectives

After completing this lab, I learned how to:

1. Create a dictionary.
2. Access dictionary values.
3. Update existing values.
4. Safely access missing keys using `get()`.
5. Handle missing keys using `KeyError`.
6. Remove dictionary entries using `pop()`.
7. Iterate over dictionary items using `items()`.
8. Iterate over dictionary keys using `keys()`.

---

## 3. Environment and Prerequisites

### System Requirements

| Component | Version / Details |
|---|---|
| Operating System | Ubuntu 24.04 LTS |
| Python | 3.12.3 |
| Package Manager | APT |
| Editor | Nano |
| Terminal | Ubuntu Terminal |

### Install Python

Update the package list:

```bash
sudo apt update
```

Install Python 3 and the virtual environment package:

```bash
sudo apt install -y python3 python3-venv
```

Check the Python version:

```bash
python3 --version
```

**Output:**

```text
Python 3.12.3
```

### Create Working Directory

```bash
mkdir -p ~/dict-lab
cd ~/dict-lab
```

For this GitHub portfolio lab, the working directory is:

```text
~/Python-Deep-DIve/Lab-09-Dictionaries-and-Key-Operations
```

---

## 4. Understanding Python Dictionaries

### 4.1 Dictionary Syntax

Basic dictionary syntax:

```python
dictionary_name = {
    "key1": "value1",
    "key2": "value2"
}
```

Example:

```python
student = {
    "name": "Abeera",
    "course": "Python",
    "level": "Beginner"
}
```

### 4.2 Keys and Values

Consider:

```python
student = {
    "name": "Abeera",
    "age": 20
}
```

- `"name"` and `"age"` are keys.
- `"Abeera"` and `20` are values.

### 4.3 Mutable Data Type

A dictionary is mutable.

This means we can change its contents after creating it.

Example:

```python
student["age"] = 21
```

The age value is updated from 20 to 21.

---

## 5. Task 1: Create a Dictionary for a User Profile

### Objective

Create a dictionary containing basic user information, including name, age, and city.

### Python Code

```python
# Step 1: Initialize a dictionary with a user's profile
user_profile = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Step 2: Display the created dictionary
print(user_profile)
```

### Execution Command

```bash
python3 dict.py
```

### Expected Output

```text
{'name': 'Alice', 'age': 30, 'city': 'New York'}
```

### Explanation

1. `user_profile` is the dictionary variable.
2. `"name"` is a key and `"Alice"` is its value.
3. `"age"` is a key and `30` is its value.
4. `"city"` is a key and `"New York"` is its value.
5. `print()` displays the complete dictionary.

### Key Concept

A dictionary stores related information using unique keys.

---

## 6. Task 2: Access and Update Dictionary Values

### Objective

Learn how to access dictionary values and update existing entries.

### 6.1 Access a Value Using Square Brackets

Syntax:

```python
dictionary_name["key"]
```

Example:

```python
print(user_profile["name"])
```

**Output:**

```text
Alice
```

Explanation:

Square brackets access the value associated with the specified key.

### 6.2 Update a Dictionary Value

Example:

```python
user_profile["age"] = 31
```

Explanation:

- `"age"` is the existing key.
- `31` is the new value.
- The old value `30` is replaced with `31`.

Display the updated dictionary:

```python
print(user_profile)
```

**Output:**

```text
{'name': 'Alice', 'age': 31, 'city': 'New York'}
```

### 6.3 Safe Access Using get()

The `get()` method accesses a value without raising an error when the key is missing.

Syntax:

```python
dictionary_name.get("key", "default value")
```

Example:

```python
print(user_profile.get("email", "not set"))
```

**Output:**

```text
not set
```

Explanation:

- `"email"` does not exist in the dictionary.
- `"not set"` is returned as the default value.
- The program continues without an error.

### 6.4 Handling KeyError

When we access a missing key using square brackets, Python raises a `KeyError`.

Example:

```python
try:
    user_profile["email"]
except KeyError as e:
    print("KeyError for missing key:", e)
```

**Output:**

```text
KeyError for missing key: 'email'
```

### Important Difference

| Method | Behaviour |
|---|---|
| `dict["key"]` | Raises KeyError if the key is missing |
| `dict.get("key")` | Returns None if the key is missing |
| `dict.get("key", default)` | Returns the specified default value |

### Key Concept

Use square brackets when the key is expected to exist. Use `get()` when the key might be missing.

---

## 7. Task 3: Remove a Key from the Dictionary

### Objective

Remove the `"city"` key and verify that it no longer exists.

### 7.1 Remove an Entry Using pop()

The `pop()` method removes a specified key and returns its value.

Syntax:

```python
dictionary_name.pop("key")
```

Example:

```python
removed = user_profile.pop("city")
print("Removed value:", removed)
```

**Output:**

```text
Removed value: New York
```

### 7.2 Display the Updated Dictionary

```python
print("Profile after removing city:", user_profile)
```

**Output:**

```text
Profile after removing city: {'name': 'Alice', 'age': 31}
```

### 7.3 Verify Key Removal Using assert

```python
assert 'city' not in user_profile
print("Verified: 'city' is not in user_profile")
```

**Output:**

```text
Verified: 'city' is not in user_profile
```

### Explanation

- `pop("city")` removes the city entry.
- The removed value is stored in the `removed` variable.
- `assert` checks whether the city key is absent.
- If the condition is false, Python raises an `AssertionError`.

### Key Concept

The `pop()` method removes a dictionary entry and returns its value.

---

## 8. Task 4: Iterate Over Dictionary Items and Keys

### Objective

Learn how to loop through dictionary items and keys.

### 8.1 Iterate Using items()

The `items()` method returns a view of the dictionary's key-value pairs.

Syntax:

```python
for key, value in dictionary_name.items():
    print(key, value)
```

Example:

```python
for key, value in user_profile.items():
    print(f"{key}: {value}")
```

**Output:**

```text
name: Alice
age: 31
```

Explanation:

- `items()` provides both keys and values.
- `key` stores the current key.
- `value` stores the corresponding value.
- The loop processes each dictionary entry.

### 8.2 Iterate Using keys()

The `keys()` method returns a view containing all dictionary keys.

Syntax:

```python
for key in dictionary_name.keys():
    print(key)
```

Example:

```python
for key in user_profile.keys():
    print(f"Key: {key}")
```

**Output:**

```text
Key: name
Key: age
```

### Difference Between items() and keys()

| Method | Purpose |
|---|---|
| `items()` | Returns key-value pairs |
| `keys()` | Returns dictionary keys |
| `values()` | Returns dictionary values |

### Important Note

Do not add or remove dictionary keys while directly iterating over the dictionary. This can raise a `RuntimeError`.

If entries need to be removed during iteration, iterate over a copy:

```python
for key in list(user_profile):
    if key == "age":
        user_profile.pop(key)
```

---

## 9. Complete Lab Program

The following is the complete `dict.py` program implemented in this lab.

```python
# Task 1: Create a dictionary for a user profile
user_profile = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Display the created dictionary
print(user_profile)

# Task 2: Access and update dictionary values
print("User's Name:", user_profile["name"])

user_profile["age"] = 31

print("Updated User Profile:", user_profile)

# Safe access using get()
print("Email:", user_profile.get("email", "not set"))

# Handle a missing key using KeyError
try:
    user_profile["email"]
except KeyError as e:
    print("KeyError for missing key:", e)

# Task 3: Remove city using pop()
removed = user_profile.pop("city")

print("Removed value:", removed)
print("Profile after removing city:", user_profile)

# Verify city key is removed
assert 'city' not in user_profile

print("Verified: 'city' is not in user_profile")

# Task 4: Iterate over dictionary items
for key, value in user_profile.items():
    print(f"{key}: {value}")

# Iterate over dictionary keys
for key in user_profile.keys():
    print(f"Key: {key}")
```

---

## 10. Complete Program Output

Command:

```bash
python3 dict.py
```

Output:

```text
{'name': 'Alice', 'age': 30, 'city': 'New York'}
User's Name: Alice
Updated User Profile: {'name': 'Alice', 'age': 31, 'city': 'New York'}
Email: not set
KeyError for missing key: 'email'
Removed value: New York
Profile after removing city: {'name': 'Alice', 'age': 31}
Verified: 'city' is not in user_profile
name: Alice
age: 31
Key: name
Key: age
```

---

## 11. Common Dictionary Methods

| Method | Description |
|---|---|
| `get()` | Safely retrieves a value |
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns key-value pairs |
| `pop()` | Removes a specified key and returns its value |
| `update()` | Adds or updates entries |
| `clear()` | Removes all dictionary entries |
| `copy()` | Creates a shallow copy |

### Additional Examples

**Using update():**

```python
user_profile.update({"email": "alice@example.com"})
```

**Using values():**

```python
print(user_profile.values())
```

**Using copy():**

```python
profile_copy = user_profile.copy()
```

---

## 12. Common Mistakes and Troubleshooting

### Mistake 1: Accessing a Missing Key

Incorrect:

```python
print(user_profile["email"])
```

If email does not exist, Python raises `KeyError`.

Solution:

```python
print(user_profile.get("email", "not set"))
```

### Mistake 2: Using Duplicate Keys

Example:

```python
student = {
    "name": "Alice",
    "name": "Bob"
}
```

The later value replaces the earlier value.

Result:

```text
{'name': 'Bob'}
```

Remember: dictionary keys must be unique.

### Mistake 3: Using Incorrect Brackets

Incorrect:

```python
student = ["name": "Alice"]
```

Correct:

```python
student = {"name": "Alice"}
```

Dictionaries use curly braces `{}`.

### Mistake 4: Removing a Missing Key

Example:

```python
user_profile.pop("country")
```

If the key does not exist and no default is supplied, Python raises `KeyError`.

---

## 13. Important Python Concepts Learned

| Concept | What I Learned |
|---|---|
| Dictionary | Stores data in key-value pairs |
| Key | Identifies a dictionary entry |
| Value | Stores information associated with a key |
| Mutable | Dictionary contents can be changed |
| Square brackets | Access and update values |
| `get()` | Safely access potentially missing keys |
| `KeyError` | Error raised when a missing key is accessed |
| `pop()` | Removes an entry and returns its value |
| `assert` | Checks whether a condition is true |
| `items()` | Iterates over key-value pairs |
| `keys()` | Iterates over dictionary keys |
| `values()` | Accesses dictionary values |

---

## 14. Testing and Verification

The following checks were completed:

| Test | Result |
|---|---|
| Python version check | Passed |
| Dictionary creation | Passed |
| Access dictionary value | Passed |
| Update dictionary value | Passed |
| Safe access with get() | Passed |
| Handle missing key with KeyError | Passed |
| Remove city using pop() | Passed |
| Verify key removal using assert | Passed |
| Iterate using items() | Passed |
| Iterate using keys() | Passed |
| Python syntax compilation | Passed |

### Syntax Verification

Command:

```bash
python3 -m py_compile dict.py
```

Result:

```text
Python syntax check: PASSED
```

No syntax errors were reported.

---

## 15. Interview Questions and Answers

### Q1. What is a dictionary in Python?

A dictionary is a built-in data type that stores information in key-value pairs.

### Q2. How do you create a dictionary?

We create a dictionary using curly braces `{}`.

Example:

```python
student = {"name": "Alice", "age": 20}
```

### Q3. What is a key-value pair?

A key-value pair consists of a unique key and its associated value.

### Q4. Can dictionary values be changed?

Yes. Dictionaries are mutable, so we can add, update, and remove entries.

### Q5. How do you access a dictionary value?

We use square brackets with the key.

```python
student["name"]
```

### Q6. What is the purpose of get()?

The `get()` method safely retrieves a value. It can return a default value if the key does not exist.

### Q7. What is KeyError?

`KeyError` is an exception raised when we try to access a dictionary key that does not exist.

### Q8. What does pop() do?

The `pop()` method removes a specified key and returns its value.

### Q9. What is the difference between keys() and items()?

`keys()` returns dictionary keys, while `items()` returns key-value pairs.

### Q10. What does values() return?

It returns a view of all values in the dictionary.

### Q11. Can a dictionary contain duplicate keys?

No. Each key must be unique. If a key is repeated, its later value replaces the earlier value.

### Q12. What does update() do?

The `update()` method adds new entries or updates existing entries.

### Q13. What is the use of assert?

`assert` checks whether a condition is true. If false, Python raises an `AssertionError`.

### Q14. What is the difference between a list and a dictionary?

A list stores items by position (index), while a dictionary stores values using keys.

### Q15. Why are dictionaries useful?

Dictionaries make it easy to store, organize, access, and update related information.

---

## 16. Repository Structure

```text
Lab-09-Dictionaries-and-Key-Operations/
│
├── README.md
├── dict.py
│
└── evidence/
    ├── python-version.txt
    ├── dict-output.txt
    └── syntax-check.txt
```

### Evidence Files

- `python-version.txt` — records the installed Python version.
- `dict-output.txt` — contains the complete program output.
- `syntax-check.txt` — records the Python syntax verification result.

---

## 17. Conclusion

In this lab, I learned how to work with Python dictionaries and perform their important operations.

I practised creating dictionaries, accessing values, updating entries, handling missing keys, removing entries, and iterating over keys and key-value pairs.

I also learned how to use `get()`, `pop()`, `items()`, `keys()`, and exception handling with `KeyError`.

These skills are useful when working with structured data, configuration files, APIs, and JSON data in Python.

**Lab 9: Dictionaries & Key Operations — Practical Tasks Completed.**
