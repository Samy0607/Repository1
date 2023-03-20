# Exceptions
########################################################################

try:  # testeaza un bloc de cod pentru erori
    print(x)
except:  # trateaza diferite tipuri de erori
    print("A aparut o eroare!")

########################################################################

try:
    print("1".Upper())
    print(1 / 0)
    print(x)
except (NameError, ZeroDivisionError):
    print("Variabila nedefinita sau diviziune cu zero!")
except AttributeError as ex:
    print(f"Eroarea : {ex}")

########################################################################

try:
    print("Hello!")
except:
    print("A aparut o eroare")
else:  # else se executa doar daca nu apare nicio eroare
    print("Nicio eroare!")

########################################################################

try:
    print(x)
except:
    print("A aparut eroarea")
finally:  # finally se executa oricum
    print("Se executa!")

########################################################################

x = -1
if x < 0:
    raise Exception("x<0")  # mesajul pe care vrem sa il afisam

########################################################################

"""
try: (Blocul try)
    bloc de cod unde ar putea aparea o eroare
    (Sfarsitul blocului try)
except NumeEroare: <-- Prinderea tuturor exceptiilor de tipul NumeEroare
    se executa doar daca se prinde NumeEroare
except (AltNumeEroare, IncaUnNumeEroare): <-- Gruparea mai multe tipuri de Exceptii
    se executa daca se prinde AltNumeEroare sau IncaUnNumeEroare
except Eroarea4 as ex: <-- Stocarea mesajului unei erori intr-o variabila (exemplul variabilei 'ex')
    se poate accesa mesajul de Eroarea4 prin variabila ex
except:
    se executa la orice alt tip de eroare nespecificat
else:
    se executa doar daca nu se arunca eroare in blocul try
finally:
    se executa indiferent daca se arunca eroare sau nu
"""