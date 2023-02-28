'''
listele sunt utilizate pentru a stoca mai multe valori intr-o singura variabila
listele sunt modificabile, ordonare si permit valori duplicabile
listele sunt indexabile, si indexul incepe de la 0
cand se adauga un elemnt in lista acesta se va adauga la final
'''

# create

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
cars = list(("bmw", "audi", "tesla"))
print(type(numbers))
print(len(fruits))

#  indexing
print(20 * "-", "indexing", 20 * "-")

print(numbers[0])
print(numbers[-1])
print(numbers[2:4])
print(numbers[::2])  # 2 este pasul, cate elemente sare la o parcurgere
print(numbers[1:-1:2])
print(numbers[::-1])  # inversarea listei

# adaugarea unui element
print(20 * "-", "add element", 20 * "-")

numbers.append(10)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.insert(0, 9)
print(numbers)
numbers.append(7)
print(numbers)

# REMOVE...eliminarea element
print(20 * "-", "remove", 20 * "-")

elem = numbers.pop()  # elimina ultimul element de la final
print(elem)
print(numbers)

elem2 = numbers.pop(0)  # elimina de la indexul specificat
print(elem2)
print(numbers)

numbers.remove(3)  # elimina prima aparitie a valorii date adica 3
print(numbers)

numbers.clear()  # elimina toate elementele din lista
print(numbers)
numbers = [3, 4, 5, 6, 7, 1, 9, 3]

# replace element

print(20 * "-", "replace element", 20 * "-")
print(fruits)
fruits[1] = "pear"
print(fruits)

# count
print(20 * "-", "count", 20 * "-")
print(numbers.count(3))

# add 2 lists

print(20 * "-", "add 2 lists", 20 * "-")
numbers2 = [1, 3, 5, 7, 9]
print(numbers + numbers2)  # modifica lista initiala
numbers.extend(numbers2)  # creaza o lista noua
print(numbers)

# reverse
print(20 * "-", "reverse", 20 * "-")
print(fruits)
print(fruits[::-1])  # nu modifica lista initiala
print(fruits)
fruits.reverse()  # modifica lista initiala (in place)
print(fruits)

# sort
print(20 * "-", "sort", 20 * "-")
numbers.sort()  # modifica lista initiala (in place)
print(numbers)
numbers.sort(reverse=True)
print(numbers)
