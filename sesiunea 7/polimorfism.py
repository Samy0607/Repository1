"""
Polimorfismul se refera la abilitatea unui obiect de a se comporta in mai multe moduri in functie
de context.
In esenta polimorfismul permite obiectelor de acelasi tip sa aiba comportamente diferite
fara a fi necesar sa se stie tipul lor exact inainte de de executie.
"""

from abc import ABC, abstractmethod
from pprint import pprint


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Creature(ABC):
    @abstractmethod
    def eat(self):
        pass


class Animal(Creature):
    def __init__(self, age, weight, species):
        self.age = age
        self.weight = weight
        self.species = species

    def eat(self):
        return f"I am am eating {self.__class__.__name__}"


class DomesticAnimal(Animal):
    def __init__(self, age, weight, species, owner):
        super().__init__(age, weight, species)
        self.owner = owner


class Pet(DomesticAnimal):
    def __init__(self, age, weight, species, owner, name):
        super().__init__(age, weight, species, owner)
        self.name = name
class WildAnimal(Animal):
    def __init__(self, age, weight, species, location):
        super().__init__(age, weight, species)
        self.location = location


def animals_eat(animals):
    for x in animals:
        print(x.eat())


p1 = Person("Sergiu", 24)
p2 = Person("Valentina", 23)
animals = [
    DomesticAnimal(age=5, weight=130, owner=p1, species="Cow"),
    Pet(name="Puffi", age=3, weight=4, owner=p2, species="Dog"),
    Pet(name="Pisu", age=1, weight=3, owner=p2, species="Cat"),
    Pet(name="Rexi", age=2, weight=3, owner=p1, species="Dog"),
    WildAnimal(age=25, weight=230, species="Bear", location="forest"),
    WildAnimal(age=18, weight=67, species="Wolf", location="forest"),
    WildAnimal(age=10, weight=59, species="Wolf", location="forest"),
    WildAnimal(age=40, weight=310, species="Elephant", location="jungle"),
    WildAnimal(age=33, weight=99, species="Giraffe", location="jungle"),
    DomesticAnimal(age=1, weight=2, owner=p1, species="Chicken"),
    DomesticAnimal(age=1, weight=145, owner=p2, species="Pig"),
    WildAnimal(age=2, weight=2, species="Squirrel", location="forest")
]

animals_eat(animals)


# Sa se scrie o functie care primeste ca parametru o lista de animale si returneaza doar
# animalele domestice din acea lista

def get_all_domestic_animals(animals):
    li = []
    for x in animals:
        if isinstance(x, DomesticAnimal):
        #     if type(x) == DomesticAnimal: # -> daca vrem doar obiecte strict de tipul DomesticAnimal
            li.append(x)
    return li


pprint(get_all_domestic_animals(animals))