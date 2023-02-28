note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# 1.
print(note_muzicale)
print(note_muzicale[::-1])
note_muzicale.reverse()
print(note_muzicale)
print(note_muzicale[::-1])

# 2.
print(note_muzicale.count("do"))

# 3.
first = [3, 1, 0, 2]
second = [6, 5, 4]
print(first + second)
first.extend(second)
print(first)

# 4.
first.sort()
print(first)
first.remove(0)
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
first.clear()
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
print(dict1.keys())

# 9.
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat noata {dict1['Dorel']}")

# 10.
dict1.update({"Dorel": 6,})
print(dict1)

# 11.
dict1.pop("Gigel")
print(dict1)
dict1.update({"Ionica": 9})
print(dict1)