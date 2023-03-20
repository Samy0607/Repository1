# # 1. lungime
#
# name = "Dragos"
# print(len(name))
#
# # 2. Majuscule
#
# name = "dragos"
# print(name.upper()) # transforma toate literele mici in majuscule
#
# # 3. Litere mici
#
# name = "DraGoS"
# print(name.lower()) # transforma toate litere in litere mici
#
# # 4. Numerare
#
# name = "anamaria"
# print(name.count("a")) # nr de aparitii al caracterului in string
# print(name.count("i"))
# print(name.count("b"))
#
# # 5. Replace
#
# name = "anamaria"
# name = name.replace("a", "b") # toate aparitiile caratcterului a au fost inlocuite cu b
# print(name)
# food = "pizza"
# print(food.replace("zz", "t"))
# name = "anamaria"
# print(name.replace("a", "b", 2))
#
# # 6. Indexing
#
# name= "john"
# print(name.index("o"))
# print(name[0])
# print(name[len(name)-1])
#
# # 7. Slicing
#
b = "Hello world"
print(b[2:5]) # de la 2-5 (fara 5)

print(b[:5]) # de la inceput pana la 5 (fara 5)
print(b[2:]) # de la caracterul al 2-lea pana la final
print(b[-5: -2]) # indexare negativa

# # len() - numarare caractere
# marca = "mercedez vito"
# print(len(marca))
# micro = "asdfghjklqwertyuiopzxcvbnmerctvybnumi"
# print(len(micro))

# upper() - majuscule
# marca = "qwertyuuioopsdhasfjhflkaj"
# print(str.upper(marca))
# print(marca.upper())
# ion = "tralala"
# print(ion.upper())
# print(str.upper(ion))

# # lower() -litere mici
# asa = "ASDFGHJKLQWERTYUIOP"
# print(str.lower(asa))
# print(asa.lower())

# count() - numararea unui singur caracter
# abc = "mama ce de omenire"
# print(abc.count("i"))
# print(abc.count("e"))
# print(abc.count("a"))

# replace() - inlocuirea cuvintelor

# ion = "Tacut"
# ion = ion.replace("T", "sl")
# print(ion)
# farfurie = "murdara rau de tot"
# farfurie = farfurie.replace("mur", "bac")
# print(farfurie)

# # indexare - verifica o anunmita litera acata e si pot controla eu care e litera intreband printr-un numar
#
# Gigel = "Nesimtitfhjhiljhuytfvhmj,hjilhyfghbjniu"
# print(Gigel[-1])
# print(Gigel[17])
# print(Gigel[7])
# print(Gigel.index("y"))
# print(Gigel.index("h"))

#. slicing - citeste un grupaj de litere fara ultima pe care o cer eu

ciao = "bun venit in lumea it"
print(ciao[0:20])
print(ciao[7:14])
print(ciao[3:21])
print(ciao.index("i"))
print(ciao[7])
