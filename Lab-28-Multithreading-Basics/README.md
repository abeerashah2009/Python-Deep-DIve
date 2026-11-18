# Lab 28 - Multithreading Basics

## 1. Introduction

Multithreading is a Python concept that allows multiple threads to run within one program.

A thread is a small unit of execution.

Python provides the `threading` module to create and manage threads.

## 2. Import Threading Module

First, import the threading module.

```python
import threading
```

**Command:**

```bash
python3 -c "import threading; print('threading OK')"
```

**Output:**

```text
threading OK
```

## 3. Create a Thread Function

A function named `print_numbers()` is created to print numbers.

It accepts three arguments:

- `thread_name` – Name of the thread.
- `start` – Starting number.
- `end` – Ending number.

The `range()` function generates the numbers.

## 4. Create Threads

Two threads are created using `threading.Thread()`.

- Thread-1 prints numbers from 0 to 4.
- Thread-2 prints numbers from 5 to 9.

**Important:** `target` specifies the function to execute, while `args` passes arguments to that function.

## 5. Start and Join Threads

Two important methods are used:

**start():** Starts the thread.

**join():** Waits until the thread finishes its execution.

Command:

```python
thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

**Verification:**

```bash
python3 threads.py
```

The program prints 10 number lines.

## 6. Race Condition

A race condition occurs when multiple threads access and modify shared data at the same time.

Because threads may interfere with each other's updates, the final result can become incorrect.

### Example: Shared Counter

In this lab, four threads update one shared counter.

- Number of threads: 4
- Iterations per thread: 100000
- Expected counter: 400000

### Without Lock

The `unsafe_increment()` function updates the counter without using a lock.

Some updates may be lost because multiple threads access the counter at the same time.

### With Lock

The `safe_increment()` function uses `threading.Lock()`.

The `with lock:` statement protects the counter update.

Only one thread can execute the protected section at a time.

**Result:**

- Without lock: A value below 400000.
- With lock: 400000.

## 7. Important Python Methods

| Method | Purpose |
|---|---|
| `threading.Thread()` | Creates a thread |
| `start()` | Starts a thread |
| `join()` | Waits for a thread to finish |
| `threading.Lock()` | Creates a lock |
| `with lock:` | Protects shared operations |

## 8. Verification Commands

Check the locked counter:

```bash
python3 threads.py | grep "With lock: 400000"
```

Expected output:

```text
With lock: 400000
```

Check total output lines:

```bash
python3 threads.py | wc -l
```

Expected output:

```text
13
```

Check Python syntax:

```bash
python3 -m py_compile threads.py
```

## 9. Real-Life Example - Bank Account

Imagine two people withdrawing money from the same bank account at the same time.

Without proper synchronization, both transactions may read the same balance and cause an incorrect update.

A lock protects the balance update and helps prevent lost updates.

## 10. Final Result

**Lab Name:** Multithreading Basics

**LMS Score:** 100 / 100

**Status:** Passed

**Evaluator:** Al Baari

## 11. Conclusion

In this lab, I learned how to create and execute multiple threads using Python.

I also learned about race conditions and how locks protect shared data.

Multithreading is useful when a program needs to handle multiple tasks concurrently.
