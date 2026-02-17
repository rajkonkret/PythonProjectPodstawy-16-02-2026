# warunki
# instrukcje warunkowe
# instrukcje sterowania przpływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu
# wyrażenie w warunku musi zwrócić typ bool

odp = True

if odp: print("Test")  # Test

if odp:
    print("Test")  # Test

# debugger - narzedzie do wykonywania kodu krok po kroku, ułatwia wyszukiwanie błedów
# pułapka - mmiejsce gdzi ema się zatrzymać debugger

# odp = False
if odp:  # blok programu wykonywany gdy warunek True
    print("Brawo")
    # print("Brawo") IndentationError: unexpected indent
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo

print("Dalsza część programu")

odp = "Radek"
if odp:
    print("Dane zostały wczytane")
# Dane zostały wczytane

if odp == "Radek":  # porównanie
    print("Jesteś Radek")  # Jesteś Radek

odp = 0  # bool(0) -> False
if odp:
    print("Działa")
else:  # w innym przypadku, wartość domyślna
    print("Zero -> False")
# Zero -> False

a = "Radek"
# jeśli długość tekstu wieksza niż 3 to ma wypisac:
# Długośc wynosi: dl, więcej niż 3

if len(a) > 3:
    print(f"Długość wynosi: {len(a)}, więcej niż 3")
# Długość wynosi: 5, więcej niż 3

n = len(a)
if n > 3:
    print(f"Długość wynosi: {n}, więcej niż 3")
# Długość wynosi: 5, więcej niż 3

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f"Długość wynosi: {n}, więcej niż 3")

# ctrl / - komentarz
# podatek = 0
# zarobki = int(input('Podaj zarobki:'))
#
# if zarobki < 10_000:
#     podatek = 0
# # elif  10000 <= zarobki < 40000:
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:  # od 100_000
#     podatek = 0.9
#
# print(f"podatek wynosi: {zarobki * podatek} pln.")
# dodać podatek 20%, dla zarobków od 10000 do 39999

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

# operator warunkowy
rabat = 25 if sum_zam > 100 else 0
print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

# napisac test z ...
# trzy patania
# punktacja

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

# punkty = 0
# odp = input("Podaj rok Chrztu Polski: ")
# if odp.strip().casefold() == '966':
#     print("Odpowiedż prawidłowa")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Doucz się!")
#
# odp = input("Podaj stolicę Polski: ")
# if odp.strip().casefold() == 'Warszawa'.casefold():
#     print("Odpowiedż prawidłowa")
#     punkty += 1
# else:
#     print("Doucz się!")
#
# odp = input("Czy Ala ma kota? : ")
# if odp.strip().casefold() == 'tak':
#     print("Odpowiedż prawidłowa")
#     punkty += 1
# else:
#     print("Doucz się!")
#
# print(f"Zdobyłeś: {punkty} pkt.")
# Podaj rok Chrztu Polski: 966
# Odpowiedż prawidłowa
# Podaj stolicę Polski: Warszawa
# Odpowiedż prawidłowa
# Zdobyłeś: 2 pkt.


# zasymulujemy system zbierania logów
# zmienna: typ sytemu -> console, email, inny
# console: "Stało się coś strasznego"
# email: "System email"
# jeśli system jest email:
# dodąc do listy błedów tłumaczenie błędu
# poziomy błędów: error, medium, inny
# error -> Krytyczny

lista_b = []
alert_system = "email"
error_level = "error"

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error_level == "error":
        lista_b.append("Krytyczny")
    elif error_level == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("inne")
else:
    print("Inny system")

print(lista_b)
# System email
# ['Krytyczny']
