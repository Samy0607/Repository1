import csv
import json
from pprint import pprint

# 1.
def csv_and_json(fisier_csv, fisier_json):
    with open(fisier_csv, "r") as f:
        result = []
        reader = csv.reader(f)
        for row in reader:
            result.append(row)

    with open(fisier_json, "w") as f:
        json.dump(result, f)

csv_and_json("fisier_csv", "fisier_json")

# 2.
def injumatatire_fisier_json(filename):
    with open(filename, "r") as f:
        reader = json.load(f)

    jum = len(reader) // 2

    prima_jum = reader[:jum]
    a_doua_jum = reader[jum:]

    with open("prima_jumatate.json", "w") as f:
        json.dump(prima_jum, f)

    with open("a_doua_jumatate.json", "w") as f:
        json.dump(a_doua_jum, f)


injumatatire_fisier_json("fisier_json_1")