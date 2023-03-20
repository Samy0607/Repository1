# variabile -> contaire de memorie pt a stoca o valoare
# 1. Creare variabile

x = 5
y = "Ionut"

print(x)
print(y)

'''
2. denumire variabile
reguli:
   *numele variabilei trebuie sa inceapa cu litera sau _
   * numele nu poate incepe cu numar
   *numele variabilei poate contine doar caractere alfa-numerice si _ (0-9, a-z, A-Z _)
   *numele variabilelor sunt case senzitive (age, Age, AGE sunt 3 variabile diferite
'''
# asa
myvar = "dina"
my_var = "dina"
my_var = "dina"
myVar = "dina"
MYVAR = "dina"
myvar2 = "dina"

# nu asa
# 2myvar = "dina"
# my-var = "dina"
# my var = "dina"

# mai multe valori la mai multe variabile
x, y, z = 6, 7, 8
print(x)
print(y)
print(z)

'''
t = x
x = y
y = t
'''
x,y = y, x
print(x,y)

# 4. o valoare la mai multe variabile
a = b = c = 10
print(a, b, c)

a =  b = c = 3
print(a, b, c)