# seturile sunt folosite pentru a stoca mai multe elemente intr-o
# singura variabila dar fara duplicate

# Create
fruits = {"apple", "banana", "cherry"}  # set
cars = set()

# length

print(20 * "-", "length", 20 * "-")

print(len(fruits))

# add elemnts

print(20 * "-", "add elemnts", 20 * "-")

fruits.add("pear")
print(fruits)
tropical = {"mango", "papaya"}
fruits.update(tropical)
print(fruits)
fruits.update(["kiwi", "orange"])
print(fruits)

fruits.add("apple")  # nu poate avea duplicate
print(fruits)

# remove elements
print(20 * "-", "remove elements", 20 * "-")
fruits.remove("banana")
print(fruits)
# fruits.remove("grapes") # arunca eroare pentru ca elementul nu exista
fruits.discard("grapes")
print(fruits)
fruits.pop()  # elimina ultimul element inserat
print(fruits)

a = {1, 2, 3}
a.clear()
print(a)

# join
print(20 * "-", "join", 20 * "-")
s1 = {"a", "b", "c"}
s2 = {1, 2, 3}
s3 = s1.union(s2)
print(s3)
print(s1 | s2)  # forma prescurtata union

# intersection
print(20 * "-", "intersection", 20 * "-")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
print(x & y)  # forma prescurata de intersection

# difference
print(20 * "-", "difference", 20 * "-")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
print(x - y)  # prescurtare la difference

# symetric difference
print(20 * "-", "symetric difference", 20 * "-")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
print(x ^ y)

# issubset si issuperset
print(20 * "-", "issubset si issuperset", 20 * "-")

x = {"a", "b", "c"}
y = {"a", "b", "c", "d", "e", "f"}
print(x.issubset(y))
print(y.issuperset(x))
