# snake_case - konwencja nazewniczna
import sys

print('Hello World')  # wypisz/wydrukuj
print("Hello World")
# blake8 - formater bardziej restrykcyjny

# ctrl / - komentarz
# print("Hello World!')
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy-16-02-2026\day1\pierwszy.py", line 6
#     print("Hello World!')
#           ^
# SyntaxError: unterminated string literal (detected at line 6)
print("Hello World!!!")
# Hello World
# Hello World
# Hello World!!!

print('"Radek"')  # "Radek"
print('Radek \"Radek\"')  # Radek "Radek"

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, dane tekstowe

print('39' + '30')  # 3930, konkatenacja, łączenie stringów

print(39 + 30)  # 69
print(type(39))  # <class 'int'>, integer, liczby całkowite

# musimy upewnic sie, ze mamy import sys
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

# print("39" + 39) # TypeError: can only concatenate str (not "int") to str

# rzutowanie typów, zamiana
print(int("39"))  # rzutowanie na liczbę cąlkowita, int
print(39 + int("39"))  # 78

print("39" + str(39))  # 3939

# zmienna
# pudełko na dane

# typowanie dynamiczne
name = 90
print(name)  # 90
print(type(name))  # <class 'int'>
# print(name + "Kowalski")

name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>
print(name + "Kowalski")  # RadekKowalski

# podpowiedzi typów
name: str = "Radek"
print(name)
name = 90
print(name)
# Radek
# 90

# mypy - sprawdzanie typów
# pip
# pip install mypy
# PythonProjectPodstawy-16-02-2026>
# cd day1 przejscie do katalogu
# mypy .\pierwszy.py
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy-16-02-2026\day1> mypy .\pierwszy.py
# pierwszy.py:52: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# pierwszy.py:55: error: Unsupported operand types for + ("int" and "str")  [operator]
# pierwszy.py:58: error: Name "name" already defined on line 47  [no-redef]
# Found 3 errors in 1 file (checked 1 source file)

print(4 * "Radek")  # RadekRadekRadekRadek
print(168 * 35)  # 5880
# ctrl d - powielanie linii
print(168 * "35")  # powiela tekst
print(168 * "35")  # powiela tekst
