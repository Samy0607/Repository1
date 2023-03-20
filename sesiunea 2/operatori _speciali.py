# 1. Operatori de identitate
# x1 = 5
# y1 = 5
# x2 = "Hello"
# y2 = "Hello"
# x3 = [1, 2, 3]
# y3 = [1, 2, 3]
# z4 = [4]
# m4 = [4]
# print(z4 is m4)
# print(x1 is y1) #pentru tipurile de date primitive se va face egalitate la valoare
# print(x2 is not y2) # inversul
# print(x3 is y3) # se verefica locatia din memoria si de aceea nu este acelasi obiect
# print(x3 is x3)
# print("#" * 50)

# 2. Operatori de apartenenta
# x = "hello"
# y = [1, 2, 3]
# print("h" in x)
# print("llo" in x)
# print(4 not in y)
# print([2, 3]in y) # nu verifica subliste...verifica daca e elemntul 2, 3 in lista si de aceea da False
# print("#" * 50)
#
# 3. Functiile all si any
print(all([1, 2, "a", "v", -7]))  # verifica daca toate elementele din lista pot fi adevarate
print(any([0, None, "", [], 1]))  # verfifca daca cel putin un element poate fi evaluat la True
