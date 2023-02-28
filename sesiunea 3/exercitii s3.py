# 1.
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
a = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
if note_muzicale == a:
    print(note_muzicale)
else:
    print(None)

if note_muzicale != a:
    print(note_muzicale)
else:
    print(note_muzicale[::-1])

if note_muzicale.reverse():
    print(note_muzicale)
else:
    print(note_muzicale)

if note_muzicale.reverse():
    print(note_muzicale)
else:
    print(note_muzicale)

# 2.
if (note_muzicale) == a:
    print(note_muzicale.count("do"))
else:
    print(note_muzicale)

# 3.
# a.
first = [3, 1, 0, 2]
second = [6, 5, 4]
if (first) == second:
    print(first)
else:
    print(first + second)
# b.
if first.extend(second):
    print(second)
else:
    print(first)

# 4.
# a.
if first.sort():
    print(second)
else:
    print(first)
# b.
if first.remove(0):
    print(second)
else:
    print(first)

# 5.
if first == second:
    print("lista este nu este goala")
else:
    print("lista este goala")

if first != second:
    print("lista nu este goala")
else:
    print("lista este goala")

# 6.
if first.clear():
    print(second)
else:
    print(first)

# 7.
if first == second:
    print("lista este nu este goala")
else:
    print("lista e goala")

# 8.
dict1 = {
    "Ana": 8,
    "Gigel": 10,
    "Dorel": 5,
}
if dict1 == True:
    print(None)
else:
    print(dict1.keys())

# 9.
if dict1 == False:
    print(None)
else:
    print(f"Ana a luat nota {dict1['Ana']}")

if dict1 == True:
    print(None)
else:
    print(f"Gigel a luat nota {dict1['Gigel']}")

if dict1 == False:
    print(None)
else:
    print(f"Dorel a luat nota {dict1['Dorel']}")

# 10.
if dict1.update({"Dorel": 6}):
    print(None)
else:
    print(dict1)

# 11.
if dict1.pop('Gigel'):
    print(dict1)
else:
    print(dict1)
if dict1.update({"Ionica": 9}):
    print(None)
else:
    print(dict1)
