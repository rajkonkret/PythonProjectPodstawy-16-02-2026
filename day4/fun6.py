# napisać funkcję obliczającą średnią
def srednia(name=None, *cyfry):  # dowolna ilosć argumentów przekazanych po pozycji
    print(cyfry)

    count = len(cyfry)
    sum_p = sum(cyfry)
    suma = 0

    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = sum_p / count
    except Exception as e:
        print("Błąd:", e)
    else:
        print(f"Średnia dla ucznia: {name} wynosi: {avg}")
        print(f"Średnia dla ucznia: {name} wynosi: {avg_p}")
    finally:
        print("Kolejny uczeń")


srednia()
srednia(1, 2)
srednia(1, 2, 3, 4)
srednia(1, 2, 3, 4, 5, 6)

# ()
# Błąd: division by zero
# Kolejny uczeń
# (1, 2)
# Średnia wynosi: 1.5
# Kolejny uczeń
# (1, 2, 3, 4)
# Średnia wynosi: 2.5
# Kolejny uczeń
# (1, 2, 3, 4, 5, 6)
# Średnia wynosi: 3.5
# Kolejny uczeń

srednia("Radek", 4, 5, 6, 5, 6, 4, 5, 6)
