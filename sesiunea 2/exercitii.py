'''
1. Sa se scrie un program care citeste 2 nr de la tastatura si afiseaza urmatoarele informatii:
    a. Daca primul numar este par
    b. Daca al doilea numar este impar
    c. Suma numerelor
    d. Catul numerelor daca al doilea este diferit de 0, altfel se afiseaza un mesaj in care se specifica “Catul nu se poate realiza”
    e. Primul numar ridicat la puterea al doilea numar
    f. Care este numar mai mare
    g. Daca ambele numere sunt pozitive
    h. Daca ambele numere sunt negative
'''

# a = int(input("introdu un nr: "))
# b = int(input("introdu un nr2: "))
#
# # a - daca primul nr e par
# if a % 2 == 0 :
#     print("a. primul numar e par")
# else:
#     print("a. ---")
#
# # b . daca al doilea este impar fara sa folosim operatori de comparatie
# if b % 2 :
#     print("b. al deoilea este impar")
# else:
#     print("b. ----")
#
# # c. suma numerelor
# print(f"c. Suma numerelor este {a + b}")
#
# # d. Catul numerelor daca al doilea este diferit de 0, altfel se afiseaza un mesaj in care se specifica “Catul nu se poate realiza"
# if b :
#     print(f"d. Catul a/b este {a/b}")
# else:
#     print("Catul nu se poate realiza")
#
# # e. primul numar ridicat la puterea al doilea numar
# print(f"e. rezultatul este {a ** b}")
#
# # f. care este numar mai mare
# print("f. a este mai mare")if a > b else print("f b este mai mare")
#
# # g. ambele numere sunt pozitive
# if a >= 0 and b >= 0:
#     print(f"g. numerele pozitive")
#
# # h. ambele numere sunt negative
# if a <= 0 and b <= 0:
#     print(f"h. numerele sunt negative")
#

















'''
1. Sa se scrie un program care citeste 2 nr de la tastatura si afiseaza urmatoarele informatii:
    a. Daca primul numar este par
    b. Daca al doilea numar este impar
    c. Suma numerelor
    d. Catul numerelor daca al doilea este diferit de 0, altfel se afiseaza un mesaj in care se specifica “Catul nu se poate realizat`”
    e. Primul numar ridicat la puterea al doilea numar
    f. Care este numar mai mare
    g. Daca ambele numere sunt pozitive
    h. Daca ambele numere sunt negative
'''

a = int(input("primul numar: "))
b = int(input("al doilea numar: "))
# a.
if a % 2 == 0:
    print("'a' este par")
else:
    print("'a' este impar")

# b.
if b % 2:
    print("'b' este impar")
else:
    print("'b' este par")

# c.
print(a + b)

# d.
if b != 0:
    print(a / b)
else:
    ("catul nu poate fi realizat")

# e.
print(f"primul numar ridicat la puterea al doikea este {a**b} ")

# f.
if a > b:
    print(f"{a} este mai mare decat {b}")
else:
    print(f"{b} este mai mare decat {a}")

# g.
if a >= 0 and b >= 0:
    print("ambele numere sunt pozitive")
else:
    print("-")

# h.
if a <= 0 and b <= 0:
    print("ambele numere sunt negative")
else:
    print("-")
