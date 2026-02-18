# csv - dane oddzielone znakiem podziału ,;tab|

# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

import csv

row = ['radek', "coe", "3", 0]

filename = "records.csv"

with open(filename, "w") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(row)
