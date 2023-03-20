class Dog:
    species = "Mammal"  # class atribute

    def __init__(self, age, name):  # instance atribute.
        self.age = age
        self.name = name

    def __str__(self):
        return f"age={self.age}, name={self.name}"

    def __repr__(self):
        return str(self)  # sau self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Dog):
            return False
        return self.age == other.age and self.name == other.name


d = Dog(2, "Pufy")
print(d)

d2 = Dog(3, "Bruno")
l = [d, d2]
print(l)

d3 = Dog(3, "Bruno")
print(d2 == d3)
print(d2 == 5)