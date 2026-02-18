# csv - dane oddzielone znakiem podziału ,;tab|

# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

import csv

row = ['radek', "coe", "3", 0]
fields = ['name', 'branch', 'year', 'cgpa']

filename = "records.csv"

# newline="" - obejście problemu pustych linii
with open(filename, "w", newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

dict_name = dict(zip(fields, row))
print(dict_name)
print(type(dict_name))
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': 0}
# <class 'dict'>

filename = "records_dict.csv"

with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()  # zapis nagłówka - nazwy kolumn
    csvwriter.writerow(dict_name)
