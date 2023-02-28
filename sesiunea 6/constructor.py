class Dog:
    species = "mammal"  # class atribute -> acelasi pt toate obiectele din aceasta clasa.
    age = 12
    name = "Rexy"


d = Dog()
print(d.name)
d2 = Dog()
d2.name = "Pufy"  # name->devine atribut de instanta.
print(d.name, d2.name)
Dog.name = "Bruno"
print(d.name, d2.name)


# Atributele de clasa sunt in general folosite pentru a crea constante in acea clasa.

class Dog2:
    species = "Mammal"  # class atribute

    def __init__(self, age, name):  # instance atribute.
        self.age = age
        self.name = name


my_dog = Dog2(2, "Pufy")
print(my_dog.age)
print(my_dog.name)
# print(Dog2.name) -> incorect pentru ca name este un atribut de instanta si poate fi accesat doar print-un obiect al acestei clase.
