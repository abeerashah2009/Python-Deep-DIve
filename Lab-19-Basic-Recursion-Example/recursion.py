import math
import sys


# Task 1 and Task 2: Recursive factorial
def factorial(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)


result = factorial(5)
print("The factorial of 5 is:", result)
print("Factorials of 0..7:", [factorial(i) for i in range(0, 8)])


# Task 3: Iterative factorial
def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


iter_result = iterative_factorial(5)
print("The factorial of 5 using iteration is:", iter_result)
print("Recursive equals iterative:", factorial(5) == iterative_factorial(5))


# Task 4: Tail-recursive factorial
def tail_recursive_factorial(n, accumulator=1):
    if n <= 1:
        return accumulator
    return tail_recursive_factorial(n - 1, n * accumulator)


tail_result = tail_recursive_factorial(5)
print("The factorial of 5 using tail recursion is:", tail_result)


# Demonstrate Python's recursion limit
print("Recursion limit:", sys.getrecursionlimit())

try:
    factorial(5000)
except RecursionError as e:
    print("RecursionError:", e)

try:
    tail_recursive_factorial(5000)
except RecursionError as e:
    print("Tail recursion also fails:", e)


# Iteration handles large values without recursion depth limits
big = iterative_factorial(5000)
print("Iterative factorial(5000) has", big.bit_length(), "bits")
print("Matches math.factorial:", big == math.factorial(5000))
print("Three methods for 5:", factorial(5), iterative_factorial(5), math.factorial(5))


# Modest recursion-limit demonstration
sys.setrecursionlimit(2000)
print("factorial(1500) works with limit 2000:", factorial(1500) == math.factorial(1500))
sys.setrecursionlimit(1000)
