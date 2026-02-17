# słownik - para klucz:wartosc
# {"user" : "Radek"}
# odpowiednik jsona
# klucze nie mogą sie powtarzać

# pusty słownik
dictionary = {}
print(dictionary)  # {} - pusty słownik
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodanie lementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}

# dodać klucz wiek
dictionary['wiek'] = 50
print(dictionary)  # {'imie': 'Radek', 'wiek': 50}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_keys(['imie', 'wiek'])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 50)])

# nadpisanie wartości
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 50}

# wypisanie wartości dla klucza
print(dictionary['imie'])  # Tomek

dictionary['imie'] = ["Radek", "Tomek", "Magda"]
print(dictionary)  # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50}

# wypisac Tomka
print(dictionary['imie'])  # ['Radek', 'Tomek', 'Magda']
print(dictionary['imie'][1])  # Tomek

print(dictionary['imie'][0].lower())  # radek
print(dictionary['imie'][::1])  # ['Radek', 'Tomek', 'Magda']

dictionary = {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50}
print(dictionary)  # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50}

# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary['Imie'.lower()])  # ['Radek', 'Tomek', 'Magda']

print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

name1 = "GROSS"
name2 = "groẞ"

print(name1.lower() == name2.lower())  # False

""" Return a version of the string suitable for caseless comparisons. """
print(name1.casefold() == name2.casefold())  # True

dictionary.update({"data": "12-12-2055"})
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50, 'data': '12-12-2055'}

# [('imie', 'Radek'), ('wiek', 50)] - lista krotek
dict_small = {'x': 2}
dict_small.update([("x", 3), ("z", 6)])
print(dict_small)  # {'x': 3, 'z': 6}

# input() - pozwala wprowadzić dane do komputera np.:  z klawiatury

# # input zwraca str
# tekst = input("Podaj imie:")
# print(tekst)
# print(type(tekst))
# # Podaj imie:Radek
# # Radek
#
# # Podaj imie:123
# # 123
# # <class 'str'>

#  napisac aplikacje kalkulator
# a = int(input("Podaj pierwsza liczbę:"))
# b = input("Podaj drugą liczbę:")
# print(a + float(b))
# Podaj pierwsza liczbę:1
# Podaj drugą liczbę:2
# 3.0

# napisac aplikację słownik pol-ang
pol_ang = {'pies': "dog", "kot": 'cat', "dach": "roof"}
print("Znam takie słówka:", pol_ang.keys())
odp = input("Podaj słówko do przetłumaczenia:")
print(f"Prawidłowa odpowiedź dla: {odp} to: {pol_ang.get(odp.strip().casefold(), "nie ma")}")
# Znam takie słówka: dict_keys(['pies', 'kot', 'dach'])
# Podaj słówko do przetłumaczenia: Pies
# Prawidłowa odpowiedź dla:  Pies to: dog

# \N{name} - Znak Unicode o podanej nazwie
print("\N{LATIN SMALL LETTER SHARP S}")  # ß
