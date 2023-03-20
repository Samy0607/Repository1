import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@do_twice
def say_hello(name):
    print(f"Hello {name}")


say_hello("Bob")