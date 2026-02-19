# hermetyzacja
class Car:
    """
    Klasa opisująca samochód w Pythonie
    """

    def __init__(self, model, year):
        """
        Konstroktur - metoda inicjalizująca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year

        # name mangling
        # pole prawie prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def hamuj(self):
        if self.__predkosc >= 10:
            self.__predkosc -= 10
        else:
            self.__predkosc = 0

        self.__zmien_bieg()

    def licznik(self):
        print(f"Prędkość wynosi: {self.__predkosc} km/h")

    def __zmien_bieg(self):
        print("Zmiana biegu")


car = Car("Audi 80", 1992)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# pole prywatne
# print(car.__predkosc)  # 50
car.licznik()  # Prędkość wynosi: 50 km/h
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()  # Prędkość wynosi: 0 km/h
car.hamuj()
car.licznik()  # Prędkość wynosi: -10 km/h -> Prędkość wynosi: 0 km/h

# car.__predkosc = 0
# car.licznik()
# Prędkość wynosi: 50 km/h
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkość wynosi: 0 km/h
# Zmiana biegu
# Prędkość wynosi: 0 km/h