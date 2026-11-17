# Task 1: Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Numbers:", numbers)

# Task 2: Use map with lambda to double each number
# map returns an iterator, so convert it into a list
doubled_numbers = list(map(lambda x: x * 2, numbers))

print("Doubled Numbers:", doubled_numbers)

# Task 3: Use filter with lambda to select even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)

# Equivalent list comprehension
print("Even (comprehension):", [x for x in numbers if x % 2 == 0])

# Task 4: Import reduce from functools
from functools import reduce

# Use reduce with lambda to calculate the sum
total_sum = reduce(lambda x, y: x + y, numbers)

print("Sum of Numbers:", total_sum)
