# dictionarele sunt folosite pentru a stoca date in perechi de forma cheie:valoare

# create
car = {
    "brand": "ford",
    "model": "mustang",
    "year": 1990,
}

car2 = dict(brand="ford", model="mustang", year=1990)

# accesing elemnts
print(20 * "-", "accesing elemnt", 20 * "-")

print(car["brand"])
# print(car["is_new"]) # arunca o eroare pentru ca nu exista acea cheie in dictionar
print(car.get("is_new"))
print(car.get("is_new", True))

# add elements
print(20 * "-", "add alements", 20 * "-")
car["is_new"] = False
print(car)

v = car.setdefault("is_new", True)
print(car)
print(v)
car.setdefault("price", 7900)
print(car)

# replace element
print(20 * "-", "replace elemnt", 20 * "-")

car["price"] = 9700
print(car)
car.update({"price": 10000, "color": "black"})
print(car)

#  remove element
print(20 * "-", "remove element", 20 * "-")

car.pop("is_new")
print(car)

car.popitem()  # ultimul elemnt inserat
print(car)

del car["year"]
print(car)

a = {1: "first", 2: "second"}
a.clear()
print(a)

# all keys
print(20 * "-", "all keys", 20 * "-")

print(car.keys())
print(list(car.keys()))

# all values

print(20 * "-", "all values", 20 * "-")
print(list(car.values()))

# all items

print(20 * "-", "all item", 20 * "-")
print(list(car.items()))

# lenght

print(20 * "-", "lenght", 20 * "-")

print(len(car))  # 3 este numarul de chei