# pętla - możliwość wykonania kodu wielokrotnie
# for - pętla iteracyjna
import random

for i in range(5):  # 0 do 4
    print(i)

for i in range(20):
    pass  # nic nie rób

print(i)  # 19

for _ in range(15):  # niema zmienna
    print("Test podłoga - niema zmienna")
    print(_)  # można odczytać wartość
# Test podłoga - niema zmienna
# 13
# Test podłoga - niema zmienna
# 14

for i in range(5):
    print(i + 2)
    print(i * 2)

# przerobic lotto na pętle
# zapisac wyniki do nowej listy

lista_wynik = []
lista_kul = list(range(1, 50))  # od 1 do 49
for _ in range(6):  # od 0 do 5
    kula = random.choice(lista_kul)
    lista_kul.remove(kula)
    # print(kula)  # 6
    lista_wynik.append(kula)

print(lista_wynik)  # [13, 23, 3, 42, 15, 7]

for i in range(10):
    if i % 2 == 0:  # reszta z dzielenia, modulo
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = []
for i in range(10):
    if i % 2 == 0:
        lista3.append(i)

print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:  # podstawia kolejne elementy z listy
    print(c)

lista_nazwy = ["Ala", 'Tomek', "Zenek", "Basia"]
for p in lista_nazwy:
    print(p)
# Ala
# Tomek
# Zenek
# Basia


for c in lista3:
    if c > 4:
        print(c, "Większe od 4")
    elif c == 4:
        print(c, "Równe 4")
    else:
        print(c, "mniejsze od 4")

    print(c)  # za każdym przejsciem pętli
print("Po zakończeniu pętli")
# 0 mniejsze od 4
# 0
# 2 mniejsze od 4
# 2
# 4 Równe 4
# 4
# 6 Większe od 4
# 6
# 8 Większe od 4
# 8
# Po zakończeniu pętli

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -2):  # (start, stop, krok), krok ujemny, liczy w dół
    print(i)

imiona = ["Radek", "Tomek", "Agata", "Marek"]

# wypisac elementy z listy jedno pod drugim

for i in range(len(imiona)):
    print(imiona[i])

for o in imiona:
    print(o)

# 0 Radek
for i in range(len(imiona)):
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

for o in imiona:
    print(imiona.index(o), o)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

# enumerate() - zwraca numer i element kolekcji
for p in enumerate(imiona):
    print(p)

# rozpokawanie krotki
a, b = (3, 'Marek')
print(a, b)

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Agata
# 4 Marek

# imiona = ["Radek", "Tomek", "Agata", "Marek"]
imiona = ["Radek", "Tomek", "Agata", "Marek", "Magda"]
wiek = [44, 56, 23, 38]

# Radek 44
# for p in imiona:
#     print(p, wiek[imiona.index((p))])
#     # IndexError: list index out of range - dla różnych długości list
# # Radek 44
# # Tomek 56
# # Agata 23
# # Marek 38

# zip() - łączy kolekcje
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 56)
# ('Agata', 23)
# ('Marek', 38)

for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 56
# Agata 23
# Marek 38

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 56))
# (2, ('Agata', 23))
# (3, ('Marek', 38))
a, b = (3, ('Marek', 38))
print(a, b)  # 3 ('Marek', 38)
c, d = ('Marek', 38)
print(c, d)
a, (c, d) = (3, ('Marek', 38))
print(a, c, d)

# musimy nawiasami wskazac, gdzie jest ta wewnętrzna krotka
for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Tomek 56
# 2 Agata 23
# 3 Marek 38
