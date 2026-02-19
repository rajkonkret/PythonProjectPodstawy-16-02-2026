# funkcja lambda
# skrócony zapis funkcji
# lambda zwraca wynik (return)
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(10, 8))  # 2

odejmij2 = lambda a, b: a - b  # domyślnie ma return
print(odejmij2(10, 2))  # 8

# przemieni oblicz_vat na lambde
# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
# 1230.0
# 1070.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(29))  # dorosły

# mapowanie danych
lista = [1, 2, 14, 24, 50, 67, 80, 100, 200, 500]

# stworzyc liste, do listy zapisać eleemnty tej listy, wykonując na nich operację: *2
l1 = []
for i in lista:
    l1.append(i * 2)
print(l1)  # [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

print([i * 2 for i in lista])  # [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

# map() - wykonuje funkcję na kolejnych elementach kolekcji
# funkcje wyższego rzędu - jako argument przyjmuje inną funkcję
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

# lambda jako funkcja anonimowa
# zadeklarowana w miejscu użycia
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 5, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 6, lista))}")
# Zastosowanie map(): [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]
# Zastosowanie map(): [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]
# Zastosowanie map(): [4, 8, 56, 96, 200, 268, 320, 400, 800, 2000]
# Zastosowanie map(): [5, 10, 70, 120, 250, 335, 400, 500, 1000, 2500]
# Zastosowanie map(): [6, 12, 84, 144, 300, 402, 480, 600, 1200, 3000]

# filtrowanie danych
l4 = []
for i in lista:
    if i < 3:
        l4.append(i)

print(l4)  # [1, 2]

# filter() - zwraca eleemnty spełniające warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")  # Zastosowanie filter(): [1, 2]
# x > 3 i x < 100
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 50, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 25, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 150, lista))}")
# Zastosowanie filter(): [1, 2, 14, 24]
# Zastosowanie filter(): [50, 67, 80, 100, 200, 500]
# Zastosowanie filter(): [1, 2, 14, 24, 50, 67, 80, 100]

print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 100, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 100, lista))}")
# Zastosowanie filter(): [14, 24, 50, 67, 80]
# Zastosowanie filter(): [14, 24, 50, 67, 80]

# zamiana filter na map
print(f"Zastosowanie filter(): {list(map(lambda x: 3 < x < 100, lista))}")
# Zastosowanie filter(): [False, False, True, True, True, True, True, False, False, False]
