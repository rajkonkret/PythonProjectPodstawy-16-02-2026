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


# wywołanie funkcji
dodaj()  # 14

# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(6, 90)  # 96
