import csv

filename = "records.csv"
filename = "records_discount.csv"

fields = []
rows = []

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)
    print(dialect.quotechar)

    csv_f.seek(0)  # powrót odczytu na początek pliku

    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x000002E1861ABAC0>

    # StopIteration - wyczerpały się dane, próba odczytu poza zakresem
    fileds = next(csvreader)  # odczyt pierwszego wiersza z danych, ustawienie odczytu na następny

    for row in csvreader:  # zaczyna od drugiego wiersza
        rows.append(row)

print("Fields:", fileds)
print("Rows:", rows)
# 3 Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]

# Fields: ['sku;exp_date;price']
# Rows: [['1;today;200'], ['2;today;100'], ['3;tomorrow;900'], ['4;today;1200'], ['5;today;7200'], ['6;today;199.99']]
# Fields: ['sku', 'exp_date', 'price']
# Rows: [['1', 'today', '200'], ['2', 'today', '100'], ['3', 'tomorrow', '900'], ['4', 'today', '1200'], ['5', 'today', '7200'], ['6', 'today', '199.99']]
