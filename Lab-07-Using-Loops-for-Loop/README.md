

# Lab 07 — Using Loops (for Loop) in Python

## 1. Introduction

A `for` loop is used to repeat a block of code for each item in a sequence, such as a list.

In this lab, we created a list of names and used a `for` loop to print a greeting for each name.

## 2. Objectives

- Understand the purpose of a Python `for` loop.
- Learn how to iterate through a list.
- Print a message for every item in a list.
- Verify the program output.

## 3. Python List

A list stores multiple values in one variable.

Example:

```python
names = ["Alice", "Bob", "Charlie"]
```

The list contains three names.

## 4. For Loop Syntax

```python
for item in sequence:
    # Code to execute for each item
```

- `for` starts the loop.
- `item` represents the current value.
- `in` connects the variable to the sequence.
- The indented code runs for each item.

## 5. Complete Python Script

File: `greeting_script.py`

```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(f"Hello, {name}!")
```

## 6. How the Script Works

1. The `names` list stores three names.
2. The `for` loop takes the first name.
3. The `print()` statement displays its greeting.
4. The loop repeats for the remaining names.
5. The loop stops after processing all list items.

## 7. Run the Program

Command:

```bash
python3 greeting_script.py
```

Expected output:

```text
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

## 8. Count the Output Lines

Command:

```bash
python3 greeting_script.py | wc -l
```

Expected output:

```text
3
```

## 9. Syntax Validation

Command:

```bash
python3 -m py_compile greeting_script.py
```

The script passed Python syntax validation.

## 10. Key Learning Points

- A `for` loop repeats code for each item in a sequence.
- Lists can store multiple values.
- The loop variable represents the current item.
- Correct indentation is required in Python.
- A loop automatically finishes after processing all items.

## 11. Conclusion

In this lab, I learned how to use a Python `for` loop to iterate through a list and print a greeting for each name. I also verified the program output and checked its syntax.
