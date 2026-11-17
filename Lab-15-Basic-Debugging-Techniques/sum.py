def calculate_sum(numbers):
    total = 0

    for num in numbers:
        total += num
        print("Debug: Adding", num, "Total so far:", total)

    return total


# Test the function
numbers = [5, 10, 15]
print("Final Sum:", calculate_sum(numbers))
