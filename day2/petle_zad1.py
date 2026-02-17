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

