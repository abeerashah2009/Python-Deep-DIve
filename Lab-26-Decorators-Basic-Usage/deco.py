import functools

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@log_decorator
def say_hello(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    say_hello("Alice")
