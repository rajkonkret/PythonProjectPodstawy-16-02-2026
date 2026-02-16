tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
""" Return a copy of the string converted to uppercase. """
# nie zmienia oryginału
tekst.upper()
print(tekst)
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie

print(tekst.lower())  # "witaj świecie"
print(tekst.capitalize())  # "Witaj świecie"

# Witaj Świecie
# 0123456789... numerowanie od 0
print(tekst[0])  # W
print(tekst[2])  # t, indeks numer 2, pozycja 3

print(tekst.index("Ś"))  # indeks numer 6, pierwszy napotkany

print(tekst.count("i"))  # wystepuje 3 x
print(tekst.count("w"))  # wystepuje 1 raz

print(tekst.index("i"))  # indeks 1, pierwszy napotkany

print(tekst.lower().count("w"))  # wystepuje 2 razy

# Witaj Świecie
# 0123456789... numerowanie od 0
print(tekst.count("j", 0, 4))  # występuje 0 razy, z prawej zbiór otwarty, 0123

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie biaych znaków, wiodących i kończących spacji
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # <class 'bytes'>, typ bajtowy
# b - typ bajtowy
# \xc5\x9a kod znaku Ś w systemie szesnastkowym
# \x - dane w systemie szesnatkowym

print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
print(len(imie))  # długość tekstu 5

# f - string, wstrzykiwanie zmiennych do tekstu, {}
tekst_format = f"\tMam na imię {imie}\n i lubię Pythona.\b"
print(tekst_format)
# "   Mam na imię Radek
#  i lubię Pythona"
# \t - tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s!"  # %s - string
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format("Radek"))  # Witaj Radek!
print(f"Witaj {imie}!")  # Witaj Radek!

print("Witaj", imie)  # Witaj Radek

print("""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"

# komentarz traktowany jako dokumentacja (docstring)
"""Komentarz
    wielolinijkowy"""
