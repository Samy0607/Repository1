'''
Sa se scrie o functie care citeste din fisierul persons.csv si adauga la datele din acel fisier
o lista de date primite ca parametru, rezultatul final va fi scris in fisierul all_persons.cvs.
Constrangeri:
    * Va trebui sa se foloseasca clase pentru manipularea datelor;
    * Logica de scriere si citire trebuie separata;
    * Nu putem avea date hard codate in functii.
'''
import csv
from dataclasses import dataclass
from pprint import pprint


@dataclass
class Person:
    name: str
    age: int
    height: int

    @classmethod
    def from_dict(cls, row):
        return cls(row["name"], int(row["age"]), int(row["height"]))

    @staticmethod
    def get_fieldnames():
        # return ["name", "age", "height"]
        return Person.__dataclass_fields__.keys()

    def to_dict(self):
        return {"name": self.name, "age": self.age, "height": self.height}


def read(filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        result = []
        for row in reader:
            result.append(Person.from_dict(row))
    return result


pprint(read("persons.csv"))


def write(filename, data):
    print(data)
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=Person.get_fieldnames())
        writer.writeheader()
        for person in data:
            writer.writerow(person.to_dict())


PERSONS = [
    Person("Sergiu", 25, 185),
    Person("Valentina", 24, 175)
]


def append_data(in_filename, out_filename, data):
    persons = read(in_filename)
    persons.extend(data)
    write(out_filename, persons)


append_data("persons.csv", "all_persons.csv", PERSONS)
