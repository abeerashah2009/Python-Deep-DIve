class MyContext:
    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting, exception:", exc_type.__name__ if exc_type else None)
        return False


try:
    with MyContext():
        print("Body")
        raise ValueError("boom")
except ValueError as e:
    print("Caught outside:", e)
