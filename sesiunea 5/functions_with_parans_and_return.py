# functions with params and return
def product(a, b):
    return a * b


p = product(3, 2)
p2 = product(11, 11)
print(p)
print(p2)


def get_all_even_numbers(numbers):
    numere_pare = []
    for number in numbers:
        if number % 2 == 0:
            numere_pare.append(number)
    return numere_pare


all_even = get_all_even_numbers([1, 2, 3, 4, 5, 6, 7, 8])
print(all_even)