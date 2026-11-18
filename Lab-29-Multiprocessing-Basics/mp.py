import multiprocessing
import os
import time

def sum_large_list(num_list):
    total = sum(num_list)
    print(f"Sum of the list is: {total} (pid {os.getpid()})")

if __name__ == '__main__':
    numbers = list(range(1000000))
    print(f"Parent pid: {os.getpid()}")

    start = time.time()
    sum_large_list(numbers)
    sum_large_list(numbers)
    print(f"Sequential time: {time.time() - start:.3f}s")

    start = time.time()
    process1 = multiprocessing.Process(target=sum_large_list, args=(numbers,))
    process2 = multiprocessing.Process(target=sum_large_list, args=(numbers,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print(f"Multiprocessing time: {time.time() - start:.3f}s")
