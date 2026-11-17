# Lab 12 – File I/O Basics in Python

## 1. Overview

This lab covers the fundamentals of File Input and Output (File I/O) in Python.

File I/O allows Python programs to create, read, write, and update files. It is useful for storing information permanently instead of keeping data only in program memory.

In this lab, I practised:
- Creating and writing to a text file.
- Appending new content to an existing file.
- Reading files line by line.
- Handling missing-file errors.
- Using context managers to manage files safely.

## 2. Learning Objectives

After completing this lab, I can:

1. Explain basic File I/O operations.
2. Open files using Python's built-in `open()` function.
3. Write text into files.
4. Append information without overwriting existing content.
5. Read files using a loop.
6. Handle `FileNotFoundError`.
7. Use context managers with the `with` statement.
8. Verify that files close automatically.

## 3. Environment

| Component | Details |
|---|---|
| Operating System | Ubuntu 24.04 |
| Programming Language | Python |
| Python Version | 3.12.3 |
| Editor | Nano |
| Terminal | Ubuntu Terminal |
| Repository | Python-Deep-DIve |
| Lab Directory | Lab-12-File-IO-Basics |

## 4. Understanding File I/O

File I/O stands for File Input and Output.

- **Input:** Reading information from a file.
- **Output:** Writing information into a file.

Python provides the built-in `open()` function for file operations.

### 4.1 Basic Syntax

```python
open("filename.txt", "mode", encoding="utf-8")
```

Parameters:

- `filename`: Name or path of the file.
- `mode`: Defines how the file should be opened.
- `encoding`: Defines the text encoding.

### 4.2 Common File Modes

| Mode | Description |
|---|---|
| `r` | Read an existing file |
| `w` | Write to a file; overwrites existing content |
| `a` | Append content at the end of a file |
| `x` | Create a new file; fails if it already exists |
| `r+` | Read and write an existing file |

## 5. Task 1 – Writing Files

### 5.1 Objective

Create a text file and write multiple lines using Python.

### 5.2 Python Script

File: `write_file.py`

```python
# write_file.py

# Open the file output.txt in write mode
with open('output.txt', 'w', encoding='utf-8') as f:

    # Write multiple lines to the file
    f.write("Hello, World!\n")
    f.write("This is a file I/O example.\n")
    f.write("Python makes File I/O easy!\n")
```

### 5.3 Explanation

- `open()` opens the file.
- `'w'` selects write mode.
- `encoding='utf-8'` specifies text encoding.
- `f.write()` writes text into the file.
- `\n` adds a new line.
- `with` manages the file resource and closes it automatically.

### 5.4 Execution

```bash
python3 write_file.py
cat output.txt
```

### 5.5 Expected Output

```text
Hello, World!
This is a file I/O example.
Python makes File I/O easy!
```

## 6. Appending Data to a File

### 6.1 Objective

Add new information to an existing file without removing its previous content.

### 6.2 Python Code

```python
with open('output.txt', 'a', encoding='utf-8') as f:
    f.write("This line was appended.\n")
```

### 6.3 Explanation

- `'a'` means append mode.
- Append mode adds content at the end of the file.
- Existing content remains unchanged.

### 6.4 Verification

```bash
tail -n 2 output.txt
```

Expected output:

```text
Python makes File I/O easy!
This line was appended.
```

## 7. Task 2 – Reading Files

### 7.1 Objective

Read a text file line by line and display its contents.

### 7.2 Python Script

File: `read_file.py`

```python
# read_file.py

# Open the file output.txt in read mode
with open('output.txt', 'r', encoding='utf-8') as f:

    # Read each line in the file
    for line in f:

        # Print the line to the console
        print(line.strip())
```

### 7.3 Explanation

- `'r'` opens the file in read mode.
- `for line in f` processes the file line by line.
- `line.strip()` removes surrounding whitespace, including newline characters.
- `print()` displays each line.

### 7.4 Execution

```bash
python3 read_file.py
```

### 7.5 Output

```text
Hello, World!
This is a file I/O example.
Python makes File I/O easy!
This line was appended.
```

### 7.6 First-Line Verification

Command:

```bash
python3 read_file.py | head -1 | grep 'Hello, World!'
```

Expected result:

```text
Hello, World!
```

## 8. Handling Missing Files

### 8.1 Objective

Understand how Python handles attempts to read files that do not exist.

### 8.2 Python Code

```python
try:
    with open('missing.txt', 'r', encoding='utf-8') as f:
        print(f.read())

except FileNotFoundError as e:
    print("Caught:", e)
```

### 8.3 Explanation

- `try` contains code that may generate an exception.
- `except` handles the exception.
- `FileNotFoundError` occurs when the requested file cannot be found.
- Exception handling prevents this expected error from terminating the program unexpectedly.

### 8.4 Verified Output

```text
Caught: [Errno 2] No such file or directory: 'missing.txt'
```

## 9. Task 3 – Context Managers

### 9.1 What Is a Context Manager?

A context manager manages resources automatically.

In Python, the `with` statement is commonly used for opening files.

It automatically closes the file after the block finishes, even if an exception occurs inside the block.

### 9.2 Example

```python
with open('output.txt', 'r', encoding='utf-8') as f:
    print("Inside with, closed =", f.closed)

print("After with, closed =", f.closed)
```

### 9.3 Explanation

- `f.closed` checks whether the file is closed.
- Inside the `with` block, the file remains open.
- After leaving the block, Python closes the file automatically.

### 9.4 Verified Output

```text
Inside with, closed = False
After with, closed = True
```

## 10. Important File I/O Functions

| Function | Purpose |
|---|---|
| `open()` | Opens a file |
| `write()` | Writes text into a file |
| `read()` | Reads the complete file |
| `readline()` | Reads one line |
| `readlines()` | Reads lines into a list |
| `close()` | Closes a file |
| `strip()` | Removes surrounding whitespace |

## 11. Difference Between Write and Append

| Write Mode (`w`) | Append Mode (`a`) |
|---|---|
| Writes content to a file | Adds content to a file |
| Replaces existing content | Preserves existing content |
| Creates a file if missing | Creates a file if missing |
| Useful for creating fresh output | Useful for adding new records |

## 12. Project Structure

```text
Lab-12-File-IO-Basics/
│
├── README.md
├── write_file.py
├── read_file.py
├── output.txt
│
└── evidence/
    ├── append-output.txt
    ├── context-manager-check.txt
    ├── first-line-check.txt
    ├── missing-file-error.txt
    ├── python-version.txt
    ├── read-output.txt
    ├── write-and-append-output.txt
    └── write-output.txt
```

## 13. Evidence and Verification

The `evidence/` directory contains the recorded results of the practical exercises.

| Evidence File | Verification |
|---|---|
| `python-version.txt` | Python version |
| `write-output.txt` | Initial file-writing result |
| `append-output.txt` | Append operation |
| `write-and-append-output.txt` | Final file content |
| `read-output.txt` | File-reading result |
| `first-line-check.txt` | First-line verification |
| `missing-file-error.txt` | Exception handling |
| `context-manager-check.txt` | Automatic file closing |

## 14. Common Mistakes and Troubleshooting

### 14.1 FileNotFoundError

**Cause:** The requested file does not exist at the specified path.

**Solution:** Check the filename and directory before opening the file.

### 14.2 Overwriting Existing Content

**Cause:** Opening a file using `'w'` replaces its existing content.

**Solution:** Use `'a'` when you want to add content without overwriting previous data.

### 14.3 Forgetting to Close a File

**Cause:** A file is opened without properly managing its lifecycle.

**Solution:** Use the `with` statement to close the file automatically.

### 14.4 Incorrect File Path

**Cause:** The program is running from a different working directory.

**Solution:** Check the current directory using:

```bash
pwd
```

## 15. Best Practices

1. Use context managers when working with files.
2. Specify an appropriate encoding, such as UTF-8.
3. Use the correct file mode.
4. Handle expected exceptions.
5. Check file paths before reading files.
6. Avoid using write mode when existing data must be preserved.
7. Verify file contents after writing.

## 16. Interview Questions and Answers

**Q1. What is File I/O in Python?**

File I/O means File Input and Output. It allows Python programs to read information from files and write information into files.

**Q2. What does the `open()` function do?**

It opens a file so that a Python program can perform operations such as reading or writing.

**Q3. What is the difference between `w` and `a` modes?**

`w` overwrites existing content, while `a` adds new content at the end of the file.

**Q4. What is read mode?**

Read mode (`r`) opens an existing file to retrieve its contents.

**Q5. What is a context manager?**

A context manager manages resources automatically. The `with` statement is commonly used to manage files.

**Q6. Why should we use `with open()`?**

It automatically closes the file after the block finishes, helping prevent resource leaks.

**Q7. What is `FileNotFoundError`?**

It is an exception raised when Python tries to access a file that does not exist at the specified path.

**Q8. What does `strip()` do?**

It removes whitespace from the beginning and end of a string.

**Q9. What does `f.closed` return?**

It returns `True` if the file is closed and `False` if it is open.

**Q10. What is UTF-8?**

UTF-8 is a widely used text encoding that supports many characters and languages.

## 17. Final Testing

The following practical checks were completed:

- [x] Python version checked.
- [x] File created using write mode.
- [x] Multiple lines written successfully.
- [x] New content appended successfully.
- [x] File read line by line.
- [x] First line verified.
- [x] Missing-file exception handled.
- [x] Context manager tested.
- [x] Automatic file closing verified.
- [x] Evidence files captured.

## 18. Conclusion

In this lab, I learned how to perform basic File I/O operations in Python.

I practised writing, appending, and reading text files. I also learned how to handle missing-file errors and use context managers to manage file resources safely.

These concepts are useful for building Python applications that store, retrieve, and process data from files.

**Lab 12 – File I/O Basics completed successfully.**
