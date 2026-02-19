class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie  # w obiekcie stwórz pole imie i nadaj mu wartość z imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    # wypisz_wiek(), wypisz_wzrost()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    # self - obiekt
    def powitanie(self):
        print(f"Nazywam się: {self.imie}")
        # print(f"Nazywam się: {cz1.imie}")

    def ruszaj(self):

        if self.plec == "m":
            print("Ruszył-em w drogę")
        else:
            print("Ruszył-am w drogę")


# cz1 = Human() # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Radek", 45, 189, "m")
print(cz1.imie)
print(cz1.wzrost)
print(cz1.wiek)
print(cz1.plec)

cz1.powitanie()
cz1.ruszaj()
# Nazywam się: Radek
# Ruszył-em w drogę

cz1.wypisz_wiek()  # Mam 45 lat.
cz1.wypisz_wzrost()  # Mam 189 cm wzrostu.
