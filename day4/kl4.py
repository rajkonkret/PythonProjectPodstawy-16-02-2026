class Ptak:
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


class Kura(Ptak):
    """
    Klasa Kura, dziedziczy po klasie Ptak
    """

    # zmieniamy konstruktor w klasie dziedziczącej
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # musimy wywołać super()

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")


# klasa Orzel -> Ptak
class Orzel(Ptak):
    """
    Klasa Orzeł dziedziczy po kalsie Ptak
    """


or1 = Ptak("Orzeł", 50)
print(or1)  # <__main__.Ptak object at 0x105ffa270>
or1.latam()  # Tu Orzeł Lecę z szybkością: 50 km/h

kur1 = Ptak("Kura", 0)
kur1.latam()  # Tu Kura Lecę z szybkością: 0 km/h

kur2 = Kura("Kura zielononóżka")
kur2.latam()  # Tu Kura zielononóżka Ja nie latam

or2 = Orzel("Orzeł Bielik", 55)
or2.latam()  # Tu Orzeł Bielik Lecę z szybkością: 55 km/h
