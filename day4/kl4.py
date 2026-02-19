from abc import ABC, abstractmethod


# klasa abstrakcyjna - kalsa, która zawiera metode abstrakcyjną
class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca - konstruktor
        :param gatunek:
        :param szybkosc:
        """

        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością:", self.szybkosc, "km/h")

    # metoda abstrakcyjna
    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Klasa Kura, dziedziczy po klasie Ptak
    """

    # zmieniamy konstruktor w klasie dziedziczącej
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # musimy wywołać super()

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("ko ko ko ko ko")


# klasa Orzel -> Ptak
class Orzel(Ptak):
    """
    Klasa Orzeł dziedziczy po kalsie Ptak
    """

    def wydaj_odglos(self):
        print("Kier kir kier ki kir")


class Sowa(Ptak):
    """
    Klasa Sowa dziedziczy po klasie Ptak
    """


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# klasa abstrakcyjna
# nie można tworzyć obiektów tej klasy
# or1 = Ptak("Orzeł", 50)
# print(or1)  # <__main__.Ptak object at 0x105ffa270>
# or1.latam()  # Tu Orzeł Lecę z szybkością: 50 km/h
# or1.wydaj_odglos()
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością: 0 km/h
# kur1.wydaj_odglos()

kur2 = Kura("Kura zielononóżka")
kur2.latam()  # Tu Kura zielononóżka Ja nie latam
kur2.wydaj_odglos()

or2 = Orzel("Orzeł Bielik", 55)
or2.latam()  # Tu Orzeł Bielik Lecę z szybkością: 55 km/h
or2.wydaj_odglos()

# Tu Kura zielononóżka Ja nie latam
# ko ko ko ko ko
# Tu Orzeł Bielik Lecę z szybkością: 55 km/h
# Kier kir kier ki kir

# brak metody 'wydaj_odglos'w kalsie Sowa - nie można tworzyc obiektu klasy Sowe
# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sowa = Sowa("Sowa", 20)

# polimorfizm - obiekty różnych klas, mogą byctraktowane jak obiekty wspolnej nadrzędnej klasy
# wiąże je metoda  abstrakcyjna
lista = [or2, kur2]  # obiekty róznych klas

for i in lista:
    i.wydaj_odglos()
    print(i.__class__.__name__)
# Kier kir kier ki kir
# Orzel
# ko ko ko ko ko
# Kura
