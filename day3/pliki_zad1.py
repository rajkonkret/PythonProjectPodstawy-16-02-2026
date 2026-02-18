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
with open("test.log", "w") as f:
    f.write('Powitanie\n')
    f.write('Jeszcze jedno\n')

# f.write("") # ValueError: I/O operation on closed file. plik został zamknięty przez context manager