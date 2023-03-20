name = "alabala portocala"
primul = name[0] # stocarea primei litere

ultim = name[-1]
name = name[1:-1]
# print(name)
primul_cap = primul.upper()
name = name.replace(primul, primul_cap)
print(name)
name= f"{primul}{name}{ultim}"
print(name)


user = input("name: ")
parola = input("password: ")
size_parola = len(parola)
hide = "*" * size_parola
print(hide)
print(f"parola pt userul {user} este {hide} si are {size_parola} caractere")