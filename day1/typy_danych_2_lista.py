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
