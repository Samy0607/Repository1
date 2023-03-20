# yield
# folosit in cadrul unei functii

def func():
    print("before_yield")
    yield 10
    print("after_yield")

# i = func()
# print(next(i))
# print(next(i))

def even_generator(n):
    generated_nrs = 0
    nr = 0
    while generated_nrs < n:
        nr += 1
        if nr % 2 == 0:
            yield nr
            generated_nrs += 1

gen = even_generator(10)

for i in gen:
    print(i)