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


