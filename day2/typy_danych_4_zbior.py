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

print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24, 25}

# usuniecie eleemntu ze zbioru
zbior.remove(55)  # wartość elementu
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24, 25}

# ctrl f - szukanie w pliku
# ctrl shift f - wyszukiwanie w projekcie

# pop()
print(zbior.pop())  # 33, usuniecie pierwszego elementu

zmienna = zbior.pop()
print(f"Zmienna: {zmienna}")  # Zmienna: 66
print('Zmienna:', zmienna)  # Zmienna: 66

zbior_copy = zbior.copy()
print(zbior_copy)
# id
print(id(zbior))  # 1848029801024
print(id(zbior_copy))  # 1848034961984

zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}
print(type(zbior_2))  # <class 'set'>

# suma zbiorów, zwraca nowy zbiór
print(zbior | zbior_2)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}

# częśc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica zbiorów
print(zbior - zbior_2)  # {24, 777, 22, 25}
print(zbior.difference(zbior_2))  # {24, 777, 22, 25}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# łączy zbiory, zmienia bazowy!!!
zbior.update(zbior_2)
print(zbior)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}


