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
