# create
fruits = ("apple", "banana", "cherry", "cherry")
print(fruits)

# count
print(20 * "-", "count", 20 * "-")
print(fruits.count("cherry"))

# indexing
print(20 * "-", "indexing", 20 * "-")
print(fruits[0])
print(fruits[1:3])
print(fruits[-1])

# adding elements
print(20 * "-", "adding elements", 20 * "-")
fruits += ("pear",)
print(fruits)
# sau
y = list(fruits)  # transformare intermediara in lista pentru adauga element
y.append("orange")
fruits = tuple(y)
print(fruits)

# remove element
print(20 * "-", "remove element", 20 * "-")
y = list(fruits)
y.remove("apple")
fruits = tuple(y)
print(fruits)
