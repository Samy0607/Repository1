# 1.
def total(a, b):
    return a + b

numere = total(2, 4)
print(numere)

# 2.
def clear(a):
    if a % 2 == 0:
        print("TRUE")
    else:
        print("FALSE")
    return

numere = clear(6)
print(numere)

# 3.
def name():
    return name()

nume = "Samuel Potop"
print(len(nume))

# 4.
def aria_dreptunghiului(L, l):
    return L * l

a = aria_dreptunghiului(6, 5)
print(a)

# 5.
def aria_cercului(r, p):
    return (p ** 2) * r

r = 5
p = 3.14
print(aria_cercului(r, p))

# 6.
def found(string, caracter):
    if caracter in string:
        return True
    else:
        return False

print(found("Acesta este un string", "a"))

# 7.
def no_return(mesaj):
    mici = 0
    mari = 0
    for x in mesaj:
        if x == x.upper():
            mari += 1
        else:
            mici += 1
    print(f"Numărul de caractere lower case este {mici}")
    print(f"Numărul de caractere upper case este {mari}")

no_return("Viata bate FILMUL")

# 8.
def numere_pozitive(lista):
    numere = []
    for n in lista:
        if n >= 0:
            numere.append(n)
    return numere
print(numere_pozitive([1, 4, 6, -3, -1, 0]))

# 9.
def comparare(x, y):
    if x > y:
        print(f"Primul numar {x} este mai mare decat al doilea {y}")
    elif x < y:
        print(f"Al doilea numar {y} este mai mare decat primul {x}")
    else:
        print(f"Numrele sunt egale")
comparare(5, 4)

# 10.
def sir_numere(a, b):
    if a not in b:
        b.append(a)
        print("Nu am adaugat numărul în sir. Acesta există deja")
        return True
    else:
        print('Nu am adaugat nr in sir. Acesta exista deja')
        return False

print(sir_numere(1,[3, 4, 5, 6, 7]))