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
print(tekst.count("j", 0, 4)) # występuje 0 razy, z prawej zbiór otwarty, 0123
