# działania z plikami
# context manager
# with - context manager

# filehandler

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================

# w - tworzy nowy plik
# gdy plik istnieje zostanie nadpisany (skasowany) !!!
with open("test.log", "w", encoding='utf-8') as f:
    f.write('Powitanie\n')
    f.write('Jeszcze jedno\n')

# f.write("") # ValueError: I/O operation on closed file. plik został zamknięty przez context manager

# x - tworzy nowy plik
# x - jesli plik istnieje dostaniemy błąd
# # FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x",  encoding='utf-8') as f:
#     f.write('Powitanie\n')
#     f.write('Jeszcze jedno\n')

with open("test.log", "w",  encoding='utf-8') as f:
    f.write('PArametr 1\n')
    f.write('PArametr 2\n')
    f.write('PArametr 3\n')
    f.write('PArametr 4\n')

# \n nowa linia
# a - dodanie na końcu pliku
with open("test.log", "a",  encoding='utf-8') as f:
    f.write('Dodane\n')
    f.write('Dodane\n')
    f.write('Dodane jescze jedno\n')
    f.write('Dodśąźńane jescze jedno\n')

with open("test.log", "r",  encoding='utf-8') as file:
    lines = file.read()

print(lines)
# PArametr 1
# PArametr 2
# PArametr 3
# PArametr 4
# Dodane
# Dodane
# Dodane jescze jedno
