from time import perf_counter

1.
def time(func):
    def wrapper(*args, **kwargs):
        inceput = perf_counter()
        func(*args, **kwargs)
        final = perf_counter()
        print(f"{final-inceput}")

    return wrapper

@time
def calcul():
    print("Bine e cand e bine")

calcul()