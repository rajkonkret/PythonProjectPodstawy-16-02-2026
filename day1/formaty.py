user = "Tomek"  # str
wiek = 39  # int

wersja = 3.900001
print(type(wersja))  # <class 'float'>, liczby zmiennoprzecinkowe
liczba = 908789876564321123  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))  # Witaj Tomek, masz teraz 39 lat.
# %s - string
# %d - digit - liczba

# TypeError: %d format: a real number is required, not str
# sprawdza typy danych
# print("Witaj %d, masz teraz %s lat." % (user, wiek)) # Witaj Tomek, masz teraz 39 lat.

# Witaj Tomek, masz teraz 39 lat. fstringiem
print(f"Witaj {user}, masz teraz {wiek} lat.")

# %i - int
# %f - float

print("używamy wersji Pythona %i" % 3)  # używamy wersji Pythona 3
print("używamy wersji Pythona %f" % 3)  # używamy wersji Pythona 3.000000
print("używamy wersji Pythona %.2f" % 3.9)  # używamy wersji Pythona 3.90
print("używamy wersji Pythona %.1f" % 3.9)  # używamy wersji Pythona 3.90
print("używamy wersji Pythona %.0f" % 3.9)  # używamy wersji Pythona 4 - zaokrągla
print("używamy wersji Pythona %.f" % 3.9)  # używamy wersji Pythona 4 - zaokrągla

x = 3.8769
print(x)
y = round(x)
print(y)  # 4

z = round(x, 2)
print(f'{z=}')  # z=3.88
print(type(z))  # <class 'float'>
