# funkcja lambda
# skrócony zapis funkcji
# lambda zwraca wynik (return)
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(10, 8))  # 2

odejmij2 = lambda a, b: a - b  # domyślnie ma return
print(odejmij2(10, 2))  # 8

# przemieni oblicz_vat na lambde
