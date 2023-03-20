# 1 functii ca argument

def say_hello(name):
    return f"hello {name}"


def say_hi(name):
    return f"Hi {name}"


def greet_Bob(func):
    return func("Bob")


print(greet_Bob(say_hi))
print(greet_Bob(say_hello))


# 2 Functii interioare
def parent():
    print("parent")

    def first_child():
        print("first_child")

    def sec_child():
        print("sec_child")

    sec_child()
    first_child()

parent()


# 3 Returnare de functii
def parent(m):
    def first_child():
        return "first child"

    def sec_child():
        return "sec_child"

    if m == 1:
        return first_child
    else:
        return sec_child


f = parent(7)
print(type(f))
print(f())