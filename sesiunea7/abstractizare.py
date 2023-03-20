"""
O clasa abstracta este o clasa care are cel putin o metoda abstracta
O metoda abstracta este o metoda fara corp (implementare)
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        raise NotImplementedError


class Dog(Animal):
    def sound(self):
        print("Woof")

    def sleep(self):
        print("zzz")


class Cat(Animal):
    def sound(self):
        print("miow")

    def sleep(self):
        print("prrr")