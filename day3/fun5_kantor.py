# stworzyc funkcję kantor -> def
# ma mieć dwie funkcje wewnętrzne: eur, usd -> 2 x def
# w zależności od parametru zwroci jedną z funkcji -> if -> return
# przekazenie kwoty do funkcji usd i eur

def kantor(waluta):
    print("Otwieram kantor")

    def usd(kwota=0):
        print(f"Wymieniam: {kwota} usd na: {kwota * 3.57} pln")

    def eur(kwota=0):
        print(f"Wymieniam: {kwota} usd na: {kwota * 4.20} pln")

    if waluta == "eur":
        return eur
    else:
        return usd


kantor_usd = kantor("usd")
kantor_eur = kantor("eur")

kantor_usd()
kantor_usd()
kantor_usd()
kantor_usd()

kantor_eur()
kantor_eur()
kantor_eur()
kantor_eur()
kantor_eur()

kantor_eur(500)
kantor_usd(345)
# Otwieram kantor
# Wymieniam: 0 usd na: 0.0
# Wymieniam: 0 usd na: 0.0
# Wymieniam: 0 usd na: 0.0
# Wymieniam: 0 usd na: 0.0
# Wymieniam: 0 usd na: 0.0
# Wymieniam: 0 usd na: 0.0
# Wymieniam: 0 usd na: 0.0
# Wymieniam: 0 usd na: 0.0
# Wymieniam: 0 usd na: 0.0
# Wymieniam: 500 usd na: 2100.0
# Wymieniam: 345 usd na: 1231.6499999999999
