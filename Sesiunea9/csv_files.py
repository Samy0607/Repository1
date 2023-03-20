import csv
from pprint import pprint


def read(filename):
    with open(filename, "r") as f:
        result = []
        reader = csv.reader(f)
        for row in reader:
            result.append(row)
    return result[1:]


pprint(read("empoyees.csv"))


def write(data, filename):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)


data = [
    ["Nume", "Varsta"],
    ["Sergiu", "25"],
    ["Andrei", "30"],
    ["Cristi", "34"]
]

write(data, "empoyees2.csv")


def read_dict(filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


pprint(read_dict("empoyees.csv"))

data2 = [
    {"Nume": "Sergiu", "Varsta": "24"},
    {"Nume": "Andrei", "Varsta": "31"},
    {"Nume": "Dan", "Varsta": "45"}

]


def write_dict(filename, data):
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, data[0].keys())
        writer.writeheader()
        write.writerows(data)

    write_dict("empoyees2.csv", data2)
