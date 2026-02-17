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

odp = False
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
