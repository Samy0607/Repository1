from contextlib import contextmanager
from time import perf_counter, sleep


class FileManager:
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self,exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager ("test.txt","w") as f:
    f.write("test")

@contextmanager
def file_manager(filename,mode):
    f = open(filename,mode)
    yield f
    f.close()

with file_manager("test.txt","w")   as f:
    f.write("test2")


class HelloContextManager:
    def __enter__(self):
        print("entering the context")
        return "Hello world"
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("leaving the context")
        if exc_type == IndexError:
            print(f"Exception message: {exc_val}")
            return True #eroarea nu se mai propaga la consola


with HelloContextManager() as hello :
    print(hello)
    print(10)
    hello[100]

"""
Sa se scrie un context manager care masoara durata de executie a blocului de cod din interior
"""
class Timer:
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = perf_counter()
        print(self.stop -self.start)

with Timer():
    sleep(3)