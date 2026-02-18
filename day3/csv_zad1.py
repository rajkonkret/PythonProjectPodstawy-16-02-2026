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

product = [
    {"sku": 1, "exp_date": 'today', "price": 200},
    {"sku": 2, "exp_date": 'today', "price": 100},
    {"sku": 3, "exp_date": 'tomorrow', "price": 900},
    {"sku": 4, "exp_date": 'today', "price": 1200},
    {"sku": 5, "exp_date": 'today', "price": 7200},
    {"sku": 6, "exp_date": 'today', "price": 199.99},
]

filename = "records_discount.csv"

list_product = [key for key in product[0]]

with open(filename, "w", newline="") as f:
    # delimiter= - znak podziału
    csvwriter = csv.DictWriter(f, fieldnames=list_product, delimiter=";")
    csvwriter.writeheader()  # zapis nagłówka - nazwy kolumn
    csvwriter.writerows(product)  # writerows, podajemy listę słowników
