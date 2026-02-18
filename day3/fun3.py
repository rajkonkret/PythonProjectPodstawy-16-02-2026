a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne. widoczne tylko wewnątrz funkcji
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    a = 7
    b = 9
    c = a + b
    print(c)


def dodaj4():
    global a  # użyj zmiennej globalnej
    a = 7  # zmienimy wartość globalnej zmiennej a
    b = 90
    print(a + b)


print(f"Wartość a zgóry: {a} (globalna)")  # Wartość a zgóry: 10 (globalna)
dodaj()  # 15
print(f"Wartość a zgóry: {a} (globalna)")  # Wartość a zgóry: 10 (globalna)
dodaj2()  # 20
print(f"Wartość a zgóry: {a} (globalna)")  # Wartość a zgóry: 10 (globalna)
dodaj3()  # 16
# print(c)  # NameError: name 'c' is not defined - zmienna nie jest widoczna poza funkcją
print(f"Wartość a zgóry: {a} (globalna)")  # Wartość a zgóry: 10 (globalna)
dodaj4()  # 97
print(f"Wartość a zgóry: {a} (globalna)")  # Wartość a zgóry: 7 (globalna)
