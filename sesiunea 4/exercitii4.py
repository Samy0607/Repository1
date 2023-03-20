# 1.
# a.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)):
    print(f"Masina mea preferata este {masini[x]}")

# b.
for x in (masini):
    print(x)

# c.
index = 0
while index < len(masini):
    print(f"Masina: {masini[index]}")
    index += 1

# 2.
for x in range(len(masini)):
    if masini[x] in ["Audi", "Opel"]:
        continue
    masini[x] = masini[x].upper()
else:
    print(masini)

# 3.
# var 1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for x in masini:
    if x == "Mercedes":
        print(f"Am gasit masina dorita de d-voastra: {x}")
        break
    else:
        print(f"Am gasit masina {x}, mai cautam")
# var 2
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
import random

while True:
    masina = random.choice(masini)
    if masina == "Mercedes":
        masina = + 1
        print(f"Am gasit masina dorita de d-voastra: {'Mecedes'}")
        break
    else:
        print(f"Am gasit masina {masina}, mai cautam")

# 4.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina in ["Lăstun", "Trabant"]:
        continue
    else:
        print(f"S-ar putea sa va placa masina {masina}")

# 5.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for x, masina in enumerate(masini):
    if masina == "Trabant" or masina == "Lăstun":
        masini_vechi.append(masina)
        masini[x] = "Tesla"
print(f"Modele vechi: {masini_vechi}")
print(f"Modele noi: {masini}")

# 6.
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

for key, value in pret_masini.items():
    if value <= 15000:
        print(key)

for key, value in pret_masini.items():
    print(key, value)

for key, value in pret_masini.items():
    if value <= 15000:
        print(f"Pentru un buget de sub 15000 euro puteți alege mașina {key}")


7.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
y = 0
for x in numere:
    if x == 3:
        y += 1
print(y)


8.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
x = 0
for y in numere:
    x += y
print(x)


9.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
big = numere[0]
for number in numere:
    if number > big:
        big = number
print(big)


10.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for x, number in enumerate(numere):
    if number > 0:
        numere[x] = number * -1
print(numere)




# 1.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for x in masini:
#     print(f"masina mea preferata este {x}")
#
# for x in masini:
#     print(x)
#
# x = 0
# while x < len(masini):
#     x += 1
#     print(f"cea mai tare masins {masini[x]}")

# 2.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for x in range(len(masini)):
#     if masini[x] in ["Audi", "Opel"]:
#         continue
#     masini[x] = masini[x].upper()
# else:
#     print(masini)

# 3.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for x in masini:
#     if x == "Mercedes":
#         print(f"Am gasit masina cautata de d-voastra: {x}")
#         break
#     else:
#         print(f"Am gasit masina {x}, mai cautam")

# 4.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for x in masini:
#     if x in ["Trabant", "Lăstun"]:
#         continue
#     else:
#         print(f"S-ar putea sa va placa masina: {x}")

# 5.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for x, masina in enumerate(masini):
#     if masina == "Lăstun" or masina == "Trabant":
#         masini_vechi.append(masina)
#         masini[x] = "Tesla"
# print(f"Modele vechi: {masini_vechi}")
# print(f"Modele noi: {masini}")

# 6.
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# for key, value in pret_masini.items():
#     if value <= 15000:
#         print(key)
#
# for key, value in pret_masini.items():
#     print(key, value)
#
# for key, value in pret_masini.items():
#     if value <= 15000:
#         print(f"Pentru un buget de sub 15000 alege masina: {key}")

# 7.
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x = 0
# for y in numere:
#     if y == 3:
#         x += 1
# print(x)

# 8.
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# y = 0
# for x in numere:
#     y += x
#     print(y)

# 9.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
mare = numere[0]
for numar in numere:
    if numar > mare:
        mare = numar
print(mare)

# 10.
index = 0
for x, index in enumerate(numere):
    if index > 0:
        numere[x] = index * -1
print(numere)

# 1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_negative = []
numere_pozitive = []

for x in alte_numere:
    if x % 2 == 0 and x > 0:
        numere_pare.append(x)

for x in alte_numere:
    if x % 2 == 1 and x > 0:
        numere_impare.append(x)

for x in alte_numere:
    if x >= 0:
        numere_pozitive.append(x)

for x in alte_numere:
    if x <= 0:
        numere_negative.append(x)

print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)