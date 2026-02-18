# funkcja - wydzielony fragment kodu, można wykonać w dowolnym momencie
# funkcja musi być najpierw zadeklarowy
# żeby uruchomić funkcję trzeba ją wywołać

a = 6
b = 8


# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # argumenty obowiązkowe
    print(a + b)


# ominięcie problemu przeciążania funkcji liczbą argumentów
def odejmij(a, b, c=0):  # c=0 argument o wartości domyślnej
    print(a - b - c)


# wywołanie funkcji
dodaj()  # 14

# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(6, 90)  # 96

odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4
