# krotka (tupla) - lista tylko do odczytu, niemutowalna
# pozwala efektywniej zarządzać pamięcią
# krotka jednoelementowa, stała, szczególny przypadek zmiennej

tupla_imiona = "Zenek", "Marek", "Radek", "Ania"
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')

# tupla_liczby = (43, 55, 22.34, 11, 200)
tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_imiona))  # <class 'tuple'>

# tupla jednoelementowa
tupla_jeden = 45,  # <class 'tuple'>
print(tupla_jeden)  # (45,)
print(type(tupla_jeden))

# PEP8 przy tworzeniu tupli jednoelementowych zaleca dodanie ()
tupla_jeden = (45,)  # <class 'tuple'>
print(tupla_jeden)  # (45,)
print(type(tupla_jeden))

# tupla jest niemutowalne
# tupla_jeden[0] = 123  # TypeError: 'tuple' object does not support item assignment

# usunięcie całej tupli
del tupla_jeden
# print(tupla_jeden)  # NameError: name 'tupla_jeden' is not defined

# ('Zenek', 'Marek', 'Radek', 'Ania')
print(tupla_imiona.index("Radek"))  # index 2
print(tupla_imiona.count("Radek"))  # występuje 1 raz

print(len(tupla_imiona))  # długość 4

tup = 1, 2
print(type(tup))  # <class 'tuple'>

# a - pierwsza wartosc, b - druga wartość
a = tup[0]
b = tup[1]
print(a, b)  # 1 2

# rozpakowanie tupli
a, b = 1, 2
print(a, b)  # 1 2

a, b = tup
print(a, b)  # 1 2

# ('Zenek', 'Marek', 'Radek', 'Ania')
# name1, name2, name3

# name1, name2, name3 = tupla_imiona # ValueError: too many values to unpack (expected 3, got 4)
name1, name2, *name3 = tupla_imiona  # * worek na pozostałe dane
print(name1, name2, name3)  # Zenek Marek ['Radek', 'Ania']

*name1, name2, name3 = tupla_imiona  # * worek na pozostałe dane
print(name1, name2, name3)  # ['Zenek', 'Marek'] Radek Ania

name1, *name2, name3 = tupla_imiona  # * worek na pozostałe dane
print(name1, name2, name3)  # Zenek ['Marek', 'Radek'] Ania
