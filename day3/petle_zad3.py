# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print('Komunikat')

licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(50 * "-")
print(licznik)

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")

# password = input("Podaj hasło:")
# while password != 'secret':  # != - różne
#     password = input("Podaj ponownie:")
# Podaj hasło:refddsd
# Podaj ponownie:asdasdaf
# Podaj ponownie:ASSDSDA
# Podaj ponownie:ASDADDD
# Podaj ponownie:SECRET
# Podaj ponownie:secret

lista = []
lista_int = []
while True:
    #  A string is numeric if all characters in the string are numeric
    wej = input("Podaj liczbę:")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)  # ['1', '2', '3', '4', '5', '6', '7']
print(lista_int)  # [1, 2, 3, 4, 5, 6, 7]
