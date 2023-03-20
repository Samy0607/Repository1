import functools


def repeat(n):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator_repeat


@repeat(5)
def say_hello(name):
    print(f"Hello {name}")
    return f"Hello {name}"


m = say_hello("Bob")
print(m)