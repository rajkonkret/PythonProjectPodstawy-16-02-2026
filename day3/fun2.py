# funkcje zwracające wynik
# kończy się : return
a = 9
b = 89


def dodaj():
    return a + b


def dodaj2(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj())  # 98

# dodaj2, odejmij
print(dodaj2(6, 90))  # 96
print(dodaj2(b=6, a=90))  # 96

print(odejmij())  # 0
print(odejmij(1))  # 1
print(odejmij(1, 2))  # -1
print(odejmij(1, 2, 3))  # -4
print(odejmij(c=1, a=2, b=3))  # -2
print(odejmij(c=1, a=2))  # 1

wynik = odejmij(6, 8, 24)
print("Wynik:", wynik)  # Wynik: -26


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(1000, 8))  # 1080.0
print(oblicz_vat(vat=15, kwota=1000))  # 1150.0

zm = oblicz_vat(1000)
print(zm)  # 1230.0 -> float
print(type(zm))  # <class 'float'>

if zm == 1230:
    print("OK")  # OK

print(dodaj2(5, 7) + odejmij(5, 89))
# -72
