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
