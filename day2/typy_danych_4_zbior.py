# zbior (set) przechowują unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # rzutowanie na zbiór set()
print(zbior)  # {33, 66, 777, 11, 44, 22, 55} - usunięte duplikaty, zmieniona kolejność
print(type(zbior))  # <class 'set'>

lista_sort = sorted(zbior)
print(lista_sort)  # [11, 22, 33, 44, 55, 66, 777]

lista_sort = list(zbior)
lista_sort.sort()
print(lista_sort)  # [11, 22, 33, 44, 55, 66, 777]

# pusty zbiór
zb2 = set()  # tylko i wyłacznie słówkiem set()
print(zb2)  # set() - pusty zbior

# dodanie eleemntu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(33)
zbior.add(33)
zbior.add(24)
zbior.add(24)
zbior.add(25)
print(zbior) # {33, 66, 777, 11, 44, 18, 22, 55, 24, 25}
