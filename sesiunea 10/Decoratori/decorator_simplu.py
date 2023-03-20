import datetime
import functools


def my_decorator(func):
    def wrapper():
        print("before func")
        func()
        print("after func")
    return wrapper


@my_decorator
def say_hi():
    print("Hi")

say_hi()

# un decorator care executa functiile decorate doar pe timpul zilei

def not_durin_the_night(func):
    @functools.wraps(func)
    def wrapper():
        if  8 <= datetime.datetime.now().hour < 20 :
            func()
        else:
            pass
    return wrapper

@not_durin_the_night
def say_hello():
    print("Hello!")

say_hello()

print(say_hello)