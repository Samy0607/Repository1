# 1. sa se scrie un program care citeste date de la tastatura si doarafizeaza primele 3 caracterediferite cu spatiu primite

a = input("Text: ")
a = a.replace(" ", "")
print(a[ :3])

# 2.  sa se scrie un program care citeste date de la tastatura si afiseaza urmatoare:
# a nr de litere a textului introdus
# b prima si ultima litera
# c textul scris doar cu majuscule
# d de cate ori apare prima litera
# e cate cuvinte are textul

b = input("Text: ")
print(f"a. {len(b)}")
print(f"b. {b[0]} {b[-1]}")
print(f"c. {b.upper()}")
print(f"d. {b.count(b[0])}")
print(f"e. {b.count(' ') + 1}")

