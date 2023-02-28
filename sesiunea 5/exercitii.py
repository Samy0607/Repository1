#1 Sa se scrie o fct care primeste oricati params si de orice fel si returneaza lista valorilor argumentelor

def get_all_param_values(*args,**kwargs):
    return list(args) + list(kwargs.values())

print(get_all_param_values(1,2,3,a=6,b=5,c=2))

# 2 Sa se scrie o fct care primeste ca parametri doua numere si returneaza pe cel mai mare

def get_max(a, b):
    return a if a > b else b


print(get_max(2, 3))
print(get_max(3, 2))

# 3 Sa se scrie o fct care primeste ca parametri o lista si un numar.
# Functia va returna de cate ori apare acel numar in lista. iar daca nu apare deloc va arunca o eroare

def numarare(elements, elem):
    count = 0
    for m in elements:
        if m == elem:
            count += 1
    if not count:
        raise Exception("Element not found")
    return count


print(numarare([1, 2, 3, 3, 3, 4, 5], 3))
print(numarare([1, 2, 3, 3, 3, 4, 5], 9))