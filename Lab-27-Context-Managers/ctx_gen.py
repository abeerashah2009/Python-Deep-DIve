from contextlib import contextmanager


@contextmanager
def my_context():
    print("Enter")
    try:
        yield
    finally:
        print("Exiting")


with my_context():
    print("Body")
