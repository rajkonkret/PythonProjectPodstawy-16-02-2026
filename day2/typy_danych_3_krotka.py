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

