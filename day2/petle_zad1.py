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
