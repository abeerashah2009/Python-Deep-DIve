class MyContext:
    def __enter__(self):
        print("Entering the context and allocating resources.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context and cleaning up resources.")
        return False


with MyContext() as context:
    print("Running within the context block.")


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Opening file")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting: closing file")
        self.file.close()


# Using the FileManager context manager to handle file operations
with FileManager('/tmp/ctx_sample.txt', 'w') as f:
    print("Writing")
    f.write("Hello, World!")

print("File closed:", f.closed)
