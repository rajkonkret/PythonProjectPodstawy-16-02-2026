# kolekcje

# lista - przechowuje dowolną ilość danych, różnego typu na raz
# zachowuje kolejność podczas dodawania elementów

# pusta lista
lista = []
print(type(lista))  # <class 'list'>
print(lista)  # []

pusta_lista = list()  # tworzenie pustej listy słówkiem list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# dodawanie do listy (na końcu listy)
lista.append("Radek")
lista.append("Tomek")
lista.append("Marek")
lista.append("Zenek")
lista.append("Anna")
lista.append("Magda")

print(lista)
# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Anna', 'Magda']

print(len(lista))  # długość 6 elementów

# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Anna', 'Magda']
#      0        1        2       3        4       5

print(lista[2])  # Marek
print(lista[4])  # Anna

# print(lista[10])  # IndexError: list index out of range

# ostatni element
print(lista[5])  # Magda
print(lista[len(lista) - 1])  # Magda
print(lista[-1])  # Magda
print(lista[-2])  # Anna
print(lista[-3])  # Zenek

# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Anna', 'Magda']
#      0        1        2       3        4       5
#      -6       -5       -4       -3      -2      -1

# slicowanie - fragment listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Marek'],indeksy: 012, z prawej zbiór otwarty
print(lista[:3])  # ['Radek', 'Tomek', 'Marek']

print(lista[2:])  # ['Marek', 'Zenek', 'Anna', 'Magda'], z ostatnim włącznie
print(lista[2:5])  # ['Marek', 'Zenek', 'Anna'], bez ostatniego

print(lista[2:9])  # ['Marek', 'Zenek', 'Anna', 'Magda']

print(lista[12:26])  # []

print(lista[:])  # ['Radek', 'Tomek', 'Marek', 'Zenek', 'Anna', 'Magda']

# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Anna', 'Magda']
#      0        1        2       3        4       5
#      -6       -5       -4       -3      -2      -1
print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Marek', 'Zenek'] -> [0:4]

# range() - generowanie liczb z zakresu (int)
lista_15 = list(range(15))
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[::2])  # [start:stop:krok], [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[::3])  # [0, 3, 6, 9, 12]

# wyświetla listę w odwrotnej kolejnosći
print(lista_15[::-1])  # [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14], (start, stop, krok)

# python nie ma typu array (tablica)
tablica = [[1, 2], [3, 4]]
print(tablica)  # [[1, 2], [3, 4]]
# numpy - biblioteka do pracy z tablicami/macierzami

# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Anna', 'Magda']
# nadpisanie elementu na wskazanym miejscu
lista[3] = "Asia"
print(lista)  # ['Radek', 'Tomek', 'Marek', 'Asia', 'Anna', 'Magda']

# wstawienie elementu na wskazanym indeksie, pomiędzy inne elementy
lista.insert(1, "Ola")
print(lista)  # ['Radek', 'Ola', 'Tomek', 'Marek', 'Asia', 'Anna', 'Magda']

# insert gdy tablica pusta
lista_darek = []
lista_darek.insert(1, "Darek")
print(lista_darek)  # ['Darek'] indeks 0

# usunięcie elementu z listy, po elemencie, pierwszy napotkany
lista.remove("Tomek")
print(lista)  # ['Radek', 'Ola', 'Marek', 'Asia', 'Anna', 'Magda']

# dodajmey element, który już jest na liście,
lista.append("Marek")
print(lista)  # ['Radek', 'Ola', 'Marek', 'Asia', 'Anna', 'Magda', 'Marek']
lista.remove("Marek")
print(lista)  # ['Radek', 'Ola', 'Asia', 'Anna', 'Magda', 'Marek']

# usunięcie po indeksie, zwraca usunięty element
# pop()
print(lista.pop(2))  # Asia
zmienna = lista.pop(-1)
print(zmienna)  # Marek
print(lista)  # ['Radek', 'Ola', 'Anna', 'Magda']

print(lista.pop())  # Magda, usunie ostatni element

print(lista)  # ['Radek', 'Ola', 'Anna']

# sprawdzenie indexu dla danego eleemntu, pierwszy napotkany
print(lista.index("Ola"))  # index 1

a = 1
b = 3
a = b
print(f'{a=}, {b=}')  # a=3, b=3

b = 9
print(f'{a=}, {b=}')  # a=3, b=9

lista2 = lista  # kopią adresu, referencji
lista_copy = lista.copy()  # kopia elementów listy do nowej listy

print(lista)  # ['Radek', 'Ola', 'Anna']
print(lista2)  # ['Radek', 'Ola', 'Anna']

lista.clear()  # usunięcie wszystkich elemntów z listy
print(lista)  # []
print(lista2)  # []
print(lista_copy)  # ['Radek', 'Ola', 'Anna']

# id() pokazuje referencje
print(id(lista))  # 2301426388928
print(id(lista2))  # 2301426388928
print(id(lista_copy))  # 2301429354368


