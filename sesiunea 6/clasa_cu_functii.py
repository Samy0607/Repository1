class Dog:
    species = "Mammal"  # class atribute

    def __init__(self, age, name):  # instance atribute.
        self.age = age
        self.name = name

    def bark(self):
        print("woof")

    def get_owner(self):
        return f"I am {self.name} owned by Andrei"


d = Dog(12, "Rexy")
d.bark()
print(d.get_owner())
d2 = Dog(4, "Pufy")
print(d2.get_owner())