# Lab 29 - Multiprocessing Basics

## 1. Objective
- Understand Python multiprocessing.
- Create and run multiple processes.
- Understand process IDs (PIDs).
- Learn the difference between processes and threads.
- Understand separate memory spaces.

## 2. Requirements
- Ubuntu Linux
- Python 3.12
- Python multiprocessing module

## 3. Files
- `mp.py` - Creates two processes to calculate the sum of a large list.
- `isolation.py` - Demonstrates memory isolation between parent and child processes.

## 4. Multiprocessing
- Multiprocessing runs tasks using separate processes.
- Each process has its own process ID (PID).
- The `Process()` function creates a new process.
- `start()` starts the process.
- `join()` waits for the process to finish.
- `if __name__ == '__main__':` protects the main program.

## 5. Output Verification
- Expected sum: `499999500000`
- Sum calculated four times successfully.
- Two separate child process IDs verified.
- Three unique PIDs confirmed, including the parent.

## 6. Memory Isolation
- Child process output: `[1]`
- Parent process output: `[]`
- Changes made in the child process did not change the parent's list.

## 7. Important Commands
```bash
python3 mp.py
python3 isolation.py
python3 -m py_compile mp.py isolation.py
```

## 8. Key Learning
- Processes have separate memory spaces.
- Threads share memory within the same process.
- Multiprocessing is useful for CPU-bound tasks.
- Passing large data between processes can create overhead.

## 9. Result
- All practical tasks completed successfully.
- Python syntax verification passed.
- Al Nafi LMS Score: **100/100**.
