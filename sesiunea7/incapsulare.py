"""
3 tipuri de metode si atribute:

- public -> accesibile peste tot
- protected -> accesibile doar in ierarhia de mostenire (_atribut)
- private -> accesibile doar in clasa (__atribut)
"""


class Car:
    __model = "Dacia"

    def get_model(self):  # getter -> returneaza datele
        return self.__model

    def set_model(self, new_model):  # setter -> modifica sau actualizeaza datele
        self.__model = new_model


car1 = Car()
print(car1.get_model())
car1.set_model("BMW")
print(car1.get_model())
# Incapsulare folosind properties

class Car:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        print("Setting as property")
        return self.__color

    # @color.getter
    # def color(self):
    #     print("Getting value")
    #     return self.__color

    @color.setter
    def color(self, value):
        print("Setting new value")
        self.__color = value

    @color.deleter
    def color(self):
        print("Deleting value")
        self.__color = None

    @property
    def is_painted(self):
        return self.__color is not None and self.__color != "white"

car1 = Car("blue")
print(car1.color)
car1.color = "red"
print(car1.color)
print(car1.is_painted)
del car1.color
print(car1.color)
print(car1.is_painted)