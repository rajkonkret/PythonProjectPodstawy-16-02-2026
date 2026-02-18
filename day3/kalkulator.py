# napiac aplikację kalkulator
# while True
# menu z opcjami
# wyświetlic ładnie wynik
# obsłużyć wyjątki

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec""")

    odp = input("Podaj wybraną opcję:")

    # if odp == "5":
    #     break

    if odp not in ["1", "2", "3", "4"]:
        break

    try:
        a = int(input("Podaj pierwszą liczbę:"))
        b = int(input("Podaj drugą liczbę:"))

        if odp == "1":
            print(f'Wynik {a} + {b} = {a + b}')
        elif odp == "2":
            print(f'Wynik {a} - {b} = {a - b}')
        elif odp == "3":
            print(f'Wynik {a} * {b} = {a * b}')
        elif odp == "4":
            print(f'Wynik {a} / {b} = {a / b}')
    except ZeroDivisionError:
        print("Nie dziel prze zero!!!")
    except Exception as e:
        print("Bład:", e)
    finally:
        print("Obliczenia wykonane")
