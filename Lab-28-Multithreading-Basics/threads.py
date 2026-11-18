import threading

def print_numbers(thread_name, start, end):
    """Prints numbers from start to end."""
    for number in range(start, end):
        print(f"{thread_name}: {number}")

# Create threads
thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 0, 5))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 5, 10))

# Start threads
thread1.start()
thread2.start()

# Join threads
thread1.join()
thread2.join()

# Shared counter race demo
import time

THREADS = 4
ITERATIONS = 100000
counter = 0
lock = threading.Lock()

def unsafe_increment():
    global counter
    for _ in range(ITERATIONS):
        value = counter
        time.sleep(0)  # yield to other threads between read and write
        counter = value + 1

def safe_increment():
    global counter
    for _ in range(ITERATIONS):
        with lock:
            value = counter
            time.sleep(0)
            counter = value + 1

def run(target):
    global counter
    counter = 0
    workers = [threading.Thread(target=target) for _ in range(THREADS)]
    for w in workers:
        w.start()
    for w in workers:
        w.join()
    return counter

print(f"Expected: {THREADS * ITERATIONS}")
print(f"Without lock: {run(unsafe_increment)}")
print(f"With lock: {run(safe_increment)}")
