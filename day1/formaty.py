user = "Tomek"  # str
wiek = 39  # int

wersja = 3.900001
print(type(wersja))  # <class 'float'>, liczby zmiennoprzecinkowe
liczba = 908789876564321123  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek)) # Witaj Tomek, masz teraz 39 lat.
# %s - string
# %d - digit - liczba

# TypeError: %d format: a real number is required, not str
# sprawdza typy danych
# print("Witaj %d, masz teraz %s lat." % (user, wiek)) # Witaj Tomek, masz teraz 39 lat.

# Witaj Tomek, masz teraz 39 lat. fstringiem
print(f"Witaj {user}, masz teraz {wiek} lat.")