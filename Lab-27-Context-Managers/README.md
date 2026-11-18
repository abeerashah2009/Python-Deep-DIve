# Lab 27: Context Managers (with Statement)

## 1. Introduction

In Python, a Context Manager is used to manage resources automatically.

It helps us open and close resources safely, such as:
- Files
- Database connections
- Network connections
- Locks

The `with` statement automatically handles setup and cleanup.

## 2. Important Methods

### `__enter__()`
- Runs when the `with` block starts.
- Used to initialize or allocate resources.
- Returns the resource or object.

### `__exit__()`
- Runs when the `with` block finishes.
- Used to release or clean up resources.
- Also runs if an exception occurs.

### `return False`
- Allows an exception to propagate.
- Does not suppress the exception.

## 3. Creating a Custom Context Manager

File: `ctx.py`

Created a class named `MyContext`.

It uses:
- `__enter__()` to start the context.
- `__exit__()` to clean up the context.

### Command

```bash
python3 ctx.py
```

### Output

```text
Entering the context and allocating resources.
Running within the context block.
Exiting the context and cleaning up resources.
```

### Verification

```bash
python3 ctx.py | grep -c Exiting
```

Output:

```text
1
```

This confirms that the first context manager exits exactly once.

## 4. FileManager Context Manager

Created a custom class named `FileManager`.

It automatically:
1. Opens a file using `open()`.
2. Allows writing inside the `with` block.
3. Closes the file through `__exit__()`.

File used: `/tmp/ctx_sample.txt`

### Output

```text
Opening file
Writing
Exiting: closing file
File closed: True
```

File content:

```text
Hello, World!
```

### Verification

```bash
python3 ctx.py | grep -c Exiting
```

Output:

```text
2
```

Both context managers successfully executed their cleanup methods.

## 5. Cleanup During an Exception

File: `ctx_exc.py`

Created a context manager that raises a `ValueError` inside the `with` block.

The `__exit__()` method still runs when the exception occurs.

### Command

```bash
python3 ctx_exc.py
```

### Output

```text
Enter
Body
Exiting, exception: ValueError
Caught outside: boom
```

### Important Note

Returning `False` from `__exit__()` allows the exception to propagate to the outer `except` block.

## 6. Generator-Based Context Manager

File: `ctx_gen.py`

Used Python's built-in `contextlib` module.

The `@contextmanager` decorator converts a generator function into a context manager.

### Important Points

- Code before `yield` runs when entering.
- `yield` separates entry and exit.
- Code inside `finally` runs during cleanup.

### Command

```bash
python3 ctx_gen.py
```

### Output

```text
Enter
Body
Exiting
```

## 7. Syntax Verification

Command:

```bash
python3 -m py_compile ctx.py ctx_exc.py ctx_gen.py
```

Result:

```text
Syntax check exit code: 0
```

All three Python scripts passed the syntax check.

## 8. Project Files

```text
Lab-27-Context-Managers/
├── README.md
├── ctx.py
├── ctx_exc.py
├── ctx_gen.py
└── evidence/
```

## 9. LMS Assessment

- Lab Name: Context Managers (with statement)
- Lab Number: 27
- Status: Passed
- Score: 100/100
- Total Time: 12h 14m
- Time Spent Today: 41m

## 10. What I Learned

After completing this lab, I learned:

- How Python context managers work.
- How to implement `__enter__()` and `__exit__()`.
- How to use the `with` statement.
- How to manage files automatically.
- How cleanup works when exceptions occur.
- How to use `contextlib.contextmanager`.
- How `try/finally` helps ensure resource cleanup.

## Conclusion

Context managers make Python resource management easier and safer.

They automatically handle resource cleanup when a `with` block finishes, even if an exception occurs.

This practical helped me understand custom context managers, file handling, exception management, and automatic cleanup in Python.
