# klasa - przepis, szablon
# cechy (zmienne)
# metody - funkcja w klasie
# obiekt - instancja klasy
# klasa musi zostac najpierw zadeklarowna
# tworzennie obiektu uruchamia funkcję inicjalizującą (konstroktur) __init__
# paradygmaty -> hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase, UpperCamelCase
class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    imie = ""
    wiek = None
    plec = "k"


# tworzenie obiektu
cz1 = Human()

print(Human.__doc__)
# Klasa Human opisująca człowieka w Pythonie

print(print.__doc__)
# pydoc - narzęzie do dokumentacji

# cd day4 - wejscie do katalogu day4
# pydoc - b - serwer dokumentacji
# pydoc -w kl1 - tworzy plik html z dokumentacją

cz1 = Human()
print(cz1)  # <__main__.Human object at 0x109e27750>

print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
#
# None
# k

cz1.imie = "Radek"
cz1.wiek = 50
cz1.plec = "m"

print(cz1.imie)  # Radek
print(cz1.wiek)  # 50
print(cz1.plec)  # m

# drugi obiekt innej plci
cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 34

print(cz2.imie)  # Anna
print(cz2.wiek)  # 34
print(cz2.plec)  # k
