# Task 1: Variable Positional Arguments (*args)

def sum_numbers(*args):
    return sum(args)


def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


# Task 1 test
assert add_numbers(1, 2, 3, 4, 5) == 15
print("add_numbers(1, 2, 3, 4, 5) =", add_numbers(1, 2, 3, 4, 5))


# Task 2: Variable Keyword Arguments (**kwargs)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Task 2 test
print("--- show_info ---")
show_info(name="Alice", age=30, city="New York")


# Task 3: Unpacking at the call site

numbers = [1, 2, 3, 4]
assert sum_numbers(*numbers) == 10
print("sum_numbers(*numbers) =", sum_numbers(*numbers))

data = {'name': 'John', 'age': 25}
print("--- print_kwargs(**data) ---")
print_kwargs(**data)

info = {'occupation': 'Engineer', 'country': 'USA'}
print("--- show_info(**info) ---")
show_info(**info)


# Both operators in one call
def describe(*args, **kwargs):
    return len(args), sorted(kwargs)


assert describe(*numbers, **info) == (4, ['country', 'occupation'])
print("describe(*numbers, **info) =", describe(*numbers, **info))

print("All tests passed")
