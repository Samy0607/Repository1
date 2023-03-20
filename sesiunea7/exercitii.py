# Abstraction
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3,14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descriere(self):
        print("Cel mai probabil am colturi")


# Inheritance

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura


# Encapsulation

    @property
    def latura(self):
        print("Latura este propietate privata")
        return self.__latura

    @latura.getter
    def latura(self):
        print("Latura existenta")
        return self.__latura

    @latura.setter
    def latura(self, modificare):
        print("Modificare latura")
        self.__latura = modificare

    @latura.deleter
    def latura(self):
        print("Stergerea laturii")
        self.__latura = None



class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.raza = raza

    @property
    def raza(self):
        print("Raza este propietate privata")
        return self.__raza

    @raza.getter
    def raza(self):
        print("Raza existenta")
        return self.__raza

    @raza.setter
    def raza(self, dimensiune_noua):
        print("Noua dimensiiune a razei")
        self.__raza = dimensiune_noua

    @raza.deleter
    def raza(self):
        print("Stergerea razei")
        self.__raza = None


# Polimorfism

# def descrie:
#     print("Eu nu am colturi")
#
# class Patrat(FormaGeometrica):
    # def __init__(self):





# class Cerc(FormaGeometrica):
    # def __init__(self):
