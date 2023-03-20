# 1. Sa se scrie un program care citeste un text de la tastatura si afiseaza o lista
# cu fiecare caracter in ordinea inversa a aparitiei in text

text = input("introdu un text: ")
text = text[::-1]
l = list(text)
print(l)

# 2. Fie seturile s1 si s2
set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}
# a. sa se afiseze toate elementele care apar in set1 si nu apar in set2
# b. --||-- care apar in ambele seturi
# c. --||-- care nu sunt comune

# a
print(set1.difference(set2))
print(set1-set2)

# b.
print(set1.intersection(set2))
print(set1&set2)

# c.
print(set1.symmetric_difference(set2))
print(set1^set2)
