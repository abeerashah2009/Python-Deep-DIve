# Task 1: list comprehension to generate squares
squares = [x**2 for x in range(10)]
print(squares)

# Filtered comprehension: only even numbers
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# Task 2: dictionary comprehension
words = ["apple", "banana", "cherry", "date"]
lengths = {word: len(word) for word in words}
print(lengths)

# Filtered dictionary comprehension: words longer than 4 letters
long_words = {word: len(word) for word in words if len(word) > 4}
print(long_words)

# Task 3: loop vs comprehension
squares_loop = []
for x in range(10):
    squares_loop.append(x**2)

squares_comp = [x**2 for x in range(10)]
print(squares_loop == squares_comp)
